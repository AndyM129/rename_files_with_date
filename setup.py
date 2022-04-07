#!/usr/bin/env python
# coding: utf-8

import re


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("rpwd/__init__.py", "r") as file:
    name = 'rpwd'
    content = file.read()
    version = re.search(r'^__VERSION__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    description = re.search(r'^__DESC__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    author = re.search(r'^__AUTHOR_NAME__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    author_email = re.search(r'^__AUTHOR_EMAIL__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    url = re.search(r'^__URL__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    license='BSD',
    packages=[name],
    python_requires='>=3.9',
    install_requires=['colorama', 'exifread'],
    entry_points={
        'console_scripts': [
            f'{name}={name}:main'
        ]
    }
)
