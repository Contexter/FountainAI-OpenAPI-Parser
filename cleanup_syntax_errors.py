# save as `cleanup_syntax_errors.py` at the root
import re
import os

def fix_import_syntax(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()

    # Fix inline import errors and misplaced commas
    fixed_lines = []
    for line in lines:
        # Move imports like 'from typing import Dict, Union from pydantic import RootModel' to separate lines
        if re.search(r"from .+ import .+ from .+ import .+", line):
            parts = line.split("from")
            fixed_lines.extend([f"from {part.strip()}" for part in parts if part.strip()])
        else:
            fixed_lines.append(line)

    with open(filepath, "w") as file:
        file.writelines(fixed_lines)

# Walk through all .py files
for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            fix_import_syntax(os.path.join(root, file))

