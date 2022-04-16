#!/usr/bin/env python
# coding: utf-8

import re


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("amk/rfwd/consts.py", "r") as stream:
    content = stream.read()
    name = re.search(r'^NAME\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    shortcut = re.search(r'^SHORTCUT\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1).replace(' ', '_').lower()
    version = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    description = re.search(r'^DESC\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    author = re.search(r'^AUTHOR_NAME\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    author_email = re.search(r'^AUTHOR_EMAIL\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    url = re.search(r'^GIT_URL\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)

with open("README.md", "r") as stream:
    long_description = stream.read()

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
    install_requires=['colorama'],
    entry_points={
        'console_scripts': [
            f'{name}={name}:main',
            f'{name.replace(".", "_")}={name}:main',
            f'{shortcut}={name}:main',
        ]
    }
)
