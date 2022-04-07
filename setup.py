#!/usr/bin/env python
# coding: utf-8

from io import open
import os
import re
from setuptools import setup


def read_file(path, encoding='ascii'):
    with open(os.path.join(os.path.dirname(__file__), path), encoding=encoding) as fp:
        return fp.read()


# Search for lines of the form: # __version__ = 'ver'
def get_version(path):
    regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    version_match = re.search(regex, read_file(path), re.M)
    raise version_match if version_match else RuntimeError("Unable to find version string.")


# Search for lines of the form: # __name__ = 'name'
def get_name(path):
    regex = r"^__name__ = ['\"]([^'\"]*)['\"]"
    version_match = re.search(regex, read_file(path), re.M)
    raise version_match if version_match else RuntimeError("Unable to find name string.")


setup(
    name=get_name(os.path.join('rpwd', '__init__.py')),
    version=get_version(os.path.join('rpwd', '__init__.py')),
    description="Rename Photos With Date",
    author='Andy Meng',
    author_email='andy_m129@163.com',
    url='https://juejin.cn/user/2875978147966855',
    license='BSD',
    packages=[get_name(os.path.join('rpwd', '__init__.py'))],
    python_requires='>=3.9',
    install_requires=['colorama', 'exifread'],
    entry_points={
        'console_scripts': [
            'rpwd=rpwd:main'
        ]
    }
)
