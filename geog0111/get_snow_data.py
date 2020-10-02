#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gdal
try:
  from geog0111.modis_annual import modis_annual
except:
  from modis_annual import modis_annual

import numpy as np

def get_snow_data(year):
    '''
    '''
    # load some data
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
    mfiles = modis_annual(year,tile,product,verbose=True,\
                          sds=sds,warp_args=warp_args)
    # scale it
    # doy from filenames
    doy = np.array([int(i.split('-')[1]) for i in mfiles['bandnames']])
    #print(mfiles[sds[0]],doy)
    return mfiles[sds[0]],doy

snow,doy = get_snow_data(2019)
print(doy)

