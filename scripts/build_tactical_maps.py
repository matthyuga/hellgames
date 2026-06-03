from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


GENERATED_DIR = Path(
    r"C:\Users\KEVIN\.codex\generated_images\019e71b8-1455-7342-9558-d489e98a7803"
)
START_MARKER = Path(".tactical_generation_start.txt")
OUT_ROOT = Path("assets/tactical_maps")
CELL_SIZE = 100
GRID_SIZE = 14
CANVAS_SIZE = CELL_SIZE * GRID_SIZE


SCENARIOS = [
    (1, "Faro de la Vigilia Sagrada", "faro_de_la_vigilia_sagrada"),
    (2, "Campamento Raíz Maldita", "campamento_raiz_maldita"),
    (3, "Minas de Hierro", "minas_de_hierro"),
    (4, "Cascada de los Susurros", "cascada_de_los_susurros"),
    (5, "Puerto del Navegante", "puerto_del_navegante"),
    (6, "Círculo de Monolitos", "circulo_de_monolitos"),
    (7, "Ruinas del Guardián", "ruinas_del_guardian"),
    (8, "Pradera Valle del Viento", "pradera_valle_del_viento"),
    (9, "Templo de las Hojas Carmesí", "templo_de_las_hojas_carmesi"),
    (10, "Bastión del Acantilado", "bastion_del_acantilado"),
    (11, "Pantano de los Olvidados", "pantano_de_los_olvidados"),
    (12, "Sector X", "sector_x"),
    (13, "Torre Centinela", "torre_centinela"),
    (14, "Granja Sangrienta", "granja_sangrienta"),
    (15, "Templo del Sol", "templo_del_sol"),
    (16, "Costa del Naufragio Negro", "costa_del_naufragio_negro"),
    (17, "Templo de la Luna", "templo_de_la_luna"),
    (18, "Cañón Partido", "canon_partido"),
    (19, "Estación Militar", "estacion_militar"),
    (20, "Observatorio Militar", "observatorio_militar"),
    (21, "Muelle Aguas Rojas", "muelle_aguas_rojas"),
    (22, "Pueblo Nevado", "pueblo_nevado"),
    (23, "Jungla de Bambú Diabólico", "jungla_de_bambu_diabolico"),
    (24, "Bastión Duna Seca", "bastion_duna_seca"),
    (25, "Volcán Ceniza Durmiente", "volcan_ceniza_durmiente"),
]


