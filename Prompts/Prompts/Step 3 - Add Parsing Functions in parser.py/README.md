
# **Prompt for Creating `parser.py`**

## **Project Overview**

First, let's review the current project structure to understand what components are already in place:

```
.
├── LICENSE
├── MANIFEST.in
├── Parser-Illustration.png
├── Parser-Illustration.py
├── Prompts
│   ├── Prompts
│   │   ├── Step 1 - Create Project Directory Structure
│   │   │   └── README.md
│   │   ├── Step 2 - Define Data Models in models.py
│   │   │   └── README.md
│   │   ├── Step 3 - Add Parsing Functions in parser.py
│   │   │   └── README.md
│   │   ├── Step 4 - Create Utility Functions in utils.py
│   │   │   └── README.md
│   │   ├── Step 5 - Generate Tests in test_parser.py
│   │   │   └── README.md
│   │   ├── Step 6 - Write Setup Script setup.py
│   │   │   └── README.md
│   │   ├── Step 7 - Create README and License
│   │   │   └── README.md
│   │   └── Step 8 - Code Quality and Best Practices
│   │       └── README.md
│   ├── README.md
│   └── structure_prompts_directory.py
├── README.md
├── app.log
├── create_project_structure.py
├── fountainai_openapi_parser
│   ├── __init__.py
│   ├── models.py
│   ├── parser.py
│   └── utils.py
├── setup.py
└── tests
    ├── __init__.py
    └── test_parser.py
```

### **Current State**

- **`models.py`**: Contains the Pydantic models representing the OpenAPI 3.1 specification. This has been completed as per previous instructions.
- **`parser.py`**: An existing file intended for parsing functions, but its implementation may not be complete.
- **`utils.py`**: A placeholder for utility functions.
- **`tests/test_parser.py`**: Exists but may require additional tests related to the parsing functionality.
- **`Prompts` Directory**: Contains prompts and README files for each development step, indicating a structured approach to the project.

---

## **Objective**

Develop the `parser.py` module within the `fountainai_openapi_parser` package. This module will provide functions to parse OpenAPI 3.1 documents (in JSON or YAML format) into Python objects using the Pydantic models defined in `models.py`. The parser should handle features specific to OpenAPI 3.1, including `$ref` references, and provide utilities for working with the parsed data.

## **Requirements**

### **1. Parsing OpenAPI Documents**

- **Support Both YAML and JSON Formats:**
  - Implement functions to read and parse OpenAPI documents in both YAML and JSON formats.
  - Automatically detect the format based on the file extension or content.
  - **Note**: Since `utils.py` exists, consider placing format detection logic in a utility function within `utils.py`.

- **Use Pydantic Models:**
  - Utilize the Pydantic models defined in `models.py` for parsing and validating the OpenAPI documents.
  - Ensure that the parsed data conforms to the OpenAPI 3.1 specification.

- **Handle `$ref` References:**
  - Implement a mechanism to resolve `$ref` references within the OpenAPI documents.
  - Support references to local components as well as external files.
  - Ensure that circular references are detected and handled gracefully.
  - **Integration with `utils.py`**: You may use `utils.py` for helper functions related to reference resolution.

### **2. Parser Functions**

- **Main Parsing Function:**
  - Create a `parse_openapi` function in `parser.py` that accepts a file path or file content and returns an instance of the `OpenAPI` model.
  - The function should handle any necessary preprocessing, such as reference resolution.
  - **Example Function Signature:**

    ```python
    def parse_openapi(
        source: Union[str, Path],
        encoding: str = 'utf-8',
        resolve_references: bool = True
    ) -> OpenAPI:
        """
        Parses an OpenAPI 3.1 document from a file path or string content.

        Args:
            source (Union[str, Path]): The file path to the OpenAPI document or the content as a string.
            encoding (str, optional): The encoding of the file if a file path is provided. Defaults to 'utf-8'.
            resolve_references (bool, optional): Whether to resolve $ref references. Defaults to True.

        Returns:
            OpenAPI: An instance of the OpenAPI model representing the parsed document.

        Raises:
            ParsingError: If there is a problem parsing the document.
            ValidationError: If the document does not conform to the OpenAPI 3.1 specification.
        """
    ```

- **Utility Functions:**
  - Implement utility functions as needed to support the parsing process, such as:
    - **`load_file`** (in `utils.py`):
      - Reads the file content from disk.
      - Detects whether the file is YAML or JSON.
    - **`resolve_references`** (in `parser.py` or `utils.py`):
      - Recursively resolves `$ref` references in the document.
    - **`validate_document`** (in `parser.py` or `utils.py`):
      - Validates the OpenAPI document against the specification.

### **3. Error Handling**

- **Informative Exceptions:**
  - Raise descriptive exceptions when parsing fails due to invalid syntax, missing files, unresolved references, or validation errors.
  - Use custom exception classes where appropriate (e.g., `ParsingError`, `ValidationError`, `ReferenceResolutionError`).
  - **File Organization**: Consider defining custom exceptions in a separate module (e.g., `exceptions.py`) within the package for better organization.

### **4. Logging**

- **Logging Mechanism:**
  - Integrate Python's built-in `logging` module to provide informative logs at various levels (DEBUG, INFO, WARNING, ERROR).
  - Allow users of the parser to configure the logging level.
  - **Configuration**: Use a configuration file or allow configuration through the `__init__.py` file in the package.

### **5. Performance Considerations**

- **Efficient Parsing:**
  - Optimize the parsing process for large OpenAPI documents.
  - Avoid unnecessary re-parsing or re-validation of components.

