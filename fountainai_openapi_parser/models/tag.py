class Tag(BaseModel):
    name: str
    description: Optional[str] = None
    externalDocs: Optional["ExternalDocumentation"] = None