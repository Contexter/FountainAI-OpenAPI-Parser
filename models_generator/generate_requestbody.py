from dataclasses import dataclass
from typing import Optional
from typing import Dict

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class RequestBody:
    description: Optional[str] = None
    content: Dict[str, 'MediaType']
    required: Optional[bool] = None
'''
