from pathlib import Path
import yaml
import json
from typing import Union, Dict, Any
from .exceptions import ReferenceResolutionError


def load_file(source: Union[str, Path], encoding: str = "utf-8") -> str:
    """
    Loads the content of a file from a given path or string.

    Args:
        source (Union[str, Path]): The file path or content as a string.
        encoding (str, optional): The encoding of the file if a file path is provided. Defaults to 'utf-8'.

    Returns:
        str: The content of the file.

    Raises:
        FileNotFoundError: If the provided file path does not exist.
        IOError: If there is an issue reading the file.
    """
    if isinstance(source, Path) or Path(source).exists():
        try:
            with open(source, "r", encoding=encoding) as f:
                return f.read()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {str(e)}")
        except IOError as e:
            raise IOError(f"Error reading file: {str(e)}")
    else:
        return source


def resolve_references(openapi_instance: Dict[str, Any],
                       base_path: Union[str, Path] = "") -> Dict[str, Any]:
    """
    Resolves $ref references within an OpenAPI document.

    Args:
        openapi_instance (Dict[str, Any]): The parsed OpenAPI document as a dictionary.
        base_path (Union[str, Path], optional): The base path to resolve external references. Defaults to "".

    Returns:
        Dict[str, Any]: The OpenAPI document with references resolved.

    Raises:
        ReferenceResolutionError: If there is an issue resolving references.
    """
    try:
        def resolve(node: Any, path: str = "") -> Any:
            """
            Recursively resolves references within the OpenAPI document.

            Args:
                node (Any): The current node in the OpenAPI document.
                path (str, optional): The current path of the node being resolved. Defaults to "".

            Returns:
                Any: The resolved node.
            """
            if isinstance(node, dict):
                if "$ref" in node:
                    ref = node["$ref"]
                    if ref.startswith("#/"):
                        # Local reference
                        ref_path = ref[2:].split("/")
                        resolved_node = openapi_instance
                        for part in ref_path:
                            resolved_node = resolved_node.get(part, {})
                        if not isinstance(resolved_node, dict):
                            raise ReferenceResolutionError(
                                f"Unable to resolve local reference: {ref}")
                        return resolve(resolved_node, path)
                    else:
                        # External reference
                        external_path = Path(base_path).parent / ref
                        external_content = load_file(external_path)
                        if external_path.suffix in [".yaml", ".yml"]:
                            external_data = yaml.safe_load(external_content)
                        else:
                            external_data = json.loads(external_content)
                        return resolve(external_data, str(external_path))
                else:
                    return {key: resolve(value, path + f"/{key}") for key, value in node.items()}
            elif isinstance(node, list):
                return [resolve(item, path + f"/[{i}]") for i, item in enumerate(node)]
            else:
                return node

        return resolve(openapi_instance)

    except Exception as e:
        raise ReferenceResolutionError(f"Failed to resolve references: {str(e)}")
