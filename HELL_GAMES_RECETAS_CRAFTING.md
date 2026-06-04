# Hell Games - Recetas de fabricacion y proyectos

Catalogo inicial de recetas para fabricar, reparar, cocinar, curar, montar
trampas y reconstruir proyectos grandes de la isla. Este documento conecta:

- `HELL_GAMES_OBJETOS_RECURSOS.md`;
- `HELL_GAMES_ARMAS.md`;
- acciones actuales del prototipo como `reparar_radio`, `fabricar_basico` y
  `montar_trampa_simple`;
- proyectos de lore como barco, monoriel, generadores, faro y vehiculos.

La idea es empezar con recetas pequenas en el sandbox de 4 casillas y dejar
preparado el camino para proyectos mayores cuando la isla completa este lista.

## Criterio de receta

Cada receta deberia tener:

- `id`;
- nombre visible;
- categoria;
- nivel o complejidad;
- estacion o lugar necesario;
- ingredientes;
- habilidades que ayudan;
- tiempo de fabricacion;
- riesgo;
- resultado;
- forma de desbloqueo.

Ejemplo:

```json
{
  "id": "fabricar_lanza_casera",
  "name": "Fabricar lanza casera",
  "category": "arma_improvisada",
  "tier": 1,
  "station": "ninguna",
  "ingredients": ["rama_seca", "piedra_filosa", "cuerda_fina"],
  "skills": ["supervivencia", "improvisar_herramienta"],
  "time_hours": 1,
  "risk": "bajo",
  "outputs": ["lanza_casera"],
  "unlock": "conocida_inicio"
}
```

## Niveles de fabricacion

| Nivel | Nombre | Funcion |
| --- | --- | --- |
| 0 | Accion simple | Usar, mezclar o reparar algo menor sin estacion. |
| 1 | Supervivencia basica | Fogatas, vendas, herramientas simples, trampas pequenas. |
| 2 | Taller improvisado | Armas mejores, reparaciones, mochilas, filtros, cerraduras. |
| 3 | Mecanica avanzada | Generadores, radios, vehiculos pequenos, sistemas electricos. |
| 4 | Proyecto mayor | Barco, tren, monoriel, compuertas, ruta de escape. |
| 5 | Proyecto de lore | Reliquias, estrellas, maquinaria antigua, tecnologia experimental. |

## Estaciones y lugares

| ID | Nombre | Donde aparece | Permite |
| --- | --- | --- | --- |
| `ninguna` | Ninguna | cualquier zona segura | recetas simples |
| `fogata` | Fogata | campamentos, refugios | cocinar, hervir agua, secar carne |
| `mesa_campamento` | Mesa de campamento | casilla 2 | vendas, mapas, trampas simples |
| `banco_trabajo` | Banco de trabajo | pueblos, ruinas, granjas | reparar, fabricar herramientas |
| `taller_mecanico` | Taller mecanico | estacion militar, puerto, mina | vehiculos, motores, generadores |
| `fundidora` | Fundidora | minas, volcan, estacion militar | lingotes, piezas metalicas |
| `laboratorio` | Laboratorio improvisado | Sector X, templos, enfermeria | quimica, venenos, antidotos |
| `altar_ritual` | Altar ritual | monolitos, templos, ruinas | reliquias, estrellas, pactos |
| `muelle` | Muelle | puerto, costa, naufragio | barcos y balsas |
| `via_mina` | Via de mina | minas abandonadas | vagon, tren, monoriel |

## 1. Supervivencia basica

Recetas pequenas para la primera demo.

