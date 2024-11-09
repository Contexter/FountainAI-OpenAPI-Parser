from dataclasses import dataclass
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Example:
    summary: Optional[str] = None
    description: Optional[str] = None
    value: Optional[str] = None
    externalValue: Optional[str] = None
'''
