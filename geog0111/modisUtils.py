#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import datetime
import fnmatch
from urlpath import URL
from pathlib import Path
from osgeo import gdal
import datetime
import scipy
import scipy.ndimage
import requests

try:
  from geog0111.cylog import Cylog
except:
  from cylog import Cylog

'''
Some MODIS utils
'''

__author__    = "P. Lewis"
__email__     = "p.lewis@ucl.ac.uk"
__date__      = "28 Aug 2020"
__copyright__ = "Copyright 2020 P. Lewis"
__license__   = "GPLv3"

def modisHTML(year=2020, month=1, day=1,tile='h08v06',\
                 product='MCD15A3H',timeout=None,\
                 version='006',no_cache=False,cache=None,\
                 verbose=False,force=False,altcache='/shared/groups/jrole001/geog0111'):
    '''

    Example of use:

      from geog0111.modisUtils import modisHTML

      modinfo = {
        'product'  : 'MCD15A3H',
        'year'     : 2020,
        'month'    : 1,
        'day'      : 5,
        'tile'     : 'h08v06'
      }

      html,html_file = modisHTML(**modinfo,verbose=False)

    Returns:
      html  : string of html from MODIS data product page
              e.g. what you would find on 
              https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05

    Control options:
      year : int of year (2000+ for Terra, 2002+ for Aqua products)
             (year=2020)
      month: int of month (1-12) (month=1)
      day  : int of day (1-31, as appropriate) (day=1)
      tile : string of tile (tile='h08v06')  
      product : string of MODIS product name (product='MCD15A3H')
      version : int or string of version (version='006')
      timeout : timeout in seconds

      verbose : verbosity (verbose=False)
      
    
    Cache options:
      no_cache : Set True if you don't want to use the cache 
                 (no_cache=False)

                 This is common for most functions, but 
                 modisFile() will use a cache in any case, 
                 as it has to store the file somewhere. 
                 If you don;'t want to keep that, then 
                 you can delete after use.
      cache    : Use cache='/home/somewhere/else' to specify 
                 a personal cache location with write permission 
                 (ie somewhere in your filespace)
                 Specify personal cache root. By default, 
                 this will be ~, and the cache will go into 
                 ./.modis_cache. You can change that to 
                 somewhere else
                 here. It will still use the sub-directory 
                 .modis_cache.
                 Use cache='/home/somewhere/else' to specify a 
                 personal cache location with write permission 
                 (ie somewhere in your filespace)
      altcache : Specify system cache root. 
                 Use altcache='/home/notme/somewhere' to specify a 
                 system cache location with read permission 
                 (ie somewhere not necessarily in your filespace)
      force    : Bool : Use force=True to override information in the cache
      

    Get the HTML associated with a MODIS product
    for a certain date and version. Since this can
    be an expensive call, the html can be cached unless no_cache = True

    This function returns the HTML for the product/date page listing
    
    You can use this to discover data file names/URLs by parsing
    the html.

    The caching is done to avoid repeated calls to expensive URL downloads.
    The idea is that there will be a system cache, where shared files will
    be set up (where you have read permission), and a personal cache
    where you can read and write your own files. Unless you
    use force=True or disble cache with no_cache=True, then the code
    will look in (i) personal; (ii) system cache before attempting
    to download any file from a URL. 

    The cached files are stored in the same structure as the URL, i.e
    
    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf
    
    will be stored (personal cache) as:
 
    ./.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    The html cache is what is returned from e.g.

    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05

    and is stored as eg

    ./.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/index.html

    '''
    year  = int(year)
    month = int(month)
    day  = int(day)
    version = f'{int(version):03d}'

    if verbose:
      print('modisHTML')
      print(f'year : {year}\nmonth : {month}\nday : {day}\ntile : {tile}')
      print(f'product : {product}\nversion : {version}\nforce : {force}')
      print(f'altcache : {altcache}')
      print(f'cache : {cache}')

    if not no_cache:
      if cache == None:
        cache = Path().cwd() # You can change the default here Path.home()

      cache = cache / ".modis_cache"
      cache.mkdir(parents=True,exist_ok=True)
      if verbose:
        print(f'cache {cache}')

    #import pdb;pdb.set_trace()
    server = modisServer(product,version=version) / f'{year}.{month:02d}.{day:02d}' 
    #server = server.with_userinfo(*Cylog(server.anchor).login())

    if verbose:
      print(f'server {server}')

    if not no_cache:
      # get cache_file
      cache_dir = Path(cache,server.hostinfo,'/'.join(server.parts[1:]))
      cache_dir.mkdir(parents=True,exist_ok=True)
      if verbose:
        print(f'cache_dir : {cache_dir}')

      # cache file
      cache_file = cache_dir / 'index.html'
      if verbose:
        print(f'cache_file : {cache_file}')

      # alternate cache
      if altcache:
        altcache_dir = Path(altcache,server.hostinfo,'/'.join(server.parts[1:]))
        altcache_file = altcache_dir / 'index.html'
        if verbose:
          print(f'altcache_file : {altcache_file}')

    html = None
    html_file = None

    if no_cache or ((not cache_file.exists()) \
       and (altcache !=  None and not altcache_file.exists())) or force:
        # we have to pull the file
        if verbose:
          print(f'getting data from server ...')
        #import pdb;pdb.set_trace()
        url = server
        with requests.Session() as s:
            s.auth = Cylog(url.anchor).login()
            r1 = requests.get(str(server))
            r = s.get(r1.url, stream=True)
            #r = server.get(timeout=timeout)
        if verbose:
          print(f'status code: {r.status_code}')

        if r.status_code == 200:
          html = r.text
          if not no_cache and (altcache != None and not altcache_file.exists()):
            # write to cache
            cache_file.write_text(html)
            html_file = cache_file
        else:
            if verbose:
                print(f'some issue without password for html {server.anchor}') 
                #import pdb;pdb.set_trace()
                getIndex((server/'index.html').as_posix(),cache_dir.as_posix())
                # https://n5eil01u.ecs.nsidc.org/MOST/MOD10A1.006/
    else:
        if cache_file.exists():
          if verbose:
            print(f'reading from cache_file')
          html = cache_file.read_text() 
          html_file = cache_file
        elif altcache != None and altcache_file.exists():
          if verbose:
            print(f'reading from altcache_file') 
          html = altcache_file.read_text()
          html_file = altcache_file
    return html,html_file 

