from dataclasses import dataclass
from typing import Optional
from typing import Dict

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class MediaType:
    schema: Optional['Schema'] = None
    example: Optional[str] = None
    examples: Optional[Dict[str, 'Example']] = None
    encoding: Optional[Dict[str, 'Encoding']] = None
'''
