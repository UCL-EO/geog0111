#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
try:
  from geog0111.gurlpath import URL
  from geog0111.cylog import Cylog
except:
  from gurlpath import URL
  from cylog import Cylog

'''
class to get MODIS datasets
'''

__author__    = "P. Lewis"
__email__     = "p.lewis@ucl.ac.uk"
__date__      = "28 Aug 2020"
__copyright__ = "Copyright 2020 P. Lewis"
__license__   = "GPLv3"

class Modis():
  '''
  get MODIS datasets from the server
  '''
  def __init__(self,product='MCD15A3H',\
                    tile='h08v06',\
                    day='01',\
                    month='*',\
                    year="2019",\
                    site='https://e4ftl01.cr.usgs.gov',\
                    verbose=False):

    self.verbose = verbose
    self.site    = site
    self.product = product
    self.tile    = tile
    self.day     = day
    self.month   = month
    self.year    = year


  def get_url(self,year=False,    month=False, day=False,\
                   product=False, tile=False, \
                   verbose=False, site=False):
    '''
    Get URL object list for NASA MODIS products
    for the specified product, tile, year, month, day
    
    Keyword Arguments:
    
    verbose:  bool
    site    : str 
    product : str e.g. 'MCD15A3H'
    tile    : str e.g. 'h08v06'
    year    : str valid 2000-present
    month   : str 01-12
    day     : str 01-(28,29,30,31)
    
    '''
    site     =  site    or 'https://e4ftl01.cr.usgs.gov'
    verbose  =  verbose or self.verbose

    product  = product or self.product 
    tile     = tile    or self.tile
    day      = day     or self.day
    month    = month   or self.month
    year     = year    or self.year

    # you should put some tests in
    site_dir = f'MOTA/{product}.006/{year}.{month}.{day}'

    site_file = f'*.{tile}*.hdf'

    url = URL(site,site_dir)
    hdf_urls = url.glob(site_file,verbose=verbose)
    return hdf_urls 
    

def main():
  modis = Modis('MCD15A3H',verbose=True)
  hdf_urls = modis.get_url("2020","*","0[1-4]")
  for u in hdf_urls:
    print(f'{u.name} : {u.exists()}')
 
if __name__ == "__main__":
    main()