def modisServer(product='MCD15A3H',version='006',**kwargs):
    '''
    modisServer : return the server and dirbase for
                  a given product. 

    e.g. modisServer('MCD15A3H') ->  https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006

    Example of use:

      from geog0111.modisUtils import modisServer

      modinfo = {
        'product'  : 'MCD15A3H',
        'year'     : 2020,
        'month'    : 1,
        'day'      : 5,
        'tile'     : 'h08v06'
      }

      server = modisServer(**modinfo,verbose=False)
      print(f'-> {server}')
      -> https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006

    Returns:
      server   : URL of core MODIS data product page
                 e.g. https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006

    Control options:
      tile : string of tile (tile='h08v06')  
      product : string of MODIS product name (product='MCD15A3H')
    
    Note that other kwargs are allowed (for compatibility) but ignored.

    '''

    if product[:5] == "MOD10" or product[:5] == "MYD10":
        # NSIDC
        site = "https://n5eil01u.ecs.nsidc.org"    
        # Terra and Aqua
        if product[:3] == 'MCD':
          sub = 'MOTA'
          # Terra
        elif product[:3] == 'MOD':
          sub = 'MOST'
          # Aqua
        elif product[:3] == 'MYD':
          sub = 'MOSA' 
        else:
          sub = 'UKNOWN'
    
    else:
        site = "https://e4ftl01.cr.usgs.gov"

        # Terra and Aqua
        if product[:3] == 'MCD':
          sub = 'MOTA'
          # Terra
        elif product[:3] == 'MOD':
          sub = 'MOLT'
          # Aqua
        elif product[:3] == 'MYD':
          sub = 'MOLA' 
        else:
          sub = 'UKNOWN'

    return URL(site,sub,product+'.'+version)    

def modisURL(year=2020, month=1, day=1,tile='h08v06',\
                 product='MCD15A3H',\
                 version='006',timeout=None,\
                 no_cache=False,cache=None,\
                 verbose=False,force=False,altcache='/shared/groups/jrole001/geog0111'):
    '''
    modisURL : return the URL for a MODIS product
               E.g.
               https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    Example of use:

      from geog0111.modisUtils import modisURL

      modinfo = {
        'product'  : 'MCD15A3H',
        'year'     : 2020,
        'month'    : 1,
        'day'      : 5,
        'tile'     : 'h08v06'
      }

      url = modisURL(**modinfo,verbose=False)
      print(f'-> {url}')
      -> https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf
    Returns:
      url  : Url (urlpath URL object) of MODIS data product
              e.g. https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    Control options:
      year : int of year (2000+ for Terra, 2002+ for Aqua products)
             (year=2020)
      month: int of month (1-12) (month=1)
      day  : int of day (1-31, as appropriate) (day=1)
      tile : string of tile (tile='h08v06')  
      product : string of MODIS product name (product='MCD15A3H')
      version : int or string of version (version='006')
      timeout : timeout in seconds

      verbose : verbosity (verbose=False)
      
    Cache options:
      no_cache : Set True if you don't want to use the cache 
                 (no_cache=False)

                 This is common for most functions, but 
                 modisFile() will use a cache in any case, 
                 as it has to store the file somewhere. 
                 If you don;'t want to keep that, then 
                 you can delete after use.
      cache    : Use cache='/home/somewhere/else' to specify 
                 a personal cache location with write permission 
                 (ie somewhere in your filespace)
                 Specify personal cache root. By default, 
                 this will be ~, and the cache will go into 
                 ~/.modis_cache. You can change that to 
                 somewhere else
                 here. It will still use the sub-directory 
                 .modis_cache.
                 Use cache='/home/somewhere/else' to specify a 
                 personal cache location with write permission 
                 (ie somewhere in your filespace)
      altcache : Specify system cache root. 
                 Use altcache='/home/notme/somewhere' to specify a 
                 system cache location with read permission 
                 (ie somewhere not necessarily in your filespace)
      force    : Bool : Use force=True to override information in the cache
      
    Get the URL associated with a MODIS product
    for a certain date and version. Since this can
    involve  an expensive call to get the html to access the file URL
    The html data used can be cached unless no_cache = True
    (See modisHTML())

    This function returns the URL for the product/date page listing

    The caching is done to avoid repeated calls to expensive URL downloads.
    The idea is that there will be a system cache, where shared files will
    be set up (where you have read permission), and a personal cache
    where you can read and write your own files. Unless you
    use force=True or disble cache with no_cache=True, then the code
    will look in (i) personal; (ii) system cache before attempting
    to download any file from a URL. 

    The cached files are stored in the same structure as the URL, i.e
    
    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf
    
    will be stored (personal cache) as:
 
    ~/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    The html cache is what is returned from e.g.

    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05

    and is stored as eg

    ~/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/index.html

    '''

    server = modisServer(product,version=version) / f'{year}.{month:02d}.{day:02d}'

    html,html_file = modisHTML(year, month, day,tile,\
                 product=product,\
                 version=version,no_cache=no_cache,cache=cache,\
                 verbose=verbose,force=force,altcache=altcache)

    if html:
      doy = datetime.date(year, month, day).strftime('%j')
      filename_start = f'{product}.A{year}{doy}.{tile}.{version}'

      # use BeautifulSoup and fnmatch to find match in the html
      links = [mylink.attrs['href'] for mylink in BeautifulSoup(html,'lxml').find_all('a')]
      filenames = [l for l in links if fnmatch.fnmatch(str(l), filename_start+'*'+'.hdf')]
    
      if len(filenames):
            filename = filenames[0]
      else:
            print(f"Problem with request: Can't find pattern {filename_start}*.hdf in {html_file}")
            #import pdb;pdb.set_trace()
            return None
        
      # result
      if verbose:
        print(f'filename: {filename}')
      
      return server / filename
    return None


