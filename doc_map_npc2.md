Sí, esto ya empieza a sentirse como una **simulación viva**, no solo un evento de casillas. Antes de avanzar: junio tiene 30 días, así que podrías hacerlo hasta el **30 de junio a las 23:59** o extenderlo al **1 de julio** si quieres darle ese “día extra final”.

La idea de que los NPC cambien su conducta según lo que encuentran es excelente. Eso permite que no sean personajes estáticos, sino “participantes vivos”.

Ejemplo simple:

> Un NPC cobarde con una lanza se anima a explorar.
> Un NPC con pistola sin balas empieza a buscar munición.
> Un NPC con 6 estrellas deja de comerciar y comienza a esconderse.
> Un NPC con comida abundante se vuelve negociador.
> Un NPC herido busca medicina, refugio o alguien que lo proteja.

---

# Sistema base de mochila y carga

Para que no sea demasiado complicado, usaría dos límites:

**Slots:** cuántos objetos puede llevar.
**Peso:** cuánto aguanta antes de cansarse más rápido.

## Mochila básica

Todos los participantes empiezan con:

* 2 estrellas.
* 1 botella plástica de agua, 1 litro.
* 1 sándwich.
* 1 manzana.
* 1 linterna con batería llena.
* 1 mochila básica.

La mochila básica podría tener:

| Contenedor     |    Slots | Peso cómodo | Peso máximo |
| -------------- | -------: | ----------: | ----------: |
| Mochila básica | 12 slots |       10 kg |       18 kg |

Hasta **10 kg**, camina normal.
Entre **10 y 18 kg**, se cansa más rápido.
Más de **18 kg**, no puede moverse bien o debe soltar cosas.

Cada punto de **Fuerza** podría aumentar el peso cómodo en **+2 kg**.
Cada punto de **Resistencia** podría reducir el cansancio por carga.

Ejemplo:

> Fuerza 3 = 10 kg base + 6 kg = 16 kg cómodos.
> Resistencia alta = se cansa más lento aunque lleve peso.

---

# Tamaño de objetos por slots

Para no calcular todo con números exactos, puedes usar categorías.

| Tamaño      | Slots | Ejemplos                                                            |
| ----------- | ----: | ------------------------------------------------------------------- |
| Muy pequeño | 0 o 1 | Bala, llave, nota, estrella, medicina pequeña                       |
| Pequeño     |     1 | Cuchillo, manzana, venda, batería, cantimplora                      |
| Mediano     |     2 | Pistola, cuerda, linterna, comida enlatada, herramienta             |
| Grande      |     3 | Hacha, lanza corta, rifle, kit médico, bidón pequeño                |
| Muy grande  |    4+ | Generador, caja de munición, pieza de motor, tienda, batería grande |

Las **estrellas** deberían ocupar poco, quizás **0 slots**, pero son robables y peligrosas de llevar.

---

# Transportes y carga extra

| Transporte          |        Carga extra | Condición                                         |
| ------------------- | -----------------: | ------------------------------------------------- |
| Mula                |  +40 kg / 16 slots | Requiere Animales o comida                        |
| Caballo             |  +25 kg / 10 slots | Más rápido, pero menos carga                      |
| Carroza con caballo | +100 kg / 40 slots | Requiere animal + reparar ruedas                  |
| Cuatri              |  +60 kg / 20 slots | Requiere combustible y mecánica                   |
| Baúl portátil       |          +20 slots | No se lleva encima, se deja en refugio o vehículo |
| Barco reparado      |        Mucha carga | Ruta de escape marítima                           |

Esto abre una jugabilidad muy buena: alguien fuerte puede cargar más, alguien con animales puede usar mula, alguien con mecánica puede usar cuatri, y alguien con construir puede hacer un depósito oculto.

---

# Sistema de objetos de la isla

## 1. Comida y agua

| Objeto          | Uso                                |
| --------------- | ---------------------------------- |
| Botella de agua | Hidratarse, llenar en ríos o pozos |
| Cantimplora     | Mejor que botella, más resistente  |
| Agua sucia      | Requiere hervir o purificar        |
| Sándwich        | Comida inicial                     |
| Manzana         | Comida ligera                      |
| Carne cruda     | Requiere fogata                    |
| Carne seca      | Dura más días                      |
| Pescado         | Requiere pescar y cocinar          |
| Bayas           | Algunas curan, otras intoxican     |
| Latas de comida | Buen recurso de supervivencia      |

## 2. Medicina

| Objeto              | Uso                           |
| ------------------- | ----------------------------- |
| Venda               | Cura heridas leves            |
| Antiséptico         | Evita infección               |
| Analgésico          | Reduce penalización por dolor |
| Antídoto            | Cura veneno                   |
| Kit médico          | Cura heridas graves           |
| Hierbas medicinales | Base para medicina            |
| Jeringa estimulante | Recupera energía, con riesgo  |

