from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets" / "skills y mats" / "hellgames_material_sets"
GUIDE_DIR = BASE / "guide"
ICONS_DIR = BASE / "icons_by_id"


LEVEL_NAMES = {
    1: "Nivel 1 - Basico / loot directo",
    2: "Nivel 2 - Procesable / requiere herramienta o contexto",
    3: "Nivel 3 - Tecnico, medico o raro",
    4: "Nivel 4 - Especial de evento o progreso mayor",
}

CATEGORY_FALLBACK_ZONES = {
    "Agua y recipientes": "4 Cascada, 17 Oasis/Templo de la Luna, 16 Costa, 21 Muelle, campamentos y recipientes abandonados.",
    "Madera y vegetales secos": "2 Campamento, 8 Pradera, 9 Templo de las Hojas, 16 Costa, 23 Jungla.",
    "Piedra, tierra y minerales": "3 Minas, 6 Monolitos, 7 Ruinas, 15 Templo del Sol, 18 Canon, 25 Volcan.",
    "Metal y chatarra": "5 Puerto, 7 Ruinas, 10 Bastion, 13 Torre, 19 Estacion Militar, 20 Observatorio.",
    "Cuerdas, telas y fibras": "2 Campamento, 5 Puerto, 16 Costa, 18 Canon, 21 Muelle, 22 Pueblo Nevado.",
    "Combustible y energia": "1 Faro, 12 Sector X, 13 Torre, 19 Estacion Militar, 20 Observatorio.",
    "Medicina y quimica": "4 Cascada, 11 Pantano, 17 Oasis, 19 Estacion Militar, Sector X/laboratorios.",
    "Plantas, hongos y alimentos vegetales": "2 Campamento, 8 Pradera, 9 Templo de las Hojas, 11 Pantano, 23 Jungla.",
    "Comida animal y conservas": "4 Cascada, 14 Granja, 16 Costa, 21 Muelle, 22 Pueblo Nevado.",
    "Tecnologia y electronica": "1 Faro, 12 Sector X, 13 Torre, 19 Estacion Militar, 20 Observatorio.",
    "Reliquias, llaves y objetos narrativos": "6 Monolitos, 7 Ruinas, 12 Sector X, 15 Templo del Sol, 25 Volcan, guardianes.",
}

ITEM_ZONE_OVERRIDES = {
    "agua_limpia": "4 Cascada, 17 Oasis/Templo de la Luna, 23 Jungla parcial; tambien 1 Faro y 2 Campamento en piloto.",
    "agua_turbia": "11 Pantano, 5 Puerto, 16 Costa, zonas inundadas o recipientes sucios.",
    "arena": "16 Costa, 21 Muelle, 24 Bastion Duna Seca, playas y dunas.",
    "cristal_verde": "12 Sector X principalmente; tambien 3 Minas como cristal raro o eventos contaminados.",
    "cristal_energetico": "12 Sector X, 25 Volcan, laboratorios, guardianes o eventos de alto riesgo.",
    "fragmento_estrella": "6 Monolitos, 12 Sector X, 15 Templo del Sol, 25 Volcan, jefes o guardianes.",
    "tela_vela": "16 Costa del Naufragio, 5 Puerto, 21 Muelle y barcos abandonados.",
    "pescado_seco": "4 Cascada, 5 Puerto, 16 Costa, 21 Muelle.",
    "bateria_pequena": "1 Faro, 13 Torre, 19 Estacion Militar, 20 Observatorio, almacenes tecnicos.",
    "bateria_auto": "19 Estacion Militar, talleres, vehiculos ocultos, puerto y zonas mecanicas.",
    "cable_electrico": "1 Faro, 12 Sector X, 13 Torre, 19 Estacion Militar, 20 Observatorio.",
    "circuito_roto": "12 Sector X, 13 Torre, 19 Estacion Militar, 20 Observatorio, drones/camaras rotas.",
    "fusible": "13 Torre, 19 Estacion Militar, 20 Observatorio, Sector X, minas/monoriel.",
    "bobina_cobre": "Sector X, Observatorio, Estacion Militar, talleres, motores y generadores.",
    "veneno_liquido": "11 Pantano, Sector X, laboratorios, tramperos y zonas de veneno.",
    "antidoto": "17 Oasis, 11 Pantano por necesidad, Sector X/laboratorio, medicos.",
}

