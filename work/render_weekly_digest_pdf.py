#!/usr/bin/env python3
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PAGE_WIDTH = 1240
PAGE_HEIGHT = 1754
MARGIN_X = 90
MARGIN_Y = 90
CONTENT_WIDTH = PAGE_WIDTH - MARGIN_X * 2


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    return parser.parse_args()


def load_fonts():
    font_path = "/System/Library/Fonts/Hiragino Sans GB.ttc"
    return {
        "title": ImageFont.truetype(font_path, 42),
        "heading": ImageFont.truetype(font_path, 28),
        "subheading": ImageFont.truetype(font_path, 24),
        "body": ImageFont.truetype(font_path, 22),
        "bullet": ImageFont.truetype(font_path, 22),
        "meta": ImageFont.truetype(font_path, 16),
    }


def wrap_text(draw, text, font, max_width):
    if not text:
        return [""]
    lines = []
    current = ""
    for char in text:
        candidate = current + char
        bbox = draw.textbbox((0, 0), candidate, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def parse_blocks(text):
    blocks = []
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            blocks.append(("spacer", ""))
        elif line.startswith("# "):
            blocks.append(("title", line[2:].strip()))
        elif line.startswith("## "):
            blocks.append(("heading", line[3:].strip()))
        elif line.startswith("### "):
            blocks.append(("subheading", line[4:].strip()))
        elif line.startswith("- "):
            blocks.append(("bullet", line[2:].strip()))
        else:
            blocks.append(("body", line.strip()))
    return blocks


def render_pages(blocks, fonts):
    pages = []
    style_map = {
        "title": (fonts["title"], 18),
        "heading": (fonts["heading"], 12),
        "subheading": (fonts["subheading"], 10),
        "body": (fonts["body"], 8),
        "bullet": (fonts["bullet"], 6),
    }

    measurement_image = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), "white")
    measurement_draw = ImageDraw.Draw(measurement_image)
    layouts = []
    for block_type, text in blocks:
        if block_type == "spacer":
            layouts.append({"type": block_type, "text": text, "height": 12})
            continue
        font, gap = style_map[block_type]
        prefix = "• " if block_type == "bullet" else ""
        lines = wrap_text(measurement_draw, prefix + text, font, CONTENT_WIDTH)
        line_height = measurement_draw.textbbox((0, 0), "测试Ag", font=font)[3] + gap
        layouts.append(
            {
                "type": block_type,
                "text": text,
                "font": font,
                "lines": lines,
                "line_height": line_height,
                "height": len(lines) * line_height + 10,
            }
        )

    image = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), "white")
    draw = ImageDraw.Draw(image)
    y = MARGIN_Y
    page_bottom = PAGE_HEIGHT - MARGIN_Y - 24

    def start_new_page():
        nonlocal image, draw, y
        pages.append(image)
        image = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), "white")
        draw = ImageDraw.Draw(image)
        y = MARGIN_Y

    def following_content_height(index, count):
        height = 0
        found = 0
        for layout in layouts[index + 1 :]:
            if layout["type"] == "spacer":
                continue
            height += layout["height"]
            found += 1
            if found >= count:
                break
        return height

    for index, layout in enumerate(layouts):
        block_type = layout["type"]
        if block_type == "spacer":
            y += layout["height"]
            continue

        reserve = 0
        if block_type in {"title", "heading"}:
            reserve = following_content_height(index, 1)
        elif block_type == "subheading":
            reserve = following_content_height(index, 2)
        elif block_type == "bullet" and index + 1 < len(layouts):
            next_layout = layouts[index + 1]
            if next_layout["type"] == "body" and next_layout["text"].startswith("http"):
                reserve = next_layout["height"]

        if y + layout["height"] + reserve > page_bottom:
            start_new_page()

        fill = "#111827" if block_type in {"title", "heading", "subheading"} else "#374151"
        for line in layout["lines"]:
            draw.text((MARGIN_X, y), line, font=layout["font"], fill=fill)
            y += layout["line_height"]
        y += 6

    pages.append(image)

    page_count = len(pages)
    for page_number, page in enumerate(pages, start=1):
        page_draw = ImageDraw.Draw(page)
        if page_number > 1:
            page_draw.text(
                (MARGIN_X, 42),
                "全球与国内 AI 情报周报 | 2026-08-03",
                font=fonts["meta"],
                fill="#9CA3AF",
            )
            page_draw.line(
                (MARGIN_X, 70, PAGE_WIDTH - MARGIN_X, 70),
                fill="#E5E7EB",
                width=1,
            )
        footer = f"第 {page_number} / {page_count} 页"
        footer_width = page_draw.textbbox((0, 0), footer, font=fonts["meta"])[2]
        page_draw.text(
            ((PAGE_WIDTH - footer_width) / 2, PAGE_HEIGHT - 54),
            footer,
            font=fonts["meta"],
            fill="#9CA3AF",
        )
    return pages


def main():
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    text = input_path.read_text(encoding="utf-8")
    fonts = load_fonts()
    pages = render_pages(parse_blocks(text), fonts)
    rgb_pages = [page.convert("RGB") for page in pages]
    rgb_pages[0].save(
        output_path,
        "PDF",
        save_all=True,
        append_images=rgb_pages[1:],
        resolution=150.0,
    )


if __name__ == "__main__":
    main()
