Sí, totalmente. El mod más conocido es **Mantella**. Lo que hace no es “darle conciencia real” al NPC, sino conectar el juego con una cadena de IA:

**jugador habla/escribe → reconocimiento de voz → modelo de lenguaje → respuesta del NPC → voz generada → acción dentro del juego**

Mantella usa una arquitectura de **Speech-to-Text → LLM → Text-to-Speech**. Puede usar Whisper/Moonshine para pasar voz a texto, un LLM para generar la respuesta, y Piper/xVASynth/XTTS para convertir texto en voz. Además, tiene memoria persistente, conciencia de eventos del juego y hasta acciones limitadas dentro del mundo. ([GitHub][1])

La parte clave no es Skyrim en sí, sino el **puente** entre el juego y el modelo de IA. Mantella tiene un programa externo en Python que recibe contexto del juego, arma el prompt del NPC, manda la consulta al modelo y devuelve una respuesta que Skyrim puede mostrar o reproducir. En otras palabras: Skyrim no “piensa”; Skyrim le pasa información a un cerebro externo. ([Hacker News][2])

Para tu **Battle Royale de Discord**, esto sería incluso más fácil en algunos aspectos, porque no necesitamos voz, animaciones ni integración con un motor 3D. Podríamos usar la misma idea, pero en texto:

```text
Usuario escribe comando
↓
Bot mira estado del mapa, casilla, NPCs cercanos, inventario, heridas, clima, ruido, memoria
↓
Elige qué NPC debe reaccionar
↓
LLM genera intención / diálogo / pensamiento
↓
Sistema de reglas valida lo que puede hacer
↓
Bot publica o manda por DM el resultado
↓
Se guarda memoria y cambia el estado del mundo
```

La diferencia importante: **no conviene que el LLM controle todo directamente**. Si dejamos que la IA decida libremente, puede inventar objetos, teletransportarse, romper reglas o hacer cosas injustas. Lo mejor sería usar una arquitectura híbrida:

**1. Motor de reglas duro**
Este decide lo real: posición, vida, hambre, sed, inventario, heridas, permisos, visión, ruido, clima, casillas, puertas, estrellas, armas, munición.

**2. IA narrativa**
Esta decide cómo piensa, habla, justifica o interpreta el NPC. Por ejemplo: “Sira sospecha de Verek porque encontró cenizas recientes cerca del molino”.

**3. Sistema de intención**
La IA no debería decir “maté a Kevin y escapé en helicóptero”. Debería devolver algo como:

```json
{
  "intencion": "investigar_ruido",
  "objetivo": "casilla_norte",
  "tono": "cauteloso",
  "dialogo": "No me gusta ese sonido... voy a mirar desde lejos."
}
```

Después el motor comprueba si puede hacerlo: si tiene energía, si puede moverse, si no está herida, si conoce esa ruta, si hay peligro, etc.

Para tu Battle Royale, podríamos implementar algo inspirado en Mantella así:

```text
NPC = ficha fija
- nombre
- personalidad
- alineamiento
- miedos
- metas
- relaciones
- habilidades
- inventario
- memoria corta
- memoria larga
- estado emocional
- estado físico

Mundo = estado dinámico
- casilla actual
- clima
- hora
- sucesos recientes
- sonidos cercanos
- olores
- rastros
- cadáveres
- objetos visibles
- otros personajes presentes

IA = narrador/mente
- interpreta la situación
- elige intención
- genera diálogo
- resume memoria
```

Ejemplo aplicado:

```text
Contexto para Sira:
Estás en la casilla 8, bosque húmedo. Tienes hambre leve, una navaja oxidada y una botella de agua a la mitad. Escuchaste un disparo al oeste hace 20 minutos. Verek te mintió ayer sobre tener comida. Tu meta principal es sobrevivir evitando combate directo. Tu rasgo dominante es desconfianza.

Opciones válidas:
- esconderse
- moverse al norte
- buscar rastros
- hablar con Verek
- preparar trampa simple
- descansar

Devuelve una intención válida y una frase breve.
```

