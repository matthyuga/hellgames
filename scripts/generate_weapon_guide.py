from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets" / "skills y mats" / "hellgames_weapon_sets"
GUIDE_DIR = BASE / "guide"
ICONS_DIR = BASE / "icons_by_id"

LEVEL_NAMES = {
    1: "Nivel 1 - Comun / inicio",
    2: "Nivel 2 - Poco comun / craft o herramienta",
    3: "Nivel 3 - Raro / alto impacto",
    4: "Nivel 4 - Epico o legendario / evento",
}

CATEGORY_ZONE_FALLBACKS = {
    "Armas cuerpo a cuerpo simples": "1 Faro, 2 Campamento, 5 Puerto, 16 Costa, pueblos, tiendas y almacenes.",
    "Armas cuerpo a cuerpo avanzadas": "3 Minas, 7 Ruinas, 10 Bastion, 15 Templo del Sol, 19 Estacion Militar, jefes o guardianes.",
    "Armas a distancia primitivas": "2 Campamento, 8 Pradera, 9 Templo de las Hojas, 10 Bastion, 23 Jungla.",
    "Armas de fuego": "1 Faro, 10 Bastion, 13 Torre Centinela, 19 Estacion Militar, 20 Observatorio.",
    "Municiones y cargas": "10 Bastion, 13 Torre, 19 Estacion Militar, 20 Observatorio, trueque y escondites.",
    "Armas improvisadas": "2 Campamento, 7 Ruinas, 16 Costa, 23 Jungla; dependen de materiales cercanos.",
    "Trampas": "2 Campamento, 7 Ruinas, 10 Bastion, 11 Pantano, 15 Templo, 23 Jungla.",
    "Armas quimicas o ambientales": "11 Pantano, 12 Sector X, 17 Oasis/laboratorio, 19 Estacion Militar.",
    "Armas especiales del evento": "1 Faro, 6 Monolitos, 7 Ruinas, 12 Sector X, 15 Templo, 19 Estacion Militar, jefes.",
}

ITEM_ZONE_OVERRIDES = {
    "cuchillo_viejo": "1 Faro y 2 Campamento en piloto; tambien campamentos, casas, puerto y trueque.",
    "palo_madera": "1 Faro y 2 Campamento en piloto; bosques, campamentos y naufragio.",
    "pistola_bengalas": "1 Faro como arma rara/especial; costa, puerto y zonas de senales.",
    "hacha_pequena": "9 Templo/Bosque, 16 Costa, 23 Jungla, campamentos y talleres.",
    "navaja_fina": "2 Campamento en piloto; tiendas, campamentos y personajes sigilosos.",
    "trampa_lazo": "2 Campamento en piloto; bosques, jungla y zonas de caza.",
    "lanza_casera": "2 Campamento en piloto; craft inicial con rama, piedra y cuerda.",
    "arco_simple": "2 Campamento como rara; bosque, pradera, jungla y cazadores.",
    "pistola_sin_balas": "2 Campamento como bluff raro; bastion, estacion militar y saqueo.",
    "piedra_filosa": "6 Monolitos en piloto; minas, ruinas, canon y zonas rocosas.",
    "dardos": "6 Monolitos en piloto; ruinas, jungla, tramperos y laboratorios.",
    "lanza_estrella": "6 Monolitos / 7 Ruinas; requiere evento, altar o fragmento de estrella.",
    "palanca_hierro": "7 Ruinas en piloto; minas, puerto, talleres y puertas cerradas.",
    "pinchos_ocultos": "7 Ruinas en piloto; jungla, bosque y accesos defendidos.",
    "ballesta_ligera": "7 Ruinas como rara; bastion, ruinas, cazadores avanzados.",
    "espada_ceremonial": "7 Ruinas como rara; templos, monolitos y guardianes.",
    "guante_electrico": "12 Sector X, 13 Torre, 19 Estacion Militar; tecnologia experimental.",
    "molotov": "16 Costa, 5 Puerto, 2 Campamento si hay frasco/tela/gasolina; alto riesgo de fuego.",
    "bomba_humo_casera": "2 Campamento o 7 Ruinas si hay lata, polvo irritante y tela.",
    "trampa_oso": "14 Granja, 22 Pueblo Nevado, zonas de caza y refugios viejos.",
}

