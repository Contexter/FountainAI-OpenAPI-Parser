from pathlib import Path
import logging
import shutil

logging.basicConfig(level=logging.INFO)


def create_project_structure():
    logging.info("Starting to create project structure...")
    project_structure = {
        "fountainai_openapi_parser": [
            "__init__.py",
            "models.py",
            "parser.py",
            "utils.py",
        ],
        "tests": ["__init__.py", "test_parser.py"],
        "": ["setup.py", "README.md", "LICENSE", "MANIFEST.in"],
    }

    for directory, files in project_structure.items():
        dir_path = Path(directory) if directory else Path(".")
        if dir_path.exists() and dir_path.is_dir() and directory:
            logging.info(f"Removing existing directory: {dir_path}")
            shutil.rmtree(dir_path)
        dir_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {dir_path}")
        for file_name in files:
            file_path = dir_path / file_name
            if file_path.exists():
                logging.info(f"Removing existing file: {file_path}")
                file_path.unlink()
            try:
                with file_path.open("w") as f:
                    f.write(get_boilerplate_content(file_name))
                logging.info(f"Successfully created file: {file_path}")
            except IOError as e:
                logging.error(f"Error creating file {file_path}: {e}")


def get_boilerplate_content(file_name):
    logging.debug(f"Fetching boilerplate content for: {file_name}")
    return {
        "__init__.py": get_init_boilerplate(),
        "models.py": get_models_boilerplate(),
        "parser.py": get_parser_boilerplate(),
        "utils.py": get_utils_boilerplate(),
        "test_parser.py": get_test_parser_boilerplate(),
        "setup.py": get_setup_boilerplate(),
        "README.md": get_readme_boilerplate(),
        "LICENSE": get_license_boilerplate(),
        "MANIFEST.in": get_manifest_boilerplate(),
    }.get(file_name, "")


def get_init_boilerplate():
    logging.debug("Generating boilerplate for __init__.py")
    return """# Initializes the module
"""


def get_models_boilerplate():
    logging.debug("Generating boilerplate for models.py")
    return """# This module contains dataclass models

import dataclasses

"""


def get_parser_boilerplate():
    logging.debug("Generating boilerplate for parser.py")
    return """# Main parsing functions for the OpenAPI parser

"""


def get_utils_boilerplate():
    logging.debug("Generating boilerplate for utils.py")
    return """# Helper functions for the OpenAPI parser

"""


def get_test_parser_boilerplate():
    logging.debug("Generating boilerplate for test_parser.py")
    return """# Unit tests for the parser functions
import pytest

"""


def get_setup_boilerplate():
    logging.debug("Generating boilerplate for setup.py")
    return """# Setup configuration for pip installation
from setuptools import setup, find_packages

setup(
    name='FountainAI-OpenAPI-Parser',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'jsonschema',
        'requests'
    ],
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
"""


def get_readme_boilerplate():
    logging.debug("Generating boilerplate for README.md")
    return """# FountainAI OpenAPI Parser

This project provides a Python library for parsing OpenAPI specifications.

## Installation

```
pip install .
```

## Usage

```
import fountainai_openapi_parser
```
"""


def get_license_boilerplate():
    logging.debug("Generating boilerplate for LICENSE")
    return """# License information
MIT License

Copyright (c) 2024 FountainAI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

..."""


def get_manifest_boilerplate():
    logging.debug("Generating boilerplate for MANIFEST.in")
    return """# Additional files for distribution
include README.md
include LICENSE
"""


if __name__ == "__main__":
    logging.info("Script started")
    create_project_structure()
    logging.info("Script finished")
