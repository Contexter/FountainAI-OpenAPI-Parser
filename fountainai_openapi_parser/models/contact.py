from typing import Optional
from pydantic import BaseModel, AnyUrl, EmailStr


class Contact(BaseModel):
    name: Optional[str] = None
    url: Optional[AnyUrl] = None
    email: Optional[EmailStr] = None
