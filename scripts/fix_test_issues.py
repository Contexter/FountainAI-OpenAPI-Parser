import os
import yaml
import logging
from pydantic import ValidationError
from fountainai_openapi_parser.parser import OpenAPI
from fountainai_openapi_parser.utils import load_file

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_file_exists(filepath):
    """Check if the necessary file exists in the directory."""
    if not os.path.exists(filepath):
        logging.error(f"Required file missing: {filepath}")
        return False
    logging.info(f"File found: {filepath}")
    return True


def validate_openapi_structure(filepath):
    """Validate the structure of the OpenAPI YAML file for compatibility with
    Pydantic."""
    try:
        with open(filepath, "r") as file:
            openapi_data = yaml.safe_load(file)
        openapi_instance = OpenAPI(**openapi_data)
        logging.info(f"OpenAPI structure in {filepath} is valid.")
    except ValidationError as e:
        logging.error(f"Validation error in {filepath}: {e}")
    except yaml.YAMLError as e:
        logging.error(f"YAML parsing error in {filepath}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in validating {filepath}: {e}")


def resolve_external_references(filepath, ref_path):
    """Load and check external references for existence and compatibility."""
    try:
        external_content = load_file(ref_path)
        logging.info(f"External reference {ref_path} loaded successfully.")
    except FileNotFoundError as e:
        logging.error(f"Missing external reference file: {e}")
    except Exception as e:
        logging.error(
            f"Unexpected error in resolving reference {ref_path}: {e}"
        )


def main():
    # Paths to necessary files
    openapi_file = "tests/data/openapi.yaml"
    external_ref_file = "tests/data/external_schema.yaml"

    # Check for presence of required files
    if check_file_exists(openapi_file):
        validate_openapi_structure(openapi_file)
    if check_file_exists(external_ref_file):
        resolve_external_references(openapi_file, external_ref_file)


if __name__ == "__main__":
    main()
