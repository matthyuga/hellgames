from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_PATH = ROOT / "data" / "prototype_runtime_4.json"
PROTOTYPE_PATH = ROOT / "data" / "prototype_island_4.json"
DEFAULT_OUTPUT_DIR = ROOT / "data" / "runs" / "maps"

TYPE_COLORS = {
    "participante": (220, 42, 42, 238),
    "lugareno": (50, 122, 235, 238),
    "criatura": (132, 60, 204, 238),
    "guardian": (246, 164, 35, 238),
    "jefe": (30, 30, 30, 245),
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_font(size: int) -> ImageFont.ImageFont:
    for name in ("arial.ttf", "segoeui.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def tactical_path(cell_id: int) -> Path:
    manifest = load_json(ROOT / "assets" / "tactical_maps" / "manifest_tactical_maps.json")
    for entry in manifest:
        if entry["scenario_id"] == cell_id:
            return ROOT / entry["grid_image"]
    raise KeyError(f"No tactical map found for scenario {cell_id}")


def parse_coord(coord: str, cell_size: int) -> tuple[int, int]:
    coord = coord.strip().upper()
    col = ord(coord[0]) - ord("A")
    row = int(coord[1:]) - 1
    return (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)


def offset_for_stack(index: int) -> tuple[int, int]:
    offsets = [
        (0, 0),
        (24, -18),
        (-24, 18),
        (24, 18),
        (-24, -18),
        (0, 28),
        (0, -28),
    ]
    return offsets[index % len(offsets)]


def draw_label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font: ImageFont.ImageFont) -> None:
    x, y = xy
    bbox = draw.textbbox((x, y), text, font=font)
    pad = 5
    draw.rounded_rectangle(
        (bbox[0] - pad, bbox[1] - pad, bbox[2] + pad, bbox[3] + pad),
        radius=6,
        fill=(18, 20, 22, 210),
    )
    draw.text((x, y), text, fill=(255, 255, 245, 245), font=font)


def draw_actor(
    draw: ImageDraw.ImageDraw,
    actor: dict,
    x: int,
    y: int,
    number: int,
    font: ImageFont.ImageFont,
) -> None:
    color = TYPE_COLORS.get(actor["type"], (245, 245, 245, 238))
    outline = (255, 255, 245, 245) if actor.get("hidden") is False else (28, 28, 28, 245)
    radius = 18 if actor["type"] != "jefe" else 23

    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline=outline, width=4)
    number_text = str(number)
    bbox = draw.textbbox((0, 0), number_text, font=font)
    draw.text(
        (x - (bbox[2] - bbox[0]) / 2, y - (bbox[3] - bbox[1]) / 2 - 1),
        number_text,
        fill=(255, 255, 255, 250),
        font=font,
    )


def render_cell(cell_id: int, actors: list[dict], output_dir: Path) -> Path:
    image_path = tactical_path(cell_id)
    image = Image.open(image_path).convert("RGBA")
    draw = ImageDraw.Draw(image, "RGBA")
    marker_font = load_font(24)
    title_font = load_font(30)
    legend_font = load_font(22)

    width, height = image.size
    # Current tactical maps are 14x14 with square cells.
    cell_size = width // 14

    draw.rounded_rectangle((14, 14, width - 14, 62), radius=8, fill=(15, 18, 20, 178))
    draw.text((28, 24), f"Casilla {cell_id} - estado piloto", fill=(255, 255, 245, 245), font=title_font)

    by_coord: dict[str, list[dict]] = defaultdict(list)
    for actor in actors:
        by_coord[actor["micro"]].append(actor)

    numbered: list[tuple[int, dict]] = []
    next_number = 1
    for coord, stack in sorted(by_coord.items()):
        base_x, base_y = parse_coord(coord, cell_size)
        for index, actor in enumerate(stack):
            dx, dy = offset_for_stack(index)
            draw_actor(draw, actor, base_x + dx, base_y + dy, next_number, marker_font)
            numbered.append((next_number, actor))
            next_number += 1

    legend_x = 18
    legend_y = height - 32 - (len(numbered) * 32)
    legend_width = 410
    legend_height = 24 + (len(numbered) * 32)
    draw.rounded_rectangle(
        (legend_x, legend_y, legend_x + legend_width, legend_y + legend_height),
        radius=8,
        fill=(15, 18, 20, 205),
    )
    for row, (number, actor) in enumerate(numbered):
        y = legend_y + 14 + row * 32
        color = TYPE_COLORS.get(actor["type"], (245, 245, 245, 238))
        draw.ellipse((legend_x + 12, y + 2, legend_x + 34, y + 24), fill=color)
        hidden = " oculto" if actor.get("hidden") else ""
        text = f"{number}. {actor['name']} ({actor['micro']}){hidden}"
        draw.text((legend_x + 44, y), text, fill=(255, 255, 245, 245), font=legend_font)

    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"prototype_state_cell_{cell_id:02d}.png"
    image.convert("RGB").save(output, quality=92)
    return output


def render_contact_sheet(paths: list[Path], output_dir: Path) -> Path:
    images = [Image.open(path).convert("RGB").resize((700, 700), Image.LANCZOS) for path in paths]
    sheet = Image.new("RGB", (1400, 1400), (20, 22, 24))
    positions = [(0, 0), (700, 0), (0, 700), (700, 700)]
    for img, pos in zip(images, positions):
        sheet.paste(img, pos)
    output = output_dir / "prototype_state_contact_sheet.png"
    sheet.save(output, quality=92)
    return output


def render_state_maps(actors: list[dict], output_dir: Path = DEFAULT_OUTPUT_DIR) -> Path:
    grouped: dict[int, list[dict]] = defaultdict(list)
    for actor in actors:
        grouped[int(actor["cell"])].append(actor)

    rendered = []
    for cell_id in (1, 2, 6, 7):
        rendered.append(render_cell(cell_id, grouped[cell_id], output_dir))
    return render_contact_sheet(rendered, output_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="Renderiza mapas de estado del prototipo Hell Games.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    runtime = load_json(RUNTIME_PATH)
    prototype = load_json(PROTOTYPE_PATH)
    base_actors = {actor["id"]: actor for actor in prototype["actors"]}
    actors = [{**base_actors.get(entry["id"], {}), **entry} for entry in runtime["actor_runtime"]]

    contact = render_state_maps(actors, args.output_dir)

    print("Mapas escritos:")
    for path in sorted(args.output_dir.glob("prototype_state_cell_*.png")):
        print(f"- {path}")
    print(f"- {contact}")


if __name__ == "__main__":
    main()
