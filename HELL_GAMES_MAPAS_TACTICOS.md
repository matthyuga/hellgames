# Hell Games - Mapas tacticos por escenario

Este documento define como podria funcionar un segundo nivel de mapa dentro de
cada una de las 25 zonas de la isla.

La isla principal sigue siendo el mapa estrategico:

```text
Casilla 1 a 25 = zona general de la isla.
```

Cada zona puede tener un mapa tactico propio:

```text
Escenario 1 / Faro de la Vigilia Sagrada = mapa interno con casillas pequeñas.
```

## 1. Idea base

Cada escenario puede tener un mapa estilo battle map, visto desde arriba, con
una grilla clara. En esa grilla se pueden colocar puntos, iconos o fichas para
mostrar ubicaciones exactas:

- participantes;
- lugareños;
- criaturas;
- loot visible;
- cuerpos;
- trampas;
- refugios;
- fuego, humo, ruido o rastros.

Esto permitiria que el bot diga:

```text
Mara esta en Faro de la Vigilia Sagrada, coordenada D6.
Varek esta oculto en F3.
Una criatura se mueve por el borde norte.
```

## 2. No todos los mapas necesitan la misma cantidad de casillas

Conviene que el tamaño varie segun el escenario.

Recomendacion:

| Tipo de escenario | Tamaño sugerido | Uso |
| --- | --- | --- |
| Pequeño | 8x8 | cabaña, torre, refugio, sala cerrada |
| Medio | 10x10 o 12x12 | granja, templo, puerto pequeño |
| Grande | 14x14 o 16x16 | bosque, pantano, ruinas, base militar |
| Muy grande | 20x20 | volcan, cañon, bastion, jungla |
| Especial | varias capas | interiores, sotanos, tuneles, edificios |

No hace falta que todas las zonas sean uniformes. Lo importante es que cada
mapa tenga coordenadas estables.

## 3. Escala recomendada

Para simplificar:

```text
1 casilla tactica = 1 posicion jugable.
```

No hace falta comprometerse al principio con metros exactos. Si mas adelante
queremos combate tactico, podemos usar:

```text
1 casilla = 1.5 metros / 5 pies.
```

Pero para la simulacion narrativa alcanza con:

```text
A1, A2, B1, B2...
```

## 4. Dos versiones por mapa

Para cada escenario conviene tener dos imagenes:

```text
mapa limpio: sin fichas, sin nombres, sin personajes
mapa con grilla: igual, pero con casillas visibles
```

Y una tercera version generada por el bot cuando haga falta:

```text
mapa de estado: grilla + puntos de personajes + nombres visibles
```

No conviene dibujar los puntos directamente en la imagen base. Mejor que el bot
los agregue encima, asi puede actualizarlos sin regenerar el mapa.

## 5. Capas de informacion

El mismo mapa puede tener capas distintas.

### Vista publica

Solo muestra lo que la transmision permite ver:

- personajes detectados;
- ruido importante;
- humo;
- combate visible;
- ubicaciones reveladas.

### Vista admin

Muestra todo:

- todos los participantes;
- NPCs ocultos;
- criaturas;
- trampas;
- loot;
- rastros;
- zonas bloqueadas.

### Vista de personaje

Muestra solo lo que ese personaje sabe o percibe:

- su posicion;
- zonas exploradas;
- enemigos detectados;
- rastros cercanos;
- puntos de interes recordados.

## 6. Colores sugeridos para puntos

| Color | Significado |
| --- | --- |
| Rojo | participante vivo |
| Azul | lugareño o NPC neutral |
| Morado | criatura |
| Amarillo | loot importante |
| Naranja | fuego, ruido o peligro activo |
| Verde | refugio, medicina o zona segura |
| Blanco | rastro, pista o señal |
| Negro | muerto, cuerpo o zona anulada |

Si hay muchos personajes, el punto puede tener numero y el nombre va en una
leyenda lateral o debajo del mapa.

## 7. Datos que necesita el bot

Cada mapa tactico deberia tener una ficha de datos:

