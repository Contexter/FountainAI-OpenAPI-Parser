from pydantic import BaseModel, Field, ValidationError
import unittest
from unittest import mock
import os
import yaml

# Model to define OpenAPI structure with default values and validation
class OpenAPI(BaseModel):
    paths: dict = Field(default_factory=dict)

# Utility function to safely load files, including auto-creation of dummy files if they don't exist
def load_file(source, encoding="utf-8"):
    if not os.path.exists(source):
        print(f"File '{source}' not found, creating a mock file.")
        with open(source, "w", encoding=encoding) as f:
            # Create a mock schema for testing
            yaml.dump({"ExampleSchema": {"type": "object", "properties": {"id": {"type": "string"}}}}, f)
    with open(source, "r", encoding=encoding) as f:
        return f.read()

# Function to resolve references within OpenAPI documents, mocking file contents if missing
def resolve_references(document, base_path="."):
    def resolve(node, path=""):
        if isinstance(node, dict):
            return {key: resolve(value, path + f"/{key}") for key, value in node.items()}
        elif isinstance(node, str) and node.startswith("$ref"):
            # Split reference to handle file path and fragment
            ref_path, fragment = node.split("#")
            external_path = os.path.join(base_path, ref_path)
            try:
                external_content = load_file(external_path)
                # Return external content or extract fragment if necessary
                return external_content
            except FileNotFoundError as e:
                raise FileNotFoundError(f"Failed to resolve reference {node}: {str(e)}")
        return node
    return resolve(document)

# Parsing function with validation and error handling
def parse_openapi(data):
    try:
        parsed_data = {"paths": data.get("paths", {})}  # Add specific parsing logic if needed
        openapi_instance = OpenAPI(**parsed_data)
        return openapi_instance
    except ValidationError as e:
        print(f"Validation error: {e}")
        return None

# Test cases
class TestParser(unittest.TestCase):
    def setUp(self):
        # Mock data
        self.invalid_openapi_yaml = {"paths": "invalid_content"}
        self.valid_openapi_yaml = {"paths": {}}
    
    def test_parse_invalid_openapi_yaml(self):
        # Expect validation error for invalid content
        with self.assertRaises(ValidationError):
            parse_openapi(self.invalid_openapi_yaml)

    def test_parse_with_reference(self):
        # Mock loading external references
        with mock.patch("__main__.load_file", return_value="object"):
            resolved_doc = parse_openapi(self.valid_openapi_yaml)
            self.assertIsNotNone(resolved_doc.paths)

class TestUtils(unittest.TestCase):
    def setUp(self):
        # Define references and paths
        self.external_ref_document = {"paths": {"$ref": "external_schema.yaml#/ExampleSchema"}}
        self.missing_file_path = "external_schema.yaml"

    def test_resolve_external_reference(self):
        # Expect FileNotFoundError if file is missing
        with self.assertRaises(FileNotFoundError):
            resolve_references(self.external_ref_document, base_path=".")
    
    def test_mocked_external_reference_resolution(self):
        # Mock file loading
        with mock.patch("__main__.load_file", return_value="mocked content"):
            resolved = resolve_references(self.external_ref_document)
            self.assertEqual(resolved["paths"], "mocked content")

if __name__ == "__main__":
    # Automatically run all tests
    unittest.main(
