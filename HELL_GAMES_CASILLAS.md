# Hell Games - Casillas de la isla

Documento canonico inicial para diseccionar el mapa en 25 escenarios jugables.
Cada casilla tiene una imagen recortada en `assets/map_cells/`.

Uso recomendado:

- Este archivo define el sabor narrativo y jugable de cada zona.
- Los detalles concretos de loot, criaturas y NPCs pueden pasar luego a JSON.
- Cada casilla debe poder generar exploracion, riesgo, rumor y memoria.

## Resumen rapido

| ID | Nombre | Rol principal | Peligro |
| --- | --- | --- | --- |
| 1 | Faro de la Vigilia Sagrada | Vision, radio, senales | Medio |
| 2 | Campamento Raíz Maldita | Inicio seguro, recursos basicos | Bajo |
| 3 | Minas de Hierro | Minerales, tuneles, derrumbes | Medio |
| 4 | Cascada de los Susurros | Agua, pesca, hierbas | Bajo |
| 5 | Puerto del Navegante | Cajas, herramientas, rutas maritimas | Medio |
| 6 | Círculo de Monolitos | Misterio, rituales, eventos nocturnos | Medio |
| 7 | Ruinas del Guardián | Trampas, acertijos, reliquias | Alto |
| 8 | Pradera Valle del Viento | Comida, campo abierto, viento | Bajo |
| 9 | Templo de las Hojas Carmesí | Caza, hongos, emboscadas | Medio |
| 10 | Bastión del Acantilado | Defensa, armas, facciones | Alto |
| 11 | Pantano de los Olvidados | Veneno, barro, ingredientes raros | Alto |
| 12 | Sector X | Cristales, energia extrana, mutaciones | Muy alto |
| 13 | Torre Centinela | Objetivo final, compuertas, drones | Muy alto |
| 14 | Granja Sangrienta | Comida, animales, herramientas | Medio |
| 15 | Templo del Sol | Acertijos solares, trampas, estrella | Alto |
| 16 | Costa del Naufragio Negro | Restos de barco, madera, botellas | Medio |
| 17 | Templo de la Luna | Agua, medicina, comercio | Medio |
| 18 | Cañón Partido | Puentes, persecuciones, emboscadas | Alto |
| 19 | Estación Militar | Tecnologia, generadores, vigilancia | Alto |
| 20 | Observatorio Militar | Radar, satelite, predicciones | Alto |
| 21 | Muelle Aguas Rojas | Trueque, pesca, refugio social | Medio |
| 22 | Pueblo Nevado | Frio, sotanos, ruta secreta | Alto |
| 23 | Jungla de Bambú Diabólico | Madera flexible, trampas, fauna rapida | Medio |
| 24 | Bastión Duna Seca | Cofres, mercado roto, calor | Alto |
| 25 | Volcán Ceniza Durmiente | Lava, humo, golem, estrella | Muy alto |

## 1. Faro de la Vigilia Sagrada

Imagen: `assets/map_cells/casilla_01_faro_de_la_vigilia_sagrada.png`

Arte de escenario: `assets/scenario_art/escenario_01_faro_de_la_vigilia_sagrada.png`

Mapa tactico: `assets/tactical_maps/scenario_01_faro_de_la_vigilia_sagrada/scenario_01_grid_14x14.png`

Rol jugable: punto de observacion, senales y radio.

Lore: Antes de que existieran los juegos, este faro era un santuario costero. Los vigilantes encendian la luz para guiar barcos y para mantener lejos algo que venia del mar. Ahora la torre sigue encendiendose algunas noches sin combustible, como si alguien rezara desde adentro.

Acciones posibles:

- subir al faro para observar casillas cercanas;
- buscar piezas de radio;
- encender una senal luminosa;
- revisar la casa del cuidador;
- ocultar objetos entre las rocas;
- vigilar movimientos en la costa norte.

Hallazgos posibles:

- mapa mojado;
- bateria pequena;
- aceite de lampara;
- lente agrietada;
- cable electrico;
- bengala;
- diario del farero.

Amenazas:

- caidas desde acantilados;
- exposicion visible desde varias casillas;
- ruido de metal en la torre;
- aves agresivas o criaturas costeras.

Ganchos:

- una transmision pide ayuda usando el nombre de un participante;
- la luz del faro apunta una noche hacia una casilla concreta;
- una estrella podria estar escondida dentro del mecanismo optico.

## 2. Campamento Raíz Maldita

Imagen: `assets/map_cells/casilla_02_campamento_raiz_maldita.png`

Arte de escenario: `assets/scenario_art/escenario_02_campamento_raiz_maldita.png`

Mapa tactico: `assets/tactical_maps/scenario_02_campamento_raiz_maldita/scenario_02_grid_14x14.png`

