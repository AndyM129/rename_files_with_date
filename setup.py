#!/usr/bin/env python
# coding: utf-8

import re


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("rpwd/__init__.py", "r") as file:
    content = file.read()
    name = 'rpwd'
    full_name = re.search(r'^__FULL_NAME__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1).replace(' ', '_').lower()
    version = re.search(r'^__VERSION__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    description = re.search(r'^__DESC__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    author = re.search(r'^__AUTHOR_NAME__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    author_email = re.search(r'^__AUTHOR_EMAIL__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    url = re.search(r'^__URL__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)

with open("README.md", "r") as fd:
    long_description = fd.read()

setup(
    name=name,
    version=version,
    description=description,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author=author,
    author_email=author_email,
    url=url,
    license='GNU General Public License v3.0',
    packages=[name],
    python_requires='>=3.9',
    install_requires=['colorama', 'exifread'],
    entry_points={
        'console_scripts': [
            f'{name}={name}:main',
            f'{full_name}={name}:main',
        ]
    }
)
