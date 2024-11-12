class License(BaseModel):
    name: str
    identifier: Optional[str] = None
    url: Optional[AnyUrl] = None