## 3. Recursos

| Objeto          | Uso                             |
| --------------- | ------------------------------- |
| Madera          | Refugios, lanzas, fogatas       |
| Piedra          | Herramientas, armas simples     |
| Hueso           | Lanzas, cuchillos, anzuelos     |
| Cristal         | Armas raras, rituales, portal   |
| Cuerda          | Trampas, escalada, reparación   |
| Tela            | Vendas, refugios                |
| Chatarra        | Mecánica, barricadas            |
| Carbón          | Fogatas, tren, forja            |
| Combustible     | Cuatri, generador, barco        |
| Batería         | Linterna, radio, sistemas       |
| Piezas de motor | Barco, generadores, vehículos   |
| Pólvora         | Munición, explosivos simples    |
| Casquillos      | Fabricar balas                  |
| Metal           | Armas, herramientas, reparación |

## 4. Armas comunes

| Arma             | Ventaja                                 |
| ---------------- | --------------------------------------- |
| Cuchillo oxidado | Ligero, fácil de ocultar                |
| Lanza de madera  | Mantiene distancia                      |
| Lanza de hueso   | Mejor contra criaturas                  |
| Lanza de cristal | Daño alto, frágil o rara                |
| Hacha            | Arma y herramienta                      |
| Machete          | Bueno para jungla y combate             |
| Arco simple      | Silencioso                              |
| Ballesta vieja   | Más daño, lenta                         |
| Pistola oxidada  | Fuerte, pero puede fallar               |
| Rifle viejo      | Largo alcance                           |
| Arma militar     | Muy poderosa, munición rara             |
| Pistola láser    | Ultra rara, quizá viene del portal      |
| Rifle láser      | Objeto legendario, peligroso de activar |

## 5. Tecnología

| Objeto            | Uso                           |
| ----------------- | ----------------------------- |
| Tarjeta militar   | Acceso a estación 19          |
| Código de torre   | Pista para hackear casilla 13 |
| Radio portátil    | Comunicación limitada         |
| Dron roto         | Puede repararse               |
| Cámara rota       | Piezas electrónicas           |
| Batería grande    | Energía para radio/generador  |
| Terminal portátil | Hackeo avanzado               |
| Núcleo láser      | Arma o llave tecnológica      |

---

# Escape secreto adicional: casilla 22

La casilla 22 puede volverse muy interesante porque parece una zona de frío y refugio, pero esconde una salida.

## Casilla 22: Pueblo Nevado / Cabaña del Sótano

Hay una cabaña vieja medio enterrada en nieve. En el sótano existe una puerta metálica cubierta por hielo. Detrás hay un pasadizo subterráneo que sale de la isla.

Condiciones posibles:

* Requiere **Explorar** o **Investigación** para encontrar la trampilla.
* Requiere **Talar** o **Fuerza** para abrir la puerta congelada.
* Requiere **Construir** o **Mecánica** para reforzar el túnel.
* Requiere comida, abrigo o antorchas para cruzar.
* Puede haber criaturas subterráneas o un NPC escondido.

Pistas conectadas:

* Sira en casilla 1 vio “luces bajo la nieve”.
* Nox en casilla 3 sabe que los túneles se conectaban con depósitos viejos.
* Eira en casilla 22 escuchó golpes bajo la cabaña.
* Un mapa roto en casilla 7 muestra una línea entre 3 y 22.

---

# Hackear la torre sin 10 estrellas

Esto es buenísimo porque agrega una ruta de alto riesgo para personajes inteligentes.

## Ruta oficial

Tener **10 estrellas**.
Los drones reconocen al jugador como autorizado.
Puede entrar por las compuertas de la casilla 13.

## Ruta ilegal

Hackear cámaras, drones y compuertas.

Requiere combinación de:

* **Informática**
* **Mecánica**
* **Investigación**
* **Alerta**
* **Ocultar presencia**
* **Coraje**

Posibles pasos:

1. Conseguir una **tarjeta militar** en casilla 19.
2. Encontrar un **código parcial** en casilla 20.
3. Reparar un terminal o batería.
4. Entrar a la torre 13 evitando drones.
5. Hackear una compuerta.
6. Resistir una alarma.

Riesgo:

> Si falla, los drones marcan al jugador como intruso. Durante 24 horas, los vigilantes de la torre pueden rastrearlo.

Esto hace que las estrellas sean la ruta “segura”, pero no la única.

---

# 10 NPC participantes nuevos

Estos NPCs son móviles. Tienen habilidades, objetos, metas y pueden cambiar de conducta según lo que encuentran.

## 1. Renzo “Manos Frías”

