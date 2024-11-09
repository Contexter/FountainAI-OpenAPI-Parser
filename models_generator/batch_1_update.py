import os
import logging
import argparse
from pathlib import Path
from shutil import copyfile

# Configure argument parsing for log file path and dry-run mode
parser = argparse.ArgumentParser(description="Update generator scripts for Batch 1.")
parser.add_argument("--log-file", type=str, default="batch_1_update.log", help="Path to log file")
parser.add_argument("--dry-run", action="store_true", help="Show changes without writing to files")
args = parser.parse_args()

# Configure logging to file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=args.log_file,
    filemode='w'
)

# Define the models and their final fields for Batch 1
batch_1_models = {
    "Contact": {
        "fields": [
            {"name": "name", "type": "Optional[str]", "default": "None"},
            {"name": "url", "type": "Optional[str]", "default": "None"},
            {"name": "email", "type": "Optional[str]", "default": "None"}
        ]
    },
    "ExternalDocumentation": {
        "fields": [
            {"name": "url", "type": "str"},
            {"name": "description", "type": "Optional[str]", "default": "None"}
        ]
    },
    "Header": {
        "fields": [
            {"name": "description", "type": "Optional[str]", "default": "None"},
            {"name": "required", "type": "Optional[bool]", "default": "False"},
            {"name": "deprecated", "type": "Optional[bool]", "default": "False"}
        ]
    },
    "Info": {
        "fields": [
            {"name": "title", "type": "str"},
            {"name": "description", "type": "Optional[str]", "default": "None"},
            {"name": "termsOfService", "type": "Optional[str]", "default": "None"},
            {"name": "contact", "type": "Optional[Contact]", "default": "None"},
            {"name": "license", "type": "Optional[License]", "default": "None"},
            {"name": "version", "type": "str"}
        ]
    },
    "License": {
        "fields": [
            {"name": "name", "type": "str"},
            {"name": "url", "type": "Optional[str]", "default": "None"}
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
    if any("Optional" in field["type"] for field in fields):
        imports += "from typing import Optional\n"
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

# Function to update each generator script in Batch 1
def update_batch_1_generators(dry_run=False):
    for model_name, model_data in batch_1_models.items():
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

    logging.info("Batch 1 update completed successfully.")

if __name__ == "__main__":
    update_batch_1_generators(dry_run=args.dry_run)
