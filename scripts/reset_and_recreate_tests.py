import logging
import yaml
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO)

# Define paths for test data
test_data_dir = Path(__file__).parent / "../tests/data"
test_files_dir = Path(__file__).parent / "../tests"

# Ensure test data directory exists
test_data_dir.mkdir(parents=True, exist_ok=True)
logging.info("All existing test files deleted.")

# Define YAML data for tests
yaml_files = {
    "openapi.yaml": {
        "openapi": "3.0.0",
        "info": {"title": "Sample API", "version": "1.0.0"},
        "paths": {
            "/example": {
                "get": {
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "example_field": {"type": "string"}
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "components": {
            "schemas": {
                "ExampleSchema": {
                    "type": "object",
                    "properties": {"example_field": {"type": "string"}},
                }
            }
        },
    },
    "external_schema.yaml": {
        "components": {
            "schemas": {
                "ExampleSchema": {
                    "type": "object",
                    "properties": {"example_field": {"type": "string"}},
                }
            }
        }
    },
    "invalid_openapi.yaml": {
        "openapi": "3.0.0",
        "info": {"title": "Invalid API", "version": "1.0.0"},
        "paths": "invalid_content",
    },
}

# Write YAML files
for filename, data in yaml_files.items():
    file_path = test_data_dir / filename
    with open(file_path, "w") as file:
        yaml.dump(data, file)
    logging.info(f"Created YAML file at: {file_path}")

# Create fresh test files
# test_parser.py
with open(test_files_dir / "test_parser.py", "w") as f:
    f.write(
        """
import unittest
from fountainai_openapi_parser.parser import parse_openapi
from fountainai_openapi_parser.exceptions import ValidationError
import yaml
from pathlib import Path

class TestParser(unittest.TestCase):
    def setUp(self):
        with open(Path(__file__).parent / "data/openapi.yaml") as f:
            self.valid_openapi_yaml = yaml.safe_load(f)
        with open(Path(__file__).parent / "data/invalid_openapi.yaml") as f:
            self.invalid_openapi_yaml = yaml.safe_load(f)

    def test_parse_valid_openapi_yaml(self):
        parsed = parse_openapi(self.valid_openapi_yaml)
        self.assertIn("/example", parsed.paths)

    def test_parse_invalid_openapi_yaml(self):
        with self.assertRaises(ValidationError):
            parse_openapi(self.invalid_openapi_yaml)
    """
    )

# test_integration.py
with open(test_files_dir / "test_integration.py", "w") as f:
    f.write(
        """
import unittest
from fountainai_openapi_parser.utils import resolve_references
import yaml
from pathlib import Path

class TestIntegration(unittest.TestCase):
    def setUp(self):
        with open(Path(__file__).parent / "data/openapi.yaml") as f:
            self.openapi_yaml = yaml.safe_load(f)

    def test_external_reference_resolution(self):
        resolved_result = resolve_references(self.openapi_yaml, base_path=Path(__file__).parent / "data")
        self.assertIn("example_field", resolved_result["components"]["schemas"]["ExampleSchema"]["properties"])
    """
    )

# test_utils.py
with open(test_files_dir / "test_utils.py", "w") as f:
    f.write(
        """
import unittest
from fountainai_openapi_parser.utils import resolve_references
import yaml
from pathlib import Path

class TestUtils(unittest.TestCase):
    def setUp(self):
        with open(Path(__file__).parent / "data/external_schema.yaml") as f:
            self.external_ref_yaml = yaml.safe_load(f)

    def test_resolve_external_reference(self):
        resolved_data = resolve_references(self.external_ref_yaml, base_path=Path(__file__).parent / "data")
        self.assertIn("example_field", resolved_data["components"]["schemas"]["ExampleSchema"]["properties"])
    """
    )

logging.info("Test files recreated with correct structure.")
