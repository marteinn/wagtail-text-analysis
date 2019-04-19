#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
from setuptools import setup, find_packages


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


current_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = ""
with open("wagtailtextanalysis/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

setup(
    name="wagtailtextanalysis",
    version=version,
    description=(
        "Detect key phrases and sentiment from your Wagtail content using cloud Api services"
    ),  # NOQA
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="marteinn",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/wagtail-text-analysis",
    packages=find_packages(
        exclude=("*.tests", "*.tests.*", "tests.*", "tests", "example*")
    ),
    include_package_data=True,
    install_requires=["requests", "wagtail>=2.4"],
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Text Processing :: Linguistic",
        "Framework :: Wagtail :: 2",
        "Framework :: Django",
        "Topic :: Utilities",
    ],
)
