# Hell Games - Libros, habilidades y recetas

Documento puente entre:

- `doc_hability1.md`: tabla base de habilidades.
- `doc_habilidades2.md`: aprendizaje con libros, practica y experiencia real.
- `HELL_GAMES_RECETAS_CRAFTING.md`: recetas, estaciones y desbloqueo.
- `HELL_GAMES_OBJETOS_RECURSOS.md`: materiales e insumos.

La idea principal:

> Los libros desbloquean conocimiento.  
> La practica desbloquea dominio.  
> La presion desbloquea experiencia real.

Un personaje puede leer para entender una tecnica, pero no deberia volverse
experto solo por esconderse con libros. El libro abre puertas; la isla cobra el
precio cuando intenta aplicarlo.

## 1. Capas de conocimiento

| Capa | Que representa | Ejemplo | Efecto |
| --- | --- | --- | --- |
| `intuicion` | Saber comun o improvisacion basica | hacer una fogata torpe | permite intentar acciones simples |
| `lectura` | Libro/manual leido parcialmente | primeros auxilios | desbloquea recetas o reduce riesgo |
| `receta_escrita` | Instruccion concreta encontrada o copiada | filtro portatil | permite fabricar si hay ingredientes |
| `practica` | Haberlo hecho en escena real | vendar a alguien herido | sube chance de exito |
| `dominio` | Habilidad consolidada | medico de campo | reduce tiempo, riesgo y consumo |
| `secreto` | Conocimiento unico de NPC, zona o evento | activar monolito | desbloquea rutas, pactos o finales |

## 2. Que habilidades deberian tener libros

No todas necesitan libros propios. Algunas pueden tener apuntes utiles, pero el
progreso real debe venir de practicar.

| Habilidad | Libro recomendado | Practica requerida | Comentario |
| --- | --- | --- | --- |
| Medicina | alta | media/alta | libros desbloquean vendas, suturas, antidotos |
| Botanica / herbolaria | alta | media | reduce errores con plantas y hongos |
| Quimica | alta | media | poderosa, con riesgo de accidente |
| Mecanica | alta | alta | requiere herramientas, piezas y tiempo |
| Electronica / informatica | alta | media/alta | radios, puertas, sensores, torre |
| Supervivencia | media | alta | fuego, refugio, agua, campamento |
| Cocina / conservacion | alta | media | comida segura, raciones, moral |
| Trampas | media | alta | libro ayuda, pero montar mal puede herir al usuario |
| Construccion / carpinteria | media | alta | refugios, puentes, barricadas |
| Herreria / fundicion | media | alta | requiere estacion, ruido y recursos |
| Cartografia / navegacion | alta | media | mapas, rutas, barco, monoriel |
| Ocultismo | alta | media | monolitos, reliquias, rituales |
| Estrategia / tactica | media | media | emboscadas, lectura de riesgos |
| Psicologia / negociacion | media | alta/social | mejora lectura social, no reemplaza interaccion |
| Pelear / armas blancas | baja | alta | libros solo desbloquean tecnicas |
| Punteria / armas de fuego | media | alta | manual ayuda a seguridad y mantenimiento |
| Fuerza, resistencia, agilidad | muy baja | muy alta | casi todo es entrenamiento fisico |

## 3. Tipos de libros y documentos

| Tipo | Rareza | Tiempo | Efecto |
| --- | --- | --- | --- |
| `folleto` | comun | 1h | pista menor o +1 intento seguro |
| `manual_basico` | comun/poco comun | 3h | nulo -> bajo o desbloquea receta simple |
| `guia_intermedia` | poco comun | 5h | bajo -> medio si hay practica minima |
| `manual_avanzado` | raro | 8h | desbloquea receta/tecnica avanzada |
| `tratado_experto` | muy raro | 12h+ | desbloquea proyectos o reduce riesgos altos |
| `plano_tecnico` | raro | variable | desbloquea reparaciones/proyectos concretos |
| `diario_npc` | raro | variable | revela receta incompleta, ruta o condicion |
| `receta_suelta` | comun/raro | 0.5h | enseña una receta puntual |
| `apunte_incompleto` | comun | 1h | requiere deduccion, NPC o segundo documento |

## 4. Objetos de conocimiento sugeridos

Estos objetos conviene sumarlos luego al catalogo de recursos/objetos.

### Libros y manuales

