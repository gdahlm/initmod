# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('LICENSE') as f:
    license = f.read()

with open('README.rst') as f:
    readme = f.read()

setup(
    name='initmod',
    version='0.1.0',
    description='Template package for new projects',
    url='https://github.com/gdahlm/initmod',
    author='Greg Dahlman',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
