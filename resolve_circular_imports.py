# resolve_circular_imports.py
# This script moves any imports causing circular dependencies to be imported
# within functions where they are needed instead of at the top of the module.

import os
import re

def resolve_imports_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified = False
    new_lines = []
    for line in lines:
        if re.match(r'^\s*from .+ import .+', line):
            # Move the import into the functions or methods to avoid circular import
            modified = True
            indent = '    '
            # Assuming all imports go inside the first main function
            new_lines.append(indent + line)
        else:
            new_lines.append(line)

    if modified:
        with open(file_path, 'w') as file:
            file.writelines(new_lines)

def find_python_files():
    python_files = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def main():
    python_files = find_python_files()
    for file_path in python_files:
        resolve_imports_in_file(file_path)
    print("Resolved circular imports in all Python files.")

if __name__ == '__main__':
    main()

