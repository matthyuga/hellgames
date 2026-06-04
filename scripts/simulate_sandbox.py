from __future__ import annotations

import argparse
import json
import random
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTOTYPE_PATH = ROOT / "data" / "prototype_island_4.json"
RUNTIME_PATH = ROOT / "data" / "prototype_runtime_4.json"
CRAFTING_PROFILES_PATH = ROOT / "data" / "actor_crafting_profiles.json"
DEFAULT_OUTPUT = ROOT / "data" / "runs" / "prototype_island_4_sandbox_log.md"

PARTICIPANTS = ["rex", "renzo_manos_frias", "silas_crow"]
LOCALS = ["sira", "verek"]
CREATURES = ["gaviotas_hueso", "larvas_raiz", "sombras_monolito"]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_optional_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_json(path)


def clamp(value: int, min_value: int = 0, max_value: int = 100) -> int:
    return max(min_value, min(max_value, value))


def phase_for_hour(hour: int) -> str:
    if 6 <= hour <= 11:
        return "manana"
    if 12 <= hour <= 17:
        return "tarde"
    if 18 <= hour <= 23:
        return "noche"
    return "madrugada"


def is_night(phase: str) -> bool:
    return phase in {"noche", "madrugada"}


def apply_hourly_decay(actor: dict, phase: str) -> None:
    if actor.get("type") in {"criatura", "guardian", "jefe"} or actor.get("hp", 1) <= 0:
        return
    actor["hunger"] = clamp(actor["hunger"] + 1)
    actor["thirst"] = clamp(actor["thirst"] + 1)
    actor["stamina"] = clamp(actor["stamina"] - 1)
    if is_night(phase):
        actor["fear"] = clamp(actor["fear"] + 2)
    if actor["hunger"] >= 95 or actor["thirst"] >= 95:
        actor["hp"] = clamp(actor["hp"] - 1)


def consume_if_needed(actor: dict) -> list[str]:
    lines: list[str] = []
    inventory = actor.get("inventory", [])
    if actor.get("hp", 0) <= 0:
        return lines
    if actor.get("thirst", 0) >= 72 and "agua_limpia" in inventory:
        inventory.remove("agua_limpia")
        actor["thirst"] = clamp(actor["thirst"] - 25)
        lines.append(f"{actor['name']} bebe agua limpia.")
    if actor.get("hunger", 0) >= 76:
        for item_id, value in (("racion_basica", 25), ("lata_pequena", 18)):
            if item_id in inventory:
                inventory.remove(item_id)
                actor["hunger"] = clamp(actor["hunger"] - value)
                lines.append(f"{actor['name']} come una provision.")
                break
    return lines


def active_cells(prototype: dict) -> dict[int, dict]:
    return {cell["id"]: cell for cell in prototype["active_cells"]}


def random_spawn_participants(actors: dict[str, dict], runtime: dict, rng: random.Random) -> list[str]:
    lines = []
    spawn = runtime["sandbox_rules"]["participant_spawn"]
    for actor_id in PARTICIPANTS:
        actor = actors[actor_id]
        cell = rng.choice(spawn["allowed_cells"])
        point = rng.choice(spawn["points"][str(cell)])
        actor["cell"] = cell
        actor["micro"] = point["micro"]
        actor["poi"] = point["poi"]
        actor["hidden"] = actor_id == "silas_crow"
        lines.append(f"{actor['name']} cae en la casilla {cell}, zona {point['poi']} ({point['micro']}).")
    return lines


def apply_local_routine(actor: dict, routine: dict, phase: str) -> str:
    step = routine[phase]
    actor["cell"] = step["cell"]
    actor["micro"] = step["micro"]
    actor["poi"] = step["poi"]
    actor["hidden"] = phase == "madrugada" or actor["id"] == "sira"
    return f"{actor['name']} sigue su rutina: {step['action']} en casilla {step['cell']} ({step['micro']})."


