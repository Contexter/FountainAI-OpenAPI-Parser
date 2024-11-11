import os
import re
import subprocess
import autopep8


def run_black():
    """Run Black to format code to fit within 79 characters."""
    print("\nRunning Black to autoformat code to fit within 79 characters...")
    subprocess.run(["black", ".", "--line-length", "79"], check=True)
    print("\nBlack formatting complete.\n")


def run_flake8():
    """Run flake8 to check for style issues."""
    print("\nRunning flake8 to check for style issues...")
    result = subprocess.run(["flake8", "."], capture_output=True, text=True)
    if result.returncode != 0:
        issues = result.stdout
        print("\nflake8 found some issues:\n")
        print(issues)
        process_flake8_issues(issues)
    else:
        print("\nNo flake8 issues found. Code is clean!\n")


def process_flake8_issues(issues):
    """Process flake8 issues and attempt automated fixes."""
    lines = issues.splitlines()
    for line in lines:
        if "F401" in line:  # Unused import
            handle_unused_import(line)
        elif "E501" in line:  # Line too long
            handle_line_too_long(line)
        elif "F821" in line:  # Undefined name
            handle_undefined_name(line)
        elif "E999" in line:  # Syntax error
            handle_syntax_error(line)


def handle_unused_import(issue_line):
    """Remove unused imports based on flake8 F401 warnings."""
    filepath, line_number, _, _ = issue_line.split(":", 3)
    line_number = int(line_number)
    with open(filepath, "r") as file:
        lines = file.readlines()
    if line_number <= len(lines):
        print(f"Removing unused import in {filepath} at line {line_number}")
        lines.pop(line_number - 1)
    with open(filepath, "w") as file:
        file.writelines(lines)


def handle_line_too_long(issue_line):
    """Attempt to split long lines based on flake8 E501 warnings."""
    filepath, line_number, _, _ = issue_line.split(":", 3)
    line_number = int(line_number)
    with open(filepath, "r") as file:
        lines = file.readlines()
    if line_number <= len(lines):
        long_line = lines[line_number - 1]
        print(f"Splitting long line in {filepath} at line {line_number}")
        fixed_line = autopep8.fix_code(
            long_line, options={"max_line_length": 79}
        )
        lines[line_number - 1] = fixed_line
    with open(filepath, "w") as file:
        file.writelines(lines)


def handle_undefined_name(issue_line):
    """Insert placeholder for undefined names based on flake8 F821 warnings."""
    filepath, line_number, _, message = issue_line.split(":", 3)
    undefined_name = re.search(r"'(.+)'", message)
    if undefined_name:
        name = undefined_name.group(1)
        line_number = int(line_number)
        with open(filepath, "r") as file:
            lines = file.readlines()
        if line_number <= len(lines):
            print(
                f"Adding placeholder for undefined name '{name}' in {filepath} at line {line_number}"
            )
            # Insert a placeholder for the undefined name
            placeholder = f"# TODO: Define '{name}'\n{name} = None  # Placeholder for undefined name\n"
            lines.insert(line_number, placeholder)
        with open(filepath, "w") as file:
            file.writelines(lines)


def handle_syntax_error(issue_line):
    """Add a TODO comment for syntax errors based on flake8 E999 warnings."""
    filepath, line_number, _, _ = issue_line.split(":", 3)
    line_number = int(line_number)
    with open(filepath, "r") as file:
        lines = file.readlines()
    if line_number <= len(lines):
        print(
            f"Adding TODO for syntax error in {filepath} at line {line_number}"
        )
        # Add a TODO comment above the syntax error line
        todo_comment = f"# TODO: Review and fix syntax error below\n"
        lines.insert(line_number - 1, todo_comment)
    with open(filepath, "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    run_black()
    run_flake8()
    print("\nFormatting and flake8 check complete.\n")
