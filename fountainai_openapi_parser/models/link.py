from typing import Dict, Union from pydantic import RootModel

class Link(BaseModel):

operationRef: Optional[str] = None

operationId: Optional[str] = None

parameters: Optional[Dict[str, Any]] = None

requestBody: Optional[Any] = None

description: Optional[str] = None

server: Optional[Server] = None
