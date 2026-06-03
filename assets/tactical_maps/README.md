# Hell Games - Tactical Maps

Mapas internos por escenario para ubicar personajes con coordenadas precisas.

Primera pasada:

```text
25 carpetas scenario_XX_nombre/
```

Cada carpeta contiene:

- `scenario_XX_clean.png`: mapa limpio sin grilla.
- `scenario_XX_grid_14x14.png`: mapa con grilla tactica A1 a N14.
- `scenario_XX_state_demo.png`: ejemplo con puntos y nombres.
- `scenario_XX_tactical.json`: datos de grilla y POI iniciales.

Archivos generales:

- `manifest_tactical_maps.json`: indice de los 25 mapas.
- `contact_sheet_tactical_maps.png`: hoja de contacto para revision visual.

Datos tecnicos:

- Grilla uniforme: 14x14.
- Coordenadas: A1 a N14.
- Tamaño normalizado: 1400x1400 px.
- Tamaño de celda: 100 px.

Flujo recomendado:

1. Usar `clean` como base visual.
2. Usar `grid` para vistas publicas o admin.
3. Generar vistas de estado encima de `grid`.
4. Guardar ubicaciones en formato `scenario_id + cell`.
