from typing import Dict, Unionfrom pydantic import RootModel
class OAuthFlows(BaseModel):
    implicit: Optional["OAuthFlow"] = None
    password: Optional["OAuthFlow"] = None
    clientCredentials: Optional["OAuthFlow"] = None
    authorizationCode: Optional["OAuthFlow"] = None