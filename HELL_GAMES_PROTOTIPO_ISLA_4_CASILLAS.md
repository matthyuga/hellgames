# Hell Games - Prototipo isla de 4 casillas

Piloto reducido para probar el comportamiento del bot con pocos actores y memoria clara.
Esta prueba usa el inicio del mapa: casilla 1 arriba izquierda, casilla 2 arriba derecha,
casilla 6 abajo izquierda y casilla 7 abajo derecha.

```txt
[1] Faro de la Vigilia Sagrada  --  [2] Campamento Raiz Maldita
 |                                      |
[6] Circulo de Monolitos        --  [7] Ruinas del Guardian
```

## Objetivo del piloto

Probar una partida corta con:

- 4 casillas activas;
- 2 NPC lugarenos;
- 3 participantes externos;
- 3 criaturas comunes;
- 2 guardianes;
- 1 jefe;
- simulacion de 3 a 5 dias;
- registro diario en bitacora;
- decisiones por personalidad, necesidad, ubicacion, miedo y memoria.

La meta no es decidir aun todo el sistema final. La meta es comprobar si el bot puede mover
personajes, generar incidentes, recordar consecuencias y producir una narracion entendible.

## Participantes elegidos

Estos tres salen de `HELL_GAMES_participantes.md`. Los elijo porque no pisan el mismo rol:
uno social y raro, uno tecnico calculador y uno oscuro oportunista.

| ID | Nombre | Rol de prueba | Por que sirve |
| --- | --- | --- | --- |
| `rex` | Rex | Participante creativo / improvisador | No es el mas fuerte. Obliga al sistema a resolver supervivencia con carisma, trueque y objetos raros. |
| `renzo_manos_frias` | Renzo "Manos Frias" | Participante tecnico / calculador | Puede interactuar con faro, radio, trampas y mecanismos. Bueno para probar decisiones logicas. |
| `silas_crow` | Silas Crow | Participante sigiloso / oportunista | Mete tension sin necesitar combate constante. Ideal para probar espionaje, saqueo, traicion y sospecha. |

Reserva posible para otra prueba: `yael_prisma`, si queremos una participante mas mistica o perceptiva
ligada a los monolitos.

## Casillas activas

### 1. Faro de la Vigilia Sagrada

Funcion en el piloto: observacion, senales y primer misterio tecnico.

Elementos:

- torre del faro;
- casa del farero;
- rocas costeras;
- vieja radio;
- lente agrietada;
- diario del farero.

Acciones principales:

- observar casillas 2 y 6;
- revisar radio;
- buscar bateria;
- encender luz;
- esconderse en la casa del farero;
- dejar una senal visible.

Riesgos:

- quedar expuesto desde lejos;
- caidas;
- ruido metalico;
- criaturas costeras de noche.

Evento especial:

- Si alguien repara la radio, escucha una transmision incompleta que menciona las ruinas.

### 2. Campamento Raiz Maldita

Funcion en el piloto: zona inicial, refugio temporal y punto de choque social.

Elementos:

- tiendas viejas;
- fogata central;
- cajas mojadas;
- raices negras bajo el suelo;
- lista de nombres tachados.

Acciones principales:

- buscar comida;
- dormir con riesgo bajo;
- encender fogata;
- recolectar cuerda y tela;
- revisar mochilas abandonadas;
- conversar o negociar.

Riesgos:

- humo visible;
- saqueos;
- raices que alteran el descanso;
- criaturas pequenas atraidas por comida.

Evento especial:

- Si alguien duerme aqui, puede despertar con un recuerdo falso o una marca de raiz en la piel.

### 6. Circulo de Monolitos

Funcion en el piloto: eventos nocturnos, pistas y presion psicologica.

Elementos:

- monolitos tallados;
- altar bajo;
- hierbas secas;
- polvo mineral;
- marcas que cambian con la luna.

Acciones principales:

