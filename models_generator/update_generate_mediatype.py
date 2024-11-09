import logging
from pathlib import Path
from shutil import copyfile

# Configure logging to file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename="update_generate_mediatype.log",
    filemode='w'
)

# Define the fields for the MediaType component
media_type_fields = [
    {"name": "schema", "type": "Optional['Schema']", "default": "None"},
    {"name": "example", "type": "Optional[str]", "default": "None"},
    {"name": "examples", "type": "Optional[Dict[str, 'Example']]", "default": "None"},
    {"name": "encoding", "type": "Optional[Dict[str, 'Encoding']]", "default": "None"}
]

# Set directory path for models
project_root = Path(__file__).resolve().parent
models_dir = project_root / "models_generator"
models_dir.mkdir(exist_ok=True)
generator_file = models_dir / "generate_mediatype.py"
backup_file = generator_file.with_suffix(".py.bak")

# Function to create generator content for MediaType
def create_media_type_content():
    imports = "from dataclasses import dataclass\n"
    imports += "from typing import Optional, Dict\n\n"
    imports += "from generate_common_imports import *\n\n"

    field_definitions = "\n    ".join(
        [f"{field['name']}: {field['type']} = {field.get('default', '')}" for field in media_type_fields]
    )

    return f"""{imports}
def generate_model():
    return '''
@dataclass
class MediaType:
    {field_definitions}
'''
"""

# Function to update generate_mediatype.py
def update_generate_mediatype():
    try:
        # Backup existing file if it exists
        if generator_file.exists():
            copyfile(generator_file, backup_file)
            logging.info(f"Backed up {generator_file} to {backup_file}")

        # Write the correct content to generate_mediatype.py
        content = create_media_type_content()
        with open(generator_file, "w") as f:
            f.write(content)
        logging.info(f"Updated {generator_file} with correct MediaType content.")
    except Exception as e:
        logging.error(f"Failed to update {generator_file}: {e}")

if __name__ == "__main__":
    update_generate_mediatype()
    logging.info("Completed updating generate_mediatype.py.")

