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
sds = ['NDSI_Snow_Cover']

def pull(year,tile=['h09v05'],doy="*",month=None,day=None,step=1):
  product = 'MYD10A1'
  kwargs = {
    'tile'      :    list(tile),
    'product'   :    product,
    'verbose'   :    True
  }
  # get the data
  print(kwargs)
  modis = Modis(**kwargs)
  mfiles = modis.get_modis(year,doy,step=step)
  return mfiles

def tidy(s):
  return str(s).replace("'","").replace('"','').replace(',','_').replace('[','_').replace(']','_')

def main():
 mfiles = pull(2019)
 mfiles = pull(2018)

if __name__ == "__main__":
    main()

