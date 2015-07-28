#!/usr/bin/env python2
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = ["ansible"]

args = {
    "name": "scale",
    "version": "0.0.1",
    "description": "deploy via ansible",
    "author": "Tyler Cipriani",
    "install_requires": dependencies,
    "packages": ["scale"],
    "entry_points": {
        "console_scripts": [
            "deploy = scale.main:main"
        ]
    }
}

setup(**args)
