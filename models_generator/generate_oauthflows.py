from dataclasses import dataclass
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class OAuthFlows:
    implicit: Optional['OAuthFlow'] = None
    password: Optional['OAuthFlow'] = None
    clientCredentials: Optional['OAuthFlow'] = None
    authorizationCode: Optional['OAuthFlow'] = None
'''
