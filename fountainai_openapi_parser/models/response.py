from typing import Dict, Union, Optional
from pydantic import BaseModel
from fountainai_openapi_parser.models import Reference, Header, MediaType, Link


class Response(BaseModel):
    description: str
    headers: Optional[Dict[str, Union[Header, Reference]]] = None
    content: Optional[Dict[str, MediaType]] = None
    links: Optional[Dict[str, Union[Link, Reference]]] = None
