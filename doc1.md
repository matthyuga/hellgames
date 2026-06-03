Sí, esta idea tiene mucho potencial. Yo lo pensaría como un **Battle Royale narrativo por Discord**, donde el canal público es solo la “terminal de acciones”, pero la verdadera experiencia ocurre en mensajes privados y en registros personales.

La clave sería esta:

> **Todos juegan en la misma isla, pero nadie ve toda la isla. Cada jugador solo conoce lo que su personaje percibe.**

Eso permite misterio, paranoia, exploración, rumores, emboscadas, alianzas y traiciones.

---

# 1. Estructura general del evento

El evento tendría tres capas:

## 1. Canal público del evento

Un único canal tipo:

`#battle-royale-evento`

Ahí los jugadores escriben comandos:

```txt
/explorar
/mover norte
/buscar recursos
/descansar
/inventario
/estado
/ayuda
/modo-automatico
```

Pero el bot **no debería responder todo en público**, porque eso saturaría el canal y revelaría información.

En público solo debería aparecer algo mínimo, por ejemplo:

```txt
Kevin realizó una acción.
Marvabot le envió el resultado por privado.
```

O incluso algo más inmersivo:

```txt
🌫️ Kevin se interna entre la niebla...
```

Pero el resultado real va por mensaje privado.

---

## 2. Mensajes privados al jugador

Cada jugador recibe su propia historia por DM.

Ejemplo:

```txt
🌲 Casilla 7 · Bosque húmedo

Te adentras entre árboles altos y raíces mojadas.
El suelo está blando, como si hubiera llovido hace poco.

Percibes:
- Humo muy leve hacia el este.
- Un ruido metálico al norte.
- Huellas recientes cerca de un tronco caído.

Actividades disponibles:
1. Buscar recursos.
2. Talar madera.
3. Seguir las huellas.
4. Esconderte.
5. Moverte a otra casilla.
```

Esto mantiene el misterio y hace que cada jugador tenga su propia experiencia.

---

## 3. Registro secreto del personaje

El bot debería guardar internamente:

```txt
Jugador: Kevin
Casilla: 7
HP: 85/100
Hambre: 40/100
Sed: 25/100
Sueño: 60/100
Estado: cansado
Inventario: cuchillo, botella vacía, madera x2
Modo: manual
Actividad actual: buscar recursos
Tiempo restante: 12 minutos
Última percepción: humo al este
```

Esto permite que el personaje siga existiendo aunque el jugador no esté mirando.

---

# 2. Información limitada por percepción

Esto es lo más importante del sistema.

El jugador no debería saber “qué pasa en la isla”, sino solo lo que su personaje puede percibir.

## Cosas que puede ver en su casilla

Si está en la misma casilla que algo importante:

```txt
Ves una cabaña abandonada entre los árboles.
La puerta está entreabierta.
Hay marcas de barro recientes en el suelo.
```

Si hay otro jugador:

```txt
Ves a una figura humana cerca del arroyo.
Parece estar revisando una mochila.
No sabes si te ha visto.
```

Si el otro jugador tiene poca habilidad de sigilo o está haciendo ruido:

```txt
Escuchas ramas quebrándose cerca.
Alguien se mueve entre los arbustos.
```

---

## Cosas que puede percibir de casillas cercanas

Si ocurre algo en una casilla adyacente:

```txt
💥 Escuchas un disparo hacia el norte.
```

O:

```txt
🔥 Sientes olor a carne ahumada desde el este.
```

O:

```txt
🐺 Escuchas aullidos lejanos hacia el oeste.
```

O:

```txt
⚙️ Un ruido metálico se repite a la distancia. Parece venir del sur.
```

Esto puede generar decisiones interesantes:

```txt
/mover norte
/investigar ruido
/esconderse
/preparar arma
/evitar zona
```

---

# 3. Sistema de casillas

Cada casilla debería tener:

