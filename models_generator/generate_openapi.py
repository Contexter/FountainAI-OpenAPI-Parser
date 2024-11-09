from dataclasses import dataclass
from typing import Dict
from typing import Optional
from typing import List

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class OpenAPI:
    openapi: str
    info: 'Info'
    servers: Optional[List['Server']] = None
    paths: Dict[str, 'PathItem']
    components: Optional['Components'] = None
    security: Optional[List['SecurityRequirement']] = None
    tags: Optional[List['Tag']] = None
    externalDocs: Optional['ExternalDocumentation'] = None
'''
