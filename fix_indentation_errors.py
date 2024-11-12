# fix_indentation_errors.py
import os
import re

def fix_indentation(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove inconsistent indentations
    fixed_lines = []
    for line in lines:
        # Replace tabs with four spaces (standard Python indentation)
        fixed_line = re.sub(r'^\t+', ' ' * 4, line)
        fixed_lines.append(fixed_line)
    
    # Write the fixed lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(fixed_lines)

    print(f"Fixed indentation in {file_path}")

def main():
    test_dir = os.path.join(os.getcwd(), "tests")
    for root, _, files in os.walk(test_dir):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    # Attempt to import the module to see if there are indentation errors
                    with open(file_path, 'r') as f:
                        code = f.read()
                        compile(code, file_path, 'exec')
                except IndentationError:
                    print(f"Indentation error found in {file_path}, attempting to fix...")
                    fix_indentation(file_path)
                except Exception as e:
                    # Log other errors but do not attempt to fix them
                    print(f"Skipping {file_path} due to a non-indentation error: {e}")

if __name__ == "__main__":
    main()
