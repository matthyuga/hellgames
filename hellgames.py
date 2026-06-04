from __future__ import annotations

import os
import traceback
import json
from pathlib import Path

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from scripts.render_prototype_state import main as render_prototype_maps
from scripts.render_prototype_state import render_state_maps
from scripts.simulate_sandbox import DEFAULT_OUTPUT as SANDBOX_LOG_PATH
from scripts.simulate_sandbox import simulate as simulate_sandbox
from scripts.simulate_sandbox import simulate_live


ROOT = Path(__file__).resolve().parent
MAP_CONTACT_SHEET = ROOT / "data" / "runs" / "maps" / "prototype_state_contact_sheet.png"
COMMANDS_PATH = ROOT / "data" / "command_unlocks.json"
ACTOR_PROFILES_PATH = ROOT / "data" / "actor_profiles.json"
ACTOR_CRAFTING_PROFILES_PATH = ROOT / "data" / "actor_crafting_profiles.json"
LIVE_STATE_PATH = ROOT / "data" / "runs" / "prototype_live_state.json"
DISCORD_TEXT_LIMIT = 1800


def load_config() -> None:
    load_dotenv(ROOT / ".env.hellgames")
    load_dotenv(ROOT / ".env")


def env_int(name: str) -> int | None:
    value = os.getenv(name, "").strip()
    if not value:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def env_int_set(name: str) -> set[int]:
    raw = os.getenv(name, "")
    values: set[int] = set()
    for part in raw.split(","):
        part = part.strip()
        if part.isdigit():
            values.add(int(part))
    return values


def read_text(path: Path, fallback: str) -> str:
    if not path.exists():
        return fallback
    return path.read_text(encoding="utf-8")


def load_actor_profiles() -> dict[str, dict]:
    if not ACTOR_PROFILES_PATH.exists():
        return {}
    data = json.loads(ACTOR_PROFILES_PATH.read_text(encoding="utf-8"))
    return {actor["id"]: actor for actor in data.get("actors", [])}


def load_actor_crafting_profiles() -> dict[str, dict]:
    if not ACTOR_CRAFTING_PROFILES_PATH.exists():
        return {}
    data = json.loads(ACTOR_CRAFTING_PROFILES_PATH.read_text(encoding="utf-8"))
    return {actor["id"]: actor for actor in data.get("actors", [])}


def load_live_pointer() -> dict | None:
    if not LIVE_STATE_PATH.exists():
        return None
    return json.loads(LIVE_STATE_PATH.read_text(encoding="utf-8"))


def write_live_snapshot(seed: int, turn_index: int) -> dict:
    snapshot = simulate_live(seed, completed_turns=turn_index)
    SANDBOX_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    SANDBOX_LOG_PATH.write_text(snapshot["log_text"], encoding="utf-8")
    LIVE_STATE_PATH.write_text(
        json.dumps(
            {
                "seed": seed,
                "turn_index": snapshot["turn_index"],
                "total_turns": snapshot["total_turns"],
                "complete": snapshot["complete"],
            },
            ensure_ascii=True,
            indent=2,
        ),
        encoding="utf-8",
    )
    render_state_maps(list(snapshot["actors"].values()))
    return snapshot


def trim_for_discord(text: str, limit: int = DISCORD_TEXT_LIMIT) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 80].rstrip() + "\n\n...[bitacora recortada para Discord]"


load_config()

TOKEN = os.getenv("HELLGAMES_TOKEN") or os.getenv("DISCORD_TOKEN")
GUILD_ID = env_int("DISCORD_GUILD_ID")
OWNER_IDS = env_int_set("HELLGAMES_OWNER_IDS")
ADMIN_ROLE_IDS = env_int_set("HELLGAMES_ADMIN_ROLE_IDS")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
hg = app_commands.Group(name="hg", description="Comandos de Hellgames")
admin = app_commands.Group(name="admin", description="Comandos admin de Hellgames")
owner = app_commands.Group(name="owner", description="Comandos owner de Hellgames")


