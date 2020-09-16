#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import gdal
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
                    size_check=True,\
                    no_clobber=True,\
                    local_dir=None,\
                    db_dir=None,\
                    verbose=False):

    self.size_check = size_check
    self.no_clobber = no_clobber
    self.local_dir = local_dir
    self.verbose = verbose
    self.site    = site
    self.product = product
    self.tile    = tile
    self.day     = day
    self.month   = month
    self.year    = year
    self.sub     = None
    self.translateoptions = gdal.TranslateOptions(gdal.ParseCommandLine("-of Gtiff -co COMPRESS=LZW"))

  def get_url(self,year=False,    month=False, day=False,\
                   product=False, tile=False, \
                   site=False):
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

    product  = product or self.product 
    tile     = tile    or self.tile
    day      = day     or self.day
    month    = month   or self.month
    year     = year    or self.year

    # you should put some tests in
    site_dir = f'MOTA/{product}.006/{year}.{month}.{day}'

    site_file = f'*.{tile}*.hdf'
    kwargs = {"verbose"    : self.verbose,\
              "no_clobber" : self.no_clobber,\
              "size_check" : self.size_check,\
              "local_dir"  : self.local_dir }

    url = URL(site,site_dir,**kwargs)
    

    hdf_urls = url.glob(site_file)
    try:
      self.cache_url[str(url)] = hdf_urls
    except:
      self.cache_url = {str(url) : hdf_urls}

    return hdf_urls 

  def get_hdf_data(self,hdf_urls):
    '''
    get the data corresponding to the list in hdf_urls
    '''
    hdf_urls = list(hdf_urls)
    local_files = []
    for url in hdf_urls:
      if type(url) == Path:
        local_file = url
      else:
        local_file = url._local_file()
      if not local_file.exists():
        hdf_data = url.read_bytes()
        # and save to a file
        obytes = url.write_bytes(hdf_data)
      local_files.append(local_file)
    return local_files

  def get_sub(self,hdf_file):
    if type(hdf_file) == URL:
      lfile = self.get_hdf_data([hdf_file])[0]
    else:
      lfile = hdf_file
    if self.sub == None:
      g = gdal.Open(str(lfile))
      self.sub = [(s0.replace(str(lfile),'{local_file}'),s1) for s0,s1 in g.GetSubDatasets()]
    
    sub = [(s1.format(local_file=str(lfile)),s2) for s1,s2 in self.sub]
    return sub 

  def hdf_to_gtiff(self,hdf_file):
    '''pull the SDS from and HDF'''
    g = gdal.Open(str(hdf_file))
    if g:
      sub = self.get_sub(hdf_file)
      glocal_file_sds = []
      for s in sub:
        g = gdal.Open(s[0])
        product = s[1].split()[1]
        name = '_'.join([product,hdf_file.with_suffix('.tif').name])
        glocal_file = hdf_file.with_name(name)
        if g:
          gout = gdal.Translate(str(glocal_file), g, options=self.translateoptions)
          del gout
        glocal_file_sds.append(glocal_file)
    return glocal_file_sds

  def get_data(self,hdf_urls):
    '''
    get the data corresponding to the list in hdf_urls
    '''
    hdf_urls = list(hdf_urls)
    hdf_data = self.get_hdf_data(hdf_urls)

    return [self.hdf_to_gtiff(f) for f in hdf_data]

def test_login(do_test):
    '''ping small (1.3 M) test file
       to test NASA Earthdata login'''
    if not do_test:
      return True
    # ping small (1.3 M) test file
    site='https://e4ftl01.cr.usgs.gov/'
    test_dir='MOLA/MYD11_L2.006/2002.07.04'
    test_file='MYD11_L2*0325*.hdf'
    # this glob interprets the wildcards to get at a suitable test file
    url = URL(site,test_dir,verbose=verbose).glob(test_file)[0]
    # test ping returns True
    return url.ping()   

def main():
  modis = Modis('MCD15A3H',verbose=True,local_dir='work')
  hdf_urls = modis.get_url("2020","*","0[1-4]")
  tif_files = modis.get_data(hdf_urls)
  database = {modis.product : modis.sub}




if __name__ == "__main__":
    main()

