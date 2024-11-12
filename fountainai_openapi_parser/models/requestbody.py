from typing import Dict, Unionfrom pydantic import RootModel
class RequestBody(BaseModel):
    description: Optional[str] = None
    content: Dict[str, MediaType]
    required: Optional[bool] = None