| ID | Resultado | Ingredientes | Estacion | Tiempo | Riesgo |
| --- | --- | --- | --- | --- | --- |
| `hacer_fogata` | `fogata` | `rama_seca`, `astillas`, `pedernal` | ninguna | 1h | bajo |
| `hervir_agua` | `agua_limpia` | `agua_turbia`, `botella_vacia`, `fogata` | fogata | 1h | bajo |
| `filtrar_agua_basico` | `agua_limpia` | `agua_turbia`, `tela`, `carbon_vegetal`, `arena` | ninguna | 1h | medio |
| `secar_carne` | `carne_seca` | `carne_cruda`, `sal`, `fogata` | fogata | 2h | bajo |
| `venda_improvisada` | `venda_limpia` | `tela`, `agua_limpia` | ninguna | 1h | bajo |
| `venda_desinfectada` | `venda_desinfectada` | `venda_limpia`, `alcohol_medicinal` | ninguna | 1h | bajo |
| `antorcha_simple` | `antorcha` | `rama_seca`, `tela`, `aceite` | ninguna | 1h | medio |
| `cuerda_primitiva` | `cuerda_primitiva` | `fibra_vegetal`, `corteza` | ninguna | 1h | bajo |
| `mochila_reparada` | `mochila_reparada` | `mochila_danada`, `hilo`, `aguja`, `retazo_tela` | mesa_campamento | 2h | bajo |

## 2. Herramientas y progreso

Estas recetas no son armas, pero abren rutas, mejoran exploracion o cambian una
escena social.

| ID | Resultado | Ingredientes | Estacion | Tiempo | Riesgo |
| --- | --- | --- | --- | --- | --- |
| `reparar_linterna` | `linterna_reparada` | `linterna`, `bateria_pequena`, `bombilla_led` | banco_trabajo | 1h | bajo |
| `kit_reparacion_basico` | `kit_reparacion_basico` | `destornillador`, `alambre`, `tornillos`, `cable_electrico` | mesa_campamento | 1h | bajo |
| `palanca_reforzada` | `palanca_hierro_reforzada` | `palanca_hierro`, `correa`, `aceite` | banco_trabajo | 1h | bajo |
| `filtro_portatil` | `filtro_portatil` | `botella_vacia`, `carbon_vegetal`, `arena`, `tela` | mesa_campamento | 2h | medio |
| `brujula_calibrada` | `brujula_calibrada` | `brujula`, `iman`, `aguja` | mesa_campamento | 1h | bajo |
| `mapa_anotado` | `mapa_anotado` | `mapa_mojado`, `carbon_vegetal`, `diario_farero` | mesa_campamento | 1h | bajo |
| `abrir_caja_oxidada` | loot variable | `llave_oxidada` o `palanca_hierro` | ninguna | 1h | medio |
| `reparar_lente_faro` | `lente_faro_reparada` | `lente_agrietada`, `resina`, `tela`, `documento_tecnico` | faro | 3h | medio |

## 3. Armas, trampas y defensa

Recetas que conectan recursos con `HELL_GAMES_ARMAS.md`.

| ID | Resultado | Ingredientes | Estacion | Tiempo | Riesgo |
| --- | --- | --- | --- | --- | --- |
| `fabricar_lanza_casera` | `lanza_casera` | `rama_seca`, `piedra_filosa`, `cuerda_fina` | ninguna | 1h | bajo |
| `fabricar_palo_clavos` | `palo_clavos` | `palo_madera`, `clavos`, `martillo` | mesa_campamento | 1h | bajo |
| `fabricar_hacha_piedra` | `hacha_piedra` | `piedra_filosa`, `rama_seca`, `cuerda_fina` | ninguna | 2h | medio |
| `fabricar_molotov` | `molotov` | `frasco_vidrio`, `tela`, `gasolina` | ninguna | 1h | alto |
| `fabricar_bomba_humo` | `bomba_humo_casera` | `lata_pequena`, `polvo_irritante`, `tela` | mesa_campamento | 1h | medio |
| `montar_trampa_lazo` | `trampa_lazo` | `soga`, `rama_seca` | zona_bosque | 1h | bajo |
| `montar_alarma_latas` | `alarma_latas` | `lata_pequena`, `cuerda_fina`, `piedra_comun` | ninguna | 1h | bajo |
| `montar_pinchos_ocultos` | `pinchos_ocultos` | `rama_seca`, `piedra_filosa`, `hojas_grandes` | zona_bosque | 2h | medio |
| `montar_cuerda_tensada` | `cuerda_tensada` | `cuerda_vieja`, `clavos` | ruinas | 1h | medio |
| `preparar_dardo_venenoso` | `dardo_venenoso` | `dardos`, `veneno_liquido` | laboratorio | 1h | alto |

## 4. Medicina, venenos y cocina avanzada

Estas recetas permiten personajes medicos, chamanes, tramperos o cocineros
peligrosos.

