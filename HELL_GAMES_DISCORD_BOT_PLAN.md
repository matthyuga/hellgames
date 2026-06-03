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

En Discord Developer Portal, dentro de OAuth2 / URL Generator, no hace falta marcar
`identify`, `email`, `guilds`, `guilds.members.read`, `messages.read` ni permisos de
RPC. Para la primera version solo queremos invitar el bot al servidor y registrar
comandos slash.

Bot tab:

- crear/copiar token del bot y guardarlo solo en `.env`;
- `Public Bot`: puede estar apagado si solo se usara en tu server;
- `Requires OAuth2 Code Grant`: apagado para una invitacion normal;
- `Message Content Intent`: apagado si usamos solo slash commands;
- `Server Members Intent`: apagado en la V0;
- `Presence Intent`: apagado en la V0.

Permisos del URL Generator al seleccionar `bot`:

- View Channels;
- Send Messages;
- Embed Links;
- Attach Files;
- Read Message History;
- Use Application Commands.

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

- `hellgames-battleroyale`: canal principal donde ocurre la accion publica;
- `hellgames-bitacora`: resumen ordenado de dias/bloques importantes;
- `hellgames-mapa`: mapas de estado publicados por el bot, idealmente limpio;
- `hellgames-rumores`: informacion parcial y desbloqueos.

Privados/admin:

- `hellgames-admin-log`: registro completo de simulacion;
- `hellgames-assets`: imagenes subidas manualmente para que el bot guarde referencias;
- `hellgames-database`: mensajes estructurados de lore, fichas, rumores o eventos cargables;
- `hellgames-debug`: pruebas tecnicas y errores.

Recomendacion para no mezclar:

- `hellgames-battleroyale` es el teatro: sucesos vivos, escenas, alertas, apuestas importantes.
- `hellgames-mapa` es el tablero: ultima imagen del mapa, posiciones reveladas y mapas tacticos.
- `hellgames-bitacora` es el archivo publico: resumen por bloque/dia, sin tanto ruido.
- `hellgames-assets` es almacenamiento visual: imagenes y adjuntos.
- `hellgames-database` es biblioteca estructurada: texto/JSON/YAML que el bot puede importar.

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

Para no saturar a la gente, conviene usar un solo comando raiz:

```txt
/hg
```

Y debajo usar subcomandos:

```txt
/hg perfil
/hg mapa
/hg observar
/hg admin sandbox
```

Esto mantiene el bot ordenado y permite que `/hg ayuda` muestre solo lo que el usuario
ya tiene desbloqueado.

## Progresion de comandos

La comunidad puede descubrir comandos por nivel de espectador/investigador.
La idea es que al principio vean poco, y con actividad desbloqueen capas mas profundas.

Admin y owner deben poder saltarse estos requisitos durante pruebas.

Regla recomendada:

- usuarios normales respetan nivel, XP y puntos de seguimiento;
- mods/admins pueden usar comandos publicos aunque no tengan nivel;
- owner puede usar todo;
- el bot debe tener un modo para probar "como usuario normal" sin bypass.

### Niveles publicos

| Nivel | Nombre | Desbloquea |
| --- | --- | --- |
| 0 | Espectador | `/hg ayuda`, `/hg perfil`, `/hg bitacora`, `/hg mapa`, `/hg personaje` |
| 1 | Curioso | `/hg mirar`, `/hg rumores`, `/hg guia` |
| 2 | Seguidor | `/hg seguir`, `/hg observar`, `/hg mis_seguidos` |
| 3 | Investigador | `/hg casilla`, `/hg rastros`, `/hg evento` |
| 4 | Espia | `/hg espiar`, `/hg relaciones`, `/hg historial` |
| 5 | Analista | `/hg analizar`, `/hg comparar`, `/hg teorias` |

### XP sugerida

| Accion | XP |
| --- | --- |
| consultar bitacora diaria | 5 |
| mirar mapa | 3 |
| mirar personaje | 4 |
| seguir personaje | 10 |
| participar en votacion | 8 |
| consultar guia desbloqueada | 4 |
| descubrir rumor nuevo | 12 |
| acertar teoria o prediccion futura | 25 |

Limites:

- XP por comando publico puede tener cooldown;
- no conviene dar XP infinita por repetir `/hg mapa`;
- los admins no deberian farmear XP mientras usan bypass.

### Puntos de seguimiento

Los puntos de seguimiento sirven para especializarse en personajes.

Ejemplo:

```txt
/hg seguir sira
```

Costo sugerido:

- seguir personaje: 2 puntos;
- profundizar seguimiento: 4 puntos;
- espiar una escena puntual: 1 punto;
- desbloquear historial parcial: 3 puntos.

Niveles de seguimiento por personaje:

| Nivel | Informacion visible |
| --- | --- |
| 0 | ubicacion solo si esta visible |
| 1 | acciones publicas |
| 2 | estado fisico/emocional aproximado |
| 3 | conversaciones cercanas o rumores asociados |
| 4 | historial parcial y relaciones importantes |
| 5 | motivaciones profundas y secretos parciales |

## Comandos publicos propuestos

Basicos:

