class OAuthFlow(BaseModel):
    authorizationUrl: Optional[AnyUrl] = None
    tokenUrl: Optional[AnyUrl] = None
    refreshUrl: Optional[AnyUrl] = None
    scopes: Dict[str, str]