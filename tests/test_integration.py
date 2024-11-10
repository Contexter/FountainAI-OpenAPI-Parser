from unittest import mock
import unittest
from pathlib import Path
from fountainai_openapi_parser.parser import parse_openapi
from fountainai_openapi_parser.utils import resolve_references
from fountainai_openapi_parser.exceptions import ParsingError, ValidationError, ReferenceResolutionError


class TestIntegration(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up example OpenAPI documents for integration testing.
        """
        self.simple_openapi_yaml = """
        openapi: 3.1.0
        info:
          title: Simple API
          version: 1.0.0
        paths:
          /simple:
            get:
              summary: Simple endpoint
              responses:
                '200':
                  description: Successful response
        """

        self.openapi_with_nested_refs = """
        openapi: 3.1.0
        info:
          title: API with Nested References
          version: 1.0.0
        paths:
          /nested:
            get:
              summary: Nested reference endpoint
              responses:
                '200':
                  description: Successful response
                  content:
                    application/json:
                      schema:
                        $ref: '#/components/schemas/ParentSchema'
        components:
          schemas:
            ParentSchema:
              type: object
              properties:
                child:
                  $ref: '#/components/schemas/ChildSchema'
            ChildSchema:
              type: object
              properties:
                message:
                  type: string
        """

        self.openapi_with_external_ref = """
        openapi: 3.1.0
        info:
          title: API with External Reference
          version: 1.0.0
        paths:
          /external:
            get:
              summary: External reference endpoint
              responses:
                '200':
                  description: Successful response
                  content:
                    application/json:
                      schema:
                        $ref: 'external_schema.yaml#/components/schemas/ExternalSchema'
        """

    def test_simple_openapi_parsing(self) -> None:
        """
        Test parsing a simple OpenAPI YAML document without references.
        """
        try:
            result = parse_openapi(self.simple_openapi_yaml)
            self.assertIsNotNone(result)
            self.assertEqual(result.info.title, "Simple API")
        except Exception as e:
            self.fail(f"Unexpected exception raised: {e}")

    def test_nested_reference_resolution(self) -> None:
        """
        Test parsing and resolving nested references in an OpenAPI document.
        """
        try:
            result = parse_openapi(self.openapi_with_nested_refs)
            self.assertIsNotNone(result)
            resolved_result = resolve_references(result.model_dump())
            self.assertIsNotNone(resolved_result)
            self.assertIn('ParentSchema', resolved_result['components']['schemas'])
            self.assertIn('ChildSchema', resolved_result['components']['schemas'])
        except ReferenceResolutionError as e:
            self.fail(f"Reference resolution failed unexpectedly: {e}")

    def test_external_reference_resolution(self) -> None:
        """
        Test parsing an OpenAPI document with an external reference.
        """
        # Mocking the external file load for simplicity
        external_schema_yaml = """
        components:
          schemas:
            ExternalSchema:
              type: object
              properties:
                data:
                  type: string
        """
        try:
            # Simulate loading the external file
            with unittest.mock.patch('fountainai_openapi_parser.utils.load_file', return_value=external_schema_yaml):
                result = parse_openapi(self.openapi_with_external_ref)
                self.assertIsNotNone(result)
                resolved_result = resolve_references(result.model_dump(), base_path=Path("."))
                self.assertIsNotNone(resolved_result)
                self.assertIn('ExternalSchema', resolved_result['components']['schemas'])
        except ReferenceResolutionError as e:
            self.fail(f"External reference resolution failed unexpectedly: {e}")


if __name__ == "__main__":
    unittest.main()