PILOT_OVERRIDES = {
    "agua_limpia": "1 Faro y 2 Campamento como loot comun; tambien inventarios iniciales.",
    "bateria_pequena": "1 Faro como loot raro; clave para radio/faro.",
    "cable_electrico": "1 Faro comun; Renzo inicia con cable corto equivalente.",
    "rama_seca": "2 Campamento comun; base de fogata y lanza.",
    "tela": "2 Campamento comun; base de vendas, filtros y antorchas.",
    "retazo_tela": "2 Campamento/runtime; Rex inicia con uno.",
    "cuerda_fina": "2 Campamento comun; base de trampas y lanzas.",
    "lata_comida": "2 Campamento comun; comida segura.",
    "pedernal": "2 Campamento comun segun lista corta.",
    "piedra_comun": "6 Monolitos y 7 Ruinas por entorno; posible en 2 Campamento.",
    "piedra_filosa": "6 Monolitos y 7 Ruinas como hallazgo; clave para lanza/hacha.",
    "piedra_lisa": "6 Monolitos como variante ritual posible.",
    "fragmento_estrella": "6 Monolitos como loot raro; objetivo de progreso.",
    "cuerda_vieja": "7 Ruinas como loot comun.",
    "placa_metalica": "7 Ruinas como loot comun.",
    "clavos": "2 Campamento y 7 Ruinas como material de trampas.",
    "alambre": "1 Faro por radio/antenas; 7 Ruinas como trampa vieja posible.",
    "polvo_irritante": "7 Ruinas o 6 Monolitos como polvo raro posible.",
}


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_manifest() -> dict:
    return json.loads((BASE / "material_sets_manifest.json").read_text(encoding="utf-8"))