def modisFile(year=2020, month=1, day=1,tile='h08v06',\
                 product='MCD15A3H',timeout=None,\
                 version='006',no_cache=False,cache=None,\
                 verbose=False,force=False,altcache='/shared/groups/jrole001/geog0111'):
    '''
    Get the filename associated with a MODIS product file
    for a certain date and version. 

    modisFile : return the filename for a MODIS product
               E.g.
               /Users/plewis/.modis_cache/e4ftl01.cr.usgs.gov/\
                    MOTA/MCD15A3H.006/2020.01.05/\
                    MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    N.B. You need to have a username and password to access the data.
    These are available at https://urs.earthdata.nasa.gov

    Example of use:

      from geog0111.modisUtils import modisURL, modisFile

      modinfo = {
        'product'  : 'MCD15A3H',
        'year'     : 2020,
        'month'    : 1,
        'day'      : 5,
        'tile'     : 'h08v06'
      }

      url = modisURL(**modinfo,verbose=False)
      print(f'-> {url}')

      filename = modisFile(**modinfo,verbose=False)
      print(f'-> {filename}')

      -> https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

      -> /Users/plewis/.modis_cache/e4ftl01.cr.usgs.gov/\
           MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf


    Returns:
      filename  : Path object of MODIS data product file
              e.g. what you would find on 

              https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

              Downloaded to some cache location e.g.

              /Users/plewis/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    Control options:
      year : int of year (2000+ for Terra, 2002+ for Aqua products)
             (year=2020)
      month: int of month (1-12) (month=1)
      day  : int of day (1-31, as appropriate) (day=1)
      tile : string of tile (tile='h08v06')  
      product : string of MODIS product name (product='MCD15A3H')
      version : int or string of version (version='006')
      timeout : timeout in seconds

      verbose : verbosity (verbose=False)
      
      
    Cache options:
      no_cache : Set True if you don't want to use the cache 
                 (no_cache=False)

                 This is common for most functions, but 
                 modisFile() will use a cache in any case, 
                 as it has to store the file somewhere. 
                 If you don;'t want to keep that, then 
                 you can delete after use.
      cache    : Use cache='/home/somewhere/else' to specify 
                 a personal cache location with write permission 
                 (ie somewhere in your filespace)
                 Specify personal cache root. By default, 
                 this will be ~, and the cache will go into 
                 ~/.modis_cache. You can change that to 
                 somewhere else
                 here. It will still use the sub-directory 
                 .modis_cache.
                 Use cache='/home/somewhere/else' to specify a 
                 personal cache location with write permission 
                 (ie somewhere in your filespace)
      altcache : Specify system cache root. 
                 Use altcache='/home/notme/somewhere' to specify a 
                 system cache location with read permission 
                 (ie somewhere not necessarily in your filespace)
      force    : Bool : Use force=True to override information in the cache
      
    Get the URL associated with a MODIS product
    for a certain date and version. Since this can
    involve  an expensive call to get the html to access the file URL
    The html data used can be cached unless no_cache = True
    (See modisHTML())

    This function returns the URL for the product/date page listing

    The caching is done to avoid repeated calls to expensive URL downloads.
    The idea is that there will be a system cache, where shared files will
    be set up (where you have read permission), and a personal cache
    where you can read and write your own files. Unless you
    use force=True or disble cache with no_cache=True, then the code
    will look in (i) personal; (ii) system cache before attempting
    to download any file from a URL. 

    The cached files are stored in the same structure as the URL, i.e
    
    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/\
                MCD15A3H.A2020005.h08v06.006.2020010210940.hdf
    
    will be stored (personal cache) as:
 
    ~/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/\
                MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    The html cache is what is returned from e.g.

    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05

    and is stored as eg

    ~/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/index.html

    '''
    if verbose:
      print('modisFile')
      print(f'year : {year}\nmonth : {month}\nday : {day}\ntile : {tile}')
      print(f'product : {product}\nversion : {version}\nforce : {force}')
      print(f'altcache : {altcache}')
      print(f'cache : {cache}')

    # get the URL for the file of interest
    url = modisURL(year, month, day,tile,product=product,version=version,\
                   no_cache=no_cache,cache=cache,altcache=altcache,\
                   force=force,verbose=verbose)

    if url == None:
        print(f'No dataset URL found for conditions requested.')
        print(f'Check the date and tile for the dataset URL that you have requested: {modisServer(product=product,version=version)}')
        print('modisFile')
        print(f'year : {year}\nmonth : {month}\nday : {day}\ntile : {tile}')
        print(f'product : {product}\nversion : {version}\nforce : {force}')
        print(f'altcache : {altcache}')
        print(f'cache : {cache}')
        print(f'If you think that is ok, then first try to rerun')
        print(f'If you still have problems, perhaps use: force=True')
        print(f'and try setting timout, e.g. timout=200 (it is in seconds)')
        return None
    if cache == None:
      cache = Path().cwd()
    cache = cache / ".modis_cache"
    cache.mkdir(parents=True,exist_ok=True)
    if not no_cache:
      if verbose:
        print(f'cache {cache}')
    #import pdb;pdb.set_trace()
    # generate the Path where the local cache would go
    cache_part = Path(url.hostinfo,'/'.join(url.parts[1:]))

    # check to see if we have it
    if (not no_cache) and (not force) and Path(cache,cache_part).exists():
      if verbose:
        print('getting from cache')
      return Path(cache,cache_part)

    # get from cache.store for backwards compatibility
    if (not no_cache) and (not force) and cache and Path(cache,cache_part.as_posix() + '.store').exists():
      if verbose:
        print('getting from cache in backward compatibility mode')
      return Path(cache,cache_part.as_posix() + '.store')

    # get from altcache
    if (not no_cache) and (not force) and altcache and Path(altcache,cache_part).exists():
      if verbose:
        print('getting from altcache')
      return Path(altcache,cache_part)

    # get from altcache.store
    if (not no_cache) and (not force) and altcache and Path(altcache,cache_part.as_posix() + '.store').exists():
      if verbose:
        print('getting from altcache in backward compatibility mode')
      return Path(altcache,cache_part.as_posix() + '.store')

    # else pull the file
    # first try a get : we have to do this twice bacause of
    # auth redirect
    if verbose:
        print(f'logging in to {url.anchor}') 

    #url2 = url.with_userinfo(*Cylog(url.anchor).login())
    if verbose:
        print(f'get info from {url.anchor}') 

    # replace this for 2022/23 using with
    #r = url2.get(timeout=timeout)
    #if verbose:
    #    print(f'get data from {url.anchor}') 
    #url3=URL(r.url).with_userinfo(*Cylog(url.anchor).login())
    #r2 = url3.get(timeout=timeout)
    #import pdb;pdb.set_trace() 
    with requests.Session() as s:
        s.auth = Cylog(url.anchor).login()
        r1 = requests.get(str(url))
        r2 = s.get(r1.url, stream=True)

    if verbose:
        print(f'done - status code {r2.status_code}') 
        
    if r2.status_code == 200:
      data = r2.content
      if verbose:
        print(f"received {len(data)} bytes")
      # write to cache file
      cache_file = cache / cache_part
      cache_file.parent.mkdir(parents=True,exist_ok=True)
      nbytes_written = cache_file.write_bytes(data)
      if not (nbytes_written == len(data)):
        if verbose:
          print(f'error writing cache file {cache_file}: {len(data)} bytes expected but {nbytes_written} bytes written')
          return None
        else:
          print(f'cached data to file {cache_file}: {len(data)}')
      return cache_file
    else:
      if verbose:
        print(f'failed to pull data from {url.anchor}')
    return None

