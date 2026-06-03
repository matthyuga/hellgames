Sí, encaja perfecto. El **desierto hollow con NPCs vivientes** puede transformarse en una versión de prueba dentro del evento Battle Royale: una isla donde los jugadores no solo buscan loot y estrellas, sino que entran en contacto con personajes que **tienen miedo, hambre, objetivos, alianzas, rencores y secretos**.

La clave sería que los NPCs no sean “misiones con patas”, sino pequeñas entidades narrativas con agenda propia.

## Concepto central del evento

**Nombre posible:**
**Battle Royale: Isla de los Ecos Vivientes**
o
**Battle Royale: Horizonte Hollow**

Los participantes del server quedan atrapados en una isla durante varios días. El objetivo final sigue siendo escapar, llegar a la torre y reunir estrellas, pero ahora el mapa está habitado por NPCs que no son simples enemigos.

Algunos NPCs quieren escapar.
Otros quieren usar a los jugadores.
Otros ya se rindieron.
Otros cazan estrellas.
Otros protegen zonas.
Otros forman cultos, bandas o refugios.

El jugador no sabe al principio quién miente.

---

# 1. Cómo hacerlo funcionar en Discord

Para el evento no hace falta simular una IA complejísima al principio. Podemos crear un sistema híbrido:

**Marvabot muestra eventos, zonas, NPCs y decisiones.**
Los jugadores responden con comandos o botones.
El bot calcula consecuencias simples.
Y vos, como director del evento, podés intervenir cuando haga falta para narrar momentos importantes.

Ejemplo:

```text
/mover zona 7
/interactuar npc "Sira"
/hablar "Busco comida, no problemas"
/ofrecer item agua
/atacar npc
/aliarse npc
/registrar zona
```

Cada jugador o grupo tendría:

```text
HP
Hambre
Sed
Moral
Inventario
Estrellas
Reputación
Relaciones con NPCs
Estado actual
Zona actual
```

Y cada NPC tendría:

```text
Nombre
Zona
Objetivo
Personalidad
Confianza hacia el jugador
Miedo
Ambición
Recursos
Secreto
Probabilidad de traición
Relaciones con otros NPCs
```

---

# 2. La idea fuerte: NPCs con agenda propia

Cada NPC debería tener tres capas:

## Capa visible

Lo que el jugador ve.

Ejemplo:

**Sira, la exploradora herida**
Está escondida en una estación abandonada. Dice que solo quiere sobrevivir. Tiene conocimientos del mapa y sabe dónde puede aparecer una estrella.

## Capa real

Lo que realmente quiere.

Sira quiere llegar a la torre antes que todos. No quiere matar, pero si el jugador consigue demasiadas estrellas, puede robarle una durante la noche.

## Capa secreta

Lo que puede descubrirse con confianza, investigación o traición.

Sira ya escapó de otra edición del evento, pero la volvieron a capturar. Sabe que la torre no es exactamente una salida limpia.

---

# 3. Tipos de NPCs para la isla

Yo usaría varios arquetipos. No todos tienen que ser enemigos.

## 1. El aliado frágil

Ayuda mucho, pero necesita protección.

Ejemplo:
**Nara, la médica improvisada**

Puede curar heridas, pero no pelea bien. Si el jugador la protege, puede salvarlo de morir una vez. Si la abandona, puede unirse a otro grupo.

Uso jugable:

```text
+ curaciones
+ información sobre venenos/heridas
- consume comida y agua
- puede ser capturada
```

---

## 2. El oportunista

No es malo, pero siempre busca ganar.

Ejemplo:
**Varek, el comerciante de chatarra**

Cambia comida, vendas, munición o pistas por estrellas, favores o secretos.

Puede vender información falsa si el jugador tiene mala reputación.

Uso jugable:

```text
+ comercio
+ rumores
+ objetos raros
- precios variables
- puede delatar tu posición
```

---

## 3. El traidor carismático

Parece el mejor aliado posible.

Ejemplo:
**Lian, el guía de la selva blanca**

Ayuda a atravesar zonas peligrosas, evita trampas y conoce rutas secretas. Pero su meta real es reunir jugadores confiados y venderlos a un grupo más fuerte.

Uso jugable:

```text
+ guía rutas seguras
+ reduce daño por exploración
+ acceso a zonas ocultas
- alta probabilidad de traición
- puede robar estrella
```

---

## 4. El cazador honorable

Puede ser enemigo o aliado, según cómo lo traten.

Ejemplo:
**Gorath, el cazador de máscaras**

No ataca a débiles ni heridos. Solo desafía a quienes tengan varias estrellas. Si el jugador demuestra valor, puede respetarlo.

Uso jugable:

