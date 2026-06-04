## Hell Games - contexto para Codex

Este proyecto tiene continuidad entre sesiones. Antes de tocar codigo o mover
archivos, leer:

1. `HELL_GAMES_CONTINUIDAD.md`
2. `BITACORA_SESION_HELL_GAMES_CASTING_CRIATURAS_2026-06-04.md`
3. `BITACORA_SESION_HELL_GAMES_ASSETS_CONOCIMIENTO_2026-06-04.md`
4. `README.md`
5. `README_HELLGAMES.md`

## Repo y ruta

- Ruta real del proyecto: `D:\2026\bot discord\bot evento`
- Repo GitHub: `https://github.com/matthyuga/hellgames.git`
- Remote Git: `origin`
- Rama principal usada: `main`

Usar `git status --short` antes de editar. Puede haber cambios locales de otras
sesiones; no revertir nada que no haya pedido el usuario.

## Assets y Git

No todos los assets visuales se versionan. La estrategia actual es:

- versionar codigo, documentos, datos JSON, manifiestos y scripts;
- mantener assets pesados locales o subirlos a Discord/CDN;
- usar IDs/rutas/URLs para conectar el bot con imagenes.

`assets/characters/` esta ignorado por Git. En esa carpeta hay personajes y
criaturas locales importantes para el piloto.

La carpeta `assets/skills y mats/` contiene sets visuales de materiales, armas,
libros y escritura generados en otra sesion. Revisar `HELL_GAMES_CONTINUIDAD.md`
antes de decidir si commitear, ignorar o subir esos assets.

## Bot

Archivo principal:

```txt
hellgames.py
```

Arranque local:

```powershell
python hellgames.py
```

Despues de cambiar comandos slash:

```txt
/hg owner sync
```

No mostrar ni commitear `.env.hellgames`.

## Flujo vivo del piloto

Para la prueba actual, preferir:

```txt
/hg admin diagnostico
/hg admin iniciar_piloto
/hg admin avanzar_turno
/hg admin stalk rex
/hg mapa
/hg bitacora
```

`/hg admin sandbox` genera una simulacion completa y sirve para pruebas
tecnicas; no es el ritmo principal del juego vivo.

## Nexus Codex

Si hace falta memoria global entre sesiones, revisar:

```txt
K:\_CodexNexus\README.md
K:\_CodexNexus\projects.md
```

Usar Nexus como mapa de contexto, no como carpeta de trabajo.