def getDate(day=1, month=1,year=2020,doy=None):
    '''
    return day, month, year from doy or day, month, year
    '''
    if doy != None:
        # use doy to month and day
        dt = datetime.datetime(year, 1, 1) + datetime.timedelta(doy - 1)
        day, month = dt.day,dt.month
    return day, month, year

def get_sds_name(name,product):
    if product[:5] != "MCD64":
        sds_name = name.split()[1]
    else:
        sds_name = ' '.join(name.split()[1:3])
        if name.split()[3] == "Uncertainty":
            sds_name = f'{sds_name} Uncertainty'
    return sds_name

def getModisFiles(doys=None,year=2020,tile='h08v06',doy=None,month=None,\
                 product='MCD15A3H',timeout=None,sds='None',\
                 version='006',no_cache=False,cache=None,\
                 verbose=False,force=False,altcache='/shared/groups/jrole001/geog0111'):
    '''
    return list of MODIS data filenames of given SDS for given MODIS tile

    N.B. You need to have a username and password to access the data.
    These are available at https://urs.earthdata.nasa.gov

    Example of use:

      from geog0111.modisUtils import getModisFiles

      modinfo = {
        'product'  : 'MCD15A3H',
        'year'     : 2020,
        'doys'     : [1,5]
        'tile'     : 'h08v06'
      }

      data = getModisFiles(**modinfo,verbose=False)
      print(f'-> {*data.keys()}')

      -> Fpar_500m Lai_500m FparLai_QC FparExtra_QC FparStdDev_500m LaiStdDev_500m


    Returns file list of MODIS data product filef
              e.g. what you would find on 

           https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

              Downloaded to some cache location e.g.

              /Users/plewis/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    Control options:
      year : int of year (2000+ for Terra, 2002+ for Aqua products)
             (year=2020)
             
      doy  : day of year (doy=None)
      OR
      month: int of month (1-12) (month=1)
      day  : int of day (1-31, as appropriate) (day=1)
      
      tile    : string of tile (tile='h08v06')  
      product : string of MODIS product name (product='MCD15A3H')
      version : int or string of version (version='006')
      sds     : only load these SDS (string or list)
           
      timeout : timeout in seconds
      verbose : verbosity (verbose=False)
      
      
    Cache options:
      no_cache : Set True if you don't want to use the cache 
                 (no_cache=False)

                 This is common for most functions, but 
                 modisFile() will use a cache in any case, 
                 as it has to store the file somewhere. 
                 If you don;'t want to keep that, then 
                 you can delete after use.
      cache    : Use cache='/home/somewhere/else' to specify 
                 a personal cache location with write permission 
                 (ie somewhere in your filespace)
                 Specify personal cache root. By default, 
                 this will be ~, and the cache will go into 
                 ~/.modis_cache. You can change that to 
                 somewhere else
                 here. It will still use the sub-directory 
                 .modis_cache.
                 Use cache='/home/somewhere/else' to specify a 
                 personal cache location with write permission 
                 (ie somewhere in your filespace)
      altcache : Specify system cache root. 
                 Use altcache='/home/notme/somewhere' to specify a 
                 system cache location with read permission 
                 (ie somewhere not necessarily in your filespace)
      force    : Bool : Use force=True to override information in the cache
      
    Get the URL associated with a MODIS product
    for a certain date and version. Since this can
    involve  an expensive call to get the html to access the file URL
    The html data used can be cached unless no_cache = True
    (See modisHTML())

    This function returns the URL for the product/date page listing

    The caching is done to avoid repeated calls to expensive URL downloads.
    The idea is that there will be a system cache, where shared files will
    be set up (where you have read permission), and a personal cache
    where you can read and write your own files. Unless you
    use force=True or disble cache with no_cache=True, then the code
    will look in (i) personal; (ii) system cache before attempting
    to download any file from a URL. 

    The cached files are stored in the same structure as the URL, i.e
    
    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf
    
    will be stored (personal cache) as:
 
    ~/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    The html cache is what is returned from e.g.

    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05

    and is stored as eg

    ~/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/index.html

    '''
    if type(sds) == str:
        sds = [sds]
        
    if type(tile) == str:
        tile = [tile]
        
    if type(doys) == int:
        doys = [doys]
    #import pdb;pdb.set_trace()

    # set up blank dictionary for output
    odata = {}

    if len(doys) == 0:
        doys = np.arange(1,366)
        
    # loop over doys
    for t in tile:
        for doy in doys:
            day, month, year = getDate(day=None, month=None, year=year, doy=doy)
            filename = modisFile(year=year, month=month, day=day,tile=t,\
                     product=product,timeout=timeout,\
                     version=version,no_cache=no_cache,cache=cache,\
                     verbose=verbose,force=force,altcache=altcache)

            if filename:
                # error checking
                if verbose:
                    print(f'reading dataset from {filename}')
                g = gdal.Open(filename.as_posix())
                if g:
                    for filename,name in g.GetSubDatasets():
                        sds_name = get_sds_name(name,product)
                        if (sds == None) or (sds == ['None']) or (sds_name in sds):
                            # get the SDS
                            sds_name = get_sds_name(name,product)
                            if verbose:
                                print(f'dataset info is: {name}')
                            
                            if sds_name not in odata.keys():
                                odata[sds_name] = {}
                            if doy not in odata[sds_name]:
                                odata[sds_name][doy] = {}
                            # load into dictionary
                            odata[sds_name][doy][t] = filename
    return odata



