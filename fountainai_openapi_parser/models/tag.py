from typing import Optional
from pydantic import BaseModel
from fountainai_openapi_parser.models.externaldocumentation import ExternalDocumentation


class Tag(BaseModel):
    name: str
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None
