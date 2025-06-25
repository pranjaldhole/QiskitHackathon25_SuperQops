#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Default config variables which maybe overridden by a user config.

Author: Pranjal Dhole
E-mail: dhole.pranjal@gmail.com
'''
import os.path as osp

# ===========================================
# PATHS
# ===========================================
PROJECT_PATH = osp.abspath(osp.join(osp.dirname(__file__), '..'))

# ===========================================
# EXPERIMENTAL PARAMETERS
# ===========================================
SIMULATOR_SEED = 42
