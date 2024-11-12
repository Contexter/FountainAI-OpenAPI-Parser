from typing import Dict, Unionfrom pydantic import RootModel
class License(BaseModel):
    name: str
    identifier: Optional[str] = None
    url: Optional[AnyUrl] = None