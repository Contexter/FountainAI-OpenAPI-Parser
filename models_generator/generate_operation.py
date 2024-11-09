from dataclasses import dataclass
from typing import Dict
from typing import Optional
from typing import List

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Operation:
    tags: Optional[List[str]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    externalDocs: Optional['ExternalDocumentation'] = None
    operationId: Optional[str] = None
    parameters: Optional[List['Parameter']] = None
    requestBody: Optional['RequestBody'] = None
    responses: 'Responses'
    callbacks: Optional[Dict[str, 'Callback']] = None
    deprecated: Optional[bool] = None
    security: Optional[List['SecurityRequirement']] = None
    servers: Optional[List['Server']] = None
'''
