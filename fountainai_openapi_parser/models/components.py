    from fountainai_openapi_parser.models import PathItem
    from fountainai_openapi_parser.models import Reference
    from typing import Dict, Union from pydantic import RootModel
class Components(BaseModel):
    schemas: Optional[Dict[str, Union[Schema, Reference]]] = None
    responses: Optional[Dict[str, Union[Response, Reference]]] = None
    parameters: Optional[Dict[str, Union[Parameter, Reference]]] = None
    examples: Optional[Dict[str, Union[Example, Reference]]] = None
    requestBodies: Optional[Dict[str, Union[RequestBody, Reference]]] = None
    headers: Optional[Dict[str, Union[Header, Reference]]] = None
    securitySchemes: Optional[Dict[str, Union[SecurityScheme, Reference]]] = None
    links: Optional[Dict[str, Union[Link, Reference]]] = None
    callbacks: Optional[Dict[str, Union[Callback, Reference]]] = None
    pathItems: Optional[Dict[str, Union[PathItem, Reference]]] = None
