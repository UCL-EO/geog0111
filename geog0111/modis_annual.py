#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
utility code to efficiently read MODIS 
time series once downloaded.

See main() for example.

'''

import gdal
try:
  from geog0111.modis import Modis
except:
  from modis import Modis

import yaml
from pathlib import Path

def modis_annual_dataset(year,tile,product,step=1,\
                         verbose=False,dbfile='data/my_db.yml'):
    # load into kwargs
    kwargs = {
    'verbose'  : verbose,
    'tile'      :    list(tile),
    'product'   :    product,
    }
    # list of doys we want
    doys = "*"
    
    # read the database
    database = Path(dbfile)
    if database.exists():
        with database.open("r") as f:
            db = yaml.safe_load(f) or {}
            
    # from above    
    key = f'{kwargs["product"]}._{"_".join(kwargs["tile"])}_.{year}'

    if key in db.keys():
        print(f"we dont need to process {key}")
        ifiles = db[key]
    else:
        modis = Modis(**kwargs)
        ifiles = modis.get_modis(year,doys,step=step)

        # put in database
        cache = {key : ifiles}
        db.update(cache)
        # write out
        with database.open("w") as f:
            yaml.safe_dump(db,f)  
        
    return ifiles



def get_modis_annual(ifiles,sds=None,warp_args={}):
    # loop over SDS sets and read into dictionary
    mfiles = {'bandnames':ifiles['bandnames']}
    del ifiles['bandnames']
    
    # useful sds default
    if sds == None:
        sds = ifiles.keys()
    
    for s in sds:
        # do this in case we dont need to cut
        if warp_args != {}:
            g = gdal.Warp("",ifiles[s],**warp_args)
            mfiles[s] = g.ReadAsArray()
        else:
            mfiles[s] = ifiles[s]
    return mfiles


def modis_annual(year,tile,product,step=1,\
                 sds=None,warp_args={},verbose=False,\
                 dbfile='data/my_db.yml'):
    
    ifiles = modis_annual_dataset(year,tile,product,\
                         step=step,dbfile=dbfile,verbose=verbose)
    mfiles = get_modis_annual(ifiles,sds=sds,warp_args=warp_args)
    # what to do is SDS is None?
    return mfiles

def main():
  warp_args = {
    'dstNodata'     : 255,
    'format'        : 'MEM',
    'cropToCutline' : True,
    'cutlineWhere'  : "FIPS='LU'",
    'cutlineDSName' : 'data/TM_WORLD_BORDERS-0.3.shp'
  }
  sds     = ['Lai_500m','LaiStdDev_500m','FparLai_QC']
  tile    = ['h17v03','h18v03','h17v04','h18v04']
  product = 'MCD15A3H'
  year    = 2019
  step    = 4 
  mfiles = modis_annual(year,tile,product,step=step,sds=sds,warp_args=warp_args)
  print(mfiles.keys())



if __name__ == "__main__":
    main()