```txt
Nombre
Tipo de terreno
Descripción
Recursos posibles
Peligros posibles
Actividades disponibles
Ruido generado
Olor generado
Visibilidad
Refugios
Eventos ocultos
```

Ejemplo:

## Casilla 4 · Bosque de pinos

```txt
Terreno: bosque
Visibilidad: baja
Recursos: madera, hierbas, setas, agua de lluvia ocasional
Peligros: lobos, trampas, jugadores ocultos
Actividades:
- Buscar madera
- Buscar alimento
- Recolectar hierbas
- Esconderse
- Cazar
- Dormir bajo refugio improvisado
Percepciones:
- Crujidos de ramas
- Olor a humedad
- Humo visible si alguien prende fuego
```

## Casilla 9 · Barco estropeado

```txt
Terreno: costa / estructura metálica
Visibilidad: media
Recursos: metal, cuerda, combustible, piezas eléctricas
Peligros: cortes, óxido, derrumbes, otros saqueadores
Actividades:
- Buscar piezas
- Extraer metal
- Reparar sistemas
- Esconderse en camarotes
- Pescar
- Investigar bodega
Percepciones:
- Olor a sal y combustible viejo
- Golpes metálicos
- Gaviotas
```

## Casilla 13 · Torre del helicóptero

```txt
Terreno: campo abierto fortificado
Visibilidad: alta
Recursos: pocos
Peligros: exposición total, otros jugadores, torretas, puertas electrónicas
Actividades:
- Examinar compuertas
- Insertar estrellas
- Hackear sistema
- Vigilar zona
- Forzar entrada
- Buscar ruta alternativa
```

---

# 4. Comandos visibles y comandos desbloqueables

Me parece excelente que el jugador no tenga todos los comandos desde el principio.

Al inicio el comando `/ayuda` podría mostrar algo simple:

```txt
📘 Comandos básicos

/estado
/inventario
/mirar
/explorar
/mover [norte/sur/este/oeste]
/buscar
/descansar
/comer
/beber
/ayuda
```

Pero a medida que aprende habilidades, encuentra libros o experimenta cosas, desbloquea nuevos comandos.

---

## Ejemplo: jugador encuentra un libro de rastreo

Después de leerlo:

```txt
Has aprendido los fundamentos de Rastreo.
Nuevo comando desbloqueado:

/rastrear
```

Ahora puede usar:

```txt
/rastrear huellas
/rastrear sangre
/rastrear olor
/rastrear ruido
```

---

## Ejemplo: jugador aprende medicina

```txt
Nuevo comando desbloqueado:

/curar
/fabricar vendaje
/diagnosticar
```

---

## Ejemplo: jugador aprende mecánica

```txt
Nuevo comando desbloqueado:

/reparar
/desarmar pieza
/construir mecanismo
```

Esto hace que el juego tenga progresión sin abrumar desde el minuto uno.

---

# 5. Actividades por tiempo real

Como el juego corre en horario argentino, cada actividad debería tener duración real.

Ejemplos:

```txt
/buscar recursos → 10 minutos
/talar arbol → 20 minutos
/leer libro básico → 30 minutos
/dormir → 2 a 6 horas
/construir refugio simple → 45 minutos
/reparar motor → 1 a 3 horas
/cazar → 30 a 60 minutos
/viajar a otra casilla → 10 a 25 minutos
```

Cuando el jugador inicia una actividad:

```txt
🌲 Comenzaste a talar un árbol.
Tiempo estimado: 20 minutos.
Ruido generado: medio.
Cansancio generado: alto.
```

Mientras hace eso, otros jugadores cercanos podrían recibir:

```txt
🪓 Escuchas golpes repetidos de hacha hacia el oeste.
```

Eso es buenísimo, porque cada acción deja rastros.

---

# 6. Modo manual y modo automático

Este sistema puede ser el corazón del juego.

## Modo manual

El jugador decide todo.

```txt
/modo-manual
```

Resultado:

