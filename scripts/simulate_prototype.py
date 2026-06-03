from __future__ import annotations

import argparse
import json
import random
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTOTYPE_PATH = ROOT / "data" / "prototype_island_4.json"
RUNTIME_PATH = ROOT / "data" / "prototype_runtime_4.json"
DEFAULT_OUTPUT = ROOT / "data" / "runs" / "prototype_island_4_last_log.md"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


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


def actor_name(actor_id: str, actors: dict[str, dict]) -> str:
    return actors.get(actor_id, {}).get("name", actor_id)


def apply_hourly_decay(actor: dict, phase: str) -> None:
    if actor.get("type") in {"criatura", "guardian", "jefe"}:
        return

    actor["hunger"] = clamp(actor["hunger"] + 1)
    actor["thirst"] = clamp(actor["thirst"] + 1)
    actor["stamina"] = clamp(actor["stamina"] - 1)

    if phase in {"noche", "madrugada"}:
        actor["fear"] = clamp(actor["fear"] + 2)

    if actor["hunger"] >= 95 or actor["thirst"] >= 95:
        actor["hp"] = clamp(actor["hp"] - 1, 0, 999)


def move_actor(actor: dict, target_cell: int, micro: str, poi: str) -> str:
    actor["cell"] = target_cell
    actor["micro"] = micro
    actor["poi"] = poi
    actor["hidden"] = False
    return f"{actor['name']} se mueve a la casilla {target_cell}, zona {poi} ({micro})."


def rest_actor(actor: dict) -> str:
    actor["stamina"] = clamp(actor["stamina"] + 18)
    actor["fear"] = clamp(actor["fear"] - 6)
    actor["hidden"] = True
    return f"{actor['name']} descansa y reduce el ruido de su presencia."


def consume_if_needed(actor: dict) -> list[str]:
    lines: list[str] = []
    inventory = actor.get("inventory", [])

    if actor.get("thirst", 0) >= 70 and "agua_limpia" in inventory:
        inventory.remove("agua_limpia")
        actor["thirst"] = clamp(actor["thirst"] - 25)
        lines.append(f"{actor['name']} bebe agua limpia.")

    food_items = {"racion_basica": 25, "lata_pequena": 18}
    if actor.get("hunger", 0) >= 75:
        for item_id, value in food_items.items():
            if item_id in inventory:
                inventory.remove(item_id)
                actor["hunger"] = clamp(actor["hunger"] - value)
                lines.append(f"{actor['name']} come una provision pequena.")
                break

    return lines


def find_loot(actor: dict, runtime: dict, rng: random.Random) -> str:
    cell_loot = runtime["cell_loot"].get(str(actor["cell"]), {})
    pool = list(cell_loot.get("common", []))
    if rng.random() < 0.2:
        pool += list(cell_loot.get("rare", []))

    if not pool:
        return f"{actor['name']} busca recursos, pero no encuentra nada util."

    item = rng.choice(pool)
    actor.setdefault("inventory", []).append(item)
    if item == "agua_limpia":
        actor["thirst"] = clamp(actor["thirst"] - 12)
    if item == "racion_basica":
        actor["hunger"] = clamp(actor["hunger"] - 10)
    return f"{actor['name']} encuentra {item.replace('_', ' ')}."


