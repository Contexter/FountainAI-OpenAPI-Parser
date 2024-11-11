import os
import subprocess
import re


def fix_parser_file():
    parser_path = "fountainai_openapi_parser/parser.py"

    with open(parser_path, "r") as file:
        lines = file.readlines()

    corrected_lines = []
    for line in lines:
        # Fix indentation for specific line in parser.py
        if "content = source if isinstance(source, dict)" in line:
            corrected_lines.append(
                "    " + line.strip() + "\n"
            )  # Add indentation
        else:
            corrected_lines.append(line)

    with open(parser_path, "w") as file:
        file.writelines(corrected_lines)

    print(f"Corrected indentation in {parser_path}")


def fix_test_parser_file():
    test_parser_path = "tests/test_parser.py"

    with open(test_parser_path, "r") as file:
        content = file.read()

    # Ensure the assert statement is within a proper method
    content = re.sub(
        r"self\.assertIn\(\"/example\", parsed\.paths\)",
        '    self.assertIn("/example", parsed.paths)',
        content,
    )

    with open(test_parser_path, "w") as file:
        file.write(content)

    print(f"Fixed syntax in {test_parser_path}")


def run_tests():
    print("Running tests...")
    subprocess.run(
        [
            "PYTHONPATH=$(pwd)",
            "python",
            "-m",
            "unittest",
            "discover",
            "-s",
            "tests",
        ],
        shell=True,
    )


def main():
    fix_parser_file()
    fix_test_parser_file()
    run_tests()


if __name__ == "__main__":
    main()
