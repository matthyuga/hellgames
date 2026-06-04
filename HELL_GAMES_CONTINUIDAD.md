# Hell Games - Continuidad del proyecto

Documento de arranque para futuras sesiones.

## Identidad del proyecto

Hell Games es un bot de Discord para simular un battle royale narrativo en una
isla viva. El juego mezcla:

- participantes externos;
- lugarenos;
- criaturas;
- guardianes;
- jefes;
- loot;
- recetas;
- conocimientos/libros;
- mapas tacticos con subcasillas;
- bitacora narrativa;
- espectadores de Discord que pueden stalkear, apostar, seguir y descubrir.

## Ruta y GitHub

Ruta local:

```txt
D:\2026\bot discord\bot evento
```

Repositorio GitHub:

```txt
https://github.com/matthyuga/hellgames.git
```

Remote Git:

```txt
origin
```

Rama actual:

```txt
main
```

Comandos utiles:

```powershell
git status --short
git remote -v
git log --oneline -5
```

Ultimos commits conocidos al 2026-06-04:

```txt
35a809f Add live pilot turns and crafting profiles
b41175a Add crafting recipes and island projects
e5ac378 Add weapons catalog
fff36c0 Add resources and map objects catalog
55902ba Add action feed and actor profiles
```

## Estado importante de Git

Al preparar esta continuidad habia cambios locales pendientes de sesiones
recientes. No revertirlos.

Cambios pendientes vistos:

```txt
 M HELL_GAMES_ESTRUCTURA_BASE.md
 M HELL_GAMES_OBJETOS_RECURSOS.md
 M HELL_GAMES_RECETAS_CRAFTING.md
?? BITACORA_SESION_HELL_GAMES_ASSETS_CONOCIMIENTO_2026-06-04.md
?? BITACORA_SESION_HELL_GAMES_CASTING_CRIATURAS_2026-06-04.md
?? HELL_GAMES_CASTING_VISUAL_PERSONAJES.md
?? HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md
?? assets/skills y mats/
?? data/skill_books_and_recipe_knowledge.json
?? scripts/generate_knowledge_guide.py
?? scripts/generate_material_guide.py
?? scripts/generate_weapon_guide.py
```

La carpeta `assets/characters/` esta ignorada por Git. Ahi existen assets
locales importantes que no aparecen en `git status`.

## Documentos que conviene leer primero

Para retomar el proyecto:

1. `README.md`
2. `README_HELLGAMES.md`
3. `HELL_GAMES_GUIA_PILOTO_DISCORD.md`
4. `BITACORA_SESION_HELL_GAMES_ASSETS_CONOCIMIENTO_2026-06-04.md`
5. `BITACORA_SESION_HELL_GAMES_CASTING_CRIATURAS_2026-06-04.md`
6. `HELL_GAMES_CASTING_VISUAL_PERSONAJES.md`
7. `HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md`
8. `HELL_GAMES_OBJETOS_RECURSOS.md`
9. `HELL_GAMES_ARMAS.md`
10. `HELL_GAMES_RECETAS_CRAFTING.md`

## Bot Discord

Archivo principal:

```txt
hellgames.py
```

Configuracion local:

```txt
.env.hellgames
```

No mostrar ni subir `.env.hellgames`; contiene token e IDs.

Arranque:

```powershell
python hellgames.py
```

Despues de cambios en comandos slash:

```txt
/hg owner sync
```

## Comandos clave del piloto vivo

El flujo recomendado ya no es publicar toda la bitacora de 3 dias. El ritmo
principal es turno por turno.

Preparacion:

```txt
/hg admin diagnostico
/hg owner sync
/hg admin publicar_fichas
```

Partida viva:

```txt
/hg admin iniciar_piloto
/hg admin avanzar_turno
/hg admin stalk rex
/hg mapa
/hg bitacora
```

Notas:

- `/hg admin iniciar_piloto` inicia la partida viva sin soltar los 3 dias.
- `/hg admin avanzar_turno` publica una escena.
- `/hg admin stalk <actor>` muestra estado interno, inventario, intereses y
  recetas.
- `/hg admin sandbox` queda como simulacion completa para pruebas tecnicas.

## Piloto actual de 4 casillas

Casillas:

| ID | Nombre |
| --- | --- |
| 1 | Faro de la Vigilia Sagrada |
| 2 | Campamento Raiz Maldita |
| 6 | Circulo de Monolitos |
| 7 | Ruinas del Guardian |

Actores base:

- Rex;
- Renzo Manos Frias;
- Silas Crow;
- Sira;
- Verek;
- Gaviotas de hueso;
- Larvas de raiz;
- Sombras de monolito;
- Custodio del Faro;
- Centinela de Piedra;
- Guardian Juramentado.

## Assets visuales locales

### Personajes

Ruta:

```txt
assets/characters/personajes hellgames
```

Contiene 52 PNG de personajes, muchos con retrato/dialogo y fullbody.

Hoja de contacto creada:

```txt
data/runs/character_contact_sheet.png
```

Documento de casting:

```txt
HELL_GAMES_CASTING_VISUAL_PERSONAJES.md
```

### Criaturas piloto creadas localmente

Ruta:

```txt
assets/characters/personajes hellgames/creature/pilot_creatures
```

Archivos:

```txt
gaviotas_hueso_piloto.png
larvas_raiz_piloto.png
sombras_monolito_piloto.png
centinela_basalto_piloto.png
pilot_creatures_contact_sheet.png
pilot_creatures_manifest.json
```

Estos assets estan bajo `assets/characters/`, por lo tanto estan ignorados por
Git. Si se quieren respaldar, hay que copiarlos/subirlos manualmente o cambiar la
estrategia de versionado.

### Materiales, armas, libros y escritura

Ruta:

```txt
assets/skills y mats
```

Contiene sets visuales generados para:

- materiales;
- armas;
- libros/manuales;
- escritura/documentos.

Segun la bitacora de assets, contiene:

- hojas 4x4;
- recortes `icons_cells`;
- recortes `icons_by_id`;
- manifiestos JSON;
- guias Markdown/PDF;
- scripts generadores.

Esta carpeta pesa aproximadamente 74 MB al 2026-06-04. Decidir con cuidado si se
sube al repo, se ignora, o se respalda por otro medio.

## Estrategia de assets recomendada

Para Discloud y GitHub:

- mantener codigo, docs, JSON y manifiestos en Git;
- mantener imagenes pesadas fuera del bot cuando sea posible;
- subir imagenes al canal `hellgames-assets` de Discord;
- guardar en JSON la URL/ID de Discord;
- el bot usa esas URLs en embeds;
- no cargar todo el peso visual dentro de Discloud.

## Siguiente implementacion probable

La proxima sesion podria seguir uno de estos caminos:

1. Crear `data/character_visual_cast.json` para conectar actores con retrato y
   fullbody.
2. Actualizar embeds de `/hg personaje`, `/hg admin stalk` y
   `/hg admin publicar_fichas` para usar imagenes.
3. Crear `data/items_catalog.json` unificando materiales, armas y conocimiento.
4. Conectar iconos de `icons_by_id` con inventario.
5. Decidir y limpiar la estrategia Git para `assets/skills y mats`.
6. Hacer commit ordenado de documentos/datos/scripts livianos.

## Regla de cuidado

Antes de cualquier commit o limpieza:

```powershell
git status --short
```

No borrar assets ni revertir documentos sin confirmacion del usuario.
