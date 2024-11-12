# fix_indentation_issues.py
import os

def fix_indentation_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    fixed_lines = []
    for line in lines:
        stripped_line = line.lstrip()
        indent_level = len(line) - len(stripped_line)
        
        # Adjust indentation to be a multiple of 4 spaces
        corrected_indent = ' ' * (indent_level // 4 * 4)
        fixed_lines.append(corrected_indent + stripped_line)
    
    with open(file_path, 'w') as file:
        file.writelines(fixed_lines)
    print(f"Fixed indentation in {file_path}")

def fix_indentation_in_tests():
    tests_dir = 'tests'  # specify the directory containing test files
    for root, dirs, files in os.walk(tests_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                fix_indentation_in_file(file_path)

if __name__ == "__main__":
    fix_indentation_in_tests()

