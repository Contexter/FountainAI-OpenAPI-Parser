import os
import logging
import argparse
from pathlib import Path
from shutil import copyfile

# Configure argument parsing for log file path and dry-run mode
parser = argparse.ArgumentParser(description="Update generator scripts for Batch 5.")
parser.add_argument("--log-file", type=str, default="batch_5_update.log", help="Path to log file")
parser.add_argument("--dry-run", action="store_true", help="Show changes without writing to files")
args = parser.parse_args()

# Configure logging to file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=args.log_file,
    filemode='w'
)

# Define the models and their final fields for Batch 5
batch_5_models = {
    "Schema": {
        "fields": [
            {"name": "title", "type": "Optional[str]", "default": "None"},
            {"name": "multipleOf", "type": "Optional[int]", "default": "None"},
            {"name": "maximum", "type": "Optional[float]", "default": "None"},
            {"name": "exclusiveMaximum", "type": "Optional[bool]", "default": "None"},
            {"name": "minimum", "type": "Optional[float]", "default": "None"},
            {"name": "exclusiveMinimum", "type": "Optional[bool]", "default": "None"},
            {"name": "maxLength", "type": "Optional[int]", "default": "None"},
            {"name": "minLength", "type": "Optional[int]", "default": "None"},
            {"name": "pattern", "type": "Optional[str]", "default": "None"},
            {"name": "maxItems", "type": "Optional[int]", "default": "None"},
            {"name": "minItems", "type": "Optional[int]", "default": "None"},
            {"name": "uniqueItems", "type": "Optional[bool]", "default": "None"},
            {"name": "enum", "type": "Optional[List[Any]]", "default": "None"},
            {"name": "type", "type": "Optional[str]", "default": "None"},
            {"name": "items", "type": "Optional['Schema']", "default": "None"},
            {"name": "properties", "type": "Optional[Dict[str, 'Schema']]", "default": "None"},
            {"name": "additionalProperties", "type": "Optional[Union['Schema', bool]]", "default": "None"},
            {"name": "description", "type": "Optional[str]", "default": "None"},
            {"name": "format", "type": "Optional[str]", "default": "None"},
            {"name": "default", "type": "Optional[Any]", "default": "None"}
        ]
    },
    "SecurityRequirement": {
        "fields": [
            {"name": "requirements", "type": "Optional[Dict[str, List[str]]]", "default": "None"}
        ]
    },
    "SecurityScheme": {
        "fields": [
            {"name": "type", "type": "str"},
            {"name": "description", "type": "Optional[str]", "default": "None"},
            {"name": "name", "type": "Optional[str]", "default": "None"},
            {"name": "in_", "type": "Optional[str]", "default": "None"},  # 'in' is reserved, using 'in_'
            {"name": "scheme", "type": "Optional[str]", "default": "None"},
            {"name": "bearerFormat", "type": "Optional[str]", "default": "None"},
            {"name": "flows", "type": "Optional['OAuthFlows']", "default": "None"},
            {"name": "openIdConnectUrl", "type": "Optional[str]", "default": "None"}
        ]
    },
    "Server": {
        "fields": [
            {"name": "url", "type": "str"},
            {"name": "description", "type": "Optional[str]", "default": "None"},
            {"name": "variables", "type": "Optional[Dict[str, 'ServerVariable']]", "default": "None"}
        ]
    },
    "ServerVariable": {
        "fields": [
            {"name": "enum", "type": "Optional[List[str]]", "default": "None"},
            {"name": "default", "type": "str"},
            {"name": "description", "type": "Optional[str]", "default": "None"}
        ]
    }
}

# Ensure the models_generator directory exists at the repository root
project_root = Path(__file__).resolve().parent.parent
models_dir = project_root / "models_generator"
models_dir.mkdir(exist_ok=True)

# Function to generate the content of each generator script using a template
def create_generator_script(name, fields):
    # Manage imports based on field types
    imports = "from dataclasses import dataclass\n"
    import_statements = {"Optional": "from typing import Optional", "Dict": "from typing import Dict", "List": "from typing import List", "Union": "from typing import Union", "Any": "from typing import Any"}
    required_imports = set()

    for field in fields:
        for key, import_stmt in import_statements.items():
            if key in field["type"]:
                required_imports.add(import_stmt)
    
    imports += "\n".join(required_imports) + "\n"
    field_lines = []
    for field in fields:
        line = f"{field['name']}: {field['type']}"
        if "default" in field:
            line += f" = {field['default']}"
        field_lines.append(line)
    field_definitions = "\n    ".join(field_lines)

    template = f"""{imports}
from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class {name}:
    {field_definitions}
'''
"""
    return template

# Function to back up existing file if it exists
def backup_file(filepath):
    backup_path = filepath.with_suffix(filepath.suffix + ".bak")
    if filepath.exists():
        copyfile(filepath, backup_path)
        logging.info(f"Backed up {filepath} to {backup_path}")

# Function to update each generator script in Batch 5
def update_batch_5_generators(dry_run=False):
    for model_name, model_data in batch_5_models.items():
        try:
            generator_path = models_dir / f"generate_{model_name.lower()}.py"
            script_content = create_generator_script(model_name, model_data["fields"])
            if dry_run:
                logging.info(f"[Dry Run] Would update {generator_path} with final content for {model_name}")
                print(script_content)  # Print to console for review
            else:
                backup_file(generator_path)
                with open(generator_path, "w") as file:
                    file.write(script_content)
                logging.info(f"Updated {generator_path} with final content for {model_name}")
        except Exception as e:
            logging.error(f"Failed to update {generator_path} for {model_name}: {e}")

    logging.info("Batch 5 update completed successfully.")

if __name__ == "__main__":
    update_batch_5_generators(dry_run=args.dry_run)

