import os

# Define the models directory and required imports
models_dir = "fountainai_openapi_parser/models"
required_imports = [
    "from typing import Dict, Union",
    "from pydantic import RootModel",
]

def ensure_imports(file_path):
    """Ensure required imports are present in a given file."""
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Check if each required import is present
    missing_imports = [imp for imp in required_imports if not any(imp in line for line in lines)]

    # If there are missing imports, add them at the top
    if missing_imports:
        print(f"Adding missing imports to {file_path}")
        lines = missing_imports + ["\n"] + lines
        with open(file_path, "w") as file:
            file.writelines(lines)

# Apply the function to each Python file in the models directory
for filename in os.listdir(models_dir):
    if filename.endswith(".py"):
        file_path = os.path.join(models_dir, filename)
        ensure_imports(file_path)

print("Script completed. Missing imports were added where necessary.")

