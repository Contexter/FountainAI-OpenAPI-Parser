from typing import Dict, Optional, Any
from pydantic import BaseModel
from fountainai_openapi_parser.models import Server


class Link(BaseModel):
    operationRef: Optional[str] = None
    operationId: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    requestBody: Optional[Any] = None
    description: Optional[str] = None
    server: Optional[Server] = None
