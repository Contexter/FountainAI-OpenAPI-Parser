import os
import re

# Define a list of common type hints that may be missing
common_type_hints = [
    "Any", "Dict", "List", "Optional", "Union", "Tuple", "Callable", "Set", 
    "Iterable", "Generator", "TypeVar", "Sequence", "Mapping"
]

def fix_incomplete_imports(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Flag to check if a file was modified
    modified = False

    print(f"Checking {file_path}...")  # Debugging output

    # Search for incomplete `from typing import` statements
    for i, line in enumerate(lines):
        match = re.match(r"^from typing import\s*$", line)
        if match:
            # If the import statement is empty, replace it with a complete list
            new_import_line = f"from typing import {', '.join(common_type_hints)}\n"
            lines[i] = new_import_line
            modified = True
            print(f"Fixed incomplete import in {file_path} on line {i + 1}")  # Debugging output

    # Write changes back to the file if it was modified
    if modified:
        with open(file_path, 'w') as file:
            file.writelines(lines)
        return True
    else:
        print(f"No incomplete import found in {file_path}")  # Debugging output
    return False

def scan_repository(directory):
    print("Scanning for incomplete imports in .py files...")
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                if fix_incomplete_imports(file_path):
                    print(f"Updated {file_path}")
                else:
                    print(f"No update needed for {file_path}")  # Debugging output

# Run the script on the current directory (repository root)
if __name__ == "__main__":
    repo_root = os.getcwd()
    scan_repository(repo_root)
