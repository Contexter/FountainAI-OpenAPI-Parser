from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass
from enum import Enum

# Define Enums for fields that use predefined values
class ParameterLocation(Enum):
    QUERY = "query"
    HEADER = "header"
    PATH = "path"
    COOKIE = "cookie"

class Style(Enum):
    MATRIX = "matrix"
    LABEL = "label"
    FORM = "form"
    SIMPLE = "simple"
    SPACE_DELIMITED = "spaceDelimited"
    PIPE_DELIMITED = "pipeDelimited"
    DEEP_OBJECT = "deepObject"

class SecuritySchemeType(Enum):
    API_KEY = "apiKey"
    HTTP = "http"
    MUTUAL_TLS = "mutualTLS"
    OAUTH2 = "oauth2"
    OPENID_CONNECT = "openIdConnect"

# Contact information for the exposed API
@dataclass
class Contact:
    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None

# License information for the exposed API
@dataclass
class License:
    name: str
    identifier: Optional[str] = None  # Added 'identifier' field
    url: Optional[str] = None

# General information about the API
@dataclass
class Info:
    title: str
    description: Optional[str] = None
    termsOfService: Optional[str] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    version: str

# Variable substitutions for server URL template
@dataclass
class ServerVariable:
    enum: Optional[List[str]] = None
    default: str
    description: Optional[str] = None

# An object representing a Server
@dataclass
class Server:
    url: str
    description: Optional[str] = None
    variables: Optional[Dict[str, ServerVariable]] = None

# Additional external documentation
@dataclass
class ExternalDocumentation:
    description: Optional[str] = None
    url: str

# Allows adding meta-data to a single tag
@dataclass
class Tag:
    name: str
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None

# A simple object to allow referencing other components
@dataclass
class Reference:
    ref: str  # Corresponds to $ref
    summary: Optional[str] = None  # Added 'summary' field
    description: Optional[str] = None  # Added 'description' field

# A metadata object that allows for more fine-tuned XML model definitions
@dataclass
class XML:
    name: Optional[str] = None
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    attribute: Optional[bool] = None
    wrapped: Optional[bool] = None

# Adds support for polymorphism and inheritance
@dataclass
class Discriminator:
    propertyName: str
    mapping: Optional[Dict[str, str]] = None

# A single encoding definition applied to a single schema property
@dataclass
class Encoding:
    contentType: Optional[str] = None
    headers: Optional[Dict[str, Union['Header', Reference]]] = None
    style: Optional[Style] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None

# An example of the media type
@dataclass
class Example:
    summary: Optional[str] = None
    description: Optional[str] = None
    value: Optional[Any] = None
    externalValue: Optional[str] = None

# Each Media Type object provides schema and examples for the media type identified by its key
@dataclass
class MediaType:
    schema: Optional[Union['Schema', Reference]] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Union[Example, Reference]]] = None
    encoding: Optional[Dict[str, Encoding]] = None

# The Schema Object allows the definition of input and output data types
@dataclass
class Schema:
    # Reference
    ref: Optional[str] = None  # Corresponds to $ref

    # Metadata
    title: Optional[str] = None
    description: Optional[str] = None
    default: Optional[Any] = None
    deprecated: Optional[bool] = None
    readOnly: Optional[bool] = None
    writeOnly: Optional[bool] = None
    examples: Optional[List[Any]] = None

    # String-specific properties
    type: Optional[Union[str, List[str]]] = None
    format: Optional[str] = None
    maxLength: Optional[int] = None
    minLength: Optional[int] = None
    pattern: Optional[str] = None
    contentMediaType: Optional[str] = None
    contentEncoding: Optional[str] = None
    contentSchema: Optional['Schema'] = None

    # Number-specific properties
    multipleOf: Optional[float] = None
    maximum: Optional[float] = None
    exclusiveMaximum: Optional[float] = None
    minimum: Optional[float] = None
    exclusiveMinimum: Optional[float] = None

    # Array-specific properties
    items: Optional[Union['Schema', List['Schema']]] = None
    prefixItems: Optional[List['Schema']] = None
    contains: Optional['Schema'] = None
    maxItems: Optional[int] = None
    minItems: Optional[int] = None
    uniqueItems: Optional[bool] = None
    maxContains: Optional[int] = None
    minContains: Optional[int] = None
    unevaluatedItems: Optional[Union['Schema', bool]] = None

    # Object-specific properties
    properties: Optional[Dict[str, 'Schema']] = None
    patternProperties: Optional[Dict[str, 'Schema']] = None
    additionalProperties: Optional[Union['Schema', bool]] = None
    maxProperties: Optional[int] = None
    minProperties: Optional[int] = None
    required: Optional[List[str]] = None
    dependentRequired: Optional[Dict[str, List[str]]] = None
    dependentSchemas: Optional[Dict[str, 'Schema']] = None
    propertyNames: Optional['Schema'] = None
    unevaluatedProperties: Optional[Union['Schema', bool]] = None

    # Conditional and logical keywords
    allOf: Optional[List['Schema']] = None
    anyOf: Optional[List['Schema']] = None
    oneOf: Optional[List['Schema']] = None
    not_: Optional['Schema'] = None  # Use 'not_' to avoid keyword conflict
    if_: Optional['Schema'] = None  # Use 'if_' to avoid keyword conflict
    then: Optional['Schema'] = None
    else_: Optional['Schema'] = None  # Use 'else_' to avoid keyword conflict

    # Enumeration and constant values
    enum: Optional[List[Any]] = None
    const: Optional[Any] = None

    # Discriminator for polymorphism
    discriminator: Optional[Discriminator] = None

    # XML model definitions
    xml: Optional[XML] = None

    # External documentation
    externalDocs: Optional[ExternalDocumentation] = None

    # Example value
    example: Optional[Any] = None

