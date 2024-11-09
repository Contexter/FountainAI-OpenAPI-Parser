import os
import importlib
from pathlib import Path
import logging
import sys
import py_compile

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='a')

models_dir = Path("models_generator")
sys.path.insert(0, str(models_dir.resolve()))

def validate_scripts():
    for script in models_dir.glob("*.py"):
        try:
            py_compile.compile(script, doraise=True)
        except py_compile.PyCompileError as e:
            logging.error(f"Syntax error in {script}: {e}")
            return False
    return True

def generate_models():
    # Validate generated scripts before proceeding
    if not validate_scripts():
        logging.error("Validation failed for one or more scripts. Exiting.")
        return

    # Initial content for the combined models.py file
    models_file_content = '''from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass, field
'''

    # List of component scripts to import and generate models
    components = [
        "generate_contact", "generate_license", "generate_info", "generate_server_variable",
        "generate_server", "generate_tag", "generate_external_documentation", "generate_reference",
        "generate_xml", "generate_discriminator", "generate_encoding", "generate_media_type",
        "generate_example", "generate_schema", "generate_parameter", "generate_request_body",
        "generate_response", "generate_link", "generate_header", "generate_callback",
        "generate_security_scheme", "generate_oauth_flows", "generate_operation",
        "generate_path_item", "generate_components", "generate_security_requirement",
        "generate_webhook", "generate_openapi"
    ]

    # Import each component and add its content to models.py
    for component in components:
        try:
            module = importlib.import_module(component)
            if hasattr(module, "generate_model"):
                model_content = module.generate_model()
                models_file_content += f"\n\n{model_content}"
            else:
                logging.warning(f"No generate_model function found for component: {component}")
        except ModuleNotFoundError as e:
            logging.error(f"Error importing {component}: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred while importing {component}: {e}")

    # Write combined models to models.py at the root of the project
    models_path = Path("models.py")
    models_path.write_text(models_file_content)
    logging.info(f"Generated combined models in {models_path}")

if __name__ == "__main__":
    generate_models()