**Perfil:** ladrón cuidadoso, evita pelear.
**Habilidades:** Hurtar, Ocultar Presencia, Explorar.
**Meta:** juntar estrellas robando sin ser visto.
**Objetos iniciales:** ganzúa, cuchillo pequeño, cuerda fina.
**Casillas preferidas:** 5, 10, 16, 21, 24.

**Cambio de conducta:**
Si consigue una estrella extra, deja de robar comida y empieza a espiar jugadores.
Si consigue un arma de fuego, se vuelve más atrevido pero sigue evitando combates directos.

---

## 2. Brina Val

**Perfil:** exploradora práctica, no confía en grupos grandes.
**Habilidades:** Supervivencia, Recolectar, Medicina.
**Meta:** sobrevivir sin matar y encontrar una salida alternativa.
**Objetos iniciales:** venda, hierbas secas, cantimplora vacía.
**Casillas preferidas:** 4, 11, 17, 22, 23.

**Cambio de conducta:**
Si encuentra antídoto o kit médico, empieza a ofrecer curaciones a cambio de pistas.
Si es traicionada, evita zonas sociales y se oculta en bosques.

---

## 3. Dagan Muro

**Perfil:** constructor fuerte, útil para refugios y barricadas.
**Habilidades:** Construir, Talar, Atletismo.
**Meta:** crear una base segura y cobrar por protección.
**Objetos iniciales:** martillo, clavos, hacha gastada.
**Casillas preferidas:** 2, 8, 14, 21, 23.

**Cambio de conducta:**
Si consigue suficiente madera, construye un refugio fortificado.
Si consigue una lanza o hacha buena, empieza a controlar el paso de una casilla.

---

## 4. Mila Kross

**Perfil:** técnica nerviosa, muy valiosa para rutas secretas.
**Habilidades:** Informática, Mecánica, Investigación.
**Meta:** hackear la torre o activar la radio militar.
**Objetos iniciales:** destornillador, batería pequeña, cable cortado.
**Casillas preferidas:** 13, 19, 20, 3, 16.

**Cambio de conducta:**
Si encuentra tarjeta militar, corre hacia la casilla 19.
Si encuentra código de torre, intenta infiltrarse en la 13.
Si consigue pistola sin balas, busca munición o alguien que la proteja.

---

## 5. Orven Sal

**Perfil:** marinero testarudo, obsesionado con escapar por mar.
**Habilidades:** Navegar, Mecánica, Negociar.
**Meta:** reparar el barco de la casilla 16.
**Objetos iniciales:** brújula rota, llave inglesa, mapa mojado.
**Casillas preferidas:** 5, 16, 21, 17, 20.

**Cambio de conducta:**
Si consigue combustible, se instala cerca del barco.
Si encuentra piezas de motor, busca aliados.
Si otro jugador tiene herramientas, intentará negociar antes de robar.

---

## 6. Yael Prisma

**Perfil:** curiosa peligrosa, atraída por el portal y los cristales.
**Habilidades:** Ocultismo, Ciencias, Coraje.
**Meta:** activar el portal de la casilla 12.
**Objetos iniciales:** cristal opaco, libreta de símbolos, vela negra.
**Casillas preferidas:** 6, 7, 11, 12, 15.

**Cambio de conducta:**
Si consigue una estrella, intenta usarla como catalizador.
Si obtiene un arma láser del portal, se vuelve impredecible.
Si falla un ritual, puede quedar herida o atraer criaturas.

---

## 7. Tarek Buey

**Perfil:** fuerte, directo, más noble de lo que parece.
**Habilidades:** Pelear, Talar, Coraje.
**Meta:** conseguir estrellas por combate o proteger a alguien débil.
**Objetos iniciales:** palo pesado, carne seca, cuerda gruesa.
**Casillas preferidas:** 2, 8, 14, 18, 25.

**Cambio de conducta:**
Si consigue un hacha, se vuelve guardián de su zona.
Si obtiene una estrella por combate, puede sentirse culpable y buscar redención.
Si una criatura amenaza a un grupo, probablemente interviene.

---

## 8. Nara Vex

**Perfil:** manipuladora social, usa pactos y mentiras.
**Habilidades:** Mentir, Persuasión, Negociar.
**Meta:** escapar usando a otros como piezas.
**Objetos iniciales:** anillo falso, comida enlatada, nota falsificada.
**Casillas preferidas:** 9, 17, 21, 24, 10.

**Cambio de conducta:**
Si consigue información sobre una ruta secreta, la vende en partes.
Si consigue arma, no la muestra.
Si alguien descubre una mentira suya, intenta culpar a otro.

---

## 9. Silas Crow

