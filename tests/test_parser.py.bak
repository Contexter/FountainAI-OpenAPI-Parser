import unittest
from pathlib import Path
from fountainai_openapi_parser.parser import parse_openapi
from fountainai_openapi_parser.exceptions import ParsingError, ValidationError, ReferenceResolutionError


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up example OpenAPI YAML content for testing.
        """
        # Example OpenAPI YAML content for testing
        self.valid_openapi_yaml: str = """
        openapi: 3.1.0
        info:
          title: Sample API
          version: 1.0.0
        paths:
          /example:
            get:
              summary: Example endpoint
              responses:
                '200':
                  description: Successful response
        """

        self.invalid_openapi_yaml: str = """
        openapi: 3.1.0
        info:
          title: Sample API
          version: 1.0.0
        paths: invalid_content
        """

        self.openapi_with_ref: str = """
        openapi: 3.1.0
        info:
          title: Sample API with Reference
          version: 1.0.0
        paths:
          /example:
            get:
              summary: Example endpoint
              responses:
                '200':
                  description: Successful response
                  content:
                    application/json:
                      schema:
                        $ref: '#/components/schemas/ExampleSchema'
        components:
          schemas:
            ExampleSchema:
              type: object
              properties:
                message:
                  type: string
        """

    def test_parse_valid_openapi_yaml(self) -> None:
        """
        Test parsing of a valid OpenAPI YAML document.
        """
        result = parse_openapi(self.valid_openapi_yaml)
        self.assertIsNotNone(result)
        self.assertEqual(result.info.title, "Sample API")

    def test_parse_invalid_openapi_yaml(self) -> None:
        """
        Test parsing of an invalid OpenAPI YAML document.
        """
        with self.assertRaises(ParsingError):
            parse_openapi(self.invalid_openapi_yaml)

    def test_parse_with_reference(self) -> None:
        """
        Test parsing of an OpenAPI YAML document with a local $ref reference.
        """
        result = parse_openapi(self.openapi_with_ref)
        self.assertIsNotNone(result)
        self.assertEqual(
            result.paths['/example'].get.responses['200'].content['application/json'].schema.type, "object"
        )

    def test_parse_nonexistent_file(self) -> None:
        """
        Test parsing a nonexistent file path.
        """
        with self.assertRaises(FileNotFoundError):
            parse_openapi(Path("nonexistent_file.yaml"))


if __name__ == "__main__":
    unittest.main()
