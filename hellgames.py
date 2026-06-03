from __future__ import annotations

import os
import traceback
from pathlib import Path

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from scripts.render_prototype_state import main as render_prototype_maps
from scripts.simulate_sandbox import DEFAULT_OUTPUT as SANDBOX_LOG_PATH
from scripts.simulate_sandbox import simulate as simulate_sandbox


ROOT = Path(__file__).resolve().parent
MAP_CONTACT_SHEET = ROOT / "data" / "runs" / "maps" / "prototype_state_contact_sheet.png"
COMMANDS_PATH = ROOT / "data" / "command_unlocks.json"
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
    if channel is None:
        channel = interaction.channel
    if channel is None or not hasattr(channel, "send"):
        raise RuntimeError(f"No pude resolver el canal de destino para {env_name}.")

    file = discord.File(str(file_path)) if file_path and file_path.exists() else None
    await channel.send(content=content, file=file)
    return channel


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
        value="`/hg ayuda`, `/hg perfil`, `/hg bitacora`, `/hg mapa`, `/hg personaje`, `/hg rumores`, `/hg monedas`, `/hg reclamar`",
        inline=False,
    )
    embed.add_field(
        name="Admin",
        value="`/hg admin montar_demo`, `/hg admin sandbox`, `/hg admin render_mapa`, `/hg admin publicar_bitacora`, `/hg admin publicar_mapa`, `/hg admin estado_actor`",
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
    await interaction.response.send_message(
        f"Ficha publica V0 de `{personaje}`: disponible cuando conectemos lectura directa del catalogo.",
        ephemeral=True,
    )


@hg.command(name="rumores", description="Muestra rumores publicos desbloqueados.")
async def hg_rumores(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(
        "- Las ruinas cobran deudas, no monedas.\n- El faro no perdona luces tardias.",
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


@admin.command(name="montar_demo", description="Genera sandbox, renderiza mapa y publica ambos.")
@app_commands.describe(seed="Numero opcional para repetir una simulacion")
async def admin_montar_demo(interaction: discord.Interaction, seed: int = 11) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    try:
        log = simulate_sandbox(seed)
        SANDBOX_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        SANDBOX_LOG_PATH.write_text(log, encoding="utf-8")
        render_prototype_maps()
        log_channel = await publish_bitacora_to_channel(interaction)
        map_channel = await publish_map_to_channel(interaction)
        await interaction.followup.send(
            f"Demo montada con seed `{seed}`.\nBitacora: {getattr(log_channel, 'mention', 'canal configurado')}\nMapa: {getattr(map_channel, 'mention', 'canal configurado')}",
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
        render_prototype_maps()
        await interaction.followup.send("Mapas generados en `data/runs/maps/`.", ephemeral=True)
    except Exception as exc:
        traceback.print_exception(type(exc), exc, exc.__traceback__)
        await interaction.followup.send(f"No pude renderizar el mapa: `{type(exc).__name__}: {exc}`", ephemeral=True)


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


@admin.command(name="estado_actor", description="Muestra estado tecnico pendiente de conectar a runtime.")
@app_commands.describe(actor="ID del actor, ejemplo: rex, verek, guardian_juramentado")
async def admin_estado_actor(interaction: discord.Interaction, actor: str) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.send_message(
        f"Estado tecnico de `{actor}`: pendiente de conectar a lectura persistente. Por ahora revisa `data/prototype_runtime_4.json`.",
        ephemeral=True,
    )


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


if not TOKEN:
    raise SystemExit("Falta HELLGAMES_TOKEN en .env.hellgames")

bot.run(TOKEN)
