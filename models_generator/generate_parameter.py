from dataclasses import dataclass
from typing import Optional
from typing import Dict

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Parameter:
    name: str
    in_: str
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allowEmptyValue: Optional[bool] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None
    schema: Optional['Schema'] = None
    example: Optional[str] = None
    examples: Optional[Dict[str, 'Example']] = None
'''
