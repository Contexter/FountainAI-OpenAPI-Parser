from typing import Optional
from pydantic import BaseModel, AnyUrl


class License(BaseModel):
    name: str
    identifier: Optional[str] = None
    url: Optional[AnyUrl] = None