Rol jugable: zona inicial, recursos basicos y refugio temprano.

Lore: El campamento fue levantado sobre raices negras que nunca dejan de crecer. Las tiendas parecen recientes, pero bajo la tierra hay estacas, cuerdas y nombres grabados en madera humeda. Quien duerme aqui suele despertar con la sensacion de haber sido contado.

Acciones posibles:

- recolectar madera y ramas secas;
- buscar comida simple;
- hacer fogata;
- dormir con riesgo reducido;
- fabricar herramientas basicas;
- revisar tiendas y cajas.

Hallazgos posibles:

- rama seca;
- tela;
- cuerda fina;
- lata de comida;
- navaja;
- pedernal;
- mochila danada.

Amenazas:

- zona demasiado obvia para principiantes;
- saqueadores oportunistas;
- humo visible si se enciende fuego;
- animales pequenos atraidos por comida.

Ganchos:

- alguien dejo una lista de nombres tachados;
- un refugio parece usado durante la noche anterior;
- un NPC herido puede aparecer pidiendo agua.

## 3. Minas de Hierro

Imagen: `assets/map_cells/casilla_03_minas_de_hierro.png`

Arte de escenario: `assets/scenario_art/escenario_03_minas_de_hierro.png`

Mapa tactico: `assets/tactical_maps/scenario_03_minas_de_hierro/scenario_03_grid_14x14.png`

Rol jugable: minerales, tuneles, metal y riesgo de derrumbe.

Lore: Las minas abastecieron a la isla durante decadas, hasta que los mineros empezaron a oir golpes desde tuneles que no habian excavado. El hierro de estas vetas es resistente, pesado y extrañamente frio, perfecto para armas, puertas y secretos enterrados.

Acciones posibles:

- extraer piedra, carbon o mineral;
- explorar tuneles;
- reparar o usar vagonetas;
- buscar cofres de mineros;
- colocar trampas en entradas estrechas;
- refugiarse durante tormentas.

Hallazgos posibles:

- pico de mineria;
- carbon;
- pedernal;
- chatarra;
- casco con lampara;
- sal mineral;
- cristal raro.

Amenazas:

- derrumbes;
- oscuridad;
- falta de aire;
- criaturas de tunel;
- ruido amplificado.

Ganchos:

- una estrella puede estar en una galeria inestable;
- las vagonetas conectan con una ruta secreta;
- una pared tiene simbolos parecidos a los monolitos.

## 4. Cascada de los Susurros

Imagen: `assets/map_cells/casilla_04_cascada_de_los_susurros.png`

Arte de escenario: `assets/scenario_art/escenario_04_cascada_de_los_susurros.png`

Mapa tactico: `assets/tactical_maps/scenario_04_cascada_de_los_susurros/scenario_04_grid_14x14.png`

Rol jugable: agua potable, pesca, hierbas y descanso.

Lore: El agua cae limpia, pero nunca en silencio. Entre la espuma se oyen voces suaves que repiten frases perdidas por otros participantes. Algunos creen que la cascada recuerda conversaciones; otros creen que simplemente aprende a imitar a los vivos.

Acciones posibles:

- llenar botellas y cantimploras;
- pescar;
- buscar hierbas medicinales;
- lavar heridas;
- ocultarse detras de la cascada;
- rastrear pisadas en barro humedo.

Hallazgos posibles:

- agua limpia;
- peces;
- hierbas medicinales;
- frasco de vidrio;
- piedra lisa;
- musgo;
- anzuelo perdido.

Amenazas:

- resbalones;
- encuentros frecuentes;
- emboscadas desde rocas altas;
- huellas faciles de seguir.

Ganchos:

- detras de la cascada hay una grieta con marcas antiguas;
- un sanador podria visitar la zona cada pocos dias;
- el agua puede cambiar de color despues de eventos del crater.

## 5. Puerto del Navegante

Imagen: `assets/map_cells/casilla_05_puerto_del_navegante.png`

Arte de escenario: `assets/scenario_art/escenario_05_puerto_del_navegante.png`

Mapa tactico: `assets/tactical_maps/scenario_05_puerto_del_navegante/scenario_05_grid_14x14.png`

Rol jugable: cajas de loot, herramientas, sogas y rutas maritimas.

Lore: Este puerto fue el ultimo lugar donde alguien intento escapar navegando. Los muelles siguen llenos de sogas, cajas y mapas incompletos. En la taberna hundida hay marcas de rutas marinas, pero ninguna termina fuera de la isla sin pagar un precio.

Acciones posibles:

- abrir cajas de carga;
- buscar herramientas;
- pescar desde los muelles;
- reparar una barca pequena;
- bucear bajo estructuras;
- comerciar con lugarenos costeros.

Hallazgos posibles:

