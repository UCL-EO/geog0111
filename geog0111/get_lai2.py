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

kwargs = {
    'verbose' : True,
    'tile'      :    ['h17v03','h18v03','h17v04','h18v04'],
    'product'   :    'MCD15A3H',
}
year = 2018
# list of doys we want
doys = "*"

modis = Modis(**kwargs)

warp_args = {
    'dstNodata'     : 255,
    'format'        : 'MEM',
    'cropToCutline' : True,
    'cutlineWhere'  : "FIPS='UK'",
    'cutlineDSName' : 'data/TM_WORLD_BORDERS-0.3.shp'
}
mfiles = modis.get_modis(year,doys,warp_args=warp_args,step=4)
print(mfiles.keys())
