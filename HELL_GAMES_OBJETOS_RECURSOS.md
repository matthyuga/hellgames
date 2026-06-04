# Hell Games - Objetos y recursos del mapa

Catalogo inicial de recursos, objetos de supervivencia y materias primas.
No incluye armas terminadas. Algunas piezas pueden servir luego para fabricar
armas, trampas o herramientas, pero las armas tendran su propio catalogo.

Fuente base:

- `doc_materiales1.md`;
- hallazgos de `HELL_GAMES_CASILLAS.md`;
- objetos piloto de `data/prototype_runtime_4.json`.

## Criterio

Cada objeto deberia tener:

- `id`;
- nombre visible;
- categoria;
- rareza;
- usos principales;
- posible estado;
- zonas donde puede aparecer.

Ejemplo:

```json
{
  "id": "agua_limpia",
  "name": "Agua limpia",
  "category": "agua",
  "rarity": "comun",
  "uses": ["beber", "curar_sed", "limpiar_heridas", "cocinar"],
  "states": ["limpia"],
  "zones": [4, 17, 23]
}
```

## 1. Agua y recipientes

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `botella_vacia` | Botella vacia | comun | guardar agua, combustible, medicina, veneno |
| `agua_limpia` | Agua limpia | comun | beber, cocinar, limpiar heridas |
| `agua_turbia` | Agua turbia | comun | beber con riesgo, purificar, trampa |
| `agua_contaminada` | Agua contaminada | poco comun | veneno, enfermedad, trampa |
| `agua_salada` | Agua salada | comun en costa | no beber directa, sal, limpieza limitada |
| `cantimplora` | Cantimplora | poco comun | recipiente reutilizable |
| `bidon_vacio` | Bidon vacio | poco comun | transportar agua/combustible |
| `bidon_agua` | Bidon de agua | raro | mucha agua, pesado |
| `hielo` | Hielo | comun en frio | derretir para agua |
| `frasco_vidrio` | Frasco de vidrio | comun | medicina, veneno, muestras |
| `tubo_quirurgico` | Tubo quirurgico | poco comun | dosis liquida pequena |
| `ampolla_sellada` | Ampolla sellada | raro | medicina o sustancia especial |

## 2. Madera y vegetales secos

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `rama_seca` | Rama seca | comun | fuego, mango, trampa simple |
| `rama_humeda` | Rama humeda | comun | construccion pobre, humo |
| `tronco` | Tronco | comun | fogata grande, barricada, refugio |
| `tabla` | Tabla | comun | reparar, construir, puente, puerta |
| `madera_mojada` | Madera mojada | comun en costa | reparar si se seca, fuego pobre |
| `madera_ligera` | Madera ligera | comun | refugios, flotacion, flechas futuras |
| `bambu` | Bambu | comun en casilla 23 | lanzas futuras, trampas, pasarelas |
| `corteza` | Corteza | comun | yesca, medicina simple, cuerda rudimentaria |
| `astillas` | Astillas | comun | yesca, relleno de trampas |
| `resina` | Resina | poco comun | pegamento, antorchas, sellar |
| `carbon_vegetal` | Carbon vegetal | poco comun | filtros, fuego estable, quimica |

## 3. Piedra, tierra y minerales

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `piedra_comun` | Piedra comun | comun | peso, trampa, herramienta simple |
| `piedra_filosa` | Piedra filosa | comun | corte primitivo, punta futura |
| `piedra_lisa` | Piedra lisa | comun | ritual, herramienta, distraccion |
| `pedernal` | Pedernal | poco comun | encender fuego |
| `arcilla` | Arcilla | comun | vasijas, sellar grietas, moldes |
| `arena` | Arena | comun | filtros, vidrio, apagar fuego |
| `piedra_tallada` | Piedra tallada | poco comun | ritual, llave primitiva, marca territorial |
| `sal_mineral` | Sal mineral | poco comun | conservar comida, atraer animales |
| `carbon_mineral` | Carbon mineral | poco comun | hornos, fundicion, energia |
| `mineral_hierro` | Mineral de hierro | poco comun | fundicion, piezas metalicas |
| `obsidiana` | Obsidiana | raro | corte, ritual, material especial |
| `ceniza_volcanica` | Ceniza volcanica | comun en volcan | ocultar rastros, contaminar agua |
| `polvo_mineral` | Polvo mineral | poco comun | ritual, pigmento, quimica |
| `polvo_ritual` | Polvo ritual | raro | activar monolitos, marcar ofrendas, rastros falsos |
| `cristal_verde` | Cristal verde | raro | energia extrana, tecnologia |
| `cristal_energetico` | Cristal energetico | muy raro | tecnologia avanzada, eventos |
| `fragmento_estrella` | Fragmento de estrella | muy raro | llaves, pactos, progreso mayor |