Respuesta de la IA:

```json
{
  "intencion": "buscar_rastros",
  "objetivo": "zona_oeste",
  "riesgo_aceptado": "bajo",
  "dialogo": "Si hubo un disparo, alguien dejó algo atrás. Pero no pienso acercarme sin mirar el suelo primero."
}
```

Luego el sistema tira dados/cálculos según habilidades: percepción, sigilo, rastreo, cansancio, heridas, clima, luz, etc.

Esto encaja muy bien con la idea que veníamos armando de **NPCs vivientes**, porque no hace falta que cada personaje tenga miles de diálogos escritos. Solo necesita una buena ficha, recuerdos y reglas. La IA rellena la parte humana: dudas, frases, excusas, paranoia, alianzas, traiciones.

Para memoria podríamos usar algo parecido a Mantella: resumir conversaciones anteriores y guardarlas por NPC. Mantella maneja memorias resumiendo conversaciones pasadas y guardándolas, para que el NPC pueda recordarlas después sin meter todo el historial completo cada vez. ([Hacker News][2])

Ejemplo de memoria de NPC:

```text
Memoria de Verek:
- Día 1: Sira lo vio escondiendo comida y desde entonces desconfía.
- Día 2: Oyó a Rex hablar de una ruta secreta cerca del tren.
- Día 3: Fue herido por una trampa de cuerda; ahora evita zonas con vegetación baja.
```

Y eso después afecta sus decisiones.

La versión más recomendable para tu proyecto sería empezar con **IA por turnos**, no en tiempo real. Por ejemplo:

Cada 1 hora real o cada “tick” del evento:

```text
1. El bot actualiza hambre/sed/cansancio.
2. Cada NPC evalúa su situación.
3. Elige una intención.
4. El motor valida.
5. Se resuelve la acción.
6. Se genera un resumen narrativo.
7. Se guarda memoria.
```

Así podrías tener 25, 50 o 100 NPCs sin que sea un caos. No todos necesitan usar IA todo el tiempo. Muchos pueden moverse con reglas simples, y solo usar LLM cuando ocurre algo interesante: encuentro, combate, traición, negociación, descubrimiento, muerte, evento raro.

Mi recomendación para el Battle Royale sería esta arquitectura:

```text
Discord Bot
↓
Game Engine propio
↓
Base de datos del mundo
↓
Sistema de reglas
↓
Módulo de IA
↓
Memoria de NPCs
↓
Narrador
```

Con módulos:

```text
/npc_estado
/npc_memoria
/npc_decision
/npc_dialogo
/npc_accion
/mundo_eventos
/jugador_comandos
/percepcion
```

Lo más potente sería que los usuarios no “hablen con ChatGPT directamente”, sino con **personajes limitados por el mundo**. Así se siente mágico, pero sigue siendo un juego justo.

Ejemplo:

Usuario:

```text
/observar sira
```

Bot:

```text
Sira está agachada junto a las raíces de un árbol. Tiene barro en las manos y mira hacia el oeste.

Parece haber encontrado huellas recientes.

Murmura:
"Alguien pasó por aquí... y no iba solo."
```

Usuario:

```text
/hablar sira "Puedo ayudarte, no busco pelea"
```

El sistema le pasa a la IA:

```text
Sira desconfía del usuario. Tiene hambre. Sabe que el usuario estuvo cerca del disparo. Está armada con navaja. No quiere combate directo.
```

Respuesta:

```text
Sira no baja la navaja.

"Eso diría cualquiera que quiere acercarse demasiado. Deja tu mochila en el suelo y hablamos."
```

Eso sería muy Mantella, pero adaptado a Discord.

Conclusión: **sí, podemos usar esa tecnología**, pero no como “poner ChatGPT dentro del NPC y ya”. Lo ideal es usar IA como **cerebro narrativo controlado**, con un motor de reglas que impida incoherencias. Para tu Battle Royale, sería incluso más viable que Skyrim porque todo ocurre por texto, embeds, comandos y estados guardados.

