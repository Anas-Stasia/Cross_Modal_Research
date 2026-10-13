from pathlib import Path
import re

NB_PATH = Path(r"c:\Users\RanVic\desktop\cross_modal_research\src\data_cleaning.ipynb")
text = NB_PATH.read_text(encoding="utf-8")

pattern = re.compile(r'(<VSCode.Cell[^>]*language="python">\n)(.*?)(\n</VSCode.Cell>)', re.DOTALL)

changed = False

def process_code_block(code):
    global changed
    lines = code.splitlines()
    new_lines = []
    for line in lines:
        # replace tabs with 4 spaces and trim trailing spaces
        new_line = line.replace('\t', '    ').rstrip()
        new_lines.append(new_line)
    new_code = "\n".join(new_lines)
    if new_code != code:
        changed = True
    return new_code


def repl(m):
    header, code, footer = m.group(1), m.group(2), m.group(3)
    new_code = process_code_block(code)
    return header + new_code + footer

new_text = pattern.sub(repl, text)

if changed:
    NB_PATH.write_text(new_text, encoding="utf-8")
    print(f"Reindented Python cells in: {NB_PATH}")
else:
    print("No changes needed; notebook already normalized.")