```txt
Tu personaje esperará tus órdenes directas.
Si pasas mucho tiempo sin actuar, puede entrar en estado pasivo.
```

Ventaja:

* Más control.
* Mejor para estrategia.
* Permite emboscadas, alianzas, decisiones finas.

Desventaja:

* Si el jugador se desconecta, el personaje puede quedar vulnerable.

---

## Modo automático

```txt
/modo-automatico
```

Resultado:

```txt
Tu personaje actuará por cuenta propia según sus necesidades, habilidades y prioridades.
```

El personaje empezaría a tomar decisiones básicas:

* Si tiene sed, busca agua.
* Si tiene hambre, busca comida.
* Si está cansado, busca refugio.
* Si escucha disparos cerca, puede esconderse.
* Si tiene personalidad agresiva, puede investigar.
* Si tiene personalidad cobarde, puede huir.
* Si tiene habilidades de supervivencia, toma mejores decisiones.
* Si tiene heridas, busca curarse.

Ejemplo:

```txt
🤖 Modo automático activado.

Prioridad actual:
1. Buscar agua.
2. Evitar combate.
3. Mantenerse oculto.
```

---

# 7. Rutinas automáticas programables

Además del modo automático general, podrías permitir que el jugador programe una rutina.

Ejemplo:

```txt
/rutina crear noche
1. buscar refugio
2. comer si hambre > 60
3. beber si sed > 50
4. dormir 6 horas
5. despertar al amanecer
```

O algo más simple:

```txt
/rutina supervivencia
```

El bot responde:

```txt
Rutina de supervivencia activada.
Tu personaje intentará:
- Buscar agua.
- Buscar comida.
- Evitar combate.
- Descansar en lugares seguros.
```

También podría haber rutinas desbloqueables:

```txt
/rutina recolector
/rutina cazador
/rutina sigiloso
/rutina saqueador
/rutina médico
/rutina mecánico
/rutina agresivo
/rutina pacifista
```

Esto permitiría que el evento avance aunque los jugadores no estén activos todo el día.

---

# 8. Necesidades básicas del personaje

Cada personaje debería tener medidores simples:

```txt
HP
Hambre
Sed
Sueño
Cansancio
Estrés
Heridas
Temperatura
```

Pero no mostraría todos como números exactos al principio. Mejor algo narrativo.

Con `/estado`:

```txt
❤️ Salud: estable
🍖 Hambre: moderada
💧 Sed: alta
😴 Sueño: bajo
🩸 Heridas: rasguños leves
🧠 Estrés: alerta
```

Si el personaje tiene habilidad médica o supervivencia alta, puede ver más detalle:

```txt
Sed: 72/100
Hambre: 48/100
Cansancio: 61/100
Riesgo de deshidratación: medio
```

Esto hace que las habilidades también afecten la interfaz.

---

# 9. Seguridad y descanso

Dormir no debería ser gratis.

El jugador necesita elegir dónde descansar.

## Dormir en campo abierto

```txt
Te recuestas bajo un árbol.
El suelo está frío.
No estás completamente oculto.

Riesgo durante el descanso: alto.
```

## Dormir en refugio improvisado

```txt
Te refugias bajo ramas y hojas.
No es cómodo, pero reduce el viento.

Riesgo durante el descanso: medio.
```

## Dormir en cabaña

```txt
Cierras la puerta de la cabaña.
El interior huele a madera húmeda.
Puedes descansar mejor, pero alguien podría encontrarte.
```

## Dormir con trampa colocada

```txt
Colocas una trampa sonora en la entrada.
Si alguien se acerca, podrías despertar.
```

Esto vuelve importante construir, esconderse, vigilar o hacer alianzas.

---

# 10. Sistema de ruido, olor y rastros

Esto sería muy importante para la inmersión.

Cada actividad debería generar señales.

## Ruido

