from typing import Dict, Unionfrom pydantic import RootModel
class ServerVariable(BaseModel):
    enum: Optional[List[str]] = None
    default: str
    description: Optional[str] = None