def parse_resource_catalog() -> dict[str, dict]:
    text = read_text("HELL_GAMES_OBJETOS_RECURSOS.md")
    current_category = ""
    items: dict[str, dict] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        section = re.match(r"^## \d+\. (.+)$", line)
        if section:
            current_category = section.group(1)
            continue
        if not line.startswith("| `"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 4:
            continue
        item_id = parts[0].strip("`")
        items[item_id] = {
            "name": parts[1],
            "rarity": parts[2],
            "uses": parts[3],
            "category": current_category,
        }
    return items


def parse_recipes() -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    text = read_text("HELL_GAMES_RECETAS_CRAFTING.md")
    as_input: dict[str, list[str]] = defaultdict(list)
    as_output: dict[str, list[str]] = defaultdict(list)
    for line in text.splitlines():
        if not line.startswith("| `"):
            continue
        ids = re.findall(r"`([^`]+)`", line)
        if len(ids) < 2:
            continue
        recipe_id = ids[0]
        output_id = ids[1]
        as_output[output_id].append(recipe_id)
        for ingredient in ids[2:]:
            as_input[ingredient].append(recipe_id)
    return as_input, as_output


def collect_materials(manifest: dict, catalog: dict, as_input: dict, as_output: dict) -> list[dict]:
    seen = set()
    materials = []
    for material_set in manifest["sets"]:
        for item in material_set["items"]:
            item_id = item["id"]
            if item_id in seen:
                continue
            seen.add(item_id)
            cat_data = catalog.get(item_id, {})
            category = cat_data.get("category") or category_from_set(material_set["id"])
            rarity = cat_data.get("rarity", "sin dato")
            level = infer_level(item_id, rarity, category, item_id in as_output)
            materials.append(
                {
                    "id": item_id,
                    "name": item["name"],
                    "category": category,
                    "rarity": rarity,
                    "level": level,
                    "level_name": LEVEL_NAMES[level],
                    "kind": infer_kind(level, rarity, category, item_id in as_output),
                    "fabrication": describe_fabrication(item_id, as_input, as_output),
                    "uses": cat_data.get("uses", "Uso pendiente de catalogar."),
                    "recipes": ", ".join(sorted(set(as_input.get(item_id, []) + as_output.get(item_id, [])))) or "Sin receta directa documentada.",
                    "pilot": PILOT_OVERRIDES.get(item_id, "No prioritario en piloto; posible por evento, trueque o exploracion."),
                    "full_island": ITEM_ZONE_OVERRIDES.get(item_id) or CATEGORY_FALLBACK_ZONES.get(category, "Zonas pendientes de definir."),
                    "icon": f"icons_by_id/{item_id}.png",
                }
            )
    return sorted(materials, key=lambda x: (x["level"], x["category"], x["id"]))


def category_from_set(set_id: str) -> str:
    return {
        "supervivencia": "Supervivencia basica",
        "minerales_metal": "Piedra, tierra y minerales",
        "fibras_alimentos": "Cuerdas, telas y fibras",
        "quimica_energia_raros": "Medicina y quimica",
    }.get(set_id, "Materiales")


def infer_level(item_id: str, rarity: str, category: str, is_output: bool) -> int:
    if item_id in {"fragmento_estrella", "cristal_verde", "cristal_energetico"}:
        return 4
    if "muy raro" in rarity or category.startswith("Reliquias"):
        return 4
    if "raro" in rarity or item_id in {"antidoto", "veneno_liquido", "acido", "bateria_auto", "bobina_cobre"}:
        return 3
    if is_output or "poco comun" in rarity or item_id in {"carbon_vegetal", "pescado_seco"}:
        return 2
    return 1


def infer_kind(level: int, rarity: str, category: str, is_output: bool) -> str:
    if level == 4:
        return "Especial / objetivo"
    if is_output and level >= 2:
        return "Fabricado o procesado"
    if level == 3:
        return "Tecnico, medico o raro"
    if level == 2:
        return "Procesable / poco comun"
    if "agua" in category.lower() or "comida" in category.lower():
        return "Basico vital"
    return "Basico"


def describe_fabrication(item_id: str, as_input: dict, as_output: dict) -> str:
    outputs = sorted(set(as_output.get(item_id, [])))
    inputs = sorted(set(as_input.get(item_id, [])))
    if outputs and inputs:
        return "Opcional: puede encontrarse o fabricarse/procesarse; tambien sirve como ingrediente."
    if outputs:
        return "Si u opcional: aparece como resultado de fabricacion/procesamiento."
    if inputs:
        return "No principalmente: se consigue como loot/recoleccion y se usa como ingrediente."
    return "No documentada: tratable como loot, trueque o hallazgo de zona."


def write_json(materials: list[dict]) -> None:
    GUIDE_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "title": "Hell Games - Guia de materiales",
        "source_docs": [
            "HELL_GAMES_OBJETOS_RECURSOS.md",
            "doc_materiales1.md",
            "HELL_GAMES_RECETAS_CRAFTING.md",
            "HELL_GAMES_CASILLAS.md",
            "data/prototype_runtime_4.json",
            "data/prototype_island_4.json",
        ],
        "hierarchy": [{"level": level, "name": name} for level, name in LEVEL_NAMES.items()],
        "items": materials,
    }
    (GUIDE_DIR / "material_guide_data.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_markdown(materials: list[dict]) -> None:
    lines = [
        "# Hell Games - Guia de materiales",
        "",
        "Guia practica de los materiales separados desde los sets de iconos. Cubre uso, jerarquia, si son loot basico o requieren fabricacion/procesamiento, y ubicaciones sugeridas para isla completa y piloto de 4 casillas.",
        "",
        "Fuentes: `HELL_GAMES_OBJETOS_RECURSOS.md`, `doc_materiales1.md`, `HELL_GAMES_RECETAS_CRAFTING.md`, `HELL_GAMES_CASILLAS.md`, `data/prototype_runtime_4.json`, `data/prototype_island_4.json`.",
        "",
        "## Jerarquia",
        "",
    ]
    for name in LEVEL_NAMES.values():
        lines.append(f"- **{name}**")
    lines += [
        "",
        "## Piloto de 4 casillas",
        "",
        "| Casilla | Rol | Materiales especialmente relevantes |",
        "| --- | --- | --- |",
        "| 1 Faro de la Vigilia Sagrada | senales, radio, misterio tecnico | `agua_limpia`, `cable_electrico`, `bateria_pequena`, `botella_vacia`, `chatarra` |",
        "| 2 Campamento Raiz Maldita | refugio, supervivencia, crafting inicial | `rama_seca`, `tela`, `retazo_tela`, `cuerda_fina`, `lata_comida`, `pedernal`, `agua_limpia`, `fibra_vegetal` |",
        "| 6 Circulo de Monolitos | ritual, pistas, presion psicologica | `piedra_comun`, `piedra_filosa`, `piedra_lisa`, `fragmento_estrella`, `hongos_alucinogenos` |",
        "| 7 Ruinas del Guardian | trampas, metal, reliquias | `cuerda_vieja`, `placa_metalica`, `clavos`, `alambre`, `piedra_filosa`, `polvo_irritante` |",
        "",
    ]

    for category in sorted({m["category"] for m in materials}):
        lines += [
            f"## {category}",
            "",
            "| Nivel | ID | Nombre | Tipo | Fabricacion | Usos | Recetas/proyectos | Piloto | Isla completa |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for item in [m for m in materials if m["category"] == category]:
            lines.append(
                f"| {item['level']} | `{item['id']}` | {item['name']} | {item['kind']} | "
                f"{item['fabrication']} | {item['uses']} | {item['recipes']} | {item['pilot']} | {item['full_island']} |"
            )
        lines.append("")
    (GUIDE_DIR / "GUIA_MATERIALES_HELLGAMES.md").write_text("\n".join(lines), encoding="utf-8")


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    path = Path("C:/Windows/Fonts") / name
    try:
        return ImageFont.truetype(str(path), size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, width: int) -> list[str]:
    words = str(text).split()
    lines: list[str] = []
    current = ""
    for word in words:
        test = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), test, font=font)[2] <= width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font, fill, width: int, line_h: int) -> int:
    x, y = xy
    for line in wrap(draw, text, font, width):
        draw.text((x, y), line, font=font, fill=fill)
        y += line_h
    return y


