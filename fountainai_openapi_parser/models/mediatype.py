from typing import Dict, Unionfrom pydantic import RootModel
class MediaType(BaseModel):
    schema_data: Optional[Union["Schema", Reference]] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Union[Example, Reference]]] = None
    encoding: Optional[Dict[str, Encoding]] = None