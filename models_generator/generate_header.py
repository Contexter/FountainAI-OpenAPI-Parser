from dataclasses import dataclass
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Header:
    description: Optional[str] = None
    required: Optional[bool] = False
    deprecated: Optional[bool] = False
'''
