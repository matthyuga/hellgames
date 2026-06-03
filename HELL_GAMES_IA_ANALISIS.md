# Hell Games - Analisis del sistema de IA

Este documento analiza `HELL_GAMES_ia.md` y lo convierte en una direccion
implementable para el bot Hellgames.

## Diagnostico rapido

El documento esta bien orientado. La idea central es correcta:

```text
La IA no controla el mundo.
La IA propone intenciones.
El motor del juego valida y resuelve.
```

Ese principio deberia ser una regla base del proyecto. Si se respeta, podemos
tener NPCs que parezcan vivos sin que inventen objetos, rutas, muertes,
estrellas, armas o resultados injustos.

## Lo mas valioso del documento

### 1. Arquitectura hibrida

La separacion entre motor de reglas e IA narrativa es la parte mas importante.

El bot debe controlar:

- ubicaciones reales;
- inventarios;
- salud, hambre, sed, energia;
- heridas;
- armas;
- loot;
- clima;
- ruido;
- rastros;
- vision;
- combate;
- muerte;
- rutas;
- estrellas;
- memoria persistente.

La IA debe controlar solo:

- tono;
- emocion;
- prioridad subjetiva;
- dialogo;
- interpretacion parcial;
- intencion propuesta.

### 2. Percepcion limitada

El documento acierta al decir que el NPC no debe recibir toda la verdad del
mundo. Debe recibir solo:

- lo que ve;
- lo que oye;
- lo que huele;
- lo que recuerda;
- lo que deduce razonablemente;
- rumores que haya escuchado;
- informacion que otro personaje le haya dicho.

Esto es clave para que haya misterio, errores, paranoia, mentiras y traiciones.

### 3. Respuesta JSON

La IA debe responder en formato estructurado. No deberia escribir directamente
al canal de Discord ni resolver la accion final.

Formato base recomendado:

```json
{
  "intencion": "rastrear",
  "objetivo": "huellas_recientes",
  "tono": "cauteloso",
  "emocion": "desconfianza",
  "dialogo": "Alguien paso por aqui... y no iba liviano.",
  "razonamiento_visible": "Prefiere investigar desde lejos antes que exponerse.",
  "nivel_riesgo": "bajo",
  "prioridad": "supervivencia"
}
```

## Punto a corregir

El documento menciona JavaScript/Node.js, pero la referencia tecnica que ya
tenemos de MarvaBot esta en Python con `discord.py`, SQLite y `.env`.

Decision recomendada:

```text
Hellgames deberia empezar en Python, no en Node.
```

Motivo:

- ya tenemos patron local con MarvaBot;
- SQLite en Python es directo;
- `discord.py` ya esta probado en el servidor;
- reduce el salto tecnico;
- facilita compartir empaquetado Discloud.

La arquitectura del documento sigue siendo valida. Solo cambiaria los nombres
de modulos:

```text
npc_ai_client.py
npc_prompt_builder.py
npc_action_schema.py
npc_action_validator.py
npc_turn_resolver.py
npc_memory.py
npc_narrator.py
```

## Tipos de entidades y como deberian pensar

No todos los seres de la isla necesitan el mismo tipo de IA.

### 1. Participantes del battle royale

Son los NPCs mas complejos.

Necesitan:

- personalidad fuerte;
- metas;
- miedo;
- memoria;
- relaciones;
- estrategia;
- hambre, sed, energia;
- inventario;
- reputacion;
- capacidad de mentir o traicionar.

Uso de IA:

- decision por turno;
- dialogo;
- negociacion;
- traicion;
- reaccion a peligro;
- resumen de memoria.

Ejemplo:

```text
Zymba oye un disparo cerca del Cañon Partido.
Tiene hambre, una lanza y mala relacion con Nara.
La IA propone investigar desde lejos.
El motor valida si puede rastrear y que riesgo asume.
```

### 2. Lugarenos

Son habitantes de la isla: comerciantes, medicos, guias, cultistas, pescadores,
cazadores o guardianes locales.

No necesitan moverse tanto como los participantes. Su IA deberia centrarse en:

- agenda;
- secretos;
- memoria social;
- precios;
- favores;
- reputacion;
- lealtad a una zona;
- reaccion ante violencia o amenazas.

Uso de IA:

- dialogo;
- trueque;
- informacion parcial;
- condicion para ayudar;
- respuesta a intimidacion o persuasion.

Ejemplo:

```text
La medica del Templo de la Luna no decide "curar gratis".
La IA propone una condicion narrativa.
El motor calcula precio, objeto requerido o favor.
```

### 3. Criaturas

Las criaturas no necesitan un LLM para cada turno. La mayoria puede funcionar
con comportamiento por reglas.

Necesitan:

- hambre;
- agresividad;
- territorio;
- sensibilidad a ruido;
- sensibilidad a olor;
- miedo al fuego;
- horario activo;
- patron de caza.

Uso de IA:

- solo para criaturas especiales;
- solo para narrar encuentros raros;
- solo para jefes o entidades inteligentes.

Ejemplo:

```text
Una criatura del Pantano de los Olvidados se mueve hacia ruido + olor.
No necesita dialogo.
El motor decide su ruta.
La IA solo puede narrar la escena si el encuentro se vuelve importante.
```

