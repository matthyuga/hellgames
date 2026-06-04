# Bitacora de sesion - Hell Games assets, materiales, armas y conocimiento

Fecha: 2026-06-04  
Proyecto: Hell Games / bot Discord de evento  
Ruta real: `D:\2026\bot discord\bot evento`

## Resumen corto

En esta sesion se avanzo desde la documentacion base de materiales, armas,
habilidades y crafting hacia un sistema visual y jugable mucho mas completo.
Se generaron sets de imagenes para materiales, armas, libros/manuales y
objetos de escritura; se separaron los iconos por ID; se crearon guias en
Markdown/PDF; y se documento una logica de conocimiento donde los libros
desbloquean recetas, la escritura transfiere conocimiento y la practica da
dominio real.

La regla principal consolidada fue:

> Los libros desbloquean conocimiento. La practica desbloquea dominio. La
> presion desbloquea experiencia real.

## Fuentes revisadas o usadas

- `HELL_GAMES_ESTRUCTURA_BASE.md`
- `HELL_GAMES_OBJETOS_RECURSOS.md`
- `HELL_GAMES_RECETAS_CRAFTING.md`
- `HELL_GAMES_ARMAS.md`
- `HELL_GAMES_CASILLAS.md`
- `doc_materiales1.md`
- `doc_armas1.md`
- `doc_hability1.md`
- `doc_habilidades2.md`
- `data/prototype_runtime_4.json`
- `data/prototype_island_4.json`

Tambien se reviso `K:\_CodexNexus\README.md` y `K:\_CodexNexus\projects.md`.
El proyecto Hell Games aun no aparece registrado en Nexus.

## 1. Materiales y materias primas

Se genero un set visual de materiales iniciales, organizado en hojas 4x4:

- `assets/skills y mats/hellgames_material_sets/hellgames_materiales_01_supervivencia.png`
- `assets/skills y mats/hellgames_material_sets/hellgames_materiales_02_minerales_metal.png`
- `assets/skills y mats/hellgames_material_sets/hellgames_materiales_03_fibras_alimentos.png`
- `assets/skills y mats/hellgames_material_sets/hellgames_materiales_04_quimica_energia_raros.png`

Se crearon indices y manifiestos:

- `assets/skills y mats/hellgames_material_sets/material_sets_manifest.json`
- `assets/skills y mats/hellgames_material_sets/icons_index.json`
- `assets/skills y mats/hellgames_material_sets/README.md`

Se separaron los iconos:

- `assets/skills y mats/hellgames_material_sets/icons_cells/`
- `assets/skills y mats/hellgames_material_sets/icons_by_id/`

Resultado aproximado:

- 64 celdas recortadas.
- 62 iconos unicos por ID.

## 2. Guia de materiales

Se creo una guia de materiales con jerarquia, usos, fabricacion/procesamiento,
ubicacion en isla completa y uso en piloto de 4 casillas.

Archivos:

- `assets/skills y mats/hellgames_material_sets/guide/GUIA_MATERIALES_HELLGAMES.md`
- `assets/skills y mats/hellgames_material_sets/guide/GUIA_MATERIALES_HELLGAMES.pdf`
- `assets/skills y mats/hellgames_material_sets/guide/material_guide_data.json`
- `assets/skills y mats/hellgames_material_sets/guide/material_icons_contact.png`
- `scripts/generate_material_guide.py`

## 3. Armas

Se genero un set visual de armas, municiones y trampas en cuatro hojas 4x4:

- `assets/skills y mats/hellgames_weapon_sets/hellgames_armas_01_melee_comunes.png`
- `assets/skills y mats/hellgames_weapon_sets/hellgames_armas_02_melee_avanzadas_improvisadas.png`
- `assets/skills y mats/hellgames_weapon_sets/hellgames_armas_03_distancia_municion.png`
- `assets/skills y mats/hellgames_weapon_sets/hellgames_armas_04_fuego_trampas_especiales.png`

Se crearon indices y manifiestos:

- `assets/skills y mats/hellgames_weapon_sets/weapon_sets_manifest.json`
- `assets/skills y mats/hellgames_weapon_sets/icons_index.json`
- `assets/skills y mats/hellgames_weapon_sets/README.md`

Se separaron los iconos:

- `assets/skills y mats/hellgames_weapon_sets/icons_cells/`
- `assets/skills y mats/hellgames_weapon_sets/icons_by_id/`

Resultado:

- 64 celdas recortadas.
- 64 iconos por ID.

## 4. Guia de armas

Se creo una guia de armas con jerarquia, dano/ruido, municion, si son loot o
fabricacion, y ubicaciones sugeridas.

Archivos:

