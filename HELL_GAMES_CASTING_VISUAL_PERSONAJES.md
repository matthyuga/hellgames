# Hell Games - Casting visual de personajes

Analisis de la carpeta:

```txt
assets/characters/personajes hellgames
```

La carpeta contiene 52 PNG. La mayoria son pares de retrato/dialogo y cuerpo
completo, lo cual encaja muy bien con fichas de Discord, escenas narrativas,
comandos de stalk y publicaciones de database.

Hoja de contacto generada para revision local:

```txt
data/runs/character_contact_sheet.png
```

## Lectura general del set

Patrones visuales detectados:

- campeonas tribales o de arena: lagarto, aracnida, fuego, plumas, huesos;
- participantes humanos con silueta clara: rojo, Beid, Menks, Tyria, whip warrior;
- perfiles oscuros o sigilosos: DyLa, Blac, Fantz, Zaricha, Zymba;
- figuras misticas o guardianas: momia solar, elfica armada, guerrera fantasmal;
- criatura clara: humanoide infectado por parasito/hongo;
- falta todavia un set de criaturas basicas pequenas para faro/campamento/monolitos.

La fuerza visual esta mas cerca de un juego de supervivencia anime oscuro con
campeones muy reconocibles que de un battle royale anonimo. Conviene aprovechar
eso: cada personaje deberia tener rol, icono, habilidad, rareza social y estilo
de escena.

## Candidatos para personajes actuales del piloto

No todos los actores actuales tienen que conservar su nombre. Estas son las
mejores equivalencias visuales si queremos poner imagenes ya:

| Actor actual | Candidato visual | Motivo | Recomendacion |
| --- | --- | --- | --- |
| Reixa (beid-warrior)| `beid-warrior-*` o `warrior_*` | Silueta joven, reconocible, menos monstruosa que el resto. | Si Rex sigue siendo improvisador humano, usar `beid`. Si queremos hacerlo mas enigmatico, usar `warrior`. |
| menks | `menks_warrior_*` | Hombre sobrio, adulto, tecnico/duro, energia de superviviente practico. | Mejor candidato para Renzo. |
| Syras Crow (Dyla) | `dyla_*`, `zaricha_*` o `zymba_*` | Oscuros, sigilosos, mirada fria. | `dyla` para Silas humano elegante; `zymba` para Silas mas asesino; `zaricha` para version no humana. |
| Bleika  (blue-haired-woman)| `blue-haired-woman-*`, `elfica_*` o `w1_guerrera_*` | Guardiana, misteriosa, vinculada a saber antiguo. | `blue-haired-woman` si Sira es lugarenia discreta; `elfica` si es protectora armada del faro/ruinas. |
| Mareya (blac) | `blac_*`, `whip_warrior_*` o `dragy-warrior-*` | Comerciante peligroso, teatral, puede mentir. | `whip_warrior` si Verek es carismatico y cruel; `blac` si es criatura/lugareno oscuro. |

## Candidatos nuevos fuertes

Estos personajes merecen nombres propios en vez de quedar como archivos sueltos.

| Archivos | Nombre propuesto | Tipo | Personalidad | Habilidades |
| --- | --- | --- | --- | --- |
| `chamana_venenista_*` | Nara Sibil | lugarenia / participante invitada | juguetona, venenista, ritual, impredecible | venenos, medicina oscura, munecos malditos, trueque con hierbas |
| `guerrera_lagarto_*` | Karra Diente Verde | participante / criatura inteligente | orgullosa, cazadora, territorial | rastreo, resistencia, intimidar, caza |
| `guerrera_aracnida_*` | Aracne Veyra | jefe menor / criatura social | confiada, depredadora, calculadora | telaranas, emboscada, veneno, captura |
| `guerrera_fuego*` | Brasa Nox | participante peligrosa / jefe de evento | provocadora, explosiva, dominante | fuego, intimidacion, combate frontal, sabotaje |
| `huesa_*` | Huesa de Cal | lugarenia ritual / guardiana menor | seca, burlona, antigua | huesos, augurios, trampas ceremoniales |
| `pandora_feather_*` | Pandora Pluma Negra | participante / exploradora | desconfiada, orgullosa, espiritual | supervivencia, arco, rutas, lectura de rastros |
| `mirya_*` | Mirya del Sombrero Negro | lugarenia / bruja comerciante | amable de lejos, peligrosa de cerca | recetas, rumores, ocultismo, falsificar mapas |
| `tyria_*` | Tyria Corte Rojo | participante | disciplinada, competitiva, directa | espada, atletismo, liderazgo, duelo |
| `jas_warrior_*` | Jaska Garra Blanca | participante salvaje | feroz, leal si se gana respeto | caza, pieles, armas primitivas |
| `fantz_ghost_warrior_*` | Fantz, la Novia del Pozo | guardian / aparicion | silenciosa, vengativa, memoriosa | miedo, posesion leve, bloqueo de ruta |
| `guerrero_rojo_*` | Roan Escarlata | participante militarizado | serio, protector, rigido | combate, tactica, escolta, armas largas futuras |
| `whip_warrior_*` | Velka del Latigo | participante / cazarrecompensas | elegante, cruel, negociadora | desarmar, intimidar, perseguir, capturar |