def getModisTiledata(doy=None,year=2020, month=1, day=1,tile='h08v06',\
                 product='MCD15A3H',timeout=None,sds='None',\
                 version='006',no_cache=False,cache=None,\
                 verbose=False,force=False,altcache='/shared/groups/jrole001/geog0111'):
    '''
    return MODIS data dictionary of given SDS for given MODIS tile

    N.B. You need to have a username and password to access the data.
    These are available at https://urs.earthdata.nasa.gov

    Example of use:

      from geog0111.modisUtils import getModisdata

      modinfo = {
        'product'  : 'MCD15A3H',
        'year'     : 2020,
        'month'    : 1,
        'day'      : 5,
        'tile'     : 'h08v06'
      }

      data = getModisdata(**modinfo,verbose=False)
      print(f'-> {*data.keys()}')

      -> Fpar_500m Lai_500m FparLai_QC FparExtra_QC FparStdDev_500m LaiStdDev_500m


    Returns data read from MODIS data product file
              e.g. what you would find on 

           https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

              Downloaded to some cache location e.g.

              /Users/plewis/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    Control options:
      year : int of year (2000+ for Terra, 2002+ for Aqua products)
             (year=2020)
             
      doy  : day of year (doy=None)
      OR
      month: int of month (1-12) (month=1)
      day  : int of day (1-31, as appropriate) (day=1)
      
      tile    : string of tile (tile='h08v06')  
      product : string of MODIS product name (product='MCD15A3H')
      version : int or string of version (version='006')
      sds     : only load these SDS (string or list)
           
      timeout : timeout in seconds
      verbose : verbosity (verbose=False)
      
      
    Cache options:
      no_cache : Set True if you don't want to use the cache 
                 (no_cache=False)

                 This is common for most functions, but 
                 modisFile() will use a cache in any case, 
                 as it has to store the file somewhere. 
                 If you don;'t want to keep that, then 
                 you can delete after use.
      cache    : Use cache='/home/somewhere/else' to specify 
                 a personal cache location with write permission 
                 (ie somewhere in your filespace)
                 Specify personal cache root. By default, 
                 this will be ~, and the cache will go into 
                 ~/.modis_cache. You can change that to 
                 somewhere else
                 here. It will still use the sub-directory 
                 .modis_cache.
                 Use cache='/home/somewhere/else' to specify a 
                 personal cache location with write permission 
                 (ie somewhere in your filespace)
      altcache : Specify system cache root. 
                 Use altcache='/home/notme/somewhere' to specify a 
                 system cache location with read permission 
                 (ie somewhere not necessarily in your filespace)
      force    : Bool : Use force=True to override information in the cache
      
    Get the URL associated with a MODIS product
    for a certain date and version. Since this can
    involve  an expensive call to get the html to access the file URL
    The html data used can be cached unless no_cache = True
    (See modisHTML())

    This function returns the URL for the product/date page listing

    The caching is done to avoid repeated calls to expensive URL downloads.
    The idea is that there will be a system cache, where shared files will
    be set up (where you have read permission), and a personal cache
    where you can read and write your own files. Unless you
    use force=True or disble cache with no_cache=True, then the code
    will look in (i) personal; (ii) system cache before attempting
    to download any file from a URL. 

    The cached files are stored in the same structure as the URL, i.e
    
    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf
    
    will be stored (personal cache) as:
 
    ~/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf

    The html cache is what is returned from e.g.

    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05

    and is stored as eg

    ~/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/index.html

    '''
    if type(sds) == str:
        sds = [sds]
           
    # set up blank dictionary for output
    odata = {}
    day, month, year = getDate(day=day, month=month, year=year, doy=doy)
    #import pdb;pdb.set_trace()
    filename = modisFile(year=year, month=month, day=day,tile=tile,\
                 product=product,timeout=timeout,\
                 version=version,no_cache=no_cache,cache=cache,\
                 verbose=verbose,force=force,altcache=altcache)
    
    # error checking
    if verbose:
        print(f'reading dataset from {filename}')
    #import pdb;pdb.set_trace()
    if not filename:
        return odata
    g = gdal.Open(filename.as_posix())
    if g:
        for filename,name in g.GetSubDatasets():
            sds_name = get_sds_name(name,product)
            if (sds == None) or (sds == ['None']) or (sds_name in sds):
                # get the SDS
                if verbose:
                    print(f'dataset info is: {name}')
                # read the dataset
                gsub = gdal.Open(filename)
                if gsub:
                    data = gsub.ReadAsArray()
                    sds_name = get_sds_name(name,product)
                    # load into dictionary
                    odata[sds_name] = data
    return odata


    
