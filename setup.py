#!/usr/bin/env python3
import os
from setuptools import setup

from medipack.dependencies.dependency import install_arg_complete, install_dependencies
from medipack.main import dependency_map

base_dir = os.path.dirname(__file__)
mod_name = 'medipack'
try:
    __info__ = {}
    with open(os.path.join(base_dir,mod_name, "__info__.py")) as f:
        exec(f.read(), __info__)
    version_info = __info__['version']
except:
    version_info = '1.0.0'

install_dependencies(dependency_map,verbose=True)
install_arg_complete()

with open("README.md", 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name=mod_name,
    version=version_info,
    description='A command line tool for media editing',
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sarbjit Singh',
    author_email='srbcheema1@gmail.com',
    url="http://github.com/srbcheema1/medipack",
    install_requires=requirements, #external packages as dependencies
    packages=[mod_name,'medipack.lib','medipack.dependencies'],  #same as name of directories
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
