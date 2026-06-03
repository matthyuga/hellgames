from __future__ import annotations

import os
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


def trim_for_discord(text: str, limit: int = 3900) -> str:
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
) -> None:
    channel_id = env_int(env_name)
    channel = interaction.client.get_channel(channel_id) if channel_id else None
    if channel is None:
        channel = interaction.channel
    if channel is None or not hasattr(channel, "send"):
        await interaction.followup.send("No pude resolver el canal de destino.", ephemeral=True)
        return

    file = discord.File(str(file_path)) if file_path and file_path.exists() else None
    await channel.send(content=content, file=file)


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
        value="`/hg admin sandbox`, `/hg admin render_mapa`, `/hg admin publicar_bitacora`, `/hg admin publicar_mapa`, `/hg admin estado_actor`",
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
    await interaction.response.send_message(f"```md\n{trim_for_discord(text)}\n```", ephemeral=True)


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


@admin.command(name="render_mapa", description="Genera los mapas de estado del piloto.")
async def admin_render_mapa(interaction: discord.Interaction) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    render_prototype_maps()
    await interaction.followup.send("Mapas generados en `data/runs/maps/`.", ephemeral=True)


@admin.command(name="publicar_bitacora", description="Publica la ultima bitacora en el canal configurado.")
async def admin_publicar_bitacora(interaction: discord.Interaction) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    text = read_text(SANDBOX_LOG_PATH, "Todavia no hay bitacora sandbox.")
    await send_to_configured_channel(interaction, "HG_PUBLIC_LOG_CHANNEL_ID", f"```md\n{trim_for_discord(text)}\n```")
    await interaction.followup.send("Bitacora publicada.", ephemeral=True)


@admin.command(name="publicar_mapa", description="Publica el ultimo mapa en el canal configurado.")
async def admin_publicar_mapa(interaction: discord.Interaction) -> None:
    if not await require_admin(interaction):
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
    if not MAP_CONTACT_SHEET.exists():
        render_prototype_maps()
    await send_to_configured_channel(interaction, "HG_PUBLIC_MAP_CHANNEL_ID", "Mapa de estado del sandbox.", MAP_CONTACT_SHEET)
    await interaction.followup.send("Mapa publicado.", ephemeral=True)


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
