#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Example script to get all days of data for MCD15A3H
for the tiles and year spewcified. 


To run this, simply type:

geog0111/get_lai.py

at the command prompt.
'''

import gdal
try:
  from geog0111.modis import Modis
except:
  from modis import Modis
import matplotlib.pyplot as plt

sds     = ['NDSI_Snow_Cover']
product = 'MOD10A1'
tile = ['h09v05']
warp_args = {
      'dstNodata'     : 255,
      'format'        : 'MEM',
      'cropToCutline' : True,
      'cutlineWhere'  : "HUC=13010001",
      'cutlineDSName' : 'data/Hydrologic_Units/HUC_Polygons.shp'
}

kwargs = {
    'verbose' : True,
    'tile'      :    tile,
    'product'   :    product,
}
for year in [2017,2018,2019,2020]:
  # list of doys we want
  doys = "*"

  modis = Modis(**kwargs)
  mfiles = modis.get_modis(year,doys,step=1)
  print(mfiles.keys())
