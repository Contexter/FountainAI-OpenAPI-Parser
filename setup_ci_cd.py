import yaml
import os

# Define the file path for the CI/CD pipeline YAML file
ci_cd_file_path = '.github/workflows/ci.yml'

# Define the pipeline modifications
new_steps = [
    {
        'name': 'Run Linter (Flake8)',
        'run': 'pip install flake8\nflake8 fountainai_openapi_parser'
    },
    {
        'name': 'Run Type Checking (Mypy)',
        'run': 'pip install mypy\nmypy fountainai_openapi_parser'
    },
    {
        'name': 'Check Code Formatting (Black)',
        'run': 'pip install black\nblack --check fountainai_openapi_parser'
    },
]

# Update the CI/CD YAML file
def update_ci_pipeline():
    if os.path.exists(ci_cd_file_path):
        with open(ci_cd_file_path, 'r') as file:
            pipeline = yaml.safe_load(file)
        
        # Add new steps in the 'jobs -> test -> steps' section
        pipeline['jobs']['test']['steps'].extend(new_steps)
        
        # Write the updated pipeline back to the file
        with open(ci_cd_file_path, 'w') as file:
            yaml.dump(pipeline, file)
        print(f"Updated {ci_cd_file_path} with linter and type-checking steps.")
    else:
        print(f"{ci_cd_file_path} not found. Please ensure the file path is correct.")

# Create configuration files if they do not exist
def create_config_files():
    # Flake8 configuration
    flake8_config = "[flake8]\nmax-line-length = 100\n"
    with open('.flake8', 'w') as file:
        file.write(flake8_config)
    print("Created .flake8 configuration file.")

    # Mypy configuration
    mypy_config = "[mypy]\nignore_missing_imports = True\n"
    with open('mypy.ini', 'w') as file:
        file.write(mypy_config)
    print("Created mypy.ini configuration file.")

    # Black configuration
    black_config = "[tool.black]\nline-length = 100\n"
    with open('pyproject.toml', 'w') as file:
        file.write(black_config)
    print("Created pyproject.toml configuration file for Black.")

# Run the functions
update_ci_pipeline()
create_config_files()

