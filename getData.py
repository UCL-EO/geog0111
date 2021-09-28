#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geog0111.modisUtils import modisAnnual

warp_args = {
    'dstNodata'     : 255,
    'format'        : 'MEM',
    'cropToCutline' : True,
    'cutlineWhere'  : "FIPS='LU'",
    'cutlineDSName' : 'data/TM_WORLD_BORDERS-0.3.shp'
}

kwargs = {
    'tile'      :    ['h18v03','h18v04','h17v03','h17v04'],
    'product'   :    'MCD15A3H',
    'sds'       :    ['Fpar_500m','Lai_500m','FparLai_QC','FparExtra_QC','FparStdDev_500m','LaiStdDev_500m']
,
    'doys'      : [i for i in range(1,366,4)],
    'year'      : 2019,
    'warp_args' : warp_args
}


# run
odict,bnames = modisAnnual(**kwargs)

