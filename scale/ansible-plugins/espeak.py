#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
espeak is a total rip-off of osx_say :)
"""
import os
import subprocess

FAILED_VOICE = ["-p0", "-v", "english-mb-en1"]
LASER_VOICE = ["-s200", "-p100"]
ESPEAK_CMD = "/usr/bin/espeak"


class CallbackModule(object):
    def __init__(self):
        self.disabled = True
        if not os.path.exists(ESPEAK_CMD):
            self.disabled = True

    def say(self, msg, voice):
        cmd = [ESPEAK_CMD, msg] + voice
        subprocess.call(cmd)

    def runner_on_failed(self, host, res, ignore_errors=False):
        self.say("Failure on host %s" % host, FAILED_VOICE)

    def runner_on_ok(self, host, res):
        self.say("pew", LASER_VOICE)

    def runner_on_skipped(self, host, item=None):
        self.say("pew", LASER_VOICE)

    def runner_on_unreachable(self, host, res):
        self.say("Failure on host %s" % host, FAILED_VOICE)

    def runner_on_async_ok(self, host, res, jid):
        self.say("pew", LASER_VOICE)

    def runner_on_async_failed(self, host, res, jid):
        self.say("Failure on host %s" % host, FAILED_VOICE)

    def playbook_on_start(self):
        self.say("Running Playbook", LASER_VOICE)

    def playbook_on_notify(self, host, handler):
        self.say("pew", LASER_VOICE)

    def playbook_on_task_start(self, name, is_conditional):
        if not is_conditional:
            self.say("Starting task: %s" % name, LASER_VOICE)
        else:
            self.say("Notifying task: %s" % name, LASER_VOICE)

    def playbook_on_setup(self):
        self.say("Gathering facts", LASER_VOICE)

    def playbook_on_play_start(self, name):
        self.say("Starting play: %s" % name, LASER_VOICE)

    def playbook_on_stats(self, stats):
        self.say("Play complete", LASER_VOICE)
