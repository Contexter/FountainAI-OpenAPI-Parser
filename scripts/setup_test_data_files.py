import os
import logging
import yaml

logging.basicConfig(level=logging.INFO)

# Directory paths
base_dir = os.path.dirname(os.path.abspath(__file__))
test_data_dir = os.path.join(base_dir, "../tests/data")

# File paths
invalid_openapi_path = os.path.join(test_data_dir, "invalid_openapi.yaml")
valid_openapi_path = os.path.join(test_data_dir, "openapi.yaml")
external_schema_path = os.path.join(test_data_dir, "external_schema.yaml")

# Ensure the test data directory exists
os.makedirs(test_data_dir, exist_ok=True)
logging.info(f"Ensured test data directory exists at {test_data_dir}")

# Content for invalid_openapi.yaml
invalid_openapi_content = {
    "openapi": "3.0.0",
    "info": {
        "title": "Invalid API",
        "version": "1.0.0"
    },
    "paths": "invalid_content"  # This is intentionally incorrect
}

# Content for openapi.yaml
valid_openapi_content = {
    "openapi": "3.0.0",
    "info": {
        "title": "Valid API",
        "version": "1.0.0"
    },
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
                                        "message": {
                                            "type": "string"
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
}

# Content for external_schema.yaml
external_schema_content = {
    "ExampleSchema": {
        "type": "object",
        "properties": {
            "example_field": {
                "type": "string"
            }
        }
    }
}

# Write invalid_openapi.yaml
with open(invalid_openapi_path, 'w') as file:
    yaml.dump(invalid_openapi_content, file)
    logging.info(f"Invalid OpenAPI YAML written to {invalid_openapi_path}")

# Write openapi.yaml
with open(valid_openapi_path, 'w') as file:
    yaml.dump(valid_openapi_content, file)
    logging.info(f"Valid OpenAPI YAML written to {valid_openapi_path}")

# Write external_schema.yaml
with open(external_schema_path, 'w') as file:
    yaml.dump(external_schema_content, file)
    logging.info(f"External schema YAML written to {external_schema_path}")

# Notify script completion
logging.info("YAML setup completed. Now you can run your tests using `python -m unittest discover -s tests`.")

