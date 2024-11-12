# fix_indentation_errors.py

import os
import re

def fix_indentation(file_path):
    """Fix indentation issues in the specified Python file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    fixed_lines = []
    for line in lines:
        # Replace tabs with 4 spaces
        fixed_line = line.replace('\t', '    ')
        
        # Remove unexpected leading spaces based on common indentation levels
        if re.match(r'^[ ]{1,3}[^ ]', fixed_line):  # Less than 4 spaces
            fixed_line = fixed_line.lstrip()
        
        fixed_lines.append(fixed_line)

    # Rewrite the file with corrected indentation
    with open(file_path, 'w') as file:
        file.writelines(fixed_lines)
    
    print(f"Fixed indentation in {file_path}")

def process_tests_directory():
    """Process all Python files in the tests directory."""
    test_dir = './tests'
    if not os.path.isdir(test_dir):
        print("The 'tests' directory does not exist.")
        return
    
    for root, _, files in os.walk(test_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                fix_indentation(file_path)

if __name__ == '__main__':
    process_tests_directory()

