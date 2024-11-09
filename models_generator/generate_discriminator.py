from dataclasses import dataclass
from typing import Dict
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Discriminator:
    propertyName: str
    mapping: Optional[Dict[str, str]] = None
'''
