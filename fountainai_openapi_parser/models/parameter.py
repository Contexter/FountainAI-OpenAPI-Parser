from fountainai_openapi_parser.models import Reference

from typing import Dict, Union from pydantic import RootModel

class Parameter(BaseModel):

name: str

in_: ParameterLocation = Field(..., alias="in")

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


class Config:

populate_by_name = True
