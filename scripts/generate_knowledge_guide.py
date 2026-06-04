from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets" / "skills y mats" / "hellgames_knowledge_sets"
GUIDE_DIR = BASE / "guide"
ICONS_DIR = BASE / "icons_by_id"
DATA_PATH = ROOT / "data" / "skill_books_and_recipe_knowledge.json"

LEVEL_NAMES = {
    "basico": "Basico - entrada segura al sistema",
    "intermedio": "Intermedio - requiere lectura y algo de practica",
    "avanzado": "Avanzado - tecnica, riesgo o proyecto concreto",
    "experto": "Experto - secreto, evento o conocimiento raro",
}

ZONE_NAMES = {
    1: "Faro",
    2: "Campamento",
    3: "Minas",
    4: "Cascada",
    5: "Puerto",
    6: "Monolitos",
    7: "Ruinas",
    11: "Pantano",
    12: "Sector X",
    13: "Torre",
    14: "Granja",
    15: "Templo del Sol",
    16: "Costa",
    17: "Templo de la Luna",
    19: "Estacion Militar",
    20: "Observatorio",
    21: "Muelle",
    22: "Pueblo Nevado",
    23: "Jungla",
    25: "Volcan",
}

PILOT_NOTES = {
    "manual_radio_faro": "Casilla 1. Permite reparar radio/faro si hay piezas.",
    "diario_farero": "Casilla 1. Pista de luz nocturna y mapa anotado.",
    "manual_primeros_auxilios": "Casilla 2. Curacion leve y venda improvisada.",
    "manual_supervivencia_humeda": "Casilla 2. Fogata, filtro y agua segura.",
    "diario_ocultista": "Casilla 6. Pista incompleta de monolito.",
    "receta_suelta": "Casilla 7. Puede revelar trampa de lazo u otra receta puntual.",
    "papel_suelto": "Casilla 2. Base para copiar recetas simples.",
    "lapiz": "Casilla 2. Escritura simple resistente y corregible.",
    "carboncillo": "Casillas 2, 6 o 7. Mapas toscos, marcas y apuntes incompletos.",
    "tiza": "Casillas 6 o 7. Marcas de ruta o simbolos temporales.",
    "receta_escrita": "Casilla 7. Transferencia de receta puntual.",
    "apunte_incompleto": "Casilla 6 o 7. Pista parcial con riesgo de error.",
}


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        return ImageFont.truetype(str(Path("C:/Windows/Fonts") / name), size)
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


def load_data() -> tuple[dict, dict]:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    icon_index = json.loads((BASE / "icons_index.json").read_text(encoding="utf-8"))
    icons = {item["id"]: item["icon"] for item in icon_index["icons"]}
    return data, icons


def zones_text(zones: list[int] | None) -> str:
    if not zones:
        return "Zona variable o pendiente."
    return ", ".join(f"{zone} {ZONE_NAMES.get(zone, '')}".strip() for zone in zones)


def collect_items(data: dict, icons: dict[str, str]) -> tuple[list[dict], list[dict], list[dict]]:
    books = []
    for book in data["books"]:
        item_id = book["id"]
        books.append(
            {
                "id": item_id,
                "name": book["name"],
                "kind": "libro/manual",
                "tier": book.get("tier", "basico"),
                "skills": ", ".join(book.get("skills", [])),
                "read_hours": book.get("read_hours", "-"),
                "unlocks": ", ".join(book.get("unlocks", [])) or "Sin desbloqueo directo.",
                "zones": zones_text(book.get("zones")),
                "pilot": PILOT_NOTES.get(item_id, "No prioritario en piloto; puede aparecer por loot, NPC o evento."),
                "icon": icons.get(item_id, ""),
            }
        )

    materials = []
    for item in data["writing_materials"]:
        item_id = item["id"]
        materials.append(
            {
                "id": item_id,
                "name": item["name"],
                "kind": "escritura/documento",
                "rarity": item.get("rarity", "variable"),
                "uses": ", ".join(item.get("uses", [])),
                "pilot": PILOT_NOTES.get(item_id, "Puede aparecer como soporte de copia, comercio o pista."),
                "icon": icons.get(item_id, ""),
            }
        )

    recipes = []
    for recipe in data["writing_recipes"]:
        recipes.append(
            {
                "id": recipe["id"],
                "outputs": ", ".join(recipe.get("outputs", [])),
                "ingredients": ", ".join(recipe.get("ingredients", [])),
                "station": recipe.get("station", "ninguna"),
                "time_hours": recipe.get("time_hours", "-"),
                "risk": recipe.get("risk", "-"),
                "unlock": recipe.get("unlock", "-"),
            }
        )
    return books, materials, recipes