```txt
Disparo: ruido alto, alcanza varias casillas.
Talar árbol: ruido medio, alcanza casillas cercanas.
Caminar: ruido bajo.
Correr: ruido medio.
Construir: ruido medio.
Combatir: ruido alto.
```

## Olor

```txt
Cocinar carne: olor fuerte.
Cadáver: olor nauseabundo.
Combustible: olor químico.
Hierbas medicinales: olor leve.
Humo: olor visible/perceptible.
```

## Rastros

```txt
Huellas
Sangre
Cenizas
Restos de comida
Ramas rotas
Casquillos de bala
Tela rasgada
Fogata apagada
Puerta forzada
```

Ejemplo de mensaje:

```txt
Notas huellas recientes en el barro.
Van hacia el norte.
Parecen de una sola persona.
```

Con mejor rastreo:

```txt
Las huellas son recientes, quizá de hace menos de 20 minutos.
La persona iba cargando peso.
Parece que cojeaba.
```

---

# 11. Actividades disponibles por casilla

Cada casilla debería tener una lista de actividades visibles y ocultas.

Ejemplo:

```txt
/mirar
```

Respuesta:

```txt
🌲 Estás en el Bosque de Pinos.

Actividades evidentes:
- /buscar recursos
- /mover norte
- /mover este
- /descansar
- /esconderse

Actividades posibles por tus habilidades:
- /rastrear huellas
- /recolectar hierbas
- /fabricar refugio

Algo te llama la atención:
- Hay marcas en un árbol cercano.
```

Si el jugador investiga:

```txt
/investigar marcas
```

Podría descubrir:

```txt
Las marcas parecen hechas con una hoja afilada.
Alguien marcó este camino antes.
```

O con habilidad de supervivencia:

```txt
Estas marcas parecen indicar una ruta hacia agua.
```

---

# 12. Objetivo principal

El objetivo oficial sería:

```txt
Sobrevivir hasta la llegada del helicóptero.
Llegar a la torre.
Reunir 10 estrellas.
Escapar.
```

Pero habría rutas alternativas.

## Ruta normal

* Conseguir 10 estrellas.
* Llegar a la torre.
* Insertarlas en una compuerta.
* Esperar o tomar el helicóptero.

## Ruta técnica

* Reparar el barco.
* Necesita mecánica, combustible, piezas, herramientas.
* Puede escapar antes, pero es muy difícil.

## Ruta del tren

* Reparar rieles o activar locomotora.
* Necesita metal, madera, carbón/combustible, conocimientos técnicos.
* Puede mover a varios jugadores.

## Ruta oculta

* Descubrir túneles.
* Requiere exploración, mapas, pistas, rastreo.
* Puede llevar al centro o a una salida secreta.

## Ruta violenta

* Robar estrellas a otros.
* Cazar jugadores.
* Llegar fuerte al final.

## Ruta social

* Formar alianza.
* Repartir roles.
* Uno cocina, otro explora, otro repara, otro vigila.
* Pero al final quizá no todos puedan escapar.

---

# 13. Sistema de estrellas

Cada jugador empieza con 2 estrellas.

Necesita 10 para entrar por la vía oficial.

Formas de conseguir estrellas:

```txt
Encontrarlas como loot raro.
Completar eventos de casilla.
Derrotar NPCs especiales.
Robarlas a jugadores.
Negociarlas.
Ganar desafíos.
Descubrir escondites.
Abrir cajas cerradas.
Resolver acertijos.
```

Importante: las estrellas deberían generar tensión.

Ejemplo:

```txt
⭐ Encontraste una estrella oxidada dentro de una caja metálica.
Sientes que este objeto podría atraer problemas.
```

Otros jugadores cercanos podrían recibir:

```txt
Un destello extraño se refleja brevemente hacia el oeste.
```

Así el loot importante también genera riesgo.

---

# 14. Encuentros con otros jugadores

Cuando dos jugadores están en la misma casilla, no necesariamente deberían verse automáticamente.

Depende de:

