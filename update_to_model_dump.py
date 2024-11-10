import os
import re

# Define the base directory for the project
BASE_DIR = "fountainai_openapi_parser"
TEST_DIR = "tests"

# Files to update
files_to_update = [
    os.path.join(BASE_DIR, "models.py"),
    os.path.join(BASE_DIR, "parser.py"),
    os.path.join(BASE_DIR, "utils.py"),
    os.path.join(TEST_DIR, "test_parser.py"),
    os.path.join(TEST_DIR, "test_utils.py")
]

# Regular expression to match .dict() calls
dict_pattern = re.compile(r'(\w+)\.dict\((.*?)\)')

def update_file(file_path):
    """Reads a file, replaces `.dict()` with `.model_dump()`, and writes it back."""
    changes_made = False
    with open(file_path, "r") as file:
        content = file.read()
    
    # Replace .dict() with .model_dump() using regex
    updated_content = dict_pattern.sub(r'\1.model_dump(\2)', content)

    # Check if any changes were made
    if content != updated_content:
        with open(file_path, "w") as file:
            file.write(updated_content)
        changes_made = True
    
    return changes_made

def main():
    """Main function to update all files in the specified list."""
    changes = {}
    for file_path in files_to_update:
        if os.path.exists(file_path):
            if update_file(file_path):
                changes[file_path] = "Updated"
            else:
                changes[file_path] = "No changes needed"
        else:
            changes[file_path] = "File not found"

    # Output the summary of changes
    print("\nUpdate Summary:")
    for file, status in changes.items():
        print(f"{file}: {status}")

if __name__ == "__main__":
    main()
