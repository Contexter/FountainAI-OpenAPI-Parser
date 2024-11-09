# Step 2 - Refined Prompt for Modularizing Data Model Generation
> Iteration 2

## Prompt

Create a set of scripts to modularize the generation of data models for OpenAPI components in Python using dataclasses. Each script should generate specific data models as follows:

### Directory Structure
- Create a new directory called `models_generator` at the root of the repository.
- Place all component-specific scripts, as well as the main orchestration script, within this directory to keep the library structure organized.

### Main Orchestration Script (`models_generator/generate_models.py`):
- Acts as an orchestrator that imports functions from individual model-generating scripts.
- Calls functions to combine all models into a single `models.py` file.
- Once all the models are generated, compress the `models_generator` directory into a `.zip` file for easy distribution or download.

### Individual Scripts for Core Components:
- Each OpenAPI component should have its own script within the `models_generator` directory (e.g., `generate_contact.py`, `generate_license.py`).
- Each script should:
  - Define a function that returns a string representation of the dataclass for its specific component.
  - Follow OpenAPI 3.1 specifications to ensure fields are correctly defined.
  - Use `Optional` and `field(default_factory=...)` where necessary for correct defaults.
  - Ensure adherence to type validation in line with the OpenAPI schema.

### Comprehensive List of Component Scripts:
1. **Contact** - `models_generator/generate_contact.py`: Generates the `Contact` dataclass model.
2. **License** - `models_generator/generate_license.py`: Generates the `License` dataclass model.
3. **Info** - `models_generator/generate_info.py`: Generates the `Info` dataclass model.
4. **ServerVariable** - `models_generator/generate_server_variable.py`: Generates the `ServerVariable` dataclass model.
5. **Server** - `models_generator/generate_server.py`: Generates the `Server` dataclass model.
6. **Tag** - `models_generator/generate_tag.py`: Generates the `Tag` dataclass model.
7. **ExternalDocumentation** - `models_generator/generate_external_documentation.py`: Generates the `ExternalDocumentation` dataclass model.
8. **Reference** - `models_generator/generate_reference.py`: Generates the `Reference` dataclass model.
9. **XML** - `models_generator/generate_xml.py`: Generates the `XML` dataclass model.
10. **Discriminator** - `models_generator/generate_discriminator.py`: Generates the `Discriminator` dataclass model.
11. **Encoding** - `models_generator/generate_encoding.py`: Generates the `Encoding` dataclass model.
12. **MediaType** - `models_generator/generate_media_type.py`: Generates the `MediaType` dataclass model.
13. **Example** - `models_generator/generate_example.py`: Generates the `Example` dataclass model.
14. **Schema** - `models_generator/generate_schema.py`: Generates the `Schema` dataclass model, including comprehensive JSON Schema Draft 2019-09 fields.
15. **Parameter** - `models_generator/generate_parameter.py`: Generates the `Parameter` dataclass model.
16. **RequestBody** - `models_generator/generate_request_body.py`: Generates the `RequestBody` dataclass model.
17. **Response** - `models_generator/generate_response.py`: Generates the `Response` dataclass model.
18. **Link** - `models_generator/generate_link.py`: Generates the `Link` dataclass model.
19. **Header** - `models_generator/generate_header.py`: Generates the `Header` dataclass model.
20. **Callback** - `models_generator/generate_callback.py`: Generates the `Callback` dataclass model.
21. **SecurityScheme** - `models_generator/generate_security_scheme.py`: Generates the `SecurityScheme` dataclass model, including different security scheme types.
22. **OAuthFlows** - `models_generator/generate_oauth_flows.py`: Generates the `OAuthFlows` dataclass model, covering all OAuth flow types.
23. **Operation** - `models_generator/generate_operation.py`: Generates the `Operation` dataclass model.
24. **PathItem** - `models_generator/generate_path_item.py`: Generates the `PathItem` dataclass model.
25. **Components** - `models_generator/generate_components.py`: Generates the `Components` dataclass model.
26. **SecurityRequirement** - `models_generator/generate_security_requirement.py`: Generates the `SecurityRequirement` dataclass model.
27. **Webhook** - `models_generator/generate_webhook.py`: Generates the `Webhook` dataclass model.
28. **OpenAPI** - `models_generator/generate_openapi.py`: Generates the `OpenAPI` dataclass model, orchestrating all other components.

### Reusable Imports Script
1. **Common Typing Imports** - `models_generator/generate_common_imports.py`: Provides reusable imports such as `Optional`, `List`, `Dict`, `Any`, and `Union` to avoid redundancy across scripts.

### Goal of Modularization
- **Maintainability**: Each OpenAPI component is defined in its own module, making updates and maintenance easier.
- **Comprehensive Coverage**: By breaking down into individual components, we ensure all OpenAPI 3.1 features are covered thoroughly.
- **Reusability**: Components can be reused or extended independently, providing flexibility for future versions or custom extensions.
- **Distribution**: After generating all the necessary components, compress the `models_generator` directory into a `.zip` file for easy sharing and downloading.

### How to Make the Generated Models Available for Download
- After all models have been generated, create a Python script to compress the `models_generator` directory into a `.zip` file.
- Provide the `.zip` file as a downloadable link so that users can easily access all generated files.