| ID | Resultado | Ingredientes | Estacion | Tiempo | Riesgo |
| --- | --- | --- | --- | --- | --- |
| `unguento_medicinal` | `unguento_medicinal` | `hierba_medicinal`, `grasa_animal`, `agua_limpia` | fogata | 2h | bajo |
| `infusion_calmante` | `infusion_calmante` | `hierba_calmante`, `agua_limpia`, `fogata` | fogata | 1h | bajo |
| `veneno_basico` | `veneno_liquido` | `hierba_venenosa`, `agua_contaminada`, `frasco_vidrio` | laboratorio | 2h | alto |
| `antidoto_basico` | `antidoto` | `flores_raras`, `hierba_medicinal`, `alcohol_medicinal` | laboratorio | 3h | medio |
| `somnifero_improvisado` | `somnifero` | `hongos_alucinogenos`, `hierba_calmante`, `tubo_quirurgico` | laboratorio | 2h | alto |
| `cebo_criaturas` | `carne_contaminada_cebo` | `carne_podrida`, `sangre`, `sal_mineral` | ninguna | 1h | medio |
| `racion_conservada` | `racion_conservada` | `carne_seca`, `galletas_secas`, `sal` | mesa_campamento | 1h | bajo |

## 5. Energia, senales y sistemas

Estas recetas empiezan a acercarse al objetivo de escapar, pedir ayuda o activar
zonas peligrosas.

| ID | Resultado | Ingredientes | Estacion | Tiempo | Riesgo |
| --- | --- | --- | --- | --- | --- |
| `reparar_radio_faro` | `radio_funcional` | `radio_rota`, `bateria_pequena`, `cable_electrico`, `antena` | faro | 3h | medio |
| `encender_faro` | `faro_encendido` | `lente_faro_reparada`, `aceite_lampara`, `bateria_pequena` | faro | 2h | alto |
| `generador_pequeno` | `generador_pequeno` | `motor_pequeno`, `cable_electrico`, `bateria_auto`, `gasolina` | taller_mecanico | 4h | alto |
| `panel_solar_reparado` | `panel_solar_reparado` | `panel_solar_roto`, `circuito_funcional`, `cable_electrico` | banco_trabajo | 4h | medio |
| `baliza_emergencia` | `baliza_emergencia` | `radio_funcional`, `bengala`, `bateria_pequena`, `antena` | faro | 2h | alto |
| `abrir_compuerta_electrica` | ruta desbloqueada | `llave_electronica`, `fusible`, `cable_electrico` | zona_militar | 2h | medio |

## 6. Proyectos mayores de escape o movilidad

No son para la primera demo completa, pero conviene dejarlos definidos para que
la isla tenga objetivos de largo plazo.

| ID | Proyecto | Componentes principales | Lugar | Tiempo | Riesgo |
| --- | --- | --- | --- | --- | --- |
| `reparar_balsa` | Balsa costera | `madera_ligera`, `soga_gruesa`, `lona`, `resina` | costa / muelle | 6h | medio |
| `reparar_bote_motor` | Bote con motor | `madera_naval`, `motor_pequeno`, `helice`, `gasolina`, `timon` | puerto / naufragio | 12h | alto |
| `reparar_barco_navegante` | Barco del navegante | `madera_naval`, `tela_vela`, `cuerda_marina`, `timon`, `motor_vehiculo`, `diesel` | Puerto del Navegante | 24h | muy alto |
| `activar_vagon_mina` | Vagon minero | `rueda`, `riel_pesado`, `grasa_animal`, `palanca_hierro` | Minas de Hierro | 6h | alto |
| `reparar_tren_mina` | Tren de mina | `carbon_mineral`, `engranaje`, `cadena`, `riel_pesado`, `bujia` | Minas de Hierro | 18h | muy alto |
| `activar_monoriel_abandonado` | Monoriel de evacuacion | `circuito_funcional`, `motor_electrico`, `fusible`, `bobina_cobre`, `llave_electronica` | Minas / Observatorio | 24h | muy alto |
| `reparar_vehiculo_oculto` | Vehiculo terrestre oculto | `motor_vehiculo`, `rueda`, `bateria_auto`, `gasolina`, `correa_motor`, `radiador` | zona secreta | 18h | muy alto |
| `blindar_vehiculo` | Vehiculo blindado | `vehiculo_reparado`, `placa_metalica`, `tornillos`, `llave_inglesa` | taller_mecanico | 8h | alto |

