import yaml
import logging
import codecs

# Configure logging
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
        validated_content = OpenAPISchemaValidator(**content).dict()
        # Attempt to parse the validated content as an OpenAPI object
        openapi = OpenAPI(**validated_content)
        return openapi
    except (ValidationError, ReferenceResolutionError) as e:
        # Raise a ParsingError if the input content cannot be validated as OpenAPI
        raise ParsingError(f"Invalid OpenAPI specification: {e}")
    except Exception as e:
        # Log and raise a generic ParsingError for unexpected errors
        logger.error("Unexpected error while parsing OpenAPI specification", exc_info=True)
        raise ParsingError(f"Unexpected error while parsing OpenAPI specification: {e}")

# Function to load OpenAPI content from a YAML string


def load_openapi_from_yaml(yaml_content: str) -> OpenAPI:
    try:
        # Load the YAML content into a Python dictionary
        content = yaml.safe_load(yaml_content)
        if not isinstance(content, dict):
            # Ensure the loaded content is a dictionary representing the OpenAPI document
            raise ParsingError(
                "YAML content must be a dictionary representing the OpenAPI document.")
        # Parse the dictionary as an OpenAPI object
        return parse_openapi(content)
    except (yaml.YAMLError, ValidationError) as e:
        raise ParsingError(f"Invalid OpenAPI document structure: {e}")
    except Exception as e:
        logger.error("Unexpected error while loading OpenAPI from YAML", exc_info=True)
        raise ParsingError(f"Unexpected error while loading OpenAPI from YAML: {e}")

# Function to load OpenAPI content from a file


def load_openapi_from_file(file_path: str) -> OpenAPI:
    try:
        # Read the YAML content from a file, handling BOM and different encodings
        with codecs.open(file_path, 'r', encoding='utf-8-sig') as file:
            yaml_content = file.read()
        # Parse the YAML content as an OpenAPI object
        return load_openapi_from_yaml(yaml_content)
    except FileNotFoundError as e:
        raise ParsingError(f"File not found: {e}")
    except IOError as e:
        raise ParsingError(f"IO error while reading the file: {e}")