```text
+ duelo justo
+ puede perdonar al jugador
+ puede protegerlo si gana respeto
- peligroso en combate
- busca estrellas
```

---

## 5. El NPC roto

No es confiable porque está psicológicamente dañado.

Ejemplo:
**Mila, la chica del faro seco**

Habla con personas que no están ahí. A veces da información brillante. A veces conduce al jugador a una trampa creyendo que lo está ayudando.

Uso jugable:

```text
+ pistas raras
+ eventos misteriosos
+ puede detectar cosas ocultas
- comportamiento impredecible
- puede activar eventos peligrosos
```

---

## 6. El líder de facción

No interactúa como NPC común, sino como poder político.

Ejemplo:
**El Barón del Pozo**

Controla una zona con agua. No necesita perseguir jugadores: todos tarde o temprano necesitan pasar por su territorio.

Uso jugable:

```text
+ acceso a recursos
+ misiones de facción
+ protección temporal
- exige tributo
- puede convertir jugadores en enemigos públicos
```

---

# 4. Facciones vivientes dentro del evento

Para que se sienta real, los NPCs no deberían estar todos aislados. Algunos pertenecen a grupos.

## Los Refugiados

Quieren sobrevivir hasta el día 20. No buscan matar, pero pueden entregar a un jugador si eso salva al grupo.

**Relación con jugadores:** cooperativa, pero desconfiada.

## Los Recolectores

Buscan estrellas, comida, armas y objetos. Son pragmáticos. Si un jugador tiene recursos, pueden comerciar o emboscarlo.

**Relación con jugadores:** neutral/peligrosa.

## Los Devotos de la Torre

Creen que solo algunos merecen escapar. Hacen rituales con estrellas y atacan a quienes consideran “impuros”.

**Relación con jugadores:** hostil o manipuladora.

## Los Hollow del Desierto

NPCs más extraños, casi espirituales. No son monstruos comunes. Algunos recuerdan vidas anteriores, otros repiten patrones, otros ofrecen pactos.

**Relación con jugadores:** misteriosa.

## Los Vigilantes

Actúan como sistema de control del evento. Pueden ser drones, guardias, entidades, máscaras o jueces. Castigan trampas, zonas prohibidas o acumulación excesiva de poder.

**Relación con jugadores:** amenaza superior.

---

# 5. Sistema de confianza y traición

Cada NPC puede tener una barra oculta de confianza.

```text
Confianza: -100 a +100
```

Ejemplo:

```text
-100: quiere matarte o venderte
-50: desconfía
0: neutral
+30: coopera
+60: te cuenta secretos
+90: arriesga su vida por vos
```

Pero también tendría una segunda variable:

```text
Interés propio: bajo / medio / alto / extremo
```

Eso evita que la confianza sea garantía absoluta.

Un NPC puede quererte mucho, pero si su hija está secuestrada y necesita una estrella, puede traicionarte igual.

Eso lo vuelve más humano.

---

# 6. Ejemplo de evento real con NPC viviente

Supongamos que un jugador entra a la casilla 9.

```text
ZONA 9 · Estación Hundida

Encuentras una estructura metálica semienterrada. Hay señales de fuego reciente.
Dentro, una mujer con una venda en el brazo apunta con una lanza improvisada.

NPC encontrado: Sira, exploradora herida.

Sira dice:
"No te acerques. No sé si eres concursante, saqueador o uno de ellos."
```

Opciones:

```text
1. Levantar las manos y hablar.
2. Ofrecer agua.
3. Preguntar por estrellas.
4. Intentar robarle.
5. Retirarse.
```

Si elige ofrecer agua:

```text
Sira baja apenas la lanza.

Confianza +15.
Pierdes: 1 agua.
Obtienes: rumor sobre la zona 12.
```

Pero internamente Sira guarda:

```text
Objetivo oculto: llegar a la torre.
Secreto: sabe una ruta hacia una compuerta lateral.
Condición de traición: si el jugador tiene 6+ estrellas y duerme en la misma zona.
```

---

# 7. Los NPCs también deberían moverse

Esto es importante. Para que parezcan vivos, no deberían quedarse siempre en la misma casilla.

Cada día del evento, algunos NPCs pueden cambiar de zona.

Ejemplo:

```text
Día 1: Sira está en zona 9.
Día 3: Sira se mueve a zona 12.
Día 5: Sira aparece comerciando con Varek.
Día 7: Sira desaparece.
Día 9: un jugador encuentra su mochila ensangrentada.
Día 11: Sira reaparece aliada con otro grupo.
```

Eso crea historia emergente.

Los jugadores empiezan a decir:

> “No confíen en Sira, a mí me robó.”
> “Mentira, a mí me salvó.”
> “Creo que depende de cómo la trates.”
> “Varek está vendiendo información de los jugadores.”