- **Caching:**
  - Implement caching mechanisms for resolved references to prevent redundant processing.
  - **Note**: If caching logic becomes complex, consider adding a `cache.py` module.

### **6. Usability and API Design**

- **User-Friendly API:**
  - Design the parser functions to be intuitive and easy to use for developers.
  - Provide clear function signatures and docstrings with examples.
  - **Consistency**: Ensure that the API aligns with existing modules in the package.

- **Extensibility:**
  - Structure the code to allow for future extensions, such as additional utilities or support for other OpenAPI versions.

### **7. Documentation**

- **Docstrings and Comments:**
  - Write comprehensive docstrings for all functions and classes, following the Google or NumPy style guides.
  - Include inline comments where necessary to explain complex logic.

- **Usage Examples:**
  - Provide examples of how to use the parser functions in the docstrings or in the main `README.md`.

- **Integration with Existing Documentation:**
  - Update the relevant `README.md` files in the `Prompts` directory, particularly under `Step 3 - Add Parsing Functions in parser.py`, to reflect the implementation details.

### **8. Testing**

- **Unit Tests:**
  - Write unit tests in `tests/test_parser.py` to cover various parsing scenarios, including:
    - Successful parsing of valid OpenAPI documents.
    - Handling of invalid documents and expected exceptions.
    - Resolution of references, including circular and external references.

- **Test Coverage:**
  - Aim for high test coverage of the `parser.py` module.
  - Use coverage tools like `coverage.py` to measure test coverage.

- **Continuous Integration:**
  - If not already in place, consider setting up a CI pipeline (e.g., GitHub Actions) to run tests automatically on commits or pull requests.

### **9. Code Quality**

- **PEP 8 Compliance:**
  - Ensure that all code follows PEP 8 style guidelines.
  - Use tools like `flake8` or `black` for linting and formatting.

- **Type Annotations:**
  - Include type annotations for all functions and variables.
  - Use `mypy` to check for type consistency.

- **Modularity:**
  - Organize code into functions and classes logically.
  - Avoid long functions by breaking them into smaller, reusable components.

### **10. Dependencies**

- **External Libraries:**
  - Use standard libraries where possible.
  - For YAML parsing, use `PyYAML` (already in use as per previous steps) or consider `ruamel.yaml` for more advanced features.
  - Ensure that all dependencies are listed in `setup.py` and `requirements.txt`.

- **Version Management:**
  - Pin versions of dependencies to avoid compatibility issues.
  - Update `setup.py` to reflect any new dependencies added during this implementation.

---

## **Implementation Guidelines**

- **File Organization:**

  - **`fountainai_openapi_parser/`**
    - **`__init__.py`**: Initialize logging configuration and expose key functions.
    - **`models.py`**: Already contains Pydantic models.
    - **`parser.py`**: Implement parsing functions as per this prompt.
    - **`utils.py`**: Place helper functions that are used across multiple modules.
    - **`exceptions.py`**: (Optional) Define custom exception classes here for better organization.

- **Functionality Breakdown:**

  - **`parser.py`:**

    - `parse_openapi`
    - `resolve_references` (if not placed in `utils.py`)
    - `validate_document`

  - **`utils.py`:**

    - `load_file`
    - `is_yaml`
    - Any additional helper functions.

- **Exception Handling:**

  - Define custom exceptions in `exceptions.py` or within `parser.py` if `exceptions.py` is not created.

- **Logging Configuration:**

  - Configure logging in `__init__.py` or within `parser.py`.
  - Provide a function to set the logging level, e.g., `set_logging_level(level: int)`.

---

## **Testing Guidelines**

- **Test Files:**

  - **`tests/test_parser.py`**: Add tests corresponding to the new parsing functions.
  - **Sample OpenAPI Documents:**
    - Place sample OpenAPI documents in a `tests/data/` directory for use in tests.
    - Include both valid and invalid documents.

- **Test Cases:**

  - **Valid Documents:**
    - Test parsing of documents with complex structures and references.
  - **Invalid Documents:**
    - Test handling of syntax errors, invalid references, and schema validation failures.
  - **Reference Resolution:**
    - Test resolution of local and external `$ref` references.
    - Test detection and handling of circular references.

---

## **Documentation**

- **Update `README.md`:**

  - Provide instructions on how to use the parser module.
  - Include examples and code snippets demonstrating common use cases.

- **Update `Prompts` Directory:**

  - In `Prompts/Prompts/Step 3 - Add Parsing Functions in parser.py/README.md`, update the content to reflect the implemented parsing functions and any deviations from the initial plan.

- **API Documentation:**

  - Generate API documentation using tools like Sphinx or MkDocs, if desired.

---

## **Additional Considerations**

- **Version Control:**

  - Commit changes with clear and descriptive messages, following the project's commit message conventions.
  - Use feature branches for development and merge into the main branch via pull requests.

- **Licensing:**

  - Ensure that any external libraries used comply with the project's licensing.
  - Update the `LICENSE` file if necessary.

- **Future Extensions:**

  - Consider how the parser can be extended to support OpenAPI 3.0 or future versions.
  - Design the code to be modular and adaptable.

---

# **Summary**

By incorporating the current project structure and existing files, this updated prompt provides a clear roadmap for developing the `parser.py` module within the FountainAI OpenAPI Parser project. It ensures that the new code aligns with the project's organization, leverages existing modules like `utils.py`, and follows the established development steps outlined in the `Prompts` directory.

Following this prompt will result in a robust and well-integrated `parser.py` module that enhances the functionality of the FountainAI OpenAPI Parser, providing users with the ability to parse and work with OpenAPI 3.1 documents effectively.

