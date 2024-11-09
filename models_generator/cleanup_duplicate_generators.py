import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename="cleanup_duplicate_generators.log",
    filemode='w'
)

# Absolute path to the project root and models_generator
project_root = Path(__file__).resolve().parent
models_dir = project_root / "models_generator"

# List of duplicates to remove
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

def remove_duplicates():
    for duplicate_file in duplicates_to_remove:
        duplicate_path = models_dir / duplicate_file
        # Confirm file exists before deletion
        if duplicate_path.is_file():
            try:
                duplicate_path.unlink()  # Delete the file
                logging.info(f"Deleted duplicate file: {duplicate_path}")
                print(f"Deleted duplicate file: {duplicate_path}")
            except Exception as e:
                logging.error(f"Error deleting {duplicate_path}: {e}")
                print(f"Error deleting {duplicate_path}: {e}")
        else:
            logging.info(f"File not found, skipping: {duplicate_path}")
            print(f"File not found, skipping: {duplicate_path}")

if __name__ == "__main__":
    remove_duplicates()
    logging.info("Duplicate file cleanup complete.")
