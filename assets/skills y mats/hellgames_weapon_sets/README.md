# Hell Games - Sets de armas

Imagenes generadas para armas, municion, trampas y armas especiales del juego.

Fuentes revisadas:

- `HELL_GAMES_ARMAS.md`
- `doc_armas1.md`
- `HELL_GAMES_RECETAS_CRAFTING.md`
- `data/prototype_runtime_4.json`

## Archivos derivados

- `icons_cells/`: 64 PNG separados, uno por cada celda exacta de las hojas.
- `icons_by_id/`: 64 PNG unicos por ID de arma, municion o trampa.
- `icons_index.json`: indice de celdas e iconos por ID.
- `guide/GUIA_ARMAS_HELLGAMES.md`: guia editable en Markdown.
- `guide/GUIA_ARMAS_HELLGAMES.pdf`: guia visual en PDF.
- `guide/weapon_guide_data.json`: datos estructurados de jerarquia, dano, ruido, fabricacion y ubicaciones.

Orden de celdas: izquierda a derecha, arriba hacia abajo.

## 01 - Melee comunes

Archivo: `hellgames_armas_01_melee_comunes.png`

| Celda | ID sugerido | Nombre |
| --- | --- | --- |
| 1 | `cuchillo_viejo` | Cuchillo viejo |
| 2 | `cuchillo_oxidado` | Cuchillo oxidado |
| 3 | `navaja_fina` | Navaja fina |
| 4 | `navaja_bolsillo` | Navaja de bolsillo |
| 5 | `palo_madera` | Palo de madera |
| 6 | `garrote_improvisado` | Garrote improvisado |
| 7 | `tubo_metalico` | Tubo metalico |
| 8 | `martillo` | Martillo |
| 9 | `pala` | Pala |
| 10 | `serrucho` | Serrucho |
| 11 | `llave_inglesa` | Llave inglesa |
| 12 | `botella_rota` | Botella rota |
| 13 | `piedra_filosa` | Piedra filosa |
| 14 | `machete` | Machete |
| 15 | `hacha_pequena` | Hacha pequena |
| 16 | `cuchillo_caza` | Cuchillo de caza |

## 02 - Melee avanzadas e improvisadas

Archivo: `hellgames_armas_02_melee_avanzadas_improvisadas.png`

| Celda | ID sugerido | Nombre |
| --- | --- | --- |
| 1 | `palanca_hierro` | Palanca de hierro |
| 2 | `pico_mineria` | Pico de mineria |
| 3 | `baston_reforzado` | Baston reforzado |
| 4 | `cadena_gancho` | Cadena con gancho |
| 5 | `hacha_bombero` | Hacha de bombero |
| 6 | `katana_vieja` | Katana vieja |
| 7 | `espada_ceremonial` | Espada ceremonial |
| 8 | `lanza_militar` | Lanza militar |
| 9 | `maza_pesada` | Maza pesada |
| 10 | `guadana_improvisada` | Guadana improvisada |
| 11 | `lanza_casera` | Lanza casera |
| 12 | `lanza_madera` | Lanza de madera |
| 13 | `palo_clavos` | Palo con clavos |
| 14 | `cuchillo_hueso` | Cuchillo de hueso |
| 15 | `hacha_piedra` | Hacha de piedra |
| 16 | `escudo_madera` | Escudo de madera |

## 03 - Distancia y municion

Archivo: `hellgames_armas_03_distancia_municion.png`

| Celda | ID sugerido | Nombre |
| --- | --- | --- |
| 1 | `honda` | Honda |
| 2 | `tirachinas` | Tirachinas |
| 3 | `jabalina` | Jabalina |
| 4 | `lanza_arrojadiza` | Lanza arrojadiza |
| 5 | `cuchillos_arrojadizos` | Cuchillos arrojadizos |
| 6 | `dardos` | Dardos |
| 7 | `arco_simple` | Arco simple |
| 8 | `arco_caza` | Arco de caza |
| 9 | `ballesta_ligera` | Ballesta ligera |
| 10 | `ballesta_silenciosa` | Ballesta silenciosa |
| 11 | `bala_pequena` | Bala pequena |
| 12 | `bala_pistola` | Bala de pistola |
| 13 | `bala_revolver` | Bala de revolver |
| 14 | `cartucho_escopeta` | Cartucho de escopeta |
| 15 | `municion_rifle` | Municion de rifle |
| 16 | `virote_ballesta` | Virote de ballesta |

## 04 - Fuego, trampas y especiales

Archivo: `hellgames_armas_04_fuego_trampas_especiales.png`

| Celda | ID sugerido | Nombre |
| --- | --- | --- |
| 1 | `pistola_sin_balas` | Pistola sin balas |
| 2 | `pistola_bengalas` | Pistola de bengalas |
| 3 | `revolver_viejo` | Revolver viejo |
| 4 | `pistola_9mm` | Pistola 9mm |
| 5 | `escopeta_recortada` | Escopeta recortada |
| 6 | `escopeta_caza` | Escopeta de caza |
| 7 | `rifle_cerrojo` | Rifle de cerrojo |
| 8 | `rifle_caza` | Rifle de caza |
| 9 | `arma_polvo_casera` | Arma casera de polvora |
| 10 | `molotov` | Coctel molotov |
| 11 | `bomba_humo_casera` | Bomba de humo casera |
| 12 | `trampa_lazo` | Trampa de lazo |
| 13 | `pinchos_ocultos` | Pinchos ocultos |
| 14 | `trampa_oso` | Trampa de oso |
| 15 | `lanza_estrella` | Lanza de estrella |
| 16 | `guante_electrico` | Guante electrico |

## Prompt base usado

Hojas de iconos de inventario RPG 2D, estilo supervivencia oscura, 4x4 celdas, fondo oscuro, sin texto, sin personajes, un arma por celda, siluetas claras, sin sangre ni gore.
