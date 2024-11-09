from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass, field



@dataclass
class Contact:
    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None



@dataclass
class License:
    name: str
    url: Optional[str] = None



@dataclass
class Info:
    title: str
    description: Optional[str] = None
    termsOfService: Optional[str] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    version: str



@dataclass
class ServerVariable:
    # Define fields based on OpenAPI 3.1 specification
    pass



@dataclass
class Server:
    url: str
    description: Optional[str] = None
    variables: Optional[Dict[str, 'ServerVariable']] = None



@dataclass
class Tag:
    name: str
    description: Optional[str] = None
    externalDocs: Optional['ExternalDocumentation'] = None



@dataclass
class ExternalDocumentation:
    # Define fields based on OpenAPI 3.1 specification
    pass



@dataclass
class Reference:
    ref: str



@dataclass
class XML:
    name: Optional[str] = None
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    attribute: Optional[bool] = None
    wrapped: Optional[bool] = None



@dataclass
class Discriminator:
    propertyName: str
    mapping: Optional[Dict[str, str]] = None



@dataclass
class Encoding:
    contentType: Optional[str] = None
    headers: Optional[Dict[str, 'Header']] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None



@dataclass
class MediaType:
    # Define fields based on OpenAPI 3.1 specification
    pass



@dataclass
class Example:
    summary: Optional[str] = None
    description: Optional[str] = None
    value: Optional[str] = None
    externalValue: Optional[str] = None



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



@dataclass
class Parameter:
    name: str
    in_: str
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allowEmptyValue: Optional[bool] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None
    schema: Optional['Schema'] = None
    example: Optional[str] = None
    examples: Optional[Dict[str, 'Example']] = None



@dataclass
class RequestBody:
    # Define fields based on OpenAPI 3.1 specification
    pass



@dataclass
class Response:
    description: str
    headers: Optional[Dict[str, 'Header']] = None
    content: Optional[Dict[str, 'MediaType']] = None
    links: Optional[Dict[str, 'Link']] = None



@dataclass
class Link:
    operationId: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    requestBody: Optional[str] = None
    description: Optional[str] = None
    server: Optional['Server'] = None



@dataclass
class Header:
    description: Optional[str] = None
    required: Optional[bool] = False
    deprecated: Optional[bool] = False



@dataclass
class Callback:
    callback_url: str
    expression: Optional[Dict[str, str]] = None



@dataclass
class SecurityScheme:
    # Define fields based on OpenAPI 3.1 specification
    pass



@dataclass
class OAuthFlows:
    # Define fields based on OpenAPI 3.1 specification
    pass



@dataclass
class Operation:
    tags: Optional[List[str]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    externalDocs: Optional['ExternalDocumentation'] = None
    operationId: Optional[str] = None
    parameters: Optional[List['Parameter']] = None
    requestBody: Optional['RequestBody'] = None
    responses: 'Responses'
    callbacks: Optional[Dict[str, 'Callback']] = None
    deprecated: Optional[bool] = None
    security: Optional[List['SecurityRequirement']] = None
    servers: Optional[List['Server']] = None



@dataclass
class PathItem:
    # Define fields based on OpenAPI 3.1 specification
    pass



@dataclass
class Components:
    schemas: Optional[Dict[str, 'Schema']] = None
    responses: Optional[Dict[str, 'Response']] = None
    parameters: Optional[Dict[str, 'Parameter']] = None
    examples: Optional[Dict[str, 'Example']] = None
    requestBodies: Optional[Dict[str, 'RequestBody']] = None



@dataclass
class SecurityRequirement:
    # Define fields based on OpenAPI 3.1 specification
    pass



@dataclass
class Webhook:
    event: str
    callbackUrl: str
    description: Optional[str] = None



@dataclass
class OpenAPI:
    openapi: str
    info: 'Info'
    servers: Optional[List['Server']] = None
    paths: Dict[str, 'PathItem']
    components: Optional['Components'] = None
    security: Optional[List['SecurityRequirement']] = None
    tags: Optional[List['Tag']] = None
    externalDocs: Optional['ExternalDocumentation'] = None
