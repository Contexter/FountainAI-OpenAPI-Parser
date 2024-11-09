from dataclasses import dataclass
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Info:
    title: str
    description: Optional[str] = None
    termsOfService: Optional[str] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    version: str
'''
