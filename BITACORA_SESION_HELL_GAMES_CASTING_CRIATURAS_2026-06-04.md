# Bitacora de sesion - Hell Games casting visual y criaturas piloto

Fecha: 2026-06-04  
Proyecto: Hell Games / bot Discord de evento  
Ruta real: `D:\2026\bot discord\bot evento`

## Resumen corto

En esta sesion se reviso la carpeta de personajes visuales generados para
Hell Games, se hizo un primer casting de candidatos para participantes,
lugarenos, criaturas, guardianes y jefes, y se crearon assets locales para las
criaturas basicas del piloto de 4 casillas.

Tambien se penso como hacer que el juego se vea mas vistoso en Discord:
embeds con retrato, fullbody, inventario con iconos, stalk privado, escenas
publicas, bestiario, mapa tactico y estados compactos.

## Carpeta analizada

```txt
assets/characters/personajes hellgames
```

Resultado visto:

- 52 PNG en total;
- muchos pares `dialogue/closeup` + `fullbody`;
- estilo general anime/fantasy oscuro;
- varios candidatos fuertes para participantes y campeones;
- una criatura ya existente: humanoide infectado por parasito/hongo;
- una jefa eventual ya existente: guerrera momia solar.

## Hoja de contacto creada

Para ver todos los personajes juntos se genero:

```txt
data/runs/character_contact_sheet.png
```

Es un archivo temporal dentro de `data/runs`, util para inspeccion visual local.

## Documento de casting creado

Se creo:

```txt
HELL_GAMES_CASTING_VISUAL_PERSONAJES.md
```

Contenido principal:

- lectura general del set visual;
- candidatos para personajes actuales del piloto;
- candidatos nuevos con nombres propuestos;
- propuesta de criaturas y guardian del piloto;
- modelo inicial de inventario/loot por slots;
- ideas para que Discord parezca mas juego;
- siguiente paso tecnico sugerido: `data/character_visual_cast.json`.

## Casting recomendado para el piloto

Propuesta rapida:

| Rol piloto | Personaje visual |
| --- | --- |
| Rex | `beid-warrior-*` |
| Renzo Manos Frias | `menks_warrior_*` |
| Silas Crow | `dyla_*` |
| Sira | `blue-haired-woman-*` o `elfica_*` |
| Verek | `whip_warrior_*` |
| Criatura evento | `parasite_humanoid_*` |
| Jefe futuro | `guerrera_momia_solar_*` |
| Guardian nuevo | El Centinela de Basalto |

## Nombres nuevos propuestos

Algunos nombres propuestos para personajes visuales fuertes:

- `chamana_venenista_*`: Nara Sibil;
- `guerrera_lagarto_*`: Karra Diente Verde;
- `guerrera_aracnida_*`: Aracne Veyra;
- `guerrera_fuego*`: Brasa Nox;
- `huesa_*`: Huesa de Cal;
- `pandora_feather_*`: Pandora Pluma Negra;
- `mirya_*`: Mirya del Sombrero Negro;
- `tyria_*`: Tyria Corte Rojo;
- `jas_warrior_*`: Jaska Garra Blanca;
- `fantz_ghost_warrior_*`: Fantz, la Novia del Pozo;
- `guerrero_rojo_*`: Roan Escarlata;
- `whip_warrior_*`: Velka del Latigo.

## Inventario y loot

Se propuso un modelo simple para V0:

- `slots_base`: 6;
- `carry_weight_base`: 10;
- equipo: 2 manos + cuerpo + accesorio;
- objetos pequenos pueden stackear;
- objetos largos/pesados ocupan mas slots;
- objetos enormes como barco, generador, vehiculo o monoriel no van al
  inventario: quedan como estado de zona.

Modificadores sugeridos:

- `mochila_reparada`: +4 slots;
- `bolsa_trueque`: +3 slots para objetos pequenos;
- `fuerza_alta`: +2 peso;
- `herido`: -2 peso;
- criaturas y guardianes usan reglas especiales.

## Presentacion recomendada en Discord

Embeds principales sugeridos:

- ficha de personaje;
- stalk privado;
- escena publica;
- loot encontrado;
- receta desbloqueada;
- mapa tactico;
- evento de amenaza;
- bestiario/database.

Elementos visuales:

