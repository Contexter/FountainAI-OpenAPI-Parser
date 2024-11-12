from typing import Dict, Unionfrom pydantic import RootModel
class Discriminator(BaseModel):
    propertyName: str
    mapping: Optional[Dict[str, str]] = None