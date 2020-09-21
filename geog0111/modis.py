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

  def __init__(self,**kwargs):
    defaults = {
     'product'    : 'MCD15A3H',\
     'tile'       : 'h08v06',\
     'log'        : None,\
     'day'        : '01',\
     'doy'        : None,
     'month'      : '*',\
     'sds'        : None,
     'year'       : "2019",\
     'site'       : 'https://e4ftl01.cr.usgs.gov',\
     'size_check' : False,\
     'noclobber'  : True,\
     'local_dir'  : 'work',\
     'local_file' : None,\
     'db_file'    : None,\
     'db_dir'     : 'work',\
     'verbose'    : False,\
    }

    self.translateoptions = gdal.TranslateOptions(gdal.ParseCommandLine("-of Gtiff -co COMPRESS=LZW"))

    defaults.update(kwargs)
    self.__dict__.update(defaults)    
    # list of tiles
    if type(self.tile) is str:
      self.tile = [self.tile]

    if type(self.sds) is str:
      self.sds = [self.sds]


  def fdict(self):
    '''return partial version of self.__dict__'''
    this = self.__dict__.copy()
    dellist = []
    for k,v in this.items():
      if k[:len('_cached')] == '_cached':
        dellist.append(k)
    for k in dellist:
      del this[k]
    return this

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
    year = int(year)
    self.year  = f'{year}'
    ayear = (datetime.datetime(year+1, 1, 1) - datetime.datetime(year, 1, 1)).days
    
    sfiles = {}
    bandlist = []
    for i,s in enumerate(self.sds):
      ofiles = []
      bandlist = []
      for doy in range(1,ayear+1,step):
        ifiles = self.stitch_date(year,doy)
        if ifiles and len(ifiles):
          bandlist.append(f'{str(i):0>2s}')
          ofiles.append(ifiles[i])
      if len(ofiles):
        spatial_file = f"{self.local_dir}/data.{self.sds[i]}." + \
                     f"{'_'.join(self.tile)}.{self.year}.vrt"
        g = gdal.BuildVRT(spatial_file,ofiles,separate=True)
        g.FlushCache()
        if not g:
          print(f"problem building dataset for {spatial_file} with {self.fdict()}")
        del g  
        sfiles[s] = spatial_file
        sfiles[s+'_name'] = bandlist
    return sfiles,bandlist

  def stitch_date(self,year,doy):
    '''stitch data for date'''
    year = int(year)
    doy  = int(doy)

    dater = (datetime.datetime(year, 1, 1) +\
               datetime.timedelta(doy - 1)).strftime('%Y %m %d').split()
    self.year  = f'{year}'
    self.month = f'{str(int(dater[1])) :0>2s}'
    self.day   = f'{str(int(dater[2])) :0>2s}'  

    hdf_urls = self.get_url(**(self.fdict()))

    for f in hdf_urls:
      d = f.read_bytes()
    hdf_files = [str(f.local()) for f in hdf_urls]

    sds = self.get_sds(hdf_files)
    ofiles = []
    for i,sd in enumerate(sds):
      spatial_file = f"{self.local_dir}/data.{self.sds[i]}." + \
                     f"{'_'.join(self.tile)}.{self.year}.{self.month}.{self.day}.vrt"
      g = gdal.BuildVRT(spatial_file,sds[i])
      if not g:
        print(f"problem building dataset for {spatial_file} with {self.fdict()}")
        sys.exit(1)
      ofiles.append(spatial_file)
    return ofiles

  #def get_files(self,**kwargs):
  #  hdf_urls = self.get_url(**kwargs)
  #  hdf_files = [f.local() for f in hdf_urls]
  #  return hdf_files

  def has_wildness(self,uc):
    is_wild   = np.logical_or(np.array(['*' in i for i in uc]),
                              np.array(['?' in i for i in uc]))
    is_wild_2 = np.logical_or(np.array(['[' in i for i in uc]),
                              np.array([']' in i for i in uc]))
    is_wild = np.logical_or(is_wild,is_wild_2)
    return is_wild

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
    doy      = ('doy' in kwargs and kwargs['doy'])         or self.doy
  
    # special cases 
    #if self.product[:5] == 'MCD19':
    #  self.site = 'https://ladsweb.modaps.eosdis.nasa.gov'
    # you should put some tests in
    if site == 'https://e4ftl01.cr.usgs.gov':
      site_dir = f'MOTA/{product}.006/{year}.{month}.{day}'
    elif site == 'https://ladsweb.modaps.eosdis.nasa.gov':
     if self.doy is None:
       try:
         doy = (datetime.datetime(year+1, 1, 1) - \
                datetime.datetime(year=int(year),month=int(month),day=int(day))).days
       except:
         self.verbose = True
         self.msg(f"ERROR: you need to specify doy explicitly for product {self.product}")
         sys.exit(1)
       site_dir = f'archive/allData/6/{product}/{year}/{doy}'

    site_file = f'*.{tile}*.hdf'
    kwargs = {"verbose"    : self.verbose,\
              "full_url"   : True,\
              "noclobber"  : self.noclobber,\
              "db_dir"     : self.db_dir,\
              "db_file"    : self.db_file,\
              "log"        : self.log,\
              "size_check" : self.size_check,\
              "local_file" : self.local_file,\
              "local_dir"  : self.local_dir }

    hdf_urls = []
    url = None
    import pdb;pdb.set_trace()
    for t in self.tile:
      url = ((url is None) and URL(site,site_dir,**kwargs)) or \
             url.update(site,site_dir,**kwargs)
      hdf_urls += url.glob(f'{self.product}*.{t}*.hdf')
    if len(hdf_urls) == 0:
      return [None]
    return hdf_urls 

  #def get_hdf_files(self,**kwargs):
  #  '''download the MODIS data and return the local filenames'''
  #  hdf_urls = self.get_url(**kwargs)
  #  for f in hdf_urls:
  #    d = f.read_bytes()
  #  hdf_files = [f.local() for f in hdf_urls]
  #  return hdf_files

  def get_sds(self,hdf_files):
    '''get defined SDS or all'''
    if type(hdf_files) is not list:
      hdf_files = [hdf_files]

    if len(hdf_files) < 1:
      return []
    lfile = hdf_files[0]
    g = gdal.Open(str(lfile))
    if not g:
      return []
    # in case not defined
    if (self.sds is None) or len(self.sds) == 0 or \
      ((len(self.sds) == 1) and len(self.sds[0]) == 0) :
      self.sds = [s1.split()[1] for s0,s1 in g.GetSubDatasets()]

    all_subs  = [(s0.replace(str(lfile),'{local_file}'),s1) for s0,s1 in g.GetSubDatasets()]
    this_subs = []
    for sd in self.sds:
      this_subs += [s0 for s0,s1 in all_subs if sd in s1]
    return [[sub.format(local_file=str(lfile)) for lfile in hdf_files] for sub in this_subs]

  #def hdf_to_gtiff(self,hdf_file):
  #  '''pull the SDS from and HDF'''
  #  g = gdal.Open(str(hdf_file))
  #  if g:
  #    sub = self.get_sub(hdf_file)
  #    glocal_file_sds = []
  #    for s in sub:
  #      g = gdal.Open(s[0])
  #      product = s[1].split()[1]
  #      name = '_'.join([product,hdf_file.with_suffix('.tif').name])
  #      glocal_file = hdf_file.with_name(name)
  #      if g:
  #        gout = gdal.Translate(str(glocal_file), g, options=self.translateoptions)
  #        del gout
  #      glocal_file_sds.append(glocal_file)
  #  return glocal_file_sds

  #def get_tdata(self,hdf_urls):
  #  '''
  #  get the data corresponding to the list in hdf_urls
  #  '''
  #  hdf_urls = list(hdf_urls)
  #  hdf_data = self.get_hdf_data(hdf_urls)
  #
  #  return [self.hdf_to_gtiff(f) for f in hdf_data]

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
  modis = Modis(product='MCD15A3H',verbose=True,local_dir='work')
  hdf_urls = modis.get_url(year="2019",month="*",day="0[1-4]")

  print(hdf_urls)

if __name__ == "__main__":
    main()