## 4. Metal y chatarra

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `chatarra` | Chatarra | comun | reparaciones, trampas, trueque |
| `placa_metalica` | Placa metalica | poco comun | blindaje, puerta, refuerzo |
| `tubo_metalico` | Tubo metalico | poco comun | soporte, reparacion, caneria |
| `alambre` | Alambre | comun | trampas, ataduras, reparacion |
| `clavos` | Clavos | comun | construccion, trampas |
| `tornillos` | Tornillos | comun | mecanismos, reparaciones |
| `bisagras` | Bisagras | poco comun | puertas, cofres, trampillas |
| `cadena` | Cadena | poco comun | atar, bloquear, mecanismos |
| `resorte` | Resorte | poco comun | trampas, mecanismos |
| `engranaje` | Engranaje | raro | maquinaria, puertas, relojes |
| `riel_pesado` | Riel pesado | raro | metal pesado, barrera, fundicion |
| `metal_quemado` | Metal quemado | poco comun | reparacion riesgosa, Sector X |

## 5. Cuerdas, telas y fibras

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `soga` | Soga | comun | escalar, atar, trampas, puentes |
| `soga_gruesa` | Soga gruesa | poco comun | carga pesada, barcos, puentes |
| `cuerda_fina` | Cuerda fina | comun | trampas pequenas, costura, mecanismos |
| `cuerda_vieja` | Cuerda vieja | comun | atar con riesgo, reparar, rastro falso |
| `cuerda_primitiva` | Cuerda primitiva | comun | fabricacion basica |
| `hilo` | Hilo | comun | sutura, ropa, reparacion fina |
| `tela` | Tela | comun | vendas, filtros, ropa, antorchas |
| `retazo_tela` | Retazo de tela | comun | craft menor, vendas pobres |
| `lona` | Lona | poco comun | refugio, cubrir objetos, camuflaje |
| `tela_vela` | Tela de vela | poco comun | refugio, barco, lona resistente |
| `tela_antigua` | Tela antigua | raro | ritual, vendas especiales, trueque |
| `cuero` | Cuero | poco comun | correas, proteccion, mochilas |
| `correa` | Correa | comun | sujetar, reparar, transporte |
| `red_pesca` | Red de pesca | poco comun | pesca, captura, trampa |
| `fibra_vegetal` | Fibra vegetal | comun | cuerda primitiva, cestas |

## 6. Combustible y energia

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `aceite_lampara` | Aceite de lampara | comun | faro, fuego, lubricar |
| `aceite` | Aceite | comun | fuego, cocina, mecanismos |
| `alcohol` | Alcohol | poco comun | medicina, combustible, desinfectar |
| `gasolina` | Gasolina | raro | generador, vehiculo, fuego peligroso |
| `diesel` | Diesel | raro | maquinaria pesada, generador |
| `bateria_pequena` | Bateria pequena | poco comun | radio, linterna, senales |
| `bateria_auto` | Bateria de auto | raro | vehiculos, generadores |
| `celda_energia` | Celda de energia | muy raro | tecnologia avanzada |
| `cable_electrico` | Cable electrico | comun | reparaciones, trampas electricas |
| `panel_solar_roto` | Panel solar roto | raro | piezas, energia si se repara |
| `bengala` | Bengala | poco comun | senal, luz, distraccion, pedir ayuda |

## 7. Medicina y quimica

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `venda_usada` | Venda usada | comun | curacion pobre, riesgo de infeccion |
| `venda_limpia` | Venda limpia | comun | curar heridas leves |
| `venda_desinfectada` | Venda desinfectada | poco comun | curar con menor riesgo |
| `hierba_medicinal` | Hierba medicinal | comun | unguentos, curacion leve |
| `hierba_calmante` | Hierba calmante | poco comun | dolor, miedo, descanso |
| `hierba_venenosa` | Hierba venenosa | poco comun | veneno, trampa, antidoto si se procesa |
| `hierbas_secas` | Hierbas secas | comun | yesca, ritual, infusion pobre |
| `antiseptico` | Antiseptico | poco comun | limpiar heridas |
| `alcohol_medicinal` | Alcohol medicinal | poco comun | desinfectar, combustible |
| `analgesico` | Analgesico | poco comun | dolor, moverse herido |
| `coagulante` | Coagulante | raro | detener sangrado |
| `suero` | Suero | raro | deshidratacion, recuperacion |
| `antidoto` | Antidoto | raro | veneno |
| `somnifero` | Somnifero | raro | dormir, sedar |
| `veneno_liquido` | Veneno liquido | raro | comida, agua, trampas |
| `acido` | Acido | raro | cerraduras, sabotaje |
| `polvo_irritante` | Polvo irritante | poco comun | cegar, distraer |
| `gas_toxico` | Gas toxico | muy raro | zona peligrosa |
| `bolsa_medica` | Bolsa medica | raro | transportar insumos |
| `jeringa` | Jeringa | poco comun | aplicar medicina o veneno |

