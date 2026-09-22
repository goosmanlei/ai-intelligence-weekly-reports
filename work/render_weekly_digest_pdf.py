#!/usr/bin/env python3
import argparse
import html
import re
from pathlib import Path


PAGE_TITLE = "全球与国内 AI 情报周报"
PRIMARY_FONT = "WeeklyAI"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    return parser.parse_args()


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


def extract_report_date(blocks):
    for block_type, text in blocks:
        if block_type != "title":
            continue
        match = re.search(r"(?:\(|（)(\d{4}-\d{2}-\d{2})(?:\)|）)", text)
        if match:
            return match.group(1)
    raise ValueError("report title must contain a YYYY-MM-DD date")


def inline_markup(text):
    """Convert the small Markdown subset used by weekly reports to ReportLab XML."""
    output = []
    cursor = 0
    token_pattern = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)|`([^`]+)`")
    for match in token_pattern.finditer(text):
        output.append(html.escape(text[cursor : match.start()], quote=False))
        if match.group(1) is not None:
            label = html.escape(match.group(1), quote=False)
            url = html.escape(match.group(2), quote=True)
            output.append(f'<link href="{url}" color="#1D4ED8"><u>{label}</u></link>')
        else:
            code = html.escape(match.group(3), quote=False)
            output.append(f'<font name="Courier" color="#334155">{code}</font>')
        cursor = match.end()
    output.append(html.escape(text[cursor:], quote=False))
    return "".join(output)


def emphasize_lead(text):
    for lead in ("主题类别：", "发生了什么：", "为什么重要：", "事实：", "判断："):
        if text.startswith(lead):
            rest = inline_markup(text[len(lead) :])
            return f'<font color="#1D4ED8">{html.escape(lead)}</font>{rest}'
    return inline_markup(text)


def resolve_font_path():
    candidates = (
        Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf"),
        Path("/System/Library/AssetsV2/com_apple_MobileAsset_Font8/53fe5be564086fefc7523ccd0a31200acf92e0e5.asset/AssetData/STHEITI.ttf"),
    )
    for path in candidates:
        if path.is_file():
            return path
    raise FileNotFoundError(
        "No supported Chinese TrueType font found; expected Arial Unicode or STHeiti"
    )


def build_styles(get_sample_style_sheet, paragraph_style, colors):
    base = get_sample_style_sheet()["Normal"]
    common = {
        "parent": base,
        "fontName": PRIMARY_FONT,
        "splitLongWords": True,
        "allowWidows": False,
        "allowOrphans": False,
    }
    return {
        "title": paragraph_style(
            "ReportTitle",
            fontSize=22.5,
            leading=29,
            textColor=colors.HexColor("#0B1F3A"),
            spaceAfter=18,
            keepWithNext=True,
            **common,
        ),
        "heading": paragraph_style(
            "SectionHeading",
            fontSize=14.5,
            leading=20,
            textColor=colors.HexColor("#164E8A"),
            spaceBefore=11,
            spaceAfter=8,
            keepWithNext=True,
            borderColor=colors.HexColor("#B9D2EA"),
            borderWidth=0,
            borderPadding=(0, 0, 4, 0),
            **common,
        ),
        "subheading": paragraph_style(
            "EntryHeading",
            fontSize=11.8,
            leading=16,
            textColor=colors.HexColor("#142B47"),
            spaceBefore=7,
            spaceAfter=4,
            keepWithNext=True,
            **common,
        ),
        "body": paragraph_style(
            "Body",
            fontSize=9.7,
            leading=15.2,
            textColor=colors.HexColor("#334155"),
            spaceAfter=5,
            **common,
        ),
        "meta": paragraph_style(
            "Meta",
            fontSize=8.7,
            leading=12.5,
            textColor=colors.HexColor("#164E8A"),
            backColor=colors.HexColor("#F2F7FC"),
            borderColor=colors.HexColor("#D5E3F0"),
            borderWidth=0.45,
            borderPadding=(4, 6, 4, 6),
            spaceAfter=6,
            keepWithNext=True,
            **common,
        ),
        "bullet": paragraph_style(
            "Bullet",
            fontSize=9.55,
            leading=14.8,
            leftIndent=15,
            firstLineIndent=-10,
            bulletIndent=0,
            bulletFontName=PRIMARY_FONT,
            bulletFontSize=7,
            textColor=colors.HexColor("#334155"),
            spaceAfter=4,
            **common,
        ),
        "summary_bullet": paragraph_style(
            "SummaryBullet",
            fontSize=9.6,
            leading=15,
            leftIndent=18,
            rightIndent=3,
            firstLineIndent=-10,
            bulletIndent=2,
            bulletFontName=PRIMARY_FONT,
            bulletFontSize=7,
            textColor=colors.HexColor("#243B53"),
            backColor=colors.HexColor("#F7FAFD"),
            borderColor=colors.HexColor("#E1EAF2"),
            borderWidth=0.35,
            borderPadding=(5, 6, 5, 6),
            spaceAfter=4,
            **common,
        ),
        "source_bullet": paragraph_style(
            "SourceBullet",
            fontSize=7.9,
            leading=10.5,
            leftIndent=14,
            firstLineIndent=-9,
            bulletIndent=0,
            bulletFontName=PRIMARY_FONT,
            bulletFontSize=6.5,
            textColor=colors.HexColor("#475569"),
            spaceAfter=0.5,
            **common,
        ),
    }


def build_story(blocks, styles, paragraph):
    story = []
    section = None
    for block_type, text in blocks:
        if block_type == "spacer":
            continue
        if block_type == "heading":
            section = text
            story.append(paragraph(inline_markup(text), styles["heading"]))
            continue
        if block_type == "title":
            story.append(paragraph(inline_markup(text), styles["title"]))
            continue
        if block_type == "subheading":
            story.append(paragraph(inline_markup(text), styles["subheading"]))
            continue
        if block_type == "body":
            style = styles["meta"] if text.startswith("主题类别：") else styles["body"]
            story.append(paragraph(emphasize_lead(text), style))
            continue
        if section == "30 秒总览":
            style = styles["summary_bullet"]
        elif section in {"来源索引", "采集说明"}:
            style = styles["source_bullet"]
        else:
            style = styles["bullet"]
        story.append(paragraph(inline_markup(text), style, bulletText="•"))
    return story


def build_pdf(input_path, output_path):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    from reportlab.platypus import Paragraph, SimpleDocTemplate

    blocks = parse_blocks(input_path.read_text(encoding="utf-8"))
    report_date = extract_report_date(blocks)
    pdfmetrics.registerFont(TTFont(PRIMARY_FONT, str(resolve_font_path())))
    styles = build_styles(getSampleStyleSheet, ParagraphStyle, colors)

    class NumberedCanvas(canvas.Canvas):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._saved_page_states = []

        def showPage(self):
            self._saved_page_states.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            page_count = len(self._saved_page_states)
            for state in self._saved_page_states:
                self.__dict__.update(state)
                self.setFillColor(colors.HexColor("#7C8A9A"))
                self.setFont(PRIMARY_FONT, 7.5)
                self.drawCentredString(A4[0] / 2, 25, f"第 {self._pageNumber} / {page_count} 页")
                super().showPage()
            super().save()

    def decorate_page(pdf_canvas, document):
        pdf_canvas.saveState()
        if document.page > 1:
            pdf_canvas.setFillColor(colors.HexColor("#7C8A9A"))
            pdf_canvas.setFont(PRIMARY_FONT, 7.5)
            pdf_canvas.drawString(document.leftMargin, A4[1] - 31, f"{PAGE_TITLE}  |  {report_date}")
            pdf_canvas.setStrokeColor(colors.HexColor("#D8E2EC"))
            pdf_canvas.setLineWidth(0.45)
            pdf_canvas.line(document.leftMargin, A4[1] - 38, A4[0] - document.rightMargin, A4[1] - 38)
        pdf_canvas.restoreState()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=47,
        rightMargin=47,
        topMargin=50,
        bottomMargin=42,
        title=f"{PAGE_TITLE}（{report_date}）",
        author="全球与国内 AI 情报周报",
        subject="全球与国内 AI 最新进展周报",
        allowSplitting=True,
    )
    story = build_story(blocks, styles, Paragraph)
    document.build(
        story,
        onFirstPage=decorate_page,
        onLaterPages=decorate_page,
        canvasmaker=NumberedCanvas,
    )


def main():
    args = parse_args()
    build_pdf(Path(args.input), Path(args.output))


if __name__ == "__main__":
    main()
