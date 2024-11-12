    from fountainai_openapi_parser.models import Reference
    from typing import Dict, Union from pydantic import RootModel
class Operation(BaseModel):
    tags: Optional[List[str]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None
    operationId: Optional[str] = None
    parameters: Optional[List[Union[Parameter, Reference]]] = None
    requestBody: Optional[Union[RequestBody, Reference]] = None
    responses: Dict[str, Union[Response, Reference]]
    callbacks: Optional[Dict[str, Union[Callback, Reference]]] = None
    deprecated: Optional[bool] = None
    security: Optional[List[Dict[str, List[str]]]] = None  # SecurityRequirements
    servers: Optional[List[Server]] = None