| ID | Nombre | Habilidad | Nivel | Desbloquea |
| --- | --- | --- | --- | --- |
| `manual_primeros_auxilios` | Manual de primeros auxilios | medicina | basico | `venda_improvisada`, diagnostico leve |
| `guia_suturas_fracturas` | Guia de suturas y fracturas | medicina | intermedio | `venda_desinfectada`, estabilizar herida |
| `tratado_toxicologia` | Tratado de toxicologia aplicada | medicina/quimica | avanzado | `antidoto_basico`, venenos procesados |
| `guia_plantas_isla` | Guia de plantas de la isla | botanica | basico | identificar hierbas, bayas, hongos |
| `herbario_pantano` | Herbario del pantano | botanica/quimica | intermedio | `veneno_basico`, evitar plantas toxicas |
| `manual_supervivencia_humeda` | Manual de supervivencia en clima humedo | supervivencia | basico | `hacer_fogata`, `filtrar_agua_basico` |
| `manual_trampas_caza` | Manual de trampas de caza | trampas/caza | intermedio | `montar_trampa_lazo`, `montar_pinchos_ocultos` |
| `manual_generadores` | Manual de generadores pequenos | mecanica | intermedio | `generador_pequeno` |
| `manual_radio_faro` | Manual de radio del faro | electronica/mecanica | intermedio | `reparar_radio_faro` |
| `guia_cableado_militar` | Guia de cableado militar | electronica/informatica | avanzado | `abrir_compuerta_electrica` |
| `manual_conservacion_alimentos` | Manual de conservacion de alimentos | cocina/supervivencia | basico | `secar_carne`, `racion_conservada` |
| `manual_embarcaciones` | Manual de reparacion de embarcaciones | mecanica/navegar | avanzado | `reparar_balsa`, pistas de barco |
| `documento_tecnico_minas` | Documento tecnico de minas | mecanica/electronica | avanzado | `activar_monoriel_abandonado` |
| `diario_ocultista` | Diario ocultista | ocultismo | avanzado | `activar_monolito_menor` |
| `codice_estrellas` | Codice de estrellas contaminadas | ocultismo/ciencias | experto | `purificar_estrella_contaminada`, pactos |

### Materiales de escritura

| ID | Nombre | Rareza | Uso |
| --- | --- | --- | --- |
| `papel_suelto` | Papel suelto | comun | escribir receta, nota o mapa simple |
| `cuaderno_mojado` | Cuaderno mojado | comun | guardar apuntes con riesgo de perder texto |
| `cuaderno_seco` | Cuaderno seco | poco comun | varias recetas o bitacora personal |
| `lapiz` | Lapiz | comun | escribir sin tinta, se gasta poco |
| `lapicera` | Lapicera | comun | escribir rapido, puede fallar si mojada |
| `pluma` | Pluma | comun/poco comun | escritura ritual o fina |
| `tinta` | Tinta | poco comun | copiar recetas legibles |
| `carboncillo` | Carboncillo | comun | marcas, mapas, receta tosca |
| `tiza` | Tiza | comun | marcas de pared, simbolos, rutas |
| `sello_cera` | Sello de cera | raro | autenticar documento o pacto |
| `mapa_en_blanco` | Mapa en blanco | poco comun | crear mapa anotado |
| `receta_escrita` | Receta escrita | variable | item de conocimiento transferible |
| `receta_suelta` | Receta suelta | variable | receta encontrada como hoja, folleto o recorte |

### Habilidad de escritura y documentacion

No hace falta que `escritura` sea una habilidad mayor al inicio. Puede funcionar
como microhabilidad de apoyo, modificada por `Ciencias`, `Investigacion`,
`Cartografia`, `Ocultismo`, `Mecanica`, `Medicina` o la habilidad tecnica que
corresponda a la receta.

| Herramienta | Sirve para | Limite recomendado |
| --- | --- | --- |
| `carbon_vegetal` | marcas grandes, mapas toscos, secar/restaurar papel | no alcanza para recetas tecnicas claras |
| `carboncillo` | apuntes incompletos, mapas, receta simple tosca | puede mancharse o perder detalle |
| `lapiz` | recetas simples, mapas, notas corregibles | necesita papel relativamente seco |
| `lapicera` | copiar rapido recetas simples o tecnicas | falla si esta mojada o sin tinta |
| `pluma` + `tinta` | documentos legibles, rituales, recetas tecnicas | lento, fragil, requiere tinta |
| `tiza` | marcas de pared, simbolos, rutas temporales | no sirve para conservar recetas en inventario |
| `sello_cera` | autenticar, pactar, falsificar o proteger documentos | no crea conocimiento por si solo |

Regla simple: una receta escrita tiene calidad. `tosca` permite intentarla con
penalizacion, `clara` funciona normal, `tecnica` exige habilidad compatible, y
`codificada` exige clave, ocultismo o investigacion.

