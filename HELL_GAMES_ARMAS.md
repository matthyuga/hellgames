# Hell Games - Catalogo de armas

Catalogo inicial de armas, municiones, trampas y herramientas usadas como armas.
Este documento queda separado de `HELL_GAMES_OBJETOS_RECURSOS.md` para que el bot
pueda distinguir entre loot de supervivencia, herramientas de progreso y objetos
de combate.

Fuente base:

- `doc_armas1.md`;
- armas piloto de `data/prototype_runtime_4.json`;
- necesidades del sandbox de 4 casillas.

## Criterio

Cada arma deberia tener:

- `id`;
- nombre visible;
- tipo;
- rareza;
- dano;
- ruido;
- amenaza;
- durabilidad;
- requisitos o habilidad relacionada;
- municion, si aplica;
- efectos narrativos.

Ejemplo:

```json
{
  "id": "cuchillo_viejo",
  "name": "Cuchillo viejo",
  "type": "melee_simple",
  "rarity": "comun",
  "damage": "medio",
  "noise": "bajo",
  "threat": "media",
  "durability": "media",
  "skills": ["sigilo", "supervivencia"],
  "ammo": null,
  "effects": ["sangrado_leve", "intimidacion"]
}
```

## Variables principales

| Variable | Uso |
| --- | --- |
| `damage` | Cuanto lastima si impacta. |
| `noise` | Cuanto atrae criaturas, guardianes o curiosos. |
| `threat` | Cuanto sirve para intimidar, negociar o forzar una rendicion. |
| `durability` | Cuanto aguanta antes de romperse o atascarse. |
| `control` | Que tan facil es usarla sin entrenamiento. |
| `ammo` | Municion o carga necesaria. |
| `risk` | Riesgo de herirse, fallar, atraer enemigos o causar incendio. |

## 1. Armas cuerpo a cuerpo simples

Armas comunes, faciles de entender y muy utiles al inicio. Algunas tambien
existen como herramientas o recursos.

| ID | Nombre | Rareza | Dano | Ruido | Usos |
| --- | --- | --- | --- | --- | --- |
| `cuchillo_viejo` | Cuchillo viejo | comun | medio | bajo | defensa, sigilo, intimidacion |
| `cuchillo_oxidado` | Cuchillo oxidado | comun | medio | bajo | ataque cercano, riesgo de infeccion |
| `navaja_fina` | Navaja fina | comun | bajo | bajo | corte rapido, sigilo, escape de ataduras |
| `navaja_bolsillo` | Navaja de bolsillo | comun | bajo | bajo | herramienta, amenaza discreta |
| `palo_madera` | Palo de madera | comun | bajo | medio | defensa basica, empujar |
| `garrote_improvisado` | Garrote improvisado | comun | medio | medio | aturdir, intimidar |
| `tubo_metalico` | Tubo metalico | comun | medio | medio | golpear, bloquear, romper vidrio |
| `martillo` | Martillo | comun | medio | medio | construir o combatir |
| `pala` | Pala | comun | medio | medio | excavar, empujar, defensa |
| `serrucho` | Serrucho | comun | medio | medio | herramienta peligrosa, terror psicologico |
| `llave_inglesa` | Llave inglesa | comun | medio | medio | reparar, golpear |
| `botella_rota` | Botella rota | comun | bajo | bajo | arma desesperada, sangrado leve |
| `piedra_filosa` | Piedra filosa | comun | bajo | bajo | corte primitivo, punta de craft |

## 2. Armas cuerpo a cuerpo avanzadas

Mas raras y decisivas. Cambian la conducta de los NPC porque aumentan la
confianza, la amenaza publica o el miedo ajeno.

| ID | Nombre | Rareza | Dano | Ruido | Usos |
| --- | --- | --- | --- | --- | --- |
| `machete` | Machete | poco comun | alto | medio | abrir vegetacion, combate cercano |
| `hacha_pequena` | Hacha pequena | poco comun | alto | medio | cortar madera, defensa fuerte |
| `cuchillo_caza` | Cuchillo de caza | poco comun | alto | bajo | caza, sigilo, remate |
| `palanca_hierro` | Palanca de hierro | poco comun | medio | medio | abrir puertas, golpear |
| `pico_mineria` | Pico de mineria | poco comun | alto | medio | mineria, perforar defensa |
| `baston_reforzado` | Baston reforzado | poco comun | medio | bajo | control de distancia |
| `cadena_gancho` | Cadena con gancho | raro | alto | alto | atraer, desarmar, atemorizar |
| `hacha_bombero` | Hacha de bombero | raro | alto | medio | romper puertas, combate brutal |
| `katana_vieja` | Katana vieja | raro | alto | bajo | amenaza alta, requiere control |
| `espada_ceremonial` | Espada ceremonial | raro | alto | bajo | reliquia, duelo, ritual |
| `lanza_militar` | Lanza militar | raro | alto | bajo | distancia, guardia, formacion |
| `maza_pesada` | Maza pesada | raro | alto | medio | romper escudos, cansancio alto |
| `guadana_improvisada` | Guadana improvisada | raro | alto | medio | zona amplia, riesgo de fallo |