## Criaturas y jefes del piloto

### Ya disponibles

| Archivo | Rol sugerido | Uso |
| --- | --- | --- |
| `creature/parasite_humanoid_*` | Infectado del hongo / raiz | Criatura rara de campamento o evento nocturno. Puede ser un antiguo participante contaminado. |
| `creature/jefe de evento especial/guerrera_momia_solar_*` | Momia solar | Jefe eventual o guardian mayor del Templo del Sol. Para el piloto puede aparecer solo como vision/amenaza futura. |

### Falta para el piloto

Para las 4 casillas hacen falta criaturas basicas con menos peso narrativo:

| Casilla | Criatura necesaria | Forma visual recomendada |
| --- | --- | --- |
| 1 Faro | Gaviotas de hueso | ave costera esqueletica, 2 variantes: vuelo y ataque |
| 2 Campamento | Larvas de raiz | gusanos/larvas oscuras con fibras vegetales, pequenas y numerosas |
| 6 Monolitos | Sombras de monolito | siluetas negras semihumanas, sin detalle facial completo |
| 7 Ruinas | Centinela menor | estatua rota, piedra con musgo, guardian lento |

### Guardian o jefe recomendado para prueba piloto

Para no gastar a la momia solar demasiado pronto, conviene crear un guardian
especifico del piloto:

**Nombre:** El Centinela de Basalto  
**Tipo:** guardian de ruinas  
**Casilla:** 7 Ruinas del Guardian  
**Visual:** estatua humanoide de piedra negra, grietas doradas, musgo, una mano
rota y un ojo encendido.  
**Personalidad:** lento, ceremonial, no odia a los vivos; odia el saqueo.  
**Habilidades:** bloquear ruta, resistir dano, aceptar ofrenda, perseguir al
portador de reliquia.  
**Trigger:** reliquia robada, dos trampas forzadas o monolito activado sin pago.  
**Debilidad:** devolver reliquia, entregar `piedra_tallada`, `amuleto_roto` o una
promesa registrada por Sira.

## Inventario y limite de loot

Conviene evitar inventarios infinitos. Recomiendo un sistema mixto por ranuras y
peso abstracto.

### Modelo simple para V0

Cada actor tiene:

| Campo | Valor sugerido |
| --- | --- |
| `slots_base` | 6 |
| `carry_weight_base` | 10 |
| `equipped_slots` | 2 manos + cuerpo + accesorio |
| `small_items_stack` | hasta 3 objetos pequenos iguales ocupan 1 slot |
| `bulky_items` | ocupan 2 o mas slots |
| `hidden_limit` | maximo 2 objetos ocultos sin mochila |

Modificadores:

- `mochila_reparada`: +4 slots;
- `bolsa_trueque`: +3 slots solo para objetos pequenos;
- `fuerza_alta`: +2 peso;
- `herido`: -2 peso;
- `criatura`: reglas especiales, no inventario normal;
- `guardian`: inventario narrativo, no saqueable completo.

### Tamanos de objeto