### 4. Jefes o entidades especiales

Gorath, guardianes, espiritus, drones avanzados o entidades del Sector X pueden
usar una IA mas rica.

Necesitan:

- reglas propias;
- condiciones de pacto;
- memoria de intrusos;
- frases ceremoniales;
- reaccion a objetos o simbolos.

Uso de IA:

- dialogo dramatico;
- pruebas;
- advertencias;
- decisiones limitadas por reglas especiales.

## Acciones validas iniciales

La lista del documento es buena, pero para el prototipo conviene reducirla.

Primera version:

```text
observar
moverse
descansar
ocultarse
vigilar
rastrear
investigar_ruido
buscar_comida
buscar_agua
hablar
esperar
```

Segunda version:

```text
negociar
mentir
curarse
preparar_trampa
saquear
huir
atacar
seguir_rastro
pedir_ayuda
```

Motivo: si metemos combate, saqueo y trampas desde el dia uno, el motor se
complica antes de tener bien resuelta percepcion y memoria.

## Flujo recomendado de turno

```text
1. Cargar NPC.
2. Cargar mundo.
3. Construir percepcion limitada.
4. Calcular acciones validas.
5. Si el NPC es simple, usar reglas.
6. Si el NPC es importante, pedir intencion a IA.
7. Validar JSON.
8. Validar accion contra reglas.
9. Resolver mecanica.
10. Guardar cambios.
11. Actualizar memoria.
12. Narrar solo si el evento merece publicarse.
```

## Uso eficiente de IA

No conviene llamar IA para todos los NPCs en cada tick.

Recomendacion:

```text
IA solo cuando hay decision interesante.
```

Activadores:

- encontro otro personaje;
- escucho un ruido importante;
- vio un cadaver;
- encontro una estrella;
- fue traicionado;
- debe negociar;
- esta herido;
- esta cerca de morir;
- hay evento ambiental fuerte;
- debe elegir entre rutas peligrosas.

Para acciones rutinarias, usar reglas:

- descansar si energia baja;
- buscar agua si sed alta;
- ocultarse si miedo alto;
- moverse si la zona se vuelve peligrosa;
- vigilar si esta en refugio.

## Memoria

Conviene separar tres niveles:

### Memoria corta

Ultimos eventos del dia.

```text
Escucho ramas al norte.
Vio humo cerca del puerto.
Perdio 10 energia por lluvia.
```

### Memoria importante

Hechos que cambian conducta.

```text
Varek le robo comida.
Nara la curo sin pedir pago.
La Estacion Militar activo una alarma.
```

### Rasgos derivados

Cambios psicologicos compactos.

```text
Desconfia mas de desconocidos.
Evita zonas abiertas.
Busca agua antes que combate.
```

La IA puede resumir memoria, pero el bot decide que memoria se conserva.

## Riesgos principales

### 1. Que la IA invente realidad

Solucion:

- acciones cerradas;
- objetos cerrados;
- objetivos cerrados;
- validacion estricta;
- fallback a observar/esperar.

### 2. Costos por demasiadas llamadas

Solucion:

- IA solo en momentos interesantes;
- reglas para rutina;
- memoria compacta;
- prompts cortos;
- modelos pequenos para decisiones simples.

### 3. NPCs demasiado parecidos

Solucion:

- arquetipo;
- miedos;
- prioridades;
- relaciones;
- frases de estilo;
- sesgos de decision.

### 4. Prompt demasiado grande

Solucion:

- enviar solo percepcion;
- no enviar historia completa;
- resumir memoria;
- usar IDs internos para objetos;
- limitar acciones validas.

## Arquitectura recomendada para Hellgames

```text
hellgames.py
hellgames_db.py
hellgames_models.py
hellgames_rules.py
hellgames_perception.py
hellgames_ai_client.py
hellgames_npc_prompt.py
hellgames_npc_validator.py
hellgames_npc_resolver.py
hellgames_npc_memory.py
hellgames_narrator.py
```

Para el prototipo, tambien se puede agrupar en menos archivos:

```text
hellgames.py
db.py
rules.py
npc_ai.py
npc_turns.py
narration.py
```

## Decision recomendada

Implementar primero un simulador local antes de conectarlo a Discord.

Primer objetivo:

```text
Ejecutar 1 turno de 3 NPCs en JSON local o SQLite.
```

Con:

- 3 NPCs;
- 3 casillas;
- 8 acciones;
- percepcion limitada;
- respuesta mock de IA o proveedor real opcional;
- validador;
- narrador.

Cuando eso funcione, se conecta al bot.

## Conclusion

`HELL_GAMES_ia.md` es una buena base conceptual. La idea fuerte que debemos
mantener es:

```text
El bot sabe la verdad.
El NPC solo sabe su perspectiva.
La IA propone intenciones.
El motor decide la realidad.
```

Para participantes, usar IA de decision y memoria.
Para lugarenos, usar IA sobre todo en dialogo, comercio y secretos.
Para criaturas, usar reglas salvo casos especiales.

La primera implementacion no deberia intentar resolver todo el battle royale.
Debe probar un turno controlado, barato y validado.
