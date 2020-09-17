#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import gdal
from pathlib import Path
import datetime
import numpy as np

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
  def set_kwargs(self,product='MCD15A3H',\
                    tile='h08v06',\
                    day='01',\
                    month='*',\
                    sds= None,
                    year="2019",\
                    site='https://e4ftl01.cr.usgs.gov',\
                    size_check=False,\
                    noclobber=True,\
                    local_dir='work',\
                    local_file=None,\
                    db_file=None,\
                    db_dir='work',\
                    verbose=False):

    self.size_check = size_check
    self.noclobber = noclobber
    self.local_dir = local_dir
    self.local_file= local_file
    self.db_dir  = db_dir
    self.db_file = db_file
    self.verbose = verbose
    self.site    = site
    self.product = product
    self.tile    = tile
    self.day     = day
    self.month   = month
    self.year    = year
    self.sub     = None
    self.sds     = sds
    self.translateoptions = gdal.TranslateOptions(gdal.ParseCommandLine("-of Gtiff -co COMPRESS=LZW"))

    # list of tiles
    if type(self.tile) is str:
      self.tile = [self.tile]

    if type(self.sds) is str:
      self.sds = [self.sds]

  def __init__(self,product='MCD15A3H',**kwargs):
    self.set_kwargs(**kwargs)
    self.kwargs = kwargs

  def get_data(self,year,doy):
    '''return data array for doy year as sds dictionary'''
    vfiles = self.stitch_date(year,doy)
    if not vfiles:
      return dict(zip(self.sds,[[]] * len(self.sds)))
    data = []
    for i,s in enumerate(self.sds):
      g = gdal.Open(vfiles[i])
      data.append(g.ReadAsArray())
    return dict(zip(self.sds,data))

  def read_data(self,ifile):
    g = gdal.Open(ifile)
    if not g:
      return None,None   
    data = np.array([g.GetRasterBand(i).ReadAsArray() for i in range(1,len(g.GetFileList()))])
    b = g.GetRasterBand(1)
    return data, (b.GetScale(),b.GetOffset())
    
  def get_year(self,year,step=4):
    '''create vrt dataset of all images for a year'''
    kwargs = self.kwargs.copy()
    kwargs['year']  = f'{year}'

    ayear = (datetime.datetime(year+1, 1, 1) - datetime.datetime(year, 1, 1)).days
    
    sfiles = {}
    for i,s in enumerate(self.sds):
      ofiles = []
      bandlist = []
      for doy in range(1,ayear+1,step):
        ifiles = self.stitch_date(year,doy)[i]
        if ifiles:
          bandlist.append(f'{str(i):0>2s}')
          ofiles.append(ifiles)
      spatial_file = f"{self.local_dir}/data.{self.sds[i]}." + \
                     f"{'_'.join(self.tile)}.{kwargs['year']}.vrt"
      g = gdal.BuildVRT(spatial_file,ofiles,separate=True)
      g.FlushCache()
      if not g:
        print(f"problem building dataset for {spatial_file} with {kwargs}")
      del g  
      sfiles[s] = spatial_file
      sfiles[s+'_name'] = bandlist
    return sfiles,bnames

  def stitch_date(self,year,doy):
    '''stitch data for date'''
    dater = (datetime.datetime(year, 1, 1) +\
               datetime.timedelta(doy - 1)).strftime('%Y %m %d').split()
    kwargs = self.kwargs.copy()
    kwargs['year']  = f'{year}'
    kwargs['month'] = f'{str(int(dater[1])) :0>2s}'
    kwargs['day']   = f'{str(int(dater[2])) :0>2s}'

    hdf_urls = self.get_url(**kwargs)
    for f in hdf_urls:
      d = f.read_bytes()
    hdf_files = [str(f.local()) for f in hdf_urls]

    sds = self.get_sds(hdf_files)
    ofiles = []
    for i,sd in enumerate(sds):
      spatial_file = f"{self.local_dir}/data.{self.sds[i]}." + \
                     f"{'_'.join(self.tile)}.{kwargs['year']}.{kwargs['month']}.{kwargs['day']}.vrt"
      g = gdal.BuildVRT(spatial_file,sds[i])
      if not g:
        print(f"problem building dataset for {spatial_file} with {kwargs}")
        sys.exit(1)
      ofiles.append(spatial_file)
    return ofiles

  def get_files(self,**kwargs):
    hdf_urls = self.get_url(**kwargs)
    hdf_files = [f.local() for f in hdf_urls]
    return hdf_files


  def get_url(self,**kwargs):
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
    site     = ('site' in kwargs and kwargs['site'])    or 'https://e4ftl01.cr.usgs.gov'

    product  = ('product' in kwargs and kwargs['product']) or self.product 
    tile     = ('tile' in kwargs and kwargs['tile'])       or self.tile
    day      = ('day' in kwargs and kwargs['day'])         or self.day
    month    = ('month' in kwargs and kwargs['month'])     or self.month
    year     = ('year' in kwargs and kwargs['year'])       or self.year

    # you should put some tests in
    site_dir = f'MOTA/{product}.006/{year}.{month}.{day}'

    site_file = f'*.{tile}*.hdf'
    kwargs = {"verbose"    : self.verbose,\
              "noclobber" : self.noclobber,\
              "db_dir"    : self.db_dir,\
              "db_file"   : self.db_file,\
              "size_check" : self.size_check,\
              "local_file" : self.local_file,\
              "local_dir"  : self.local_dir }

    hdf_urls = []
    for t in self.tile:
      hdf_urls += URL(site,site_dir,**kwargs).glob(f'*.{t}*.hdf')
    return hdf_urls 

  def get_hdf_files(self,**kwargs):
    '''download the MODIS data and return the local filenames'''
    hdf_urls = self.get_url(**kwargs)
    for f in hdf_urls:
      d = f.read_bytes()
    hdf_files = [f.local() for f in hdf_urls]
    return hdf_files

  def get_sds(self,hdf_files):

    if len(hdf_files) < 1:
      return []
    lfile = hdf_files[0]
    g = gdal.Open(str(lfile))
    if not g:
      return []
    all_subs  = [(s0.replace(str(lfile),'{local_file}'),s1) for s0,s1 in g.GetSubDatasets()]
    this_subs = []
    for sd in self.sds:
      this_subs += [s0 for s0,s1 in all_subs if sd in s1]
    return [[sub.format(local_file=str(lfile)) for lfile in hdf_files] for sub in this_subs]

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

  def get_tdata(self,hdf_urls):
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
  hdf_urls = modis.get_url(year="2020",month="*",day="0[1-4]")
  tif_files = modis.get_data(hdf_urls)
  database = {modis.product : modis.sub}




if __name__ == "__main__":
    main()

