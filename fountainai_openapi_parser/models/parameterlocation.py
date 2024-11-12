from enum import Enum
from pydantic import RootModel


class ParameterLocation(str, Enum):
    QUERY = "query"
    HEADER = "header"
    PATH = "path"
    COOKIE = "cookie"
