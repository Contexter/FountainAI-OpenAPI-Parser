from pydantic import RootModel
class Callback(RootModel[Dict[str, Union["PathItem", Reference]]]):
    pass