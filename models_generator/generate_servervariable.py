from dataclasses import dataclass
from typing import List
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class ServerVariable:
    enum: Optional[List[str]] = None
    default: str
    description: Optional[str] = None
'''