```txt
Visibilidad de la casilla
Ruido
Sigilo
Hora del día
Clima
Actividad actual
Estado del personaje
Habilidad de percepción
```

Ejemplo:

```txt
Estás en una zona de niebla.
Crees haber visto una silueta entre los árboles.
```

El otro jugador recibe:

```txt
Sientes que alguien podría estar cerca.
```

Opciones:

```txt
/llamar
/esconderse
/preparar arma
/huir
/acercarse
/observar
/atacar
```

Si uno usa `/llamar`:

```txt
Gritas: “¿Hay alguien ahí?”
```

El otro recibe:

```txt
Escuchas una voz cercana.
Parece venir desde el claro.
```

Esto permite encuentros tensos sin revelar de golpe todo.

---

# 15. Canal público como “rumor de isla”

Aunque la mayoría sea privado, el canal público podría tener mensajes globales ocasionales.

Ejemplos:

```txt
📢 Día 3 · 21:00
La noche cae sobre la isla.
Las temperaturas bajan.
Los sonidos del bosque se vuelven más intensos.
```

```txt
💥 Un disparo retumba en algún punto de la isla.
```

```txt
🔥 Una columna de humo se eleva a lo lejos.
```

```txt
📡 Una transmisión rota suena en las radios:
“...el helicóptero llegará el día 20... solo los aptos...”
```

```txt
☠️ Un participante ha muerto.
```

Pero no necesariamente diría quién, dónde ni cómo, salvo que el diseño quiera hacerlo.

---

# 16. Ciclo diario del juego

Como el tiempo es real, podrías dividir el día en fases.

## 06:00 a 10:00 · Mañana

* Buena visibilidad.
* Menos frío.
* Ideal para explorar.
* Animales activos.
* Menos riesgo de emboscadas.

## 10:00 a 17:00 · Día

* Mejor para recolectar, construir, moverse.
* Mayor exposición.
* Otros jugadores también están activos.

## 17:00 a 21:00 · Atardecer

* Visibilidad media.
* Buen momento para volver a refugio.
* Más tensión.

## 21:00 a 05:00 · Noche

* Visibilidad baja.
* Más frío.
* Más riesgo.
* Mejora el sigilo.
* Dormir es importante.
* Algunos NPCs o animales son más peligrosos.

Ejemplo:

```txt
🌙 Son las 21:00 en la isla.
La noche empieza.
La visibilidad baja.
Los ruidos lejanos se vuelven más difíciles de ubicar.
```

---

# 17. Sistema de acción recomendado

Para que sea manejable, cada personaje debería tener:

```txt
Actividad actual
Cola de acciones
Modo actual
Prioridades
Interrupciones
```

Ejemplo:

```txt
Actividad actual: talar árbol
Tiempo restante: 12 minutos
Siguiente acción: recoger madera
Después: volver al refugio
Modo: automático parcial
```

Comando:

```txt
/cola
```

Respuesta:

```txt
Tus próximas acciones:
1. Terminar de talar árbol.
2. Recoger madera.
3. Buscar refugio.
4. Descansar si el cansancio supera 70.
```

Comando:

```txt
/cancelar
```

Respuesta:

```txt
Cancelaste la actividad actual.
Has dejado el tronco a medio cortar.
```

Esto permite que el jugador no esté obligado a estar todo el día pendiente.

---

# 18. Manual, automático y semi-automático

Yo usaría tres modos, no solo dos.

## Manual

El jugador decide todo.

```txt
/modo manual
```

## Semi-automático

El jugador da una intención general.

```txt
/modo semi
/prioridad buscar agua
/prioridad evitar combate
```

El personaje hace cosas, pero pide confirmación ante decisiones graves.

Ejemplo:

```txt
Encontraste una mochila abandonada.
Parece sospechosa.

¿Quieres abrirla?
/confirmar
/ignorar
/revisar trampa
```

## Automático total

El personaje decide solo.

```txt
/modo automatico
```

