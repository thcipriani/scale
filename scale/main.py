#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Sync all the things!
"""

import sys
from scale import env
from scale import log
from scale import config
from scale import playbook

LOG = log.LOG


def main():
    conf = config.load()
    pb = playbook.Playbook(conf)
    pb.run()

if __name__ == "__main__":
    sys.exit(main())
