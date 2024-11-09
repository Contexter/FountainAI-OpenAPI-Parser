import os
import logging
from pathlib import Path

# Configure logging to file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename="cleanup_duplicate_generators.log",
    filemode='w'
)

# Set directory path for models
project_root = Path(__file__).resolve().parent
models_dir = project_root / "models_generator"

# List of duplicate files to remove, keeping the correct naming convention with underscores
duplicates_to_remove = [
    "generate_externaldocumentation.py",
    "generate_mediatype.py",
    "generate_oauthflows.py",
    "generate_pathitem.py",
    "generate_requestbody.py",
    "generate_securityrequirement.py",
    "generate_securityscheme.py",
    "generate_servervariable.py"
]

# Function to remove duplicate files
def remove_duplicates():
    for duplicate_file in duplicates_to_remove:
        duplicate_path = models_dir / duplicate_file
        if duplicate_path.exists():
            try:
                duplicate_path.unlink()  # Delete the duplicate file
                logging.info(f"Deleted duplicate file: {duplicate_file}")
                print(f"Deleted duplicate file: {duplicate_file}")
            except Exception as e:
                logging.error(f"Failed to delete {duplicate_file}: {e}")
        else:
            logging.info(f"File not found, skipping: {duplicate_file}")

if __name__ == "__main__":
    remove_duplicates()
    logging.info("Completed cleanup of duplicate generator files.")