Ideal para jugadores ausentes, pero con riesgo.

```txt
Tu personaje actuará por instinto.
Puede tomar decisiones imperfectas.
```

---

# 19. Personalidad del personaje

Para que el automático no sea genérico, cada personaje debería tener una personalidad o tendencia.

Ejemplos:

```txt
Cauteloso: evita combate, prioriza refugio.
Agresivo: investiga ruidos, busca armas.
Superviviente: prioriza agua, comida y descanso.
Saqueador: busca estructuras y loot.
Social: intenta contactar con otros.
Técnico: busca piezas, herramientas y rutas alternativas.
Nómada: se mueve mucho.
Territorial: fortifica una casilla.
```

Esto hace que el modo automático sea más vivo.

Un jugador podría elegir al inicio:

```txt
Tu instinto principal:
1. Superviviente
2. Cazador
3. Técnico
4. Médico
5. Saqueador
6. Diplomático
7. Solitario
```

---

# 20. Ejemplo de experiencia completa

Jugador escribe en canal público:

```txt
/explorar
```

El bot responde en público:

```txt
🌫️ Kevin explora la zona...
```

Por privado recibe:

```txt
🌲 Casilla 6 · Bosque bajo

Avanzas con cuidado entre ramas húmedas.
El aire huele a tierra mojada.

Encuentras:
- Ramas secas.
- Huellas pequeñas de animal.
- Una lata oxidada medio enterrada.

Percibes:
- Un golpe metálico hacia el norte.
- Olor a humo muy leve hacia el este.

Puedes hacer:
/buscar recursos
/rastrear huellas
/mover norte
/mover este
/esconderse
/volver
```

El jugador decide:

```txt
/mover este
```

Respuesta privada:

```txt
Te mueves hacia el este.
Tiempo estimado: 15 minutos.
Ruido generado: bajo.
```

Mientras tanto, otro jugador en una casilla cercana recibe:

```txt
Escuchas pasos lejanos entre la vegetación.
No parecen venir directamente hacia ti.
```

Esto ya crea juego emergente.

---

# 21. Comando `/ayuda` progresivo

El `/ayuda` debería cambiar según lo que el jugador sabe.

Al inicio:

```txt
📘 Ayuda básica

Comandos:
 /estado
 /inventario
 /mirar
 /explorar
 /mover
 /buscar
 /descansar
 /comer
 /beber
 /modo
```

Después de aprender rastreo:

```txt
Nuevos comandos conocidos:
 /rastrear
 /analizar huellas
```

Después de aprender fabricación:

```txt
Nuevos comandos conocidos:
 /fabricar
 /reparar
 /desarmar
```

Después de descubrir el sistema de estrellas:

```txt
Comandos de objetivo:
 /estrellas
 /insertar estrella
 /examinar compuerta
```

Así el bot enseña el juego de forma natural.

---

# 22. Sistema de diario personal

Sería muy bueno que cada jugador tenga un diario.

Comando:

```txt
/diario
```

Respuesta:

```txt
📓 Diario de supervivencia

Día 1:
- Despertaste en la costa.
- Encontraste una botella vacía.
- Escuchaste un disparo hacia el norte.
- Viste humo al este.
- Aprendiste a fabricar una cuerda simple.

Pistas importantes:
- La torre requiere 10 estrellas.
- El barco podría repararse.
- Hay huellas grandes cerca del bosque.
```

El diario sirve para que el jugador no se pierda.

También ayuda si alguien vuelve después de varias horas.

---

# 23. Sistema de “memoria de casilla”

Cada jugador debería ir completando su mapa.

Comando:

```txt
/mapa
```

Al inicio:

```txt
Mapa conocido:
[ ? ][ ? ][ ? ]
[ ? ][Tú][ ? ]
[ ? ][ ? ][ ? ]
```

Después de explorar:

```txt
Mapa conocido:
[ Bosque ][ ? ][ ? ]
[ Costa  ][Tú][ Ruinas ]
[ ?      ][ ? ][ ?     ]
```

