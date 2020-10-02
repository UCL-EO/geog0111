#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Example script to get all days of data for MCD64A1
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
    'product'   :    'MCD64A1',
}
for year in [2017,1018,2019]:
  modis = Modis(**kwargs)
  modis.stitch(year,day=1,month="*")