Ahí el evento empieza a vivir en la comunidad.

---

# 8. Sistema simple de memoria para Marvabot

Para empezar, Marvabot no necesita una IA autónoma perfecta. Solo necesita guardar estados.

Por ejemplo:

```json
{
  "npc_sira": {
    "zona": 12,
    "estado": "herida",
    "confianza": {
      "usuario_1": 45,
      "usuario_2": -20
    },
    "secreto_revelado_a": ["usuario_1"],
    "objetivo": "reunir 3 estrellas",
    "aliado_actual": "usuario_1",
    "traicion_realizada": false
  }
}
```

Con eso, el bot puede responder distinto a cada usuario.

Usuario A:

```text
Sira te reconoce y guarda la lanza.
"Volviste. Pensé que habías muerto."
```

Usuario B:

```text
Sira te apunta de inmediato.
"Después de lo que hiciste, no vuelvas a acercarte."
```

Eso ya da sensación de NPC viviente.

---

# 9. Cómo conectar esto con las estrellas

Las estrellas no deberían estar solo tiradas como loot. Algunas deberían estar ligadas a NPCs.

Ejemplos:

## Estrella protegida

Un NPC la tiene, pero no sabe su valor real.

## Estrella maldita

Da acceso a la torre, pero atrae enemigos durante la noche.

## Estrella negociada

Un comerciante la entrega si el jugador cumple una misión.

## Estrella robada

Un NPC se la quitó a otro jugador o a otro NPC.

## Estrella emocional

Un NPC la entrega solo si el jugador salva a alguien importante para él.

Esto hace que la recolección sea más narrativa.

---

# 10. Eventos nocturnos

La noche puede ser el momento donde los NPCs se sienten más vivos.

Cada noche, Marvabot podría hacer tiradas automáticas:

```text
- NPC se mueve.
- NPC roba recurso.
- NPC busca refugio.
- NPC ataca a otro NPC.
- NPC deja una pista.
- NPC es capturado.
- Facción cambia de zona.
- Un jugador con baja moral sufre penalización.
- Un aliado traiciona.
- Un aliado protege.
```

Ejemplo de anuncio global:

```text
NOCHE 4

Se escucharon disparos cerca del viejo observatorio.
El pozo del sector 6 fue tomado por los Recolectores.
Varek ya no está en el mercado del puente.
Un cuerpo apareció colgado en la entrada de la zona 3.
Alguien dejó una estrella falsa en la capilla rota.
```

Eso genera conversación en el server.

---

# 11. NPCs especiales para probar el sistema

Te propongo empezar con pocos NPCs, pero bien diseñados.

## Sira, la exploradora herida

Rol: aliada ambigua.
Meta: escapar.
Puede ayudar, robar o sacrificarse.

## Varek, el comerciante de chatarra

Rol: vendedor de recursos e información.
Meta: enriquecerse y sobrevivir.
Puede vender secretos de jugadores.

## Nara, la médica refugiada

Rol: curadora.
Meta: proteger a su hermano menor.
Puede abandonar al jugador si este actúa con crueldad.

## Gorath, el cazador de estrellas

Rol: amenaza honorable.
Meta: reunir estrellas mediante duelos.
No ataca jugadores débiles.

## Mila, la chica del faro seco

Rol: NPC misteriosa.
Meta: encontrar “la voz bajo la arena”.
Puede revelar secretos o activar horrores.

## El Barón del Pozo

Rol: líder de facción.
Meta: controlar el agua de la isla.
Puede ser aliado político o villano.

## Los Gemelos Sin Nombre

Rol: evento raro.
Meta: copiar identidades.
Pueden hacerse pasar por otro NPC.

---

# 12. El sistema de “realismo narrativo”

Para que se sientan vivos, cada NPC debería tener estas reglas:

```text
1. Quiere algo.
2. Teme algo.
3. Necesita algo.
4. Oculta algo.
5. Cambia si el jugador lo afecta.
6. Puede actuar aunque el jugador no esté presente.
```

Ejemplo:

**Nara**

```text
Quiere: salvar a su hermano.
Teme: quedarse sin medicinas.
Necesita: vendas, agua limpia, refugio.
Oculta: su hermano fue mordido por algo.
Cambia: si el jugador mata inocentes, deja de ayudarlo.
Actúa sola: puede buscar medicinas durante la noche.
```

Esto es más importante que tener cientos de líneas de diálogo.

---

# 13. Sistema de reputación del jugador

Además de la relación individual con cada NPC, el jugador puede tener reputación global.

```text
Reputación:
- Protector
- Comerciante
- Traidor
- Asesino
- Saqueador
- Médico
- Cazador de estrellas
- Mentiroso
- Líder
```