## 8. Plantas, hongos y alimentos vegetales

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `raiz_comestible` | Raiz comestible | comun | comida basica |
| `raiz_toxica` | Raiz toxica | poco comun | veneno o medicina procesada |
| `bayas_comestibles` | Bayas comestibles | comun | comida rapida |
| `bayas_venenosas` | Bayas venenosas | poco comun | trampa, veneno |
| `hongos_comestibles` | Hongos comestibles | comun | comida |
| `hongos_alucinogenos` | Hongos alucinogenos | raro | confusion, miedo, ritual |
| `hojas_grandes` | Hojas grandes | comun | envolver comida, techo, camuflaje |
| `flores_raras` | Flores raras | raro | antidotos, medicina avanzada |
| `frutas` | Frutas | comun | comida, hidratacion menor |
| `verduras_silvestres` | Verduras silvestres | comun | comida simple |
| `semillas` | Semillas | comun | comida, cultivo, trueque |
| `grano` | Grano | comun | comida, harina |
| `harina` | Harina | poco comun | cocinar |
| `especias` | Especias | poco comun | cocina, comercio |

## 9. Comida animal y conservas

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `carne_cruda` | Carne cruda | comun | comida con riesgo, cocinar |
| `carne_cocida` | Carne cocida | comun | comida segura |
| `carne_seca` | Carne seca | poco comun | comida conservada |
| `carne_podrida` | Carne podrida | comun | cebo, enfermedad |
| `pescado_crudo` | Pescado crudo | comun | comida con riesgo |
| `pescado_seco` | Pescado seco | poco comun | comida conservada |
| `huevos` | Huevos | comun | comida fragil |
| `leche` | Leche | comun | alimento perecedero |
| `queso` | Queso | poco comun | alimento duradero |
| `lata_comida` | Lata de comida | comun | comida segura |
| `lata_pequena` | Lata pequena | comun | comida ligera |
| `racion_basica` | Racion basica | comun | comida de emergencia |
| `galletas_secas` | Galletas secas | comun | comida liviana |
| `miel` | Miel | poco comun | energia, medicina leve |
| `sal` | Sal | comun | conservar carne/pescado |

## 10. Partes de animales

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `piel` | Piel | comun | abrigo, cuero |
| `cuero_curtido` | Cuero curtido | poco comun | proteccion, correas, mochilas |
| `huesos` | Huesos | comun | agujas, anzuelos, puntas futuras |
| `tendones` | Tendones | poco comun | cuerda fuerte |
| `grasa_animal` | Grasa animal | comun | cocina, combustible, unguentos |
| `sangre` | Sangre | comun | cebo, ritual, rastro |
| `cuernos` | Cuernos | poco comun | herramienta, trueque |
| `colmillos` | Colmillos | poco comun | puntas, trofeo |
| `plumas` | Plumas | comun | senuelos, flechas futuras |
| `lana` | Lana | comun | abrigo, ropa |
| `veneno_serpiente` | Veneno de serpiente | raro | veneno, antidoto procesado |
| `piel_reptil` | Piel de reptil | poco comun | cuero resistente |

## 11. Tecnologia y electronica

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `circuito_roto` | Circuito roto | poco comun | piezas electronicas |
| `circuito_funcional` | Circuito funcional | raro | reparar puertas/radios |
| `chip_danado` | Chip danado | raro | tecnologia avanzada si se repara |
| `placa_madre_rota` | Placa madre rota | raro | fuente de piezas |
| `fusible` | Fusible | poco comun | activar sistemas |
| `sensor` | Sensor | raro | alarmas, trampas automaticas |
| `camara_rota` | Camara rota | raro | vigilancia o piezas opticas |
| `radio_rota` | Radio rota | poco comun | comunicacion si se repara |
| `radio_funcional` | Radio funcional | raro | comunicacion |
| `antena` | Antena | poco comun | senal, rastreo |
| `gps_roto` | GPS roto | raro | orientacion si se repara |
| `linterna` | Linterna | poco comun | exploracion |
| `bombilla_led` | Bombilla / LED | comun | senal, trampa visual |
| `motor_electrico` | Motor electrico | raro | puertas, generadores pequenos |
| `bobina_cobre` | Bobina de cobre | poco comun | electricidad |
| `iman` | Iman | poco comun | mecanismos |
| `dron_roto` | Dron roto | muy raro | piezas raras |

