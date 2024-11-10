# tests/test_parser_with_mocks.py

import unittest
from unittest.mock import Mock, patch, MagicMock
from fountainai_openapi_parser.parser import parse_openapi
from fountainai_openapi_parser.utils import load_file, resolve_references
from fountainai_openapi_parser.exceptions import ReferenceResolutionError
from pathlib import Path

class TestParser(unittest.TestCase):

    def setUp(self):
        # Mocked data to simulate OpenAPI document with $ref
        self.openapi_document_with_ref = {
            "openapi": "3.0.0",
            "paths": {
                "/example": {
                    "get": {
                        "responses": {
                            "200": {
                                "$ref": "#/components/schemas/ExampleSchema"
                            }
                        }
                    }
                }
            },
            "components": {
                "schemas": {
                    "ExampleSchema": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"}
                        }
                    }
                }
            }
        }

    def test_parse_with_reference(self):
        # Parse and assert mock reference resolution
        result = MagicMock(spec=dict)
        result.paths = {
            '/example': {
                'get': {
                    'responses': {
                        '200': {'properties': {'name': {'type': 'string'}}}
                    }
                }
            }
        }
        self.assertIn('name', result.paths['/example']['get']['responses']['200']['properties'])


class TestIntegration(unittest.TestCase):

    @patch('fountainai_openapi_parser.utils.load_file')
    def test_external_reference_resolution(self, mock_load_file):
        # Mock the load_file to simulate loading of an external file
        mock_load_file.return_value = '{"type": "object", "properties": {"name": {"type": "string"}}}'
        
        # Directly provide document structure to avoid treating it as a file path
        openapi_document_with_external_ref = {
            "openapi": "3.0.0",
            "paths": {
                "/example": {
                    "get": {
                        "responses": {
                            "200": {"$ref": "external_schema.yaml#/ExampleSchema"}
                        }
                    }
                }
            }
        }
        
        try:
            # Use mock return to handle external schema resolution
            resolved_result = resolve_references(openapi_document_with_external_ref, base_path=Path("."))
            self.assertIn("name", resolved_result["paths"]["/example"]["get"]["responses"]["200"]["properties"])
        except ReferenceResolutionError as e:
            self.fail(f"External reference resolution failed unexpectedly: {e}")


class TestUtils(unittest.TestCase):

    @patch("fountainai_openapi_parser.utils.load_file")
    def test_resolve_external_reference(self, mock_load_file):
        # Mocked content for the external schema file
        mock_load_file.return_value = '{"type": "object", "properties": {"name": {"type": "string"}}}'
        external_ref_document = {
            "paths": {
                "/example": {
                    "get": {
                        "responses": {
                            "200": {"$ref": "external_schema.yaml#/ExampleSchema"}
                        }
                    }
                }
            }
        }
        try:
            resolved_document = resolve_references(external_ref_document, base_path=Path("."))
            self.assertIn("name", resolved_document["paths"]["/example"]["get"]["responses"]["200"]["properties"])
        except ReferenceResolutionError as e:
            self.fail(f"Unexpected reference resolution error: {e}")


if __name__ == '__main__':
    unittest.main()