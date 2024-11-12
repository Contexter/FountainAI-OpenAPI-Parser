# Filename: check_and_fix_imports_and_indentation_errors_v3.py

import subprocess
import re
import os

def scan_and_fix_file(file_path):
    """Scan a file for syntax or indentation errors and attempt to fix simple issues."""
    print(f"Checking {file_path} for issues...")
    try:
        # Try to compile the file
        result = subprocess.run(['python3', '-m', 'py_compile', file_path], capture_output=True, text=True)

        if result.stderr:
            # Detect indentation or syntax errors from compiler output
            if "IndentationError" in result.stderr or "SyntaxError" in result.stderr:
                print(f"Error detected in {file_path}:")
                print(result.stderr.strip())
                
                # Attempt to auto-fix simple indentation issues
                if "unexpected indent" in result.stderr or "unindent does not match" in result.stderr:
                    fix_indentation(file_path)
            else:
                print(f"Other error in {file_path}:")
                print(result.stderr.strip())
        else:
            print(f"No issues detected in {file_path}.")

    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def fix_indentation(file_path):
    """Attempt to fix simple indentation issues in a Python file."""
    print(f"Attempting to fix indentation in {file_path}...")
    fixed_lines = []
    indentation_level = 0

    with open(file_path, 'r') as file:
        for line in file:
            # Strip leading whitespace and reapply consistent indentation
            stripped_line = line.lstrip()
            if stripped_line:
                if stripped_line.startswith("def ") or stripped_line.startswith("class "):
                    indentation_level = 0  # Reset indentation for new definitions

                fixed_line = (' ' * (indentation_level * 4)) + stripped_line  # Apply consistent 4 spaces
                fixed_lines.append(fixed_line)

                # Update indentation level for blocks
                if stripped_line.endswith(":"):
                    indentation_level += 1
            else:
                fixed_lines.append("")  # Keep empty lines as-is

    # Write the fixed lines back to the file
    with open(file_path, 'w') as file:
        file.write("\n".join(fixed_lines))
    
    print(f"Fixed indentation for {file_path}.")

def scan_repository():
    print("Starting scan of repository for incomplete imports and indentation errors...")
    issues = []

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                scan_and_fix_file(file_path)

    print("\nScan completed.")

if __name__ == "__main__":
    scan_repository()