## 12. Herramientas no clasificadas como armas

Algunas herramientas pueden usarse como armas improvisadas, pero en este catalogo
cuentan como herramientas de progreso.

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `martillo` | Martillo | comun | construir, reparar |
| `serrucho` | Serrucho | comun | cortar madera |
| `pico_mineria` | Pico de mineria | poco comun | extraer piedra/mineral |
| `pala` | Pala | comun | excavar, enterrar, trampas |
| `alicate` | Alicate | poco comun | alambre, electronica |
| `destornillador` | Destornillador | comun | reparaciones |
| `llave_inglesa` | Llave inglesa | poco comun | mecanica |
| `aguja` | Aguja | comun | suturas, ropa |
| `anzuelo` | Anzuelo | comun | pesca |
| `encendedor` | Encendedor | poco comun | fuego |
| `lupa` | Lupa | poco comun | fuego, investigacion |
| `brujula` | Brujula | poco comun | orientacion |
| `mapa_mojado` | Mapa mojado | comun | pista incompleta |
| `mapa_viejo` | Mapa viejo | poco comun | exploracion |
| `mapa_parcial` | Mapa parcial | raro | rutas/secretos |
| `diario_farero` | Diario del farero | raro | lore, regla del faro |
| `diario_ocultista` | Diario ocultista | raro | monolitos, rituales |
| `documento_tecnico` | Documento tecnico | raro | recetas avanzadas |
| `lente_agrietada` | Lente agrietada | raro | faro, senal, reparacion optica |
| `lista_nombres_tachados` | Lista de nombres tachados | raro | pista social, paranoia, lore |
| `mochila_danada` | Mochila danada | poco comun | transportar objetos si se repara |

## 13. Vehiculos, barcos y piezas grandes

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `rueda` | Rueda | poco comun | vehiculos, barricadas |
| `motor_pequeno` | Motor pequeno | raro | generador, bote |
| `motor_vehiculo` | Motor de vehiculo | muy raro | vehiculo |
| `bujia` | Bujia | poco comun | encendido |
| `correa_motor` | Correa de motor | poco comun | reparacion |
| `filtro_aire` | Filtro de aire | poco comun | vehiculo |
| `radiador` | Radiador | raro | motor |
| `cadena_moto` | Cadena de moto | raro | vehiculo, mecanismo |
| `helice` | Helice | raro | barco, ventilacion |
| `timon` | Timon | raro | barco |
| `vela_barco` | Vela de barco | poco comun | navegacion, tela grande |
| `ancla_pequena` | Ancla pequena | poco comun | peso, bloqueo |
| `barril` | Barril | comun | agua, combustible, flotacion |
| `cuerda_marina` | Cuerda marina | poco comun | barco, carga |
| `madera_naval` | Madera naval | poco comun | reparar bote/refugio |

## 14. Reliquias, llaves y objetos narrativos

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `reliquia_antigua` | Reliquia antigua | raro | activar guardian, trueque peligroso |
| `llave_antigua` | Llave antigua | raro | abrir ruinas/cofres |
| `llave_oxidada` | Llave oxidada | poco comun | sotanos, puertas viejas |
| `tarjeta_rota` | Tarjeta rota | raro | tecnologia militar |
| `llave_electronica` | Llave electronica | muy raro | compuertas |
| `amuleto_roto` | Amuleto roto | poco comun | ritual, trueque |
| `amuleto_solar` | Amuleto solar | raro | templo del sol |
| `gema_opaca` | Gema opaca | raro | ruinas, comercio |
| `estrella_falsa` | Estrella falsa | raro | engano social |
| `estrella_contaminada` | Estrella contaminada | muy raro | progreso con riesgo |
| `estrella_protegida` | Estrella protegida | muy raro | objetivo mayor |
| `moneda_vieja` | Moneda vieja | comun | trueque, coleccion |
| `joya` | Joya | raro | trueque |
| `nucleo_oxidado` | Nucleo oxidado | muy raro | maquina antigua |

## 15. Conocimiento, libros y escritura

