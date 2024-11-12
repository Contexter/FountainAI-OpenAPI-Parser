import os
import autopep8
import flake8.api.legacy as flake8
import ast
import re

TARGET_DIRECTORY = "fountainai_openapi_parser"

# Function to run autopep8 on a file


def run_autopep8(file_path):
    with open(file_path, 'r') as file:
        original_code = file.read()
    formatted_code = autopep8.fix_code(original_code, options={'max_line_length': 100})
    with open(file_path, 'w') as file:
        file.write(formatted_code)
    print(f"Ran autopep8 on {file_path}")

# Function to check a file with flake8


def run_flake8(file_path):
    style_guide = flake8.get_style_guide(ignore=["E203", "W503"], max_line_length=100)
    report = style_guide.check_files([file_path])
    if report.total_errors > 0:
        print(f"Checked {file_path} with flake8, found {report.total_errors} issues.")
    else:
        print(f"Checked {file_path} with flake8, found 0 issues.")

# Function to remove unused imports from a file


def remove_unused_imports(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    tree = ast.parse("".join(content), filename=file_path)
    imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
    imports += [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]

    modified_content = content[:]
    for item in imports:
        if not re.search(rf"\b{item}\b", "".join(content)):
            modified_content = [line for line in modified_content if item not in line]

    with open(file_path, 'w') as file:
        file.writelines(modified_content)
    print(f"Removed unused imports in {file_path}")

# Function to replace wildcard imports with specific imports


def replace_wildcard_imports(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    tree = ast.parse("".join(content), filename=file_path)
    modified_content = content[:]
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.names[0].name == '*':
            module = node.module
            if module:
                module_path = os.path.join(TARGET_DIRECTORY, *module.split(".")) + ".py"
                if os.path.exists(module_path):
                    with open(module_path, 'r') as mod_file:
                        mod_tree = ast.parse(mod_file.read())
                        imports = [
                            n.name for n in ast.walk(mod_tree)
                            if isinstance(n, ast.FunctionDef) or isinstance(n, ast.ClassDef)
                        ]
                        specific_imports = ', '.join(imports)
                        modified_content = [
                            line.replace(f'from {module} import *', f'from {module} import {specific_imports}')
                            if 'import *' in line else line
                            for line in modified_content
                        ]

    with open(file_path, 'w') as file:
        file.writelines(modified_content)
    print(f"Replaced wildcard imports in {file_path}")

# Main function to process all files


def fix_all_files():
    for root, _, files in os.walk(TARGET_DIRECTORY):
        for file_name in files:
            if file_name.endswith(".py"):
                file_path = os.path.join(root, file_name)
                run_autopep8(file_path)
                run_flake8(file_path)
                remove_unused_imports(file_path)
                replace_wildcard_imports(file_path)


# Run the script
if __name__ == "__main__":
    fix_all_files()
