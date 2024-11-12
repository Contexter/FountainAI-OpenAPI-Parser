from typing import Dict, Optional
from pydantic import BaseModel


class Discriminator(BaseModel):
    propertyName: str
    mapping: Optional[Dict[str, str]] = None
