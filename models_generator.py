import os
from pathlib import Path
import importlib
import logging
import sys
import py_compile

# Configure logging for better error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='a')

# Step 1: Create the 'models_generator' directory
# This directory will hold all the scripts responsible for generating individual data models
models_dir = Path("models_generator")
models_dir.mkdir(exist_ok=True)

# Step 2: Create reusable imports script
# This script contains common imports used by all data model scripts to avoid redundancy
common_imports_content = """from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass, field
"""
(common_imports_path := models_dir / "generate_common_imports.py").write_text(common_imports_content)

# Step 3: Create individual scripts for each component
# Each component script will generate a specific data model following OpenAPI 3.1 specifications
component_scripts = [
    ("generate_contact.py", "Contact"),
    ("generate_license.py", "License"),
    ("generate_info.py", "Info"),
    ("generate_server_variable.py", "ServerVariable"),
    ("generate_server.py", "Server"),
    ("generate_tag.py", "Tag"),
    ("generate_external_documentation.py", "ExternalDocumentation"),
    ("generate_reference.py", "Reference"),
    ("generate_xml.py", "XML"),
    ("generate_discriminator.py", "Discriminator"),
    ("generate_encoding.py", "Encoding"),
    ("generate_media_type.py", "MediaType"),
    ("generate_example.py", "Example"),
    ("generate_schema.py", "Schema"),
    ("generate_parameter.py", "Parameter"),
    ("generate_request_body.py", "RequestBody"),
    ("generate_response.py", "Response"),
    ("generate_link.py", "Link"),
    ("generate_header.py", "Header"),
    ("generate_callback.py", "Callback"),
    ("generate_security_scheme.py", "SecurityScheme"),
    ("generate_oauth_flows.py", "OAuthFlows"),
    ("generate_operation.py", "Operation"),
    ("generate_path_item.py", "PathItem"),
    ("generate_components.py", "Components"),
    ("generate_security_requirement.py", "SecurityRequirement"),
    ("generate_webhook.py", "Webhook"),
    ("generate_openapi.py", "OpenAPI"),
]

for script_name, model_name in component_scripts:
    # Each script defines a dataclass model with the name corresponding to the component
    script_content = f"""from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class {model_name}:
    # Define fields based on OpenAPI 3.1 specification
    pass
'''
"""
    (models_dir / script_name).write_text(script_content)

# Step 4: Create the main orchestration script
# This script orchestrates the generation of all models by importing and executing individual scripts
# The resulting models.py will contain all the dataclass definitions with fields yet to be implemented.
# After running this script, the models.py file will look like a series of dataclass placeholders for each OpenAPI component.
# To complete the implementation, you need to add the actual fields to each dataclass based on OpenAPI 3.1 specifications.
# 
# NOTE: This is a two-step process:
# 1. Run 'models_generator.py' to create individual component scripts and the 'generate_models.py' script.
# 2. Navigate to 'models_generator' and run 'generate_models.py' to generate the combined 'models.py'.
orchestration_script_content = """import os
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
"""
(models_dir / "generate_models.py").write_text(orchestration_script_content)

# Print confirmation message
logging.info("Scripts for generating data models have been successfully created.")