- soga;
- clavos;
- anzuelo;
- red;
- aceite;
- madera mojada;
- caja sellada;
- pieza de motor.

Amenazas:

- madera podrida;
- ahogamiento;
- criaturas marinas;
- emboscadas entre pasarelas;
- ruido de metal y tablas.

Ganchos:

- una caja militar aparece encadenada bajo el muelle;
- un bote podria servir como ruta de escape parcial;
- alguien usa el puerto para mover objetos robados.

## 6. Círculo de Monolitos

Imagen: `assets/map_cells/casilla_06_circulo_de_monolitos.png`

Arte de escenario: `assets/scenario_art/escenario_06_circulo_de_monolitos.png`

Mapa tactico: `assets/tactical_maps/scenario_06_circulo_de_monolitos/scenario_06_grid_14x14.png`

Rol jugable: misterio, ocultismo y eventos nocturnos.

Lore: Los monolitos son mas antiguos que cualquier construccion cercana. De dia parecen piedras ceremoniales; de noche forman una brujula que apunta hacia peligros, estrellas o muertos recientes. Nadie sabe si el circulo predice los juegos o si los provoca.

Acciones posibles:

- investigar simbolos;
- realizar o interrumpir rituales;
- escuchar rumores antiguos;
- buscar compartimentos bajo las piedras;
- descansar con riesgo psicologico;
- activar eventos de luna o tormenta.

Hallazgos posibles:

- piedra tallada;
- amuleto roto;
- hierbas secas;
- polvo mineral;
- fragmento de estrella;
- diario ocultista.

Amenazas:

- miedo;
- desorientacion;
- presencia de cultistas;
- criaturas atraidas por energia extrana;
- eventos nocturnos impredecibles.

Ganchos:

- los monolitos senalan una casilla distinta cada noche;
- puede abrir una ruta oculta si se resuelve una secuencia;
- una estrella podria no ser fisica, sino pactada.

## 7. Ruinas del Guardián

Imagen: `assets/map_cells/casilla_07_ruinas_del_guardian.png`

Arte de escenario: `assets/scenario_art/escenario_07_ruinas_del_guardian.png`

Mapa tactico: `assets/tactical_maps/scenario_07_ruinas_del_guardian/scenario_07_grid_14x14.png`

Rol jugable: acertijos, trampas y guardianes antiguos.

Lore: Las ruinas pertenecieron a una orden que custodiaba una puerta bajo la isla. El Guardian ya no es una persona, sino una presencia hecha de juramentos, trampas y memoria. Premia a quien entiende la prueba y castiga a quien solo viene a saquear.

Acciones posibles:

- resolver puzzles;
- desactivar trampas;
- explorar camaras;
- saquear cofres antiguos;
- negociar con un guardian neutral;
- ocultarse entre muros derruidos.

Hallazgos posibles:

- reliquia;
- llave antigua;
- placa metalica;
- gema opaca;
- cuerda vieja;
- mapa parcial;
- estrella protegida.

Amenazas:

- trampas de pinchos;
- derrumbes;
- guardian mecanico o espiritual;
- callejones sin salida;
- otros participantes buscando reliquias.

Ganchos:

- el guardian solo habla con quien no haya matado ese dia;
- una puerta exige sacrificar un objeto valioso;
- las ruinas recuerdan acciones anteriores de los personajes.

## 8. Pradera Valle del Viento

Imagen: `assets/map_cells/casilla_08_pradera_valle_del_viento.png`

Arte de escenario: `assets/scenario_art/escenario_08_pradera_valle_del_viento.png`

Mapa tactico: `assets/tactical_maps/scenario_08_pradera_valle_del_viento/scenario_08_grid_14x14.png`

Rol jugable: comida, viento, rutas abiertas y exposicion.

Lore: El valle parece abierto y amable, pero el viento funciona como mensajero. Lleva humo, pasos, gritos y olor mucho mas lejos de lo normal. Quien controla esta pradera puede moverse rapido; quien se descuida queda visto por media isla.

Acciones posibles:

- recolectar trigo o semillas;
- revisar el molino;
- secar ropa y materiales;
- vigilar caminos;
- viajar rapido;
- montar campamento temporal.

Hallazgos posibles:

- grano;
- tela;
- madera ligera;
- harina;
- cuerda;
- cuchillo de cocina;
- herramienta agricola.

Amenazas:

- poca cobertura;
- rastros faciles;
- ataques a distancia;
- incendios de campo;
- viento que delata ruidos.

Ganchos:

- el molino puede ocultar un mecanismo bajo el suelo;
- una figura se ve cruzando la pradera al atardecer;
- fuego en esta zona podria cambiar varias casillas cercanas.

## 9. Templo de las Hojas Carmesí