- `assets/skills y mats/hellgames_weapon_sets/guide/GUIA_ARMAS_HELLGAMES.md`
- `assets/skills y mats/hellgames_weapon_sets/guide/GUIA_ARMAS_HELLGAMES.pdf`
- `assets/skills y mats/hellgames_weapon_sets/guide/weapon_guide_data.json`
- `assets/skills y mats/hellgames_weapon_sets/guide/weapon_icons_contact.png`
- `scripts/generate_weapon_guide.py`

## 5. Sistema de libros, habilidades y recetas

Se creo el documento principal:

- `HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md`

Contenido consolidado:

- Capas de conocimiento: `intuicion`, `lectura`, `receta_escrita`, `practica`, `dominio`, `secreto`.
- Habilidades que conviene relacionar con libros: medicina, botanica/herbolaria, quimica, mecanica, electronica/informatica, supervivencia, cocina, trampas, construccion, herreria, cartografia, ocultismo, estrategia y psicologia/negociacion.
- Tipos de documento: `folleto`, `manual_basico`, `guia_intermedia`, `manual_avanzado`, `tratado_experto`, `plano_tecnico`, `diario_npc`, `receta_suelta`, `apunte_incompleto`.
- Materiales de escritura: `papel_suelto`, `cuaderno_mojado`, `cuaderno_seco`, `lapiz`, `lapicera`, `pluma`, `tinta`, `carboncillo`, `tiza`, `sello_cera`, `mapa_en_blanco`, `receta_escrita`.
- Recetas de escritura y copia: `preparar_carboncillo`, `copiar_receta_simple`, `copiar_receta_tecnica`, `crear_apunte_incompleto`, `crear_manual_corto`, `dibujar_mapa_receta`, `falsificar_receta`, `restaurar_documento_mojado`.
- Distribucion sugerida por isla completa y version piloto de 4 casillas.

Se creo el JSON utilizable por el bot:

- `data/skill_books_and_recipe_knowledge.json`

Incluye:

- `asset_sets`
- `knowledge_layers`
- `unlock_modes`
- `writing_logic`
- `writing_materials`
- `books`
- `writing_recipes`
- `pilot_books`

## 6. Logica de escritura

Se definio que `escritura` no tiene que ser una habilidad mayor obligatoria al
inicio. Funciona mejor como microhabilidad de apoyo modificada por:

- `Ciencias`
- `Investigacion`
- `Cartografia`
- `Ocultismo`
- `Mecanica`
- `Medicina`
- la habilidad tecnica relacionada con la receta

Reglas importantes:

- `carbon_vegetal` sirve para marcas grandes, mapas toscos y restaurar papel.
- `carbon_vegetal` puede sustituir al `carboncillo`, pero con baja legibilidad.
- `carboncillo` sirve para apuntes incompletos, mapas y recetas simples toscas.
- `lapiz` sirve para recetas simples y mapas corregibles.
- `lapicera` sirve para copiar rapido, pero puede fallar si esta mojada.
- `pluma` + `tinta` sirve para documentos tecnicos, rituales o legibles.
- `tiza` sirve para paredes/rutas/simbolos, no para conservar recetas en inventario.
- `sello_cera` autentica, pacta, falsifica o protege documentos.

Calidades de receta escrita:

- `tosca`
- `clara`
- `tecnica`
- `codificada`
- `falsa`
- `danada`

## 7. Assets visuales de libros y escritura

Se genero un set visual nuevo:

- `assets/skills y mats/hellgames_knowledge_sets/`

Hojas principales:

- `assets/skills y mats/hellgames_knowledge_sets/hellgames_conocimiento_01_libros_manuales.png`
- `assets/skills y mats/hellgames_knowledge_sets/hellgames_conocimiento_02_escritura_documentos.png`

Indices y manifiestos:

- `assets/skills y mats/hellgames_knowledge_sets/knowledge_sets_manifest.json`
- `assets/skills y mats/hellgames_knowledge_sets/icons_index.json`
- `assets/skills y mats/hellgames_knowledge_sets/README.md`

Iconos separados:

- `assets/skills y mats/hellgames_knowledge_sets/icons_cells/`
- `assets/skills y mats/hellgames_knowledge_sets/icons_by_id/`

Resultado:

- 32 celdas recortadas.
- 32 iconos por ID.

Incluye iconos para:

- manuales medicos, botanicos, mecanicos, electronicos, de trampas, de radio/faro y de ocultismo;
- `papel_suelto`, `cuaderno_mojado`, `cuaderno_seco`, `lapiz`, `lapicera`, `pluma`, `tinta`, `carboncillo`, `tiza`, `sello_cera`, `mapa_en_blanco`;
- `receta_escrita`, `receta_escrita_tecnica`, `apunte_incompleto`, `manual_corto_artesanal`, `receta_falsa`, `receta_suelta`.