def find_loot(actor: dict, runtime: dict, rng: random.Random) -> str:
    loot = runtime["cell_loot"].get(str(actor["cell"]), {})
    pool = list(loot.get("common", []))
    if rng.random() < 0.18:
        pool.extend(loot.get("rare", []))
    if not pool:
        return f"{actor['name']} busca recursos, pero solo encuentra barro y silencio."
    item = rng.choice(pool)
    actor.setdefault("inventory", []).append(item)
    if item == "agua_limpia":
        actor["thirst"] = clamp(actor["thirst"] - 10)
    if item == "racion_basica":
        actor["hunger"] = clamp(actor["hunger"] - 10)
    return f"{actor['name']} encuentra {item.replace('_', ' ')}."


def move_to_neighbor(actor: dict, cells: dict[int, dict], runtime: dict, rng: random.Random) -> str:
    current = cells[actor["cell"]]
    target = rng.choice(current["neighbors"])
    target_name = cells[target]["name"]
    spawn_points = runtime["sandbox_rules"]["participant_spawn"]["points"].get(str(target))
    if spawn_points:
        point = rng.choice(spawn_points)
    elif target == 7:
        point = rng.choice([
            {"micro": "E6", "poi": "trampas"},
            {"micro": "G7", "poi": "patio"},
            {"micro": "H4", "poi": "puerta"},
        ])
    else:
        point = {"micro": "G7", "poi": "zona_abierta"}
    actor["cell"] = target
    actor["micro"] = point["micro"]
    actor["poi"] = point["poi"]
    actor["hidden"] = False
    return f"{actor['name']} sale de {current['name']} y se desplaza a {target_name}, {point['poi']} ({point['micro']})."


def rest_or_hide(actor: dict) -> str:
    actor["stamina"] = clamp(actor["stamina"] + 18)
    actor["fear"] = clamp(actor["fear"] - 8)
    actor["hidden"] = True
    return f"{actor['name']} se oculta y recupera algo de energia."


def try_recipe_action(actor: dict, memories: dict, crafting_profiles: dict[str, dict]) -> str | None:
    profile = crafting_profiles.get(actor["id"], {})
    known = set(profile.get("known_recipes", []))
    interests = set(profile.get("interests", []))
    inventory = actor.setdefault("inventory", [])

    if actor["id"] == "rex" and "venda_improvisada" in known:
        if "aguja" in inventory and "retazo_tela" in inventory and not memories.get("rex_fabrico_venda"):
            inventory.remove("retazo_tela")
            inventory.append("venda_limpia")
            actor["stamina"] = clamp(actor["stamina"] - 4)
            memories["rex_fabrico_venda"] = True
            return "Rex improvisa una venda con aguja y retazo de tela; no es elegante, pero puede salvar una escena."

    if actor["id"] == "renzo_manos_frias" and "reparar_radio_faro" in known:
        if actor["cell"] == 1 and not memories.get("radio_reparada"):
            memories["radio_reparada"] = actor["id"]
            actor["stamina"] = clamp(actor["stamina"] - 8)
            return "Renzo usa sus conocimientos tecnicos para reparar la radio del faro y capta una advertencia incompleta sobre las ruinas."

    if actor["id"] == "silas_crow" and "montar_cuerda_tensada" in known:
        if actor["cell"] == 7 and "cuerda_negra" in inventory and not memories.get("silas_monto_trampa_ruinas"):
            memories["silas_monto_trampa_ruinas"] = True
            actor["stamina"] = clamp(actor["stamina"] - 6)
            return "Silas tensa una cuerda negra entre piedras rotas; cualquiera que corra por las ruinas pagara por no mirar al suelo."

    if actor["id"] == "sira" and "mapa_anotado" in known:
        if "lore" in interests and not memories.get("sira_marco_ruta_segura"):
            memories["sira_marco_ruta_segura"] = True
            return "Sira anota una ruta segura entre marcas antiguas, aunque no decide todavia con quien compartirla."

    return None


