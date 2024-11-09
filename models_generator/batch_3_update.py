import os
import logging
import argparse
from pathlib import Path
from shutil import copyfile

# Configure argument parsing for log file path and dry-run mode
parser = argparse.ArgumentParser(description="Update generator scripts for Batch 3.")
parser.add_argument("--log-file", type=str, default="batch_3_update.log", help="Path to log file")
parser.add_argument("--dry-run", action="store_true", help="Show changes without writing to files")
args = parser.parse_args()

# Configure logging to file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=args.log_file,
    filemode='w'
)

# Define the models and their final fields for Batch 3
batch_3_models = {
    "Link": {
        "fields": [
            {"name": "operationId", "type": "Optional[str]", "default": "None"},
            {"name": "parameters", "type": "Optional[Dict[str, str]]", "default": "None"},
            {"name": "requestBody", "type": "Optional[str]", "default": "None"},
            {"name": "description", "type": "Optional[str]", "default": "None"},
            {"name": "server", "type": "Optional['Server']", "default": "None"}
        ]
    },
    "MediaType": {
        "fields": [
            {"name": "schema", "type": "Optional['Schema']", "default": "None"},
            {"name": "example", "type": "Optional[str]", "default": "None"},
            {"name": "examples", "type": "Optional[Dict[str, 'Example']]", "default": "None"},
            {"name": "encoding", "type": "Optional[Dict[str, 'Encoding']]", "default": "None"}
        ]
    },
    "OAuthFlows": {
        "fields": [
            {"name": "implicit", "type": "Optional['OAuthFlow']", "default": "None"},
            {"name": "password", "type": "Optional['OAuthFlow']", "default": "None"},
            {"name": "clientCredentials", "type": "Optional['OAuthFlow']", "default": "None"},
            {"name": "authorizationCode", "type": "Optional['OAuthFlow']", "default": "None"}
        ]
    },
    "OpenAPI": {
        "fields": [
            {"name": "openapi", "type": "str"},
            {"name": "info", "type": "'Info'"},
            {"name": "servers", "type": "Optional[List['Server']]", "default": "None"},
            {"name": "paths", "type": "Dict[str, 'PathItem']"},
            {"name": "components", "type": "Optional['Components']", "default": "None"},
            {"name": "security", "type": "Optional[List['SecurityRequirement']]", "default": "None"},
            {"name": "tags", "type": "Optional[List['Tag']]", "default": "None"},
            {"name": "externalDocs", "type": "Optional['ExternalDocumentation']", "default": "None"}
        ]
    },
    "Operation": {
        "fields": [
            {"name": "tags", "type": "Optional[List[str]]", "default": "None"},
            {"name": "summary", "type": "Optional[str]", "default": "None"},
            {"name": "description", "type": "Optional[str]", "default": "None"},
            {"name": "externalDocs", "type": "Optional['ExternalDocumentation']", "default": "None"},
            {"name": "operationId", "type": "Optional[str]", "default": "None"},
            {"name": "parameters", "type": "Optional[List['Parameter']]", "default": "None"},
            {"name": "requestBody", "type": "Optional['RequestBody']", "default": "None"},
            {"name": "responses", "type": "'Responses'"},
            {"name": "callbacks", "type": "Optional[Dict[str, 'Callback']]", "default": "None"},
            {"name": "deprecated", "type": "Optional[bool]", "default": "None"},
            {"name": "security", "type": "Optional[List['SecurityRequirement']]", "default": "None"},
            {"name": "servers", "type": "Optional[List['Server']]", "default": "None"}
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
    import_statements = {"Optional": "from typing import Optional", "Dict": "from typing import Dict", "List": "from typing import List"}
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

# Function to update each generator script in Batch 3
def update_batch_3_generators(dry_run=False):
    for model_name, model_data in batch_3_models.items():
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

    logging.info("Batch 3 update completed successfully.")

if __name__ == "__main__":
    update_batch_3_generators(dry_run=args.dry_run)

