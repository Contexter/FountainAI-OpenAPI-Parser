import unittest
import os
from fountainai_openapi_parser.parser import parse_openapi
from fountainai_openapi_parser.utils import resolve_references

class TestParserAuto(unittest.TestCase):
    
    def setUp(self):
        # Load test OpenAPI YAML files for testing
        self.sample_yaml_path = os.path.join(os.path.dirname(__file__), 'data', 'sample_openapi.yaml')
        self.external_yaml_path = os.path.join(os.path.dirname(__file__), 'data', 'external_schema.yaml')

    def test_parse_valid_openapi(self):
        """Test parsing of a valid OpenAPI YAML file"""
        with open(self.sample_yaml_path, 'r') as f:
            content = f.read()
        parsed_data = parse_openapi(content)
        self.assertIsNotNone(parsed_data)
        self.assertIn('paths', parsed_data)
        self.assertIn('components', parsed_data)

    def test_parse_invalid_openapi(self):
        """Test parsing of an invalid OpenAPI YAML file"""
        invalid_yaml = "invalid_content: true"
        with self.assertRaises(Exception):
            parse_openapi(invalid_yaml)

    def test_resolve_references(self):
        """Test resolving of $ref references in OpenAPI document"""
        with open(self.sample_yaml_path, 'r') as f:
            content = f.read()
        parsed_data = parse_openapi(content)
        resolved_data = resolve_references(parsed_data, base_path=self.sample_yaml_path)
        self.assertIsNotNone(resolved_data)
        # Ensure reference resolution is accurate by checking the resolved schema content
        self.assertIn('ExampleSchema', resolved_data.get('components', {}).get('schemas', {}))

    def test_external_reference_resolution(self):
        """Test resolution of external $ref references"""
        with open(self.external_yaml_path, 'r') as f:
            external_schema_yaml = f.read()
        with unittest.mock.patch('fountainai_openapi_parser.utils.load_file', return_value=external_schema_yaml):
            with open(self.sample_yaml_path, 'r') as f:
                content = f.read()
            parsed_data = parse_openapi(content)
            resolved_data = resolve_references(parsed_data, base_path=self.sample_yaml_path)
            self.assertIn('ExampleSchema', resolved_data.get('components', {}).get('schemas', {}))

if __name__ == "__main__":
    unittest.main()