def choose_participant_action(
    actor: dict,
    cells: dict[int, dict],
    runtime: dict,
    memories: dict,
    phase: str,
    rng: random.Random,
    crafting_profiles: dict[str, dict],
) -> str:
    if actor["hp"] <= 0:
        return f"{actor['name']} ya no puede actuar."

    if actor["thirst"] >= 70 or actor["hunger"] >= 72:
        return find_loot(actor, runtime, rng)
    if actor["stamina"] <= 25 or actor["fear"] >= 78:
        return rest_or_hide(actor)

    recipe_action = try_recipe_action(actor, memories, crafting_profiles)
    if recipe_action:
        return recipe_action

    if actor["id"] == "silas_crow" and actor["cell"] in {6, 7} and rng.random() < 0.42:
        if actor["cell"] == 6:
            memories["silas_rumbo_ruinas"] = True
            return move_to_neighbor(actor, cells, runtime, rng)
        if not memories.get("reliquia_robada") and rng.random() < 0.5:
            actor.setdefault("inventory", []).append("reliquia_antigua")
            memories["reliquia_robada"] = actor["id"]
            memories["ruinas_perturbadas"] = True
            return "Silas roba una reliquia antigua y deja una marca negra en el polvo."

    if actor["id"] == "rex" and rng.random() < 0.35:
        actor["hidden"] = False
        actor["fear"] = clamp(actor["fear"] - 4)
        return "Rex intenta hacerse visible y buscar una alianza antes de que oscurezca."

    if rng.random() < 0.45:
        return find_loot(actor, runtime, rng)
    return move_to_neighbor(actor, cells, runtime, rng)


def interaction_phase(actors: dict[str, dict], memories: dict, rng: random.Random) -> list[str]:
    lines: list[str] = []
    alive_people = [actor for actor in actors.values() if actor.get("type") in {"participante", "lugareno"} and actor.get("hp", 0) > 0]
    by_cell: dict[int, list[dict]] = {}
    for actor in alive_people:
        by_cell.setdefault(actor["cell"], []).append(actor)

    for cell, present in sorted(by_cell.items()):
        if len(present) < 2:
            continue
        names = ", ".join(actor["name"] for actor in present)
        if cell == 2 and any(actor["id"] == "verek" for actor in present):
            partner = next((actor for actor in present if actor["id"] in PARTICIPANTS), None)
            if partner:
                lines.append(handle_trade(partner, actors["verek"], memories))
                continue
        if cell == 1 and any(actor["id"] == "sira" for actor in present):
            partner = next((actor for actor in present if actor["id"] in PARTICIPANTS), None)
            if partner:
                memories[f"{partner['id']}_recibio_advertencia_sira"] = True
                partner["fear"] = clamp(partner["fear"] - 3)
                lines.append(f"Sira advierte a {partner['name']}: sobrevivir no siempre significa abrir la siguiente puerta.")
                continue
        if rng.random() < 0.35:
            lines.append(f"{names} coinciden en la casilla {cell}; nadie ataca, pero todos recuerdan el encuentro.")
    return lines


def handle_trade(partner: dict, verek: dict, memories: dict) -> str:
    food = next((item for item in partner.get("inventory", []) if item in {"lata_pequena", "racion_basica"}), None)
    if food:
        partner["inventory"].remove(food)
        verek.setdefault("inventory", []).append(food)
        memories[f"{partner['id']}_trato_con_verek"] = True
        partner["fear"] = clamp(partner["fear"] - 4)
        return f"{partner['name']} entrega {food.replace('_', ' ')} a Verek a cambio de un rumor: 'las ruinas cobran deudas, no monedas'."
    partner["morale"] = clamp(partner["morale"] - 3)
    return f"Verek tantea a {partner['name']}, pero no acepta un trato sin comida ni ventaja clara."


