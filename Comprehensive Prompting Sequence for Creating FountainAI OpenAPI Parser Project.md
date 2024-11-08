# Comprehensive Prompting Sequence for Creating FountainAI OpenAPI Parser Project

This documentation provides a step-by-step guide for generating all necessary components of the FountainAI OpenAPI Parser project using prompt-driven script creation. Each step is designed to automate the process of building a high-quality, modular Python library that adheres to best practices for maintainability and extensibility.

## Step 1: Create Project Directory Structure

**Prompt:**

Write a script (`create_project_structure.py`) to automate the creation of the following directory structure for the `FountainAI-OpenAPI-Parser` project:

- `fountainai_openapi_parser/` (main module)
  - `__init__.py` (initializes the module)
  - `models.py` (contains dataclass models)
  - `parser.py` (main parsing functions)
  - `utils.py` (helper functions)
- `tests/` (unit tests)
  - `__init__.py` (initializes the tests package)
  - `test_parser.py` (contains unit tests)
- `setup.py` (setup configuration for pip installation)
- `README.md` (documentation)
- `LICENSE` (license information)
- `MANIFEST.in` (defines additional files for distribution)

The script should:
- Automatically create all the required directories and files.
- Include boilerplate content in each file to initialize the project structure.

**Goal:** Ensure that all necessary files and directories are created consistently, with minimal manual intervention.

---

## Step 2: Define Data Models in `models.py`

**Prompt:**

Create a script (`generate_models.py`) that writes the data models to `models.py`. 
This script should:
- Generate Python `dataclasses` for all core OpenAPI components (`Contact`, `License`, `Info`, etc.).
- Include all fields and types, following OpenAPI 3.1 specifications.
- Use `Optional` and `field(default_factory=...)` where necessary for correct defaults.
- Include type validation for fields to ensure adherence to the OpenAPI schema.

**Goal:** To automate the creation of comprehensive dataclass models, reducing manual errors and ensuring compliance with the OpenAPI specification.

---

## Step 3: Add Parsing Functions in `parser.py`

**Prompt:**

Create a script (`generate_parser.py`) to write the parsing functions to `parser.py`.
This script should:
- Implement functions to load and parse YAML/JSON files (`load_yaml_or_json`).
- Parse the loaded data into the `OpenAPI` data model (`parse_openapi`).
- Create helper functions for nested components (`create_path_item`, `create_operation`).
- Add comprehensive error handling and validation to ensure robustness.
- Include logging for debugging and traceability.

**Goal:** To build a robust parsing mechanism that handles errors gracefully, validates input, and supports deep integration with other components.

---

## Step 4: Create Utility Functions in `utils.py`

**Prompt:**

Write a script (`generate_utils.py`) to populate `utils.py` with utility functions.
These utility functions should include:
- **Reference Resolution (`resolve_references`)**: Handle both local and remote `$ref` references with caching to avoid circular references.
- **Validation (`validate_openapi`)**: Validate the OpenAPI document against the OpenAPI 3.1 schema, providing clear error messages.
- **Common Utility Functions**: Add reusable helper functions for common operations like type checks or data normalization.
- Ensure all utility functions have comprehensive error handling and logging.

**Goal:** To provide a set of reusable utilities that improve the maintainability of the code and facilitate common operations in the parser.

---

## Step 5: Generate Tests in `test_parser.py`

**Prompt:**

Write a script (`generate_tests.py`) to create unit tests in `tests/test_parser.py`.
The script should:
- Set up positive and negative test cases for all the core parsing functions.
- Use `pytest` as the testing framework.
- Include fixtures for setting up test data.
- Mock network requests for reference resolution.
- Ensure each test provides meaningful output and catches edge cases.

**Goal:** To ensure full test coverage, verifying that the parser works correctly under various conditions and handles edge cases appropriately.

---

## Step 6: Write Setup Script (`setup.py`)

**Prompt:**

Create a script (`generate_setup.py`) that generates `setup.py` for packaging the library.
Ensure the setup file includes:
- Metadata such as `name`, `version`, `author`, `description`, etc.
- Dependency management (`install_requires`) for necessary packages (`PyYAML`, `jsonschema`, `requests`).
- An entry point to easily install the package using `pip`.
- Include compatibility tags for different Python versions.

**Goal:** To facilitate easy installation and distribution of the library through `pip`, ensuring that all dependencies are correctly managed.

---

## Step 7: Create README and License

**Prompt:**

Write a script (`generate_documentation.py`) that generates `README.md` and `LICENSE`.
- **README.md**: Provide an overview, installation instructions, usage examples, and contribution guidelines.
- **LICENSE**: Include an MIT License (or other specified license) with the correct year and author.
- Ensure the README is well-formatted for readability and usability.

**Goal:** To provide comprehensive documentation, making it easy for others to understand, use, and contribute to the project.

---

## Step 8: Code Quality and Best Practices

**Prompt:**

Enhance code quality by:
- **Linting**: Set up a script to configure `flake8` for PEP8 compliance and create a linting script (`run_linter.py`).
- **Type Checking**: Use `mypy` for enforcing type hints and catching type-related errors, and add a script (`run_mypy.py`) to automate this check.
- **Testing**: Integrate continuous integration (CI) using GitHub Actions to automatically run tests and check code quality on every push.
- **Documentation Strings**: Add comprehensive docstrings to every function and class, explaining parameters, return types, and examples.
- **Logging**: Replace all print statements with proper `logging` to improve debugging and monitoring.
- **Error Handling**: Implement custom exception classes for specific errors encountered during parsing and validation.

**Goal:** To ensure that the code follows industry standards for quality and maintainability, making it robust, easy to extend, and pleasant to work with.

---

## Summary

This prompting sequence helps create a fully functional, modular OpenAPI 3.1 parser library for Python. By using scripts for each component, we can ensure consistency, avoid manual errors, and build a well-structured library with clear documentation and thorough testing. Each step aims to facilitate automation while promoting best practices, ensuring that the resulting library is high-quality and ready for use in production environments.
