"""Convert PDF/DOCX/PPTX/XLSX in a folder to Markdown copies under <root>/_md/, mirroring paths.

Usage: python convert_to_md.py <root>
Originals are left untouched. Prints one status line per file.
"""
import re
import sys
from datetime import date
from pathlib import Path

import fitz
import mammoth
import openpyxl
import pptx
from markdownify import markdownify

ROOT = Path(sys.argv[1]).resolve()
OUT = ROOT / "_md"
EXTS = {".pdf", ".docx", ".pptx", ".xlsx"}


# Thai fonts in some PDFs store shifted vowel/tone glyphs in the Private Use Area (U+F700-F71A).
THAI_PUA = dict(zip(range(0xF700, 0xF71B), (
    "ฐิีึื่้๊๋์่้๊๋์"
    "ญั็่้๊๋์ฺุูํ"
)))
THAI_MARK = "ัิ-ฺ็-๎"


def fix_thai(text):
    text = text.translate(THAI_PUA)
    # stray glyph-mapping junk (š ę Ě �) right after Thai characters
    text = re.sub("(?<=[฀-๿])[šęĚ�]+", "", text)
    # duplicated combining marks (e.g. ดููแล -> ดูแล); Thai never repeats the same mark
    text = re.sub(f"([{THAI_MARK}])\\1+", r"\1", text)
    # junk that only became adjacent to Thai once the marks around it were cleaned
    return re.sub("(?<=[฀-๿])[šęĚ�]+", "", text)


def cell(v):
    if v is None:
        return ""
    return str(v).replace("|", "\\|").replace("\r", " ").replace("\n", "<br>").strip()


def md_table(rows):
    rows = [r for r in rows if any(c != "" for c in r)]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
    lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(lines)


def conv_pdf(p):
    doc = fitz.open(p)
    pages = doc.page_count
    parts, chars = [], 0
    for i, pg in enumerate(doc, 1):
        text = pg.get_text("text", sort=True).strip()
        chars += len(text)
        parts.append(f"## Page {i}\n\n{text}")
    doc.close()
    note = ""
    if pages and chars / pages < 100:
        note = "> **Warning:** little or no text layer (likely scanned or image-based). Content below may be incomplete.\n\n"
    return note + "\n\n".join(parts), f"{pages} pages{' — LOW TEXT' if note else ''}"


def conv_docx(p):
    drop_images = mammoth.images.img_element(lambda image: {"alt": "image omitted", "src": ""})
    with open(p, "rb") as f:
        html = mammoth.convert_to_html(f, convert_image=drop_images).value
    body = markdownify(html, heading_style="ATX", bullets="-")
    body = re.sub(r"!\[image omitted\]\(\)", "*[image omitted]*", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body, ""


def conv_pptx(p):
    prs = pptx.Presentation(p)
    out = []
    for i, slide in enumerate(prs.slides, 1):
        out.append(f"## Slide {i}")
        for shape in slide.shapes:
            if shape.has_text_frame:
                text = "\n".join(par.text for par in shape.text_frame.paragraphs if par.text.strip())
                if text:
                    out.append(text)
            if getattr(shape, "has_table", False) and shape.has_table:
                rows = [[cell(c.text) for c in r.cells] for r in shape.table.rows]
                out.append(md_table(rows))
            if shape.shape_type == 13:
                out.append("*[image omitted]*")
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text.strip()
            if notes:
                out.append("**Speaker notes:** " + notes)
    return "\n\n".join(out), f"{len(prs.slides)} slides"


def conv_xlsx(p):
    wb = openpyxl.load_workbook(p, data_only=True, read_only=True)
    out = []
    for ws in wb.worksheets:
        rows = [[cell(v) for v in r] for r in ws.iter_rows(values_only=True)]
        out.append(f"## Sheet: {ws.title}\n\n" + (md_table(rows) or "*(empty)*"))
    n = len(wb.worksheets)
    wb.close()
    return "\n\n".join(out), f"{n} sheets"


CONVERTERS = {".pdf": conv_pdf, ".docx": conv_docx, ".pptx": conv_pptx, ".xlsx": conv_xlsx}

for src in sorted(ROOT.rglob("*")):
    if not src.is_file() or src.suffix.lower() not in EXTS:
        continue
    if OUT in src.parents or src.name.startswith("~$"):
        continue
    rel = src.relative_to(ROOT)
    dst = OUT / rel.parent / (src.name + ".md")
    if dst.exists() and dst.stat().st_mtime > src.stat().st_mtime:
        print(f"SKIP\t{rel}\talready converted")
        continue
    try:
        body, info = CONVERTERS[src.suffix.lower()](src)
    except Exception as e:
        print(f"FAIL\t{rel}\t{type(e).__name__}: {e}")
        continue
    header = (
        f"# {src.name}\n\n"
        f"*Auto-converted to Markdown on {date.today():%d %b %Y} from `{rel}`. "
        f"Images are omitted and layout may be lost; the original file is authoritative.*\n\n---\n\n"
    )
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(header + fix_thai(body), encoding="utf-8")
    print(f"OK\t{rel}\t{info}\t{len(body):,} chars")
