from typing import Dict, Unionfrom pydantic import RootModel
class Contact(BaseModel):
    name: Optional[str] = None
    url: Optional[AnyUrl] = None
    email: Optional[EmailStr] = None