def stitchModisDate(year=2019,doy=1,sds='Lai_500m',timeout=None,\
              tile=['h17v03','h18v03'],verbose=False,\
              product='MCD15A3H'):
    '''
    function called stitchModisDate with arguments:
    
    year
    doy

    keywords/defaults:

        sds      : 'Lai_500m'
        tile     : ['h17v03','h18v03']
        product  : 'MCD15A3H'

    generates a stitched VRT file with the appropriate data,

    returns VRT filename for this dataset.
    
    Options:
    timeout : None
    verbose : False
    
    '''
    
    kwargs = {
        'product'    : product,
        'tile'       : tile,
        'year'       : year,
        'doys'       : [doy],
        'sds'        : [sds]
    }
    #import pdb;pdb.set_trace()
    data = getModisFiles(verbose=verbose,timeout=1000,**kwargs)

    ofiles = []
    
    for sds,sds_v in data.items():
        if verbose:
            print('sds',sds)
        for doy,doy_v in sds_v.items():
            if verbose:
                print('doy',doy)
            # build a VRT 
            tiles = doy_v.keys()

            ofile = f"work/stitch_{sds}_{kwargs['year']}_{doy:03d}_{'Tiles_'+'_'.join(tiles)}.vrt"
            if verbose:
                print(f'saving to {ofile}')    
            stitch_vrt = gdal.BuildVRT(ofile, list(doy_v.values()))
            del stitch_vrt
            ofiles.append(ofile)
    #import pdb;pdb.set_trace()    
    if len(ofiles):
        return ofiles[0]
    else:
        print(f'error in stitchModisDate: {data}\n{kwargs}')
        return None

