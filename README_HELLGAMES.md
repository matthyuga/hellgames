# Hellgames Bot

Primera version local del bot de Discord para probar el sandbox de Hell Games.

Para contexto completo entre sesiones, leer `HELL_GAMES_CONTINUIDAD.md`.

Repo GitHub:

```txt
https://github.com/matthyuga/hellgames.git
```

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
- `/hg guia`
- `/hg perfil`
- `/hg monedas`
- `/hg reclamar`
- `/hg bitacora`
- `/hg mapa`
- `/hg personaje`
- `/hg rumores`

Admin:

- `/hg admin diagnostico`
- `/hg admin iniciar_piloto`
- `/hg admin avanzar_turno`
- `/hg admin stalk`
- `/hg admin montar_demo`
- `/hg admin sandbox`
- `/hg admin render_mapa`
- `/hg admin publicar_accion`
- `/hg admin publicar_fichas`
- `/hg admin publicar_bitacora`
- `/hg admin publicar_mapa`
- `/hg admin estado_actor`

Owner:

- `/hg owner sync`
- `/hg owner set_canal`

## Flujo de prueba

Flujo recomendado para partida viva:

1. Ejecuta `/hg admin diagnostico`.
2. Si reiniciaste o cambiaste comandos, ejecuta `/hg owner sync`.
3. Ejecuta `/hg admin publicar_fichas`.
4. Ejecuta `/hg admin iniciar_piloto`.
5. Usa `/hg admin avanzar_turno` para publicar una escena cada vez.
6. Usa `/hg admin stalk rex` o cualquier actor para revisar estado interno.
7. Usuarios prueban `/hg bitacora`, `/hg mapa`, `/hg rumores`, `/hg personaje`.

`/hg admin sandbox` genera la simulacion completa de 3 dias y queda como comando
tecnico. Para dirigir la prueba, usar `iniciar_piloto` y `avanzar_turno`.
