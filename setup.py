#!/usr/bin/env python3
import os
from setuptools import setup, find_packages

try:
    '''
    in no case, setup should fail.
    take care of it that setup.py should not fail due to change in other files.
    if it fails it will cause a serious problem
    we can detect that from version number that will be installed during failure
    if your version is 1.0.0 please report srbcheema2@gmail.com
    '''
    from medipack import __version__, __mod_name__
    from medipack.dependencies.dependencies import dependency_map
    from medipack.dependencies.dependency import install_arg_complete, install_dependencies
    install_dependencies(dependency_map,verbose=True)
    install_arg_complete()
except:
    __version__ = '1.0.0'
    __mod_name__ = 'medipack'
    print('something really bad happened, please report to srbcheema2@gmail.com')


try:
    with open("README.md", 'r') as f:
        long_description = f.read()
    with open('requirements.txt', 'r') as f:
        requirements = [line.strip() for line in f.readlines()]
except:
    long_description='A command line tool for media editing',
    requirements = []

setup(
    name=__mod_name__,
    version=__version__,
    description='A command line tool for media editing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sarbjit Singh',
    author_email='srbcheema1@gmail.com',
    url='http://github.com/srbcheema1/'+__mod_name__,

    # packages=[__mod_name__,__mod_name__+'.lib',__mod_name__+'.dependencies'],  #same as name of directories
    packages=find_packages(), # provides same list, looks for __init__.py file in dir
    include_package_data=True,
    install_requires=requirements, #external packages as dependencies

    entry_points={
        'console_scripts': [__mod_name__+'='+__mod_name__+'.main:main']
    },

    classifiers=[
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    license='MIT License',
)
