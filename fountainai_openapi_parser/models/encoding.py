from typing import Dict, Optional, Union
from pydantic import BaseModel
from fountainai_openapi_parser.models import Reference, Header, Style


class Encoding(BaseModel):
    contentType: Optional[str] = None
    headers: Optional[Dict[str, Union["Header", Reference]]] = None
    style: Optional[Style] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None
