# -*- coding: utf-8 -*-

from setuptools import setup
#, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='patentparser',
    version='0.0.1',
    description='Parsing patent information.',
    long_description=readme,
    author='Ben Hoyle',
    author_email='benjhoyle@gmail.com',
    url='https://github.com/benhoyle/patentparser',
    license=license,
    #packages=find_packages(exclude=('tests', 'docs'))
    packages=['patentparser']
)