Pero no muestra jugadores salvo que los haya visto.

Esto refuerza el misterio.

---

# 24. Cómo evitar saturación

Para no llenar el canal:

## Público

Solo mensajes breves:

```txt
Kevin realizó una acción.
Una explosión se escuchó en la isla.
La noche ha caído.
Un participante ha sido eliminado.
```

## Privado

Todo lo personal:

```txt
Resultado de acción.
Inventario.
Estado.
Percepción.
Mapa.
Diario.
Combate.
Loot.
```

## Grupal temporal

Si varios jugadores están en la misma casilla, el bot podría crear o usar un mini-hilo privado temporal, pero eso puede ser más complejo.

Alternativa más simple:

Cada jugador recibe el mismo mensaje por privado:

```txt
También están presentes:
- Una figura encapuchada.
- Un jugador herido cerca del fuego.
```

Pero sin revelar nombre hasta que se identifiquen.

---

# 25. Sistema de identificación

No siempre deberías saber quién es quién.

Ejemplo:

```txt
Ves a una persona con una chaqueta oscura.
```

Si se acerca o habla:

```txt
La persona dice ser “Rex”.
```

Si ya lo conoces:

```txt
Reconoces a Rex cerca del refugio.
```

Comandos:

```txt
/presentarse
/hablar
/susurrar
/gritar
/amenazar
/negociar
/intercambiar
```

Esto permite engaños.

Un jugador puede decir que se llama de otra forma.

---

# 26. Sistema de combate

El combate debería ser peligroso, no algo que se spamee.

Antes de atacar, normalmente hay una fase de tensión:

```txt
Ves una figura cerca.
Tiene algo en la mano.
No sabes si es un arma.

Opciones:
 /observar
 /hablar
 /esconderse
 /preparar arma
 /atacar
 /huir
```

Si ataca:

```txt
/atacar cuchillo
```

Resultado:

```txt
Te lanzas hacia la figura con el cuchillo.
El ataque genera ruido alto.
```

El otro recibe:

```txt
Una figura sale de entre los árboles y te ataca.
Tienes pocos segundos para reaccionar.
```

Si está en automático, su reacción depende de percepción, agilidad, estado y personalidad.

---

# 27. Muerte, heridas y eliminación

Yo no haría que todo sea muerte instantánea.

Podría haber estados:

```txt
Sano
Herido leve
Herido grave
Sangrando
Inconsciente
Moribundo
Muerto
```

Un jugador inconsciente puede ser:

* Robado.
* Curado.
* Capturado.
* Rematado.
* Abandonado.
* Encontrado por animales.
* Salvado por NPCs.

Esto da muchas historias.

---

# 28. NPCs vivientes

Los NPCs encajan perfecto.

Cada NPC tendría:

```txt
Ubicación
Objetivo
Miedo
Necesidad
Habilidades
Inventario
Nivel de confianza
Agenda
```

Ejemplo:

```txt
NPC: Mara
Objetivo: escapar por el barco
Habilidad: mecánica
Personalidad: desconfiada
Objeto: llave inglesa, estrella x1, botella de agua
Conducta: evita combate, busca piezas
```

El jugador puede encontrar rastros de ella:

```txt
Ves marcas de herramientas cerca de una puerta metálica.
Alguien estuvo trabajando aquí hace poco.
```

O escucharla:

```txt
Escuchas una voz murmurando dentro del barco.
```

---

# 29. Eventos ambientales

Para que la isla se sienta viva, cada cierto tiempo pueden ocurrir eventos.

```txt
Lluvia
Tormenta
Niebla
Incendio
Animales migrando
Zona contaminada
Derrumbe
Marea alta
Fallo eléctrico en la torre
Transmisión de radio
Drop de suministros
```

Ejemplo global:

```txt
🌧️ Comienza a llover en la isla.
Las huellas serán más difíciles de seguir.
El fuego se apagará más rápido.
El agua de lluvia puede recolectarse.
```

