"""
LicScan by @fakerybakery.
License: NOSCL-C-2.0.
Please see the source code repositories for documentation, full license text, and more: https://github.com/fakerybakery/licscan

VERSION 1.0.0
"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="LicScan",
    version="1.0.0",
    author="GitHub @fakerybakery",
    author_email="me@mrfake.name",
    description="Check your requirements to make sure your requirements have the correct licenses.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fakerybakery/licscan",
    packages=["licscan"],
    install_requires=["requirements-parser", "tqdm"],
    entry_points={
        "console_scripts": [
            "licscan = licscan.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    platforms=["Any"],
    license="NOSCL-C-2.0 - Copyright (c) 2023 mrfakename. All rights reserved. Please read the full NOSCL-C-2.0 license, available at: https://github.com/fakerybakery/licscan"
)