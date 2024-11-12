from typing import Dict, Unionfrom pydantic import RootModel
class Reference(BaseModel):
    ref: str = Field(..., alias="$ref")
    summary: Optional[str] = None
    description: Optional[str] = None

    class Config:
        populate_by_name = True