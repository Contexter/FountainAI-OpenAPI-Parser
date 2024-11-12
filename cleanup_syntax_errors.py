# cleanup_syntax_errors.py

import re

def fix_syntax_errors(file_content):
    # Fix concatenated imports and separate statements without proper delimiters
    fixed_lines = []
    for line in file_content.splitlines():
        # Detect concatenated imports without proper separation
        if re.search(r'from\s+\w+\s+import\s+\w+from\s+', line):
            line = re.sub(r'from\s+(\w+)\s+import\s+(\w+)from\s+', r'from \1 import \2\nfrom ', line)

        # Detect common patterns with improper concatenation in imports
        if "import" in line and "from" in line:
            # Ensure there's only one 'from' and 'import' in each line
            split_line = re.split(r'(from\s+\w+\s+import\s+)', line)
            if len(split_line) > 2:
                line = '\n'.join(split_line[i] + split_line[i + 1].strip() for i in range(0, len(split_line) - 1, 2))

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)


def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    fixed_content = fix_syntax_errors(content)

    with open(file_path, 'w') as file:
        file.write(fixed_content)


def main():
    import os

    # Define the directory where we need to process files
    directory = "fountainai_openapi_parser"

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                process_file(os.path.join(root, file))


if __name__ == "__main__":
    main()
