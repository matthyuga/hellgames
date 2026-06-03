# MarvaBot

Bot separado para moderacion honeypot/autoban.

## Configuracion

Edita `.env.marvabot`:

```env
MARVABOT_TOKEN=token_real_de_marvabot
DISCORD_GUILD_ID=463380191587336192
HONEYPOT_CHANNEL_ID=id_del_canal_spam_autoban
MOD_LOG_CHANNEL_ID=id_del_canal_marvabot_logs
AUTOBAN_DRY_RUN=true
MARVABOT_DATABASE=data/marvabot.sqlite3
MEE6_GUILD_ID=463380191587336192
MEE6_CACHE_SECONDS=60
MEE6_COOLDOWN_SECONDS=60
```

Dejalo en `AUTOBAN_DRY_RUN=true` para la primera prueba. En ese modo MarvaBot
solo reporta lo que haria, sin banear.

## Permisos recomendados

- Ver canales
- Enviar mensajes
- Gestionar mensajes
- Leer historial de mensajes
- Insertar enlaces
- Usar comandos de barra diagonal
- Banear miembros
- Moderar miembros

El rol de MarvaBot debe estar por encima de los roles de usuarios nuevos o no
verificados. No necesita Administrador.

## Canal trampa

El canal trampa debe tener ID exacto en `HONEYPOT_CHANNEL_ID`.

Mensaje fijado sugerido:

```text
DO NOT POST HERE.
This is a honeypot channel for spambots.
Anyone who posts here may be automatically banned.
If you are a real user, do not write in this channel.
```

## Canal de logs

Crea un canal privado, por ejemplo `#marvabot-logs`, y pega su ID en
`MOD_LOG_CHANNEL_ID`.

## Comandos

- `/marva-estado`: muestra configuracion activa.
- `/marva-test`: revisa permisos basicos.
- `/marva-kills`: muestra contador de bans registrados.
- `/marva-barrido [limite]`: borra mensajes recientes del canal trampa,
  conservando mensajes fijados salvo que indiques lo contrario.
- `/mee6-top [cantidad] [pagina]`: muestra el ranking publico de MEE6.
- `/mee6-link`: manda el link publico del leaderboard MEE6.

## Arranque

```powershell
python marvabot.py
```

o doble clic en:

```text
iniciar_marvabot.cmd
```

Cuando el dry-run funcione bien, cambia:

```env
AUTOBAN_DRY_RUN=false
DELETE_TRIGGER_MESSAGE=true
```

Reinicia el bot y el autoban real quedara activo. Para borrar el mensaje o
imagen del scammer, MarvaBot necesita `Gestionar mensajes` en el canal trampa.

## Discloud Free

Para probar MarvaBot 24/7 sin depender de la PC local, ver:

```text
README_DISCLOUD_MARVABOT.md
```

El repo ya incluye:

- `discloud.config`
- `scripts/package_marvabot_discloud.ps1`