Imagen: `assets/map_cells/casilla_09_templo_de_las_hojas_carmesi.png`

Arte de escenario: `assets/scenario_art/escenario_09_templo_de_las_hojas_carmesi.png`

Mapa tactico: `assets/tactical_maps/scenario_09_templo_de_las_hojas_carmesi/scenario_09_grid_14x14.png`

Rol jugable: caza, hongos, sigilo y encuentros ambiguos.

Lore: El bosque otoñal oculta un templo de madera y piedra roja. Sus hojas nunca se pudren y caen como pequeñas señales de sangre seca. Los cazadores dicen que el templo acepta ofrendas de memoria: algo que amas, algo que temes o algo que hiciste.

Acciones posibles:

- cazar animales;
- recolectar hongos y bayas;
- seguir huellas;
- ocultar campamentos;
- preparar emboscadas;
- buscar al comerciante errante.

Hallazgos posibles:

- bayas;
- hongos comestibles o toxicos;
- cuero;
- arco simple;
- plumas;
- hierbas raras;
- caja enterrada.

Amenazas:

- confundir comida venenosa;
- cazadores;
- trampas ocultas;
- baja visibilidad;
- criaturas que imitan sonidos.

Ganchos:

- un NPC comerciante aparece solo si nadie lo persigue;
- un arbol tiene nombres tallados de participantes muertos;
- las hojas cubren un rastro fresco hacia la fortaleza.

## 10. Bastión del Acantilado

Imagen: `assets/map_cells/casilla_10_bastion_del_acantilado.png`

Arte de escenario: `assets/scenario_art/escenario_10_bastion_del_acantilado.png`

Mapa tactico: `assets/tactical_maps/scenario_10_bastion_del_acantilado/scenario_10_grid_14x14.png`

Rol jugable: defensa, armas, control territorial y facciones.

Lore: El bastion fue construido para resistir ataques desde el mar, pero termino vigilando a la propia isla. Sus balcones dominan la costa y sus almacenes aun guardan defensas improvisadas. Es refugio, fortaleza y trampa politica al mismo tiempo.

Acciones posibles:

- fortificar puertas;
- buscar armas o escudos;
- vigilar casillas costeras;
- negociar entrada con una faccion;
- preparar una defensa;
- saquear almacenes.

Hallazgos posibles:

- lanza;
- escudo de madera;
- clavos;
- placa metalica;
- cuerda;
- aceite;
- municion rara.

Amenazas:

- facciones hostiles;
- asedios;
- trampas en accesos;
- ser visto desde lejos;
- combates por control.

Ganchos:

- una faccion podria declarar la fortaleza como territorio propio;
- un sotano conecta con la costa;
- una bandera izada cambia la moral de ciertos NPCs.

## 11. Pantano de los Olvidados

Imagen: `assets/map_cells/casilla_11_pantano_de_los_olvidados.png`

Arte de escenario: `assets/scenario_art/escenario_11_pantano_de_los_olvidados.png`

Mapa tactico: `assets/tactical_maps/scenario_11_pantano_de_los_olvidados/scenario_11_grid_14x14.png`

Rol jugable: venenos, barro, niebla e ingredientes raros.

Lore: En el pantano se hunden cuerpos, objetos y versiones incomodas de la verdad. Las cabañas pertenecieron a gente que aprendio a vivir con la niebla y a vender remedios, venenos o silencio. Lo que se pierde aqui rara vez desaparece del todo.

Acciones posibles:

- recolectar plantas toxicas;
- esconder rastros en barro;
- pescar animales de pantano;
- buscar refugio en cabanas;
- fabricar veneno o antidoto;
- tender trampas en pasarelas.

Hallazgos posibles:

- agua turbia;
- hierbas venenosas;
- frasco;
- tubo quirurgico;
- red;
- piel de reptil;
- antidoto incompleto.

Amenazas:

- infecciones;
- insectos;
- barro profundo;
- criaturas anfibias;
- niebla que reduce percepcion;
- agua contaminada.

Ganchos:

- el cazador del pantano vende informacion por favores;
- una cabana contiene un mapa lleno de alfileres;
- los rastros organicos duran mas por la humedad.

## 12. Sector X

Imagen: `assets/map_cells/casilla_12_sector_x.png`

Arte de escenario: `assets/scenario_art/escenario_12_sector_x.png`

Mapa tactico: `assets/tactical_maps/scenario_12_sector_x/scenario_12_grid_14x14.png`

Rol jugable: energia extrana, cristales, mutaciones y alto riesgo.

Lore: El Sector X no aparece en los mapas antiguos. Fue cerrado por los organizadores tras un experimento fallido, aunque las luces verdes siguen funcionando bajo la roca. Los cristales alteran maquinas, criaturas y personas; por eso todos lo temen y todos lo necesitan.

