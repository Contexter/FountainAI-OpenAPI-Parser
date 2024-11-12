from typing import Optional, List
from pydantic import BaseModel


class ServerVariable(BaseModel):
    enum: Optional[List[str]] = None
    default: str
    description: Optional[str] = None
