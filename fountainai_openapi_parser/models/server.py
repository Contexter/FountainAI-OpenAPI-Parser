from typing import Dict, Optional
from pydantic import BaseModel
from fountainai_openapi_parser.models.servervariable import ServerVariable


class Server(BaseModel):
    url: str
    description: Optional[str] = None
    variables: Optional[Dict[str, ServerVariable]] = None