DEFAULT_POI = {
    1: [
        ("faro", "Torre del faro", ["F5", "F6", "G5", "G6"]),
        ("casa_cuidador", "Casa del cuidador", ["I6", "J6", "I7", "J7"]),
        ("santuario", "Santuario de vigilia", ["C8", "D8"]),
        ("acantilado", "Borde del acantilado", ["A1", "A2", "A3", "B1", "N1", "N2"]),
        ("radio_mastil", "Mastil de radio roto", ["K4"]),
    ],
    2: [
        ("fogata", "Fogata central", ["G7"]),
        ("tiendas", "Tiendas rasgadas", ["E5", "F5", "I6"]),
        ("raices", "Raices negras", ["C8", "D8", "E9"]),
    ],
    3: [
        ("entrada_mina", "Entrada principal", ["F4", "G4"]),
        ("rieles", "Rieles de vagoneta", ["G5", "G6", "G7"]),
        ("mineral", "Veta de hierro", ["J5", "J6"]),
    ],
    4: [
        ("cascada", "Cascada", ["G2", "H2"]),
        ("poza", "Poza azul", ["G5", "H5", "G6", "H6"]),
        ("hierbas", "Hierbas medicinales", ["D8", "E8"]),
    ],
    5: [
        ("muelle", "Muelle principal", ["G6", "H6", "I6"]),
        ("barco", "Barco dañado", ["K8", "K9"]),
        ("cajas", "Cajas de carga", ["E5", "F5"]),
    ],
    6: [
        ("circulo", "Centro ritual", ["G7", "H7"]),
        ("monolitos", "Piedras exteriores", ["D5", "K5", "D10", "K10"]),
    ],
    7: [
        ("puerta", "Puerta sellada", ["H4", "I4"]),
        ("patio", "Patio de ruinas", ["G7", "H7"]),
        ("trampas", "Pasillo de trampas", ["E6", "E7", "E8"]),
    ],
    8: [
        ("molino", "Molino viejo", ["G5", "H5"]),
        ("campo", "Campo abierto", ["F8", "G8", "H8"]),
        ("zanjas", "Zanjas de viento", ["C10", "D10"]),
    ],
    9: [
        ("templo", "Templo carmesi", ["G5", "H5"]),
        ("ofrendas", "Piedras de ofrenda", ["G8", "H8"]),
        ("arroyo", "Arroyo de hojas", ["C9", "D9"]),
    ],
    10: [
        ("muralla", "Muralla del bastion", ["F4", "G4", "H4"]),
        ("patio", "Patio fortificado", ["G7", "H7"]),
        ("torre", "Torre de vigia", ["K5"]),
    ],
    11: [
        ("cabanas", "Cabanas elevadas", ["F5", "I6"]),
        ("pasarela", "Pasarela podrida", ["G7", "H7", "I7"]),
        ("agua", "Agua negra", ["D9", "E9"]),
    ],
    12: [
        ("cristales", "Cristales verdes", ["G6", "H6", "I6"]),
        ("contencion", "Barreras rotas", ["E8", "F8"]),
        ("pozo", "Pozo contaminado", ["J9"]),
    ],
    13: [
        ("torre", "Torre central", ["G6", "H6", "G7", "H7"]),
        ("compuerta", "Compuerta principal", ["G10", "H10"]),
        ("drones", "Puestos de drones", ["D5", "K5"]),
    ],
    14: [
        ("granja", "Casa roja", ["G5", "H5"]),
        ("granero", "Granero", ["J7", "K7"]),
        ("huerto", "Huerto sangriento", ["E9", "F9"]),
    ],
    15: [
        ("altar", "Altar solar", ["G7", "H7"]),
        ("columnas", "Columnas rotas", ["D5", "K5", "D10", "K10"]),
        ("escalera", "Escalera enterrada", ["H11"]),
    ],
    16: [
        ("naufragio", "Naufragio negro", ["G6", "H6", "I6"]),
        ("bodega", "Abertura de bodega", ["J7"]),
        ("marea", "Borde de marea", ["C10", "D10"]),
    ],
    17: [
        ("templo", "Templo lunar", ["G5", "H5"]),
        ("pozas", "Pozas reflectantes", ["F8", "I8"]),
        ("mercado", "Puestos silenciosos", ["D7", "E7"]),
    ],
    18: [
        ("puente", "Puente central", ["G7", "H7"]),
        ("cueva", "Boca de cueva", ["K5"]),
        ("precipicio", "Borde del cañon", ["C8", "D8"]),
    ],
    19: [
        ("antena", "Antena principal", ["G4"]),
        ("generador", "Generador", ["I7", "J7"]),
        ("bunker", "Bunker", ["F8", "G8"]),
    ],
    20: [
        ("plato", "Plato satelital", ["G6", "H6"]),
        ("bunker", "Bunker de observacion", ["I8", "J8"]),
        ("cables", "Campo de cables", ["E9", "F9"]),
    ],
    21: [
        ("muelle", "Muelle rojo", ["G7", "H7", "I7"]),
        ("casas", "Casas sobre agua", ["E5", "J5"]),
        ("barcas", "Barcas amarradas", ["K9"]),
    ],
    22: [
        ("plaza", "Plaza nevada", ["G7", "H7"]),
        ("sotano", "Entrada al sotano", ["I8"]),
        ("cabana", "Cabana helada", ["E5", "F5"]),
    ],
    23: [
        ("pasarela", "Pasarela elevada", ["G6", "H6", "I6"]),
        ("bambu", "Bambu cerrado", ["C5", "D5", "K9"]),
        ("choza", "Choza alta", ["J6"]),
    ],
    24: [
        ("mercado", "Mercado roto", ["G6", "H6"]),
        ("pozo", "Pozo seco", ["E8"]),
        ("cofres", "Cofres enterrados", ["J8", "K8"]),
    ],
    25: [
        ("cono", "Cono volcanico", ["G5", "H5"]),
        ("lava", "Grietas de lava", ["F8", "G8", "H8"]),
        ("plataforma", "Plataforma negra", ["J9"]),
    ],
}


