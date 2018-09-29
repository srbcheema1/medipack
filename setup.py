#!/usr/bin/env python3
from setuptools import setup

import medipack

with open("extra/README.md", 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]
setup(
    name='medipack',
    version=medipack.__version__,
    description='A command line tool for media editing',
    license="MIT",
    long_description=long_description,
    author='Sarbjit Singh',
    author_email='srbcheema1@gmail.com',
    url="http://github.com/srbcheema1/medipack",
    install_requires=requirements, #external packages as dependencies
    packages=['medipack','medipack.lib'],  #same as name of directories
    # packages=find_packages(), # provides same list, looks for __init__.py file in dir
    include_package_data=True,
    entry_points={
        'console_scripts': ['medipack=medipack.main:main']
    },
)