---

# 30. Diseño recomendado del núcleo del bot

A nivel lógico, cada cierto tiempo el bot debería procesar “ticks”.

Por ejemplo, cada 5 minutos:

```txt
Actualizar hambre/sed/sueño.
Reducir tiempos de actividad.
Resolver actividades terminadas.
Mover NPCs.
Procesar modo automático.
Generar percepciones.
Enviar mensajes privados relevantes.
Actualizar clima/eventos.
```

No hace falta que sea cada segundo. Con ticks de 5 o 10 minutos ya se sentiría vivo y sería más fácil de programar.

---

# 31. Comandos iniciales recomendados

Yo empezaría con pocos:

```txt
/entrar
/estado
/inventario
/mirar
/explorar
/mover norte
/mover sur
/mover este
/mover oeste
/buscar
/descansar
/comer
/beber
/ayuda
/modo manual
/modo automatico
/diario
/mapa
```

Después agregaría:

```txt
/rastrear
/fabricar
/reparar
/leer
/cazar
/pescar
/esconderse
/vigilar
/hablar
/intercambiar
/atacar
/huir
/curar
/cocinar
/encender fuego
/apagar fuego
/colocar trampa
```

---

# 32. Cómo lo simplificaría para la primera versión

Para no hacerlo imposible desde el comienzo, la primera versión debería tener esto:

## Versión 1 jugable

* 9 a 13 casillas.
* 10 a 20 jugadores.
* Mensajes privados.
* Movimiento entre casillas.
* Estado básico: HP, hambre, sed, sueño.
* Inventario simple.
* Buscar recursos.
* Comer/beber/descansar.
* Modo automático básico.
* Ruido entre casillas.
* Estrellas.
* Torre final.
* Algunos NPCs simples.
* Diario.
* Mapa personal.

Con eso ya tienes un evento muy potente.

Después agregas:

* Olores.
* Rastreo avanzado.
* Clima.
* Crafteo complejo.
* Barco/tren/rutas alternativas.
* NPCs con agenda real.
* Comandos desbloqueables.
* Sistema de libros.
* Combate profundo.
* Rutinas personalizadas.

---

# 33. Mi propuesta de loop principal

El ciclo jugable sería:

```txt
1. Despiertas en una casilla.
2. Miras el entorno.
3. Percibes señales.
4. Decides explorar, recolectar, moverte, esconderte o descansar.
5. Encuentras recursos, peligros, pistas o jugadores.
6. Tu hambre/sed/sueño avanzan con el tiempo.
7. Aprendes habilidades o consigues objetos.
8. Descubres rutas hacia estrellas o escapes alternativos.
9. Sobrevives hasta el día del helicóptero.
10. Llegas a la torre o encuentras otra forma de escapar.
```

La gracia está en que cada jugador vive una historia distinta.

---

# 34. Frase base del diseño

Yo definiría el juego así:

> **Un Battle Royale narrativo de supervivencia en tiempo real, jugado por comandos de Discord, donde cada participante solo conoce lo que su personaje ve, escucha, huele, recuerda o deduce.**

Eso resume muy bien la identidad.

---

# 35. Conclusión

La idea funciona mejor si el juego no se siente como una tabla de números, sino como una historia viva.

El canal público sería la superficie.

Los mensajes privados serían la experiencia real.

El bot sería como un narrador, árbitro y simulador de mundo.

Y el modo automático permitiría que el evento siga vivo incluso cuando los jugadores no están conectados todo el día.

Para mí, los pilares deberían ser:

```txt
Información limitada.
Tiempo real.
Supervivencia.
Percepción.
Rastros.
Automatización.
Misterio.
Decisiones con riesgo.
Historias personales.
```

Con eso, el evento puede sentirse como una mezcla entre **Battle Royale, juego de rol por texto, simulador de supervivencia y novela emergente multijugador**.
