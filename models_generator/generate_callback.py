from dataclasses import dataclass
from typing import Dict
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Callback:
    callback_url: str
    expression: Optional[Dict[str, str]] = None
'''