def getModis(year=2019,doys=[1],sds='Lai_500m',\
              tile=['h17v03','h18v03'],\
              format='VRT',verbose=False,timeout=None,\
              product='MCD15A3H',warp_args={}):
    '''
    function to return Modis data array for defined
    conditions, for a single day and single SDS and
    product.
    
    Arguments:
        year     : int - year (2019)
        doys     : list of int - day of year ([1])
        sds      : SDS we want to retrieve ('Lai_500m')
        tile     : list of tiles to process (['h17v03','h18v03'])
        product  : MODIS data product (MCD15A3H')
        warp_args: cropping or warping arguments ({})
        
        ofile    : output (GTiff) filename
        format   : 'VRT' or 'GTiff' ('VRT' default)
        
        verbose  : verbose (False)
        timeout  : timeout (None) in seconds. Set to e.g. 1000 if
                   you are having problems
 
  
    generates stitched VRT files for each doy with the appropriate data,
    save in VRT of GTiff, along with data you can use to identify the year and doy 

    returns:
    
        VRT (or GTiff) filename, a list of strings of year-doy
    '''
    ofiles = []
    bnames = []
    year = int(year)
    #import pdb;pdb.set_trace()
    for doy in doys:
        doy = int(doy)
        bnames.append(f'{year}-{doy:03d}')
        kwargs = {
            'product'    : product,
            'tile'       : tile,
            'year'       : year,
            'doy'       : doy,
            'sds'        : sds
        }
        if verbose:
            print(kwargs)
        vrtFile = stitchModisDate(verbose=verbose,timeout=timeout,**kwargs)

        warp_args['format']   = format
        if vrtFile == None or len(vrtFile) == 0:
            print(f'Problem with doy {doy} ... continuing ...')
        else:
            # things are good
            ofile = vrtFile[:-4]

            if 'cutlineWhere' in warp_args:
                # put the selektor in the filename
                ext = warp_args['cutlineWhere']
                # but tidy it up for awkward characters
                ext = ext.replace("'","").replace('"',"").replace('=','_')
                ofile = f'{ofile}_Selektor_{ext}'

            if format == 'GTiff':
                warp_args['options']  = ['COMPRESS=LZW']
                ofile = f'{ofile}_warp.tif'
            elif format == 'VRT':
                ofile = f'{ofile}_warp.vrt'
            else:
                ofile = f'{ofile}_warp.dat'

            # build a VRT for the first SDS
            #import pdb;pdb.set_trace()
            #if type(kwargs['sds']) == str:
            #    builder = kwargs['sds']
            #else:
            #    try:
            #        builder = kwargs['sds'][0]
            #    except:
            #        print(f"problem with SDS specification {kwargs['sds']}: should be str or first item in list")
            #        return None,None
            #stitch_vrt = gdal.BuildVRT(vrtFile, builder)
            #del stitch_vrt
            # now warp it
            if (len(warp_args.keys()) == 0) and format == 'VRT':
                if verbose:
                    print('No warp_args specified')
                ofile = vrtFile
            else:

                if verbose:
                    print(f'selecting from {vrtFile} to {ofile}')
                g = gdal.Warp(ofile, vrtFile,**warp_args)
                g.FlushCache()
                del g
            ofiles.append(ofile)
        
    return ofiles,bnames


def modisAnnual(ofile_root='work/output_filename',**kwargs):
    '''
        generate dictionary of SDS datasets as VRT files
    
       arguments based on:

        warp_args = {
            'dstNodata'     : 255,
            'format'        : 'MEM',
            'cropToCutline' : True,
            'cutlineWhere'  : "FIPS='LU'",
            'cutlineDSName' : 'data/TM_WORLD_BORDERS-0.3.shp'
        }

        kwargs = {
            'tile'      :    ['h18v03','h18v04'],
            'product'   :    'MCD15A3H',
            'sds'       :    ['Lai_500m', 'Fpar_500m'],
            'doys'      : [i for i in range(1,60,4)],
            'year'      : 2019,
            'warp_args' : warp_args
        }
        
        Return odict,bnames
        
        where odict keys are SDS values and the values VRT filenames
    '''
    if 'sds' in kwargs:
        sds_list =  kwargs['sds']
    else:
        print("You need to specify 'sds' in calling modisAnnual")
        print(kwargs)
        return None,None

    if 'year' in kwargs:
        year =  kwargs['year']
    else:
        print("You need to specify 'year' in calling modisAnnual")
        print(kwargs)
        return None,None
    
    if 'doys' in kwargs:
        doys =  np.array(kwargs['doys'])
    else:
        print("You need to specify 'doys' in calling modisAnnual")
        print(kwargs)
        return None,None
    
    if 'verbose' in kwargs:
        verbose = kwargs['verbose']
    else:
        verbose = False
 
    # output dict
    odict = {}
    if ('force' in kwargs.keys()) and kwargs['force'] == False:
        redo = False
        del kwargs['force']
    elif ('force' in kwargs.keys()) and kwargs['force'] == True:
        redo = True
        del kwargs['force']
    else:
        redo = True
        
    if 'warp_args' in kwargs:
        warp_args = kwargs['warp_args']
        if 'cutlineWhere' in warp_args:
            # put the selektor in the filename
            ext = warp_args['cutlineWhere']
            # but tidy it up for awkward characters
            ext = ext.replace("'","").replace('"',"").replace('=','_')
            ofile_root = f'{ofile_root}_Selektor_{ext}'
            if verbose:
                print(f'selektor: {ext}')
        
    bnames = []  
    
    ofile_root = f'{ofile_root}_YEAR_{year}_DOYS_{doys.min()}_{doys.max()}'
    if verbose:
        print(f'root name of output file: {ofile_root}')
    
    for s in sds_list:
        datafiles = None
        ofile = f"{ofile_root}_SDS_{s}.vrt"
        bofile = Path(f'{ofile}_bands')
        if not redo:
            if (not Path(ofile).exists()) or (not bofile.exists()):
                kwargs['sds'] = s 
                datafiles,bnames = getModis(**kwargs) 
                if datafiles != None:
                    stitch_vrt = gdal.BuildVRT(ofile, datafiles,separate=True)
                    # save the band names
                    bofile = Path(f'{ofile}_bands')
                    bofile.write_text(' '.join(bnames))
                    del stitch_vrt
                 
        else:
            kwargs['sds'] = s 
            datafiles,bnames = getModis(**kwargs) 
            if datafiles != None:
                stitch_vrt = gdal.BuildVRT(ofile, datafiles,separate=True)
                del stitch_vrt
                # save the band names
                bofile = Path(f'{ofile}_bands')
                bofile.write_text(' '.join(bnames))
        if datafiles != None:
            odict[s] = ofile
            bofile = Path(f'{ofile}_bands')
            bnames = bofile.read_text().split()
    return odict,bnames

