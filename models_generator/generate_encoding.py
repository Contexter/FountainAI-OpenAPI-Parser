from dataclasses import dataclass
from typing import Dict
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Encoding:
    contentType: Optional[str] = None
    headers: Optional[Dict[str, 'Header']] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None
'''
