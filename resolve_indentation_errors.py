import re

def fix_indentation_errors(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    corrected_lines = []
    indentation_level = 0
    indent_stack = []

    for line in lines:
        stripped_line = line.lstrip()

        # Determine expected indentation
        if stripped_line.startswith("def ") or stripped_line.startswith("class "):
            indentation_level = 0
            indent_stack = []

        if stripped_line:
            leading_spaces = len(line) - len(stripped_line)

            # Adjust if leading spaces do not match the expected level
            if indent_stack and leading_spaces != indent_stack[-1]:
                line = ' ' * indent_stack[-1] + stripped_line
                leading_spaces = indent_stack[-1]

            corrected_lines.append(line)

            # Update indentation stack for nested levels
            if stripped_line.endswith(":"):
                if indent_stack and leading_spaces < indent_stack[-1]:
                    indent_stack.pop()
                indent_stack.append(leading_spaces + 4)  # Assume 4-space indentation

        else:
            corrected_lines.append(line)  # Preserve blank lines

    with open(file_path, "w") as file:
        file.writelines(corrected_lines)
    print(f"Indentation issues fixed in {file_path}")

# Usage example:
# fix_indentation_errors("path/to/your_script.py")