## 5. Recetas de escritura y copia

Estas recetas no fabrican objetos fisicos poderosos por si mismas; fabrican
conocimiento transferible.

| ID | Resultado | Ingredientes | Estacion | Tiempo | Riesgo | Desbloqueo |
| --- | --- | --- | --- | --- | --- | --- |
| `preparar_carboncillo` | `carboncillo` | `carbon_vegetal` o rama quemada, `tela` o `corteza` | fogata/refugio | 0.5h | bajo | supervivencia basica |
| `copiar_receta_simple` | `receta_escrita` | `papel_suelto`, `lapiz` o `lapicera`, receta conocida | ninguna | 1h | bajo | saber receta original |
| `copiar_receta_tecnica` | `receta_escrita_tecnica` | `cuaderno_seco`, `lapicera` o `pluma`+`tinta`, receta tecnica conocida | mesa_campamento | 2h | medio | habilidad relacionada baja/media |
| `crear_apunte_incompleto` | `apunte_incompleto` | `papel_suelto`, `carboncillo` | ninguna | 0.5h | medio | observar intento o fallo |
| `crear_manual_corto` | `manual_corto_artesanal` | `cuaderno_seco`, herramienta de escritura, 3 recetas conocidas relacionadas | mesa_campamento | 4h | medio | habilidad media |
| `dibujar_mapa_receta` | `mapa_anotado` | `mapa_en_blanco` o `mapa_mojado`, `carboncillo`, ruta conocida | mesa_campamento | 1h | bajo | explorar ruta |
| `falsificar_receta` | `receta_falsa` | `papel_suelto`, tinta o lapicera | ninguna | 1h | alto social | mentir/hurtar |
| `restaurar_documento_mojado` | documento legible parcial | `cuaderno_mojado`, `tela`, `carbon_vegetal`, refugio seco | mesa_campamento | 2h | medio | educacion/investigacion |

Regla para `receta_falsa`: no debe ser solo troll. Puede servir para estafa,
emboscada o guerra psicologica, pero si se descubre afecta reputacion y puede
causar accidente al que la use.

## 5.1. Assets visuales

Los iconos generados para este sistema estan en:

- `assets/skills y mats/hellgames_knowledge_sets/hellgames_conocimiento_01_libros_manuales.png`
- `assets/skills y mats/hellgames_knowledge_sets/hellgames_conocimiento_02_escritura_documentos.png`
- `assets/skills y mats/hellgames_knowledge_sets/icons_by_id/`
- `assets/skills y mats/hellgames_knowledge_sets/knowledge_sets_manifest.json`
- `assets/skills y mats/hellgames_knowledge_sets/guide/GUIA_LIBROS_HABILIDADES_HELLGAMES.pdf`

## 6. Como se desbloquean las recetas

Cada receta deberia tener una fuente de desbloqueo:

| Modo | Uso |
| --- | --- |
| `conocida_inicio` | recetas basicas: fogata, venda simple, lanza casera |
| `habilidad_basica` | el personaje ya sabe por trasfondo |
| `manual_basico` | libro comun desbloquea la receta |
| `manual_avanzado` | requiere lectura + habilidad previa |
| `plano_tecnico` | proyecto concreto: radio, generador, monoriel |
| `diario_npc` | lore o receta parcial |
| `maestro_npc` | Sira, Verek, medica, tecnico u otro NPC enseña |
| `deduccion` | inteligencia/ciencias/investigacion permite inferir |
| `experimentacion` | probar con materiales, riesgo de fallo |
| `evento_guardian` | ruinas, monolitos, estrellas o jefes |

## 7. Crear recetas nuevas durante el juego

Un personaje puede crear una receta si cumple una de estas condiciones:

1. Tiene habilidad media o superior en el area.
2. Tiene un libro/manual relacionado.
3. Ya fabrico algo parecido antes.
4. Presencio o estudio una receta en uso.
5. Tiene materiales de escritura para dejarla registrada.

La receta creada puede tener estados:

| Estado | Significado |
| --- | --- |
| `clara` | otro personaje puede usarla sin penalizacion |
| `incompleta` | requiere deduccion, NPC o intento extra |
| `peligrosa` | funciona, pero aumenta riesgo |
| `falsa` | no funciona o causa accidente |
| `codificada` | requiere idioma, ocultismo o clave |
| `mojada_danada` | se entiende parcialmente |

## 8. Ejemplos conectados a recetas actuales

