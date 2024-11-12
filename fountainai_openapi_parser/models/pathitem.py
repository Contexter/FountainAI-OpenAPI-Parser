    from fountainai_openapi_parser.models import PathItem
    from fountainai_openapi_parser.models import Reference
    from typing import Dict, Union from pydantic import RootModel
class PathItem(BaseModel):
    ref: Optional[str] = Field(default=None, alias="$ref")
    summary: Optional[str] = None
    description: Optional[str] = None
    get: Optional[Operation] = None
    put: Optional[Operation] = None
    post: Optional[Operation] = None
    delete: Optional[Operation] = None
    options: Optional[Operation] = None
    head: Optional[Operation] = None
    patch: Optional[Operation] = None
    trace: Optional[Operation] = None
    servers: Optional[List[Server]] = None
    parameters: Optional[List[Union[Parameter, Reference]]] = None

    class Config:
        populate_by_name = True
