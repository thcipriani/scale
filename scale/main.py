#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Sync all the things!
"""

from __future__ import print_function

import os
import yaml
import sys
import ansible.inventory
import ansible.callbacks

from scale import playbook
from scale import log

from git.repo import Repo

LOG = log.LOG


def load_config():
    repo = Repo('.')

    config_file = os.path.join(
        repo.working_dir,
        ".scale.yml"
    )

    LOG.info("Loading config from {}".format(config_file))
    with open(config_file, 'r') as f:
        return yaml.safe_load(f.read())


def load_inv(conf):
    dsh_group_path = '/etc/dsh/group'
    dsh_group = conf['dsh_targets']
    host_file = os.path.join(dsh_group_path, dsh_group)
    inv = []
    with open(host_file, 'r') as f:
        for host in f:
            inv.append(host.strip())

    LOG.info("Loading host list from {}".format(host_file))
    return ansible.inventory.Inventory(host_list=inv)


def main():
    ansible.callbacks.display(__doc__, color='green')
    conf = load_config()
    inv = load_inv(conf)
    pb = playbook.Playbook(conf)
    pb.run(inv)

if __name__ == "__main__":
    sys.exit(main())
