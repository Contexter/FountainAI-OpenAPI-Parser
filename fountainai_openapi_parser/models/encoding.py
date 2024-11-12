from fountainai_openapi_parser.models import Reference
from typing import Dict, Union from pydantic import RootModel
class Encoding(BaseModel):
    contentType: Optional[str] = None
    headers: Optional[Dict[str, Union["Header", Reference]]] = None
    style: Optional[Style] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None