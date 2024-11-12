import yaml
import logging
from typing import Any, Dict, Optional
from pydantic import ValidationError
from pydantic import BaseModel, Field
from fountainai_openapi_parser.models import OpenAPI, Components, Info, Paths
from fountainai_openapi_parser.exceptions import ParsingError, ReferenceResolutionError
import codecs

# Configure logging
# Set up logging to capture errors for debugging purposes
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Define a schema validator for OpenAPI content using Pydantic
class OpenAPISchemaValidator(BaseModel):
    # The 'info' field is required and represents metadata about the API
    info: Info
    # The 'paths' field is optional and contains the available paths and operations for the API
    paths: Optional[Paths] = None
    # The 'components' field is optional and defines reusable components, such as schemas
    components: Optional[Components] = None
    # The 'servers' field is optional and lists the servers for the API
    servers: Optional[list] = Field(default_factory=list)
    # The 'tags' field is optional and provides additional documentation tags
    tags: Optional[list] = Field(default_factory=list)
    # The 'externalDocs' field is optional and provides additional external documentation
    externalDocs: Optional[Any] = None

# Function to parse OpenAPI content from a dictionary
def parse_openapi(content: Dict[str, Any]) -> OpenAPI:
    try:
        # Validate content against OpenAPISchemaValidator
        # This ensures that required fields are present and the content adheres to the expected structure
        validated_content = OpenAPISchemaValidator(**content).dict()

        # Attempt to parse the validated content as an OpenAPI object
        openapi = OpenAPI(**validated_content)
        return openapi
    except (ValidationError, ReferenceResolutionError) as e:
        # Handle validation and reference resolution errors
        # Raise a ParsingError if the input content cannot be validated as OpenAPI
        raise ParsingError(f"Invalid OpenAPI specification: {e}")
    except Exception as e:
        # Catch any other exceptions that may arise and raise a generic ParsingError
        # Log the full stack trace to help identify the root cause of unexpected errors
        logger.error("Unexpected error while parsing OpenAPI specification", exc_info=True)
        raise ParsingError(f"Unexpected error while parsing OpenAPI specification: {e}")

# Function to load OpenAPI content from a YAML string
def load_openapi_from_yaml(yaml_content: str) -> OpenAPI:
    try:
        # Load the YAML content into a Python dictionary
        # Use safe_load to avoid executing arbitrary code
        content = yaml.safe_load(yaml_content)
        if not isinstance(content, dict):
            # Ensure the loaded content is a dictionary representing the OpenAPI document
            raise ParsingError("YAML content must be a dictionary representing the OpenAPI document.")
        
        # Parse the dictionary as an OpenAPI object
        return parse_openapi(content)
    except (yaml.YAMLError, ValidationError) as e:
        # Handle YAML parsing errors and validation errors
        raise ParsingError(f"Invalid OpenAPI document structure: {e}")
    except Exception as e:
        # Catch any other exceptions that may arise
        # Log the full stack trace to help identify the root cause of unexpected errors
        logger.error("Unexpected error while loading OpenAPI from YAML", exc_info=True)
        raise ParsingError(f"Unexpected error while loading OpenAPI from YAML: {e}")

# Function to load OpenAPI content from a file
def load_openapi_from_file(file_path: str) -> OpenAPI:
    try:
        # Read the YAML content from a file using a context manager to handle BOM and different encodings
        # Using 'codecs.open' with 'utf-8-sig' ensures that files with BOM are correctly handled
        with codecs.open(file_path, 'r', encoding='utf-8-sig') as file:
            yaml_content = file.read()
        # Parse the YAML content as an OpenAPI object
        return load_openapi_from_yaml(yaml_content)
    except FileNotFoundError as e:
        # Handle file not found error
        raise ParsingError(f"File not found: {e}")
    except IOError as e:
        # Handle general I/O errors
        raise ParsingError(f"IO error while reading the file: {e}")
