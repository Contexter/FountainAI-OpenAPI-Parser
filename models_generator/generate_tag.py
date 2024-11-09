from dataclasses import dataclass
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Tag:
    name: str
    description: Optional[str] = None
    externalDocs: Optional['ExternalDocumentation'] = None
'''
