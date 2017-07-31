# -*- coding: utf-8 -*-
"""Glue to help work around path oddities"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import initmod  # pylint: disable=wrong-import-position,unused-import
