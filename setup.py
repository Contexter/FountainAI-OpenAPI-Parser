# Setup configuration for pip installation
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
