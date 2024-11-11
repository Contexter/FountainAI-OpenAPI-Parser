import subprocess
import re
import os


def run_black():
    """Run black to autoformat the code."""
    print(
        "\nRunning Black to autoformat code to fit within 79 characters...\n"
    )
    subprocess.run(["black", ".", "--line-length", "79"])
    print("\nBlack formatting complete.\n")


def run_flake8():
    """Run flake8 to check for style issues."""
    print("\nRunning flake8 to check for style issues...\n")
    result = subprocess.run(
        ["flake8", "--max-line-length=79"], stdout=subprocess.PIPE, text=True
    )
    issues = result.stdout.strip()
    if issues:
        print("flake8 found some issues:\n")
        print(issues)
    else:
        print("No flake8 issues found!")
    return issues


def process_flake8_issues(issues):
    """Process and manually wrap long lines flagged by flake8."""
    lines_to_edit = []
    for line in issues.splitlines():
        match = re.search(
            r"(.+):(\d+):(\d+): E501 line too long \((\d+) > 79 characters\)",
            line,
        )
        if match:
            file_path, line_no = match.group(1), int(match.group(2))
            lines_to_edit.append((file_path, line_no))

    # Process each line that exceeds 79 characters
    for file_path, line_no in lines_to_edit:
        with open(file_path, "r") as f:
            lines = f.readlines()

        long_line = lines[line_no - 1].strip()
        if long_line:
            # Insert line breaks manually at logical split points
            split_lines = split_long_line(long_line)
            lines[line_no - 1] = split_lines

            # Write the adjusted content back to the file
            with open(file_path, "w") as f:
                f.writelines(lines)


def split_long_line(line, max_length=79):
    """Splits a long line into multiple lines within the max length limit."""
    words = line.split(" ")
    new_line = ""
    split_lines = []

    for word in words:
        # Check if adding the next word would exceed max length
        if len(new_line) + len(word) + 1 <= max_length:
            new_line += word + " "
        else:
            split_lines.append(new_line.strip() + "\n")
            new_line = word + " "

    if new_line:
        split_lines.append(new_line.strip() + "\n")

    return "".join(split_lines)


if __name__ == "__main__":
    run_black()
    flake8_issues = run_flake8()

    if flake8_issues:
        print("\nProcessing flake8 line length issues...\n")
        process_flake8_issues(flake8_issues)
        print("\nRe-running flake8 check to confirm resolution...\n")
        run_flake8()
    else:
        print("No line length issues to process.")

    print("\nFormatting and flake8 check complete.")