def write_pdf(materials: list[dict]) -> None:
    page_w, page_h = 1240, 1754
    margin = 70
    bg = (247, 244, 236)
    ink = (30, 28, 24)
    muted = (91, 83, 70)
    accent = (95, 50, 36)
    card = (255, 252, 244)
    line = (190, 179, 160)

    font_title = load_font("arialbd.ttf", 42)
    font_h1 = load_font("arialbd.ttf", 30)
    font_h2 = load_font("arialbd.ttf", 22)
    font_body = load_font("arial.ttf", 18)
    font_small = load_font("arial.ttf", 15)
    font_bold = load_font("arialbd.ttf", 17)

    def new_page():
        image = Image.new("RGB", (page_w, page_h), bg)
        return image, ImageDraw.Draw(image)

    pages = []
    image, draw = new_page()
    y = 90
    draw.text((margin, y), "Hell Games", font=font_title, fill=accent)
    y += 58
    draw.text((margin, y), "Guia de materiales", font=font_h1, fill=ink)
    y += 54
    y = draw_wrapped(
        draw,
        (margin, y),
        "Materiales separados desde los sets de iconos. Incluye uso jugable, jerarquia, relacion con fabricacion y ubicaciones sugeridas para isla completa y piloto de 4 casillas.",
        font_body,
        ink,
        page_w - 2 * margin,
        26,
    )
    y += 35
    draw.text((margin, y), "Jerarquia de progreso", font=font_h1, fill=ink)
    y += 40
    for level, text in LEVEL_NAMES.items():
        draw.rounded_rectangle((margin, y, page_w - margin, y + 72), radius=10, fill=card, outline=line)
        draw.text((margin + 20, y + 14), f"Nivel {level}", font=font_h2, fill=accent)
        draw.text((margin + 140, y + 18), text.split(" - ", 1)[1], font=font_body, fill=ink)
        y += 88
    y += 20
    draw.text((margin, y), "Piloto de 4 casillas", font=font_h1, fill=ink)
    y += 40
    for text in [
        "1 Faro: agua limpia, cable electrico, bateria pequena, botella/chatarra posible.",
        "2 Campamento: rama seca, tela, retazo, cuerda fina, lata, pedernal, fibra vegetal.",
        "6 Monolitos: piedra, piedra filosa/lisa, fragmento de estrella, hongos raros posibles.",
        "7 Ruinas: cuerda vieja, placa metalica, clavos, alambre, piedra filosa, polvo irritante.",
    ]:
        y = draw_wrapped(draw, (margin + 10, y), "- " + text, font_body, ink, page_w - 2 * margin - 20, 26)
        y += 8
    pages.append(image)

    for category in sorted({m["category"] for m in materials}):
        category_items = [m for m in materials if m["category"] == category]
        image, draw = new_page()
        y = 58
        draw.text((margin, y), category, font=font_h1, fill=accent)
        y += 48
        for item in category_items:
            card_h = 174
            if y + card_h > page_h - 70:
                pages.append(image)
                image, draw = new_page()
                y = 58
                draw.text((margin, y), category + " (cont.)", font=font_h1, fill=accent)
                y += 48
            draw.rounded_rectangle((margin, y, page_w - margin, y + card_h), radius=10, fill=card, outline=line)
            icon_path = BASE / item["icon"]
            if icon_path.exists():
                icon = Image.open(icon_path).convert("RGB").resize((112, 112), Image.Resampling.LANCZOS)
                image.paste(icon, (margin + 18, y + 18))
            tx = margin + 150
            draw.text((tx, y + 14), f"{item['name']}  ({item['id']})", font=font_h2, fill=ink)
            draw.text((tx, y + 42), f"Nivel {item['level']} - {item['kind']}", font=font_bold, fill=accent)
            yy = y + 68
            yy = draw_wrapped(draw, (tx, yy), "Fabricacion: " + item["fabrication"], font_small, ink, page_w - margin - tx - 20, 20)
            yy = draw_wrapped(draw, (tx, yy), "Usos: " + item["uses"], font_small, ink, page_w - margin - tx - 20, 20)
            draw_wrapped(draw, (tx, yy), "Piloto: " + item["pilot"], font_small, muted, page_w - margin - tx - 20, 20)
            y += card_h + 18
        pages.append(image)

    pdf_path = GUIDE_DIR / "GUIA_MATERIALES_HELLGAMES.pdf"
    pages[0].save(pdf_path, save_all=True, append_images=pages[1:])


def main() -> None:
    manifest = load_manifest()
    catalog = parse_resource_catalog()
    as_input, as_output = parse_recipes()
    materials = collect_materials(manifest, catalog, as_input, as_output)
    write_json(materials)
    write_markdown(materials)
    write_pdf(materials)
    print(f"materials: {len(materials)}")
    print((GUIDE_DIR / "GUIA_MATERIALES_HELLGAMES.md").resolve())
    print((GUIDE_DIR / "material_guide_data.json").resolve())
    print((GUIDE_DIR / "GUIA_MATERIALES_HELLGAMES.pdf").resolve())


if __name__ == "__main__":
    main()
