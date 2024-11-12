class Server(BaseModel):
    url: str
    description: Optional[str] = None
    variables: Optional[Dict[str, ServerVariable]] = None