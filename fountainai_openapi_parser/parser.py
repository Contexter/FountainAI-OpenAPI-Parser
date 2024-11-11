from pydantic import BaseModel, ValidationError
from typing import Any, Dict, Union
from pathlib import Path
import yaml


class OpenAPI(BaseModel):
    openapi: str
    info: Dict[str, Any]
    paths: Dict[str, Any]


def load_file(
    source: Union[str, Path], encoding: str = "utf-8"
) -> Dict[str, Any]:
    with open(source, "r", encoding=encoding) as file:
        return yaml.safe_load(file)


def parse_openapi(
    source: Union[str, Path, Dict[str, Any]], encoding: str = "utf-8"
) -> OpenAPI:
    content = (
        source if isinstance(source, dict) else load_file(source, encoding)
    )
    try:
        return OpenAPI(**content)
    except ValidationError as e:
        raise ValueError(f"Invalid OpenAPI specification: {e}")
