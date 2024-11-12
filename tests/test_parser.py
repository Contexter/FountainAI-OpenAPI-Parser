import unittest
from fountainai_openapi_parser.parser import parse_openapi, OpenAPI
from fountainai_openapi_parser.exceptions import ParsingError, ValidationError, ReferenceResolutionError

# Issue #41: Added tests to validate the basic parsing of `openapi.yaml` for standard OpenAPI documents as part of foundational core parser functionality.

class TestParser(unittest.TestCase):

    def setUp(self):
        # Sample valid OpenAPI 3.1 document
        self.valid_openapi_yaml = {
            "openapi": "3.1.0",
            "info": {"title": "Sample API", "version": "1.0.0"},
            "paths": {
                "/example": {
                    "get": {
                        "responses": {
                            "200": {
                                "description": "A successful response",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$schema": "https://json-schema.org/draft/2020-12/schema",
                                            "type": "object",
                                            "properties": {
                                                "example_field": {
                                                    "type": "string"
                                                }
                                            },
                                        }
                                    }
                                },
                            }
                        }
                    }
                }
            },
            "components": {
                "schemas": {
                    "Pet": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"},
                            "tag": {"type": "string"}
                        }
                    },
                    "Error": {
                        "type": "object",
                        "properties": {
                            "code": {"type": "integer"},
                            "message": {"type": "string"}
                        }
                    }
                }
            }
        }

        # Sample invalid OpenAPI document
        self.invalid_openapi_yaml = {
            "openapi": "3.1.0",
            "info": "Invalid structure",
            "paths": "invalid_content",
        }

        # Sample OpenAPI document with reference resolution error
        self.ref_resolution_error_yaml = {
            "openapi": "3.1.0",
            "info": {"title": "Sample API with Reference", "version": "1.0.0"},
            "paths": {
                "/pets": {
                    "get": {
                        "responses": {
                            "200": {
                                "description": "A list of pets.",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/NonExistentSchema"
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
                    "Pet": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"},
                            "tag": {"type": "string"}
                        }
                    }
                }
            }
        }

    def test_parse_valid_openapi_yaml(self):
        # Test parsing a valid OpenAPI document
        parsed = parse_openapi(self.valid_openapi_yaml)
        self.assertIsInstance(parsed, OpenAPI)
        self.assertIn("/example", parsed.paths)
        # Check that the schema type for the /example path is correctly parsed as 'object'
        self.assertEqual(
            parsed.paths["/example"]["get"]["responses"]["200"]["content"][
                "application/json"
            ]["schema"]["type"],
            "object",
        )

    def test_parse_invalid_openapi_yaml(self):
        # Test parsing an invalid OpenAPI document, should raise ParsingError or ValidationError
        with self.assertRaises((ParsingError, ValidationError)):
            parse_openapi(self.invalid_openapi_yaml)

    def test_parse_ref_resolution_error_yaml(self):
        # Test parsing an OpenAPI document with reference resolution error
        with self.assertRaises(ReferenceResolutionError):
            parse_openapi(self.ref_resolution_error_yaml)

    def test_paths_existence(self):
        """Test that paths are correctly parsed."""
        parsed = parse_openapi(self.valid_openapi_yaml)
        # Check that the expected paths exist in the parsed data
        self.assertIn('/example', parsed.paths, "Path '/example' should exist in parsed data.")

    def test_methods_existence(self):
        """Test that HTTP methods are correctly parsed for each path."""
        parsed = parse_openapi(self.valid_openapi_yaml)
        # Check that the GET method exists for the /example path
        self.assertIn('get', parsed.paths['/example'], "Method 'get' should be available for path '/example'.")

    def test_responses_parsing(self):
        """Test that responses are correctly parsed for a method."""
        parsed = parse_openapi(self.valid_openapi_yaml)
        responses = parsed.paths['/example']['get']['responses']
        # Check that the response code 200 is present for the GET /example method
        self.assertIn('200', responses, "Response 200 should be defined for GET /example.")
        # Verify that the description for response 200 is correct
        self.assertEqual(responses['200']['description'], 'A successful response')

    def test_schemas(self):
        """Test that schemas in components are parsed correctly."""
        parsed = parse_openapi(self.valid_openapi_yaml)
        # Check that the 'Pet' and 'Error' schemas are present in the components section
        self.assertIn('Pet', parsed.components['schemas'], "Schema 'Pet' should be present in components.")
        self.assertIn('Error', parsed.components['schemas'], "Schema 'Error' should be present in components.")

    def test_schema_properties(self):
        """Test that the properties of schemas are correctly parsed."""
        parsed = parse_openapi(self.valid_openapi_yaml)
        pet_schema = parsed.components['schemas']['Pet']
        # Verify that the properties 'id', 'name', and 'tag' are present in the 'Pet' schema
        self.assertIn('id', pet_schema['properties'], "Property 'id' should be in 'Pet' schema.")
        self.assertIn('name', pet_schema['properties'], "Property 'name' should be in 'Pet' schema.")
        self.assertIn('tag', pet_schema['properties'], "Property 'tag' should be in 'Pet' schema.")

    def test_info_parsing(self):
        """Test that the info section is parsed correctly."""
        parsed = parse_openapi(self.valid_openapi_yaml)
        # Verify that the title and version are correctly parsed in the info section
        self.assertEqual(parsed.info['title'], 'Sample API', "The title should be 'Sample API'.")
        self.assertEqual(parsed.info['version'], '1.0.0', "The version should be '1.0.0'.")

    def test_component_schemas_existence(self):
        """Test that component schemas are correctly identified and parsed."""
        parsed = parse_openapi(self.valid_openapi_yaml)
        self.assertIn('Pet', parsed.components['schemas'], "Component schema 'Pet' should be present.")
        self.assertIn('Error', parsed.components['schemas'], "Component schema 'Error' should be present.")

    def test_parse_standard_openapi_document(self):
        """Issue #41: Test parsing a standard OpenAPI document to validate core functionality."""
        parsed = parse_openapi(self.valid_openapi_yaml)
        self.assertIsInstance(parsed, OpenAPI, "Parsed object should be an instance of OpenAPI.")
        # Ensure no errors are raised and all key sections are parsed
        self.assertIn('paths', parsed.__dict__, "Parsed document should contain 'paths'.")
        self.assertIn('components', parsed.__dict__, "Parsed document should contain 'components'.")

# Run the tests
if __name__ == '__main__':
    unittest.main()
