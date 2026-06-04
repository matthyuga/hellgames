# Hell Games - Guia de materiales

Guia practica de los materiales separados desde los sets de iconos. Cubre uso, jerarquia, si son loot basico o requieren fabricacion/procesamiento, y ubicaciones sugeridas para isla completa y piloto de 4 casillas.

Fuentes: `HELL_GAMES_OBJETOS_RECURSOS.md`, `doc_materiales1.md`, `HELL_GAMES_RECETAS_CRAFTING.md`, `HELL_GAMES_CASILLAS.md`, `data/prototype_runtime_4.json`, `data/prototype_island_4.json`.

## Jerarquia

- **Nivel 1 - Basico / loot directo**
- **Nivel 2 - Procesable / requiere herramienta o contexto**
- **Nivel 3 - Tecnico, medico o raro**
- **Nivel 4 - Especial de evento o progreso mayor**

## Piloto de 4 casillas

| Casilla | Rol | Materiales especialmente relevantes |
| --- | --- | --- |
| 1 Faro de la Vigilia Sagrada | senales, radio, misterio tecnico | `agua_limpia`, `cable_electrico`, `bateria_pequena`, `botella_vacia`, `chatarra` |
| 2 Campamento Raiz Maldita | refugio, supervivencia, crafting inicial | `rama_seca`, `tela`, `retazo_tela`, `cuerda_fina`, `lata_comida`, `pedernal`, `agua_limpia`, `fibra_vegetal` |
| 6 Circulo de Monolitos | ritual, pistas, presion psicologica | `piedra_comun`, `piedra_filosa`, `piedra_lisa`, `fragmento_estrella`, `hongos_alucinogenos` |
| 7 Ruinas del Guardian | trampas, metal, reliquias | `cuerda_vieja`, `placa_metalica`, `clavos`, `alambre`, `piedra_filosa`, `polvo_irritante` |

## Agua y recipientes

| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `agua_turbia` | Agua turbia | Basico vital | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | beber con riesgo, purificar, trampa | filtrar_agua_basico, hervir_agua | No prioritario en piloto; posible por evento, trueque o exploracion. | 11 Pantano, 5 Puerto, 16 Costa, zonas inundadas o recipientes sucios. |
| 1 | `botella_vacia` | Botella vacia | Basico vital | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | guardar agua, combustible, medicina, veneno | filtro_portatil, hervir_agua | No prioritario en piloto; posible por evento, trueque o exploracion. | 4 Cascada, 17 Oasis/Templo de la Luna, 16 Costa, 21 Muelle, campamentos y recipientes abandonados. |
| 2 | `agua_limpia` | Agua limpia | Fabricado o procesado | Opcional: puede encontrarse o fabricarse/procesarse; tambien sirve como ingrediente. | beber, cocinar, limpiar heridas | filtrar_agua_basico, hervir_agua, infusion_calmante, purificar_estrella_contaminada, unguento_medicinal, venda_improvisada | 1 Faro y 2 Campamento como loot comun; tambien inventarios iniciales. | 4 Cascada, 17 Oasis/Templo de la Luna, 23 Jungla parcial; tambien 1 Faro y 2 Campamento en piloto. |
| 2 | `tubo_quirurgico` | Tubo quirurgico | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | dosis liquida pequena | somnifero_improvisado | No prioritario en piloto; posible por evento, trueque o exploracion. | 4 Cascada, 17 Oasis/Templo de la Luna, 16 Costa, 21 Muelle, campamentos y recipientes abandonados. |
| 3 | `ampolla_sellada` | Ampolla sellada | Tecnico, medico o raro | No documentada: tratable como loot, trueque o hallazgo de zona. | medicina o sustancia especial | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 4 Cascada, 17 Oasis/Templo de la Luna, 16 Costa, 21 Muelle, campamentos y recipientes abandonados. |

## Combustible y energia

| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `cable_electrico` | Cable electrico | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | reparaciones, trampas electricas | abrir_compuerta_electrica, generador_pequeno, kit_reparacion_basico, panel_solar_reparado, reparar_radio_faro | 1 Faro comun; Renzo inicia con cable corto equivalente. | 1 Faro, 12 Sector X, 13 Torre, 19 Estacion Militar, 20 Observatorio. |
| 2 | `bateria_pequena` | Bateria pequena | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | radio, linterna, senales | baliza_emergencia, encender_faro, reparar_linterna, reparar_radio_faro | 1 Faro como loot raro; clave para radio/faro. | 1 Faro, 13 Torre, 19 Estacion Militar, 20 Observatorio, almacenes tecnicos. |
| 3 | `bateria_auto` | Bateria de auto | Tecnico, medico o raro | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | vehiculos, generadores | generador_pequeno, reparar_vehiculo_oculto | No prioritario en piloto; posible por evento, trueque o exploracion. | 19 Estacion Militar, talleres, vehiculos ocultos, puerto y zonas mecanicas. |

## Comida animal y conservas

| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `carne_cruda` | Carne cruda | Basico vital | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | comida con riesgo, cocinar | secar_carne | No prioritario en piloto; posible por evento, trueque o exploracion. | 4 Cascada, 14 Granja, 16 Costa, 21 Muelle, 22 Pueblo Nevado. |
| 1 | `lata_comida` | Lata de comida | Basico vital | No documentada: tratable como loot, trueque o hallazgo de zona. | comida segura | Sin receta directa documentada. | 2 Campamento comun; comida segura. | 4 Cascada, 14 Granja, 16 Costa, 21 Muelle, 22 Pueblo Nevado. |
| 2 | `pescado_seco` | Pescado seco | Procesable / poco comun | No documentada: tratable como loot, trueque o hallazgo de zona. | comida conservada | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 4 Cascada, 5 Puerto, 16 Costa, 21 Muelle. |

## Cuerdas, telas y fibras

| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `correa` | Correa | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | sujetar, reparar, transporte | palanca_reforzada | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 1 | `cuerda_fina` | Cuerda fina | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | trampas pequenas, costura, mecanismos | fabricar_hacha_piedra, fabricar_lanza_casera, montar_alarma_latas | 2 Campamento comun; base de trampas y lanzas. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 1 | `cuerda_vieja` | Cuerda vieja | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | atar con riesgo, reparar, rastro falso | montar_cuerda_tensada | 7 Ruinas como loot comun. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 1 | `fibra_vegetal` | Fibra vegetal | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | cuerda primitiva, cestas | cuerda_primitiva | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 1 | `hilo` | Hilo | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | sutura, ropa, reparacion fina | mochila_reparada | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 1 | `retazo_tela` | Retazo de tela | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | craft menor, vendas pobres | mochila_reparada | 2 Campamento/runtime; Rex inicia con uno. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 1 | `tela` | Tela | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | vendas, filtros, ropa, antorchas | antorcha_simple, fabricar_bomba_humo, fabricar_molotov, filtrar_agua_basico, filtro_portatil, reparar_lente_faro, venda_improvisada | 2 Campamento comun; base de vendas, filtros y antorchas. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 2 | `cuero` | Cuero | Procesable / poco comun | No documentada: tratable como loot, trueque o hallazgo de zona. | correas, proteccion, mochilas | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 2 | `lona` | Lona | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | refugio, cubrir objetos, camuflaje | reparar_balsa | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 2 | `red_pesca` | Red de pesca | Procesable / poco comun | No documentada: tratable como loot, trueque o hallazgo de zona. | pesca, captura, trampa | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 2 | `soga_gruesa` | Soga gruesa | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | carga pesada, barcos, puentes | reparar_balsa | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado. |
| 2 | `tela_vela` | Tela de vela | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | refugio, barco, lona resistente | reparar_barco_navegante | No prioritario en piloto; posible por evento, trueque o exploracion. | 16 Costa del Naufragio, 5 Puerto, 21 Muelle y barcos abandonados. |

