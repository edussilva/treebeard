# Treebeard
[![PyPI](https://img.shields.io/pypi/v/treebeard.svg)](https://pypi.python.org/pypi/treebeard/0.1.0)
[![Travis branch](https://img.shields.io/travis/muriloviana/treebeard/master.svg)](https://travis-ci.org/muriloviana/treebeard)
[![Codecov branch](https://img.shields.io/codecov/c/github/muriloviana/treebeard/master.svg)](https://codecov.io/gh/muriloviana/treebeard)

## Overview

Python library to generate a directory tree representation in different formats.

Treebeard supports Python 2.7 & 3.3-3.5, enjoy it!

## Installation

To install Treebeard, simply:

    pip install treebeard

## Usage

You can create different representations of directory tree with Treebeard, for example:

### Python dictionary

    In [1]: from treebeard.utils import tree_to_dict
    
    In [2]: d = tree_to_dict('directory-path')
    
    In [3]: type(d)
    Out[3]: dict
    
    In [4]: print(d)
    Out[4]: {'type': 'directory', 'name': 'directory-path', 'children': [{'type': 'file', 'name': 'children-file'}]}

### JSON

    In [1]: from treebeard.generator import generate_json
    
    In [2]: f = generate_json('directory-path')
    
    In [3]: type(f)
    Out[3]: _io.TextIOWrapper
    
    In [4]: f.name
    Out[4]: 'directory-path.json'
