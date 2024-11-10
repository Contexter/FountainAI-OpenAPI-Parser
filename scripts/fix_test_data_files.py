import os
import yaml
import logging

logging.basicConfig(level=logging.INFO)

def ensure_directory_exists(path):
    os.makedirs(path, exist_ok=True)
    logging.info(f"Ensured test data directory exists at {path}")

def write_yaml(filepath, data):
    with open(filepath, 'w') as f:
        yaml.dump(data, f)
    logging.info(f"Updated YAML file at {filepath}")

def fix_invalid_openapi_yaml(path):
    # Use a dictionary with a placeholder invalid content
    invalid_openapi = {
        'openapi': '3.0.0',
        'info': {'title': 'Invalid API', 'version': '1.0.0'},
        'paths': {'/invalid': 'invalid_content'}  # placeholder to trigger validation error
    }
    write_yaml(path, invalid_openapi)

def fix_openapi_yaml(path):
    openapi_data = {
        'openapi': '3.0.0',
        'info': {'title': 'Sample API', 'version': '1.0.0'},
        'paths': {
            '/example': {
                'get': {
                    'responses': {
                        '200': {
                            'description': 'A successful response',
                            'content': {
                                'application/json': {
                                    'schema': {
                                        'type': 'object',  # Added type
                                        'properties': {
                                            'message': {'type': 'string'}
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
    write_yaml(path, openapi_data)

def fix_external_schema_yaml(path):
    external_schema = {
        'ExampleSchema': {  # Define ExampleSchema
            'type': 'object',
            'properties': {
                'example_field': {'type': 'string'}
            }
        }
    }
    write_yaml(path, external_schema)

def main():
    test_data_dir = os.path.join(os.path.dirname(__file__), '../tests/data')
    ensure_directory_exists(test_data_dir)

    # Fix invalid_openapi.yaml
    invalid_openapi_yaml_path = os.path.join(test_data_dir, 'invalid_openapi.yaml')
    fix_invalid_openapi_yaml(invalid_openapi_yaml_path)

    # Fix openapi.yaml
    openapi_yaml_path = os.path.join(test_data_dir, 'openapi.yaml')
    fix_openapi_yaml(openapi_yaml_path)

    # Fix external_schema.yaml
    external_schema_yaml_path = os.path.join(test_data_dir, 'external_schema.yaml')
    fix_external_schema_yaml(external_schema_yaml_path)

    logging.info("Validation and correction script completed.")

if __name__ == "__main__":
    main()
