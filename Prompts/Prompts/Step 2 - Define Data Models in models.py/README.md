# Step 2 - Comprehensive Prompt for Creating Data Models in `models.py`
> Iteration 3

## Prompt

Create a single Python file, `models.py`, that defines comprehensive data models for all OpenAPI 3.1 components using Python dataclasses. This file should fully represent each component, with no placeholders or incomplete definitions.

### Requirements

1. **Dataclass Structure**: Define each OpenAPI component as a standalone Python dataclass. Import all necessary types, including `Optional`, `List`, `Dict`, `Any`, and `Union` at the top of `models.py`.

2. **Component Fields**:
   - **Required Fields**: Implement all mandatory fields as specified in OpenAPI 3.1.
   - **Optional Fields**: Use `Optional` for fields that are not required, with default values set to `None`.
   - **Nested References**: For fields referencing other components, use type hints with forward references where necessary (e.g., `Optional['Schema']`).

3. **Components to Implement**:
   Define each of the following components as fully detailed dataclasses with fields adhering to OpenAPI 3.1 specifications:
   - `Contact`, `License`, `Info`, `ServerVariable`, `Server`, `Tag`, `ExternalDocumentation`, `Reference`, `XML`, `Discriminator`, `Encoding`, `MediaType`, `Example`, `Schema`, `Parameter`, `RequestBody`, `Response`, `Link`, `Header`, `Callback`, `SecurityScheme`, `OAuthFlows`, `Operation`, `PathItem`, `Components`, `SecurityRequirement`, `Webhook`, and `OpenAPI`.

4. **Accurate Type Definitions**:
   - **Enums**: Use Python’s `Enum` class for fields that accept a set of predefined values.
   - **Dictionaries and Lists**: Implement dictionary and list fields exactly as defined in OpenAPI 3.1.
   - **Boolean Defaults**: Default boolean fields to `False` if required.

5. **Example Content**:
   - Provide example values or docstrings at the class level, illustrating the instantiation of each component with realistic OpenAPI data.

6. **Testing and Validation**:
   - Ensure each model allows realistic OpenAPI content, validating that all fields, types, and formats align with OpenAPI 3.1 requirements.
   - The final `models.py` should contain no placeholder comments or unimplemented fields.

### Expected Output for Each Component

The following is an example of the expected structure for each dataclass:

```python
from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass

@dataclass
class Contact:
    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None

@dataclass
class ServerVariable:
    enum: Optional[List[str]] = None
    default: str
    description: Optional[str] = None

@dataclass
class Server:
    url: str
    description: Optional[str] = None
    variables: Optional[Dict[str, ServerVariable]] = None
```

This structure should be applied comprehensively for each component in the list, ensuring every detail is covered based on the OpenAPI 3.1 specification.

### Modularization

1. **Directory Setup**: Organize all component generator scripts within a `models_generator` directory.
2. **Orchestration Script**: Use a main script, `generate_models.py`, to combine these individual component scripts into a final, fully-implemented `models.py`.
3. **Reusable Imports**: Include a `generate_common_imports.py` for shared imports, such as `Optional`, `List`, `Dict`, `Any`, and `Union`.

### Goals of the Model Generation

- **Maintainability**: Each component is modularized, allowing updates to specific components without modifying the entire file.
- **Comprehensive Coverage**: Ensure that every OpenAPI 3.1 feature is thoroughly covered in `models.py`.
- **Distribution**: Compress `models_generator` into a `.zip` file to provide easy access to all generated models.

---

This updated prompt now clearly defines a step-by-step approach for producing a complete and accurate `models.py` that adheres to OpenAPI 3.1, leaving no room for partial implementations or placeholders.