Los NPCs reaccionan según esa fama.

Ejemplo:

```text
Si eres conocido como Protector:
Los refugiados confían más rápido en ti.

Si eres conocido como Traidor:
Los comerciantes suben precios.
Los aliados duermen lejos de ti.
Los cazadores pueden buscarte.

Si eres conocido como Asesino:
Algunos te temen.
Otros quieren matarte antes de que crezcas.
```

---

# 14. Cómo probarlo sin hacerlo enorme

Yo lo haría en fases.

## Fase 1: Evento simple

Duración: 7 días de prueba.
Mapa: 10 a 15 casillas.
NPCs: 5 principales.
Recursos: comida, agua, vendas, arma simple, estrella.
Acciones por día: 2 o 3 por jugador.

Objetivo: ver si la gente interactúa con NPCs y si le importa lo que pasa.

---

## Fase 2: Isla completa

Duración: 20 días.
Mapa: 20+ casillas.
NPCs: 10 a 15.
Facciones: 3 o 4.
Eventos nocturnos.
Estrellas escasas.
Final en la torre.

---

## Fase 3: NPCs semiautónomos

Marvabot empieza a mover NPCs según objetivos.

Ejemplo:

```text
Si Sira tiene 2 estrellas, intentará ir hacia zona cercana a la torre.
Si Varek tiene poca mercancía, buscará zona de saqueo.
Si Nara pierde a su hermano, cambia su personalidad.
Si Gorath oye que alguien tiene 5 estrellas, lo persigue.
```

---

# 15. Ejemplo de tabla de NPC

Podrías manejar algo así:

| NPC            | Rol          | Meta                | Ayuda                  | Riesgo                |
| -------------- | ------------ | ------------------- | ---------------------- | --------------------- |
| Sira           | Exploradora  | Escapar             | Rutas, pistas          | Puede robar estrellas |
| Varek          | Comerciante  | Acumular recursos   | Compra/venta           | Vende información     |
| Nara           | Médica       | Salvar a su hermano | Curación               | Puede exigir favores  |
| Gorath         | Cazador      | Reunir estrellas    | Respeto/duelos         | Ataca fuertes         |
| Mila           | Oráculo rota | Seguir voces        | Secretos raros         | Eventos impredecibles |
| Barón del Pozo | Líder        | Controlar agua      | Protección             | Extorsión             |
| Gemelos        | Entidad      | Copiar identidades  | Información falsa/real | Engaño extremo        |

---

# 16. El toque “Hollow”

Para conectar con el desierto hollow, la isla puede tener una zona especial: **El Desierto Blanco**.

No es toda la isla, sino una región peligrosa.

Ahí los NPCs se comportan raro.
Las voces imitan jugadores.
Los muertos pueden dejar ecos.
Algunos NPCs recuerdan cosas que no deberían saber.
Puede haber estrellas enterradas en restos de competidores anteriores.

Ejemplo de zona:

```text
ZONA 17 · Desierto Blanco

La arena no es arena. Parece polvo de hueso.
Cada paso produce un sonido hueco.
A lo lejos, alguien grita tu nombre usando la voz de un amigo del server.
```

Eventos posibles:

```text
- Encuentras un eco de un NPC muerto.
- Una estrella falsa intenta guiarte.
- Un aliado empieza a desconfiar de ti.
- Aparece una copia de un jugador.
- Un NPC revela una memoria que no vivió.
```

Esto puede ser la parte más psicológica del evento.

---

# 17. Lo más importante: que los jugadores hablen entre sí

El verdadero éxito del evento no sería solo que usen comandos. Sería que en el Discord empiecen a comentar:

```text
"¿Alguien vio a Varek?"
"No entren al desierto blanco de noche."
"Sira me salvó, no la maten."
"El Barón está cobrando agua demasiado cara."
"Gorath me retó porque tengo 4 estrellas."
"Creo que Mila sabe dónde está una compuerta."
```

Ahí el evento deja de ser un minijuego y se vuelve una historia comunitaria.

---

# Mi recomendación

Sí, lo pondría a prueba. Pero no empezaría con una simulación gigante. Haría una **temporada piloto**:

```text
Duración: 7 días
Participantes: voluntarios
Mapa: 12 casillas
NPCs principales: 6
Facciones: 2
Objetivo: conseguir 3 estrellas y llegar a una zona de extracción menor
```

Después de esa prueba, si la gente se engancha, se expande al evento grande de 20 días con la torre, las 10 estrellas y los NPCs más complejos.

La idea tiene muchísimo potencial porque convierte el Battle Royale en algo más que combate: lo vuelve una mezcla de **supervivencia, rol social, misterio, traición y reputación comunitaria**.