Acciones posibles:

- extraer cristales;
- investigar energia rara;
- buscar una estrella custodiada;
- cargar dispositivos;
- estudiar criaturas mutadas;
- arriesgarse a una vision.

Hallazgos posibles:

- cristal verde;
- celda de energia;
- metal quemado;
- polvo toxico;
- fragmento tecnologico;
- estrella contaminada.

Amenazas:

- radiacion o corrupcion;
- mutantes;
- alucinaciones;
- heridas que no cierran bien;
- fallos de equipo.

Ganchos:

- un cristal puede abrir puertas de la torre;
- un NPC podria volverse mas fuerte pero menos estable;
- los drones evitan esta zona por una razon desconocida.

## 13. Torre Centinela

Imagen: `assets/map_cells/casilla_13_torre_centinela.png`

Arte de escenario: `assets/scenario_art/escenario_13_torre_centinela.png`

Mapa tactico: `assets/tactical_maps/scenario_13_torre_centinela/scenario_13_grid_14x14.png`

Rol jugable: objetivo final, compuertas, vigilancia y escape.

Lore: La Torre Centinela es el ojo central de Hell Games. Sus antenas escuchan, sus compuertas juzgan y sus drones patrullan como si defendieran una salida sagrada. Todos creen que la torre permite escapar, pero pocos preguntan hacia donde.

Acciones posibles:

- insertar estrellas;
- hackear terminales;
- reparar generadores;
- observar camaras;
- esquivar drones;
- negociar acceso final;
- intentar entrada ilegal.

Hallazgos posibles:

- tarjeta rota;
- cable electrico;
- bateria;
- registro del sistema;
- municion de dron;
- plano de compuertas.

Amenazas:

- drones;
- puertas cerradas;
- campo abierto;
- vigilancia constante;
- otros participantes llegando al final;
- defensas automaticas.

Ganchos:

- las 10 estrellas abren la ruta oficial;
- informatica y mecanica pueden abrir una ruta ilegal;
- la torre podria no ser una salida limpia.

## 14. Granja Sangrienta

Imagen: `assets/map_cells/casilla_14_granja_sangrienta.png`

Arte de escenario: `assets/scenario_art/escenario_14_granja_sangrienta.png`

Mapa tactico: `assets/tactical_maps/scenario_14_granja_sangrienta/scenario_14_grid_14x14.png`

Rol jugable: comida, animales, herramientas y refugio disputado.

Lore: La granja produce mas de lo que deberia, incluso cuando nadie la cuida. El suelo es oscuro, fertil y demasiado rojo despues de la lluvia. Los viejos cercos tienen marcas de uñas, y el granero conserva herramientas que sirven tanto para cosechar como para sobrevivir.

Acciones posibles:

- cosechar alimentos;
- cuidar o cazar animales;
- reparar cercas;
- cocinar;
- construir refugio;
- esconder suministros en el granero.

Hallazgos posibles:

- semillas;
- verduras;
- huevos;
- leche;
- pala;
- hacha pequena;
- cuerda;
- saco de grano.

Amenazas:

- saqueadores;
- incendios;
- animales nerviosos;
- enfermedades si se descuida la higiene;
- ataques durante la noche.

Ganchos:

- una familia de lugarenos podria reclamar la granja;
- un silo guarda algo que no es comida;
- controlar la granja puede cambiar la economia de la isla.

## 15. Templo del Sol

Imagen: `assets/map_cells/casilla_15_templo_del_sol.png`

Arte de escenario: `assets/scenario_art/escenario_15_templo_del_sol.png`

Mapa tactico: `assets/tactical_maps/scenario_15_templo_del_sol/scenario_15_grid_14x14.png`

Rol jugable: acertijos solares, calor, trampas y estrella.

Lore: El templo solo revela su verdadero camino cuando el sol cae en el angulo correcto. Sus columnas funcionan como relojes, cerraduras y advertencias. Quien entra de noche encuentra piedra muerta; quien entra al mediodia puede encontrar una bendicion o una sentencia.

Acciones posibles:

- resolver acertijos de luz;
- excavar entradas;
- buscar reliquias;
- evitar trampas de arena;
- estudiar inscripciones;
- refugiarse del viento.

Hallazgos posibles:

- amuleto solar;
- cristal amarillo;
- tela antigua;
- vasija;
- mapa grabado;
- estrella sellada.

Amenazas:

- calor;
- deshidratacion;
- trampas de presion;
- arena que oculta fosos;
- criaturas bajo la superficie.

Ganchos:

- solo se abre una camara durante una hora del dia;
- un acertijo exige reflejar luz desde otro objeto;
- el templo conoce una ruta hacia el bastion.

## 16. Costa del Naufragio Negro

Imagen: `assets/map_cells/casilla_16_costa_del_naufragio_negro.png`

