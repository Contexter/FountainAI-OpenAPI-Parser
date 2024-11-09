from dataclasses import dataclass
from typing import Dict
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Components:
    schemas: Optional[Dict[str, 'Schema']] = None
    responses: Optional[Dict[str, 'Response']] = None
    parameters: Optional[Dict[str, 'Parameter']] = None
    examples: Optional[Dict[str, 'Example']] = None
    requestBodies: Optional[Dict[str, 'RequestBody']] = None
'''
