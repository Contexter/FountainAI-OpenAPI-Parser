from typing import Dict, Union from pydantic import RootModel
class ExternalDocumentation(BaseModel):
    description: Optional[str] = None
    url: AnyUrl