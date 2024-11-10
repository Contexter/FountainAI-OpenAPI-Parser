import unittest
from fountainai_openapi_parser.parser import parse_openapi, OpenAPI

class TestParser(unittest.TestCase):

    def setUp(self):
        self.valid_openapi_yaml = {
            "openapi": "3.0.0",
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
                                            "type": "object",
                                            "properties": {
                                                "example_field": {"type": "string"}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        self.invalid_openapi_yaml = {
            "openapi": "3.0.0",
            "info": "Invalid structure",
            "paths": "invalid_content"
        }

    def test_parse_valid_openapi_yaml(self):
        parsed = parse_openapi(self.valid_openapi_yaml)
        self.assertIsInstance(parsed, OpenAPI)
        self.assertIn("/example", parsed.paths)
        self.assertEqual(
            parsed.paths["/example"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]["type"],
            "object"
        )

    def test_parse_invalid_openapi_yaml(self):
        with self.assertRaises(ValueError):
            parse_openapi(self.invalid_openapi_yaml)

if __name__ == "__main__":
    unittest.main()
