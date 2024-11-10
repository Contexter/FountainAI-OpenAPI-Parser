import os
import subprocess

def create_github_workflow_directory(directory: str) -> None:
    """
    Ensure that the GitHub workflow directory exists.
    Args:
        directory (str): The path to the GitHub workflow directory.
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except PermissionError as e:
        print(f"Error: Permission denied while creating directory {directory}. {e}")
        raise
    except OSError as e:
        print(f"Error: Failed to create directory {directory}. {e}")
        raise

def write_github_workflow_file(file_path: str, content: str) -> None:
    """
    Write the GitHub Actions workflow content to the specified file.
    Args:
        file_path (str): The path to the workflow file.
        content (str): The content of the GitHub Actions workflow.
    """
    try:
        with open(file_path, "w") as workflow_file:
            workflow_file.write(content)
        print(f"GitHub Actions workflow has been created at {file_path}")
    except IOError as e:
        print(f"Error: Failed to write to file {file_path}. {e}")
        raise

def commit_and_push_workflow(file_path: str, commit_message: str) -> None:
    """
    Add the workflow file to Git, commit the changes, and push to the repository.
    Args:
        file_path (str): The path to the workflow file to be committed.
        commit_message (str): The commit message for the Git commit.
    """
    try:
        subprocess.run(["git", "add", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to add file to Git. {e}")
        raise

    try:
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to commit changes. {e}")
        raise

    try:
        subprocess.run(["git", "push", "origin", "main"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to push changes to the repository. {e}")
        raise

def main() -> None:
    """
    Main function to create the GitHub Actions CI/CD workflow file, commit, and push it.
    """
    # Define the YAML content for the GitHub Actions workflow
    github_workflow_content = """
    name: FountainAI OpenAPI Parser CI

    on:
      push:
        branches:
          - main
      pull_request:
        branches:
          - main

    jobs:
      test:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout repository
            uses: actions/checkout@v3

          - name: Set up Python
            uses: actions/setup-python@v4
            with:
              python-version: '3.9'

          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              pip install -r requirements.txt

          - name: Run Unit Tests
            run: |
              python -m unittest discover tests/
    """

    # Define the path for the GitHub Actions workflow file
    workflow_directory = ".github/workflows"
    workflow_file_path = os.path.join(workflow_directory, "ci.yml")

    # Create the GitHub workflow directory
    create_github_workflow_directory(workflow_directory)

    # Write the GitHub Actions workflow content to the file
    write_github_workflow_file(workflow_file_path, github_workflow_content)

    # Commit and push the workflow file to the repository
    commit_and_push_workflow(workflow_file_path, "ci: Add GitHub Actions workflow for CI/CD")

if __name__ == "__main__":
    main()