import numpy as np
from osgeo import gdal


def getLai(year=2019,tile=['h18v03','h18v04'],country='LU',\
           force=False,\
           ofile_root='work/modisLAI',verbose=False):
    '''
    Get LAI and std for year,tile,country
    
    Options:
    You should fill these out!!
    
    '''

    # filename
    s = f'{ofile_root}_{year}_{country}_Tiles_{"_".join(tile)}'

    warp_args = {
        'dstNodata'     : 255,
        'format'        : 'MEM',
        'cropToCutline' : True,
        'cutlineWhere'  : f"FIPS='{country}'",
        'cutlineDSName' : 'data/TM_WORLD_BORDERS-0.3.shp'
    }

    kwargs = {
        'tile'      :    tile,
        'product'   :    'MCD15A3H',
        'sds'       :    ['Lai_500m','LaiStdDev_500m']
    ,
        'doys'      : [i for i in range(1,366,4)],
        'year'      : year,
        'warp_args' : warp_args,
        'verbose'   : False
    }
    

    # run
    if verbose:
        print(f'gathering modis annual data for {kwargs}')
        
    
    odict,bnames = modisAnnual(**kwargs)
    
    # read the data
    if verbose:
        print(f'reading datasets')
    ddict = {}
    for k,v in odict.items():
        if verbose:
            print(f'...{k} -> {v}')
        g = gdal.Open(v)
        if g:
            ddict[k] = g.ReadAsArray()
    
    # scale it
    lai = ddict['Lai_500m'] * 0.1
    std = ddict['LaiStdDev_500m'] * 0.1
    # doy from filenames
    doy = np.array([int(i.split('-')[1]) for i in bnames])
    if verbose:
        print(f'done')
    return lai,std,doy


def get_weight(lai,std):
    std[std<1] = 1
    weight = np.zeros_like(std)
    mask = (std > 0)
    weight[mask] = 1./(std[mask]**2)
    weight[lai > 10] = 0.

    return weight

# regularise
def regularise(lai,weight,sigma):
    '''
    takes as argument:
    
        lai     : MODIS LAI dataset:     shape (Nt,Nx,Ny)
        weight  : MODIS LAI weight:      shape (Nt,Nx,Ny)
        sigma   : Gaussian filter width: float
        
    returns an array the same shape as 
    lai of regularised LAI. Regularisation takes place along
    axis 0 (the time axis)
    '''
    x = np.arange(-3*sigma,3*sigma+1)
    gaussian = np.exp((-(x/sigma)**2)/2.0)

    numerator = scipy.ndimage.filters.convolve1d(lai * weight, gaussian, axis=0,mode='wrap')
    denominator = scipy.ndimage.filters.convolve1d(weight, gaussian, axis=0,mode='wrap')

    # avoid divide by 0 problems by setting zero values
    # of the denominator to not a number (NaN)
    denominator[denominator==0] = np.nan

    interpolated_lai = numerator/denominator
    # (Nt,Nx,Ny)
    return interpolated_lai


def get_lc(year,tile,fips):
    '''
    Return LC mask for year,tile,fips
    '''
    # SDS for land cover data
    LC_SDS = ['LC_Prop1', 'LC_Prop1_Assessment', 'LC_Prop2', \
              'LC_Prop2_Assessment', 'LC_Prop3', 'LC_Prop3_Assessment', \
              'LC_Type1', 'LC_Type2', 'LC_Type3', 'LC_Type4', 'LC_Type5', 'LW', 'QC']

    warp_args = {
        'dstNodata'     : 255,
        'format'        : 'MEM',
        'cropToCutline' : True,
        'cutlineWhere'  : f"FIPS='{fips}'",
        'cutlineDSName' : 'data/TM_WORLD_BORDERS-0.3.shp'
    }
    # LU

    kwargs = {
        'tile'      :    tile,
        'product'   :    'MCD12Q1',
        'year'      :    year,
        'sds'       : LC_SDS,
        'doys'      :    [1],
        'warp_args' : warp_args
    }

    # get the data
    lcfiles,bnames = modisAnnual(**kwargs)
    
    # get the item we want
    g = gdal.Open(lcfiles['LC_Type3'])
    # error checking
    if not g:
        print(f"cannot open LC file {lcfiles['LC_Type3']}")
        return None
    lc = g.ReadAsArray()
    del g
    
    # in your function, print out the unique values in the 
    # landcover dataset to give some feedback to the user
    print(f"class codes: {np.unique(lc)}")
    return lc

import subprocess
def preamble():
    uid,password = Cylog('https://n5eil01u.ecs.nsidc.org').login()
    cmd = "echo 'machine urs.earthdata.nasa.gov login {uid} password {password}' >> ~/.netrc && chmod 0600 ~/.netrc"
    subprocess.run(cmd.split())
    
def getIndex(url,location):
    cmd = f'cd {location} && wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --keep-session-cookies --no-check-certificate  --auth-no-challenge=on -np -e robots=off {url}'
    subprocess.run(cmd.split())
