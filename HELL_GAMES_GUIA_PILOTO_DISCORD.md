# Hell Games - Guia de prueba piloto en Discord

Esta guia explica como seguir la demo viva de 4 casillas sin publicar los 3 dias
de golpe.

## Idea correcta del ritmo

La accion principal no deberia ser la bitacora completa. La bitacora es el
archivo historico. El ritmo de juego se sigue asi:

1. El admin inicia el piloto.
2. El bot publica el inicio en `hellgames-battleroyale`.
3. El admin avanza un turno cuando quiera que pase una escena.
4. Cada turno equivale a 6 horas de isla en la V0.
5. El mapa y la bitacora se actualizan hasta el turno actual.
6. Si quieres ver detalles internos, usas stalk/estado_actor.

## Comandos recomendados

### Preparacion

```txt
/hg admin diagnostico
/hg owner sync
/hg admin publicar_fichas
```

Usa `diagnostico` para confirmar permisos de canales. Usa `sync` despues de
reiniciar el bot o agregar comandos nuevos. Usa `publicar_fichas` para subir las
fichas base al canal database.

### Inicio de partida viva

```txt
/hg admin iniciar_piloto
```

Esto crea el estado vivo en:

```txt
data/runs/prototype_live_state.json
```

Tambien crea la bitacora parcial en:

```txt
data/runs/prototype_island_4_sandbox_log.md
```

Y renderiza el mapa actual en:

```txt
data/runs/maps/
```

### Avanzar la historia

```txt
/hg admin avanzar_turno
```

Cada uso publica una sola escena en el canal principal. No publica los 3 dias de
una vez.

### Seguir personajes

```txt
/hg admin stalk rex
/hg admin stalk renzo_manos_frias
/hg admin stalk silas_crow
/hg admin stalk sira
/hg admin stalk verek
```

`stalk` muestra:

- ubicacion exacta;
- HP, hambre, sed, energia y miedo;
- si esta oculto;
- inventario;
- intereses;
- recetas conocidas;
- recursos que busca.

Tambien puedes usar:

```txt
/hg admin estado_actor rex
```

Es una version textual mas compacta.

### Revisar mapa y bitacora

```txt
/hg mapa
/hg bitacora
/hg admin publicar_mapa
/hg admin publicar_bitacora
```

`/hg mapa` y `/hg bitacora` son privados para quien los usa. Los comandos
`publicar_*` mandan contenido a los canales configurados.

## Diferencia entre comandos antiguos y vivos

| Comando | Uso |
| --- | --- |
| `/hg admin iniciar_piloto` | recomendado para la prueba viva |
| `/hg admin avanzar_turno` | recomendado para narrar paso a paso |
| `/hg admin montar_demo` | atajo que inicia la demo viva y publica inicio/mapa/bitacora inicial |
| `/hg admin sandbox` | genera simulacion completa de 3 dias, util para pruebas tecnicas |
| `/hg admin publicar_accion` | publica escenas desde una bitacora ya generada; puede ser mucho contenido |

Para dirigir la partida, usa `iniciar_piloto` y `avanzar_turno`.

## Crafting e intereses

Los actores tienen un perfil de recetas en:

```txt
data/actor_crafting_profiles.json
```

Eso define:

- recetas conocidas;
- intereses;
- recursos que buscan;
- objetos por los que harian trueque;
- cosas que evitan;
- notas de comportamiento.

Ejemplos:

- Rex intenta convertir materiales simples en utilidad, como vendas o lanzas.
- Renzo prioriza radio, energia, cables, baterias y rutas tecnicas.
- Silas busca trampas, reliquias, venenos y ventajas sociales.
- Sira conoce rutas, rituales y consecuencias del faro.
- Verek comercia con piezas, rumores y recetas incompletas.

## Ritmo sugerido para una sesion

1. Iniciar piloto.
2. Mirar mapa.
3. Avanzar turno.
4. Stalkear 1 o 2 actores importantes.
5. Publicar mapa si el movimiento fue interesante.
6. Avanzar otro turno.
7. Revisar bitacora si algo se complica.
8. Parar cuando haya cliffhanger.

No hace falta terminar los 3 dias en una sola sesion. El piloto puede quedar en
el turno actual y continuar despues.
