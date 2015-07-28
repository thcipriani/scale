#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Command line interface for SCALE
"""

from __future__ import print_function

import sys
import ansible.inventory
import ansible.callbacks

from deploy import config


def main():
    startup = """
    Begin SCALE:
    ---
    Sync
    Common
    All
    Literally
    Everything
    """
    ansible.callbacks.display(startup.lstrip(' '), color='green')


if __name__ == "__main__":
    sys.exit(main())