def is_owner(interaction: discord.Interaction) -> bool:
    if interaction.user.id in OWNER_IDS:
        return True
    return bool(bot.owner_id and interaction.user.id == bot.owner_id)


def is_admin(interaction: discord.Interaction) -> bool:
    if is_owner(interaction):
        return True
    user = interaction.user
    if isinstance(user, discord.Member):
        return any(role.id in ADMIN_ROLE_IDS for role in user.roles)
    return False


async def require_admin(interaction: discord.Interaction) -> bool:
    if is_admin(interaction):
        return True
    await interaction.response.send_message("Este comando requiere admin/owner de Hellgames.", ephemeral=True)
    return False


async def send_to_configured_channel(
    interaction: discord.Interaction,
    env_name: str,
    content: str | None = None,
    file_path: Path | None = None,
) -> discord.abc.Messageable:
    channel_id = env_int(env_name)
    channel = interaction.client.get_channel(channel_id) if channel_id else None
    if channel is None and channel_id:
        channel = await interaction.client.fetch_channel(channel_id)
    if channel is None:
        channel = interaction.channel
    if channel is None or not hasattr(channel, "send"):
        raise RuntimeError(f"No pude resolver el canal de destino para {env_name}.")

    file = discord.File(str(file_path)) if file_path and file_path.exists() else None
    await channel.send(content=content, file=file)
    return channel


def required_channel_permissions(need_file: bool = False) -> tuple[str, ...]:
    base = ("view_channel", "send_messages", "embed_links", "read_message_history")
    if need_file:
        return base + ("attach_files",)
    return base


async def describe_channel_access(interaction: discord.Interaction, env_name: str, need_file: bool = False) -> str:
    channel_id = env_int(env_name)
    if not channel_id:
        return f"- `{env_name}`: FALTA ID"
    try:
        channel = interaction.client.get_channel(channel_id) or await interaction.client.fetch_channel(channel_id)
    except Exception as exc:
        return f"- `{env_name}` `{channel_id}`: no accesible (`{type(exc).__name__}: {exc}`)"

    guild = interaction.guild
    me = guild.me if guild else None
    if me is None or not isinstance(channel, discord.abc.GuildChannel):
        return f"- `{env_name}` {getattr(channel, 'mention', channel_id)}: no pude leer permisos del guild"

    perms = channel.permissions_for(me)
    missing = [perm for perm in required_channel_permissions(need_file) if not getattr(perms, perm, False)]
    if missing:
        return f"- `{env_name}` {channel.mention}: FALTAN {', '.join(missing)}"
    return f"- `{env_name}` {channel.mention}: OK"


async def publish_bitacora_to_channel(interaction: discord.Interaction) -> discord.abc.Messageable:
    text = read_text(SANDBOX_LOG_PATH, "Todavia no hay bitacora sandbox.")
    preview = trim_for_discord(text, 1300)
    content = f"**Bitacora sandbox generada**\n```md\n{preview}\n```"
    return await send_to_configured_channel(
        interaction,
        "HG_PUBLIC_LOG_CHANNEL_ID",
        content,
        SANDBOX_LOG_PATH if SANDBOX_LOG_PATH.exists() else None,
    )


async def publish_map_to_channel(interaction: discord.Interaction) -> discord.abc.Messageable:
    if not MAP_CONTACT_SHEET.exists():
        render_prototype_maps()
    size_mb = MAP_CONTACT_SHEET.stat().st_size / (1024 * 1024)
    content = f"**Mapa de estado del sandbox**\nArchivo: `{size_mb:.2f} MB`"
    return await send_to_configured_channel(interaction, "HG_PUBLIC_MAP_CHANNEL_ID", content, MAP_CONTACT_SHEET)


def split_bitacora_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current_title = "Inicio"
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current_lines:
                sections.append((current_title, "\n".join(current_lines).strip()))
            current_title = line.replace("## ", "", 1).strip()
            current_lines = [line]
        else:
            current_lines.append(line)
    if current_lines:
        sections.append((current_title, "\n".join(current_lines).strip()))
    return [(title, body) for title, body in sections if body]


