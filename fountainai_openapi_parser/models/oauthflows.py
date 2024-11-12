from typing import Optional
from pydantic import BaseModel
from fountainai_openapi_parser.models.oauthflow import OAuthFlow


class OAuthFlows(BaseModel):
    implicit: Optional[OAuthFlow] = None
    password: Optional[OAuthFlow] = None
    clientCredentials: Optional[OAuthFlow] = None
    authorizationCode: Optional[OAuthFlow] = None
