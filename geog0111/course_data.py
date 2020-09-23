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
local download of MNODIS datasets and storage in dbfile
'''

__author__    = "P. Lewis"
__email__     = "p.lewis@ucl.ac.uk"
__date__      = "28 Aug 2020"
__copyright__ = "Copyright 2020 P. Lewis"
__license__   = "GPLv3"

def uk_lai(year=2019):
  kwargs = {
    'tile'      :    ['h17v03', 'h17v04', 'h18v03', 'h18v04'],
    'product'   :    'MCD15A3H',  
    'log'       :    f'work/uk_lai_{year}_log.txt',
    'db_file'   :    ['data/database.db',f'work/uk_lai_{year}.db'],
    'local_dir' :    'work',
    'verbose'   :    True
  }
  modis = Modis(**kwargs)
  
  result = modis.get_year(year,step=4)
  return result

def tidy(s):
  return str(s).replace("'","").replace('"','').replace(',','_').replace('[','_').replace(']','_')

def snow_data(year=2019,tile=['h19v03']):
  name = f'work/snow_{year}_{tidy(tile)}'
  kwargs = {
    'verbose' : True,
    'log'       :    f'{name}_log.txt',
    'db_file'   :    ['data/database.db',f'{name}.db'],
    'tile'      :    tile,
    'product'   :    'MOD10A1',
  }
  modis = Modis(**kwargs)

  for month in range(1,13):
    sfiles,bandlist = modis.stitch_month(year,month)

def main():
    #for year in [2018, 2019]:
    for year in [2019,2020]:
      #uk_lai_data = uk_lai(year)
      snow_data(year=year,tile=['h19v03'])
if __name__ == "__main__":
    main()

