import os
import yaml

# Paths to files
parser_file_path = "fountainai_openapi_parser/parser.py"
utils_file_path = "fountainai_openapi_parser/utils.py"
test_parser_file_path = "tests/test_parser.py"


# Update `parse_openapi` function in `parser.py`
def update_parser_function():
    with open(parser_file_path, "r") as f:
        lines = f.readlines()

    with open(parser_file_path, "w") as f:
        for line in lines:
# Modify the line where `load_file` is called to bypass if `source` is a dict
            if "content = load_file(source, encoding)" in line:
                f.write(
"    content = source if isinstance(source, dict) else load_file(source,
encoding)\n"
                )
            else:
                f.write(line)
    print(f"Updated `parse_openapi` function in {parser_file_path}")


# Update `test_parser.py` to load YAML directly as a dictionary before passing
def update_test_parser():
    with open(test_parser_file_path, "r") as f:
        lines = f.readlines()

    with open(test_parser_file_path, "w") as f:
for line in lines:
            # Replace instances where files are passed directly to `parse_openapi`
            if "parse_openapi(" in line:
                line = line.replace(
                    "parse_openapi(", "parse_openapi(yaml.safe_load(open("
                )
                line = line.replace("))", ")), encoding='utf-8')")
            f.write(line)
    print(f"Updated `test_parser.py` to load YAML content as dictionaries.")


# Run the update functions
update_parser_function()
update_test_parser()

print("Modifications complete. Please run the tests to verify.")