```json
{
  "scenario_id": 1,
  "name": "Faro de la Vigilia Sagrada",
  "grid_width": 12,
  "grid_height": 12,
  "base_image": "assets/tactical_maps/scenario_01_clean.png",
  "grid_image": "assets/tactical_maps/scenario_01_grid.png",
  "blocked_cells": ["A1", "A2", "B1"],
  "poi": [
    {"id": "faro", "name": "Torre del faro", "cells": ["F5", "F6", "G5", "G6"]},
    {"id": "casa", "name": "Casa del cuidador", "cells": ["I7", "J7"]},
    {"id": "rocas", "name": "Rocas del acantilado", "cells": ["B9", "C9"]}
  ]
}
```

Y cada personaje tendria:

```json
{
  "character_id": "mara",
  "scenario_id": 1,
  "cell": "D6",
  "hidden": false,
  "last_seen_cell": "D6"
}
```

## 8. Como generarlos sin perder precision

La mejor forma no es pedirle a la IA que dibuje una grilla perfecta.

Flujo recomendado:

1. Generar o crear el arte del mapa limpio desde arriba.
2. Definir tamaño de grilla: por ejemplo 12x12.
3. Dibujar la grilla encima con Python/Pillow.
4. Guardar `clean`, `grid` y `admin_overlay`.
5. El bot dibuja puntos y nombres sobre la version con grilla.

Asi el arte puede ser bonito y la grilla siempre queda matematicamente precisa.

## 9. Priorizacion

No hace falta crear 25 mapas tacticos de golpe.

Primera tanda recomendada:

1. `13 - Torre Centinela`: objetivo final y pruebas de posiciones.
2. `2 - Campamento Raíz Maldita`: zona simple para probar movimiento.
3. `5 - Puerto del Navegante`: pasarelas, agua y bloqueos.
4. `11 - Pantano de los Olvidados`: terreno dificil y ocultamiento.
5. `19 - Estación Militar`: interiores, tecnologia y vigilancia.

Con esos cinco mapas se prueban casi todos los problemas importantes:

- espacios abiertos;
- interiores;
- caminos estrechos;
- agua;
- zonas bloqueadas;
- visibilidad;
- refugios;
- combate;
- ocultamiento.

## 10. Decision de diseño

Si hacemos mapas tacticos, el sistema de ubicacion deberia tener dos niveles:

```text
macro_ubicacion = casilla 1 a 25
micro_ubicacion = coordenada dentro del mapa tactico
```

Ejemplo:

```text
Mara:
  macro: 5, Puerto del Navegante
  micro: H4, pasarela norte
```

Esto permite narracion simple para el publico y precision para el bot.

## 11. Mapas tacticos creados

Primera pasada creada:

```text
25 escenarios
Grilla uniforme 14x14
Coordenadas A1 a N14
```

Carpeta:

```text
assets/tactical_maps/
```

Cada escenario tiene:

```text
scenario_XX_clean.png
scenario_XX_grid_14x14.png
scenario_XX_state_demo.png
scenario_XX_tactical.json
```

Indice general:

```text
assets/tactical_maps/manifest_tactical_maps.json
assets/tactical_maps/contact_sheet_tactical_maps.png
```

Datos tecnicos:

- grilla: 14x14 en todos los mapas;
- coordenadas: A1 a N14;
- celda: 100 px en la version normalizada;
- tamaño normalizado: 1400x1400 px;
- uso: localizacion exacta, puntos de personajes, POI, rastros y eventos.

Puntos de interes iniciales:

- Cada `scenario_XX_tactical.json` incluye una primera lista de `poi`.
- Esos POI son orientativos y conviene revisarlos manualmente antes de
  convertirlos en canon estricto.

Las imagenes limpias no tienen grilla ni fichas. La grilla fue agregada por
script, no generada dentro del arte, para mantener coordenadas precisas.

Nota de revision:

- `Campamento Raíz Maldita` y `Jungla de Bambú Diabólico` quedaron oscuros en
  esta primera pasada. Funcionan para prototipo, pero son candidatos a
  regenerar si se busca maxima legibilidad.
