#!/usr/bin/env python
# coding: utf-8

"""setuptools based setup module"""

from setuptools import setup
# from setuptools import find_packages
# To use a consistent encoding
import codecs
from os import path

import cadracks_ide

here = path.abspath(path.dirname(__file__))

# Get the long description from the README_SHORT file
with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name=cadracks_ide.__name__,
    version=cadracks_ide.__version__,
    description=cadracks_ide.__description__,
    long_description=long_description,
    url=cadracks_ide.__url__,
    download_url=cadracks_ide.__download_url__,
    author=cadracks_ide.__author__,
    author_email=cadracks_ide.__author_email__,
    license=cadracks_ide.__license__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=['OpenCascade', 'PythonOCC', 'ccad', 'CAD', 'parts', 'json'],
    packages=['cadracks_ide'],
    install_requires=[],
    # OCC, scipy and wx cannot be installed via pip
    extras_require={'dev': [],
                    'test': ['pytest', 'coverage'], },
    package_data={},
    data_files=[('cadracks_ide/icons',
                 ['cadracks_ide/icons/blue_folder.png',
                  'cadracks_ide/icons/file_icon.png',
                  'cadracks_ide/icons/folder.png',
                  'cadracks_ide/icons/green_folder.png',
                  'cadracks_ide/icons/open.png',
                  'cadracks_ide/icons/python_icon.png',
                  'cadracks_ide/icons/quit.png',
                  'cadracks_ide/icons/refresh.png',
                  'cadracks_ide/icons/save.png']),
                ('cadracks_ide',
                 ['cadracks_ide/cadracks-ide.ico',
                  'cadracks_ide/cadracks-ide.ini'])],
    entry_points={},
    scripts=['bin/cadracks-ide']
    )
