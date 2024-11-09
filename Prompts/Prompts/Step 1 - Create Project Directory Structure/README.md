# Step 1 - Create Project Directory Structure
> Iteration 2

## Prompt

Write a script (`create_project_structure.py`) to be placed at the **root** of the `FountainAI-OpenAPI-Parser` repository. This script will automate the creation of the following directory and file structure, laying the foundation for the project:

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

The script should perform the following:

1. **Directory and File Creation**: Automatically create all required directories and files as listed above.
2. **Boilerplate Content**: Add boilerplate content to each file to initialize the project structure. For example:
   - `__init__.py` files should contain a brief comment or placeholder to initialize the package.
   - `README.md`, `LICENSE`, and `setup.py` should include minimal placeholder content relevant to each file's purpose.
   
## Goal

The goal is to ensure a consistent project structure with minimal manual intervention, providing a standardized foundation that all team members can use to begin development.

---

By running this script at the repository root, developers can quickly establish a clean, organized project directory with all essential files in place, ready for subsequent development steps.
