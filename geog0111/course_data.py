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

def pull(product,year,tile,doy=None,month=None,day=None,step=1):
  kwargs = {
    'tile'      :    list(tile),
    'product'   :    product,
    'log'       :    f'{gwork}/{product}_{year}_{tidy(tile)}_log.txt',
    'db_file'   :    [f'{gwork}/database.db',f'{gwork}/{product}_database.db'],
    'local_dir' :    f'{gwork}',
    'verbose'   :    True
  }
  # get the data
  print(kwargs)
  modis = Modis(**kwargs)
  #modis.get_data(year,doy=doy,day=day,step=step,month=month) 
  modis.stitch(year,doy=doy,day=day,step=step,month=month)
  return modis

def tidy(s):
  return str(s).replace("'","").replace('"','').replace(',','_').replace('[','_').replace(']','_')

def main():
    for tile in ['h17v03', 'h17v04', 'h18v03', 'h18v04','h09v04','h10v04','h11v04','h12v04','h19v03','h19v04','h30v10','h31v10','h19v11','h19v10','h22v10','h23v10']:
      for year in [2018,2019,2020]:
        try:
          # LAI
          r = pull('MCD15A3H',year,tile,step=4)
        except:
          pass
        try:
          # snow 1
          r = pull('MOD10A1',year,tile,step=1)
        except:
          pass
        try:
          # snow 2
          r = pull('MYD10A1',year,tile,step=1)
        except:
          pass
        try:
          # LC
          r = pull('MCD12Q1',year,tile,step=400)
        except:
          pass
        try:
          # BA
          r = pull('MCD64A1',year,tile,month="*",day=1)
        except:
          pass


if __name__ == "__main__":
    main()

