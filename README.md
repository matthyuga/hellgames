# Hellgames

Proyecto de bot de Discord para un battle royale narrativo en una isla viva.

La idea central es simular participantes, lugarenos, criaturas, guardianes y jefes
que se mueven por casillas, recuerdan sucesos y generan una bitacora para Discord.

## Estado actual

El repositorio arranca como base de diseno y prototipo:

- documentos canonicos de casillas, IA, participantes y sistemas;
- datos iniciales en `data/`;
- scripts de apoyo en `scripts/`;
- prototipo reducido de 4 casillas para probar simulacion.

## Prototipo principal

Ver:

- `HELL_GAMES_PROTOTIPO_ISLA_4_CASILLAS.md`
- `data/prototype_island_4.json`

Ese piloto usa:

- casilla 1: Faro de la Vigilia Sagrada;
- casilla 2: Campamento Raiz Maldita;
- casilla 6: Circulo de Monolitos;
- casilla 7: Ruinas del Guardian.

Incluye 2 lugarenos, 3 participantes, 3 criaturas, 2 guardianes y 1 jefe.

## Assets

Los assets visuales pesados no se suben todos al repo. Este proyecto tiene una
carpeta local `assets/` muy grande, especialmente `assets/characters/`.

La estrategia recomendada es:

- versionar documentos, manifiestos y datos livianos;
- guardar imagenes pesadas localmente, en Discord/CDN o en releases separadas;
- usar IDs, rutas o URLs para que el bot pueda referenciar las imagenes sin cargar
  todo dentro de Discloud.
