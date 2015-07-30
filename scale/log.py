#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Shared logging for scale
"""

import logging


logging.basicConfig(format='%(message)s', level=logging.INFO)
LOG = logging.getLogger(__name__)
