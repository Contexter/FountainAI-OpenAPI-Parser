from typing import Dict, Union, Optional, Any
from pydantic import BaseModel
from fountainai_openapi_parser.models import Reference, Style, Schema, Example, MediaType


class Header(BaseModel):
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allowEmptyValue: Optional[bool] = None
    style: Optional[Style] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None
    schema_data: Optional[Union[Schema, Reference]] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Union[Example, Reference]]] = None
    content: Optional[Dict[str, MediaType]] = None
