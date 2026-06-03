# Hell Games - Bot de Discord y assets por ID

Guia practica para preparar la primera version del bot Hellgames en Discord.

## Primera version recomendada

Empezar con datos locales:

- `data/prototype_island_4.json`;
- `data/prototype_runtime_4.json`;
- scripts de simulacion y mapas;
- bitacoras generadas en local o en una base SQLite pequena.

En esta etapa el bot no necesita cargar todo el banco visual. Solo necesita:

- leer datos JSON;
- generar o adjuntar mapas de estado;
- publicar bitacoras;
- responder comandos de prueba.

## Permisos minimos del bot

Scopes al invitarlo:

- `bot`;
- `applications.commands`.

Permisos para canales publicos del evento:

- ver canales;
- enviar mensajes;
- insertar enlaces;
- adjuntar archivos;
- leer historial de mensajes;
- usar comandos de aplicacion.

Permisos para canales privados/admin:

- ver canal;
- enviar mensajes;
- leer historial de mensajes;
- adjuntar archivos.

Permisos opcionales, no necesarios al inicio:

- gestionar mensajes, solo si queremos que limpie bitacoras viejas;
- anadir reacciones, si queremos votaciones simples;
- usar emojis externos, si luego se usan iconos de facciones o estados.

Evitaria permisos amplios al principio:

- administrador;
- gestionar servidor;
- expulsar o banear miembros;
- gestionar roles.

## Canales sugeridos

Publicos:

- `hellgames-bitacora`: sucesos narrativos importantes;
- `hellgames-mapa`: mapas de estado publicados por el bot;
- `hellgames-rumores`: informacion parcial y desbloqueos.

Privados/admin:

- `hellgames-admin-log`: registro completo de simulacion;
- `hellgames-assets`: imagenes subidas manualmente para que el bot guarde referencias;
- `hellgames-debug`: pruebas tecnicas y errores.

## Usar imagenes del server por ID

Si subes imagenes a un canal privado de Discord, cada imagen queda en un mensaje
con `channel_id`, `message_id` y un adjunto. El bot puede guardar una ficha asi:

```json
{
  "id": "rex_retrato_01",
  "type": "character_portrait",
  "discord": {
    "guild_id": "123",
    "channel_id": "456",
    "message_id": "789",
    "attachment_index": 0
  },
  "fallback_local": null,
  "tags": ["rex", "participante", "retrato"]
}
```

Ventaja:

- el bot no carga con el peso de todas las imagenes en Discloud;
- puede publicar embeds usando la URL del adjunto;
- podemos cambiar o ampliar assets sin redeploy completo.

Riesgos:

- si borras el mensaje original, el asset puede perderse;
- si el canal deja de ser accesible para el bot, no podra resolver la imagen;
- conviene guardar tambien nombre, tags y descripcion del asset.

## Comandos iniciales

Admin:

- `/hg simular_dia`: avanza un dia o bloque del piloto;
- `/hg render_mapa`: genera mapa de estado;
- `/hg publicar_bitacora`: envia la bitacora al canal publico;
- `/hg registrar_asset`: guarda una imagen subida en `hellgames-assets`;
- `/hg estado_actor`: muestra datos completos de un personaje.

Publicos:

- `/hg bitacora`: muestra ultimo resumen publico;
- `/hg mapa`: muestra mapa publico;
- `/hg personaje`: ficha visible de un personaje;
- `/hg rumores`: rumores desbloqueados.

## Flujo recomendado

1. Crear la aplicacion Hellgames en Discord Developer Portal.
2. Activar bot y copiar token para `.env`.
3. Invitarlo con `bot` + `applications.commands`.
4. Crear canales publicos y privados.
5. Probar comandos solo con el piloto local de 4 casillas.
6. Subir algunas imagenes al canal privado de assets.
7. Registrar sus IDs con el bot.
8. Publicar mapas/bitacoras usando esas referencias.

## Variables de entorno futuras

```txt
DISCORD_TOKEN=
DISCORD_GUILD_ID=
HG_PUBLIC_LOG_CHANNEL_ID=
HG_PUBLIC_MAP_CHANNEL_ID=
HG_ADMIN_LOG_CHANNEL_ID=
HG_ASSET_CHANNEL_ID=
```
