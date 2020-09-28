#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Example script to get all days of data for MCD15A3H
for the tiles and year spewcified. 

from pathlib import Path

To run this, simply type:

ipython geog0111/get_lai.py

at the command prompt.
'''
from pathlib import Path
import gdal
import geog0111
from geog0111.modis import Modis
import matplotlib.pyplot as plt


product = 'MCD15A3H'

kwargs = {
    'verbose' : True,
    'tile'      :    ['h17v04','h18v04','h17v03','h18v03'],
    'product'   :    'MCD15A3H',
    'sds'       :    'Lai_500m',
}
year = 2019
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