- `/hg ayuda`: muestra comandos disponibles para tu nivel;
- `/hg perfil`: muestra nivel, XP, puntos y personajes seguidos;
- `/hg monedas`: muestra Hellcoins actuales;
- `/hg reclamar`: reclama bono diario de Hellcoins;
- `/hg ranking`: ranking de espectadores/investigadores;
- `/hg bitacora`: ultimo resumen publico del evento;
- `/hg mapa`: mapa publico de la isla o del sandbox;
- `/hg personaje <id>`: ficha publica de un personaje;
- `/hg mirar <personaje>`: vistazo superficial;
- `/hg mirar_casilla <id>`: descripcion publica de una casilla;
- `/hg rumores`: rumores desbloqueados;
- `/hg guia <categoria>`: guia parcial de isla, fauna, objetos, heridas, etc.

Seguimiento:

- `/hg seguir <personaje>`: desbloquea seguimiento basico;
- `/hg dejar_seguir <personaje>`: deja de gastar foco en ese personaje;
- `/hg mis_seguidos`: lista personajes seguidos;
- `/hg observar <personaje>`: observacion mejorada segun nivel;
- `/hg profundizar <personaje>`: sube nivel de seguimiento si hay puntos;
- `/hg historial <personaje>`: historial visible segun nivel;
- `/hg relaciones <personaje>`: relaciones aproximadas visibles;
- `/hg espiar <personaje>`: escena puntual con riesgo/costo;
- `/hg rastros <casilla>`: pistas visibles en una zona;
- `/hg analizar <personaje>`: resumen de patron, sospechas y cambios.

Comunidad:

- `/hg votar`: votacion activa;
- `/hg apuestas`: lista apuestas abiertas;
- `/hg apostar <apuesta> <opcion> <cantidad>`: apuesta Hellcoins;
- `/hg mis_apuestas`: muestra apuestas activas del usuario;
- `/hg mercado`: muestra gastos disponibles con Hellcoins;
- `/hg comprar <opcion>`: compra pista, seguimiento o utilidad;
- `/hg teoria <texto>`: registra una teoria del usuario;
- `/hg comparar <a> <b>`: compara dos personajes si se tiene nivel;
- `/hg evento`: explica el evento publico actual.

## Comandos admin propuestos

Admin:

- `/hg simular_dia`: avanza un dia o bloque del piloto;
- `/hg sandbox`: corre el sandbox de 3 dias o un bloque de prueba;
- `/hg render_mapa`: genera mapa de estado;
- `/hg publicar_bitacora`: envia la bitacora al canal publico;
- `/hg registrar_asset`: guarda una imagen subida en `hellgames-assets`;
- `/hg estado_actor`: muestra datos completos de un personaje.

Mas admin:

- `/hg admin reset_demo`: reinicia el sandbox local;
- `/hg admin set_estado <actor>`: cambia HP, hambre, sed, miedo, etc.;
- `/hg admin mover <actor> <casilla> <micro>`: mueve un actor manualmente;
- `/hg admin dar_item <actor> <item>`: entrega un item;
- `/hg admin quitar_item <actor> <item>`: quita un item;
- `/hg admin publicar_mapa`: publica mapa generado;
- `/hg admin log`: muestra ultimo log tecnico;
- `/hg admin xp <usuario> <cantidad>`: ajusta XP;
- `/hg admin puntos <usuario> <cantidad>`: ajusta puntos de seguimiento;
- `/hg admin desbloquear <usuario> <comando>`: desbloqueo manual.
- `/hg admin apuesta_crear`: crea una apuesta vinculada a una memoria/evento;
- `/hg admin apuesta_cerrar`: cierra entradas de una apuesta;
- `/hg admin apuesta_resolver`: resuelve apuesta y paga Hellcoins;
- `/hg admin monedas <usuario> <cantidad>`: ajusta Hellcoins;
- `/hg admin transacciones`: revisa movimientos economicos.

Owner:

- `/hg owner config`: muestra configuracion sensible no secreta;
- `/hg owner set_canal <tipo> <canal>`: configura canales;
- `/hg owner sync`: sincroniza slash commands;
- `/hg owner backup`: exporta datos locales;
- `/hg owner importar_assets`: reindexa assets de un canal;
- `/hg owner modo_bypass <on/off>`: activa/desactiva bypass global de prueba.

## Version 0 recomendada

No implementaria todo de golpe. Primera version real:

Publicos:

- `/hg ayuda`;
- `/hg perfil`;
- `/hg monedas`;
- `/hg reclamar`;
- `/hg bitacora`;
- `/hg mapa`;
- `/hg personaje`;
- `/hg mirar`;
- `/hg apuestas`;
- `/hg apostar`;
- `/hg seguir`;
- `/hg observar`;
- `/hg rumores`.

Admin/owner:

- `/hg admin sandbox`;
- `/hg admin render_mapa`;
- `/hg admin publicar_bitacora`;
- `/hg admin estado_actor`;
- `/hg admin reset_demo`;
- `/hg admin apuesta_crear`;
- `/hg admin apuesta_resolver`;
- `/hg admin monedas`;
- `/hg owner sync`;
- `/hg owner set_canal`.

Con eso ya se puede probar el loop completo:

```txt
admin corre sandbox -> bot genera bitacora/mapa -> publica -> usuarios miran/siguen/observan -> ganan XP
```

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
