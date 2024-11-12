from fountainai_openapi_parser.models import Reference

from typing import Dict, Union from pydantic import RootModel

class Reference(BaseModel):

ref: str = Field(..., alias="$ref")

summary: Optional[str] = None

description: Optional[str] = None


class Config:

populate_by_name = True