def load_font(size: int):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


def normalize_image(source: Path) -> Image.Image:
    img = Image.open(source).convert("RGB")
    width, height = img.size
    side = min(width, height)
    left = (width - side) // 2
    top = (height - side) // 2
    return img.crop((left, top, left + side, top + side)).resize(
        (CANVAS_SIZE, CANVAS_SIZE), Image.LANCZOS
    )


def add_grid(img: Image.Image) -> Image.Image:
    grid = img.convert("RGBA")
    draw = ImageDraw.Draw(grid, "RGBA")
    for index in range(GRID_SIZE + 1):
        pos = index * CELL_SIZE
        alpha = 92 if index in (0, GRID_SIZE) else 58
        width = 3 if index in (0, GRID_SIZE) else 2
        draw.line([(pos, 0), (pos, CANVAS_SIZE)], fill=(245, 238, 205, alpha), width=width)
        draw.line([(0, pos), (CANVAS_SIZE, pos)], fill=(245, 238, 205, alpha), width=width)

    font = load_font(22)
    letters = "ABCDEFGHIJKLMN"
    for idx, letter in enumerate(letters):
        draw.text((idx * CELL_SIZE + 8, 6), letter, fill=(255, 250, 220, 135), font=font)
    for idx in range(GRID_SIZE):
        draw.text((6, idx * CELL_SIZE + 8), str(idx + 1), fill=(255, 250, 220, 135), font=font)
    return grid.convert("RGB")


def add_demo_markers(img: Image.Image) -> Image.Image:
    state = img.convert("RGBA")
    draw = ImageDraw.Draw(state, "RGBA")
    font = load_font(24)
    markers = [
        ("Mara", "D6", (225, 55, 55, 235)),
        ("Varek", "H8", (225, 55, 55, 235)),
        ("NPC", "K5", (55, 120, 230, 235)),
        ("Ruido", "B10", (245, 165, 45, 235)),
    ]
    letters = "ABCDEFGHIJKLMN"
    for name, coord, color in markers:
        col = letters.index(coord[0])
        row = int(coord[1:]) - 1
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        draw.ellipse((x - 18, y - 18, x + 18, y + 18), fill=color, outline=(255, 255, 255, 230), width=3)
        label_width = max(58, len(name) * 14)
        draw.rounded_rectangle((x + 22, y - 18, x + 22 + label_width, y + 16), radius=6, fill=(0, 0, 0, 150))
        draw.text((x + 30, y - 15), name, fill=(255, 255, 255, 235), font=font)
    return state.convert("RGB")


def scenario_dir(scenario_id: int, slug: str) -> Path:
    return OUT_ROOT / f"scenario_{scenario_id:02d}_{slug}"


