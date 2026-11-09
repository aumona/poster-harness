"""Check LaTeX layout diagnostics without additional Python dependencies."""
from pathlib import Path
import re
log = Path("output/pdf/main.log").read_text(errors="replace")
problems = re.findall(r"(?:Missing character: [^\n]*|Overfull [^\n]*|LaTeX Warning: [^\n]*|Package [^\n]*Warning:[^\n]*|! [^\n]*)", log)
pages = re.search(r"Output written on .*?\((\d+) page", log)
if not pages or pages.group(1) != "1":
    problems.append("Expected exactly one PDF page")
if problems:
    raise SystemExit("\n".join(problems))
print("PASS: one page; no overfull boxes or LaTeX/package warnings. Visually inspect the PDF before printing.")
