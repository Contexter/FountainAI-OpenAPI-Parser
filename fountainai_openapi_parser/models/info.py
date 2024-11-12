class Info(BaseModel):
    title: str
    description: Optional[str] = None
    termsOfService: Optional[AnyUrl] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    version: str