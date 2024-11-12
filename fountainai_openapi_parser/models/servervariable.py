class ServerVariable(BaseModel):
    enum: Optional[List[str]] = None
    default: str
    description: Optional[str] = None