- `embed.set_thumbnail` para retrato/dialogo;
- `embed.set_image` para fullbody, mapa o escena;
- colores por tipo: participante rojo, lugareno azul, criatura morado,
  guardian naranja, jefe dorado/negro;
- botones persistentes: `Stalk`, `Inventario`, `Rumor`, `Mapa`, `Seguir`;
- inventario con iconos de `icons_by_id`;
- barras compactas: `HP 82 | Sed 44 | Miedo 61`;
- rarezas: comun, poco comun, raro, epico, legendario, maldito.

## Criaturas creadas en esta sesion

Se intento usar generacion de imagen con prompts de concept art, pero el sistema
bloqueo los prompts incluso siendo criaturas no humanas. Para no detener el
avance, se crearon assets locales con Pillow en estilo icon/concept asset.

Carpeta:

```txt
assets/characters/personajes hellgames/creature/pilot_creatures
```

Archivos creados:

```txt
gaviotas_hueso_piloto.png
larvas_raiz_piloto.png
sombras_monolito_piloto.png
centinela_basalto_piloto.png
pilot_creatures_contact_sheet.png
pilot_creatures_manifest.json
```

Roles:

| ID | Nombre | Tipo | Casilla |
| --- | --- | --- | --- |
| `gaviotas_hueso` | Gaviotas de hueso | criatura | 1 Faro |
| `larvas_raiz` | Larvas de raiz | criatura | 2 Campamento |
| `sombras_monolito` | Sombras de monolito | criatura | 6 Monolitos |
| `centinela_basalto` | El Centinela de Basalto | guardian | 7 Ruinas |

Nota: son PNG transparentes y pesan poco. Sirven para embeds, bestiario,
eventos, mapas o database. No son ilustraciones anime complejas; son assets
locales estilizados para avanzar.

## Manifiesto creado

```txt
assets/characters/personajes hellgames/creature/pilot_creatures/pilot_creatures_manifest.json
```

Incluye:

- ID;
- nombre visible;
- tipo;
- casilla;
- rol;
- ruta de imagen;
- usos sugeridos.

Fue validado con:

```powershell
python -m json.tool "assets\characters\personajes hellgames\creature\pilot_creatures\pilot_creatures_manifest.json"
```

## Estado de Git

Al final de la sesion habia cambios pendientes de la sesion anterior y cambios
nuevos de esta sesion.

Se observo que `assets/characters/` esta ignorado por `.gitignore`, por lo que
las criaturas creadas no aparecen en `git status` ni se suben al repo por defecto.

Estado visto durante la sesion:

```txt
 M HELL_GAMES_ESTRUCTURA_BASE.md
 M HELL_GAMES_OBJETOS_RECURSOS.md
 M HELL_GAMES_RECETAS_CRAFTING.md
?? BITACORA_SESION_HELL_GAMES_ASSETS_CONOCIMIENTO_2026-06-04.md
?? HELL_GAMES_CASTING_VISUAL_PERSONAJES.md
?? HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md
?? assets/skills y mats/
?? data/skill_books_and_recipe_knowledge.json
?? scripts/generate_knowledge_guide.py
?? scripts/generate_material_guide.py
?? scripts/generate_weapon_guide.py
```

No se hizo commit en esta sesion para no mezclar cambios grandes de otra sesion
sin confirmacion.

## Pendientes sugeridos

1. Decidir si se hace commit de los documentos/assets pendientes.
2. Crear `data/character_visual_cast.json` para conectar actores con retrato y
   fullbody.
3. Decidir casting definitivo de Rex, Renzo, Silas, Sira y Verek.
4. Conectar embeds del bot con `character_visual_cast.json`.
5. Conectar inventario con iconos de materiales, armas y libros.
6. Decidir si las criaturas generadas localmente son suficientes para V0 o si se
   reemplazan luego por ilustraciones mas elaboradas.
7. Crear version mejorada del Centinela de Basalto si se quiere un guardian mas
   impresionante para el piloto.

## Rutas clave para retomar

```txt
HELL_GAMES_CASTING_VISUAL_PERSONAJES.md
data/runs/character_contact_sheet.png
assets/characters/personajes hellgames/creature/pilot_creatures/
assets/characters/personajes hellgames/creature/pilot_creatures/pilot_creatures_manifest.json
```
