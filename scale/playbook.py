#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Handles tasks related to building/running ansible playbook
"""
import yaml
import ansible.playbook

from tempfile import NamedTemporaryFile
from scale import log
from ansible import callbacks, utils
from ansible.callbacks import display

LOG = log.LOG


class Playbook(object):
    playbook = {
        "hosts": "all",
        "gather_facts": False,
        "sudo": True,
        "serial": 0,
    }

    def __init__(self, conf):
        self.conf = conf
        self.playbook.update(self._get_conf_override())
        self.playbook["tasks"] = self._build_tasks()
        tmp = NamedTemporaryFile(delete=False)
        with open(tmp.name, 'w') as f:
            f.write(yaml.dump([self.playbook]))

        self.tmp = tmp.name

    def run(self):
        stats = callbacks.AggregateStats()
        runner_cb = callbacks.PlaybookRunnerCallbacks(
            stats,
            verbose=utils.VERBOSITY)

        playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)

        pb = ansible.playbook.PlayBook(
            playbook=self.tmp,
            inventory=self.conf["inventory"],
            remote_user=self.conf["remote_user"],
            callbacks=playbook_cb,
            runner_callbacks=runner_cb,
            stats=stats
        )
        pb.run()
        hosts = sorted(pb.stats.processed.keys())
        display(callbacks.banner("‽"))

        for h in hosts:
            t = pb.stats.summarize(h)

            display(
                "%s : %s %s %s %s" % (
                    h,
                    t['ok'],
                    t['changed'],
                    t['unreachable'],
                    t['failures'],),
                screen_only=True
            )

    def _get_conf_override(self):
        """Filters configuration keys to the set in the default playbook"""
        return {
            k: self.conf[k]
            for k in self.playbook
            if self.conf.get(k) is not None
        }

    def _build_tasks(self):
        """Add tasks to playbook based on config"""
        tasks = []

        tasks.append({
            "name": "checkout repo",
            "git": {
                "repo": "http://{}/{}.git".format(
                    self.conf["git_server"], self.conf["git_repo"]),
                "dest": "{}/{}".format(
                    self.conf["git_deploy_dir"], self.conf["git_repo"]),
                "track_submodules": False,
                "version": self.conf["git_rev"],
                "force": True,
            }
        })

        return tasks