def creature_events(actors: dict[str, dict], runtime: dict, memories: dict, phase: str, rng: random.Random) -> list[str]:
    chances = runtime["sandbox_rules"]["event_chances"]
    chance = chances["creature_minor_night"] if is_night(phase) else chances["creature_minor_day"]
    if rng.random() > chance:
        return []

    lines: list[str] = []
    event = rng.choice(CREATURES)
    creature = actors[event]
    creature["hidden"] = False
    if event == "gaviotas_hueso":
        target = random_alive_participant_in_cell(actors, 1, rng)
        if target:
            target["fear"] = clamp(target["fear"] + 8)
            lines.append(f"Las gaviotas de hueso chillan sobre {target['name']} y delatan su posicion cerca del faro.")
        else:
            lines.append("Las gaviotas de hueso rodean el faro, buscando comida visible.")
    elif event == "larvas_raiz":
        target = random_alive_participant_in_cell(actors, 2, rng)
        if target:
            target["hp"] = clamp(target["hp"] - 4)
            target["fear"] = clamp(target["fear"] + 6)
            lines.append(f"Larvas de raiz muerden a {target['name']} bajo el campamento.")
        else:
            lines.append("Las larvas de raiz remueven las tiendas vacias del campamento.")
    else:
        target = random_alive_participant_in_cell(actors, 6, rng)
        if target:
            target["fear"] = clamp(target["fear"] + 14)
            memories["sombra_vista"] = target["id"]
            lines.append(f"Una sombra de monolito imita a {target['name']} hasta quebrarle la calma.")
        else:
            lines.append("Las sombras de monolito cruzan el circulo sin encontrar testigos.")
    return lines


def random_alive_participant_in_cell(actors: dict[str, dict], cell: int, rng: random.Random) -> dict | None:
    options = [actors[actor_id] for actor_id in PARTICIPANTS if actors[actor_id]["cell"] == cell and actors[actor_id]["hp"] > 0]
    return rng.choice(options) if options else None


def guardian_events(actors: dict[str, dict], runtime: dict, memories: dict, phase: str, rng: random.Random) -> list[str]:
    lines: list[str] = []
    if memories.get("reliquia_robada") and actors["centinela_piedra"]["hidden"]:
        actors["centinela_piedra"]["hidden"] = False
        lines.append("El Centinela de Piedra despierta en las ruinas para proteger lo que ya fue tomado.")

    if is_night(phase) and memories.get("radio_reparada") and rng.random() < 0.18:
        actors["custodio_faro"]["hidden"] = False
        lines.append("El Custodio del Faro aparece en la escalera, silencioso, como una regla vieja.")

    if phase == "noche" and memories.get("ruinas_perturbadas"):
        chance = runtime["sandbox_rules"]["event_chances"]["boss_final_night_if_ruins_disturbed"]
        if rng.random() < chance:
            actors["guardian_juramentado"]["hidden"] = False
            memories["guardian_juramentado_despierto"] = True
            lines.append("El Guardian Juramentado despierta: no busca escapar, busca juzgar la supervivencia de los vivos.")
    return lines


def build_actors(prototype: dict, runtime: dict) -> dict[str, dict]:
    base_actors = {actor["id"]: actor for actor in prototype["actors"]}
    return deepcopy({entry["id"]: {**base_actors.get(entry["id"], {}), **entry} for entry in runtime["actor_runtime"]})


