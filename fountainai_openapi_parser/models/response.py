    from fountainai_openapi_parser.models import Reference
    from typing import Dict, Union from pydantic import RootModel
class Response(BaseModel):
    description: str
    headers: Optional[Dict[str, Union["Header", Reference]]] = None
    content: Optional[Dict[str, MediaType]] = None
    links: Optional[Dict[str, Union["Link", Reference]]] = None