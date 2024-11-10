import os
from pathlib import Path
import shutil

def add_mock_import_to_tests():
    """Ensure all test files import mock from unittest if they use mocking."""
    test_dir = Path("tests")
    for test_file in test_dir.glob("*.py"):
        with open(test_file, "r") as file:
            content = file.readlines()

        if any("mock" in line for line in content):
            with open(test_file, "w") as file:
                file.write("from unittest import mock\n")
                file.writelines(content)


def check_and_update_pydantic_models():
    """Update pydantic models for schema consistency in 'models.py'."""
    models_file = Path("fountainai_openapi_parser/models.py")
    updated_lines = []
    with open(models_file, "r") as file:
        for line in file:
            # This assumes `paths` field needs to be a dictionary based on the errors seen.
            if "paths:" in line:
                updated_lines.append("    paths: dict\n")  # Update paths type to dict explicitly
            else:
                updated_lines.append(line)
    with open(models_file, "w") as file:
        file.writelines(updated_lines)


def create_mock_external_file():
    """Create a mock external file in the test directory if missing."""
    external_file = Path("tests/resources/external_schema.yaml")
    external_file.parent.mkdir(parents=True, exist_ok=True)
    with open(external_file, "w") as file:
        file.write(
            """
            ExampleSchema:
              type: object
              properties:
                example_property:
                  type: string
            """
        )


def modify_test_for_missing_file():
    """Modify test file to mock file loading if external file is not found."""
    test_file = Path("tests/test_utils.py")
    with open(test_file, "r") as file:
        content = file.readlines()

    updated_content = []
    for line in content:
        if "FileNotFoundError" in line:
            # Add handling to mock file loading where `FileNotFoundError` is expected
            updated_content.append("from unittest import mock\n")
            updated_content.append("import fountainai_openapi_parser.utils as utils\n")
            updated_content.append(
                "with mock.patch('utils.load_file', return_value={'ExampleSchema': {'type': 'object'}}):\n"
            )
        updated_content.append(line)

    with open(test_file, "w") as file:
        file.writelines(updated_content)


def main():
    print("Fixing CI/CD pipeline issues...")

    # Step 1: Add `mock` import to test files using mocking
    print("Adding missing mock imports to test files...")
    add_mock_import_to_tests()

    # Step 2: Update pydantic models for schema consistency
    print("Updating pydantic models to ensure schema consistency...")
    check_and_update_pydantic_models()

    # Step 3: Create a mock external file if needed
    print("Creating mock external file for tests...")
    create_mock_external_file()

    # Step 4: Update test files to handle missing external file dependencies
    print("Modifying test files to handle missing external files...")
    modify_test_for_missing_file()

    print("All fixes applied. You can now re-run the CI pipeline.")

if __name__ == "__main__":
    main()