[1]: https://github.com/art-from-the-machine/Mantella?utm_source=chatgpt.com "Mantella is a Skyrim and Fallout 4 mod which ..."
[2]: https://news.ycombinator.com/item?id=37370815&utm_source=chatgpt.com "Show HN: Mantella – Talk to AI-Powered NPCs in Skyrim"




________________________

Sí, esa es la clave: **la IA no debe ser el dios del juego**, debe ser “el cerebro parcial” de cada NPC. El mundo y las reglas las controla tu bot.

Para tu Battle Royale, yo usaría una de estas 3 rutas:

## Opción 1: OpenRouter para empezar barato

Esta sería la más práctica para experimentar. OpenRouter te deja usar muchos modelos distintos desde una sola API, incluyendo modelos gratuitos o baratos, y también tiene un router de modelos gratis que selecciona modelos disponibles según lo que necesites, como JSON estructurado o tool calling. ([OpenRouter][1])

Para tu caso serviría porque podrías probar varios modelos sin reescribir todo el bot.

Ejemplo de uso:

```text
Discord Bot
↓
OpenRouter API
↓
Modelo barato/gratis
↓
Respuesta JSON del NPC
↓
Tu motor valida la acción
```

Ventaja: barato, flexible, ideal para pruebas.
Desventaja: los modelos gratis pueden cambiar, tener límites o responder con calidad variable.

Yo lo usaría para la **fase prototipo**.

---

## Opción 2: OpenAI API para estabilidad

Para una versión más seria, usaría un modelo pequeño/medio de OpenAI. Por ejemplo, **GPT-4.1 mini** aparece en la documentación de OpenAI con ventana de contexto grande y precio de referencia de **$0.40 por 1M tokens de entrada** y **$1.60 por 1M tokens de salida**. También la página muestra comparación con **GPT-5 mini** a menor costo de entrada. ([Desarrolladores OpenAI][2])

Esto te conviene si quieres que los NPCs respeten mejor instrucciones, devuelvan JSON más limpio y sean más consistentes.

Ventaja: más estable y confiable.
Desventaja: requiere pagar API.

Yo lo usaría para los NPCs importantes: líderes, traidores, personajes profundos, eventos dramáticos.

---

## Opción 3: Ollama local para pruebas sin pagar

Ollama permite correr modelos en tu propia PC, y su documentación incluye soporte para **tool calling** y **structured outputs**, o sea respuestas en formato controlado tipo JSON. ([Ollama Documentation][3])

Esto sirve si quieres probar sin depender de API. Pero hay un problema: para un bot 24/7 en Discloud, la IA local no estaría en la misma máquina salvo que tengas una PC tuya prendida actuando como servidor.

Ventaja: no pagas por token.
Desventaja: consume recursos, puede ser lento y necesitas mantener una PC encendida.

Yo lo usaría para desarrollo en casa, no para el evento final.

---

# Mi recomendación para tu Battle Royale

Usaría una arquitectura mixta:

```text
OpenRouter / OpenAI = mente narrativa
Base de datos = memoria real
Motor del bot = leyes del mundo
Sistema de validación = policía anti-invenciones
```

La IA nunca debería recibir todo el mapa ni toda la verdad. Solo debe recibir lo que su personaje sabe.

Por ejemplo, Sira no recibe esto:

```text
Hay 25 casillas. Verek está en la casilla 12. Rex tiene una pistola. La estrella está escondida en la casilla 18.
```

Recibe esto:

```text
Eres Sira.
Estás en la casilla 8.
Tienes hambre leve.
Escuchaste un disparo hacia el oeste.
Viste huellas recientes.
Desconfías de Verek porque ayer ocultó comida.
No sabes dónde están los demás.
No sabes dónde están las estrellas.
```

Entonces la IA responde solo desde su perspectiva.

---

# Lo más importante: respuestas en JSON

No le pediría a la IA que escriba directamente la acción final. Le pediría una **intención**.

Ejemplo:

