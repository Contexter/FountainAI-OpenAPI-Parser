from dataclasses import dataclass
from typing import Dict
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Server:
    url: str
    description: Optional[str] = None
    variables: Optional[Dict[str, 'ServerVariable']] = None
'''