## 3. Armas a distancia primitivas

Buenas para cazadores, personajes sigilosos y NPCs tacticos. Suelen depender de
municion fabricable.

| ID | Nombre | Rareza | Dano | Ruido | Municion |
| --- | --- | --- | --- | --- | --- |
| `honda` | Honda | comun | bajo | bajo | `piedra_comun` |
| `tirachinas` | Tirachinas | comun | bajo | bajo | `piedra_pequena` |
| `jabalina` | Jabalina | comun | medio | bajo | ninguna |
| `lanza_arrojadiza` | Lanza arrojadiza | poco comun | medio | bajo | ninguna |
| `cuchillos_arrojadizos` | Cuchillos arrojadizos | poco comun | medio | bajo | cuchillos |
| `dardos` | Dardos | poco comun | bajo | bajo | `dardo` |
| `arco_simple` | Arco simple | poco comun | medio | bajo | `flecha` |
| `arco_caza` | Arco de caza | raro | alto | bajo | `flecha` |
| `ballesta_ligera` | Ballesta ligera | raro | alto | bajo | `virote_ballesta` |
| `ballesta_silenciosa` | Ballesta silenciosa | raro | alto | muy bajo | `virote_ballesta` |

## 4. Armas de fuego

Deben ser raras y tener municion limitada. Un arma descargada igual puede servir
para mentir, intimidar, negociar o provocar una traicion.

| ID | Nombre | Rareza | Dano | Ruido | Municion |
| --- | --- | --- | --- | --- | --- |
| `pistola_sin_balas` | Pistola sin balas | poco comun | nulo | bajo | ninguna |
| `pistola_sin_cargador` | Pistola sin cargador | poco comun | nulo | bajo | `cargador_pistola` |
| `pistola_bengalas` | Pistola de bengalas | poco comun | bajo | alto | `bengala` |
| `revolver_viejo` | Revolver viejo | raro | alto | alto | `bala_revolver` |
| `pistola_9mm` | Pistola 9mm | raro | alto | alto | `bala_pistola` |
| `escopeta_recortada` | Escopeta recortada | raro | alto | muy alto | `cartucho_escopeta` |
| `escopeta_caza` | Escopeta de caza | raro | alto | muy alto | `cartucho_escopeta` |
| `rifle_cerrojo` | Rifle de cerrojo | raro | alto | alto | `municion_rifle` |
| `rifle_caza` | Rifle de caza | raro | alto | alto | `municion_rifle` |
| `subfusil_danado` | Subfusil danado | epica | alto | muy alto | `cargador_subfusil` |
| `fusil_militar` | Fusil militar | epica | alto | muy alto | `cargador_fusil` |
| `rifle_francotirador` | Rifle francotirador | epica | letal | alto | `municion_rifle` |
| `arma_polvo_casera` | Arma casera de polvora | rara | alto | muy alto | `polvora`, `plomo` |

## 5. Municiones y cargas

La municion va separada para forzar exploracion, trueque, robo y bluff.

| ID | Nombre | Rareza | Uso |
| --- | --- | --- | --- |
| `bala_pequena` | Bala pequena | poco comun | municion menor o craft |
| `bala_pistola` | Bala de pistola | poco comun | pistolas |
| `bala_revolver` | Bala de revolver | poco comun | revolver |
| `cartucho_escopeta` | Cartucho de escopeta | raro | escopetas |
| `municion_rifle` | Municion de rifle | raro | rifles |
| `flecha` | Flecha | comun | arcos |
| `flecha_reforzada` | Flecha reforzada | poco comun | arcos, mas dano |
| `virote_ballesta` | Virote de ballesta | poco comun | ballestas |
| `bengala` | Bengala | poco comun | senal, fuego, pistola de bengalas |
| `polvora` | Polvora | raro | armas caseras, explosivos |
| `casquillo_vacio` | Casquillo vacio | comun | craft de municion |
| `plomo` | Plomo | poco comun | craft de municion |
| `cargador_vacio` | Cargador vacio | poco comun | recargar si hay balas |
| `cargador_pistola` | Cargador de pistola | raro | pistola 9mm |
| `cargador_subfusil` | Cargador de subfusil | epica | subfusil |
| `cargador_fusil` | Cargador de fusil | epica | fusil militar |

