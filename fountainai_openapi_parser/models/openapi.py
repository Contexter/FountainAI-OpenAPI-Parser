class OpenAPI(BaseModel):
    openapi: str
    info: Info
    jsonSchemaDialect: Optional[AnyUrl] = None
    servers: Optional[List[Server]] = None
    paths: dict
    webhooks: Optional[Dict[str, Union[PathItem, Reference]]] = None
    components: Optional[Components] = None
    security: Optional[List[Dict[str, List[str]]]] = None  # SecurityRequirements
    tags: Optional[List[Tag]] = None
    externalDocs: Optional[ExternalDocumentation] = None