## 8. Guia de libros y habilidades

Se creo una guia nueva en Markdown/PDF:

- `assets/skills y mats/hellgames_knowledge_sets/guide/GUIA_LIBROS_HABILIDADES_HELLGAMES.md`
- `assets/skills y mats/hellgames_knowledge_sets/guide/GUIA_LIBROS_HABILIDADES_HELLGAMES.pdf`
- `assets/skills y mats/hellgames_knowledge_sets/guide/knowledge_guide_data.json`
- `assets/skills y mats/hellgames_knowledge_sets/guide/knowledge_icons_contact.png`
- `scripts/generate_knowledge_guide.py`

Contenido:

- regla central de aprendizaje;
- capas de conocimiento;
- version piloto de 4 casillas;
- libros/manuales con habilidades, horas de lectura, desbloqueos y zonas;
- materiales de escritura;
- recetas de escritura/copia;
- hoja contacto de iconos.

Conteo al generar:

- 15 libros/manuales.
- 17 materiales/documentos de escritura.
- 8 recetas de escritura.

## 9. Documentos principales actualizados

Se actualizaron:

- `HELL_GAMES_ESTRUCTURA_BASE.md`
- `HELL_GAMES_OBJETOS_RECURSOS.md`
- `HELL_GAMES_RECETAS_CRAFTING.md`
- `HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md`
- `data/skill_books_and_recipe_knowledge.json`
- `assets/skills y mats/hellgames_knowledge_sets/README.md`

Cambios destacados:

- `HELL_GAMES_ESTRUCTURA_BASE.md` ahora referencia el sistema de libros y el set visual de conocimiento.
- `HELL_GAMES_OBJETOS_RECURSOS.md` ahora incluye la categoria de conocimiento, libros y escritura.
- `HELL_GAMES_RECETAS_CRAFTING.md` ahora incluye una seccion de escritura, libros y transferencia de recetas.
- `HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md` quedo como documento puente entre habilidades, crafting, objetos y assets visuales.

## 10. Validaciones realizadas

Se validaron los JSON con `python -m json.tool`:

- `data/skill_books_and_recipe_knowledge.json`
- `assets/skills y mats/hellgames_knowledge_sets/knowledge_sets_manifest.json`
- `assets/skills y mats/hellgames_knowledge_sets/icons_index.json`
- `assets/skills y mats/hellgames_knowledge_sets/guide/knowledge_guide_data.json`

Tambien se revisaron visualmente:

- hoja de materiales;
- hoja de armas;
- hoja de libros/manuales;
- hoja de escritura/documentos;
- recortes individuales como `pluma.png` y `manual_radio_faro.png`;
- `knowledge_icons_contact.png`.

## 11. Estado de git al final

Estado visto al cierre de la sesion:

```txt
 M HELL_GAMES_ESTRUCTURA_BASE.md
 M HELL_GAMES_OBJETOS_RECURSOS.md
 M HELL_GAMES_RECETAS_CRAFTING.md
?? HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md
?? assets/skills y mats/
?? data/skill_books_and_recipe_knowledge.json
?? scripts/generate_knowledge_guide.py
?? scripts/generate_material_guide.py
?? scripts/generate_weapon_guide.py
```

No se hizo commit.

## 12. Pendientes sugeridos

Pendientes logicos para una proxima sesion:

1. Registrar el proyecto Hell Games en `K:\_CodexNexus\projects.md` si se quiere continuidad central.
2. Crear `data/crafting_recipes.json` desde `HELL_GAMES_RECETAS_CRAFTING.md`.
3. Crear `data/items_catalog.json` unificando materiales, armas, conocimiento y escritura.
4. Conectar `icons_by_id` con embeds o inventario del bot.
5. Decidir si `escritura` queda solo como microhabilidad o si aparece como stat visible avanzada.
6. Crear guias similares para NPCs, zonas/POIs o facciones.
7. Revisar nombres con acentos si el bot necesita IDs estrictamente ASCII y nombres visibles separados.

## 13. Comandos utiles para regenerar guias

```powershell
python scripts/generate_material_guide.py
python scripts/generate_weapon_guide.py
python scripts/generate_knowledge_guide.py
```

## 14. Rutas clave para retomar

- Materiales: `assets/skills y mats/hellgames_material_sets/`
- Armas: `assets/skills y mats/hellgames_weapon_sets/`
- Libros/escritura: `assets/skills y mats/hellgames_knowledge_sets/`
- Documento de conocimiento: `HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md`
- Datos de conocimiento: `data/skill_books_and_recipe_knowledge.json`
- Recetas: `HELL_GAMES_RECETAS_CRAFTING.md`
- Catalogo de objetos: `HELL_GAMES_OBJETOS_RECURSOS.md`