| Tamano | Ejemplos | Slots |
| --- | --- | --- |
| pequeno | aguja, bala, moneda, hierba, llave | 0.25 o stack |
| normal | botella, venda, cuchillo, libro | 1 |
| largo | lanza, rifle, tubo metalico | 2 |
| pesado | bateria auto, motor pequeno, placa grande | 3 |
| zona | barco, generador grande, monoriel | no va en inventario; queda como estado de casilla |

### Lo que se veria en Discord

Embed de stalk:

```txt
Stalk: Rex
Casilla 2 - Fogata (G7)
HP 96 | Hambre 51 | Sed 31 | Energia 72 | Miedo 48

Equipo:
Mano 1: cuchillo viejo
Mano 2: vacia
Cuerpo: mochila reparada

Inventario 5/10:
[icon] venda limpia x1
[icon] aguja x1
[icon] lata pequena x1
[icon] cuerda fina x1
[icon] mapa anotado x1

Intereses:
aliados, medicina_basica, herramientas_ligeras

Proxima intencion probable:
buscar agua o negociar con Verek
```

## Como hacer que parezca mas juego en Discord

### Embeds principales

| Embed | Funcion |
| --- | --- |
| ficha de personaje | retrato, rol, rasgos, habilidades, imagen grande |
| stalk privado | estado real, inventario, intencion probable |
| escena publica | narrativa del turno con miniatura del personaje protagonista |
| loot encontrado | iconos, rareza, quien lo vio, si queda oculto |
| receta desbloqueada | libro/manual, requisitos, quien la aprendio |
| mapa tactico | imagen de casilla con puntos y leyenda |
| evento de amenaza | criatura/jefe, trigger, zona afectada |

### Componentes visuales

- usar `embed.set_thumbnail` para retrato/dialogo;
- usar `embed.set_image` para fullbody, mapa o escena;
- colores por tipo: participante rojo, lugareno azul, criatura morado, guardian naranja, jefe dorado/negro;
- botones en mensajes persistentes: `Stalk`, `Inventario`, `Rumor`, `Mapa`, `Seguir`;
- iconos de items en inventario usando `icons_by_id` subidos a `hellgames-assets`;
- barra textual compacta para estados: `HP 82 | Sed 44 | Miedo 61`;
- rarezas con nombres: comun, poco comun, raro, epico, legendario, maldito.

### Canales ideales

| Canal | Contenido |
| --- | --- |
| `hellgames-battleroyale` | escenas vivas, eventos, decisiones visibles |
| `hellgames-map` | mapa tactico actualizado |
| `hellgames-bitacora` | archivo/resumen historico |
| `hellgames-database` | fichas, bestiario, catalogos, recetas descubiertas |
| `hellgames-assets` | imagenes subidas para usar por URL/ID |
| `hellgames-debug` | errores, logs, pruebas internas |

## Recomendacion de casting para la prueba piloto

Si queremos que el piloto se vea bonito pronto, usaria:

| Rol piloto | Personaje visual |
| --- | --- |
| Rex | `beid-warrior-*` |
| Renzo | `menks_warrior_*` |
| Silas | `dyla_*` |
| Sira | `blue-haired-woman-*` o `elfica_*` |
| Verek | `whip_warrior_*` |
| Criatura evento | `parasite_humanoid_*` |
| Jefe futuro | `guerrera_momia_solar_*` |
| Guardian nuevo a crear | Centinela de Basalto |
| Criaturas basicas a crear | gaviotas de hueso, larvas de raiz, sombras de monolito |

Esta seleccion deja al piloto con identidad visual sin quemar todos los
personajes potentes de la isla completa.

## Siguiente paso tecnico

Crear un archivo:

```txt
data/character_visual_cast.json
```

Con esta estructura:

```json
{
  "actor_id": "rex",
  "display_name": "Rex",
  "portrait": "assets/characters/personajes hellgames/beid-warrior-closeup.png",
  "fullbody": "assets/characters/personajes hellgames/beid-warrior-fullbody.png",
  "discord_portrait_url": null,
  "discord_fullbody_url": null
}
```

Luego el bot podria:

- publicar fichas con imagen;
- mostrar `stalk` con retrato;
- mostrar inventario con iconos;
- usar fullbody en database;
- usar retrato en escenas del canal principal.
