#! /bin/env python
# -*- encoding: utf-8 -*-
from __future__ import print_function

import logging
import os

import click

import clickable.utils
import clickable.coloredlogs
import clickable_ansible
import clickable_igloo


clickable.coloredlogs.bootstrap()
logger = logging.getLogger('stdout.clickable')


# name consistently with click-infra entry point
@click.group()
@click.pass_context
def igloo_ansible(ctx):
    """
    Deployment or development tasks
    """
    clickable.utils.load_config(ctx, __name__, __file__, 'clickables.yml')
    igloo_ansible_playbooks = os.path.join(ctx.obj['project_root'], 'dependencies', 'igloo-ansible-playbooks')
    clickable_igloo.symlink_folders(igloo_ansible_playbooks, ctx.obj['project_root'])


full = clickable_ansible.run_playbook_task(igloo_ansible, 'full',
        'playbooks/igloo-playbooks/full.yml',
        short_help="Igloo full deployment",
        help="""Deploy a full Igloo stack.""",
        # allow customization
        common_hosts="igloo.vagrant")
