from typing import Optional
from pydantic import BaseModel, AnyUrl


class ExternalDocumentation(BaseModel):
    description: Optional[str] = None
    url: AnyUrl