async def publish_action_feed(interaction: discord.Interaction, max_sections: int = 12) -> discord.abc.Messageable:
    text = read_text(SANDBOX_LOG_PATH, "Todavia no hay bitacora sandbox.")
    channel_id = env_int("HG_ACTION_CHANNEL_ID")
    channel = interaction.client.get_channel(channel_id) if channel_id else None
    if channel is None and channel_id:
        channel = await interaction.client.fetch_channel(channel_id)
    if channel is None or not hasattr(channel, "send"):
        raise RuntimeError("No pude resolver HG_ACTION_CHANNEL_ID.")

    sections = split_bitacora_sections(text)
    sent_channel = channel
    await sent_channel.send("**Hellgames Battle Royale - accion del sandbox**")
    for title, body in sections[:max_sections]:
        if title.lower().startswith("bitacora sandbox"):
            continue
        await sent_channel.send(f"```md\n{trim_for_discord(body, 1700)}\n```")
    return sent_channel


async def get_action_channel(interaction: discord.Interaction) -> discord.abc.Messageable:
    channel_id = env_int("HG_ACTION_CHANNEL_ID")
    channel = interaction.client.get_channel(channel_id) if channel_id else None
    if channel is None and channel_id:
        channel = await interaction.client.fetch_channel(channel_id)
    if channel is None or not hasattr(channel, "send"):
        raise RuntimeError("No pude resolver HG_ACTION_CHANNEL_ID.")
    return channel


async def publish_live_intro(interaction: discord.Interaction, snapshot: dict) -> discord.abc.Messageable:
    channel = await get_action_channel(interaction)
    lines = "\n".join(f"- {line}" for line in snapshot["intro_events"])
    await channel.send(
        "**Hellgames Battle Royale - piloto iniciado**\n"
        f"Seed `{snapshot['seed']}` | turno `0/{snapshot['total_turns']}`\n"
        f"```md\n## Inicio\n{trim_for_discord(lines, 1500)}\n```"
    )
    return channel


async def publish_live_turn(interaction: discord.Interaction, snapshot: dict) -> discord.abc.Messageable:
    channel = await get_action_channel(interaction)
    turn = snapshot.get("latest_turn")
    if not turn:
        await channel.send("**Hellgames Battle Royale**\nNo hay turno narrativo para publicar todavia.")
        return channel
    body = "\n".join(f"- {line}" for line in turn["lines"])
    await channel.send(
        f"**Hellgames Battle Royale - turno {snapshot['turn_index']}/{snapshot['total_turns']}**\n"
        f"```md\n## {turn['title']}\n{trim_for_discord(body, 1600)}\n```"
    )
    if snapshot.get("complete"):
        await channel.send("**La prueba piloto llego al final.** Usa `/hg bitacora` para revisar el archivo completo.")
    return channel


def actor_profile_embed(profile: dict) -> discord.Embed:
    color_by_kind = {
        "participante": discord.Color.red(),
        "lugareno": discord.Color.blue(),
        "criatura": discord.Color.purple(),
        "guardian": discord.Color.orange(),
        "jefe": discord.Color.dark_gold(),
    }
    embed = discord.Embed(
        title=profile["name"],
        description=profile.get("public_summary", ""),
        color=color_by_kind.get(profile.get("kind"), discord.Color.dark_grey()),
    )
    embed.add_field(name="Tipo", value=profile.get("kind", "desconocido"), inline=True)
    embed.add_field(name="Rol", value=profile.get("role", "sin rol"), inline=True)
    embed.add_field(name="Rasgos", value=", ".join(profile.get("personality", [])) or "sin datos", inline=False)
    embed.add_field(name="Habilidades", value=", ".join(profile.get("known_skills", [])) or "sin datos", inline=False)
    hooks = profile.get("public_hooks", [])
    if hooks:
        embed.add_field(name="Ganchos", value="\n".join(f"- {hook}" for hook in hooks), inline=False)
    if profile.get("image_asset_id"):
        embed.set_footer(text=f"Asset: {profile['image_asset_id']}")
    else:
        embed.set_footer(text="Imagen pendiente de asignar")
    return embed


