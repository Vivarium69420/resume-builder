# LaTeX Resume Builder

A lightweight and customizable resume builder using Python, Jinja2, and LaTeX (XeLaTeX).  
The project generates a professional ATS-friendly PDF resume from structured JSON data.

---

## Features

- JSON-based resume content management
- Jinja2-powered LaTeX templating
- Automatic PDF generation using XeLaTeX
- Keyword highlighting for ATS optimization
- Clean and customizable LaTeX styling
- Modular project structure
- Unicode support via XeLaTeX

---

## Project Structure

```text
resume-builder/
│
├── data/
│   └── resume.json
│
├── templates/
│   └── resume.tex.j2
│
├── output/
│   ├── resume.tex
│   └── resume.pdf
│
├── generate_resume.py
├── requirements.txt
└── README.md
```

---

## Requirements

### System Dependencies

Install the following tools before running the project:

- Python 3.9+
- XeLaTeX (TeX Live or MacTeX)

### macOS

Install MacTeX:

```bash
brew install --cask mactex
```

Verify installation:

```bash
xelatex --version
```

### Ubuntu/Debian

```bash
sudo apt update

sudo apt install texlive-xetex texlive-fonts-recommended texlive-latex-extra
```

### Windows

Install:

- MiKTeX: https://miktex.org/
or
- TeX Live: https://www.tug.org/texlive/

Make sure `xelatex` is available in PATH.

---

## Python Dependencies

Install dependencies:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
Jinja2
```

---

## Environment Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>

cd resume-builder
```

### 2. Create Virtual Environment (Recommended)

#### macOS/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

#### Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Resume Configuration

All resume data is stored inside:

```text
data/resume.json
```

### Example Sections

- Basics
- Professional Summary
- Education
- Work Experience
- Projects
- Skills
- Awards

---

## Professional Summary

Example:

```json
"summary": "Embedded Software Engineer with experience in automotive ECU development and AUTOSAR-based systems."
```

The summary appears below the resume header automatically.

---

## Keyword Highlighting

The project supports automatic highlighting of important keywords.

Defined in:

```python
KEYWORDS = [
    "AUTOSAR",
    "CAN",
    "UDS",
    "ASPICE",
    "ISO 26262",
]
```

Keywords are rendered in bold small caps using:

```latex
\keyword{AUTOSAR}
```

---

## Generate Resume

Run:

```bash
python3 generate_resume.py
```

Generated files:

```text
output/resume.tex
output/resume.pdf
```

---

## How It Works

### Step 1 — Load Resume JSON

The script loads structured resume data from:

```text
data/resume.json
```

### Step 2 — Process Keywords

The script scans:
- Work experience
- Projects
- Skills
- Awards
- Summary

and automatically highlights configured keywords.

### Step 3 — Render LaTeX Template

Jinja2 renders:

```text
templates/resume.tex.j2
```

into:

```text
output/resume.tex
```

### Step 4 — Compile PDF

XeLaTeX compiles the final PDF resume.

---

## Customization

### Change Font

Modify:

```latex
\setmainfont{Times New Roman}
```

inside:

```text
templates/resume.tex.j2
```

### Adjust Margins

```latex
\usepackage[a4paper,margin=0.7in]{geometry}
```

### Modify Section Styling

```latex
\titleformat{\section}
{\large\scshape}
{}
{0em}
{}[\titlerule]
```

---

## Recommended Improvements

Possible future upgrades:

- Multiple resume themes
- Dark mode PDF theme
- Automatic LinkedIn export
- YAML support
- Docker support
- CI/CD PDF generation
- GitHub Actions integration
- Multi-language resume support

---

## Common Issues

### XeLaTeX Not Found

Error:

```text
FileNotFoundError: xelatex
```

Fix:
- Ensure TeX distribution is installed
- Verify `xelatex` is in PATH

### Font Errors

If `Times New Roman` is unavailable:

Replace:

```latex
\setmainfont{Times New Roman}
```

with:

```latex
\setmainfont{TeX Gyre Termes}
```

### PDF Compilation Failed

Check generated:

```text
output/resume.log
```

for detailed LaTeX errors.

---

## Example Command Workflow

```bash
source .venv/bin/activate

python3 generate_resume.py
```

---

## Technologies Used

- Python
- Jinja2
- LaTeX
- XeLaTeX

---

## License

MIT License

---

## Author

Mai Hai Dang