- investigar simbolos;
- hacer o interrumpir ritual;
- buscar fragmento oculto;
- escuchar ecos;
- ocultarse entre piedras;
- rastrear energia hacia las ruinas.

Riesgos:

- miedo;
- desorientacion;
- atraer criaturas;
- activar guardianes.

Evento especial:

- De noche, los monolitos senalan una casilla: 1 si hay senal en el faro, 7 si alguien saquea las ruinas.

### 7. Ruinas del Guardian

Funcion en el piloto: peligro alto, prueba de trampas y mini-jefe.

Elementos:

- arco derrumbado;
- camara sellada;
- placas de presion;
- cofre antiguo;
- puerta con juramento grabado.

Acciones principales:

- explorar camaras;
- desactivar trampas;
- resolver acertijo;
- robar reliquia;
- negociar con guardian neutral;
- escapar de persecucion.

Riesgos:

- trampas;
- derrumbe;
- guardianes;
- callejones sin salida;
- castigo por saquear sin entender.

Evento especial:

- Si dos o mas personajes entran con intenciones incompatibles, las ruinas fuerzan una prueba: cooperar, sacrificar un objeto o separarse.

## Lugarenos

### Sira

ID: `sira`

Tipo: lugarena importante.

Ubicacion inicial: casilla 1, casa del farero.

Perfil:

- desconfiada;
- herida leve;
- conoce rutas entre faro y monolitos;
- sabe leer marcas antiguas;
- evita hablar de las ruinas.

Objetivos:

- proteger el diario del farero;
- evitar que los participantes activen la luz de noche;
- comprobar si las raices del campamento volvieron a crecer.

Uso en el piloto:

- NPC de informacion;
- posible aliada si recibe ayuda;
- posible enemiga si alguien roba el diario.

### Verek

ID: `verek`

Tipo: lugareno peligroso / saqueador paciente.

Ubicacion inicial: casilla 2, borde del campamento.

Perfil:

- comerciante de chatarra;
- oportunista;
- conoce escondites;
- no pelea si puede negociar;
- recuerda deudas y ofensas.

Objetivos:

- conseguir la lente del faro;
- vender informacion incompleta;
- descubrir quien entra a las ruinas.

Uso en el piloto:

- prueba de trueque;
- fuente de rumores falsos y verdaderos;
- detonante de conflictos con Silas o Renzo.

## Participantes

### Rex

ID: `rex`

Ubicacion inicial: casilla 2.

Personalidad:

- curioso;
- dramatico;
- evita matar si puede;
- improvisa con objetos;
- habla demasiado cuando tiene miedo.

Necesidades iniciales:

- comida: media;
- sed: baja;
- miedo: medio;
- energia: alta.

Habilidades:

- improvisar herramienta;
- distraer;
- evaluar telas, cuerdas y materiales;
- negociar con humor.

Objetivo personal:

- sobrevivir sin convertirse en asesino.

Posible arco:

- puede volverse cronista informal de lo ocurrido si encuentra el diario del farero.

### Renzo "Manos Frias"

ID: `renzo_manos_frias`

Ubicacion inicial: casilla 1.

Personalidad:

- calculador;
- paciente;
- poco expresivo;
- prefiere ventaja tecnica antes que combate;
- ayuda si eso mejora sus probabilidades.

Necesidades iniciales:

- comida: baja;
- sed: media;
- miedo: bajo;
- energia: media.

Habilidades:

- reparar radio;
- montar trampa simple;
- abrir caja;
- leer mecanismos.

Objetivo personal:

- encontrar una salida funcional antes de que el grupo se vuelva incontrolable.

Posible arco:

- puede obsesionarse con reparar el faro y atraer peligro sin querer.

### Silas Crow

ID: `silas_crow`

Ubicacion inicial: casilla 6.

Personalidad:

- observador;
- reservado;
- oportunista;
- miente bien;
- prefiere seguir rastros antes que anunciarse.

Necesidades iniciales:

- comida: baja;
- sed: baja;
- miedo: bajo;
- energia: alta.