**Perfil:** tirador metódico, paciente y frío.
**Habilidades:** Puntería, Alerta, Investigación.
**Meta:** conseguir munición y controlar zonas abiertas.
**Objetos iniciales:** pistola oxidada sin balas, mira rota, 2 casquillos vacíos.
**Casillas preferidas:** 19, 20, 10, 18, 25.

**Cambio de conducta:**
Si consigue balas, evita negociar y empieza a vigilar rutas.
Si no encuentra munición, busca pólvora o alguien con artillería.
Si queda herido, se esconde en altura y dispara solo como amenaza.

---

## 10. Ivo Lumbre

**Perfil:** artesano de armas improvisadas.
**Habilidades:** Artesanía, Artillería, Recolectar.
**Meta:** fabricar armas raras y venderlas o usarlas.
**Objetos iniciales:** piedra afilada, trozo de metal, tela vieja.
**Casillas preferidas:** 3, 12, 18, 24, 25.

**Cambio de conducta:**
Si consigue huesos, fabrica lanzas.
Si consigue cristal, intenta crear arma especial.
Si consigue pólvora y casquillos, fabrica munición y se vuelve muy buscado.

---

# Tabla rápida de conducta por objeto encontrado

Esto te puede servir para que el bot o el narrador decida qué hacen los NPC.

| Objeto encontrado     | Cambio probable de conducta                          |
| --------------------- | ---------------------------------------------------- |
| Arma cuerpo a cuerpo  | Explora más, se defiende, puede amenazar             |
| Pistola sin balas     | Busca munición, pólvora o trueque                    |
| Munición              | Se vuelve más peligroso y evita zonas de negociación |
| Comida abundante      | Puede comerciar o esconderse                         |
| Medicina              | Se vuelve valioso para otros o busca aliados         |
| Tarjeta militar       | Se dirige a 19 o 20                                  |
| Código de torre       | Se dirige a 13 o busca informática                   |
| Madera y herramientas | Construye refugio o barricada                        |
| Combustible           | Va hacia 16, 19 o vehículos                          |
| Cristal raro          | Va hacia 12, 15 o 25                                 |
| Estrella extra        | Se oculta, negocia fuerte o atrae cazadores          |
| Arma legendaria       | Cambia completamente su rol en la isla               |

---

# Rutas de escape actualizadas

| Ruta                |    Casilla | Estilo                   | Requisitos posibles                       |
| ------------------- | ---------: | ------------------------ | ----------------------------------------- |
| Helicóptero oficial |         13 | Final principal          | 10 estrellas                              |
| Hackeo de la torre  | 13 + 19/20 | Alto riesgo              | Informática, tarjeta, código              |
| Tren subterráneo    |          3 | Ruta técnica/subterránea | Carbón, llave, reparar vía                |
| Portal inestable    |         12 | Ruta sobrenatural/rara   | Cristales, ocultismo, estrella            |
| Barco reparado      |         16 | Ruta marítima            | Madera, piezas, combustible, navegar      |
| Radio militar       | 19/20 → 13 | Escape anticipado        | Antena, radio, coordenadas de torre       |
| Sótano nevado       |         22 | Ruta secreta oculta      | Investigar, abrir trampilla, cruzar túnel |

---

# Golem de lava del volcán

La casilla 25 puede tener un evento especial.

## Gorath, el Golem de Lava

No es simplemente enemigo. Puede actuar según el comportamiento del jugador.

**Ataca si:**

* El jugador roba cristal volcánico sin permiso.
* Usa explosivos.
* Lleva un arma láser activa.
* Intenta saquear el núcleo del volcán.

**Ayuda si:**

* El jugador le entrega cristal del portal.
* Tiene Coraje alto y no lo ataca.
* Usa Ocultismo o Ciencias para comunicarse.
* Derrota a una criatura que estaba dañando el volcán.

**Recompensas posibles:**

* Núcleo de lava.
* Cristal ígneo.
* Protección temporal.
* Una estrella custodiada.
* Pista sobre el portal o el tren subterráneo.

---

# Cómo esto mueve el evento

Lo mejor de este sistema es que los NPC participantes pueden crear noticias diarias.

Ejemplos:

> Día 5: Silas encontró una pistola oxidada en la estación militar, pero aún no tiene balas. Se rumorea que busca pólvora en el Bastión del Desierto.

> Día 8: Orven consiguió una pieza de motor. Fue visto caminando hacia la Playa del Naufragio.

> Día 11: Nara vendió tres mapas distintos a tres participantes diferentes. Al menos dos eran falsos.

> Día 14: Mila Kross activó una cámara en la torre. Los drones comenzaron a patrullar una zona más amplia.

> Día 18: Alguien abrió la cabaña nevada. Desde entonces, se escuchan golpes bajo la casilla 22.

Esto le da vida a la isla incluso aunque los jugadores reales no hagan nada durante unas horas.