PILOT_OVERRIDES = {
    "cuchillo_viejo": "1 Faro comun; tambien Verek inicia con uno.",
    "palo_madera": "1 Faro comun como defensa simple.",
    "pistola_bengalas": "1 Faro rara/especial; sirve para senal y amenaza.",
    "navaja_fina": "2 Campamento comun; Silas inicia con una.",
    "trampa_lazo": "2 Campamento comun/craft; defensa sin combate directo.",
    "lanza_casera": "2 Campamento comun/craft; primera arma fabricable.",
    "arco_simple": "2 Campamento rara.",
    "pistola_sin_balas": "2 Campamento rara; bluff social.",
    "piedra_filosa": "6 Monolitos comun; tambien material/arma primitiva.",
    "dardos": "6 Monolitos comun.",
    "lanza_estrella": "6 Monolitos rara/legendaria; evento de progreso.",
    "palanca_hierro": "7 Ruinas comun; abre puertas o fuerza cofres.",
    "pinchos_ocultos": "7 Ruinas comun/trampa.",
    "ballesta_ligera": "7 Ruinas rara.",
    "espada_ceremonial": "7 Ruinas rara.",
}


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_manifest() -> dict:
    return json.loads((BASE / "weapon_sets_manifest.json").read_text(encoding="utf-8"))


def parse_weapon_catalog() -> dict[str, dict]:
    text = read_text("HELL_GAMES_ARMAS.md")
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
        row = {"name": parts[1], "category": current_category}
        if current_category == "Municiones y cargas":
            row.update({"rarity": parts[2], "damage": "", "noise": "", "uses": parts[3], "ammo": ""})
        elif current_category == "Armas especiales del evento":
            row.update({"rarity": parts[2], "damage": parts[3], "noise": parts[4], "uses": parts[5], "ammo": ""})
        elif current_category in {"Armas a distancia primitivas", "Armas de fuego"}:
            row.update({"rarity": parts[2], "damage": parts[3], "noise": parts[4], "ammo": parts[5], "uses": f"Municion/requisito: {parts[5]}"})
        elif current_category == "Trampas" or current_category == "Armas quimicas o ambientales":
            row.update({"rarity": parts[2], "damage": parts[3], "noise": parts[4], "uses": parts[5], "ammo": ""})
        elif current_category == "Armas improvisadas":
            row.update({"rarity": parts[2], "damage": parts[3], "noise": parts[4], "uses": f"Recursos base: {parts[5]}", "ammo": ""})
        else:
            row.update({"rarity": parts[2], "damage": parts[3], "noise": parts[4], "uses": parts[5], "ammo": ""})
        items[item_id] = row
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


def collect_weapons(manifest: dict, catalog: dict, as_input: dict, as_output: dict) -> list[dict]:
    seen = set()
    weapons = []
    for weapon_set in manifest["sets"]:
        for item in weapon_set["items"]:
            item_id = item["id"]
            if item_id in seen:
                continue
            seen.add(item_id)
            cat_data = catalog.get(item_id, {})
            category = cat_data.get("category") or category_from_set(weapon_set["id"])
            rarity = cat_data.get("rarity", "sin dato")
            level = infer_level(item_id, rarity, category, item_id in as_output)
            weapons.append(
                {
                    "id": item_id,
                    "name": item["name"],
                    "category": category,
                    "rarity": rarity,
                    "level": level,
                    "level_name": LEVEL_NAMES[level],
                    "kind": infer_kind(level, category, item_id in as_output),
                    "damage": cat_data.get("damage", ""),
                    "noise": cat_data.get("noise", ""),
                    "ammo": cat_data.get("ammo", ""),
                    "fabrication": describe_fabrication(item_id, category, as_input, as_output),
                    "uses": cat_data.get("uses", "Uso pendiente de catalogar."),
                    "recipes": ", ".join(sorted(set(as_input.get(item_id, []) + as_output.get(item_id, [])))) or "Sin receta directa documentada.",
                    "pilot": PILOT_OVERRIDES.get(item_id, "No prioritario en piloto; posible por loot, evento o trueque."),
                    "full_island": ITEM_ZONE_OVERRIDES.get(item_id) or CATEGORY_ZONE_FALLBACKS.get(category, "Zonas pendientes de definir."),
                    "icon": f"icons_by_id/{item_id}.png",
                }
            )
    return sorted(weapons, key=lambda x: (x["level"], x["category"], x["id"]))


