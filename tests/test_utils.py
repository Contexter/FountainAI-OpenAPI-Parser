import unittest
from pathlib import Path
import yaml
import json
from fountainai_openapi_parser.utils import load_file, resolve_references
from fountainai_openapi_parser.exceptions import ReferenceResolutionError


class TestUtils(unittest.TestCase):
    def setUp(self):
        # Example OpenAPI document for testing
        self.openapi_document = {
            "openapi": "3.1.0",
            "info": {
                "title": "Sample API",
                "version": "1.0.0"
            },
            "paths": {
                "/example": {
                    "get": {
                        "summary": "Example endpoint",
                        "responses": {
                            "200": {
                                "description": "Successful response"
                            }
                        }
                    }
                }
            }
        }

        self.openapi_with_ref = {
            "openapi": "3.1.0",
            "info": {
                "title": "Sample API with Reference",
                "version": "1.0.0"
            },
            "paths": {
                "/example": {
                    "get": {
                        "summary": "Example endpoint",
                        "responses": {
                            "200": {
                                "description": "Successful response",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/ExampleSchema"
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
                        "properties": {
                            "message": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }

    def test_load_file_from_path(self):
        # Test loading content from a file path
        path = Path("test_openapi.yaml")
        content = yaml.dump(self.openapi_document)
        path.write_text(content)

        try:
            result = load_file(path)
            self.assertEqual(result, content)
        finally:
            path.unlink()  # Clean up after test

    def test_load_file_from_string(self):
        # Test loading content directly from a string
        content = yaml.dump(self.openapi_document)
        result = load_file(content)
        self.assertEqual(result, content)

    def test_resolve_local_reference(self):
        # Test resolving a local $ref reference
        try:
            resolved_document = resolve_references(self.openapi_with_ref)
            self.assertIn("components", resolved_document)
            self.assertEqual(
                resolved_document["paths"]["/example"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]["type"],
                "object"
            )
        except ReferenceResolutionError as e:
            self.fail(f"Unexpected reference resolution error: {e}")

    def test_resolve_missing_reference(self):
        # Test resolving a missing $ref reference
        document_with_missing_ref = {
            "openapi": "3.1.0",
            "info": {
                "title": "Sample API with Missing Reference",
                "version": "1.0.0"
            },
            "paths": {
                "/example": {
                    "get": {
                        "summary": "Example endpoint",
                        "responses": {
                            "200": {
                                "description": "Successful response",
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
            }
        }

        with self.assertRaises(ReferenceResolutionError):
            resolve_references(document_with_missing_ref)


if __name__ == "__main__":
    unittest.main()

