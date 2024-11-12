# fix_import_errors.py
import os
import re

# Directory containing the problematic files
source_dir = "fountainai_openapi_parser/models"

# Mapping of classes to their respective imports (add more if needed)
required_imports = {
    "Reference": "from fountainai_openapi_parser.models import Reference",
    "PathItem": "from fountainai_openapi_parser.models import PathItem",
    # Add other missing imports if any are discovered
}

def add_import(file_path, import_statement):
    """Add import statement to file if not already present"""
    with open(file_path, "r") as file:
        content = file.read()

    if import_statement not in content:
        with open(file_path, "w") as file:
            file.write(import_statement + "\n" + content)

def fix_missing_imports():
    """Loop through source files and fix missing imports"""
    for filename in os.listdir(source_dir):
        if filename.endswith(".py"):
            file_path = os.path.join(source_dir, filename)
            with open(file_path, "r") as file:
                content = file.read()
                
            for class_name, import_statement in required_imports.items():
                # Check if class is used in the file without an import
                if re.search(rf'\b{class_name}\b', content) and import_statement not in content:
                    print(f"Adding import for {class_name} in {filename}")
                    add_import(file_path, import_statement)

if __name__ == "__main__":
    fix_missing_imports()
    print("Import errors fixed.")

