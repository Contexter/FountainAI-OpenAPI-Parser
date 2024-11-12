

class XML(BaseModel):
    name: Optional[str] = None
    namespace: Optional[AnyUrl] = None
    prefix: Optional[str] = None
    attribute: Optional[bool] = None
    wrapped: Optional[bool] = None
