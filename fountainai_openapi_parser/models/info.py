from typing import Optional
from pydantic import BaseModel, AnyUrl
from fountainai_openapi_parser.models import Contact, License


class Info(BaseModel):
    title: str
    description: Optional[str] = None
    termsOfService: Optional[AnyUrl] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    version: str
