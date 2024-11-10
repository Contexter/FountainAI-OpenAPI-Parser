from typing import Union
from pathlib import Path
import yaml
import json
from .models import OpenAPI
from .utils import load_file, resolve_references
from .exceptions import ParsingError, ValidationError, ReferenceResolutionError


def parse_openapi(
    source: Union[str, Path],
    encoding: str = 'utf-8',
    resolve_references_flag: bool = True
) -> OpenAPI:
    """
    Parses an OpenAPI 3.1 document from a file path or string content.

    Args:
        source (Union[str, Path]): The file path to the OpenAPI document or the content as a string.
        encoding (str, optional): The encoding of the file if a file path is provided. Defaults to 'utf-8'.
        resolve_references_flag (bool, optional): Whether to resolve $ref references. Defaults to True.

    Returns:
        OpenAPI: An instance of the OpenAPI model representing the parsed document.

    Raises:
        ParsingError: If there is a problem parsing the document.
        ValidationError: If the document does not conform to the OpenAPI 3.1 specification.
        ReferenceResolutionError: If there is an issue resolving references in the document.
    """
    try:
        content = load_file(source, encoding)

        # Determine if the content is JSON or YAML
        if content.strip().startswith("{"):
            parsed_data = json.loads(content)
        else:
            parsed_data = yaml.safe_load(content)

        # Validate and create an OpenAPI object
        openapi_instance = OpenAPI(**parsed_data)

        # Resolve references if flag is set
        if resolve_references_flag:
            openapi_instance = resolve_references(openapi_instance)

        return openapi_instance

    except (yaml.YAMLError, json.JSONDecodeError) as e:
        raise ParsingError(f"Failed to parse the document: {str(e)}")
    except ValidationError as e:
        raise ValidationError(f"Validation error: {str(e)}")
    except ReferenceResolutionError as e:
        raise ReferenceResolutionError(f"Reference resolution error: {str(e)}")
