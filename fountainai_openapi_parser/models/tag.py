    from typing import Dict, Union from pydantic import RootModel
class Tag(BaseModel):
    name: str
    description: Optional[str] = None
    externalDocs: Optional["ExternalDocumentation"] = None