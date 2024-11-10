import sys
import os
import unittest

# Add the parent directory to the Python path to access fountainai_openapi_parser
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

from fountainai_openapi_parser.parser import parse_openapi  # Import the parse_openapi function

class AutoTestParser(unittest.TestCase):
    def setUp(self):
        # Example OpenAPI YAML content for testing
        self.valid_openapi_yaml = """
        openapi: "3.0.0"
        info:
          title: Test API
          version: "1.0.0"
        paths:
          /test:
            get:
              responses:
                '200':
                  description: Success
        """
        self.invalid_openapi_yaml = """
        openapi: "3.0.0"
        info:
          title: Test API
          version: "1.0.0"
        paths:
          invalid_content
        """

    def test_parse_valid_openapi_yaml(self):
        """Test parsing of a valid OpenAPI YAML document."""
        result = parse_openapi(self.valid_openapi_yaml)
        self.assertIsNotNone(result)
        self.assertEqual(result.info.title, "Test API")
        self.assertEqual(result.info.version, "1.0.0")

    def test_parse_invalid_openapi_yaml(self):
        """Test parsing of an invalid OpenAPI YAML document."""
        with self.assertRaises(Exception):
            parse_openapi(self.invalid_openapi_yaml)

if __name__ == "__main__":
    unittest.main()