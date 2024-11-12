from typing import Dict, Unionfrom pydantic import RootModel
class ParameterLocation(str, Enum):
    QUERY = "query"
    HEADER = "header"
    PATH = "path"
    COOKIE = "cookie"