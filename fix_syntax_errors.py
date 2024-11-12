#!/usr/bin/env python3

import os
import re

def fix_syntax_error_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    fixed_lines = []
    syntax_fixed = False

    # Pattern to find the "Union from" typo and correct it
    for line in lines:
        # Fix the "Union from" issue
        corrected_line = re.sub(r"(Union from)", "Union from", line)
        if corrected_line != line:
            syntax_fixed = True
            print(f"Fixing syntax error in {file_path}: {line.strip()} -> {corrected_line.strip()}")
        fixed_lines.append(corrected_line)

    # Write back the changes only if any fix was made
    if syntax_fixed:
        with open(file_path, 'w') as file:
            file.writelines(fixed_lines)
        print(f"Syntax error fixed in {file_path}")
    else:
        print(f"No syntax error found in {file_path}")

def find_and_fix_syntax_errors(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(subdir, file)
                fix_syntax_error_in_file(file_path)

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.dirname(__file__))
    print(f"Scanning project directory for syntax errors: {project_root}")
    find_and_fix_syntax_errors(project_root)
    print("Script completed.")

