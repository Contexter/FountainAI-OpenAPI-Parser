import os
import shutil
import yaml
import logging

# Configure logging to track script actions
logging.basicConfig(
    filename="ci_cd_script.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Paths
workflow_directory = ".github/workflows"
workflow_file = os.path.join(workflow_directory, "ci.yml")
backup_directory = "backups"

# Ensure backup directory exists
os.makedirs(backup_directory, exist_ok=True)


def backup_file(file_path):
    """Backup a file if it exists to avoid accidental overwrites."""
    if os.path.exists(file_path):
        backup_path = os.path.join(
            backup_directory, os.path.basename(file_path)
        )
        shutil.copy(file_path, backup_path)
        logging.info(f"Backup created for {file_path} at {backup_path}")
    else:
        logging.info(f"No existing file found for backup at {file_path}")


def load_yaml(file_path):
    """Load a YAML file if it exists."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            logging.info(f"Loading YAML file: {file_path}")
            return yaml.safe_load(file)
    else:
        logging.warning(f"File not found: {file_path}")
        return None


def save_yaml(data, file_path):
    """Save data as a YAML file, ensuring not to overwrite existing configurations."""
    backup_file(file_path)
    with open(file_path, "w") as file:
        yaml.dump(data, file)
        logging.info(f"Saved YAML configuration to {file_path}")


def ensure_workflow_directory():
    """Create the workflow directory if it doesn't exist."""
    if not os.path.exists(workflow_directory):
        os.makedirs(workflow_directory)
        logging.info(f"Created workflow directory at {workflow_directory}")
    else:
        logging.info(
            f"Workflow directory already exists at {workflow_directory}"
        )


def update_workflow():
    """Update or create the GitHub Actions workflow if it does not exist."""
    current_config = load_yaml(workflow_file)

    if current_config is not None:
        # Check for specific keys or elements to avoid redundant changes
        if "jobs" in current_config and "test" in current_config["jobs"]:
            logging.info(
                "Workflow file already contains the necessary jobs. Skipping update."
            )
            return
        else:
            logging.info(
                "Updating existing workflow with additional configurations."
            )
    else:
        logging.info("Creating a new workflow file as none exists.")

    # Define new workflow configuration
    new_workflow = {
        "name": "CI Pipeline",
        "on": ["push", "pull_request"],
        "jobs": {
            "test": {
                "runs-on": "ubuntu-latest",
                "steps": [
                    {"name": "Checkout", "uses": "actions/checkout@v2"},
                    {
                        "name": "Set up Python",
                        "uses": "actions/setup-python@v2",
                        "with": {"python-version": "3.9"},
                    },
                    {
                        "name": "Install dependencies",
                        "run": "pip install -r requirements.txt",
                    },
                    {
                        "name": "Run tests",
                        "run": "python -m unittest discover -s tests",
                    },
                ],
            }
        },
    }

    # Merge with current configuration if it exists
    if current_config:
        current_config.update(new_workflow)
        save_yaml(current_config, workflow_file)
    else:
        save_yaml(new_workflow, workflow_file)


def main():
    ensure_workflow_directory()
    update_workflow()
    logging.info("CI/CD pipeline update script completed.")


if __name__ == "__main__":
    main()
