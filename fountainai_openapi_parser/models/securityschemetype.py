    from typing import Dict, Union from pydantic import RootModel
class SecuritySchemeType(str, Enum):
    API_KEY = "apiKey"
    HTTP = "http"
    MUTUAL_TLS = "mutualTLS"
    OAUTH2 = "oauth2"
    OPENID_CONNECT = "openIdConnect"