Arte de escenario: `assets/scenario_art/escenario_16_costa_del_naufragio_negro.png`

Mapa tactico: `assets/tactical_maps/scenario_16_costa_del_naufragio_negro/scenario_16_grid_14x14.png`

Rol jugable: madera, restos de barco, botellas y supervivencia costera.

Lore: El barco negro encallo antes de que empezaran los juegos, o eso dice la version oficial. Su madera esta quemada por dentro y salada por fuera. Cada marea trae botellas, restos y mensajes escritos por manos que tal vez nunca estuvieron vivas.

Acciones posibles:

- desmontar madera del barco;
- buscar botellas con mensajes;
- pescar o recolectar mariscos;
- reparar una balsa;
- explorar la bodega;
- encender una senal en la playa.

Hallazgos posibles:

- tabla;
- soga gruesa;
- botella;
- ancla pequena;
- tela de vela;
- cuchillo oxidado;
- mapa humedo.

Amenazas:

- marea;
- cortes con metal oxidado;
- poca sombra;
- saqueadores costeros;
- criaturas nocturnas atraidas por restos.

Ganchos:

- un mensaje en botella menciona una ruta de escape falsa o real;
- la bodega solo se abre con marea baja;
- el naufragio contiene un nombre conectado a la torre.

## 17. Templo de la Luna

Imagen: `assets/map_cells/casilla_17_templo_de_la_luna.png`

Arte de escenario: `assets/scenario_art/escenario_17_templo_de_la_luna.png`

Mapa tactico: `assets/tactical_maps/scenario_17_templo_de_la_luna/scenario_17_grid_14x14.png`

Rol jugable: agua, comercio, medicina y acuerdos fragiles.

Lore: El oasis rodea un templo lunar semienterrado. Durante el dia parece un lugar de descanso y comercio; durante la noche, el agua refleja una luna que no siempre coincide con el cielo. Los pactos hechos aqui pesan mas cuando nadie los oye.

Acciones posibles:

- llenar agua;
- comerciar;
- recibir curacion;
- escuchar rumores;
- descansar;
- contratar guia;
- negociar favores.

Hallazgos posibles:

- agua limpia;
- vendas;
- hierbas medicinales;
- especias;
- frascos;
- comida seca;
- informacion.

Amenazas:

- estafas;
- venenos discretos;
- espias;
- peleas por agua;
- precio variable segun reputacion.

Ganchos:

- la medica del oasis cura a cambio de ingredientes raros;
- alguien vende una estrella que podria ser falsa;
- las fuentes bajan de nivel si se abusa de la zona.

## 18. Cañón Partido

Imagen: `assets/map_cells/casilla_18_canon_partido.png`

Arte de escenario: `assets/scenario_art/escenario_18_canon_partido.png`

Mapa tactico: `assets/tactical_maps/scenario_18_canon_partido/scenario_18_grid_14x14.png`

Rol jugable: persecuciones, puentes, emboscadas y rutas rapidas.

Lore: El cañon divide rutas, alianzas y persecuciones. Sus paredes rojizas guardan ecos con retraso, de modo que una amenaza puede sonar cerca cuando ya esta lejos. Los puentes son atajos valiosos y tambien sentencias si alguien corta la cuerda correcta.

Acciones posibles:

- cruzar puentes;
- escalar paredes;
- preparar emboscadas;
- cortar rutas;
- buscar cuevas laterales;
- huir de perseguidores.

Hallazgos posibles:

- cuerda;
- minerales rojizos;
- huesos secos;
- mochila caida;
- cuchillo arrojadizo;
- mapa de atajos.

Amenazas:

- caidas;
- puentes rotos;
- ataques desde altura;
- sed;
- desprendimientos;
- poca escapatoria si te rodean.

Ganchos:

- un puente puede ser sabotado y recordado por la simulacion;
- una cueva conecta con la mina;
- ecos revelan conversaciones a distancia.

## 19. Estación Militar

Imagen: `assets/map_cells/casilla_19_estacion_militar.png`

Arte de escenario: `assets/scenario_art/escenario_19_estacion_militar.png`

Mapa tactico: `assets/tactical_maps/scenario_19_estacion_militar/scenario_19_grid_14x14.png`

Rol jugable: generadores, vigilancia, armas y tecnologia.

Lore: La estacion fue abandonada con demasiada prisa. En sus terminales quedan ordenes incompletas, mapas de patrulla y grabaciones borradas a medias. Quien reactive sus generadores puede ver partes de la isla, pero tambien hacer que la isla lo vea de vuelta.

Acciones posibles:

- reparar generadores;
- buscar armas;
- revisar terminales;
- activar camaras;
- rastrear senales;
- abrir puertas bloqueadas;
- montar defensa.

