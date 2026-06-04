# Hell Games - Guia de libros, habilidades y recetas

Guia practica del sistema de conocimiento: libros, manuales, folletos, recetas escritas, herramientas de escritura y su relacion con habilidades.

Regla central: **Los libros desbloquean conocimiento; la practica desbloquea dominio; la presion desbloquea experiencia real.**

## Capas de conocimiento

- `intuicion`
- `lectura`
- `receta_escrita`
- `practica`
- `dominio`
- `secreto`

## Habilidad de escritura

La escritura funciona como microhabilidad de apoyo. No reemplaza habilidades tecnicas: permite copiar, conservar, falsificar o transferir conocimiento.

| Herramienta | Mejor uso | Limites |
| --- | --- | --- |
| `carbon_vegetal` | marcas, mapa_tosco, restaurar_documento_mojado | no_recetas_tecnicas_claras, legibilidad_baja |
| `carboncillo` | apunte_incompleto, mapa_anotado, receta_simple_tosca | manchas, detalle_limitado |
| `lapiz` | receta_simple, mapa_anotado, nota_corregible | requiere_papel_relativamente_seco |
| `lapicera` | copia_rapida, receta_tecnica_simple | falla_mojada, tinta_limitada |
| `pluma_tinta` | receta_tecnica, documento_ritual, documento_legible | lenta, fragil, requiere_tinta |
| `tiza` | marcas_pared, simbolos, rutas_temporales | no_conserva_recetas_en_inventario |

## Libros y manuales

| Nivel | ID | Nombre | Habilidades | Lectura | Desbloquea | Zonas | Piloto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| basico | `guia_plantas_isla` | Guia de plantas de la isla | botanica, herbolaria, recolectar | 3h | identificar_hierbas, unguento_medicinal | 4 Cascada, 11 Pantano, 17 Templo de la Luna, 23 Jungla | No prioritario en piloto; puede aparecer por loot, NPC o evento. |
| basico | `manual_conservacion_alimentos` | Manual de conservacion de alimentos | cocina, supervivencia | 3h | secar_carne, racion_conservada | 2 Campamento, 5 Puerto, 14 Granja, 21 Muelle, 22 Pueblo Nevado | No prioritario en piloto; puede aparecer por loot, NPC o evento. |
| basico | `manual_primeros_auxilios` | Manual de primeros auxilios | medicina | 3h | venda_improvisada | 1 Faro, 2 Campamento, 17 Templo de la Luna, 19 Estacion Militar | Casilla 2. Curacion leve y venda improvisada. |
| basico | `manual_supervivencia_humeda` | Manual de supervivencia en clima humedo | supervivencia | 3h | hacer_fogata, filtrar_agua_basico | 2 Campamento, 4 Cascada, 11 Pantano, 23 Jungla | Casilla 2. Fogata, filtro y agua segura. |
| intermedio | `guia_suturas_fracturas` | Guia de suturas y fracturas | medicina | 5h | venda_desinfectada | 17 Templo de la Luna, 19 Estacion Militar | No prioritario en piloto; puede aparecer por loot, NPC o evento. |
| intermedio | `herbario_pantano` | Herbario del pantano | botanica, quimica | 5h | veneno_basico, evitar_plantas_toxicas | 11 Pantano, 12 Sector X | No prioritario en piloto; puede aparecer por loot, NPC o evento. |
| intermedio | `manual_generadores` | Manual de generadores pequenos | mecanica, electronica | 6h | generador_pequeno | 3 Minas, 13 Torre, 19 Estacion Militar | No prioritario en piloto; puede aparecer por loot, NPC o evento. |
| intermedio | `manual_radio_faro` | Manual de radio del faro | electronica, mecanica | 5h | reparar_radio_faro | 1 Faro, 20 Observatorio | Casilla 1. Permite reparar radio/faro si hay piezas. |
| intermedio | `manual_trampas_caza` | Manual de trampas de caza | trampas, caza, supervivencia | 5h | montar_trampa_lazo, montar_pinchos_ocultos | 2 Campamento, 7 Ruinas, 14 Granja, 23 Jungla | No prioritario en piloto; puede aparecer por loot, NPC o evento. |
| avanzado | `diario_ocultista` | Diario ocultista | ocultismo, investigacion | 6h | activar_monolito_menor, abrir_ruta_salida_oculta | 6 Monolitos, 7 Ruinas, 15 Templo del Sol | Casilla 6. Pista incompleta de monolito. |
| avanzado | `documento_tecnico_minas` | Documento tecnico de minas | mecanica, electronica | 8h | activar_vagon_mina, reparar_tren_mina, activar_monoriel_abandonado | 3 Minas, 20 Observatorio | No prioritario en piloto; puede aparecer por loot, NPC o evento. |
| avanzado | `guia_cableado_militar` | Guia de cableado militar | electronica, informatica | 8h | abrir_compuerta_electrica, panel_solar_reparado | 13 Torre, 19 Estacion Militar, 20 Observatorio | No prioritario en piloto; puede aparecer por loot, NPC o evento. |
| avanzado | `manual_embarcaciones` | Manual de reparacion de embarcaciones | mecanica, navegar | 8h | reparar_balsa, reparar_bote_motor | 5 Puerto, 16 Costa, 21 Muelle | No prioritario en piloto; puede aparecer por loot, NPC o evento. |
| avanzado | `tratado_toxicologia` | Tratado de toxicologia aplicada | medicina, quimica | 8h | antidoto_basico, veneno_basico | 11 Pantano, 12 Sector X, 17 Templo de la Luna, 19 Estacion Militar | No prioritario en piloto; puede aparecer por loot, NPC o evento. |
| experto | `codice_estrellas` | Codice de estrellas contaminadas | ocultismo, ciencias | 12h | purificar_estrella_contaminada, forjar_lanza_estrella | 6 Monolitos, 12 Sector X, 15 Templo del Sol, 25 Volcan | No prioritario en piloto; puede aparecer por loot, NPC o evento. |

