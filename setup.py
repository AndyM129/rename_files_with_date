#!/usr/bin/env python
# coding: utf-8

from io import open
import os
import re
from setuptools import setup


__NAME__ = 'rpwd'


# 加载 __init__.py 中定义的常量值
def get_const(const_name):
    file_path = f'{os.path.dirname(__file__)}/src/{__NAME__}/__init__.py'
    with open(file_path) as stream:
        file_content = stream.read()
        pattern = f"^{const_name} = ['\"]([^'\"]*)['\"]"
        match = re.search(pattern, file_content, re.M)
        if match: return match.group(1)
        raise RuntimeError("Unable to find version string.")


setup(
    name=get_const('__NAME__'),
    version=get_const('__VERSION__'),
    description=get_const('__DESC__'),
    author=get_const('__AUTHOR_NAME__'),
    author_email=get_const('__AUTHOR_EMAIL__'),
    url=get_const('__URL__'),
    license='BSD',
    packages=[__NAME__],
    python_requires='>=3.9',
    install_requires=['colorama', 'exifread'],
    entry_points={
        'console_scripts': [
            f'{__NAME__}={__NAME__}:main'
        ]
    }
)
