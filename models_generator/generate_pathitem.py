from dataclasses import dataclass
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class PathItem:
    ref: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    get: Optional['Operation'] = None
    put: Optional['Operation'] = None
    post: Optional['Operation'] = None
    delete: Optional['Operation'] = None
    options: Optional['Operation'] = None
    head: Optional['Operation'] = None
    patch: Optional['Operation'] = None
    trace: Optional['Operation'] = None
'''