Habilidades:

- sigilo;
- rastrear;
- saquear sin dejar muchas pistas;
- intimidar en privado.

Objetivo personal:

- conseguir una reliquia o ventaja antes de que los demas entiendan el mapa.

Posible arco:

- puede convertirse en sospechoso principal aunque no siempre sea culpable.

## Criaturas

### Gaviotas de hueso

ID: `gaviotas_hueso`

Zona: casilla 1.

Conducta:

- aparecen al atardecer;
- atacan comida visible;
- chillan si detectan sangre o carne;
- pueden revelar posiciones.

Uso:

- amenaza menor;
- alarma natural;
- molestia para quien se esconde en el faro.

### Larvas de raiz

ID: `larvas_raiz`

Zona: casilla 2.

Conducta:

- salen si hay comida tirada o fuego mal apagado;
- muerden poco, pero infectan;
- se esconden bajo tiendas y raices.

Uso:

- riesgo de campamento;
- castigo suave por descuidar higiene o descanso.

### Sombras de monolito

ID: `sombras_monolito`

Zona: casilla 6.

Conducta:

- solo de noche;
- imitan siluetas de personajes cercanos;
- causan miedo y confusion;
- no matan de inicio, pero pueden separar al grupo.

Uso:

- presion psicologica;
- prueba de percepcion y memoria.

## Guardianes

### Custodio del Faro

ID: `custodio_faro`

Zona: casilla 1.

Tipo: guardian espiritual menor.

Condicion de aparicion:

- aparece si alguien enciende la luz del faro despues de medianoche sin haber leido el diario.

Conducta:

- no ataca primero;
- bloquea la escalera;
- exige apagar la luz o nombrar a quien se quiere salvar;
- recuerda promesas.

Uso:

- guardian de reglas;
- prueba de dialogo condicional.

### Centinela de Piedra

ID: `centinela_piedra`

Zona: casilla 7.

Tipo: guardian antiguo fisico.

Condicion de aparicion:

- aparece si alguien roba una reliquia o falla una trampa dos veces.

Conducta:

- lento;
- resistente;
- persigue hasta el arco exterior;
- se detiene si recibe una ofrenda valida.

Uso:

- amenaza fuerte sin ser jefe final;
- fuerza huida, negociacion o sacrificio de objeto.

## Jefe

### El Guardián Juramentado

ID: `guardian_juramentado`

Zona: casilla 7.

Tipo: jefe del piloto.

Condicion de aparicion:

- aparece al final del dia 3 si alguien tiene la reliquia antigua;
- tambien puede aparecer antes si el cofre de la camara sellada se abre por fuerza.

Conducta:

- habla antes de combatir;
- juzga acciones registradas en la bitacora;
- castiga traicion, saqueo gratuito y mentiras ante las ruinas;
- permite escapar si se devuelve la reliquia o se entrega una memoria importante.

Uso:

- probar memoria del mundo;
- probar consecuencias acumuladas;
- cerrar el piloto con escena fuerte.

## Estado inicial recomendado

| Actor | Ubicacion | Estado | Inventario inicial | Intencion inicial |
| --- | --- | --- | --- | --- |
| Sira | 1 | herida leve, desconfiada | venda usada, diario oculto | vigilar faro |
| Verek | 2 | alerta, hambriento leve | cuchillo viejo, bolsa de trueque | vender rumor |
| Rex | 2 | nervioso, energia alta | aguja, retazo de tela, lata pequena | buscar aliados |
| Renzo | 1 | sereno, sed media | destornillador, cable corto | revisar radio |
| Silas Crow | 6 | oculto, energia alta | navaja fina, cuerda negra | observar monolitos |
| Gaviotas de hueso | 1 | pasivas de dia | ninguno | buscar comida |
| Larvas de raiz | 2 | dormidas | ninguno | despertar con humo/comida |
| Sombras de monolito | 6 | inactivas de dia | ninguno | aparecer de noche |
| Custodio del Faro | 1 | dormido | ninguno | proteger la luz |
| Centinela de Piedra | 7 | dormido | ninguno | proteger reliquia |
| Guardian Juramentado | 7 | sellado | reliquia vinculada | juzgar al final |

