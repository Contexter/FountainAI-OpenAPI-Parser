# save this as "format_and_check_flake8.py" in your repo root

import subprocess
import sys


# Step 1: Run black to autoformat the code to 79 characters
def run_black():
    print("Running Black to autoformat code to fit within 79 characters...")
    result = subprocess.run(
        ["black", ".", "--line-length", "79"],
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    print(result.stderr)


# Step 2: Run flake8 to check for remaining style issues
def run_flake8():
    print("\nRunning flake8 to check for style issues...")
    result = subprocess.run(
        ["flake8", "fountainai_openapi_parser"],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print("flake8 check passed, no issues found.")
    else:
        print("flake8 found some issues:\n")
        print(result.stdout)
        print(result.stderr)


# Execute steps
if __name__ == "__main__":
    run_black()
    run_flake8()
    print("\nFormatting and flake8 check complete.")
