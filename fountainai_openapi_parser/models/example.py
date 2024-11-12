class Example(BaseModel):
    summary: Optional[str] = None
    description: Optional[str] = None
    value: Optional[Any] = None
    externalValue: Optional[AnyUrl] = None