| Receta | Libro o conocimiento recomendado | Habilidad | Observacion |
| --- | --- | --- | --- |
| `hacer_fogata` | manual_supervivencia_humeda | supervivencia | conocida si supervivencia baja |
| `filtrar_agua_basico` | manual_supervivencia_humeda | supervivencia/ciencias | usa tela, carbon y arena |
| `venda_improvisada` | manual_primeros_auxilios | medicina | receta de inicio para medicos |
| `venda_desinfectada` | guia_suturas_fracturas | medicina | requiere alcohol medicinal |
| `unguento_medicinal` | guia_plantas_isla | botanica/medicina | Sira podria enseñarla |
| `veneno_basico` | herbario_pantano | botanica/quimica | riesgo alto sin practica |
| `antidoto_basico` | tratado_toxicologia | medicina/quimica | laboratorio recomendado |
| `kit_reparacion_basico` | guia_cableado_militar | mecanica/electronica | Renzo/Verek pueden saberlo |
| `reparar_radio_faro` | manual_radio_faro | electronica/mecanica | objetivo de casilla 1 |
| `generador_pequeno` | manual_generadores | mecanica | ruido y riesgo alto |
| `fabricar_lanza_casera` | manual_trampas_caza o intuicion | supervivencia/artesania | primer arma craftable |
| `montar_trampa_lazo` | manual_trampas_caza | trampas/caza | defensa sin combate directo |
| `activar_monolito_menor` | diario_ocultista | ocultismo | requiere condicion nocturna |
| `activar_monoriel_abandonado` | documento_tecnico_minas | mecanica/electronica | proyecto mayor |
| `forjar_lanza_estrella` | codice_estrellas | ocultismo/herreria | pacto o sacrificio |

## 9. Distribucion sugerida por isla

| Zona | Libros/documentos probables |
| --- | --- |
| 1 Faro | `manual_radio_faro`, `diario_farero`, mapas, cuadernos mojados |
| 2 Campamento | manuales basicos, papel, lapiz, recetas simples |
| 3 Minas | `documento_tecnico_minas`, notas de fundicion, planos de via |
| 4 Cascada | guia de plantas, notas de pesca, remedios naturales |
| 5 Puerto | manual de embarcaciones, cartas nauticas, recetas de reparacion |
| 6 Monolitos | diario ocultista, simbolos codificados, polvo ritual |
| 7 Ruinas | recetas codificadas, trampas antiguas, mapas parciales |
| 11 Pantano | herbario del pantano, toxicologia, notas sobre venenos |
| 12 Sector X | quimica avanzada, electronica experimental, documentos dañados |
| 13 Torre | manuales de seguridad, informatica, compuertas, sensores |
| 17 Templo de la Luna | medicina, acuerdos escritos, tratados de curacion |
| 19 Estacion Militar | manuales de armas, mecanica, radio, explosivos, tactica |
| 20 Observatorio | cartografia, astronomia, coordenadas, electronica |
| 23 Jungla | trampas de caza, herbolaria, supervivencia |
| 25 Volcan | fundicion, ceniza, cristal negro, rituales peligrosos |

## 10. Version piloto de 4 casillas

Para el piloto conviene usar pocos documentos:

| Casilla | Documento | Funcion |
| --- | --- | --- |
| 1 Faro | `manual_radio_faro` | permite `reparar_radio_faro` si hay piezas |
| 1 Faro | `diario_farero` | pista de luz nocturna y mapa anotado |
| 2 Campamento | `manual_primeros_auxilios` | `venda_improvisada` y curacion leve |
| 2 Campamento | `manual_supervivencia_humeda` | fogata, filtro, agua segura |
| 6 Monolitos | `diario_ocultista` incompleto | pista de `activar_monolito_menor` |
| 7 Ruinas | `receta_trampa_lazo` o marcas de trampa | enseña trampas si se sobrevive |

## 11. Regla simple para el bot

Cada actor puede tener:

```json
{
  "known_recipes": ["venda_improvisada"],
  "known_books": ["manual_primeros_auxilios"],
  "study_progress": {"manual_radio_faro": 2},
  "recipe_notes": ["receta_escrita:filtro_portatil"],
  "practice_log": {"medicina": 1, "mecanica": 0}
}
```

Al resolver una accion de fabricacion:

1. Ver si conoce la receta.
2. Si no la conoce, revisar libro, nota, NPC o habilidad compatible.
3. Ver si tiene ingredientes y estacion.
4. Aplicar bonificacion por habilidad/practica.
5. Aplicar riesgo por cansancio, miedo, clima, oscuridad o documento incompleto.
6. Si falla, decidir si pierde materiales, crea objeto defectuoso o aprende algo.
