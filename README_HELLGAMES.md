# Hellgames Bot

Primera version local del bot de Discord para probar el sandbox de Hell Games.

## Configuracion local

1. Copia `.env.hellgames.example` a `.env.hellgames`.
2. Pega el token en `HELLGAMES_TOKEN`.
3. Activa Developer Mode en Discord y copia IDs de servidor/canales.
4. Rellena al menos:

```txt
DISCORD_GUILD_ID=
HG_ACTION_CHANNEL_ID=
HG_PUBLIC_MAP_CHANNEL_ID=
HG_PUBLIC_LOG_CHANNEL_ID=
HG_ADMIN_LOG_CHANNEL_ID=
HG_DEBUG_CHANNEL_ID=
```

Para poder usar comandos admin, agrega tu ID de usuario:

```txt
HELLGAMES_OWNER_IDS=tu_id
```

## Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

## Arrancar

```powershell
python hellgames.py
```

o doble clic en:

```txt
iniciar_hellgames.cmd
```

## Comandos V0

Publicos:

- `/hg ayuda`
- `/hg perfil`
- `/hg monedas`
- `/hg reclamar`
- `/hg bitacora`
- `/hg mapa`
- `/hg personaje`
- `/hg rumores`

Admin:

- `/hg admin sandbox`
- `/hg admin render_mapa`
- `/hg admin publicar_bitacora`
- `/hg admin publicar_mapa`
- `/hg admin estado_actor`

Owner:

- `/hg owner sync`
- `/hg owner set_canal`

## Flujo de prueba

1. Ejecuta `/hg admin sandbox`.
2. Ejecuta `/hg admin render_mapa`.
3. Ejecuta `/hg admin publicar_bitacora`.
4. Ejecuta `/hg admin publicar_mapa`.
5. Usuarios prueban `/hg bitacora`, `/hg mapa`, `/hg rumores`.