## Madera y vegetales secos

| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `corteza` | Corteza | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | yesca, medicina simple, cuerda rudimentaria | cuerda_primitiva | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 16 Costa, 23 Jungla. |
| 1 | `rama_seca` | Rama seca | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | fuego, mango, trampa simple | antorcha_simple, fabricar_hacha_piedra, fabricar_lanza_casera, hacer_fogata, montar_pinchos_ocultos, montar_trampa_lazo | 2 Campamento comun; base de fogata y lanza. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 16 Costa, 23 Jungla. |
| 1 | `tabla` | Tabla | Basico | No documentada: tratable como loot, trueque o hallazgo de zona. | reparar, construir, puente, puerta | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 16 Costa, 23 Jungla. |
| 1 | `tronco` | Tronco | Basico | No documentada: tratable como loot, trueque o hallazgo de zona. | fogata grande, barricada, refugio | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 16 Costa, 23 Jungla. |
| 2 | `carbon_vegetal` | Carbon vegetal | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | filtros, fuego estable, quimica | filtrar_agua_basico, filtro_portatil, mapa_anotado | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 16 Costa, 23 Jungla. |

## Medicina y quimica

| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `hierba_medicinal` | Hierba medicinal | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | unguentos, curacion leve | antidoto_basico, unguento_medicinal | No prioritario en piloto; posible por evento, trueque o exploracion. | 4 Cascada, 11 Pantano, 17 Oasis, 19 Estacion Militar, Sector X/laboratorios. |
| 2 | `alcohol_medicinal` | Alcohol medicinal | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | desinfectar, combustible | antidoto_basico, venda_desinfectada | No prioritario en piloto; posible por evento, trueque o exploracion. | 4 Cascada, 11 Pantano, 17 Oasis, 19 Estacion Militar, Sector X/laboratorios. |
| 2 | `antiseptico` | Antiseptico | Procesable / poco comun | No documentada: tratable como loot, trueque o hallazgo de zona. | limpiar heridas | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 4 Cascada, 11 Pantano, 17 Oasis, 19 Estacion Militar, Sector X/laboratorios. |
| 2 | `jeringa` | Jeringa | Procesable / poco comun | No documentada: tratable como loot, trueque o hallazgo de zona. | aplicar medicina o veneno | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 4 Cascada, 11 Pantano, 17 Oasis, 19 Estacion Militar, Sector X/laboratorios. |
| 2 | `polvo_irritante` | Polvo irritante | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | cegar, distraer | fabricar_bomba_humo | 7 Ruinas o 6 Monolitos como polvo raro posible. | 4 Cascada, 11 Pantano, 17 Oasis, 19 Estacion Militar, Sector X/laboratorios. |
| 3 | `acido` | Acido | Tecnico, medico o raro | No documentada: tratable como loot, trueque o hallazgo de zona. | cerraduras, sabotaje | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 4 Cascada, 11 Pantano, 17 Oasis, 19 Estacion Militar, Sector X/laboratorios. |
| 3 | `antidoto` | Antidoto | Fabricado o procesado | Si u opcional: aparece como resultado de fabricacion/procesamiento. | veneno | antidoto_basico | No prioritario en piloto; posible por evento, trueque o exploracion. | 17 Oasis, 11 Pantano por necesidad, Sector X/laboratorio, medicos. |
| 3 | `veneno_liquido` | Veneno liquido | Fabricado o procesado | Opcional: puede encontrarse o fabricarse/procesarse; tambien sirve como ingrediente. | comida, agua, trampas | preparar_dardo_venenoso, veneno_basico | No prioritario en piloto; posible por evento, trueque o exploracion. | 11 Pantano, Sector X, laboratorios, tramperos y zonas de veneno. |

## Metal y chatarra

| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `alambre` | Alambre | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | trampas, ataduras, reparacion | kit_reparacion_basico | 1 Faro por radio/antenas; 7 Ruinas como trampa vieja posible. | 5 Puerto, 7 Ruinas, 10 Bastion, 13 Torre, 19 Estacion Militar, 20 Observatorio. |
| 1 | `chatarra` | Chatarra | Basico | No documentada: tratable como loot, trueque o hallazgo de zona. | reparaciones, trampas, trueque | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 5 Puerto, 7 Ruinas, 10 Bastion, 13 Torre, 19 Estacion Militar, 20 Observatorio. |
| 1 | `clavos` | Clavos | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | construccion, trampas | fabricar_palo_clavos, montar_cuerda_tensada | 2 Campamento y 7 Ruinas como material de trampas. | 5 Puerto, 7 Ruinas, 10 Bastion, 13 Torre, 19 Estacion Militar, 20 Observatorio. |
| 2 | `placa_metalica` | Placa metalica | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | blindaje, puerta, refuerzo | blindar_vehiculo | 7 Ruinas como loot comun. | 5 Puerto, 7 Ruinas, 10 Bastion, 13 Torre, 19 Estacion Militar, 20 Observatorio. |
| 2 | `tubo_metalico` | Tubo metalico | Procesable / poco comun | No documentada: tratable como loot, trueque o hallazgo de zona. | soporte, reparacion, caneria | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 5 Puerto, 7 Ruinas, 10 Bastion, 13 Torre, 19 Estacion Militar, 20 Observatorio. |

## Piedra, tierra y minerales

| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `arcilla` | Arcilla | Basico | No documentada: tratable como loot, trueque o hallazgo de zona. | vasijas, sellar grietas, moldes | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 3 Minas, 6 Monolitos, 7 Ruinas, 15 Templo del Sol, 18 Canon, 25 Volcan. |
| 1 | `arena` | Arena | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | filtros, vidrio, apagar fuego | filtrar_agua_basico, filtro_portatil | No prioritario en piloto; posible por evento, trueque o exploracion. | 16 Costa, 21 Muelle, 24 Bastion Duna Seca, playas y dunas. |
| 1 | `piedra_comun` | Piedra comun | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | peso, trampa, herramienta simple | montar_alarma_latas | 6 Monolitos y 7 Ruinas por entorno; posible en 2 Campamento. | 3 Minas, 6 Monolitos, 7 Ruinas, 15 Templo del Sol, 18 Canon, 25 Volcan. |
| 1 | `piedra_filosa` | Piedra filosa | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | corte primitivo, punta futura | fabricar_hacha_piedra, fabricar_lanza_casera, montar_pinchos_ocultos | 6 Monolitos y 7 Ruinas como hallazgo; clave para lanza/hacha. | 3 Minas, 6 Monolitos, 7 Ruinas, 15 Templo del Sol, 18 Canon, 25 Volcan. |
| 1 | `piedra_lisa` | Piedra lisa | Basico | No documentada: tratable como loot, trueque o hallazgo de zona. | ritual, herramienta, distraccion | Sin receta directa documentada. | 6 Monolitos como variante ritual posible. | 3 Minas, 6 Monolitos, 7 Ruinas, 15 Templo del Sol, 18 Canon, 25 Volcan. |
| 2 | `carbon_mineral` | Carbon mineral | Fabricado o procesado | Si u opcional: aparece como resultado de fabricacion/procesamiento. | hornos, fundicion, energia | reparar_tren_mina | No prioritario en piloto; posible por evento, trueque o exploracion. | 3 Minas, 6 Monolitos, 7 Ruinas, 15 Templo del Sol, 18 Canon, 25 Volcan. |
| 2 | `mineral_hierro` | Mineral de hierro | Procesable / poco comun | No documentada: tratable como loot, trueque o hallazgo de zona. | fundicion, piezas metalicas | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 3 Minas, 6 Monolitos, 7 Ruinas, 15 Templo del Sol, 18 Canon, 25 Volcan. |
| 2 | `pedernal` | Pedernal | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | encender fuego | hacer_fogata | 2 Campamento comun segun lista corta. | 3 Minas, 6 Monolitos, 7 Ruinas, 15 Templo del Sol, 18 Canon, 25 Volcan. |
| 2 | `sal_mineral` | Sal mineral | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | conservar comida, atraer animales | cebo_criaturas | No prioritario en piloto; posible por evento, trueque o exploracion. | 3 Minas, 6 Monolitos, 7 Ruinas, 15 Templo del Sol, 18 Canon, 25 Volcan. |
| 4 | `cristal_energetico` | Cristal energetico | Especial / objetivo | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | tecnologia avanzada, eventos | forjar_lanza_estrella | No prioritario en piloto; posible por evento, trueque o exploracion. | 12 Sector X, 25 Volcan, laboratorios, guardianes o eventos de alto riesgo. |
| 4 | `cristal_verde` | Cristal verde | Especial / objetivo | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | energia extrana, tecnologia | encender_nucleo_oxidado | No prioritario en piloto; posible por evento, trueque o exploracion. | 12 Sector X principalmente; tambien 3 Minas como cristal raro o eventos contaminados. |
| 4 | `fragmento_estrella` | Fragmento de estrella | Especial / objetivo | Si u opcional: aparece como resultado de fabricacion/procesamiento. | llaves, pactos, progreso mayor | forjar_lanza_estrella | 6 Monolitos como loot raro; objetivo de progreso. | 6 Monolitos, 12 Sector X, 15 Templo del Sol, 25 Volcan, jefes o guardianes. |

