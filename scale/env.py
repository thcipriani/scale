#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Sets up environment variables for ansible run
Must be first thing imported
"""

import os


# Setup environment variables for ansible
os.environ["ANSIBLE_NOCOWS"] = "1"  # Don't use cowsay for logging output
os.environ["ANSIBLE_CALLBACK_PLUGINS"] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "ansible-plugins")