def category_from_set(set_id: str) -> str:
    return {
        "melee_comunes": "Armas cuerpo a cuerpo simples",
        "melee_avanzadas_improvisadas": "Armas cuerpo a cuerpo avanzadas",
        "distancia_municion": "Armas a distancia primitivas",
        "fuego_trampas_especiales": "Armas de fuego",
    }.get(set_id, "Armas")


def infer_level(item_id: str, rarity: str, category: str, is_output: bool) -> int:
    if "legendaria" in rarity or "epica" in rarity or item_id in {"lanza_estrella", "guante_electrico"}:
        return 4
    if "raro" in rarity:
        return 3
    if "poco comun" in rarity or is_output:
        return 2
    return 1


def infer_kind(level: int, category: str, is_output: bool) -> str:
    if category == "Municiones y cargas":
        return "Municion / carga"
    if category == "Trampas":
        return "Trampa"
    if "fuego" in category.lower():
        return "Arma de fuego"
    if is_output:
        return "Fabricada / improvisada"
    if level == 4:
        return "Especial de evento"
    if level == 3:
        return "Rara / alto impacto"
    if level == 2:
        return "Poco comun"
    return "Basica"


def describe_fabrication(item_id: str, category: str, as_input: dict, as_output: dict) -> str:
    outputs = sorted(set(as_output.get(item_id, [])))
    if outputs:
        return "Si: se fabrica, monta o repara mediante receta documentada."
    if category == "Municiones y cargas":
        return "No principalmente: se encuentra separada del arma; algunas cargas pueden recargarse o fabricarse en sistema avanzado."
    if category == "Armas improvisadas":
        return "Normalmente si: nace de materiales, aunque puede aparecer ya hecha."
    if category == "Trampas":
        return "Normalmente si: se monta en zona; puede existir ya instalada."
    if category == "Armas especiales del evento":
        return "No: evento, guardian, zona unica o pacto; no es loot comun."
    return "No principalmente: loot, herramienta encontrada, trueque o arma de zona."