```json
{
  "pensamiento": "Ese disparo puede significar peligro, pero también recursos abandonados.",
  "emocion": "cautelosa",
  "intencion": "investigar_rastros",
  "objetivo": "oeste",
  "dialogo": "No voy a correr hacia un disparo... pero si alguien dejó algo, quiero saberlo.",
  "nivel_riesgo": "bajo"
}
```

Después tu bot revisa:

```text
¿Sira puede ir al oeste?
¿Tiene energía?
¿Está herida?
¿Hay camino?
¿Tiene habilidad de rastreo?
¿Hay enemigos?
¿El clima afecta?
```

Y recién ahí el motor decide el resultado.

---

# Separaría las IA por tareas

No hace falta usar un modelo caro para todo.

## 1. IA de decisión

Para cuando un NPC debe decidir qué hacer.

```text
Modelo recomendado:
- OpenAI GPT-4.1 mini / GPT-5 mini si quieres estabilidad.
- OpenRouter con modelo barato si estás testeando.
```

## 2. IA de diálogo

Para generar frases, amenazas, mentiras, súplicas, traiciones.

```text
Puede ser más barata.
No necesita pensar tanto, solo escribir bien.
```

## 3. IA de resumen de memoria

Cada cierto tiempo resume lo que vivió el NPC.

```text
Día 2:
Sira encontró huellas cerca del bosque.
Sospecha que Verek tiene comida.
Tiene miedo de acercarse a zonas abiertas.
```

Esta puede ser una IA barata porque solo resume.

## 4. Motor de reglas

Este no debería ser IA. Debería ser código normal.

```text
vida
hambre
sed
energía
inventario
movimiento
ruido
visión
combate
heridas
estrellas
casillas
```

---

# Sistema ideal para evitar que invente cosas

Yo haría una lista cerrada de acciones válidas.

Por ejemplo:

```js
const accionesValidas = [
  "moverse",
  "buscar_comida",
  "buscar_agua",
  "descansar",
  "ocultarse",
  "hablar",
  "negociar",
  "atacar",
  "huir",
  "rastrear",
  "curarse",
  "preparar_trampa",
  "explorar_ruido",
  "vigilar",
  "saquear"
]
```

La IA solo puede elegir una de esas.

Si devuelve algo inválido como:

```json
{
  "intencion": "invocar_dragon"
}
```

El bot lo rechaza y fuerza una respuesta nueva o elige una acción por defecto.

---

# Ejemplo real para tu bot

Comando:

```text
/turno_npc sira
```

El bot arma el contexto:

```text
NPC: Sira
Personalidad: desconfiada, práctica, evita combate directo.
Meta: sobrevivir y conseguir una estrella.
Ubicación: Bosque de la casilla 8.
Estado: hambre leve, sed normal, energía 60%.
Inventario: navaja oxidada, botella de agua medio llena.
Memoria: Verek ocultó comida ayer. Oyó un disparo al oeste.
Percepción: huellas recientes, olor a humo débil.
Acciones válidas: ocultarse, rastrear, moverse norte, moverse oeste, descansar, preparar trampa.
```

La IA responde:

```json
{
  "intencion": "rastrear",
  "objetivo": "huellas_recientes",
  "dialogo": "Alguien pasó por aquí. Si fue Verek, quiero saber hacia dónde fue.",
  "tono": "susurrante",
  "riesgo": "medio"
}
```

El bot valida y resuelve:

```text
Sira intenta rastrear las huellas.
Tirada: percepción + rastreo + clima.
Resultado: éxito parcial.
```

Mensaje visible:

```text
Sira se agacha junto al barro húmedo y pasa dos dedos sobre una marca de bota.

"Alguien pasó por aquí... y llevaba peso."

Las huellas se pierden hacia el oeste.
```

---

# Para mí, la mejor combinación inicial sería esta