def scripted_turn(day: int, phase: str, actors: dict[str, dict], runtime: dict, memories: dict, rng: random.Random) -> list[str]:
    lines: list[str] = []

    sira = actors["sira"]
    verek = actors["verek"]
    rex = actors["rex"]
    renzo = actors["renzo_manos_frias"]
    silas = actors["silas_crow"]

    if day == 1 and phase == "manana":
        memories["radio_reparada"] = "renzo_manos_frias"
        lines.append("Renzo abre el mastil de radio y une el cable corto con paciencia.")
        lines.append("La radio escupe una frase rota: '...ruinas... no abrir... juramento...'.")
        lines.append("Sira lo observa desde la casa del cuidador sin abandonar su escondite.")
        lines.append("Rex intenta negociar con Verek junto a la fogata del campamento.")
        lines.append("Silas Crow permanece oculto entre los monolitos, contando salidas.")
        return lines

    if day == 1 and phase == "tarde":
        lines += consume_if_needed(rex)
        lines.append(find_loot(rex, runtime, rng))
        memories["trato_con_verek"] = "rex"
        verek["morale"] = clamp(verek["morale"] + 4)
        rex["fear"] = clamp(rex["fear"] - 5)
        lines.append("Verek vende a Rex un rumor barato: el faro no perdona luces tardias.")
        return lines

    if day == 1 and phase == "noche":
        memories["sombra_vista"] = "rex"
        actors["sombras_monolito"]["hidden"] = False
        rex["fear"] = clamp(rex["fear"] + 12)
        lines.append("Una sombra con la silueta de Rex cruza el borde del campamento.")
        lines.append("Verek mira a Rex como si acabara de descubrir una mentira.")
        return lines

    if day == 1 and phase == "madrugada":
        lines.append(rest_actor(sira))
        lines.append(rest_actor(rex))
        lines.append("Silas no duerme: memoriza el patron de las piedras exteriores.")
        return lines

    if day == 2 and phase == "manana":
        lines.append(move_actor(silas, 7, "E6", "trampas"))
        memories["quien_entro_ruinas"] = "silas_crow"
        lines.append("Silas entra a las ruinas por el pasillo de trampas sin avisar a nadie.")
        lines.append("Renzo decide que la radio necesita una lente estable para emitir mejor.")
        return lines

    if day == 2 and phase == "tarde":
        lines.append(move_actor(rex, 1, "I7", "casa_cuidador"))
        sira["hidden"] = False
        memories["rex_vio_sira"] = True
        lines.append("Rex encuentra a Sira en la casa del cuidador y baja la voz por primera vez.")
        lines.append("Sira no le entrega el diario, pero le advierte que las ruinas escuchan.")
        return lines

    if day == 2 and phase == "noche":
        memories["larvas_despertadas"] = "campamento"
        actors["larvas_raiz"]["hidden"] = False
        verek["hp"] = clamp(verek["hp"] - 4, 0, 999)
        lines.append("Las larvas de raiz despiertan bajo las tiendas del campamento.")
        lines.append("Verek recibe una mordida pequena y empieza a maldecir el humo viejo.")
        return lines

    if day == 2 and phase == "madrugada":
        lines.append(rest_actor(renzo))
        lines.append("El faro queda oscuro, pero el metal de la torre suena como si alguien subiera.")
        return lines

    if day == 3 and phase == "manana":
        memories["reliquia_disponible"] = True
        lines.append("La puerta sellada de las ruinas muestra una grieta nueva al amanecer.")
        lines.append("El Centinela de Piedra gira apenas la cabeza, todavia dormido.")
        return lines

    if day == 3 and phase == "tarde":
        if silas["cell"] == 7:
            silas.setdefault("inventory", []).append("reliquia_antigua")
            memories["quien_robo_reliquia"] = "silas_crow"
            memories["reliquia_robada"] = True
            actors["centinela_piedra"]["hidden"] = False
            lines.append("Silas toma la reliquia antigua del patio y el aire pierde temperatura.")
            lines.append("El Centinela de Piedra despierta con un crujido lento.")
        else:
            lines.append("La reliquia sigue esperando en las ruinas.")
        return lines

    if day == 3 and phase == "noche":
        if memories.get("reliquia_robada"):
            memories["guardian_juramentado_despierto"] = True
            actors["guardian_juramentado"]["hidden"] = False
            lines.append("El Guardian Juramentado despierta y pronuncia los nombres que la isla recuerda.")
            lines.append("Su juicio empieza por Silas Crow, pero tambien mira hacia quienes callaron.")
        else:
            lines.append("Las ruinas permanecen cerradas. La isla parece contener la respiracion.")
        return lines

    if day == 3 and phase == "madrugada":
        lines.append("La madrugada deja a todos con menos fuerza y mas preguntas.")
        return lines

    return lines


def simulate(seed: int) -> str:
    prototype = load_json(PROTOTYPE_PATH)
    runtime = load_json(RUNTIME_PATH)
    rng = random.Random(seed)

    base_actors = {actor["id"]: actor for actor in prototype["actors"]}
    actors = deepcopy({entry["id"]: {**base_actors.get(entry["id"], {}), **entry} for entry in runtime["actor_runtime"]})
    memories: dict[str, object] = {}

    clock = runtime["clock"]
    start_hour = clock["start_hour"]
    total_hours = ((clock["pilot_days"] - 1) * clock["hours_per_day"]) + (clock["hours_per_day"] - start_hour)
    turn_hours = clock["narrative_turn_hours"]

    lines = [
        "# Bitacora simulada - Prototipo isla 4 casillas",
        "",
        f"Seed: `{seed}`",
        f"Escala: 1 minuto real = {clock['real_minute_equals_island_hours']} hora isla",
        "",
    ]

    for hour_index in range(0, total_hours):
        absolute_hour = start_hour + hour_index
        day = ((absolute_hour // 24) + 1)
        island_hour = absolute_hour % 24
        phase = phase_for_hour(island_hour)

        for actor in actors.values():
            apply_hourly_decay(actor, phase)

        if hour_index % turn_hours != 0:
            continue

        lines.append(f"## Dia {day} - {phase.title()} ({island_hour:02d}:00)")
        auto_lines: list[str] = []
        for actor_id in ["sira", "verek", "rex", "renzo_manos_frias", "silas_crow"]:
            auto_lines.extend(consume_if_needed(actors[actor_id]))
        turn_lines = scripted_turn(day, phase, actors, runtime, memories, rng)
        if auto_lines:
            turn_lines = auto_lines + turn_lines
        if not turn_lines:
            turn_lines = ["La isla avanza sin un incidente publico claro."]
        lines.extend(f"- {line}" for line in turn_lines)
        lines.append("")

    lines.append("## Estado final")
    for actor_id in ["sira", "verek", "rex", "renzo_manos_frias", "silas_crow"]:
        actor = actors[actor_id]
        lines.append(
            f"- {actor['name']}: casilla {actor['cell']} {actor['micro']}, "
            f"HP {actor['hp']}, hambre {actor['hunger']}, sed {actor['thirst']}, "
            f"energia {actor['stamina']}, miedo {actor['fear']}."
        )

    lines.append("")
    lines.append("## Memorias globales")
    if memories:
        for key in sorted(memories):
            value = memories[key]
            if isinstance(value, str):
                value = actor_name(value, actors)
            lines.append(f"- `{key}`: {value}")
    else:
        lines.append("- Sin memorias globales registradas.")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Simula el prototipo de 4 casillas de Hell Games.")
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    log = simulate(args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(log, encoding="utf-8")
    print(f"Bitacora escrita en: {args.output}")


if __name__ == "__main__":
    main()