def write_json(weapons: list[dict]) -> None:
    GUIDE_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "title": "Hell Games - Guia de armas",
        "source_docs": ["HELL_GAMES_ARMAS.md", "doc_armas1.md", "HELL_GAMES_RECETAS_CRAFTING.md", "HELL_GAMES_CASILLAS.md", "data/prototype_runtime_4.json"],
        "hierarchy": [{"level": level, "name": name} for level, name in LEVEL_NAMES.items()],
        "items": weapons,
    }
    (GUIDE_DIR / "weapon_guide_data.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_index(manifest: dict) -> None:
    index = {"cell_icons": [], "id_icons": []}
    seen = set()
    for weapon_set in manifest["sets"]:
        for item in weapon_set["items"]:
            index["cell_icons"].append(
                {
                    "set": weapon_set["id"],
                    "source_sheet": weapon_set["file"],
                    "cell": item["cell"],
                    "id": item["id"],
                    "name": item["name"],
                    "icon": f"icons_cells/{weapon_set['id']}_{item['cell']:02d}_{item['id']}.png",
                }
            )
            if item["id"] not in seen:
                index["id_icons"].append({"id": item["id"], "name": item["name"], "icon": f"icons_by_id/{item['id']}.png"})
                seen.add(item["id"])
    (BASE / "icons_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


def write_markdown(weapons: list[dict]) -> None:
    lines = [
        "# Hell Games - Guia de armas",
        "",
        "Guia practica de armas, municiones y trampas separadas desde los sets de iconos. Incluye jerarquia, dano/ruido, si son loot o requieren fabricacion, y ubicaciones sugeridas para isla completa y piloto de 4 casillas.",
        "",
        "Fuentes: `HELL_GAMES_ARMAS.md`, `doc_armas1.md`, `HELL_GAMES_RECETAS_CRAFTING.md`, `HELL_GAMES_CASILLAS.md`, `data/prototype_runtime_4.json`.",
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
        "| Casilla | Rol | Armas especialmente relevantes |",
        "| --- | --- | --- |",
        "| 1 Faro de la Vigilia Sagrada | defensa simple, senales, amenaza social | `cuchillo_viejo`, `palo_madera`, `pistola_bengalas` |",
        "| 2 Campamento Raiz Maldita | craft inicial, defensa sin matar | `navaja_fina`, `trampa_lazo`, `lanza_casera`, `arco_simple`, `pistola_sin_balas` |",
        "| 6 Circulo de Monolitos | sigilo, ritual, amenaza rara | `piedra_filosa`, `dardos`, `lanza_estrella` |",
        "| 7 Ruinas del Guardian | trampas, cofres, guardianes | `palanca_hierro`, `pinchos_ocultos`, `ballesta_ligera`, `espada_ceremonial` |",
        "",
    ]
    for category in sorted({w["category"] for w in weapons}):
        lines += [
            f"## {category}",
            "",
            "| Nivel | ID | Nombre | Rareza | Dano | Ruido | Tipo | Fabricacion | Uso | Recetas/proyectos | Piloto | Isla completa |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for item in [w for w in weapons if w["category"] == category]:
            lines.append(
                f"| {item['level']} | `{item['id']}` | {item['name']} | {item['rarity']} | {item['damage']} | {item['noise']} | "
                f"{item['kind']} | {item['fabrication']} | {item['uses']} | {item['recipes']} | {item['pilot']} | {item['full_island']} |"
            )
        lines.append("")
    (GUIDE_DIR / "GUIA_ARMAS_HELLGAMES.md").write_text("\n".join(lines), encoding="utf-8")


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


def write_pdf(weapons: list[dict]) -> None:
    page_w, page_h = 1240, 1754
    margin = 70
    bg = (244, 241, 235)
    ink = (27, 25, 23)
    muted = (86, 79, 70)
    accent = (103, 35, 29)
    card = (255, 252, 246)
    line = (185, 174, 160)

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
    draw.text((margin, y), "Guia de armas", font=font_h1, fill=ink)
    y += 54
    y = draw_wrapped(
        draw,
        (margin, y),
        "Armas, municiones y trampas separadas desde los sets de iconos. Incluye jerarquia, dano, ruido, fabricacion y ubicaciones para isla completa y piloto de 4 casillas.",
        font_body,
        ink,
        page_w - 2 * margin,
        26,
    )
    y += 35
    draw.text((margin, y), "Jerarquia de amenaza", font=font_h1, fill=ink)
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
        "1 Faro: cuchillo viejo, palo de madera, pistola de bengalas.",
        "2 Campamento: navaja fina, trampa de lazo, lanza casera, arco simple, pistola sin balas.",
        "6 Monolitos: piedra filosa, dardos, lanza de estrella.",
        "7 Ruinas: palanca de hierro, pinchos ocultos, ballesta ligera, espada ceremonial.",
    ]:
        y = draw_wrapped(draw, (margin + 10, y), "- " + text, font_body, ink, page_w - 2 * margin - 20, 26)
        y += 8
    pages.append(image)

    for category in sorted({w["category"] for w in weapons}):
        category_items = [w for w in weapons if w["category"] == category]
        image, draw = new_page()
        y = 58
        draw.text((margin, y), category, font=font_h1, fill=accent)
        y += 48
        for item in category_items:
            card_h = 178
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
            draw.text((tx, y + 42), f"Nivel {item['level']} - {item['kind']} | dano {item['damage'] or '-'} | ruido {item['noise'] or '-'}", font=font_bold, fill=accent)
            yy = y + 70
            yy = draw_wrapped(draw, (tx, yy), "Fabricacion: " + item["fabrication"], font_small, ink, page_w - margin - tx - 20, 20)
            yy = draw_wrapped(draw, (tx, yy), "Uso: " + item["uses"], font_small, ink, page_w - margin - tx - 20, 20)
            draw_wrapped(draw, (tx, yy), "Piloto: " + item["pilot"], font_small, muted, page_w - margin - tx - 20, 20)
            y += card_h + 18
        pages.append(image)

    pdf_path = GUIDE_DIR / "GUIA_ARMAS_HELLGAMES.pdf"
    pages[0].save(pdf_path, save_all=True, append_images=pages[1:])


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
    sheet.save(GUIDE_DIR / "weapon_icons_contact.png")


def main() -> None:
    GUIDE_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()
    catalog = parse_weapon_catalog()
    as_input, as_output = parse_recipes()
    weapons = collect_weapons(manifest, catalog, as_input, as_output)
    write_index(manifest)
    write_json(weapons)
    write_markdown(weapons)
    write_pdf(weapons)
    write_contact_sheet()
    print(f"weapons: {len(weapons)}")
    print((GUIDE_DIR / "GUIA_ARMAS_HELLGAMES.md").resolve())
    print((GUIDE_DIR / "weapon_guide_data.json").resolve())
    print((GUIDE_DIR / "GUIA_ARMAS_HELLGAMES.pdf").resolve())


if __name__ == "__main__":
    main()