def write_json(data: dict, books: list[dict], materials: list[dict], recipes: list[dict]) -> None:
    GUIDE_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "title": "Hell Games - Guia de libros y habilidades",
        "source_docs": [
            "HELL_GAMES_LIBROS_HABILIDADES_RECETAS.md",
            "doc_hability1.md",
            "doc_habilidades2.md",
            "HELL_GAMES_RECETAS_CRAFTING.md",
            "HELL_GAMES_OBJETOS_RECURSOS.md",
            "data/skill_books_and_recipe_knowledge.json",
        ],
        "learning_rule": data["learning_rule"],
        "knowledge_layers": data["knowledge_layers"],
        "unlock_modes": data["unlock_modes"],
        "writing_logic": data["writing_logic"],
        "books": books,
        "writing_materials": materials,
        "writing_recipes": recipes,
        "pilot_books": data.get("pilot_books", {}),
    }
    (GUIDE_DIR / "knowledge_guide_data.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_markdown(data: dict, books: list[dict], materials: list[dict], recipes: list[dict]) -> None:
    lines = [
        "# Hell Games - Guia de libros, habilidades y recetas",
        "",
        "Guia practica del sistema de conocimiento: libros, manuales, folletos, recetas escritas, herramientas de escritura y su relacion con habilidades.",
        "",
        f"Regla central: **{data['learning_rule']}**",
        "",
        "## Capas de conocimiento",
        "",
    ]
    for layer in data["knowledge_layers"]:
        lines.append(f"- `{layer}`")
    lines += [
        "",
        "## Habilidad de escritura",
        "",
        "La escritura funciona como microhabilidad de apoyo. No reemplaza habilidades tecnicas: permite copiar, conservar, falsificar o transferir conocimiento.",
        "",
        "| Herramienta | Mejor uso | Limites |",
        "| --- | --- | --- |",
    ]
    for tool_id, rule in data["writing_logic"]["tool_rules"].items():
        lines.append(
            f"| `{tool_id}` | {', '.join(rule.get('best_for', []))} | {', '.join(rule.get('limits', []))} |"
        )

    lines += [
        "",
        "## Libros y manuales",
        "",
        "| Nivel | ID | Nombre | Habilidades | Lectura | Desbloquea | Zonas | Piloto |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    tier_order = {"basico": 1, "intermedio": 2, "avanzado": 3, "experto": 4}
    for item in sorted(books, key=lambda x: (tier_order.get(x["tier"], 9), x["id"])):
        lines.append(
            f"| {item['tier']} | `{item['id']}` | {item['name']} | {item['skills']} | {item['read_hours']}h | {item['unlocks']} | {item['zones']} | {item['pilot']} |"
        )

    lines += [
        "",
        "## Materiales de escritura y documentos",
        "",
        "| ID | Nombre | Rareza | Usos | Piloto |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in materials:
        lines.append(f"| `{item['id']}` | {item['name']} | {item['rarity']} | {item['uses']} | {item['pilot']} |")

    lines += [
        "",
        "## Recetas de escritura y copia",
        "",
        "| ID | Resultado | Ingredientes | Estacion | Tiempo | Riesgo | Desbloqueo |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for recipe in recipes:
        lines.append(
            f"| `{recipe['id']}` | {recipe['outputs']} | {recipe['ingredients']} | {recipe['station']} | {recipe['time_hours']}h | {recipe['risk']} | {recipe['unlock']} |"
        )

    lines += [
        "",
        "## Assets",
        "",
        "- `assets/skills y mats/hellgames_knowledge_sets/icons_by_id/`",
        "- `assets/skills y mats/hellgames_knowledge_sets/knowledge_sets_manifest.json`",
        "- `assets/skills y mats/hellgames_knowledge_sets/icons_index.json`",
    ]
    (GUIDE_DIR / "GUIA_LIBROS_HABILIDADES_HELLGAMES.md").write_text("\n".join(lines), encoding="utf-8")


def draw_icon(image: Image.Image, item: dict, xy: tuple[int, int], size: int) -> None:
    icon_ref = item.get("icon")
    if not icon_ref:
        return
    icon_path = BASE / icon_ref
    if icon_path.exists():
        icon = Image.open(icon_path).convert("RGB").resize((size, size), Image.Resampling.LANCZOS)
        image.paste(icon, xy)


def write_pdf(data: dict, books: list[dict], materials: list[dict], recipes: list[dict]) -> None:
    page_w, page_h = 1240, 1754
    margin = 70
    bg = (244, 241, 235)
    ink = (28, 25, 22)
    muted = (85, 77, 68)
    accent = (72, 48, 94)
    card = (255, 252, 246)
    line = (184, 174, 160)

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
    draw.text((margin, y), "Guia de libros y habilidades", font=font_h1, fill=ink)
    y += 54
    y = draw_wrapped(draw, (margin, y), data["learning_rule"], font_body, ink, page_w - 2 * margin, 28)
    y += 34
    draw.text((margin, y), "Capas de conocimiento", font=font_h1, fill=ink)
    y += 42
    for layer in data["knowledge_layers"]:
        draw.rounded_rectangle((margin, y, page_w - margin, y + 56), radius=10, fill=card, outline=line)
        draw.text((margin + 22, y + 15), layer, font=font_h2, fill=accent)
        y += 70
    y += 20
    draw.text((margin, y), "Version piloto", font=font_h1, fill=ink)
    y += 40
    for text in [
        "1 Faro: manual_radio_faro, diario_farero.",
        "2 Campamento: manual_primeros_auxilios, manual_supervivencia_humeda, papel, lapiz.",
        "6 Monolitos: diario_ocultista incompleto, marcas, tiza o carboncillo.",
        "7 Ruinas: receta_suelta, apunte_incompleto, mapas parciales o recetas de trampa.",
    ]:
        y = draw_wrapped(draw, (margin + 10, y), "- " + text, font_body, ink, page_w - 2 * margin - 20, 26)
        y += 8
    pages.append(image)

    tier_order = {"basico": 1, "intermedio": 2, "avanzado": 3, "experto": 4}
    sorted_books = sorted(books, key=lambda x: (tier_order.get(x["tier"], 9), x["id"]))
    image, draw = new_page()
    y = 58
    draw.text((margin, y), "Libros y manuales", font=font_h1, fill=accent)
    y += 48
    for item in sorted_books:
        card_h = 184
        if y + card_h > page_h - 70:
            pages.append(image)
            image, draw = new_page()
            y = 58
            draw.text((margin, y), "Libros y manuales (cont.)", font=font_h1, fill=accent)
            y += 48
        draw.rounded_rectangle((margin, y, page_w - margin, y + card_h), radius=10, fill=card, outline=line)
        draw_icon(image, item, (margin + 18, y + 18), 112)
        tx = margin + 150
        draw.text((tx, y + 14), f"{item['name']}  ({item['id']})", font=font_h2, fill=ink)
        draw.text((tx, y + 42), f"{item['tier']} | {item['skills']} | lectura {item['read_hours']}h", font=font_bold, fill=accent)
        yy = y + 70
        yy = draw_wrapped(draw, (tx, yy), "Desbloquea: " + item["unlocks"], font_small, ink, page_w - margin - tx - 20, 20)
        yy = draw_wrapped(draw, (tx, yy), "Zonas: " + item["zones"], font_small, ink, page_w - margin - tx - 20, 20)
        draw_wrapped(draw, (tx, yy), "Piloto: " + item["pilot"], font_small, muted, page_w - margin - tx - 20, 20)
        y += card_h + 18
    pages.append(image)

    image, draw = new_page()
    y = 58
    draw.text((margin, y), "Escritura y documentos", font=font_h1, fill=accent)
    y += 48
    for item in materials:
        card_h = 146
        if y + card_h > page_h - 70:
            pages.append(image)
            image, draw = new_page()
            y = 58
            draw.text((margin, y), "Escritura y documentos (cont.)", font=font_h1, fill=accent)
            y += 48
        draw.rounded_rectangle((margin, y, page_w - margin, y + card_h), radius=10, fill=card, outline=line)
        draw_icon(image, item, (margin + 18, y + 18), 96)
        tx = margin + 132
        draw.text((tx, y + 14), f"{item['name']}  ({item['id']})", font=font_h2, fill=ink)
        draw.text((tx, y + 42), f"Rareza: {item['rarity']}", font=font_bold, fill=accent)
        yy = y + 68
        yy = draw_wrapped(draw, (tx, yy), "Usos: " + item["uses"], font_small, ink, page_w - margin - tx - 20, 20)
        draw_wrapped(draw, (tx, yy), "Piloto: " + item["pilot"], font_small, muted, page_w - margin - tx - 20, 20)
        y += card_h + 18
    pages.append(image)

    image, draw = new_page()
    y = 58
    draw.text((margin, y), "Recetas de escritura", font=font_h1, fill=accent)
    y += 50
    for recipe in recipes:
        card_h = 130
        if y + card_h > page_h - 70:
            pages.append(image)
            image, draw = new_page()
            y = 58
            draw.text((margin, y), "Recetas de escritura (cont.)", font=font_h1, fill=accent)
            y += 50
        draw.rounded_rectangle((margin, y, page_w - margin, y + card_h), radius=10, fill=card, outline=line)
        draw.text((margin + 20, y + 14), recipe["id"], font=font_h2, fill=ink)
        draw.text((margin + 20, y + 42), f"Resultado: {recipe['outputs']} | {recipe['time_hours']}h | riesgo {recipe['risk']}", font=font_bold, fill=accent)
        yy = y + 70
        yy = draw_wrapped(draw, (margin + 20, yy), "Ingredientes: " + recipe["ingredients"], font_small, ink, page_w - 2 * margin - 40, 20)
        draw_wrapped(draw, (margin + 20, yy), "Desbloqueo: " + recipe["unlock"], font_small, muted, page_w - 2 * margin - 40, 20)
        y += card_h + 18
    pages.append(image)

    pages[0].save(GUIDE_DIR / "GUIA_LIBROS_HABILIDADES_HELLGAMES.pdf", save_all=True, append_images=pages[1:])


def write_contact_sheet() -> None:
    icons = sorted(ICONS_DIR.glob("*.png"))
    thumb = 96
    label_h = 34
    cols = 8
    rows = (len(icons) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb, rows * (thumb + label_h)), (28, 28, 28))
    draw = ImageDraw.Draw(sheet)
    font = load_font("arial.ttf", 10)
    for i, path in enumerate(icons):
        icon = Image.open(path).convert("RGB").resize((84, 84), Image.Resampling.LANCZOS)
        x = (i % cols) * thumb
        y = (i // cols) * (thumb + label_h)
        sheet.paste(icon, (x + 6, y + 4))
        draw.text((x + 4, y + thumb + 2), path.stem[:14], fill=(235, 235, 225), font=font)
    sheet.save(GUIDE_DIR / "knowledge_icons_contact.png")


def main() -> None:
    GUIDE_DIR.mkdir(parents=True, exist_ok=True)
    data, icons = load_data()
    books, materials, recipes = collect_items(data, icons)
    write_json(data, books, materials, recipes)
    write_markdown(data, books, materials, recipes)
    write_pdf(data, books, materials, recipes)
    write_contact_sheet()
    print(f"books: {len(books)}")
    print(f"writing materials/documents: {len(materials)}")
    print(f"writing recipes: {len(recipes)}")
    print((GUIDE_DIR / "GUIA_LIBROS_HABILIDADES_HELLGAMES.md").resolve())
    print((GUIDE_DIR / "knowledge_guide_data.json").resolve())
    print((GUIDE_DIR / "GUIA_LIBROS_HABILIDADES_HELLGAMES.pdf").resolve())


if __name__ == "__main__":
    main()
