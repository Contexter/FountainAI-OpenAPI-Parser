from dataclasses import dataclass
from typing import Dict
from typing import Union
from typing import Any
from typing import List
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Schema:
    title: Optional[str] = None
    multipleOf: Optional[int] = None
    maximum: Optional[float] = None
    exclusiveMaximum: Optional[bool] = None
    minimum: Optional[float] = None
    exclusiveMinimum: Optional[bool] = None
    maxLength: Optional[int] = None
    minLength: Optional[int] = None
    pattern: Optional[str] = None
    maxItems: Optional[int] = None
    minItems: Optional[int] = None
    uniqueItems: Optional[bool] = None
    enum: Optional[List[Any]] = None
    type: Optional[str] = None
    items: Optional['Schema'] = None
    properties: Optional[Dict[str, 'Schema']] = None
    additionalProperties: Optional[Union['Schema', bool]] = None
    description: Optional[str] = None
    format: Optional[str] = None
    default: Optional[Any] = None
'''
