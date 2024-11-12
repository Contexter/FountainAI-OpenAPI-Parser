from typing import Dict, Union from pydantic import RootModel

class License(BaseModel):

name: str

identifier: Optional[str] = None

url: Optional[AnyUrl] = None