```text
Fase 1 - Prototipo:
OpenRouter + modelo gratis/barato
SQLite o JSON para guardar estado
NPCs con acciones limitadas
Respuestas en JSON

Fase 2 - Evento jugable:
OpenAI modelo mini para decisiones importantes
Modelo barato para diálogos simples
Motor de reglas propio
Memoria resumida por NPC

Fase 3 - Versión avanzada:
NPCs con relaciones
Recuerdos falsos o incompletos
Rumores
Traumas
Mentiras
Percepción limitada
Eventos automáticos por hora
```

La idea más fuerte es esta:

**El bot sabe la verdad del mundo.
El NPC solo sabe su verdad parcial.
La IA interpreta esa verdad parcial.
El motor decide qué ocurre realmente.**

Así conseguimos NPCs que parecen vivos, pero sin que rompan las reglas del Battle Royale.

[1]: https://openrouter.ai/docs/quickstart?utm_source=chatgpt.com "OpenRouter Quickstart Guide | Developer Documentation"
[2]: https://developers.openai.com/api/docs/models/gpt-4.1-mini?utm_source=chatgpt.com "GPT-4.1 mini Model | OpenAI API"
[3]: https://docs.ollama.com/capabilities/tool-calling?utm_source=chatgpt.com "Tool calling"


_____________________________


Sí. Acá tienes un **contexto listo para pegarle a Codex**. La idea está pensada para tu bot de Discord tipo Marvabot y el evento Battle Royale con NPCs vivientes.

Los puntos técnicos importantes son: usar **structured outputs / JSON Schema** para que la IA devuelva respuestas controladas, algo soportado oficialmente por OpenAI, OpenRouter y Ollama. Esto sirve justo para evitar que el modelo invente acciones fuera de las reglas. ([Desarrolladores de OpenAI][1])

---