## 6. Armas improvisadas

Nacen de recursos. Ideales para personajes creativos o desesperados.

| ID | Nombre | Rareza | Dano | Ruido | Recursos base |
| --- | --- | --- | --- | --- | --- |
| `lanza_casera` | Lanza casera | comun | medio | bajo | `rama_seca`, `piedra_filosa`, `cuerda_fina` |
| `lanza_madera` | Lanza de madera | comun | medio | bajo | `rama_seca`, `cuchillo_viejo` |
| `palo_clavos` | Palo con clavos | poco comun | medio | medio | `palo_madera`, `clavos` |
| `cuchillo_hueso` | Cuchillo de hueso | poco comun | medio | bajo | `huesos`, `piedra_filosa` |
| `hacha_piedra` | Hacha de piedra | poco comun | medio | medio | `piedra_filosa`, `rama_seca`, `cuerda_fina` |
| `antorcha` | Antorcha | comun | bajo | medio | `rama_seca`, `tela`, `aceite` |
| `soga_piedra` | Soga con piedra | comun | bajo | bajo | `soga`, `piedra_comun` |
| `red_improvisada` | Red improvisada | poco comun | bajo | bajo | `red_pesca`, `soga` |
| `escudo_madera` | Escudo de madera | poco comun | bajo | medio | `tabla`, `correa`, `clavos` |
| `molotov` | Coctel molotov | raro | alto | alto | `frasco_vidrio`, `tela`, `gasolina` |
| `bomba_humo_casera` | Bomba de humo casera | poco comun | nulo | medio | `lata_pequena`, `polvo_irritante`, `tela` |
| `bomba_incendiaria_casera` | Bomba incendiaria casera | raro | alto | alto | `aceite`, `frasco_vidrio`, `tela` |

## 7. Trampas

Las trampas mueven el juego sin exigir combate directo. Sirven para cazar,
proteger una zona, bloquear rutas, crear miedo o atraer criaturas.

| ID | Nombre | Rareza | Dano | Ruido | Efecto |
| --- | --- | --- | --- | --- | --- |
| `trampa_lazo` | Trampa de lazo | comun | bajo | bajo | inmoviliza |
| `alarma_latas` | Alarma con latas | comun | nulo | alto | revela movimiento |
| `cuerda_tensada` | Cuerda tensada | comun | bajo | medio | tropiezo |
| `cable_trampa` | Cable trampa | poco comun | bajo | medio | activa otra trampa |
| `pinchos_ocultos` | Pinchos ocultos | poco comun | medio | bajo | herida, sangrado |
| `foso_cubierto` | Foso cubierto | poco comun | medio | medio | caida, encierro |
| `red_colgante` | Red colgante | poco comun | bajo | medio | captura |
| `trampa_pinchos_portatil` | Trampa de pinchos portatil | poco comun | medio | bajo | bloqueo de paso |
| `trampa_oso` | Trampa de oso | raro | alto | medio | inmoviliza, dano alto |
| `trampa_venenosa` | Trampa venenosa | raro | medio | bajo | veneno |
| `trampa_incendiaria` | Trampa incendiaria | raro | alto | alto | fuego, panico |
| `trampa_explosiva_casera` | Trampa explosiva casera | epica | letal | muy alto | explosion |
| `trampa_ruido` | Trampa de ruido | comun | nulo | alto | atrae criaturas o guardianes |

## 8. Armas quimicas o ambientales

Fuertes para personajes astutos, medicos, chamanes, cientificos o tramperos.
Deben tener limite de uso y consecuencias.

