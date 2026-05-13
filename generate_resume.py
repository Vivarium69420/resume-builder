import json
import re
import subprocess
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# ====================
# Paths
# ====================

BASE_DIR = Path(__file__).parent

DATA_FILE = BASE_DIR / "data" / "resume.json"

TEMPLATE_DIR = BASE_DIR / "templates"
TEMPLATE_FILE = "resume.tex.j2"

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_TEX = OUTPUT_DIR / "resume.tex"

# ====================
# Keywords
# ====================

KEYWORDS = [

]

# ====================
# Helpers
# ====================

def highlight_keywords(text):
    """
    Wrap keywords with LaTeX command.

    Example:
    AUTOSAR -> \\keyword{AUTOSAR}
    """

    if not text:
        return text

    for kw in KEYWORDS:
        pattern = r"\b" + re.escape(kw) + r"\b"

        text = re.sub(
            pattern,
            r"\\keyword{" + kw + "}",
            text
        )

    return text


def process_resume_data(data):

    # Work experience highlights
    if "work" in data:
        for job in data["work"]:

            if "highlights" in job:
                job["highlights"] = [
                    highlight_keywords(bullet)
                    for bullet in job["highlights"]
                ]

            if "summary" in job:
                job["summary"] = highlight_keywords(
                    job["summary"]
                )

    # Projects
    if "projects" in data:
        for project in data["projects"]:

            if "description" in project:
                project["description"] = highlight_keywords(
                    project["description"]
                )

    # Awards
    if "awards" in data:
        for award in data["awards"]:

            if "summary" in award:
                award["summary"] = highlight_keywords(
                    award["summary"]
                )

    # Skills
    if "skills" in data:
        for skill in data["skills"]:

            if "keywords" in skill:
                skill["keywords"] = [
                    highlight_keywords(k)
                    for k in skill["keywords"]
                ]

    # Summary
    if "basics" in data and "summary" in data["basics"]:
        data["basics"]["summary"] = highlight_keywords(
            data["basics"]["summary"]
        )

    return data


# ====================
# Load Resume Data
# ====================

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

data = process_resume_data(data)

# ====================
# Jinja Environment
# ====================

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=False,
    trim_blocks=True,
    lstrip_blocks=True,

    # Prevent conflicts with LaTeX
    comment_start_string="/*",
    comment_end_string="*/",
)

template = env.get_template(TEMPLATE_FILE)

# ====================
# Render LaTeX
# ====================

rendered_tex = template.render(**data)

with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
    f.write(rendered_tex)

print(f"Generated: {OUTPUT_TEX}")

# ====================
# Compile PDF
# ====================

try:
    subprocess.run(
        [
            "xelatex",
            "-interaction=nonstopmode",
            f"-output-directory={OUTPUT_DIR}",
            str(OUTPUT_TEX),
        ],
        check=True,
    )

    print("PDF compilation successful!")

except subprocess.CalledProcessError as e:
    print("\nPDF compilation failed")
    print(e)
