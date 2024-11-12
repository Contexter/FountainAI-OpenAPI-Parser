import os
    from string import Template
import ast

# Define the base paths for the parser and test directories
BASE_DIR = 'fountainai_openapi_parser'
MODELS_DIR = os.path.join(BASE_DIR, 'models')
TESTS_DIR = 'tests'

# Step 1: Create Models Directory
def create_models_directory():
    """Create the directory for storing individual model files."""
    os.makedirs(MODELS_DIR, exist_ok=True)
    print(f"Ensured directory exists: {MODELS_DIR}")

# Step 2: Split Models into Separate Files
def split_models():
    """Split models.py into separate files for each model class."""
    models_file = os.path.join(BASE_DIR, 'models.py')
    if not os.path.exists(models_file):
        raise FileNotFoundError(f"models.py not found in {BASE_DIR}")

    with open(models_file, 'r') as f:
        # Process the file line by line for better memory efficiency
        models_code_lines = f.readlines()

    # Parse the models.py file using AST to extract class definitions
    models_code = ''.join(models_code_lines)
    tree = ast.parse(models_code)
    
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            model_name = node.name
            model_code = ast.get_source_segment(models_code, node)

            model_file = os.path.join(MODELS_DIR, f"{model_name.lower()}.py")
            with open(model_file, 'w') as f:
                f.write(model_code)
            print(f"Created model file: {model_file}")

# Step 3: Create __init__.py for Models Directory
def create_init_file():
    """Create an __init__.py file to import all model classes for easy access."""
    init_file = os.path.join(MODELS_DIR, '__init__.py')
    with open(init_file, 'w') as f:
        for file_name in os.listdir(MODELS_DIR):
            if file_name.endswith('.py') and file_name != '__init__.py':
                module_name = file_name[:-3]
                f.write(f'from .{module_name} import *\n')
    print(f"Created __init__.py in {MODELS_DIR}")

# Step 4: Create Utility to Assemble Models
def create_assemble_utility():
    """Create a utility script to assemble all models into a dictionary."""
    assemble_file = os.path.join(MODELS_DIR, 'assemble.py')
    with open(assemble_file, 'w') as f:
        f.write("from . import *\n\n")
        f.write("def get_models():\n")
        f.write("    return {\n")
        for file_name in os.listdir(MODELS_DIR):
            if file_name.endswith('.py') and file_name not in ['__init__.py', 'assemble.py']:
                model_name = file_name[:-3]
                f.write(f"        '{model_name}': {model_name},\n")
        f.write("    }\n")
    print(f"Created assemble utility: {assemble_file}")

# Step 5: Update Parser to Use Assemble Utility
def update_parser():
    """Update parser.py to use the assemble utility for accessing models."""
    parser_file = os.path.join(BASE_DIR, 'parser.py')
    if not os.path.exists(parser_file):
        raise FileNotFoundError(f"parser.py not found in {BASE_DIR}")

    with open(parser_file, 'r') as f:
        parser_code = f.read()

    updated_code = "from .models.assemble import get_models\n" + parser_code
    with open(parser_file, 'w') as f:
        f.write(updated_code)
    print(f"Updated parser to use assemble utility: {parser_file}")

# Step 6: Create Unit Test Files for Each Model
def create_unit_tests():
    """Create individual unit test files for each model class."""
    os.makedirs(TESTS_DIR, exist_ok=True)
    print(f"Ensured tests directory exists: {TESTS_DIR}")

    test_template = Template("""
import unittest
    from fountainai_openapi_parser.models.$model_name import $model_name

class Test$model_name(unittest.TestCase):
    def test_initialization(self):
        # Add tests for $model_name here
        pass

if __name__ == '__main__':
    unittest.main()
""")

    for file_name in os.listdir(MODELS_DIR):
        if file_name.endswith('.py') and file_name not in ['__init__.py', 'assemble.py']:
            model_name = file_name[:-3]
            test_code = test_template.substitute(model_name=model_name)
            test_file = os.path.join(TESTS_DIR, f"test_{model_name}.py")
            with open(test_file, 'w') as f:
                f.write(test_code)
            print(f"Created test file: {test_file}")

# Main Execution
def main():
    """Main function to execute all steps of the refactoring process."""
    create_models_directory()
    split_models()
    create_init_file()
    create_assemble_utility()
    update_parser()
    create_unit_tests()

if __name__ == "__main__":
    main()