## 7. Proyectos de lore y tecnologia extrana

Estas recetas no deberian funcionar como crafting normal. Requieren pistas,
rituales, condiciones de tiempo o consecuencias narrativas.

| ID | Proyecto | Componentes | Lugar | Condicion |
| --- | --- | --- | --- | --- |
| `activar_monolito_menor` | Monolito menor | `piedra_tallada`, `polvo_ritual`, `amuleto_roto` | Circulo de Monolitos | noche o luna visible |
| `sellar_reliquia_guardian` | Reliquia sellada | `reliquia_antigua`, `estrella_protegida`, `tela_antigua` | Ruinas del Guardian | guardian despierto |
| `purificar_estrella_contaminada` | Estrella purificada | `estrella_contaminada`, `agua_limpia`, `flores_raras`, `polvo_ritual` | templo | riesgo de maldicion |
| `forjar_lanza_estrella` | Lanza de estrella | `fragmento_estrella`, `lanza_militar`, `cristal_energetico`, `resina` | altar_ritual | pacto o sacrificio |
| `encender_nucleo_oxidado` | Nucleo activo | `nucleo_oxidado`, `celda_energia`, `bobina_cobre`, `cristal_verde` | Sector X | evento peligroso |
| `abrir_ruta_salida_oculta` | Ruta oculta | `mapa_parcial`, `llave_antigua`, `diario_ocultista`, `estrella_protegida` | ruinas / torre | acertijo resuelto |

## Desbloqueo de recetas

Las recetas pueden desbloquearse de varias formas:

- conocidas desde el inicio por supervivencia basica;
- aprendidas por habilidad del personaje;
- descubiertas al leer diarios, mapas o documentos tecnicos;
- ensenadas por lugarenos a cambio de trueque;
- reveladas al explorar POIs;
- desbloqueadas por eventos de guardianes o jefes;
- deducidas si el NPC tiene rasgos compatibles.

Ejemplos:

| Receta | Como se desbloquea |
| --- | --- |
| `hacer_fogata` | cualquier participante con supervivencia minima |
| `reparar_radio_faro` | Renzo o documento tecnico del faro |
| `activar_monolito_menor` | diario ocultista o trato con lugareno |
| `reparar_bote_motor` | mapa del puerto + motor encontrado |
| `activar_monoriel_abandonado` | documento tecnico de minas + llave electronica |

## Reglas narrativas para el bot

- Fabricar consume tiempo de isla; con la escala actual, 1h = 1 minuto real.
- Un proyecto mayor puede quedar en progreso y ser robado, saboteado o defendido.
- Algunas recetas hacen ruido y atraen criaturas o lugarenos.
- Algunas recetas revelan ubicacion: un faro encendido, una bengala o un motor se ven desde lejos.
- Un NPC puede mentir diciendo que conoce una receta.
- Un lugareno puede vender una receta incompleta.
- Una receta fallida puede crear un objeto defectuoso en vez de perderlo todo.
- Los objetos grandes no entran al inventario; quedan como estado de zona.

## Lista corta para experimentar en el sandbox de 4 casillas

Para la demo usaria estas recetas primero:

| Receta | Por que sirve |
| --- | --- |
| `hacer_fogata` | comida, noche, criaturas, senales pequenas |
| `hervir_agua` | supervivencia clara y facil de entender |
| `venda_improvisada` | heridas sin meter medicina compleja |
| `fabricar_lanza_casera` | primer arma craftable |
| `montar_trampa_lazo` | defensa sin combate directo |
| `reparar_radio_faro` | objetivo narrativo de casilla 1 |
| `mapa_anotado` | conecta exploracion con decisiones |
| `activar_monolito_menor` | prueba de lore y consecuencias |

## Siguiente paso

Cuando este esquema sea aprobado, conviene convertirlo a:

```txt
data/crafting_recipes.json
```

Ese JSON sera el sistema que el bot pueda usar para fabricar, reparar, desbloquear
rutas, crear proyectos de zona y mover objetivos de largo plazo.