def turn_schedule(runtime: dict) -> list[dict]:
    clock = runtime["clock"]
    start_hour = clock["start_hour"]
    total_hours = ((clock["pilot_days"] - 1) * clock["hours_per_day"]) + (clock["hours_per_day"] - start_hour)
    turn_hours = clock["narrative_turn_hours"]
    schedule = []
    for hour_index in range(total_hours):
        if hour_index % turn_hours != 0:
            continue
        absolute_hour = start_hour + hour_index
        island_hour = absolute_hour % 24
        schedule.append(
            {
                "hour_index": hour_index,
                "day": (absolute_hour // 24) + 1,
                "hour": island_hour,
                "phase": phase_for_hour(island_hour),
            }
        )
    return schedule


def format_result_lines(actors: dict[str, dict], memories: dict) -> list[str]:
    lines = ["## Resultado del sandbox"]
    survivors = []
    for actor_id in PARTICIPANTS:
        actor = actors[actor_id]
        alive = actor["hp"] > 0
        if alive:
            survivors.append(actor["name"])
        status = "sobrevive" if alive else "queda fuera de juego"
        lines.append(
            f"- {actor['name']} {status}: casilla {actor['cell']} {actor['micro']}, "
            f"HP {actor['hp']}, hambre {actor['hunger']}, sed {actor['thirst']}, "
            f"energia {actor['stamina']}, miedo {actor['fear']}."
        )

    lines.append("")
    lines.append(f"Supervivientes: {', '.join(survivors) if survivors else 'ninguno'}.")
    lines.append("")
    lines.append("## Memorias globales")
    if memories:
        for key in sorted(memories):
            value = memories[key]
            if isinstance(value, str) and value in actors:
                value = actors[value]["name"]
            lines.append(f"- `{key}`: {value}")
    else:
        lines.append("- Sin memorias globales registradas.")
    return lines


def simulate_live(seed: int, completed_turns: int | None = None) -> dict:
    prototype = load_json(PROTOTYPE_PATH)
    runtime = load_json(RUNTIME_PATH)
    crafting_profiles_data = load_optional_json(CRAFTING_PROFILES_PATH)
    crafting_profiles = {entry["id"]: entry for entry in crafting_profiles_data.get("actors", [])}
    rng = random.Random(seed)
    actors = build_actors(prototype, runtime)
    cells = active_cells(prototype)
    memories: dict[str, object] = {}

    clock = runtime["clock"]
    schedule = turn_schedule(runtime)
    target_turns = len(schedule) if completed_turns is None else max(0, min(completed_turns, len(schedule)))

    intro_lines = [
        "# Bitacora sandbox - Prototipo isla 4 casillas",
        "",
        f"Seed: `{seed}`",
        "Objetivo: sobrevivir 3 dias sin casilla de escape.",
        f"Escala: 1 minuto real = {clock['real_minute_equals_island_hours']} hora isla",
        "",
        "## Inicio",
    ]
    intro_events = random_spawn_participants(actors, runtime, rng)
    intro_lines.extend(f"- {line}" for line in intro_events)
    intro_lines.append("")

    routines = runtime["sandbox_rules"]["local_routines"]
    schedule_by_hour = {entry["hour_index"]: entry for entry in schedule}
    total_hours = schedule[-1]["hour_index"] + 1 if schedule else 0
    turn_logs: list[dict] = []
    completed = 0

    for hour_index in range(total_hours):
        meta = schedule_by_hour.get(hour_index)
        phase = meta["phase"] if meta else phase_for_hour((clock["start_hour"] + hour_index) % 24)

        for actor in actors.values():
            apply_hourly_decay(actor, phase)

        if meta is None:
            continue
        if completed >= target_turns:
            break

        turn: list[str] = []
        for actor_id in PARTICIPANTS + LOCALS:
            turn.extend(consume_if_needed(actors[actor_id]))

        for local_id in LOCALS:
            turn.append(apply_local_routine(actors[local_id], routines[local_id], meta["phase"]))
            recipe_action = try_recipe_action(actors[local_id], memories, crafting_profiles)
            if recipe_action:
                turn.append(recipe_action)

        for actor_id in PARTICIPANTS:
            turn.append(choose_participant_action(actors[actor_id], cells, runtime, memories, meta["phase"], rng, crafting_profiles))

        turn.extend(interaction_phase(actors, memories, rng))
        turn.extend(creature_events(actors, runtime, memories, meta["phase"], rng))
        turn.extend(guardian_events(actors, runtime, memories, meta["phase"], rng))

        if not turn:
            turn.append("La isla avanza sin incidentes visibles.")

        completed += 1
        turn_logs.append(
            {
                "index": completed,
                "title": f"Dia {meta['day']} - {meta['phase'].title()} ({meta['hour']:02d}:00)",
                "day": meta["day"],
                "hour": meta["hour"],
                "phase": meta["phase"],
                "lines": turn,
            }
        )

    log_lines = intro_lines[:]
    for turn in turn_logs:
        log_lines.append(f"## {turn['title']}")
        log_lines.extend(f"- {line}" for line in turn["lines"])
        log_lines.append("")

    complete = completed >= len(schedule)
    if complete:
        log_lines.extend(format_result_lines(actors, memories))

    return {
        "seed": seed,
        "turn_index": completed,
        "total_turns": len(schedule),
        "complete": complete,
        "intro_events": intro_events,
        "turns": turn_logs,
        "latest_turn": turn_logs[-1] if turn_logs else None,
        "actors": actors,
        "memories": memories,
        "log_text": "\n".join(log_lines).rstrip() + "\n",
    }


def simulate(seed: int) -> str:
    prototype = load_json(PROTOTYPE_PATH)
    runtime = load_json(RUNTIME_PATH)
    crafting_profiles_data = load_optional_json(CRAFTING_PROFILES_PATH)
    crafting_profiles = {entry["id"]: entry for entry in crafting_profiles_data.get("actors", [])}
    rng = random.Random(seed)
    actors = build_actors(prototype, runtime)
    cells = active_cells(prototype)
    memories: dict[str, object] = {}

    clock = runtime["clock"]
    start_hour = clock["start_hour"]
    total_hours = ((clock["pilot_days"] - 1) * clock["hours_per_day"]) + (clock["hours_per_day"] - start_hour)
    turn_hours = clock["narrative_turn_hours"]

    lines = [
        "# Bitacora sandbox - Prototipo isla 4 casillas",
        "",
        f"Seed: `{seed}`",
        "Objetivo: sobrevivir 3 dias sin casilla de escape.",
        f"Escala: 1 minuto real = {clock['real_minute_equals_island_hours']} hora isla",
        "",
        "## Inicio",
    ]
    lines.extend(f"- {line}" for line in random_spawn_participants(actors, runtime, rng))
    lines.append("")

    routines = runtime["sandbox_rules"]["local_routines"]

    for hour_index in range(total_hours):
        absolute_hour = start_hour + hour_index
        day = (absolute_hour // 24) + 1
        island_hour = absolute_hour % 24
        phase = phase_for_hour(island_hour)

        for actor in actors.values():
            apply_hourly_decay(actor, phase)

        if hour_index % turn_hours != 0:
            continue

        lines.append(f"## Dia {day} - {phase.title()} ({island_hour:02d}:00)")
        turn: list[str] = []

        for actor_id in PARTICIPANTS + LOCALS:
            turn.extend(consume_if_needed(actors[actor_id]))

        for local_id in LOCALS:
            turn.append(apply_local_routine(actors[local_id], routines[local_id], phase))

        for actor_id in PARTICIPANTS:
            turn.append(choose_participant_action(actors[actor_id], cells, runtime, memories, phase, rng, crafting_profiles))

        turn.extend(interaction_phase(actors, memories, rng))
        turn.extend(creature_events(actors, runtime, memories, phase, rng))
        turn.extend(guardian_events(actors, runtime, memories, phase, rng))

        if not turn:
            turn.append("La isla avanza sin incidentes visibles.")
        lines.extend(f"- {line}" for line in turn)
        lines.append("")

    lines.append("## Resultado del sandbox")
    survivors = []
    for actor_id in PARTICIPANTS:
        actor = actors[actor_id]
        alive = actor["hp"] > 0
        if alive:
            survivors.append(actor["name"])
        status = "sobrevive" if alive else "queda fuera de juego"
        lines.append(
            f"- {actor['name']} {status}: casilla {actor['cell']} {actor['micro']}, "
            f"HP {actor['hp']}, hambre {actor['hunger']}, sed {actor['thirst']}, "
            f"energia {actor['stamina']}, miedo {actor['fear']}."
        )

    lines.append("")
    lines.append(f"Supervivientes: {', '.join(survivors) if survivors else 'ninguno'}.")
    lines.append("")
    lines.append("## Memorias globales")
    if memories:
        for key in sorted(memories):
            value = memories[key]
            if isinstance(value, str) and value in actors:
                value = actors[value]["name"]
            lines.append(f"- `{key}`: {value}")
    else:
        lines.append("- Sin memorias globales registradas.")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Simula el sandbox de supervivencia de 4 casillas.")
    parser.add_argument("--seed", type=int, default=11)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    log = simulate(args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(log, encoding="utf-8")
    print(f"Bitacora sandbox escrita en: {args.output}")


if __name__ == "__main__":
    main()
