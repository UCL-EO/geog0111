#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import gdal
from pathlib import Path
import datetime
import numpy as np
import os
import pandas as pd

try:
  from geog0111.gurlpath import URL
  from geog0111.cylog import Cylog
  from geog0111.database import Database
  from geog0111.fdict import fdict
  from geog0111.get_doy import get_doy
  from geog0111.monthdays import monthdays,yeardays
  from geog0111.lists import ginit,list_resolve,name_resolve,list_info
  from geog0111.create_blank_file import create_blank_file
  from geog0111.list_of_doys import list_of_doys
except:
  from gurlpath import URL
  from cylog import Cylog
  from database import Database
  from fdict import fdict
  from get_doy import get_doy
  from monthdays import monthdays,yeardays
  from lists import ginit,list_resolve,name_resolve,list_info
  from create_blank_file import create_blank_file
  from list_of_doys import list_of_doys
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
    kwargs['defaults'] = {
     'version'    : 6,
     'store_msg'  : [],\
     'database'   : None,\
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
     'stderr'     : sys.stderr
    }
    self.__dict__.update(ginit(self,**kwargs))
    if 'database' in self.__dict__ and type(self.database) == Database:
        # already have databse stored
        pass
    else:
        self.database = Database(self.db_file,\
                          **(fdict(self.__dict__.copy(),ignore=['db_dir','db_file'])))

    self.translateoptions = gdal.TranslateOptions(gdal.ParseCommandLine("-of Gtiff -co COMPRESS=LZW"))
    # list of tiles
    if type(self.tile) is str:
      self.tile = [self.tile]

    if type(self.sds) is str:
      self.sds = [self.sds]
    if self.sds is not None:
      self.msg(f'initial SDS {self.sds}')
      self.required_sds = self.sds

    # for most transactions, we want all SDS
    # so self.sds should reflect that
    self.sds = None
    response = self.database.get_from_db('SDS',self.product)
    if response:
      self.msg("found SDS names in database")
      self.sds = response
      self.msg(self.sds)
      # require them all 
      if 'required_sds' not in self.__dict__:
        self.required_sds = self.sds

  def msg(self,*args):
    '''msg to self.stderr'''
    this = str(*args)
    try:
      # DONT REPEAT MESSAGES ... doesnt work as yet
      if this in self.store_msg:
        return
      self.store_msg.append(this)
    except:
      self.store_msg = [this]
    try:
        if self.verbose or (self.log is not None):
            print('-->',*args,file=self.stderr)
    except:
        pass

  def get_data(self,year,doy=None,idict=None,month=None,day=None,step=1,fatal=False):
    '''
    Return data dictionary of MODIS dataset for specified time period

    args:
      year  : year (2000 to present for MOD, or 2002 to present if using MYD)
              NB this is ignoired if idict is given
 
    options:
      doy   : day in year, or day in month if month specified, or None
              when specified as day in year, or day in month, can be a list
              1-365/366 or 1-28-31 as appropriate
      day   : day in month or None. Can be list.
      month : month index 1-12 or None. Can be list.
      step  : dataset step. Default 1, but set to 4 for 4-day product, i
              8 for 8-day, 365/366 for year etc.
      fatal : default False. If True, exit if dataset not found.
      idict : data file dictionary provided by eg call to
              self.get_modis(year,doy=None,month=None,step=1,fatal=False)
              see get_modis for more details
 
    returns:
      data dictionary with keys specified by:
            - self.sds list 
            - or all SDS if self.sds is None (default)
      data dictionary key 'bandnames' of DOY 

      Each data item a 2- or 3-dimensional numpy array:

      For a single date:
        kwargs = {
            'tile'      :    ['h17v03', 'h17v04', 'h18v03', 'h18v04'],
            'product'   :    'MCD15A3H',
            'sds'       :    'Lai_500m',
        }
        modis = Modis(**kwargs)
        # specify day of year (DOY) and year
        data_MCD15A3H = modis.get_data(2019,doy=1+4*10)

        print(data_MCD15A3H.keys())
        dict_keys(['Lai_500m', 'bandnames', 'files'])

        print(data_MCD15A3H['Lai_500m'].shape)
        (4800, 4800)
 
        print(len(data_MCD15A3H['bandnames']))
        1

      If a list of days, or a month or year is specified, the datasets are 3-D:
        kwargs = {
            'tile'      :    ['h19v03'],
            'product'   :    'MOD10A1',
            'sds'       :     ['NDSI_Snow_Cover']
        }

        year  = 2019
        month = 1
        # get the data
        modis = Modis(**kwargs)
        # specify month and year
        data_MOD10A1 = modis.get_data(year,month=1)

        print(data_MOD10A1.keys())
        dict_keys(['NDSI_Snow_Cover', 'bandnames', 'files'])

        print(data_MOD10A1['NDSI_Snow_Cover'].shape)
        (31, 2400, 2400)

        print(len(data_MOD10A1['bandnames']))
        31
        

    '''
    idict = idict or self.get_modis(year,day=day,doy=doy,month=month,step=step,fatal=fatal)
    # for get_data, we only want required_sds
    try:
      if 'required_sds' in self.__dict__:
        sds = self.required_sds
        bandnames = idict['bandnames']
      else:
        bandnames = idict['bandnames']
        del idict['bandnames']
        self.required_sds = idict.keys()
        sds = self.required_sds

      vfiles = [idict[k] for k in sds]

      data = []
      for i,s in enumerate(sds):
        g = gdal.Open(vfiles[i])
        dataset = g.ReadAsArray()
        if dataset is None:
          msg = f"WARNING: no datasets in get_data() for {vfiles[i]}\n" +\
                f"check datasets and database file {str(self.db_file)}"
          print(msg)
          self.msg(msg)
          if fatal == True:
            sys.exit(1)
        data.append(dataset)
      # enforce 3D
      data = np.atleast_3d(np.array(data).T).T
      odict = dict(zip(sds,data))
      odict['bandnames'] = bandnames
      odict['files']  = idict
      return odict
    except:
      self.msg("Error calling get_data")
    return {}


  def sort_vfiles(self,vfiles,sds):
    # reconcile the order of sds and vfiles list
    _sds = np.array([self.tidy(s) for s in sds])
    _vfiles = np.array([f.split('/')[-1].split('.')[1] for f in vfiles])
    index = tuple([np.where(_vfiles == ts)[0][0]  for ts in _sds])
    vf = vfiles.copy()
    vfiles = [vf[i] for i in index]
    return vfiles

  def get_modis(self,year,doy=None,day=None,month=None,step=1,\
                     warp_args=None,dstNodata=None,fatal=False):
    '''
    Return data dictionary of MODIS datasets for specified time period
      
    args:     
      year  : year (2000 to present for MOD, or 2002 to present if using MYD)
      
    options:  
      doy       : day in year, or day in month if month specified, or None
                  when specified as day in year, or day in month, can be a list
                  1-365/366 or 1-28-31 as appropriate 
      day       : day in month or None. Can be list.
      month     : month index 1-12 or None. Can be list.
      step      : dataset step. Integer. Default 1, but set to 4 for 4-day product, i
                  8 for 8-day, 365/366 for year etc.
      dstNodata : fill value 
      warp_args : sub-setting and warping control
      fatal     : default False. If True, exit if dataset not found.
     
    returns:
      data dictionary with SDS names as keys and gdal VRT filename
      data dictionary key 'bandnames' of DOY 
            
      For a single date:
        kwargs = {
            'tile'      :    ['h17v03', 'h17v04', 'h18v03', 'h18v04'],
            'product'   :    'MCD15A3H',
        } 
        modis = Modis(**kwargs)
        # specify day of year (DOY) and year
        data_MCD15A3H = modis.get_modis(2019,1+4*10)
        
        print(data_MCD15A3H.keys())
        dict_keys(['Lai_500m', ... 'bandnames'])
        
        print(len(data_MCD15A3H['bandnames']))
        1
        
      If a list of days, or a month or year is specified, the datasets are 3-D:
        kwargs = {
            'tile'      :    ['h19v03'],
            'product'   :    'MOD10A1',
        }
        
        year  = 2019
        month = 1
        # get the data
        modis = Modis(**kwargs)
        # specify month and year
        data_MOD10A1 = modis.get_modis(year,month=1)

        print(data_MOD10A1.keys())
        dict_keys(['NDSI_Snow_Cover', ... 'bandnames'])

        print(len(data_MOD10A1['bandnames']))
        31

     If a month and day are specified, the datasets are 3-D:
        kwargs = {      
            'tile'      :    ['h22v10'],
            'product'   :    'MCD64A1',
        }

        year  = 2019
        month = 1
        day = 1
        # get the data
        modis = Modis(**kwargs)
        # specify month and year
        data_MCD64A1 = modis.get_modis(year,month=month,day=day)

        print(data_MCD64A1.keys())
        dict_keys(['NDSI_Snow_Cover', ... 'bandnames'])

        print(len(data_MCD64A1['bandnames']))
        31

    '''
    #store for diagnostics
    kwargs = {'doy':doy,'day':day,'month':month,'step':step,\
              'warp_args':warp_args,'dstNodata':dstNodata,'fatal':fatal}

    # work entirely in terms of year and doy
    dates = list_of_doys(year,doy=doy,day=day,month=month,step=step)
    year_list,doy_list = list(dates['year']),list(dates['doy'])
    bandnames = [f'{year}-{d :0>3d}' for d,y in zip(doy_list,year_list)]

    # this is the core call to get the files we want
    # many will be cached 
    vfiles = self.stitch(year=year_list,doy=doy_list,\
                         dstNodata=dstNodata,warp_args=warp_args)
    # error 
    if (not vfiles) or (len(vfiles) == 0) or (len(vfiles) and (vfiles[0] == None)):
      msg = f"WARNING: no datasets in get_data() for product {self.product} tile {self.tile} year {year} month {month} doy {doy}"
      print(msg)
      self.msg(msg)
      self.msg(f"dict   : {self.__dict__}")
      self.msg(f"kwargs : {kwargs}")
      try:
        return dict(zip(self.sds,[[]] * len(self.sds)))
      except:
        return {None:None}

    if 'required_sds' in self.__dict__:
      sds = self.required_sds
    else:
      sds = self.sds

    vfiles = self.sort_vfiles(vfiles,sds)
    odict  = dict(zip(sds,vfiles))
    odict['bandnames'] = bandnames
    return odict

  def tidy(self,s):
    ss = str(s).replace("'","").replace('"','').replace(',','_').replace('[','_').replace(']','_')
    ss = ss.replace(' ','')
    return ss

  def read_data(self,ifile):
    g = gdal.Open(ifile)
    if not g:
      return None,None
    data = np.array([g.GetRasterBand(i).ReadAsArray() for i in range(1,len(g.GetFileList()))])
    b = g.GetRasterBand(1)
    return data, (b.GetScale(),b.GetOffset())

  def fix_sds(self,sds,year,doy,do_all=True):
    '''
    fix sds

    only use self.required_sds if do_all==False

    '''
    if sds:
      return sds
    if 'required_sds' in self.__dict__:
      if do_all == False:
        self.sds = self.required_sds

    # else look in dictionary
    response = self.database.get_from_db("SDS",self.product)
    if response:
      self.msg("found SDS names in database")
      self.sds = response
      self.msg(self.sds)

    # else need to derive it 
    self.msg("polling for SDS names")
    # get hold of a datafile and pull the
    # the names from there: test=True
    self.stitch_date(year,doy,test=True)

    if self.sds is None:
      # try again
      self.msg("error finding SDS names")
      return []
    if 'required_sds' not in self.__dict__:
      # set this in case its not set
      self.required_sds = self.sds
    self.msg(f"SDS: {self.sds}")
    return self.sds

  def get_blank(self,dstNodata,s,i):
    # no dataset
    if ('blanco' in self.__dict__) and (Path(self.blanco).exists()):
      output_filename = self.blanco
      self.msg(f'using file with value {dstNodata} {output_filename}')
      bthis = f'blank-{dstNodata}-{str(i):0>2s}'
      this = output_filename
    else:
      try:
        # repeat last for now
        self.msg(f'no dataset for sds {s} for dataset {i}: using filler')
        this = ofiles[-1]
        output_filename = this.replace('.vrt','{dstNodata}_blank.tif')
        if not Path(output_filename).exists():
          # need to set to invalid number ...
          self.msg(f'creating dummy file')
          create_blank_file(this,output_filename,value=dstNodata)
        self.msg(f'using file with value {dstNodata} {output_filename}')
        self.blanco = output_filename
        bthis = f'blank-{dstNodata}-{str(i):0>2s}'
        this = output_filename
      except:
        bthis = f'blank-{dstNodata}-{str(i):0>2s}'
        this = None
    return this,bthis

  def stitch(self,year,month=None,day=None,doy=None,step=1,warp_args=None,dstNodata=None):
    '''create vrt dataset of all images for doys / a month / year'''
    # get a dict of year, doy
    dates = list_of_doys(year,month=month,day=day,doy=doy,step=step);
    years,doys = list(dates['year']),list(dates['doy'])

    ndays = len(years)
    self.msg(f"create vrt dataset for doys {doys} year {years}")

    sfiles = {}
    bandlist = []
    # sds may not be defined
    self.fix_sds(self.sds,years[0],doys[0])
      
    # set nodata value
    if (warp_args is not None) and (dstNodata is None):
      dstNodata = warp_args['dstNodata']
    if dstNodata is None:
      dstNodata = 0
    
    if (warp_args is not None) and ('dstNodata' not in warp_args):
      warp_args['dstNodata'] = dstNodata

    # loop over sds
    store_files = [None]*len(years)
    for i,s in enumerate(self.sds):
      ofiles = []
      bandlist = []
      for j,(year,doy) in enumerate(zip(years,doys)):
        year       = int(year)
        doy        = int(doy)
        ifiles = self.stitch_date(year,doy)
      
        if (not ifiles) or (len(ifiles) and ifiles[0] == None):
          this,bthis = self.get_blank(dstNodata,s,i)
        else:
          this,bthis = ifiles[i],f'{str(i):0>2s}'

        store_files[j] = ifiles
 
        if this:
          bandlist.append(bthis)
          ofiles.append(this)
      if len(ofiles):
        ofile = self.tidy(f"{self.product}/data.{self.sds[i]}.{self.tidy(self.tile)}." + \
                f"{year}.{str(int(doy)) :0>3s}.{str(int(step)) :0>3s}.vrt")
        spatial_file = Path(f"{self.local_dir[0]}",ofile)
        spatial_file.parent.mkdir(parents=True,exist_ok=True)
        g = gdal.BuildVRT(spatial_file.as_posix(),ofiles,separate=True)
        try:
          g.FlushCache()
        except:
          pass
        if not g:
          d = self.__dict__
          print(f"problem building dataset for {spatial_file} with {fdict(d)}")
        del g
        if warp_args is not None:
          warp_args['format'] = 'VRT'
          # warp the files using warp_args
          spatial_ofile = Path(spatial_file.as_posix().replace('.vrt','_warp.vrt'))
          self.msg(f"warping to {spatial_ofile} using {warp_args}")
          g = gdal.Warp(spatial_ofile.as_posix(),spatial_file.as_posix(),**warp_args)
          try:
            g.FlushCache()
          except:
            pass
          if not g:
            d = self.__dict__
            print(f"problem building dataset for {spatial_ofile} with {fdict(d)}")
          del g
          sfiles[s] = spatial_ofile
        else:
          sfiles[s] = spatial_file

    # build list of files
    ofiles = [str(i) for i in sfiles.values()]
    return ofiles
    
  def test_ok(self,hdffile,dosubs=True):
    '''sanity check on file'''
    if not Path(hdffile).exists():
      msg = f'test: file {hdffile} does not exist'
      self.msg(msg)
      return False
    g = gdal.Open(hdffile)
    if not g:
      msg = f'test: file {hdffile} failed to open with gdal'
      self.msg(msg)
      del g
      return False
    # check referenced files
    if dosubs:
      for f in g.GetFileList():
        # dont do too much recursion
        if not self.test_ok(f,dosubs=False):
          return False
    data = g.ReadAsArray(xsize=1,ysize=1)
    if data is None:
      msg = f'test: file {hdffile} failed: None returned in read '
      self.msg(msg)
      del g
      return False
    return True

  def stitch  

  def stitch_date(self,year,doy,flush=True,get_files=False,test=False,do_all=True):
    ''' 
    stitch multiple tiles for given year,doy
    '''

    db_key,db_value = self.get_keys(tile,year,doy)

    if test:
      return self.stitch_date_tile_sds(tile,year,doy,test=True)

    if get_files:
      hdf_files = []
      for tile in self.tiles:
        hdf_files.extend(self.stitch_date_tile_sds(tile,year,doy,get_files=True))
      sds = self.get_sds(hdf_files,do_all=False)
      return hdf_files,sds

    # look in DB
    ofiles = self.get_from_db(db_key,db_value)
    if ofiles is not None:
      return ofiles    

    ofilebase = f"{self.product}/data.__SDS__.{db_value}.vrt"

    ifiles = [] 
    for t in self.tiles:
      ifiles.extend(self.stitch_date_tile_sds(tile,year,doy,flush=False,test=False,do_all=True))
    # a list of pairs (sds,vrtfile)
    return self.do_VRT(ifiles,ofilebase,db_key,db_value)   

  def do_VRT(self,ifiles,ofilebase,db_key,db_value):    
    # main purpose: we have the HDF files and the SDS
    # so build the VRTs for each SDS

    ofiles = []
    for i,sd in enumerate(self.sds):
      ofile = self.tidy(ofilebase.replace("__SDS__",self.sds[i]))
      spatial_file = Path(f"{self.local_dir[0]}",ofile)
      spatial_file.parent.mkdir(parents=True,exist_ok=True)

      # filter on s
      flist = [f for s,f in ifiles if s == sd]
      if len(flist):
        g = gdal.BuildVRT(spatial_file.as_posix(),flist)
        if not g:
          d = self.__dict__
          print(f"problem building dataset for {spatial_file} with {fdict(d)}")
          sys.exit(1)
        del g
        # make new pairs 
        ofiles.append((sd,Path(spatial_file).absolute().as_posix()))

    # store in db
    if len(ofiles)
      self.set_db(db_key,db_value,ofiles)
    return ofiles

  def set_db(self,db_key,db_value,entry,flush=True):
    # store in db
    database = self.get_database()
    cache = {db_key: { db_value : ofiles }}
    database.set_db(cache,write=flush)

  def get_database(self):
    if 'db_file' in self.__dict__:
      if 'database' not in self.__dict__:
        # load database
        d = self.__dict__.copy()
        self.database = Database(self.db_file,**(fdict(d,ignore=['db_dir','db_file'])))
    return self.database

  def get_keys(self,tile,year,doy):
    '''get DB key and value for year. doy
    year = int(year)
    doy  = int(doy)

    if type(tile) == list:
      stile = '_'.join(tile)
    else:
      stile = str(tile)

    dater = (datetime.datetime(year, 1, 1) +\
               datetime.timedelta(doy - 1)).strftime('%Y %m %d').split()
    syear    = f'{year}'
    smonth   = f'{str(int(dater[1])) :0>2s}'
    sday     = f'{str(int(dater[2])) :0>2s}'
    sversion = f'{str(int(self.version)) :0>2s}'

    # database key for this entry
    db_value = f"{stile}.{syear}.{smonth}.{sday}.{sversion}"
    db_key   = "modis"
    return db_key,db_value

  def get_from_db(self,db_key,db_value):
    # get the database
    database = self.get_database()

    # look up in database
    response = database.get_from_db(db_key,db_value)
    if response and self.noclobber:
      # test
      if self.test_ok(response[0]):
        # safe to return
        self.msg(f'positive response from database')
        ofiles = response
        return ofiles
      else:
        msg=f'WARNING: invalid entry {response[0]} in database {str(self.db_file)}'
        print(msg)
        self.msg(msg)
        return None
    return None

  def stitch_date_tile_sds(self,tile,year,doy,flush=True,get_files=False,test=False,do_all=True):
    '''
    produce a vrt of SDS for single tile

    '''
    db_key,db_value = self.get_keys(tile,year,doy)
    ofilebase = f"{self.product}/data.__SDS__.{db_value}.vrt"

    # get the URLS associated with this 
    d = self.__dict__.copy()
    fd = fdict(d)
    hdf_urls = self.get_url(**(fd))

    # nothing doing
    if not(len(hdf_urls) and (type(hdf_urls[0]) == URL)):
      if get_files:
        return None,None
      return [None]

    if not test and not get_files:
      ofiles = self.get_from_db(db_key,db_value)
      if ofiles is not None:
        return ofiles

    # so its not in the database ...
    # get the HDF file names    
    try:
      hdf_files = [str(f.local()) for f in hdf_urls]
    except:
      for f in hdf_urls:
        d = f.read_bytes()
      hdf_files = [str(f.local()) for f in hdf_urls]

    # just want the HDF filenames so return
    if get_files:
      return hdf_files

    # get the SDS fields for this product
    sds = self.get_sds(hdf_files,do_all=True)

    # catch in case not found from that
    # force a read, then look again
    if sds == []:
      for f in hdf_urls:
        d = f.read_bytes()
      del d
      hdf_files = [str(f.local()) for f in hdf_urls]
      sds = self.get_sds(hdf_files,do_all=True)

    # early return if we just want sds
    if (test == True) and len(sds):
      return sds

    # one last catch: might not be needed
    if len(sds) == 0:
      # failed to get SDS: need to download example file
      for f in hdf_urls:
        d = f.read_bytes()
      hdf_files = [str(f.local()) for f in hdf_urls]
      sds = self.get_sds(hdf_files,do_all=True)
      if test:
        return sds

    # main purpose: we have the HDF files and the SDS
    # so build the VRTs for each SDS

    ofiles = []
    # self.sds is a list if SDS names
    # sds is a list of HDF SDS specs
    for i,sd in enumerate(self.sds):
      ofile = self.tidy(ofilebase.replace("__SDS__",sd))
      spatial_file = Path(f"{self.local_dir[0]}",ofile)
      spatial_file.parent.mkdir(parents=True,exist_ok=True)
      g = gdal.BuildVRT(spatial_file.as_posix(),sds[i])
      if not g:
        d = self.__dict__
        print(f"problem building dataset for {spatial_file} with {fdict(d)}")
        sys.exit(1)
      del g
      ofiles.append((sd,Path(spatial_file).absolute().as_posix()))
    # store in db
    if len(ofiles)
      self.set_db(db_key,db_value,ofiles)
    return ofiles

  def get_files(self,year,doy):
    '''
    get MODIS dataset for specified doy and year

    return:
      files : list of filenames
      sds   : list of SDS names
    '''
    return self.stitch_date(year,doy,get_files=True)

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
 

    if product[:5] == "MOD10" or product[:5] == "MYD10":
      # NSIDC
      site = "https://n5eil01u.ecs.nsidc.org"
      self.msg(f"Snow and ice product {product}") 
      self.msg(f"switching to server {site}")

    if product[:3] == "MOD":
      code = "MOST"
    elif product[:3] == "MYD":
      code = "MOSA"
    else:
      code = "MOTA"
    self.msg(f"product {product} -> code {code}")

    # special cases 
    #if self.product[:5] == 'MCD19':
    #  self.site = 'https://ladsweb.modaps.eosdis.nasa.gov'
    # you should put some tests in
    site_dir = f'{code}/{product}.006/{year}.{month}.{day}'
    if site == 'https://ladsweb.modaps.eosdis.nasa.gov':
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
              "database"   : self.database.database,
              "local_dir"  : self.local_dir }

    hdf_urls = []
    url = None
    for t in self.tile:
      url = ((url is None) and URL(site,site_dir,**kwargs)) or \
             url.update(site,site_dir,**kwargs)
      hdf_urls += url.glob(f'{self.product}*.{t}*.hdf')
    if len(hdf_urls) == 0:
      return [None]

    self.db_file = hdf_urls[0].db_file
    
    return hdf_urls 

  def sdscode(self,s1):
    '''PITA decoding of SDS from HDF field that comes from s0,s1 in g.GetSubDatasets()'''
    return (' '.join(s1.split()[1:-3])).split(self.product)[0].split('MOD')[0].strip()

  def get_sds_names_from_hdffile(self,hdf_files):
    '''if need to, get SDS names from HDF files'''
    not_sds = ((self.sds is None) or len(self.sds) == 0 or \
               ((len(self.sds) == 1) and len(self.sds[0]) == 0))
    if not not_sds:
      return self.sds
    try:
      g = None
      # hopefully one of them exists!
      for lfile in hdf_files:
        if Path(lfile).exists():
          g = gdal.Open(str(lfile))
          break
      if not g:
        return []
    except:
      # need to pull an HDF file first
      try:
        del g
      except:
        pass
      return []

    self.msg("trying to get SDS names")
    if 'required_sds' not in self.__dict__:
      self.required_sds = self.sds
    self.sds = [self.sdscode(s1) for s0,s1 in g.GetSubDatasets()]
    cache = {"SDS": {self.product: self.sds}}
    self.database.set_db(cache,write=True)
    return self.sds

  def get_sds(self,hdf_files,do_all=False):
    '''try to get SDS names from HDF files'''
    all_sds = self.get_sds_names_from_hdffile(hdf_files)
    # force a list
    if type(hdf_files) is not list:
      hdf_files = [hdf_files]

    if (all_sds == []) or (len(hdf_files) < 1):
      return []

    all_subs  = [(s0.replace(str(lfile),'{local_file}'),s1) for s0,s1 in g.GetSubDatasets()]

    this_subs = []

    if (not do_all) and ('required_sds' in self.__dict__):
      sds = self.required_sds
    else:
      sds = self.sds

    for sd in sds:
      this_subs += [s0 for s0,s1 in all_subs if sd == self.sdscode(s1)]
    ofiles = [[sub.format(local_file=str(lfile)) for lfile in hdf_files] for sub in this_subs]
    return ofiles

def test_login(do_test,verbose=True):
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
  # test blank: try one that doesnt exist
  modis = Modis(product='MCD15A3H',verbose=False,local_dir='work')
  l = modis.stitch(2019,month=None,doy=[1,2],step=1)
  print(l)

  modis = Modis(product='MCD15A3H',verbose=False,local_dir='work')
  hdf_urls = modis.get_url(year="2019",month="*",day="0[1-4]")
  print(hdf_urls)

  kwargs = {
    'product'   :    'MCD12Q1',
    'local_dir' :    'work',
  }
  # get the data
  modis = Modis(**kwargs)
  # specify day of year (DOY) and year
  data_MCD12Q1 = modis.get_data(2011,1,step=366)
  print(data_MCD12Q1) 

if __name__ == "__main__":
    main()

