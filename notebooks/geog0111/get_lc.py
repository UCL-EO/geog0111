#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Example script to get all days of data for MCD12Q1
for the tiles and year spewcified. 


To run this, simply type:

geog0111/get_lc.py

at the command prompt.
'''

import gdal
try:
  from geog0111.modis import Modis
except:
  from modis import Modis
import matplotlib.pyplot as plt

for tile in [['h17v03','h18v03','h17v04','h18v04'],[h22v10']]:
  kwargs = {
    'verbose' : True,
    'tile'      :    tile,
    'product'   :    'MCD12Q1',
  }
  for year in [2017,2018,2019]:
    modis = Modis(**kwargs)
    mfiles = modis.get_modis(year,[1])
    print(mfiles.keys())