## Plantas, hongos y alimentos vegetales

| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `bayas_comestibles` | Bayas comestibles | Basico | No documentada: tratable como loot, trueque o hallazgo de zona. | comida rapida | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 11 Pantano, 23 Jungla. |
| 1 | `hojas_grandes` | Hojas grandes | Basico | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | envolver comida, techo, camuflaje | montar_pinchos_ocultos | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 11 Pantano, 23 Jungla. |
| 1 | `hongos_comestibles` | Hongos comestibles | Basico | No documentada: tratable como loot, trueque o hallazgo de zona. | comida | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 11 Pantano, 23 Jungla. |
| 1 | `raiz_comestible` | Raiz comestible | Basico | No documentada: tratable como loot, trueque o hallazgo de zona. | comida basica | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 11 Pantano, 23 Jungla. |
| 2 | `raiz_toxica` | Raiz toxica | Procesable / poco comun | No documentada: tratable como loot, trueque o hallazgo de zona. | veneno o medicina procesada | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 11 Pantano, 23 Jungla. |
| 3 | `hongos_alucinogenos` | Hongos alucinogenos | Tecnico, medico o raro | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | confusion, miedo, ritual | somnifero_improvisado | No prioritario en piloto; posible por evento, trueque o exploracion. | 2 Campamento, 8 Pradera, 9 Templo de las Hojas, 11 Pantano, 23 Jungla. |

## Tecnologia y electronica

| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | `circuito_roto` | Circuito roto | Procesable / poco comun | No documentada: tratable como loot, trueque o hallazgo de zona. | piezas electronicas | Sin receta directa documentada. | No prioritario en piloto; posible por evento, trueque o exploracion. | 12 Sector X, 13 Torre, 19 Estacion Militar, 20 Observatorio, drones/camaras rotas. |
| 2 | `fusible` | Fusible | Procesable / poco comun | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | activar sistemas | abrir_compuerta_electrica, activar_monoriel_abandonado | No prioritario en piloto; posible por evento, trueque o exploracion. | 13 Torre, 19 Estacion Militar, 20 Observatorio, Sector X, minas/monoriel. |
| 3 | `bobina_cobre` | Bobina de cobre | Tecnico, medico o raro | No principalmente: se consigue como loot/recoleccion y se usa como ingrediente. | electricidad | activar_monoriel_abandonado, encender_nucleo_oxidado | No prioritario en piloto; posible por evento, trueque o exploracion. | Sector X, Observatorio, Estacion Militar, talleres, motores y generadores. |
