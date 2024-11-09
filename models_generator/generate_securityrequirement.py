from dataclasses import dataclass
from typing import List
from typing import Dict
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class SecurityRequirement:
    requirements: Optional[Dict[str, List[str]]] = None
'''
