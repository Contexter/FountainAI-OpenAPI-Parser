from typing import Optional
from pydantic import BaseModel, Field, AnyUrl
from fountainai_openapi_parser.models import SecuritySchemeType, ParameterLocation, OAuthFlows


class SecurityScheme(BaseModel):
    type: SecuritySchemeType
    description: Optional[str] = None
    name: Optional[str] = None
    in_: Optional[ParameterLocation] = Field(default=None, alias="in")
    scheme: Optional[str] = None
    bearerFormat: Optional[str] = None
    flows: Optional[OAuthFlows] = None
    openIdConnectUrl: Optional[AnyUrl] = None

    class Config:
        populate_by_name = True
