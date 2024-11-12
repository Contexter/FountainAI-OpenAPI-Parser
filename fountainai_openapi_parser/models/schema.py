class Schema(BaseModel):
    ref: Optional[str] = Field(default=None, alias="$ref")

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
    contentSchema: Optional["Schema"] = None

    # Number-specific properties
    multipleOf: Optional[float] = None
    maximum: Optional[float] = None
    exclusiveMaximum: Optional[float] = None
    minimum: Optional[float] = None
    exclusiveMinimum: Optional[float] = None

    # Array-specific properties
    items: Optional[Union["Schema", List["Schema"]]] = None
    prefixItems: Optional[List["Schema"]] = None
    contains: Optional["Schema"] = None
    maxItems: Optional[int] = None
    minItems: Optional[int] = None
    uniqueItems: Optional[bool] = None
    maxContains: Optional[int] = None
    minContains: Optional[int] = None
    unevaluatedItems: Optional[Union["Schema", bool]] = None

    # Object-specific properties
    properties: Optional[Dict[str, "Schema"]] = None
    patternProperties: Optional[Dict[str, "Schema"]] = None
    additionalProperties: Optional[Union["Schema", bool]] = None
    maxProperties: Optional[int] = None
    minProperties: Optional[int] = None
    required: Optional[List[str]] = None
    dependentRequired: Optional[Dict[str, List[str]]] = None
    dependentSchemas: Optional[Dict[str, "Schema"]] = None
    propertyNames: Optional["Schema"] = None
    unevaluatedProperties: Optional[Union["Schema", bool]] = None

    # Conditional and logical keywords
    allOf: Optional[List["Schema"]] = None
    anyOf: Optional[List["Schema"]] = None
    oneOf: Optional[List["Schema"]] = None
    not_: Optional["Schema"] = Field(default=None, alias="not")
    if_: Optional["Schema"] = Field(default=None, alias="if")
    then: Optional["Schema"] = None
    else_: Optional["Schema"] = Field(default=None, alias="else")

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

    class Config:
        populate_by_name = True