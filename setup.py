#-*- coding: utf-8 -*-

"""
    pyglassdoor
    ~~~~~~~~~

    Setup
    `````

    $ pip install pyglassdoor
"""

import os
from distutils.core import setup

setup(
    name='pyglassdoor',
    version='0.0.1',
    url='http://github.com/ghanemar/pyglassdoor',
    author='ghanemar',
    author_email='amer@ghanem.ps',
    packages=[
        'pyglassdoor',
        'test'
        ],
    platforms='any',
    license='LICENSE',
    install_requires=[
        'requests >= 1.2.3',
        'simplejson >= 3.6.2',
    ],
    scripts=[
        "scripts/pyglassdoor"
        ],
    description="PyGlassdoor is a Python API for Glassdoor",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
)
