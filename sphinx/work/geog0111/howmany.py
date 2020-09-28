#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import numpy as np
import os
try:
  from geog0111.modis import Modis
except:
  from modis import Modis

'''
local download of MODIS datasets and storage in dbfile
'''

__author__    = "P. Lewis"
__email__     = "p.lewis@ucl.ac.uk"
__date__      = "28 Aug 2020"
__copyright__ = "Copyright 2020 P. Lewis"
__license__   = "GPLv3"

import os

gwork = '/shared/groups/jrole001/geog0111/'
if not Path(gwork).exists():
  gwork = 'work'

for product in ['MCD64', 'MCD12Q1', 'MYD10A1', 'MOD10A1' , 'MCD15A3H']:
  print(product)
  cmd = f'ls -lh {gwork}/*/*/*/*/{product}*store | wc -l'
  os.system(cmd)
  
