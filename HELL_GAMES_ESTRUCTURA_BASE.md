# Hell Games - Estructura base implementable

Este documento es la base canonica para empezar a experimentar con el bot.
Los documentos `doc*.md` siguen siendo biblioteca de ideas, ejemplos y material
narrativo. Cuando una regla pase a implementacion, deberia quedar resumida aca
o en un catalogo de datos.

## 1. Objetivo del juego

Hell Games es una simulacion narrativa de battle royale en Discord.

La isla tiene 25 casillas. Varios NPC participantes despiertan en ella,
exploran, sobreviven, se enfrentan, forman alianzas, roban, negocian y buscan
escapar. La comunidad observa la transmision, consulta personajes, comenta,
apuesta o influye de forma limitada.

Objetivo principal de los participantes:

- sobrevivir hasta encontrar una ruta de escape;
- reunir estrellas o recursos clave;
- llegar a la torre del helipuerto en la casilla 13;
- escapar antes del cierre de la temporada.

## 2. Version experimental inicial

Para no intentar construir todo de golpe, la primera version jugable deberia
ser pequena pero viva.

Alcance recomendado:

- 25 casillas definidas, pero solo 8 a 10 con eventos ricos al principio;
- 12 NPC participantes;
- 6 NPC lugarenos o especiales;
- 8 criaturas o amenazas ambientales;
- 40 objetos iniciales;
- 15 armas iniciales;
- 12 habilidades principales;
- simulacion por ticks;
- resumen publico diario;
- bitacora privada de eventos;
- respaldo diario en Discord.

Queda fuera del primer prototipo:

- combate demasiado tactico;
- crafting profundo;
- economia compleja;
- decenas de estados corporales;
- IA generativa libre para cada decision;
- rutas de escape demasiado numerosas.

## 3. Capas del sistema

### 3.1 Estado vivo

Vive en SQLite dentro del bot.

Contiene:

- personajes;
- ubicaciones;
- estados fisicos y mentales;
- inventarios;
- relaciones;
- loot por casilla;
- eventos pendientes;
- clima;
- dia y hora de juego.

### 3.2 Catalogos

Viven como JSON, YAML o tablas SQLite semilla.

Contienen:

- mapa;
- casillas;
- armas;
- objetos;
- materiales;
- criaturas;
- habilidades;
- tipos de evento;
- assets visuales.

### 3.3 Narracion

Vive en Discord y en bitacoras compactas.

Contiene:

- anuncios publicos;
- rumores;
- escenas importantes;
- cierres de dia;
- muertes;
- descubrimientos;
- snapshots resumidos.

## 4. Canales de Discord

Canales publicos o visibles:

- `#hell-games-transmision`: eventos importantes y escenas narrativas.
- `#hell-games-rumores`: senales parciales por zona.
- `#hell-games-observatorio`: consultas, embeds y comandos de espectadores.

Canales privados:

- `#hell-games-admin-log`: log tecnico y eventos internos importantes.
- `#hell-games-backups`: snapshots diarios recuperables.
- `#hell-games-assets`: indice o mensajes raiz de assets.
- `#hell-assets-npcs`: imagenes de NPCs.
- `#hell-assets-armas`: imagenes de armas.
- `#hell-assets-objetos`: imagenes de objetos.
- `#hell-assets-criaturas`: imagenes de criaturas.

## 5. Entidades principales

### 5.1 Participante

Campos minimos:

- `id`
- `nombre`
- `tipo`: participante
- `estado`: vivo, herido, inconsciente, muerto, escapado
- `casilla_id`
- `salud`
- `hambre`
- `sed`
- `energia`
- `moral`
- `miedo`
- `estrellas`
- `personalidad`
- `objetivo_actual`
- `plan_actual`
- `asset_id`

Memoria compacta:

- 3 a 8 recuerdos importantes;
- ultima amenaza percibida;
- relacion dominante con otros personajes;
- resumen psicologico del ultimo dia.

### 5.2 Lugareno

NPC no participante que habita la isla.

Campos minimos:

- `id`
- `nombre`
- `casilla_base`
- `movilidad`: fijo, local, errante
- `rol`: comerciante, medico, guia, enemigo, informante, ritualista
- `agenda`
- `secreto`
- `confianza_base`
- `asset_id`

