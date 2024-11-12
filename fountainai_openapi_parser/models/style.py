from typing import Dict, Union from pydantic import RootModel

class Style(str, Enum):

MATRIX = "matrix"

LABEL = "label"

FORM = "form"

SIMPLE = "simple"

SPACE_DELIMITED = "spaceDelimited"

PIPE_DELIMITED = "pipeDelimited"

DEEP_OBJECT = "deepObject"