Estos objetos conectan habilidades, recetas y aprendizaje. El sistema completo
esta descrito en `HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md` y en
`data/skill_books_and_recipe_knowledge.json`.

| ID | Nombre | Rareza | Usos |
| --- | --- | --- | --- |
| `manual_primeros_auxilios` | Manual de primeros auxilios | comun | desbloquear medicina basica, vendas |
| `guia_plantas_isla` | Guia de plantas de la isla | poco comun | botanica, herbolaria, identificacion |
| `manual_supervivencia_humeda` | Manual de supervivencia humeda | comun | fogata, filtro de agua, campamento |
| `manual_radio_faro` | Manual de radio del faro | poco comun | reparar radio, entender antenas |
| `manual_generadores` | Manual de generadores pequenos | raro | generadores, energia, mecanica |
| `guia_cableado_militar` | Guia de cableado militar | raro | electronica, compuertas, sensores |
| `manual_trampas_caza` | Manual de trampas de caza | poco comun | lazos, pinchos, alarmas |
| `diario_ocultista` | Diario ocultista | raro | monolitos, rituales, rutas ocultas |
| `documento_tecnico_minas` | Documento tecnico de minas | raro | tren, vagon, monoriel |
| `codice_estrellas` | Codice de estrellas contaminadas | muy raro | purificacion, lanza de estrella, pactos |
| `papel_suelto` | Papel suelto | comun | copiar recetas, notas, mapas simples |
| `cuaderno_mojado` | Cuaderno mojado | comun | pistas danadas, restaurar documento |
| `cuaderno_seco` | Cuaderno seco | poco comun | varias recetas, bitacora personal |
| `lapiz` | Lapiz | comun | escribir sin tinta, mapas, recetas |
| `lapicera` | Lapicera | comun | copiar recetas rapido |
| `pluma` | Pluma | comun | escritura fina o ritual |
| `tinta` | Tinta | poco comun | copiar recetas legibles |
| `carboncillo` | Carboncillo | comun | marcas, mapas, apuntes incompletos |
| `tiza` | Tiza | comun | marcas de pared, simbolos, rutas |
| `sello_cera` | Sello de cera | raro | autenticar documento, pacto, falsificacion |
| `mapa_en_blanco` | Mapa en blanco | poco comun | crear mapa anotado |
| `receta_escrita` | Receta escrita | variable | transferir conocimiento de crafting |
| `receta_suelta` | Receta suelta | variable | hallazgo de una receta puntual |
| `receta_escrita_tecnica` | Receta escrita tecnica | raro | transferir receta avanzada o reparacion |
| `apunte_incompleto` | Apunte incompleto | comun | pista parcial, deduccion, riesgo de error |
| `manual_corto_artesanal` | Manual corto artesanal | poco comun | compartir varias recetas relacionadas |
| `receta_falsa` | Receta falsa | variable | estafa, sabotaje, guerra social |
| `mapa_anotado` | Mapa anotado | poco comun | rutas, peligros, zonas de recurso |

## Estados posibles

Un objeto puede tener modificadores:

- `limpio`;
- `sucio`;
- `contaminado`;
- `fresco`;
- `podrido`;
- `seco`;
- `humedo`;
- `roto`;
- `reparado`;
- `oxidado`;
- `refinado`;
- `cargado`;
- `descargado`;
- `sellado`;
- `maldito`.

## Lista corta para el sandbox de 4 casillas

Para la primera demo no hace falta cargar todo. Usaria:

| Casilla | Loot comun | Loot raro |
| --- | --- | --- |
| 1 Faro | `agua_limpia`, `bengala`, `aceite_lampara`, `cable_electrico`, `mapa_mojado` | `lente_agrietada`, `diario_farero`, `bateria_pequena` |
| 2 Campamento | `rama_seca`, `tela`, `cuerda_fina`, `lata_comida`, `pedernal`, `agua_limpia` | `venda_limpia`, `mochila_danada`, `lista_nombres_tachados` |
| 6 Monolitos | `piedra_tallada`, `hierbas_secas`, `polvo_mineral`, `amuleto_roto` | `fragmento_estrella`, `diario_ocultista`, `polvo_ritual` |
| 7 Ruinas | `cuerda_vieja`, `placa_metalica`, `gema_opaca`, `mapa_parcial` | `reliquia_antigua`, `llave_antigua`, `estrella_protegida` |

## Siguiente paso

Cuando esta lista sea aprobada, conviene convertirla a:

```txt
data/items_resources.json
```

Ese JSON sera el catalogo que el bot pueda usar para loot, trueque, inventarios,
crafting y apuestas sobre objetos encontrados.
