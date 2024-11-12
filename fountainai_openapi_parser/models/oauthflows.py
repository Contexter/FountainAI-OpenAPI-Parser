from typing import Dict, Union from pydantic import RootModel
class OAuthFlows(BaseModel):
    implicit: Optional["OAuthFlow"] = None
    password: Optional["OAuthFlow"] = None
    clientCredentials: Optional["OAuthFlow"] = None
    authorizationCode: Optional["OAuthFlow"] = None