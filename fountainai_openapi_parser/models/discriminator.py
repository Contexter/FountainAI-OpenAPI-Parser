    from typing import Dict, Union from pydantic import RootModel
class Discriminator(BaseModel):
    propertyName: str
    mapping: Optional[Dict[str, str]] = None
