import os

def fix_import_syntax():
    """Fixes syntax issues in import statements in __init__.py files in the 'models' directory."""
    base_dir = os.path.join(os.getcwd(), "fountainai_openapi_parser", "models")
    init_file = os.path.join(base_dir, "__init__.py")

    # Check if the file exists
    if os.path.exists(init_file):
        with open(init_file, 'r') as file:
            content = file.read()

        # Correct the faulty import syntax
        corrected_content = content.replace(
            "from typing import Dict, Union from pydantic import RootModel",
            "from typing import Dict, Union\nfrom pydantic import RootModel"
        )

        with open(init_file, 'w') as file:
            file.write(corrected_content)
        print("Syntax error fixed in __init__.py")
    else:
        print(f"File {init_file} does not exist")

if __name__ == "__main__":
    fix_import_syntax()
