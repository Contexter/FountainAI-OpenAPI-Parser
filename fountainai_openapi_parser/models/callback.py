    from fountainai_openapi_parser.models import PathItem
    from fountainai_openapi_parser.models import Reference
    from typing import Dict, Union
    from pydantic import RootModel
class Callback(RootModel[Dict[str, Union["PathItem", Reference]]]):
    pass