```text
Estoy desarrollando un bot de Discord para un evento narrativo llamado Battle Royale.

El juego ocurre en una isla dividida en casillas. Hay jugadores reales y NPCs vivientes. Cada NPC debe tener personalidad, memoria, metas, estado físico, emociones, inventario y percepción limitada del mundo.

Quiero implementar un sistema de IA para que los NPCs parezcan vivos, pero con una regla fundamental:

LA IA NO CONTROLA EL MUNDO.
LA IA NO PUEDE INVENTAR OBJETOS, UBICACIONES, MUERTES, ATAJOS, ESTRELLAS, ARMAS NI EVENTOS.
LA IA SOLO PUEDE PROPONER UNA INTENCIÓN NARRATIVA BASADA EN EL CONTEXTO QUE EL BOT LE DA.
EL MOTOR DEL JUEGO VALIDA SI ESA INTENCIÓN ES POSIBLE.

Arquitectura deseada:

Discord Bot
→ Game Engine del Battle Royale
→ Base de datos del mundo
→ Módulo de percepción del NPC
→ Llamada a IA
→ Respuesta JSON con intención
→ Validador de reglas
→ Resolución mecánica
→ Narrador final
→ Guardado de memoria

Necesito que el sistema esté pensado para usar una API de IA como OpenRouter, OpenAI u Ollama local.

La IA debe responder siempre en JSON estructurado. Si el modelo devuelve una acción inválida, el bot debe rechazarla y usar una acción por defecto o pedir otra respuesta.

Objetivo inicial:
Crear una primera versión funcional del módulo de IA para NPCs.

Reglas conceptuales:

1. El bot conoce la verdad completa del mundo.
2. Cada NPC solo recibe lo que puede saber, ver, oír, oler o recordar.
3. La IA solo interpreta la mente del NPC.
4. El motor de reglas decide si la acción ocurre.
5. La narración final se genera después de validar la acción.
6. La memoria del NPC se actualiza con un resumen breve.

Ejemplo:

El NPC Sira está en la casilla 8.
Tiene hambre leve.
Tiene una navaja oxidada.
Escuchó un disparo hacia el oeste.
No sabe quién disparó.
No sabe dónde están los demás jugadores.
Recuerda que Verek le ocultó comida ayer.
La IA puede decidir que Sira quiera rastrear las huellas, esconderse o moverse con cautela.
Pero no puede decidir que encuentra una pistola si el motor no dice que existe una pistola ahí.

Acciones válidas iniciales:

- moverse
- observar
- rastrear
- buscar_comida
- buscar_agua
- descansar
- ocultarse
- hablar
- negociar
- mentir
- atacar
- huir
- curarse
- preparar_trampa
- saquear
- vigilar
- investigar_ruido
- seguir_rastro
- pedir_ayuda
- esperar

La IA debe elegir solo una de esas acciones.

Formato JSON esperado de la IA:

{
  "intencion": "rastrear",
  "objetivo": "huellas_recientes",
  "tono": "cauteloso",
  "emocion": "desconfianza",
  "dialogo": "Alguien pasó por aquí... y no iba liviano.",
  "razonamiento_visible": "Sira prefiere investigar desde lejos antes que exponerse.",
  "nivel_riesgo": "bajo",
  "prioridad": "supervivencia"
}

Importante:
No quiero razonamiento interno largo. Solo una explicación visible breve, útil para logs narrativos.

Estados del NPC:

Cada NPC debe tener una ficha similar a esta:

{
  "id": "sira",
  "nombre": "Sira",
  "personalidad": ["desconfiada", "práctica", "evita combate directo"],
  "meta_principal": "sobrevivir y conseguir una estrella",
  "meta_secundaria": "evitar depender de otros",
  "miedos": ["ser traicionada", "quedar atrapada en campo abierto"],
  "alineamiento": "neutral cautelosa",
  "ubicacion": 8,
  "vida": 100,
  "hambre": 25,
  "sed": 10,
  "energia": 60,
  "estado_emocional": "alerta",
  "inventario": ["navaja_oxidada", "botella_agua_media"],
  "habilidades": {
    "percepcion": 3,
    "sigilo": 2,
    "combate": 1,
    "rastreo": 2,
    "supervivencia": 3
  },
  "memoria": [
    "Verek ocultó comida el día anterior.",
    "Escuchó un disparo hacia el oeste hace 20 minutos."
  ],
  "relaciones": {
    "verek": {
      "confianza": -30,
      "nota": "Sospecha que le mintió sobre comida."
    }
  }
}

El contexto enviado a la IA debe construirse con una función tipo:

buildNpcPrompt(npc, worldState, perception, validActions)

Pero el prompt NO debe incluir información secreta del mundo que el NPC no conoce.

Ejemplo de prompt interno:

Eres Sira, una participante del Battle Royale.
No eres narradora omnisciente.
Solo sabes lo que aparece en tu contexto.
No puedes inventar objetos, enemigos, rutas, armas, estrellas, muertes ni eventos.
Debes elegir UNA intención de la lista de acciones válidas.
Devuelve solo JSON válido.

Contexto:
- Ubicación: casilla 8, bosque húmedo.
- Estado físico: hambre leve, sed normal, energía 60%.
- Inventario: navaja oxidada, botella de agua medio llena.
- Personalidad: desconfiada, práctica, evita combate directo.
- Memoria relevante: Verek ocultó comida ayer. Escuchaste un disparo al oeste.
- Percepción actual: huellas recientes en el barro, olor débil a humo.
- Acciones válidas: ocultarse, rastrear, moverse_oeste, descansar, preparar_trampa, vigilar.

Devuelve:
{
  "intencion": "...",
  "objetivo": "...",
  "tono": "...",
  "emocion": "...",
  "dialogo": "...",
  "razonamiento_visible": "...",
  "nivel_riesgo": "...",
  "prioridad": "..."
}

Luego el bot debe validar:

- ¿La intención existe en la lista de acciones válidas?
- ¿El objetivo existe o fue percibido?
- ¿El NPC tiene energía suficiente?
- ¿La acción es posible en la casilla actual?
- ¿El inventario permite esa acción?
- ¿La acción requiere habilidad?
- ¿Hay riesgo de fallar?
- ¿Debe hacerse una tirada?
- ¿Debe generar ruido?
- ¿Debe revelar la ubicación?
- ¿Debe actualizar memoria?

Si la IA devuelve una acción inválida:
- Registrar error.
- Reintentar una vez con una advertencia.
- Si vuelve a fallar, usar acción por defecto: observar o esperar.

Necesito que implementes estos módulos:

1. npc_ai_client.js
Módulo para llamar a una IA externa.
Debe soportar al menos OpenRouter usando fetch.
Debe estar preparado para cambiar después a OpenAI u Ollama.

2. npc_prompt_builder.js
Construye el contexto limitado del NPC.
No debe incluir información omnisciente.

3. npc_action_schema.js
Define el JSON Schema esperado de respuesta.

4. npc_action_validator.js
Valida que la acción devuelta por la IA sea legal.

5. npc_turn_resolver.js
Resuelve mecánicamente la acción.
Aplica tiradas, gasto de energía, movimiento, búsqueda, combate o cambios de estado.

6. npc_memory.js
Guarda memoria corta y memoria resumida del NPC.

7. npc_narrator.js
Convierte el resultado validado en texto narrativo para Discord.

Flujo de turno:

async function runNpcTurn(npcId) {
  const npc = await getNpc(npcId)
  const worldState = await getWorldState()
  const perception = buildNpcPerception(npc, worldState)
  const validActions = getValidActions(npc, worldState, perception)

  const prompt = buildNpcPrompt(npc, perception, validActions)
  const aiDecision = await requestNpcDecision(prompt)

  const validation = validateNpcDecision(aiDecision, validActions, npc, perception)

  let finalDecision
  if (!validation.ok) {
    finalDecision = getFallbackDecision(npc, perception)
  } else {
    finalDecision = aiDecision
  }

  const result = await resolveNpcAction(npc, finalDecision, worldState)
  await updateNpcMemory(npc, result)
  await saveWorldState(result.updatedWorldState)

  return narrateNpcResult(npc, result)
}

Primera implementación deseada:
- Sin combate complejo todavía.
- Solo movimiento, observar, rastrear, ocultarse, descansar, vigilar e investigar ruido.
- Base de datos puede ser JSON local o SQLite.
- Código en JavaScript/Node.js.
- Compatible con un bot de Discord existente.
- Usar variables de entorno para API keys.

Ejemplo de .env:

OPENROUTER_API_KEY=...
AI_PROVIDER=openrouter
AI_MODEL=openrouter/free

La IA no debe escribir directamente al canal de Discord.
El bot siempre debe revisar y transformar la respuesta antes de mostrarla.

Resultado narrativo ejemplo:

Sira se agacha junto al barro húmedo. Pasa dos dedos por una marca de bota y mira hacia el oeste.

"Alguien pasó por aquí... y no iba liviano."

Resultado mecánico:
- Acción: rastrear
- Éxito parcial
- Energía -5
- Nueva pista descubierta: rastro_hacia_oeste
- Memoria añadida: Sira encontró huellas profundas en la casilla 8.

Crea el código base con archivos separados, funciones claras y comentarios.
No hardcodear todo en un solo archivo.
Priorizar seguridad contra invenciones de la IA.
```

Y este sería el **resumen corto para decirle a Codex qué estamos construyendo**:

```text
Queremos NPCs con IA para un Battle Royale de Discord, pero la IA no controla el juego. La IA solo recibe percepción limitada del NPC y devuelve una intención en JSON. El motor del bot valida esa intención contra reglas reales del mundo. Si es válida, se resuelve mecánicamente; si no, se rechaza. El objetivo es que los NPCs parezcan vivos sin romper el balance ni inventar cosas.
```

La frase clave para que Codex no se desvíe sería:

```text
No construyas un chatbot libre. Construye un sistema de decisiones controladas para NPCs, donde el LLM solo propone intenciones y el motor del juego decide la realidad.
```

[1]: https://developers.openai.com/api/docs/guides/structured-outputs?utm_source=chatgpt.com "Structured model outputs | OpenAI API"