# Describes a single operation parameter
@dataclass
class Parameter:
    name: str
    in_: ParameterLocation  # Use 'in_' to avoid keyword conflict
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allowEmptyValue: Optional[bool] = None
    style: Optional[Style] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None
    schema: Optional[Union[Schema, Reference]] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Union[Example, Reference]]] = None
    content: Optional[Dict[str, MediaType]] = None

# Describes a single request body
@dataclass
class RequestBody:
    description: Optional[str] = None
    content: Dict[str, MediaType]
    required: Optional[bool] = None

# Describes a single response from an API Operation
@dataclass
class Response:
    description: str
    headers: Optional[Dict[str, Union['Header', Reference]]] = None
    content: Optional[Dict[str, MediaType]] = None
    links: Optional[Dict[str, Union['Link', Reference]]] = None

# The Link object represents a possible design-time link for a response
@dataclass
class Link:
    operationRef: Optional[str] = None
    operationId: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    requestBody: Optional[Any] = None
    description: Optional[str] = None
    server: Optional[Server] = None

# Header follows the structure of the Parameter Object with some changes
@dataclass
class Header:
    description: Optional[str] = None
    required: Optional[bool] = False
    deprecated: Optional[bool] = False
    style: Optional[Style] = None
    explode: Optional[bool] = None
    schema: Optional[Union[Schema, Reference]] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Union[Example, Reference]]] = None
    content: Optional[Dict[str, MediaType]] = None

# A map of possible out-of-band callbacks related to the parent operation
@dataclass
class Callback:
    expressions: Dict[str, Union['PathItem', Reference]]

# Defines a security scheme that can be used by the operations
@dataclass
class SecurityScheme:
    type: SecuritySchemeType
    description: Optional[str] = None
    name: Optional[str] = None
    in_: Optional[ParameterLocation] = None
    scheme: Optional[str] = None
    bearerFormat: Optional[str] = None
    flows: Optional['OAuthFlows'] = None
    openIdConnectUrl: Optional[str] = None

# Allows configuration of the supported OAuth Flows
@dataclass
class OAuthFlows:
    implicit: Optional['OAuthFlow'] = None
    password: Optional['OAuthFlow'] = None
    clientCredentials: Optional['OAuthFlow'] = None
    authorizationCode: Optional['OAuthFlow'] = None

# Configuration details for a supported OAuth Flow
@dataclass
class OAuthFlow:
    authorizationUrl: Optional[str] = None
    tokenUrl: Optional[str] = None
    refreshUrl: Optional[str] = None
    scopes: Dict[str, str]

# Describes a single API operation on a path
@dataclass
class Operation:
    tags: Optional[List[str]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None
    operationId: Optional[str] = None
    parameters: Optional[List[Union[Parameter, Reference]]] = None
    requestBody: Optional[Union[RequestBody, Reference]] = None
    responses: Dict[str, Union[Response, Reference]]
    callbacks: Optional[Dict[str, Union[Callback, Reference]]] = None
    deprecated: Optional[bool] = None
    security: Optional[List[Dict[str, List[str]]]] = None  # List of SecurityRequirement
    servers: Optional[List[Server]] = None

# Describes the operations available on a single path
@dataclass
class PathItem:
    ref: Optional[str] = None  # Corresponds to $ref
    summary: Optional[str] = None
    description: Optional[str] = None
    get: Optional[Operation] = None
    put: Optional[Operation] = None
    post: Optional[Operation] = None
    delete: Optional[Operation] = None
    options: Optional[Operation] = None
    head: Optional[Operation] = None
    patch: Optional[Operation] = None
    trace: Optional[Operation] = None
    servers: Optional[List[Server]] = None
    parameters: Optional[List[Union[Parameter, Reference]]] = None

# Holds a set of reusable objects for different aspects of the OAS
@dataclass
class Components:
    schemas: Optional[Dict[str, Union[Schema, Reference]]] = None
    responses: Optional[Dict[str, Union[Response, Reference]]] = None
    parameters: Optional[Dict[str, Union[Parameter, Reference]]] = None
    examples: Optional[Dict[str, Union[Example, Reference]]] = None
    requestBodies: Optional[Dict[str, Union[RequestBody, Reference]]] = None
    headers: Optional[Dict[str, Union[Header, Reference]]] = None
    securitySchemes: Optional[Dict[str, Union[SecurityScheme, Reference]]] = None
    links: Optional[Dict[str, Union[Link, Reference]]] = None
    callbacks: Optional[Dict[str, Union[Callback, Reference]]] = None
    pathItems: Optional[Dict[str, Union[PathItem, Reference]]] = None  # Added pathItems for OpenAPI 3.1

# A declaration of which security mechanisms can be used across the API
SecurityRequirement = Dict[str, List[str]]  # Each name must correspond to a security scheme declared in the Security Schemes

# The root document object of the OpenAPI document
@dataclass
class OpenAPI:
    openapi: str
    info: Info
    jsonSchemaDialect: Optional[str] = None  # Specifies the default JSON Schema dialect for the schema objects
    servers: Optional[List[Server]] = None
    paths: Dict[str, PathItem]
    webhooks: Optional[Dict[str, Union[PathItem, Reference]]] = None  # Supports webhooks in OpenAPI 3.1
    components: Optional[Components] = None
    security: Optional[List[SecurityRequirement]] = None
    tags: Optional[List[Tag]] = None
    externalDocs: Optional[ExternalDocumentation] = None