### 5.3 Criatura

Amenaza o presencia no humana.

Campos minimos:

- `id`
- `nombre`
- `casilla_actual`
- `habitat`
- `agresividad`
- `percepcion`
- `ruido`
- `olor`
- `horario_activo`
- `loot_posible`
- `asset_id`

### 5.4 Casilla

Campos minimos:

- `id`: 1 a 25
- `nombre`
- `bioma`
- `peligro_base`: 1 a 5
- `recursos_comunes`
- `recursos_raros`
- `eventos_posibles`
- `conexiones`
- `secreto`
- `asset_id`

### 5.5 Objeto

Campos minimos:

- `id`
- `nombre`
- `tipo`
- `rareza`
- `peso`
- `slots`
- `durabilidad`
- `usos`
- `ruido`
- `valor_narrativo`
- `asset_id`

### 5.6 Arma

Campos minimos:

- `id`
- `nombre`
- `tipo`
- `rareza`
- `dano`
- `ruido`
- `riesgo`
- `durabilidad`
- `municion_tipo`
- `habilidad_relacionada`
- `efecto_especial`
- `asset_id`

## 6. Mapa inicial

La casilla 13 es el centro objetivo: Torre Centinela.

Estructura 5x5 sugerida:

| ID | Zona |
| --- | --- |
| 1 | Faro de la Vigilia Sagrada |
| 2 | Campamento Raíz Maldita |
| 3 | Minas de Hierro |
| 4 | Cascada de los Susurros |
| 5 | Puerto del Navegante |
| 6 | Círculo de Monolitos |
| 7 | Ruinas del Guardián |
| 8 | Pradera Valle del Viento |
| 9 | Templo de las Hojas Carmesí |
| 10 | Bastión del Acantilado |
| 11 | Pantano de los Olvidados |
| 12 | Sector X |
| 13 | Torre Centinela |
| 14 | Granja Sangrienta |
| 15 | Templo del Sol |
| 16 | Costa del Naufragio Negro |
| 17 | Templo de la Luna |
| 18 | Cañón Partido |
| 19 | Estación Militar |
| 20 | Observatorio Militar |
| 21 | Muelle Aguas Rojas |
| 22 | Pueblo Nevado |
| 23 | Jungla de Bambú Diabólico |
| 24 | Bastión Duna Seca |
| 25 | Volcán Ceniza Durmiente |

## 7. Loop de simulacion

### Tick corto

Frecuencia recomendada: cada 15 a 30 minutos.

Hace:

- avanzar acciones actuales;
- mover algunos NPCs;
- resolver hambre, sed y energia;
- generar encuentros menores;
- registrar hechos internos;
- publicar solo eventos relevantes.

### Tick largo

Frecuencia recomendada: cada 6 horas de juego o por bloque del dia.

Hace:

- actualizar clima;
- resolver planes de NPCs;
- mover criaturas;
- generar rumores;
- degradar rastros;
- refrescar loot limitado.

### Cierre diario

Frecuencia recomendada: una vez por dia real.

Hace:

- compactar eventos;
- actualizar memorias;
- limpiar cache temporal;
- guardar snapshot;
- publicar cronica del dia;
- preparar el dia siguiente.

## 8. Regla de oro de datos

Separar siempre hecho, estado y narracion.

Hecho:

```json
{"dia":3,"hora":"noche","actor":"mara","accion":"mover","de":8,"a":9}
```

Estado:

```json
{"actor":"mara","casilla":9,"energia":42,"miedo":61}
```

Narracion:

```text
Mara cruzo la pradera de noche. Algo la siguio desde los arboles.
```

El bot calcula con hechos y estados. Discord muestra narracion.

## 9. Comandos iniciales

Comandos publicos para espectadores:

- `/hell_estado`
- `/hell_ver_personaje nombre`
- `/hell_ver_casilla id`
- `/hell_top`
- `/hell_rumores`
- `/hell_cronica dia`

Comandos privados/admin:

- `/hell_tick`
- `/hell_cerrar_dia`
- `/hell_snapshot`
- `/hell_restaurar_snapshot`
- `/hell_crear_npc`
- `/hell_mover_npc`
- `/hell_dar_objeto`
- `/hell_publicar_evento`

