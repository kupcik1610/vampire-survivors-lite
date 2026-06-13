"""Convert each curriculum markdown -> a styled HTML -> PDF (via headless Chrome).

Maintainer tool — a learner never needs to run this.
Needs:  pip install markdown pygments
Run from the repo root:  ./venv/bin/python curriculum/build_pdf.py
"""
import markdown
import pathlib
import subprocess

HERE = pathlib.Path(__file__).parent

# Every curriculum file to turn into a PDF. Add more here and they'll all build.
DOCS = ["Curriculum-JavaScript", "Curriculum-Python"]


def build(stem):
    md_text = (HERE / f"{stem}.md").read_text()

    # Convert markdown (with code fences, tables) to an HTML fragment.
    body = markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "codehilite", "toc"],
        extension_configs={"codehilite": {"noclasses": True, "pygments_style": "friendly"}},
    )

    # Wrap it in a printable, nicely-styled page.
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
  @page {{ size: A4; margin: 18mm 16mm; }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #1d1d27;
    max-width: 100%;
  }}
  h1 {{
    font-size: 23pt; color: #2a2a40; margin: 0 0 4pt;
    border-bottom: 3px solid #5a7bd4; padding-bottom: 6pt;
  }}
  h2 {{
    font-size: 15pt; color: #34406b; margin: 22pt 0 6pt;
    padding-top: 6pt; border-top: 1px solid #e2e2ec;
    page-break-after: avoid;
  }}
  h3 {{ font-size: 12pt; color: #4a4a66; margin: 14pt 0 4pt; page-break-after: avoid; }}
  p, li {{ margin: 4pt 0; }}
  strong {{ color: #2a2a40; }}
  hr {{ border: none; border-top: 1px solid #e2e2ec; margin: 16pt 0; }}
  a {{ color: #3a5bbf; text-decoration: none; }}

  /* Inline code */
  code {{
    font-family: "SF Mono", "Menlo", Consolas, monospace;
    font-size: 9.5pt;
    background: #eef0f6;
    padding: 1px 5px;
    border-radius: 4px;
    color: #b2295a;
  }}
  /* Code blocks */
  pre {{
    background: #1e1e2e;
    border-radius: 7px;
    padding: 11pt 13pt;
    overflow-x: auto;
    line-height: 1.45;
    page-break-inside: avoid;
    border: 1px solid #2c2c44;
  }}
  pre code {{
    background: none;
    color: #e6e6f0;
    padding: 0;
    font-size: 9pt;
  }}

  /* Tables */
  table {{ border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 10pt; }}
  th, td {{ border: 1px solid #d4d4e0; padding: 5pt 8pt; text-align: left; vertical-align: top; }}
  th {{ background: #eef0f6; color: #34406b; }}

  blockquote {{
    margin: 8pt 0; padding: 6pt 12pt;
    background: #f5f7fb; border-left: 3px solid #5a7bd4;
    color: #444; font-size: 10pt;
  }}
  ul, ol {{ padding-left: 20pt; }}
</style>
</head>
<body>
{body}
</body>
</html>
"""

    html_path = HERE / f"{stem}.html"
    html_path.write_text(html)

    pdf_path = HERE / f"{stem}.pdf"
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.run([
        chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}", html_path.as_uri(),
    ], check=True)

    html_path.unlink()   # the .html was just a stepping stone to the PDF
    print("Wrote", pdf_path)


for stem in DOCS:
    build(stem)
