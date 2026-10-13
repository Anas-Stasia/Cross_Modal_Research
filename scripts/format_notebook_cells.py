import re
from pathlib import Path

NB_PATH = Path(r"c:\Users\RanVic\desktop\cross_modal_research\src\data_cleaning.ipynb")

text = NB_PATH.read_text(encoding="utf-8")

pattern = re.compile(r'(<VSCode.Cell[^>]*language="python">\n)(.*?)(\n</VSCode.Cell>)', re.DOTALL)

try:
    import black
except Exception:
    raise SystemExit("Black is required. Install it with: python -m pip install black")


def format_block(code):
    # Black expects a module, so ensure it ends with a newline
    formatted = black.format_str(code, mode=black.Mode())
    # Remove any leading/trailing blank lines to fit the notebook pattern
    return formatted.rstrip("\n")


def repl(m):
    header, code, footer = m.group(1), m.group(2), m.group(3)
    try:
        new_code = format_block(code)
    except Exception as e:
        print("Failed to format a code block:", e)
        return m.group(0)
    return header + new_code + footer

new_text = pattern.sub(repl, text)

if new_text != text:
    NB_PATH.write_text(new_text, encoding="utf-8")
    print("Notebook formatted and saved:", NB_PATH)
else:
    print("No changes made.")
