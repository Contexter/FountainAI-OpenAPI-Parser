from dataclasses import dataclass
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class SecurityScheme:
    type: str
    description: Optional[str] = None
    name: Optional[str] = None
    in_: Optional[str] = None
    scheme: Optional[str] = None
    bearerFormat: Optional[str] = None
    flows: Optional['OAuthFlows'] = None
    openIdConnectUrl: Optional[str] = None
'''
