from typing import Dict, Optional
from pydantic import BaseModel
from fountainai_openapi_parser.models.mediatype import MediaType


class RequestBody(BaseModel):
    description: Optional[str] = None
    content: Dict[str, MediaType]
    required: Optional[bool] = None
