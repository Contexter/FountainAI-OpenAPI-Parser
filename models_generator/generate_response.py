from dataclasses import dataclass
from typing import Optional
from typing import Dict

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Response:
    description: str
    headers: Optional[Dict[str, 'Header']] = None
    content: Optional[Dict[str, 'MediaType']] = None
    links: Optional[Dict[str, 'Link']] = None
'''