Hallazgos posibles:

- bateria de auto;
- cable electrico;
- radio;
- municion;
- botiquin;
- tarjeta de acceso;
- casco militar.

Amenazas:

- torretas o drones;
- puertas trabadas;
- alarmas;
- facciones armadas;
- explosivos viejos.

Ganchos:

- puede revelar movimientos cerca de la torre;
- una terminal contiene videos del evento anterior;
- apagar una antena deja ciegos a los drones por poco tiempo.

## 20. Observatorio Militar

Imagen: `assets/map_cells/casilla_20_observatorio_militar.png`

Arte de escenario: `assets/scenario_art/escenario_20_observatorio_militar.png`

Mapa tactico: `assets/tactical_maps/scenario_20_observatorio_militar/scenario_20_grid_14x14.png`

Rol jugable: radar, predicciones, satelite y informacion estrategica.

Lore: El observatorio mezcla astronomia y vigilancia. Sus platos no solo miran al cielo: rastrean calor, radios, drones y caidas de objetos. Los militares intentaron predecir el comportamiento de la isla; lo inquietante es que a veces la isla les respondia.

Acciones posibles:

- reparar radar;
- observar estrellas caidas;
- leer datos del satelite;
- predecir clima;
- triangular senales;
- estudiar el crater verde.

Hallazgos posibles:

- lente optica;
- disco duro;
- panel solar roto;
- cable;
- cuaderno de astronomia;
- coordenadas de loot.

Amenazas:

- terreno rocoso;
- exposicion;
- radiacion residual;
- equipos inestables;
- visitantes que buscan informacion.

Ganchos:

- puede revelar donde caera una estrella al dia siguiente;
- una antena apunta al faro durante tormentas;
- el satelite podria contener instrucciones de escape.

## 21. Muelle Aguas Rojas

Imagen: `assets/map_cells/casilla_21_muelle_aguas_rojas.png`

Arte de escenario: `assets/scenario_art/escenario_21_muelle_aguas_rojas.png`

Mapa tactico: `assets/tactical_maps/scenario_21_muelle_aguas_rojas/scenario_21_grid_14x14.png`

Rol jugable: pesca, trueque, rumores y refugio social.

Lore: El agua bajo estos muelles se vuelve roja al atardecer, incluso sin sangre visible. Los habitantes aprendieron a no hacer preguntas y a comerciar antes de que oscurezca. En sus pasarelas se venden pescado, favores y mentiras muy bien envueltas.

Acciones posibles:

- pescar;
- comerciar;
- dormir bajo techo;
- contratar informacion;
- reparar redes;
- esconderse bajo muelles;
- negociar pactos.

Hallazgos posibles:

- pescado;
- red;
- soga;
- sal;
- madera tratada;
- anzuelo;
- rumor fiable o falso.

Amenazas:

- robos discretos;
- extorsion local;
- caidas al agua;
- incendios entre casas juntas;
- deudas con lugarenos.

Ganchos:

- los pescadores saben que algo grande se mueve cerca del puerto;
- una casa tiene un sotano seco bajo el nivel del mar;
- ayudar a la aldea puede crear una zona aliada.

## 22. Pueblo Nevado

Imagen: `assets/map_cells/casilla_22_pueblo_nevado.png`

Arte de escenario: `assets/scenario_art/escenario_22_pueblo_nevado.png`

Mapa tactico: `assets/tactical_maps/scenario_22_pueblo_nevado/scenario_22_grid_14x14.png`

Rol jugable: frio extremo, sotanos, ropa termica y ruta secreta.

Lore: El frio de este pueblo no pertenece al clima. Las casas conservan comida, huellas y secretos como si el tiempo se hubiera congelado con ellas. Bajo una cabaña hay un sotano que podria llevar a una ruta de escape o a una sala que nadie debio abrir.

Acciones posibles:

- buscar ropa termica;
- encender estufas;
- rastrear huellas en nieve;
- explorar sotanos;
- conservar comida;
- esconder objetos bajo hielo.

Hallazgos posibles:

- abrigo;
- lena seca;
- comida congelada;
- pala;
- cuerda;
- llave oxidada;
- documento viejo.

Amenazas:

- hipotermia;
- huellas demasiado visibles;
- tormentas de nieve;
- lobos o criaturas frias;
- refugios que se cierran desde fuera.

Ganchos:

- una ruta secreta podria empezar en la cabana del sotano;
- la nieve conserva rastros de alguien que murio dias antes;
- una radio vieja solo funciona durante ventiscas.

## 23. Jungla de Bambú Diabólico

Imagen: `assets/map_cells/casilla_23_jungla_de_bambu_diabolico.png`

Arte de escenario: `assets/scenario_art/escenario_23_jungla_de_bambu_diabolico.png`