def actor_status_embed(actor: dict, profile: dict | None = None, crafting: dict | None = None) -> discord.Embed:
    title = actor.get("name", actor.get("id", "Actor"))
    embed = discord.Embed(title=f"Stalk: {title}", color=discord.Color.dark_red())
    if profile:
        embed.description = profile.get("public_summary", "")
    embed.add_field(name="Ubicacion", value=f"Casilla {actor.get('cell')} | {actor.get('poi')} ({actor.get('micro')})", inline=False)
    embed.add_field(
        name="Estado",
        value=(
            f"HP {actor.get('hp', '?')} | hambre {actor.get('hunger', '?')} | sed {actor.get('thirst', '?')}\n"
            f"energia {actor.get('stamina', '?')} | miedo {actor.get('fear', '?')} | oculto {actor.get('hidden', False)}"
        ),
        inline=False,
    )
    inventory = actor.get("inventory", [])
    embed.add_field(name="Inventario", value=", ".join(inventory) if inventory else "sin objetos visibles", inline=False)
    if crafting:
        embed.add_field(name="Intereses", value=", ".join(crafting.get("interests", [])) or "sin datos", inline=False)
        embed.add_field(name="Recetas conocidas", value=", ".join(crafting.get("known_recipes", [])) or "sin datos", inline=False)
        embed.add_field(name="Busca", value=", ".join(crafting.get("search_priorities", [])) or "sin datos", inline=False)
    return embed


@bot.event
async def on_ready() -> None:
    if GUILD_ID:
        guild = discord.Object(id=GUILD_ID)
        bot.tree.copy_global_to(guild=guild)
        synced = await bot.tree.sync(guild=guild)
        print(f"Hellgames listo como {bot.user} | sync guild {GUILD_ID}: {len(synced)} comandos")
    else:
        synced = await bot.tree.sync()
        print(f"Hellgames listo como {bot.user} | sync global: {len(synced)} comandos")


@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
    print("Error en comando slash:")
    traceback.print_exception(type(error), error, error.__traceback__)
    message = f"Algo fallo ejecutando el comando: `{type(error).__name__}`."
    try:
        if interaction.response.is_done():
            await interaction.followup.send(message, ephemeral=True)
        else:
            await interaction.response.send_message(message, ephemeral=True)
    except Exception:
        pass


