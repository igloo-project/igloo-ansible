#! /bin/env python
# -*- encoding: utf-8 -*-
from __future__ import print_function

import logging
import os
import pprint
import sys

import click
from ruamel.yaml import YAML

from clickable.utils import PathResolver
import clickable.coloredlogs
import clickable_ansible


clickable.coloredlogs.bootstrap()
logger = logging.getLogger('stdout.clickable')


# name consistently with click-infra entry point
@click.group()
@click.pass_context
def igloo_ansible(ctx):
    ctx.obj = {}
    ctx.obj['path_resolver'] = clickable.utils.PathResolver(sys.modules[__name__])
    ctx.obj['project_root'] = os.path.dirname(__file__)
    conf_path = os.path.join(ctx.obj['project_root'], 'clickable.yaml')
    if os.path.isfile(conf_path):
        with open(conf_path) as f:
            yaml = YAML(typ='safe')
            configuration = yaml.load(f)
            ctx.obj.update(configuration)
    logger.debug('loaded configuration: \n{}'.format(pprint.pformat(ctx.obj)))
    # loaded from config
    ctx.obj['virtualenv_path'] = ctx.obj['ansible']['virtualenv']['path']
    """
    Deployment or development tasks
    """
    pass

full = clickable_ansible.run_playbook_task(igloo_ansible, 'full',
        'playbooks/igloo-ansible/full.yml',
        short_help="Igloo full deployment",
        help="""Deploy a full Igloo stack.""")