def write_tactical_data(scenario_id: int, name: str, slug: str, clean: Path, grid: Path, demo: Path) -> Path:
    pois = [
        {"id": poi_id, "name": poi_name, "cells": cells}
        for poi_id, poi_name, cells in DEFAULT_POI.get(scenario_id, [])
    ]
    data = {
        "scenario_id": scenario_id,
        "name": name,
        "grid_width": GRID_SIZE,
        "grid_height": GRID_SIZE,
        "cell_size_px": CELL_SIZE,
        "clean_image": clean.as_posix(),
        "grid_image": grid.as_posix(),
        "state_demo_image": demo.as_posix(),
        "poi": pois,
        "blocked_cells_initial": [],
        "notes": "Mapa tactico generado como primera pasada. Revisar POI y celdas bloqueadas manualmente antes de usarlo como canon estricto.",
    }
    path = scenario_dir(scenario_id, slug) / f"scenario_{scenario_id:02d}_tactical.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def build_contact_sheet(manifest: list[dict]) -> None:
    thumb_w, thumb_h = 180, 180
    label_h = 44
    pad = 10
    cols = 5
    rows = 5
    sheet = Image.new(
        "RGB",
        (cols * (thumb_w + pad) + pad, rows * (thumb_h + label_h + pad) + pad),
        (18, 20, 24),
    )
    draw = ImageDraw.Draw(sheet)
    font = load_font(13)
    for idx, item in enumerate(manifest):
        row, col = divmod(idx, cols)
        x = pad + col * (thumb_w + pad)
        y = pad + row * (thumb_h + label_h + pad)
        img = Image.open(item["grid_image"]).convert("RGB")
        img.thumbnail((thumb_w, thumb_h), Image.LANCZOS)
        sheet.paste(img, (x + (thumb_w - img.width) // 2, y + (thumb_h - img.height) // 2))
        label = f"{item['scenario_id']:02d} {item['name']}"
        words = label.split()
        lines: list[str] = []
        current = ""
        for word in words:
            test = (current + " " + word).strip()
            if len(test) > 25 and current:
                lines.append(current)
                current = word
            else:
                current = test
        if current:
            lines.append(current)
        for line_no, line in enumerate(lines[:2]):
            draw.text((x, y + thumb_h + 5 + line_no * 16), line, fill=(235, 235, 235), font=font)
    sheet.save(OUT_ROOT / "contact_sheet_tactical_maps.png", optimize=True)


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    start_text = START_MARKER.read_text(encoding="ascii").strip()
    # Marker is local time text; use file ordering after it was written.
    marker_time = START_MARKER.stat().st_mtime
    generated = sorted(
        [p for p in GENERATED_DIR.glob("*.png") if p.stat().st_mtime >= marker_time],
        key=lambda p: p.stat().st_mtime,
    )
    if len(generated) < 24:
        raise SystemExit(f"Expected 24 new generated maps after {start_text}; found {len(generated)}")

    manifest: list[dict] = []
    # Scenario 1 already exists. Normalize manifest entry first.
    first_dir = scenario_dir(1, SCENARIOS[0][2])
    first_data = first_dir / "scenario_01_tactical.json"
    if first_data.exists():
        existing = json.loads(first_data.read_text(encoding="utf-8"))
        manifest.append(
            {
                "scenario_id": 1,
                "name": SCENARIOS[0][1],
                "grid_width": existing["grid_width"],
                "grid_height": existing["grid_height"],
                "clean_image": existing["clean_image"],
                "grid_image": existing["grid_image"],
                "tactical_data": first_data.as_posix(),
            }
        )

    for (scenario_id, name, slug), source in zip(SCENARIOS[1:], generated[:24]):
        out_dir = scenario_dir(scenario_id, slug)
        out_dir.mkdir(parents=True, exist_ok=True)
        normalized = normalize_image(source)
        clean = out_dir / f"scenario_{scenario_id:02d}_clean.png"
        grid = out_dir / f"scenario_{scenario_id:02d}_grid_14x14.png"
        demo = out_dir / f"scenario_{scenario_id:02d}_state_demo.png"
        normalized.save(clean, optimize=True)
        grid_img = add_grid(normalized)
        grid_img.save(grid, optimize=True)
        add_demo_markers(grid_img).save(demo, optimize=True)
        data_path = write_tactical_data(scenario_id, name, slug, clean, grid, demo)
        manifest.append(
            {
                "scenario_id": scenario_id,
                "name": name,
                "grid_width": GRID_SIZE,
                "grid_height": GRID_SIZE,
                "clean_image": clean.as_posix(),
                "grid_image": grid.as_posix(),
                "tactical_data": data_path.as_posix(),
            }
        )

    manifest_path = OUT_ROOT / "manifest_tactical_maps.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    build_contact_sheet(manifest)
    print(f"Built tactical maps: {len(manifest)}")


if __name__ == "__main__":
    main()