@hg.command(name="ayuda", description="Muestra comandos disponibles en la V0.")
async def hg_ayuda(interaction: discord.Interaction) -> None:
    embed = discord.Embed(
        title="Hellgames V0",
        description="Sandbox de supervivencia de 4 casillas. Los comandos con admin son privados para pruebas.",
        color=discord.Color.dark_red(),
    )
    embed.add_field(
        name="Publicos",
        value="`/hg ayuda`, `/hg guia`, `/hg perfil`, `/hg bitacora`, `/hg mapa`, `/hg personaje`, `/hg rumores`, `/hg monedas`, `/hg reclamar`",
        inline=False,
    )
    embed.add_field(
        name="Admin",
        value="`/hg admin iniciar_piloto`, `/hg admin avanzar_turno`, `/hg admin stalk`, `/hg admin diagnostico`, `/hg admin montar_demo`, `/hg admin publicar_accion`, `/hg admin publicar_fichas`, `/hg admin sandbox`, `/hg admin render_mapa`, `/hg admin publicar_bitacora`, `/hg admin publicar_mapa`, `/hg admin estado_actor`",
        inline=False,
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


@hg.command(name="guia", description="Guia breve para seguir la prueba piloto.")
async def hg_guia(interaction: discord.Interaction) -> None:
    embed = discord.Embed(
        title="Guia de ritmo - piloto Hellgames",
        description="La prueba viva funciona por turnos. Cada turno son 6 horas de isla; con la escala actual puedes avanzarlo manualmente cuando quieras.",
        color=discord.Color.dark_gold(),
    )
    embed.add_field(
        name="Inicio recomendado",
        value="1. `/hg admin diagnostico`\n2. `/hg owner sync` si reiniciaste el bot\n3. `/hg admin publicar_fichas`\n4. `/hg admin iniciar_piloto`\n5. `/hg admin avanzar_turno` para cada escena",
        inline=False,
    )
    embed.add_field(
        name="Seguimiento",
        value="`/hg admin stalk rex` revisa estado interno.\n`/hg mapa` muestra el ultimo mapa renderizado.\n`/hg bitacora` guarda lo ocurrido hasta el turno actual.",
        inline=False,
    )
    embed.add_field(
        name="Canales",
        value="La accion vive en battleroyale. El mapa queda separado. La bitacora es archivo/resumen, no el ritmo principal.",
        inline=False,
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


@hg.command(name="perfil", description="Muestra tu perfil inicial de espectador.")
async def hg_perfil(interaction: discord.Interaction) -> None:
    embed = discord.Embed(title=f"Perfil de {interaction.user.display_name}", color=discord.Color.gold())
    embed.add_field(name="Nivel", value="0 - Espectador", inline=True)
    embed.add_field(name="XP", value="0", inline=True)
    embed.add_field(name="Hellcoins", value="100 iniciales cuando activemos base de datos", inline=False)
    embed.set_footer(text="V0: perfil simulado. La persistencia real vendra con SQLite.")
    await interaction.response.send_message(embed=embed, ephemeral=True)


@hg.command(name="monedas", description="Muestra tus Hellcoins.")
async def hg_monedas(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(
        "V0 local: tendrias **100 Hellcoins** iniciales. La cartera persistente vendra con SQLite.",
        ephemeral=True,
    )


@hg.command(name="reclamar", description="Reclama bono diario de Hellcoins.")
async def hg_reclamar(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(
        "Bono diario previsto: **+25 Hellcoins**. En V0 aun no se guarda saldo persistente.",
        ephemeral=True,
    )


@hg.command(name="bitacora", description="Muestra la ultima bitacora sandbox generada.")
async def hg_bitacora(interaction: discord.Interaction) -> None:
    text = read_text(SANDBOX_LOG_PATH, "Todavia no hay bitacora. Un admin debe ejecutar `/hg admin sandbox`.")
    file = discord.File(str(SANDBOX_LOG_PATH)) if SANDBOX_LOG_PATH.exists() else None
    await interaction.response.send_message(f"```md\n{trim_for_discord(text)}\n```", file=file, ephemeral=True)


@hg.command(name="mapa", description="Muestra el ultimo mapa de estado generado.")
async def hg_mapa(interaction: discord.Interaction) -> None:
    if not MAP_CONTACT_SHEET.exists():
        await interaction.response.send_message("Todavia no hay mapa. Un admin debe ejecutar `/hg admin render_mapa`.", ephemeral=True)
        return
    await interaction.response.send_message(file=discord.File(str(MAP_CONTACT_SHEET)), ephemeral=True)


@hg.command(name="personaje", description="Muestra una ficha publica basica.")
@app_commands.describe(personaje="ID del personaje, ejemplo: rex, sira, silas_crow")
async def hg_personaje(interaction: discord.Interaction, personaje: str) -> None:
    profiles = load_actor_profiles()
    profile = profiles.get(personaje.strip().lower())
    if not profile:
        await interaction.response.send_message(
            f"No encontre `{personaje}`. Prueba: {', '.join(sorted(profiles)[:8])}",
            ephemeral=True,
        )
        return
    await interaction.response.send_message(embed=actor_profile_embed(profile), ephemeral=True)


@hg.command(name="rumores", description="Muestra rumores publicos desbloqueados.")
async def hg_rumores(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(
        "- Las ruinas cobran deudas, no monedas.\n- El faro no perdona luces tardias.",
        ephemeral=True,
    )


@admin.command(name="iniciar_piloto", description="Inicia la partida viva sin publicar los 3 dias completos.")
@app_commands.describe(seed="Numero opcional para repetir una simulacion")
async def admin_iniciar_piloto(interaction: discord.Interaction, seed: int = 11) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    try:
        snapshot = write_live_snapshot(seed, 0)
        channel = await publish_live_intro(interaction, snapshot)
        await interaction.followup.send(
            f"Piloto iniciado con seed `{seed}`.\nAccion: {getattr(channel, 'mention', 'canal configurado')}\nTurno actual: `0/{snapshot['total_turns']}`.",
            ephemeral=True,
        )
    except Exception as exc:
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        await interaction.followup.send(f"No pude iniciar el piloto: `{type(exc).__name__}: {exc}`", ephemeral=True)


@admin.command(name="avanzar_turno", description="Avanza una escena viva del piloto.")
async def admin_avanzar_turno(interaction: discord.Interaction) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    try:
        pointer = load_live_pointer()
        if not pointer:
            await interaction.followup.send("No hay piloto vivo. Usa `/hg admin iniciar_piloto` primero.", ephemeral=True)
            return
        if pointer.get("complete"):
            await interaction.followup.send("El piloto ya esta completo. Usa `/hg admin iniciar_piloto` para reiniciar.", ephemeral=True)
            return
        next_turn = int(pointer["turn_index"]) + 1
        snapshot = write_live_snapshot(int(pointer["seed"]), next_turn)
        channel = await publish_live_turn(interaction, snapshot)
        await interaction.followup.send(
            f"Turno publicado en {getattr(channel, 'mention', 'el canal configurado')}.\nTurno actual: `{snapshot['turn_index']}/{snapshot['total_turns']}`. Mapa y bitacora local actualizados.",
            ephemeral=True,
        )
    except Exception as exc:
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        await interaction.followup.send(f"No pude avanzar el turno: `{type(exc).__name__}: {exc}`", ephemeral=True)


@admin.command(name="stalk", description="Revisa el estado vivo de un actor.")
@app_commands.describe(actor="ID del actor, ejemplo: rex, renzo_manos_frias, sira")
async def admin_stalk(interaction: discord.Interaction, actor: str) -> None:
    if not await require_admin(interaction):
        return
    pointer = load_live_pointer()
    if not pointer:
        await interaction.response.send_message("No hay piloto vivo. Usa `/hg admin iniciar_piloto` primero.", ephemeral=True)
        return
    snapshot = simulate_live(int(pointer["seed"]), completed_turns=int(pointer["turn_index"]))
    actor_id = actor.strip().lower()
    target = snapshot["actors"].get(actor_id)
    if not target:
        await interaction.response.send_message(
            f"No encontre `{actor}`. Prueba: {', '.join(sorted(snapshot['actors'])[:10])}",
            ephemeral=True,
        )
        return
    profiles = load_actor_profiles()
    crafting = load_actor_crafting_profiles()
    await interaction.response.send_message(
        embed=actor_status_embed(target, profiles.get(actor_id), crafting.get(actor_id)),
        ephemeral=True,
    )


@admin.command(name="sandbox", description="Ejecuta una simulacion sandbox de 3 dias.")
@app_commands.describe(seed="Numero opcional para repetir una simulacion")
async def admin_sandbox(interaction: discord.Interaction, seed: int = 11) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    log = simulate_sandbox(seed)
    SANDBOX_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    SANDBOX_LOG_PATH.write_text(log, encoding="utf-8")
    await interaction.followup.send(f"Sandbox generado con seed `{seed}`.\n`{SANDBOX_LOG_PATH}`", ephemeral=True)


@admin.command(name="diagnostico", description="Revisa acceso del bot a los canales configurados.")
async def admin_diagnostico(interaction: discord.Interaction) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    checks = [
        ("HG_ACTION_CHANNEL_ID", False),
        ("HG_PUBLIC_MAP_CHANNEL_ID", True),
        ("HG_PUBLIC_LOG_CHANNEL_ID", True),
        ("HG_RUMORS_CHANNEL_ID", False),
        ("HG_ADMIN_LOG_CHANNEL_ID", False),
        ("HG_ASSET_CHANNEL_ID", True),
        ("HG_DATABASE_CHANNEL_ID", False),
        ("HG_DEBUG_CHANNEL_ID", False),
    ]
    lines = [await describe_channel_access(interaction, env_name, need_file) for env_name, need_file in checks]
    await interaction.followup.send("**Diagnostico de canales Hellgames**\n" + "\n".join(lines), ephemeral=True)


@admin.command(name="montar_demo", description="Atajo: inicia piloto vivo, publica inicio, mapa y bitacora inicial.")
@app_commands.describe(seed="Numero opcional para repetir una simulacion")
async def admin_montar_demo(interaction: discord.Interaction, seed: int = 11) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    try:
        snapshot = write_live_snapshot(seed, 0)
        action_channel = await publish_live_intro(interaction, snapshot)
        log_channel = await publish_bitacora_to_channel(interaction)
        map_channel = await publish_map_to_channel(interaction)
        await interaction.followup.send(
            f"Demo viva montada con seed `{seed}`.\nAccion: {getattr(action_channel, 'mention', 'canal configurado')}\nBitacora inicial: {getattr(log_channel, 'mention', 'canal configurado')}\nMapa: {getattr(map_channel, 'mention', 'canal configurado')}\nSiguiente paso: `/hg admin avanzar_turno`.",
            ephemeral=True,
        )
    except Exception as exc:
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        await interaction.followup.send(f"No pude montar la demo: `{type(exc).__name__}: {exc}`", ephemeral=True)


@admin.command(name="render_mapa", description="Genera los mapas de estado del piloto.")
async def admin_render_mapa(interaction: discord.Interaction) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    try:
        pointer = load_live_pointer()
        if pointer:
            snapshot = simulate_live(int(pointer["seed"]), completed_turns=int(pointer["turn_index"]))
            render_state_maps(list(snapshot["actors"].values()))
            await interaction.followup.send("Mapas vivos generados en `data/runs/maps/`.", ephemeral=True)
        else:
            render_prototype_maps()
            await interaction.followup.send("Mapas iniciales generados en `data/runs/maps/`.", ephemeral=True)
    except Exception as exc:
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        await interaction.followup.send(f"No pude renderizar el mapa: `{type(exc).__name__}: {exc}`", ephemeral=True)


@admin.command(name="publicar_accion", description="Publica la bitacora por escenas en el canal principal.")
async def admin_publicar_accion(interaction: discord.Interaction) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    try:
        channel = await publish_action_feed(interaction)
        await interaction.followup.send(f"Accion publicada en {getattr(channel, 'mention', 'el canal configurado')}.", ephemeral=True)
    except Exception as exc:
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        await interaction.followup.send(f"No pude publicar la accion: `{type(exc).__name__}: {exc}`", ephemeral=True)


@admin.command(name="publicar_fichas", description="Publica fichas base en el canal database.")
async def admin_publicar_fichas(interaction: discord.Interaction) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    try:
        channel_id = env_int("HG_DATABASE_CHANNEL_ID")
        channel = interaction.client.get_channel(channel_id) if channel_id else None
        if channel is None and channel_id:
            channel = await interaction.client.fetch_channel(channel_id)
        if channel is None or not hasattr(channel, "send"):
            raise RuntimeError("No pude resolver HG_DATABASE_CHANNEL_ID.")

        profiles = load_actor_profiles()
        await channel.send("**Hellgames database - fichas base V0**")
        for profile in profiles.values():
            await channel.send(embed=actor_profile_embed(profile))
        await channel.send(file=discord.File(str(ACTOR_PROFILES_PATH)))
        if ACTOR_CRAFTING_PROFILES_PATH.exists():
            await channel.send("**Hellgames database - conocimientos de recetas e intereses V0**")
            await channel.send(file=discord.File(str(ACTOR_CRAFTING_PROFILES_PATH)))
        await interaction.followup.send(f"Fichas publicadas en {getattr(channel, 'mention', 'el canal database')}.", ephemeral=True)
    except Exception as exc:
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        await interaction.followup.send(f"No pude publicar fichas: `{type(exc).__name__}: {exc}`", ephemeral=True)


@admin.command(name="publicar_bitacora", description="Publica la ultima bitacora en el canal configurado.")
async def admin_publicar_bitacora(interaction: discord.Interaction) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    try:
        channel = await publish_bitacora_to_channel(interaction)
        await interaction.followup.send(f"Bitacora publicada en {getattr(channel, 'mention', 'el canal configurado')}.", ephemeral=True)
    except Exception as exc:
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        await interaction.followup.send(f"No pude publicar la bitacora: `{type(exc).__name__}: {exc}`", ephemeral=True)


@admin.command(name="publicar_mapa", description="Publica el ultimo mapa en el canal configurado.")
async def admin_publicar_mapa(interaction: discord.Interaction) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    try:
        channel = await publish_map_to_channel(interaction)
        await interaction.followup.send(f"Mapa publicado en {getattr(channel, 'mention', 'el canal configurado')}.", ephemeral=True)
    except Exception as exc:
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        await interaction.followup.send(f"No pude publicar el mapa: `{type(exc).__name__}: {exc}`", ephemeral=True)


@admin.command(name="estado_actor", description="Muestra el estado vivo de un actor.")
@app_commands.describe(actor="ID del actor, ejemplo: rex, verek, guardian_juramentado")
async def admin_estado_actor(interaction: discord.Interaction, actor: str) -> None:
    if not await require_admin(interaction):
        return
    pointer = load_live_pointer()
    if not pointer:
        await interaction.response.send_message("No hay piloto vivo. Usa `/hg admin iniciar_piloto` primero.", ephemeral=True)
        return
    snapshot = simulate_live(int(pointer["seed"]), completed_turns=int(pointer["turn_index"]))
    actor_id = actor.strip().lower()
    target = snapshot["actors"].get(actor_id)
    if not target:
        await interaction.response.send_message(f"No encontre `{actor}`.", ephemeral=True)
        return
    lines = [
        f"**{target['name']}**",
        f"Turno `{snapshot['turn_index']}/{snapshot['total_turns']}`",
        f"Ubicacion: casilla `{target.get('cell')}`, `{target.get('poi')}` (`{target.get('micro')}`)",
        f"HP `{target.get('hp')}` | hambre `{target.get('hunger')}` | sed `{target.get('thirst')}` | energia `{target.get('stamina')}` | miedo `{target.get('fear')}`",
        f"Inventario: {', '.join(target.get('inventory', [])) or 'sin objetos'}",
    ]
    await interaction.response.send_message("\n".join(lines), ephemeral=True)


@owner.command(name="sync", description="Sincroniza comandos slash.")
async def owner_sync(interaction: discord.Interaction) -> None:
    if not is_owner(interaction):
        await interaction.response.send_message("Este comando requiere owner.", ephemeral=True)
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    if GUILD_ID:
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
    else:
        synced = await bot.tree.sync()
    await interaction.followup.send(f"Comandos sincronizados: {len(synced)}.", ephemeral=True)


@owner.command(name="set_canal", description="Placeholder para configuracion futura de canales.")
async def owner_set_canal(interaction: discord.Interaction) -> None:
    if not is_owner(interaction):
        await interaction.response.send_message("Este comando requiere owner.", ephemeral=True)
        return
    await interaction.response.send_message("V0: configura canales editando `.env.hellgames`.", ephemeral=True)


hg.add_command(admin)
hg.add_command(owner)
bot.tree.add_command(hg)


if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("Falta HELLGAMES_TOKEN en .env.hellgames")
    bot.run(TOKEN)
