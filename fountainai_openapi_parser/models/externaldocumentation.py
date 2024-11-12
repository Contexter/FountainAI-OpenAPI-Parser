from typing import Dict, Unionfrom pydantic import RootModel
class ExternalDocumentation(BaseModel):
    description: Optional[str] = None
    url: AnyUrl