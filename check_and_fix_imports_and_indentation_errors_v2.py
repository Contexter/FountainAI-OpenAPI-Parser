# Filename: check_and_fix_imports_and_indentation_errors_v2.py

import subprocess
import re
import os

def scan_repository():
    print("Starting scan of repository for incomplete imports and indentation errors...")

    # List to hold files with issues
    issues = []

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)

                # Attempt to compile each file and capture output
                result = subprocess.run(['python3', '-m', 'py_compile', file_path], capture_output=True, text=True)

                # Parse output for syntax, import, or indentation errors
                if result.stderr:
                    issues.append((file_path, result.stderr.strip()))

    if issues:
        print("\nDetected issues:")
        for file, error in issues:
            print(f"\nError in {file}:\n{error}\n")
    else:
        print("No incomplete imports or indentation errors found.")

    print("\nScan completed.")

if __name__ == "__main__":
    scan_repository()
