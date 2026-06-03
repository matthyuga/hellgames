# Hell Games - Progresion, XP y Hellcoins

Sistema para usuarios humanos del servidor. No representa la experiencia de los
personajes dentro de la isla, sino el progreso del espectador/investigador.

## Idea base

Los usuarios suben de nivel usando comandos, siguiendo personajes, leyendo
bitacoras, desbloqueando rumores, votando y acertando predicciones.

Los niveles desbloquean mas formas de mirar la isla.

Las Hellcoins funcionan como moneda del evento:

- apostar por sucesos;
- pagar observaciones especiales;
- profundizar seguimiento;
- participar en votaciones premium;
- comprar pequenas ventajas de informacion;
- entrar en rankings.

## XP de usuario

La XP mide participacion y curiosidad. Debe tener cooldowns para evitar farmear
comandos repetidos.

| Accion | XP sugerida | Nota |
| --- | --- | --- |
| consultar bitacora diaria | 5 | una vez por bloque o dia |
| mirar mapa | 3 | con cooldown |
| mirar personaje | 4 | con cooldown por personaje |
| seguir personaje | 10 | al pagar puntos de seguimiento |
| observar personaje | 6 | si el comando devuelve informacion nueva |
| participar en votacion | 8 | solo si votacion activa |
| consultar guia desbloqueada | 4 | con cooldown |
| descubrir rumor nuevo | 12 | solo primera vez |
| acertar teoria o prediccion | 25 | validado por evento real |
| ganar apuesta | 10 | bonus pequeno, separado de Hellcoins |

## Niveles

| Nivel | Nombre | XP requerida | Rol |
| --- | --- | --- | --- |
| 0 | Espectador | 0 | mira lo publico |
| 1 | Curioso | 50 | consulta detalles simples |
| 2 | Seguidor | 150 | sigue personajes |
| 3 | Investigador | 350 | rastros, casillas, eventos |
| 4 | Espia | 700 | relaciones, historial, espiar |
| 5 | Analista | 1200 | comparar, teorias, patrones |

## Hellcoins

Las Hellcoins son moneda interna del evento. No deben representar dinero real.
Sirven para crear juego social y tension sin controlar directamente a los NPCs.

Fuentes:

- bono diario por reclamar actividad;
- participar en votaciones;
- acertar apuestas;
- descubrir rumores;
- eventos especiales;
- premios manuales de admin.

Gastos:

- apostar;
- seguir o profundizar personajes;
- espiar una escena;
- comprar una pista publica;
- votar con peso extra si se permite;
- desbloquear cosmeticos o titulos.

Valores iniciales sugeridos:

| Accion | Hellcoins |
| --- | --- |
| bono diario | +25 |
| participar en votacion | +5 |
| descubrir rumor nuevo | +15 |
| seguir personaje | -20 |
| profundizar personaje | -40 |
| espiar escena puntual | -15 |
| comprar pista menor | -30 |

## Apuestas

Las apuestas permiten que los usuarios predigan sucesos del sandbox.

Ejemplos:

- quien sobrevive al dia 3;
- si alguien entra a las ruinas;
- si el jefe despierta;
- si Rex negocia con Verek;
- si Silas roba una reliquia;
- si Renzo repara la radio;
- si Sira ayuda a un participante;
- si aparece una criatura de noche.

Formato conceptual:

```txt
/hg apuesta crear evento=guardian_juramentado_despierto opciones=si,no cierre=dia_3_tarde
/hg apostar evento=guardian_juramentado_despierto opcion=si cantidad=50
```

Para la V0 conviene que las apuestas sean creadas por admin, no libres por usuarios.
Asi evitamos spam, ambiguedad y apuestas imposibles de resolver.

## Resolucion de apuestas

Cada apuesta debe apuntar a una memoria o resultado verificable del mundo.

Ejemplo:

```json
{
  "id": "apuesta_jefe_despierta",
  "question": "Despertara el Guardian Juramentado antes del final?",
  "options": ["si", "no"],
  "resolver": {
    "type": "memory_equals",
    "key": "guardian_juramentado_despierto",
    "value": true
  }
}
```

Si el valor ocurre:

- ganan quienes apostaron por `si`;
- pierden quienes apostaron por `no`.

Si no ocurre antes del cierre:

- gana `no`.

## Pagos

Para empezar, usaria pagos simples tipo multiplicador fijo.

| Tipo | Pago sugerido |
| --- | --- |
| opcion comun | x1.5 |
| opcion equilibrada | x2 |
| opcion dificil | x3 |
| opcion muy rara | x4 |

Ejemplo:

```txt
Kevin apuesta 50 Hellcoins a que Silas roba una reliquia.
Multiplicador: x3
Si ocurre: recibe 150 Hellcoins.
Ganancia neta: +100.
Si no ocurre: pierde 50.
```

Mas adelante puede haber cuotas dinamicas segun cuanta gente apuesta por cada
opcion, pero no hace falta para la primera version.

## Riesgos y reglas sanas

Para que el sistema no se rompa:

- no usar dinero real;
- limitar apuestas por usuario y evento;
- poner cierre antes de que el resultado sea obvio;
- no permitir apuestas creadas libremente al inicio;
- registrar todas las transacciones;
- permitir reembolso admin si una apuesta queda invalida;
- separar XP de Hellcoins para que apostar no sea la unica forma de progresar.

## Comandos sugeridos

Publicos:

- `/hg monedas`: muestra Hellcoins actuales;
- `/hg reclamar`: reclama bono diario;
- `/hg apuestas`: lista apuestas abiertas;
- `/hg apostar <apuesta> <opcion> <cantidad>`: apuesta Hellcoins;
- `/hg mis_apuestas`: apuestas activas del usuario;
- `/hg mercado`: muestra gastos disponibles;
- `/hg comprar <opcion>`: compra pista, seguimiento o utilidad.

Admin:

- `/hg admin apuesta_crear`: crea apuesta;
- `/hg admin apuesta_cerrar`: cierra nuevas entradas;
- `/hg admin apuesta_resolver`: resuelve y paga;
- `/hg admin monedas`: ajusta Hellcoins de un usuario;
- `/hg admin transacciones`: revisa movimientos.

## Demo recomendada

Para el piloto de 4 casillas:

1. Todos empiezan con 100 Hellcoins.
2. Se abren 3 apuestas simples:
   - sobrevive Rex al dia 3;
   - alguien roba una reliquia;
   - despierta el Guardian Juramentado.
3. Cada usuario puede apostar maximo 50 por apuesta.
4. El admin corre `/hg admin sandbox`.
5. El bot resuelve apuestas usando las memorias del sandbox.
