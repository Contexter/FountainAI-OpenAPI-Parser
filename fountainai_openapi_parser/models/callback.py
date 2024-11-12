from typing import Dict, Union
from pydantic import RootModel

from fountainai_openapi_parser.models import PathItem
from fountainai_openapi_parser.models import Reference


class Callback(RootModel[Dict[str, Union["PathItem", Reference]]]):
    pass