| ID | Nombre | Rareza | Dano | Ruido | Efecto |
| --- | --- | --- | --- | --- | --- |
| `veneno_casero` | Veneno casero | poco comun | medio | bajo | veneno en comida/agua |
| `dardo_venenoso` | Dardo venenoso | raro | medio | bajo | veneno a distancia |
| `polvo_irritante_arma` | Polvo irritante | poco comun | bajo | bajo | ceguera breve, distraccion |
| `acido_debil` | Acido debil | raro | medio | bajo | abrir cerraduras, sabotaje |
| `bomba_humo` | Bomba de humo | poco comun | nulo | medio | ocultamiento |
| `bomba_pimienta` | Bomba de pimienta | raro | bajo | medio | ceguera, panico |
| `gas_lacrimogeno` | Gas lacrimogeno | raro | bajo | alto | dispersa grupos |
| `esporas_toxicas` | Esporas toxicas | raro | medio | bajo | enfermedad, miedo |
| `frasco_combustible` | Frasco de combustible | poco comun | medio | alto | fuego si se enciende |
| `carne_contaminada_cebo` | Carne contaminada como cebo | comun | bajo | bajo | atrae criaturas, enferma |

## 9. Armas especiales del evento

Piezas unicas o casi unicas. Conviene ubicarlas en guardianes, jefes, secretos o
eventos de alto riesgo.

| ID | Nombre | Rareza | Dano | Ruido | Lugar sugerido |
| --- | --- | --- | --- | --- | --- |
| `hacha_farero` | Hacha del farero | legendaria | alto | medio | Faro de la Vigilia Sagrada |
| `rifle_vigilante` | Rifle del vigilante | legendaria | letal | alto | Torre Centinela / Faro |
| `lanza_estrella` | Lanza de estrella | legendaria | letal | bajo | Monolitos / Ruinas |
| `pistola_dorada_una_bala` | Pistola dorada de una bala | legendaria | letal | alto | evento especial |
| `katana_partida` | Katana partida | epica | alto | bajo | templo o jefe errante |
| `escopeta_ceremonial` | Escopeta ceremonial | epica | alto | muy alto | templo o bastion |
| `guante_electrico` | Guante electrico | epica | alto | medio | Sector X / militar |
| `granada_antigua` | Granada antigua | epica | letal | muy alto | ruinas militares |
| `dron_explosivo_danado` | Dron explosivo danado | epica | letal | alto | observatorio / Sector X |
| `torreta_portatil_defectuosa` | Torreta portatil defectuosa | epica | alto | muy alto | estacion militar |
| `baston_choque` | Baston de choque | epica | alto | medio | guardian tecnologico |
| `arma_experimental_org` | Arma experimental de la organizacion | legendaria | variable | variable | evento mayor |

## Estados posibles

Un arma puede tener modificadores:

- `nueva`;
- `gastada`;
- `oxidada`;
- `rota`;
- `afilada`;
- `desafilada`;
- `cargada`;
- `descargada`;
- `atascada`;
- `silenciada`;
- `improvisada`;
- `contaminada`;
- `bendecida`;
- `maldita`.

## Reglas narrativas utiles

- Un arma con `noise: alto` puede atraer criaturas, lugarenos armados o guardianes.
- Un arma con `threat: alta` puede resolver una escena sin combate si el rival cree la amenaza.
- Un arma descargada puede servir para mentir, pero si la mentira se descubre sube la hostilidad.
- Las armas improvisadas deberian romperse mas seguido, pero ser faciles de fabricar.
- Las trampas deberian tener memoria de zona: si alguien cae en una, otros NPCs pueden evitar esa ruta.
- Algunas armas deberian abrir rutas: palanca para puertas, hacha para madera, explosivo para barricadas.
- Las armas especiales no deberian aparecer por loot comun; deben tener historia, guardian o costo.

## Lista corta para el sandbox de 4 casillas

Para la primera demo cargaria pocas armas y muchas decisiones:

| Casilla | Armas comunes | Armas raras o especiales |
| --- | --- | --- |
| 1 Faro | `cuchillo_viejo`, `palo_madera`, `antorcha` | `pistola_bengalas`, `hacha_farero` |
| 2 Campamento | `navaja_fina`, `trampa_lazo`, `lanza_casera` | `arco_simple`, `pistola_sin_balas` |
| 6 Monolitos | `piedra_filosa`, `soga_piedra`, `dardos` | `dardo_venenoso`, `lanza_estrella` |
| 7 Ruinas | `palanca_hierro`, `pinchos_ocultos`, `cuerda_tensada` | `ballesta_ligera`, `espada_ceremonial` |

## Siguiente paso

Cuando esta lista sea aprobada, conviene convertirla a:

```txt
data/items_weapons.json
```

Ese JSON sera el catalogo que el bot pueda usar para loot, combate, amenazas,
trampas, trueque, crafting y eventos de zona.
