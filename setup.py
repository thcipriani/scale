#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
S.C.A.L.E
---

Sync Common All (Literally Everything)

A command line tool that syncs things.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = ["ansible>=1.9.0", "GitPython>=0.3.2.RC1"]

args = {
    "name": "scale",
    "version": "0.0.1",
    "description": "deploy via ansible",
    "long_description": __doc__,
    "author": "Tyler Cipriani",
    "install_requires": dependencies,
    "packages": ["scale"],
    "entry_points": {
        "console_scripts": [
            "scale = scale.main:main"
        ]
    }
}

setup(**args)