Mapa tactico: `assets/tactical_maps/scenario_23_jungla_de_bambu_diabolico/scenario_23_grid_14x14.png`

Rol jugable: bambu, trampas, animales rapidos y camuflaje.

Lore: El bambu crece rapido, torcido y afilado. Cuando el viento lo mueve, la jungla parece reirse con miles de dientes verdes. Los puentes elevados no se construyeron por comodidad, sino porque algo entre las raices aprende los caminos de quienes pisan demasiado bajo.

Acciones posibles:

- cortar bambu;
- fabricar lanzas o trampas;
- recolectar plantas;
- esconder campamento;
- seguir animales;
- cruzar por pasarelas.

Hallazgos posibles:

- bambu;
- fibra vegetal;
- agua limpia parcial;
- frutas;
- lanza improvisada;
- cuerda primitiva;
- huevos o plumas.

Amenazas:

- serpientes;
- trampas naturales;
- humedad;
- heridas infectadas;
- sonidos que confunden ubicacion.

Ganchos:

- un guia carismatico conoce rutas entre bambu;
- las casas elevadas guardan objetos de participantes anteriores;
- cortar demasiado bambu cambia la cobertura de la zona.

## 24. Bastión Duna Seca

Imagen: `assets/map_cells/casilla_24_bastion_duna_seca.png`

Arte de escenario: `assets/scenario_art/escenario_24_bastion_duna_seca.png`

Mapa tactico: `assets/tactical_maps/scenario_24_bastion_duna_seca/scenario_24_grid_14x14.png`

Rol jugable: cofres enterrados, mercado roto, calor y rutas ocultas.

Lore: El bastion fue mercado, fortaleza y tumba de caravanas. La arena entra por las puertas selladas como si buscara algo. Bajo los toldos rotos hay cofres, mapas y deudas antiguas; cada trato aqui parece simple hasta que el desierto cobra intereses.

Acciones posibles:

- excavar cofres;
- buscar agua escondida;
- comerciar con oportunistas;
- explorar tuneles bajos;
- reparar toldos;
- estudiar mapas de caravanas.

Hallazgos posibles:

- moneda vieja;
- cantimplora;
- tela;
- especias;
- cuchillo curvo;
- joya;
- mapa hacia el templo.

Amenazas:

- deshidratacion;
- tormentas de arena;
- ladrones;
- trampas en cofres;
- espejismos.

Ganchos:

- un cofre exige dos llaves de casillas distintas;
- una ruta subterranea conecta con el templo de arena;
- alguien del oasis compra reliquias del bastion sin preguntar.

## 25. Volcán Ceniza Durmiente

Imagen: `assets/map_cells/casilla_25_volcan_ceniza_durmiente.png`

Arte de escenario: `assets/scenario_art/escenario_25_volcan_ceniza_durmiente.png`

Mapa tactico: `assets/tactical_maps/scenario_25_volcan_ceniza_durmiente/scenario_25_grid_14x14.png`

Rol jugable: maximo riesgo, lava, ceniza, golem y recompensa mayor.

Lore: El volcan parece dormir, pero su ceniza cae incluso en dias claros. Las grietas respiran naranja bajo la roca negra, y Gorath vigila las laderas como un juramento de lava. La recompensa aqui puede cambiar una partida, si el calor no cambia antes al participante.

Acciones posibles:

- buscar una estrella garantizada o casi garantizada;
- recolectar obsidiana;
- estudiar lava y ceniza;
- enfrentar o evitar al golem;
- fabricar armas con materiales raros;
- realizar senales visibles desde media isla.

Hallazgos posibles:

- obsidiana;
- ceniza;
- roca volcanica;
- mineral raro;
- cristal negro;
- arma quemada;
- estrella custodiada.

Amenazas:

- lava;
- humo toxico;
- calor extremo;
- derrumbes;
- golem de lava;
- equipo que se degrada rapido.

Ganchos:

- Gorath, el Golem de Lava, protege una estrella con reglas propias;
- una erupcion menor puede cerrar rutas cercanas;
- la ceniza puede ocultar rastros o contaminar agua.

## Siguiente conversion a datos

Cuando el bot empiece a usar estas zonas, cada casilla deberia pasar a una
estructura tipo:

```json
{
  "id": 1,
  "name": "Faro de la Vigilia Sagrada",
  "image": "assets/map_cells/casilla_01_faro_de_la_vigilia_sagrada.png",
  "danger": 3,
  "biome": "costa/torre",
  "actions": ["observar", "buscar_radio", "senalizar"],
  "common_loot": ["aceite", "cable", "bengala"],
  "rare_loot": ["lente_agrietada", "fragmento_estrella"],
  "threats": ["caida", "exposicion", "criatura_costera"]
}
```






