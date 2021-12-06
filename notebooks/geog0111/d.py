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


gwork = '/shared/groups/jrole001/geog0111/'
if not Path(gwork).exists():
  gwork = 'work'

for p in ['MOD10A1', 'MYD10A1']:
  kwargs = {
    'tile'      :    ['h09v05'],
    'product'   :    p,
    'sds'       :     ['NDSI_Snow_Cover'],
    'verbose'   : True
  }
        
  warp_args = {
    'dstNodata'     : 255,
    'format'        : 'MEM',
    'cropToCutline' : True,
    'cutlineWhere'  : f"HUC=13010001",
    'cutlineDSName' : 'data/Hydrologic_Units/HUC_Polygons.shp'
  }

  # look in the winter
  for year in [2016,2017,2018,2019,2020]:
    doys = '*'

    modis = Modis(**kwargs)
    mfiles = modis.get_modis(year,doys,warp_args=warp_args)

