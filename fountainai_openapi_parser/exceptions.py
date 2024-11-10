class ParsingError(Exception):
    """
    Raised when an error occurs during parsing of the OpenAPI document.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ValidationError(Exception):
    """
    Raised when the OpenAPI document fails validation.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ReferenceResolutionError(Exception):
    """
    Raised when there is an issue resolving $ref references in the OpenAPI document.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