## 10. Documentos actuales como fuente

Uso recomendado de los documentos existentes:

- `HELL_GAMES_CASILLAS.md`: documento canonico inicial de escenarios por casilla.
- `HELL_GAMES_MAPAS_TACTICOS.md`: diseño de mapas internos con grilla por escenario.
- `doc1.md`: vision amplia, percepcion, loop, comandos, combate y MVP.
- `doc2.md`: version con NPCs autonomos y espectadores.
- `doc_map1.md`: base de las 25 casillas.
- `doc_map_npc1.md`: lore por casilla, tipos de NPC y rutas secretas.
- `doc_map_npc2.md`: mochila, objetos, NPC participantes y rutas extra.
- `doc_npcs1.md`: filosofia de NPCs vivientes, confianza y facciones.
- `doc_hability1.md`: tabla inicial de habilidades y parametros.
- `doc_habilidades2.md`: aprendizaje, libros y habilidades avanzadas.
- `HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md`: sistema consolidado de libros, documentos, recetas escritas y desbloqueo de conocimiento.
- `assets/skills y mats/hellgames_knowledge_sets/`: iconos de libros, manuales, escritura y recetas transferibles.
- `doc_armas1.md`: catalogo base de armas.
- `doc_materiales1.md`: materiales, animales, recursos y transformaciones.
- `doc_esces.md`: rastros, olor e higiene como mecanica opcional.

## 11. Prioridad de implementacion

Orden sugerido:

1. Crear bot separado de Hell Games.
2. Crear SQLite con tablas basicas.
3. Cargar catalogo de mapa y NPCs semilla.
4. Implementar comando `/hell_estado`.
5. Implementar simulacion de un tick.
6. Implementar embeds de personaje y casilla.
7. Implementar bitacora privada.
8. Implementar cierre diario y snapshot.
9. Agregar assets visuales desde Discord.
10. Expandir combate, loot y criaturas.

## 12. Decision actual

Los documentos actuales estan bien como laboratorio creativo, pero no conviene
programar directamente desde ellos. Para implementar, este archivo debe actuar
como contrato inicial. Cada sistema nuevo debe tener:

- datos minimos;
- reglas simples;
- comandos afectados;
- como se guarda;
- como se muestra en Discord;
- que queda fuera del primer prototipo.

## 13. Bot y referencia tecnica

Nombre del bot: **Hellgames**.

Referencia local existente:

- MarvaBot vive en `D:\2026\bot discord\discordbot`.
- Es un bot de moderacion/honeypot separado.
- No conviene mezclar Hellgames dentro de MarvaBot.
- Si conviene reutilizar su estructura tecnica como plantilla.

Piezas reutilizables de MarvaBot:

- Python con `discord.py`.
- Variables de entorno con `python-dotenv`.
- SQLite en carpeta `data/`.
- Slash commands con `bot.tree.command`.
- Sincronizacion de comandos por `DISCORD_GUILD_ID`.
- Embeds simples para respuestas.
- Script PowerShell de empaquetado para Discloud.
- `discloud.config`.
- `.env.example` separado del `.env` real.
- `.gitignore` ignorando `.env`, `data/`, `logs/`, `dist/` y `__pycache__/`.

Piezas que Hellgames deberia cambiar:

- Token propio: `HELLGAMES_TOKEN`.
- Base de datos propia: `data/hellgames.sqlite3`.
- Config propia: `.env.hellgames`.
- Main propio: `hellgames.py`.
- Discloud config con `NAME=Hellgames` y `MAIN=hellgames.py`.
- Permisos mas orientados a canales, embeds, adjuntos, historial y comandos.

Estructura inicial recomendada:

```text
hellgames.py
requirements.txt
discloud.config
.env.hellgames.example
README_HELLGAMES.md
data/
  hellgames.sqlite3
scripts/
  package_hellgames_discloud.ps1
catalogs/
  map.json
  npcs.json
  items.json
  weapons.json
  skills.json
```

Decision: Hellgames debe ser un bot nuevo, separado de MarvaBot, pero puede
nacer copiando el esqueleto tecnico de MarvaBot y reemplazando la logica de
moderacion por la simulacion narrativa del evento.

