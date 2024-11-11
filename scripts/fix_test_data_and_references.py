import logging
import yaml
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO)

# Paths for test YAML files
test_data_dir = Path(__file__).parent / "../tests/data"
test_files_dir = Path(__file__).parent / "../tests"

# Ensure test data directory exists
test_data_dir.mkdir(parents=True, exist_ok=True)
logging.info("All existing test files deleted.")

# Create fresh test YAML files
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

# Create new test_parser.py
with open(test_files_dir / "test_parser.py", "w") as f:
    f.write(
        """
import unittest
from fountainai_openapi_parser.parser import parse_openapi
from fountainai_openapi_parser.exceptions import ValidationError
from pathlib import Path
import yaml

class TestParser(unittest.TestCase):
    def setUp(self):
        self.valid_openapi_path = Path(__file__).parent / "data/openapi.yaml"
        self.invalid_openapi_path = Path(__file__).parent / "data/invalid_openapi.yaml"

    def test_parse_valid_openapi_yaml(self):
        with open(self.valid_openapi_path) as f:
            openapi_yaml = yaml.safe_load(f)
        parsed = parse_openapi(openapi_yaml)
        self.assertIsNotNone(parsed)

    def test_parse_invalid_openapi_yaml(self):
        with open(self.invalid_openapi_path) as f:
            openapi_yaml = yaml.safe_load(f)
        with self.assertRaises(ValidationError):
            parse_openapi(openapi_yaml)
    """
    )

logging.info("Created test_parser.py with new test cases.")

# Create new test_integration.py
with open(test_files_dir / "test_integration.py", "w") as f:
    f.write(
        """
import unittest
from fountainai_openapi_parser.utils import resolve_references
from pathlib import Path
import yaml

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.openapi_path = Path(__file__).parent / "data/openapi.yaml"

    def test_external_reference_resolution(self):
        with open(self.openapi_path) as f:
            openapi_yaml = yaml.safe_load(f)
        resolved_result = resolve_references(openapi_yaml, base_path=Path(__file__).parent / "data")
        self.assertIn("example_field", resolved_result['components']['schemas']['ExampleSchema']['properties'])
    """
    )

logging.info("Created test_integration.py with new test cases.")

# Create new test_utils.py
with open(test_files_dir / "test_utils.py", "w") as f:
    f.write(
        """
import unittest
from fountainai_openapi_parser.utils import resolve_references
from pathlib import Path
import yaml

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.external_ref_path = Path(__file__).parent / "data/external_schema.yaml"

    def test_resolve_external_reference(self):
        with open(self.external_ref_path) as f:
            external_yaml = yaml.safe_load(f)
        resolved_data = resolve_references(external_yaml, base_path=Path(__file__).parent / "data")
        self.assertIn("example_field", resolved_data['components']['schemas']['ExampleSchema']['properties'])
    """
    )

logging.info("Created test_utils.py with new test cases.")
logging.info("All test files have been recreated with fresh test cases.")
