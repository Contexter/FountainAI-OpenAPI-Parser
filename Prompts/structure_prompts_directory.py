import os

# Define the steps and their descriptions as subdirectories under `Prompts`
steps = {
    "Step 1 - Create Project Directory Structure": (
        "Write a script (`create_project_structure.py`) to automate the creation of the main project structure for FountainAI-OpenAPI-Parser."
    ),
    "Step 2 - Define Data Models in models.py": (
        "Create a script (`generate_models.py`) to write data models in `models.py`, adhering to OpenAPI 3.1 specifications with dataclasses."
    ),
    "Step 3 - Add Parsing Functions in parser.py": (
        "Write a script (`generate_parser.py`) to implement parsing functions, error handling, and logging in `parser.py`."
    ),
    "Step 4 - Create Utility Functions in utils.py": (
        "Write a script (`generate_utils.py`) to populate `utils.py` with reusable utility functions, including reference resolution and validation."
    ),
    "Step 5 - Generate Tests in test_parser.py": (
        "Write a script (`generate_tests.py`) to create unit tests in `tests/test_parser.py` for all core parsing functions."
    ),
    "Step 6 - Write Setup Script setup.py": (
        "Create a script (`generate_setup.py`) to generate `setup.py`, ensuring all metadata and dependencies are managed correctly."
    ),
    "Step 7 - Create README and License": (
        "Write a script (`generate_documentation.py`) to create `README.md` and `LICENSE`, providing project overview and installation instructions."
    ),
    "Step 8 - Code Quality and Best Practices": (
        "Enhance code quality with linting, type-checking, and CI setup. Add comprehensive docstrings, error handling, and logging."
    ),
}

# Create the `Prompts/` directory if it doesn't exist
base_dir = "Prompts"
os.makedirs(base_dir, exist_ok=True)

# Create each step as a subdirectory with a README
for step, description in steps.items():
    # Create the subdirectory for each step
    step_dir = os.path.join(base_dir, step)
    os.makedirs(step_dir, exist_ok=True)

    # Create a README.md file in each step directory with the description
    readme_path = os.path.join(step_dir, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(f"# {step}\n\n{description}")

print(
    "Prompts directory structured successfully with step-specific README files."
)