## Materiales de escritura y documentos

| ID | Nombre | Rareza | Usos | Piloto |
| --- | --- | --- | --- | --- |
| `papel_suelto` | Papel suelto | comun | copiar_receta_simple, nota, mapa_simple | Casilla 2. Base para copiar recetas simples. |
| `cuaderno_mojado` | Cuaderno mojado | comun | pistas_danadas, restaurar_documento_mojado | Puede aparecer como soporte de copia, comercio o pista. |
| `cuaderno_seco` | Cuaderno seco | poco_comun | varias_recetas, bitacora_personal | Puede aparecer como soporte de copia, comercio o pista. |
| `lapiz` | Lapiz | comun | copiar_receta_simple, mapa_anotado | Casilla 2. Escritura simple resistente y corregible. |
| `lapicera` | Lapicera | comun | copiar_receta_simple, copiar_receta_tecnica | Puede aparecer como soporte de copia, comercio o pista. |
| `pluma` | Pluma | comun | escritura_ritual, copiar_receta_tecnica | Puede aparecer como soporte de copia, comercio o pista. |
| `tinta` | Tinta | poco_comun | copiar_receta_tecnica, documento_legible | Puede aparecer como soporte de copia, comercio o pista. |
| `carboncillo` | Carboncillo | comun | apunte_incompleto, mapa_anotado, marcas | Casillas 2, 6 o 7. Mapas toscos, marcas y apuntes incompletos. |
| `tiza` | Tiza | comun | marcas_pared, simbolos, rutas | Casillas 6 o 7. Marcas de ruta o simbolos temporales. |
| `sello_cera` | Sello de cera | raro | autenticar_documento, pacto | Puede aparecer como soporte de copia, comercio o pista. |
| `mapa_en_blanco` | Mapa en blanco | poco_comun | mapa_anotado | Puede aparecer como soporte de copia, comercio o pista. |
| `receta_escrita` | Receta escrita | variable | transferir_conocimiento | Casilla 7. Transferencia de receta puntual. |
| `receta_suelta` | Receta suelta | variable | desbloquear_receta_puntual | Casilla 7. Puede revelar trampa de lazo u otra receta puntual. |
| `receta_escrita_tecnica` | Receta escrita tecnica | raro | transferir_receta_avanzada | Puede aparecer como soporte de copia, comercio o pista. |
| `apunte_incompleto` | Apunte incompleto | comun | deduccion, pista_parcial | Casilla 6 o 7. Pista parcial con riesgo de error. |
| `manual_corto_artesanal` | Manual corto artesanal | poco_comun | compartir_recetas_relacionadas | Puede aparecer como soporte de copia, comercio o pista. |
| `receta_falsa` | Receta falsa | variable | estafa, sabotaje, guerra_social | Puede aparecer como soporte de copia, comercio o pista. |

## Recetas de escritura y copia

| ID | Resultado | Ingredientes | Estacion | Tiempo | Riesgo | Desbloqueo |
| --- | --- | --- | --- | --- | --- | --- |
| `preparar_carboncillo` | carboncillo | carbon_vegetal|rama_quemada, tela|corteza | fogata_o_refugio | 0.5h | bajo | supervivencia_basica |
| `copiar_receta_simple` | receta_escrita | papel_suelto, lapiz|lapicera, receta_conocida | ninguna | 1h | bajo | saber_receta_original |
| `copiar_receta_tecnica` | receta_escrita_tecnica | cuaderno_seco, lapicera|pluma+tinta, receta_tecnica_conocida | mesa_campamento | 2h | medio | habilidad_relacionada_baja_o_media |
| `crear_apunte_incompleto` | apunte_incompleto | papel_suelto, carboncillo | ninguna | 0.5h | medio | observar_intento_o_fallo |
| `crear_manual_corto` | manual_corto_artesanal | cuaderno_seco, herramienta_escritura, tres_recetas_relacionadas | mesa_campamento | 4h | medio | habilidad_media |
| `dibujar_mapa_receta` | mapa_anotado | mapa_en_blanco|mapa_mojado, carboncillo|lapiz, ruta_conocida | mesa_campamento | 1h | bajo | explorar_ruta |
| `falsificar_receta` | receta_falsa | papel_suelto, tinta|lapicera | ninguna | 1h | alto_social | mentir_o_hurtar |
| `restaurar_documento_mojado` | documento_legible_parcial | cuaderno_mojado, tela, carbon_vegetal, refugio_seco | mesa_campamento | 2h | medio | educacion_o_investigacion |

## Assets

- `assets/skills y mats/hellgames_knowledge_sets/icons_by_id/`
- `assets/skills y mats/hellgames_knowledge_sets/knowledge_sets_manifest.json`
- `assets/skills y mats/hellgames_knowledge_sets/icons_index.json`