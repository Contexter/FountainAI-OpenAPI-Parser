from dataclasses import dataclass
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class License:
    name: str
    url: Optional[str] = None
'''