## Acciones reducidas para el piloto

Acciones generales:

- `observar`;
- `moverse`;
- `descansar`;
- `ocultarse`;
- `vigilar`;
- `rastrear`;
- `investigar_ruido`;
- `buscar_comida`;
- `buscar_agua`;
- `buscar_materiales`;
- `hablar`;
- `negociar`;
- `esperar`.

Acciones especiales por casilla:

- casilla 1: `reparar_radio`, `encender_faro`, `leer_diario`;
- casilla 2: `hacer_fogata`, `revisar_tiendas`, `fabricar_basico`;
- casilla 6: `leer_monolitos`, `hacer_ritual`, `seguir_ecos`;
- casilla 7: `desactivar_trampa`, `resolver_acertijo`, `abrir_cofre`, `devolver_reliquia`.

## Reglas simples de movimiento

Rutas permitidas:

- 1 <-> 2;
- 1 <-> 6;
- 2 <-> 7;
- 6 <-> 7.

Ruta opcional:

- 2 <-> 6 solo si se habilita movimiento diagonal. Para la primera prueba conviene dejarla cerrada.

Tiempo:

- moverse entre casillas consume 1 bloque de tiempo;
- cada dia tiene 4 bloques: manana, tarde, noche, madrugada;
- de madrugada suben el miedo y los riesgos de criatura.

## Memorias que el bot debe guardar

Memorias minimas por actor:

- ultima ubicacion;
- ultimo actor visto;
- ultima amenaza vista;
- deuda u ofensa reciente;
- objeto importante conocido;
- si mintio o fue descubierto;
- si fue ayudado o atacado.

Memorias globales:

- quien encendio el faro;
- quien leyo el diario;
- quien entro a las ruinas;
- quien robo una reliquia;
- quien negocio con Verek;
- quien fue visto por Silas;
- quien desperto criaturas;
- si el jefe fue liberado.

## Guion sugerido de prueba

### Dia 1

- Renzo revisa la radio del faro.
- Sira observa a Renzo y decide si hablar o esconder el diario.
- Rex intenta negociar con Verek en el campamento.
- Silas estudia los monolitos y encuentra una marca apuntando a las ruinas.
- Por la noche, una sombra imita a Rex cerca del campamento.

### Dia 2

- Alguien debe elegir entre reparar la radio, buscar comida o explorar ruinas.
- Verek vende un rumor: "el faro llama al guardian si la luz se enciende tarde".
- Silas puede seguir a quien viaje hacia las ruinas.
- Las larvas aparecen si hubo fogata mal apagada.
- El Centinela de Piedra despierta si se fuerza una puerta.

### Dia 3

- La reliquia queda disponible en las ruinas.
- El Custodio del Faro puede aparecer si Renzo enciende la luz de noche.
- El Guardian Juramentado despierta si alguien roba la reliquia.
- El cierre del piloto debe resumir: alianzas, heridas, mentiras, objetos y secretos revelados.

## Criterios para saber si el piloto funciona

Funciona si al final se puede responder:

- donde estuvo cada personaje cada dia;
- que queria hacer cada uno;
- que decisiones fueron causadas por personalidad y no solo azar;
- que eventos cambiaron el estado del mapa;
- que memorias afectaron escenas posteriores;
- que partes fueron aburridas o demasiado confusas;
- que datos faltaron para que el bot narre mejor.

## Siguiente paso tecnico

Convertir este prototipo en datos cargables:

- `data/prototype_island_4.json` para mapa, actores y estados iniciales;
- una tabla SQLite posterior para guardar ticks y bitacoras;
- un comando admin tipo `/hg simular_dia piloto_4`;
- un comando publico tipo `/hg bitacora piloto_4`.
