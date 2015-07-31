#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Grab config from .scale.yml
"""

import os
import yaml
from git.repo import Repo
from scale import log
import ansible.inventory

LOG = log.LOG


def load():
    repo = Repo('.')

    config_file = os.path.join(
        repo.working_dir,
        ".scale.yml"
    )

    with open(config_file, 'r') as f:
        config = yaml.safe_load(f.read())

    config["inventory"] = _load_inventory(config["dsh_targets"])
    return config


def _load_inventory(dsh_group):
    dsh_group_path = "/etc/dsh/group"
    host_file = os.path.join(dsh_group_path, dsh_group)
    inv = []
    with open(host_file, 'r') as f:
        for host in f:
            inv.append(host.strip())

    LOG.info("Loading host list from {}".format(host_file))
    return ansible.inventory.Inventory(host_list=inv)
