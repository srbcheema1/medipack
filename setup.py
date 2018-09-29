#!/usr/bin/env python3
import os
from setuptools import setup

import medipack

with open("README.md", 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

def line_adder(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        lines = [x.strip() for x in f.readlines()]
        if(not line in lines):
            f.seek(0, 0)
            f.write(content + '\n' + line + '\n')

line = 'eval "$(register-python-argcomplete medipack)"'
filename = os.environ['HOME'] + '/.bashrc'
line_adder(filename,line)

setup(
    name='medipack',
    version=medipack.__version__,
    description='A command line tool for media editing',
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
)
