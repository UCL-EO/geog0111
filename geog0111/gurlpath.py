#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import yaml
import os
from pathlib import Path
import urlpath

import urllib
from pathlib import _PosixFlavour, PurePath
import collections.abc
import functools
import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
import fnmatch
import numpy as np
import io


try:
  from geog0111.cylog import Cylog
except:
  from cylog import Cylog

'''
class derived from urlpath to provide pathlib-like
interface to url data
'''

__author__    = "P. Lewis"
__email__     = "p.lewis@ucl.ac.uk"
__date__      = "28 Aug 2020"
__copyright__ = "Copyright 2020 P. Lewis"
__license__   = "GPLv3"

class URL(urlpath.URL,urllib.parse._NetlocResultMixinStr, PurePath):
  '''
  Derived from 
  https://raw.githubusercontent.com/chrono-meter/urlpath/master/urlpath.py

  to provide more compatibility with pathlib.Path functionality

  '''

  '''
  modified new and init
  '''
  def __new__(cls,*args,**kwargs):
      self = super(URL, cls).__new__(cls,*args) 
      self.kwargs = dict(kwargs)
      if 'level' not in self.kwargs:
        self.kwargs['level'] = 0
      return self

  def __init__(self,*args,**kwargs):
      # remove any trailing '/' from args
      args = list(args)
      for i,arg in enumerate(args):
        arg = str(arg)
        while arg[-1] == '/':
          if len(arg) == 1:
            break
          arg = arg[:-1]
        args[i] = arg
      args = tuple(args)
      if not kwargs:
        kwargs = {}
      if 'level' in kwargs.keys():
        kwargs['level'] += 1
      else:
        kwargs['level'] = 0
      self._init(**kwargs)

  def _init(self,**kwargs):
      '''kwargs setup'''
      self.verbose    = False
      self.local_dir  = None
      self.local_file = None
      self.noclobber  = True
      self.size_check = True

      # extra arguments
      keys = kwargs.keys()
      if 'verbose' in keys:
        self.verbose = kwargs['verbose']
      if 'noclobber' in keys:
        self.noclobber = kwargs['noclobber']
      if 'size_check' in keys:
        self.size_check = kwargs['size_check']

      # local_dir may be a cache
      if 'CACHE_DIR' in os.environ.keys() and os.environ['CACHE_DIR'] != None:
        self.local_dir = Path(os.environ['CACHE_DIR']).absolute()
        #self.msg(f"cache directory set from $CACHE_DIR : {self.local_dir}")
      if 'local_dir' in keys and kwargs['local_dir'] != None:
        self.local_dir = Path(kwargs['local_dir']).absolute()
        #self.msg(f"cache directory set from cmd line : {self.local_dir}")

      if 'local_file' in keys and kwargs['local_file'] != None:
        self.local_file = Path(kwargs['local_file']).absolute()
        self.msg(f"cache file set from cmd line : {self.local_file}")

      if self.local_file and self.local_dir == None:
        self.local_dir = self.local_file.parent
      # so self.local_dir is either None or a Path

      if self.local_file == None and self.local_dir:
        self.local_file = Path(self.local_dir,self.name)

      if self.local_dir:
        if not self.local_dir.exists():
          self.msg(f"mkdir local dir {self.local_dir}")
          self.local_dir.mkdir(parents=True,exist_ok=True)

  def _local_file(self):

      if self.local_dir:
        self.local_dir = Path(self.local_dir)
        local_file = Path(self.local_dir,self.name) 
        self.local_dir.mkdir(parents=True,exist_ok=True)
      else:
        local_file = self.local_file

      if local_file == None:
        return local_file

      #local_file =  Path(local_file or Path(self.components[2][1:]))
      # dont make it if it doesnt exist
      #if not nomkdir:
      #  self.msg(f"mkdir local dir {local_dir}")
      #  local_dir.mkdir(parents=True,exist_ok=True)

      if local_file.is_dir():
        return None

      if local_file.exists():
        lsize = local_file.stat().st_size
        #self.msg(f"existing file {local_file} {lsize} Bytes")
        self.msg(f'noclobber: {self.noclobber}')
        # delete the file if noclobber is False
        if not self.noclobber:
          self.msg("deleting existing file {local_file}")
          local_file.unlink()
        else:
          self.msg(f"keeping existing file {local_file}")
      
      return local_file

  def open(self,mode='r',buffering=-1, encoding=None, errors=None, newline=None):
      '''
      Open the file pointed by this URL and return a file object, as
      the built-in open() function does.
      '''
      kwargs = {'mode':mode,'buffering':buffering,'encoding':encoding,\
                'errors':errors,'newline':newline}

      if self._isfile():
        self.msg(f'{self} is not a URL: interpreting as Path')
        return Path(self).open(**kwargs)

      binary = ('b' in mode) and ('t' not in mode) 

      local_file = self._local_file()
      get_download = self._test_already_local()

      if not get_download:
        self.msg(f'opening already downloaded file {local_file}')
        return Path(local_file).open(**kwargs)

      self.msg(f'opening stream to {self}:') 

      if 'r' in mode:
        self.msg(f"reading data from {self}")
        # read 
        if binary:
          self.msg("open() binary stream")
          return io.BytesIO(self.read_bytes())
        else:
          self.msg("open() text stream")
          return  io.StringIO(self.read_text())

      # fallback
      self.msg(f'fallback open()')
      self.msg(f'opening already downloaded file {local_file}')
      return Path(local_file).open(**kwargs)

  def write_text(self,data, encoding=None, errors=None):
      '''Open the file in text mode, write to it, and close the file.'''
      kwargs = {'encoding':encoding}
      if self._isfile():
          self.msg(f'{self} is not a URL: interpreting as Path')
          return Path(self).write_text(data)

      local_file = self._local_file()
      get_download = self._test_already_local()

      if not get_download:
        self.msg(f'opening already downloaded file {local_file}')
        return Path(local_file).write_text(data,**kwargs)

      if not local_file.exists():
          kwargs = {'encoding':encoding,'errors':errors}
          self.msg(f"writing data ...")
          retval = local_file.write_text(data,**kwargs)
      else:
          self.msg("file exists so not writing")
          retval = local_file.stat().st_size
      self.msg(f"done : {retval}")
      return retval

  def write_bytes(self,data):
      '''Open the file in bytes mode, write to it, and close the file.'''
      if self._isfile():
          self.msg(f'{self} is not a URL: interpreting as Path')
          return Path(self).write_bytes(data)

      local_file = self._local_file()
      get_download = self._test_already_local()

      if not get_download:
        self.msg(f'opening already downloaded file {local_file}')
        return Path(local_file).write_bytes(data)

      if not local_file.exists():
          self.msg(f"writing data ...")
          retval = local_file.write_bytes(data)
          self.msg(f"done : {retval}")
      else:
          self.msg("file exists so not writing")
          retval = local_file.stat().st_size
      self.msg(f"done : {retval}")
      return retval

  def _get_login(self,head=True):
      u = self.resolve()
      u._init(**(self.kwargs))
      with requests.Session() as session:
        if u.username and u.password:
          session.auth = u.username,u.password
        else:
          uinfo = Cylog(u.anchor).login()
          if uinfo == (None,None):
            return None
          session.auth = uinfo[0].decode('utf-8'),uinfo[1].decode('utf-8')
          u.msg(f'logging in to {u.anchor}')
        try:
          r1 = session.request('get',u)
          if r1.status_code == 200:
            u.msg(f'data read from {u.anchor}')
            return r1
          # try encoded login
          if head:
            r2 = session.head(r1.url)
          else:
            r2 = session.get(r1.url)
          if r2.status_code == 200:
            u.msg(f'data read from {u.anchor}')
          if type(r2) == requests.models.Response:
            return r2
        except:
          u.msg(f'failure reading data from {u.anchor}')
          return None
      u.msg(f'failure reading data from {u.anchor}')
      return None

  def msg(self,*args):
    '''msg to stderr'''
    try:
      # DONT REPEAT MESSAGES
      if args in self.store_msg:
        return
      self.store_msg.append(args)
    except:
      self.store_msg = [args]
    try:
        if self.verbose:
            print('-->',*args,file=sys.stderr)
    except:
        pass

  def _test_already_local(self):
    # get local_filename we would use for output
    # delete it if not noclobber
    # dont greate dir if it doesnt exist
    local_file = self._local_file()
    if local_file:
      self.msg(f'local file: {local_file}')
    else:
      return True
    # local file doesnt exists

    if local_file.is_dir():
      return False

    if not local_file.exists():
      #self.msg(f'local file {local_file} does not exist')
      return True

    # simple if no size check
    if (not self.size_check) and local_file.exists():
      self.msg(f'local file {local_file} exists: no size check')
      return False

    if self.size_check:
      lsize = local_file.stat().st_size
      rsize = self.stat().st_size
      if rsize < 0:
        # then its not available
        self.msg(f'not downloading file')
        # we might not want to download
        return False
      elif lsize == rsize:
        self.msg(f'local and remote file sizes equal {lsize}')
        self.msg(f'not downloading file')
        # we might not want to download
        return False
      self.msg(f'local and remote file sizes not equal {lsize}/{rsize} respectively')
      self.msg(f'so we need to download (or set size_check=False)')
      if not self.noclobber:
        self.msg(f'deleting local file {local_file}')
        local_file.unlink()
    return True


  def read_text(self, encoding=None, errors=None):
    '''Open the URL, read in text mode and return text.'''  

    kwargs = {'encoding':encoding}
    u = self.resolve()
    u._init(**(self.kwargs))
    if u._isfile():
      self.msg(f'{u} is not a URL: interpreting as Path')
      return Path(u).read_text()

    local_file = self._local_file()
    get_download = self._test_already_local()


    if not get_download:
      self.msg(f'opening already downloaded file {local_file}')
      return Path(local_file).read_text(**kwargs)

    try:
      u.msg(f'trying {self}')
      return u.get_text()
    except:
      pass

    u.msg(f'getting login')
    r = u._get_login(head=False)
    if type(r) != requests.models.Response:
      return None
    if r.status_code == 200:
        u.msg(f'code {r.status_code}')
        return r.text
    if type(r) == requests.models.Response:
        u.msg(f'code {r.status_code}')
        return r
    u.msg(f'failed to connect')
    return None

  def exists(self):
    '''Whether this URL exists and can be accessed'''
    return self.ping()

  def stat(self, head=False):
    '''
    Some of the functionality of stat for URLs

    Currently, only stat_result.st_size is used.
    '''
    input = [0,0,0,0,0,0,self._st_size(head=head),0,0,0]
    stat_result = os.stat_result(input)
    return stat_result

  def absolute(self):
    '''resolve'''
    return self.resolve

  def _isfile(self):
    if self.scheme == '' or self.scheme == 'file':
      self.msg('we are a file ...')
      return True
    #self.msg('we are not a file ...')
    return False

  def _st_size(self, head=False):
    '''
    retrieve the remote file size

    You should specify any required login/password with
    with_components(username=str,password=str)

    Returns:
      int if data available
    Or:
      -1
    '''
    u = self.resolve()
    u._init(**(self.kwargs))

    remote_size = -1
    if u._isfile():
      self.msg(f'{u} is not a URL: interpreting as Path')
      # not a URL
      u = Path(u)
      return u.stat().st_size
    try:
      u.msg(f'trying {u}')
      if head:
        r = u.head()
      else:
        r = u.get()
      if type(r) == requests.models.Response:
        if r.status_code == 200:
          u.msg(f'code 200')
          hdr = r.headers
          if "Content-Length" in hdr.keys():
              remote_size = int(hdr["Content-Length"])
          elif 'Transfer-Encoding' in hdr.keys() and hdr["Transfer-Encoding"] == 'chunked':
              u.msg(f'file is compressed, remote size not directly available')
          #self.msg(hdr)
          if remote_size > 0:
            return(remote_size)

        # 
        if r.status_code == 401:
          u.msg(f'code 401')
          # unauthorised
          # more complex session login and auth
          # e.g. needed for NASA Earthdata login
          u.msg(f'getting login')
          r = u._get_login(head=head)
          if r.status_code == 200:
            u.msg(f'code 200')
            hdr = r.headers
            if "Content-Length" in hdr:
              remote_size = int(hdr["Content-Length"])
            if remote_size > 0:
              return(remote_size)
        elif head == False:
          u.msg(f'code {r.status_code}')
          return remote_size
        # return it even if 0
        return remote_size
    except:
      pass
    if head == False:
      u.msg(f'failed to connect')
      return remote_size
    u.msg(f'trying get')
    return u.st_size(head=False)

  def ping(self, head=True):
    '''
    ping the URL data return True if response is 200

    You should specify any required login/password with
    with_components(username=str,password=str)

    Returns:
      True if data available
    Or:
      False
    '''
    u = self.resolve()
    u._init(**(self.kwargs))
    if u._isfile():
      self.msg(f'{u} is not a URL: interpreting as Path')
      # not a URL
      u = Path(u)
      return u.exists()
    try:
      u.msg(f'trying {u}')
      if head:
        r = u.head()
      else:
        r = u.get()
      if type(r) == requests.models.Response:
        if r.status_code == 200:
          u.msg(f'code 200')
          return True
        if r.status_code == 401:
          u.msg(f'code 401')
          u.msg(f'trying another')
          # unauthorised
          # more complex session login and auth
          # e.g. needed for NASA Earthdata login
          u.msg(f'getting login')
          r = u._get_login(head=head)
          if r.status_code == 200:
            u.msg(f'code 200')
            return True
        elif head == False:
          u.msg(f'code {r.status_code}')
          return False
    except:
      pass
    if head == False:
      u.msg(f'failed to connect')
      return False
    u.msg(f'trying get')
    return u.ping(head=False)

  def read_bytes(self):
    '''
    Open the URL data in bytes mode, read it and return the data

    This first tried self.get() but if the authorisation is more complex
    (e.g. when using NASA server) then a fuller 2-pass session
    is used.

    You should specify any required login/password with 
    with_components(username=str,password=str) 

    Returns:
      data from url
    Or:
      None                     : on failure 
      requests.models.Response : on connection problem
    '''
    u = self.resolve()
    u._init(**(self.kwargs))

    if u._isfile():
      self.msg(f'{u} is not a URL: interpreting as Path')
      return Path(u).read_bytes()

    local_file = self._local_file()
    get_download = self._test_already_local()

    if not get_download:
      self.msg(f'opening already downloaded file {local_file}')
      return Path(local_file).read_bytes()

    try:
      u.msg(f'trying {u}')
      r = u.get()
      if type(r) == requests.models.Response:
        if r.status_code == 200:
          u.msg(f'code {r.status_code}')
          return r.content
        if r.status_code == 401:
          u.msg(f'code {r.status_code}')
          u.msg(f'trying another')
          # unauthorised
          # more complex session login and auth
          # e.g. needed for NASA Earthdata login
          u.msg(f'getting login')
          r = u._get_login(head=False)
          if type(r) != requests.models.Response:
            return None
          if r.status_code == 200:
            u.msg(f'code {r.status_code}')
            return r.content
        else:
          u.msg(f'code {r.status_code}')
          return r
    except:
      pass

    u.msg(f'failed to connect')
    return None 


  def _convert_to_abs(self,ilist):
    # this url
    this = str(self.resolve())
    olist = []
    for l in ilist:
      if URL(l,**(self.kwargs)).hostname:
        pass
      else:
        try:
          # trim
          while len(l) > 1 and l[-1] == '/':
            l = l[:-1]
          if l not in ['about', '/','#'] and l[0] not in ['/','#']:
            olist.append(str(URL(this,l,**(self.kwargs)).resolve()))
        except:
          pass
    return olist

  def _filter(self,list,pattern):
    list = self._convert_to_abs(list)
    olist = []
    try:
      p = self.done[pattern]
    except:
      try:
        self.done[pattern] = []
        
      except:
        self.done = {pattern:[]}
    p = self.done[pattern]
    
    olist = [u for u in list if u not in p]    
    self.done[pattern] = self.done[pattern] + olist
    return olist

  def glob(self,pattern):
    '''
    Iterate over this subtree and yield all existing files (of any
    kind, including directories) matching the given relative pattern.

    The URL here then needs to return lxml html code.

    Positional arguments:
       patterm  : to search for e.g. */2021.*.01
                  only wildcards * and ? considered at present

    '''
    u = self.resolve()
    u._init(**(self.kwargs))
    url = str(u)
    if url[-1] == '/':
      url = urls[:-1]
    url = URL(url,pattern,**(self.kwargs))
    uc = np.array(url.parts)
    is_wild   = np.logical_or(np.array(['*' in i for i in uc]),
                              np.array(['?' in i for i in uc]))
    is_wild_2 = np.logical_or(np.array(['[' in i for i in uc]),
                              np.array([']' in i for i in uc]))
    is_wild = np.logical_or(is_wild,is_wild_2)
    first_wild = np.where(np.cumsum(is_wild)>0)[0][0]
    base_list = [str(URL(*list(uc[:first_wild]),**(self.kwargs)).resolve())]
    wilds = uc[first_wild:]
    u.msg(f'wildcards in: {wilds}')
    for i,w in enumerate(wilds):
      u.msg(f'level {i}/{len(wilds)} : {w}')
      new_list = []
      for b in base_list:
        new_list = new_list + URL(b,**(self.kwargs))._glob(w)
      base_list = np.array(new_list).flatten()
    olist = list(np.array([URL(i,**(self.kwargs)) for i in base_list]).flatten())
    for l in olist:
      l._init(**(self.kwargs))
    return olist

  def rglob(self, pattern):
    '''
    Recursively yield all existing files (of any kind, including
    directories) matching the given relative pattern, anywhere in
    this subtree.

    Positional arguments:
       patterm  : to search for e.g. 2021.*.01
                  only wildcards * and ? considered at present


    '''
    u = self.resolve()
    u._init(**(self.kwargs))
    return u.glob(pattern)


  def _glob(self, pattern):
    '''
    Iterate over this subtree and yield all existing files (of any
    kind, including directories) matching the given relative pattern.

    The URL here then needs to return lxml html code.
    '''
    # take off training slash
    if pattern[-1] == '/':
      pattern = pattern[:-1]

    try:
      html = self.read_text()
      links = np.array([mylink.attrs['href'] for mylink in BeautifulSoup(html,'lxml').find_all('a')])
      links = np.array(self._filter(links,pattern))

      matches = np.array([fnmatch.fnmatch(str(l), '*'+pattern) for l in links]) 
      files = list(links[matches])
    except:
      files = []
    self.msg(f'discovered {len(files)} files with pattern {pattern} in {str(self.resolve())}')
    return files 

def main():
  if False:
    u='https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h09v06.006.2015084002115.hdf'
    url = URL(u)
    data = url.read_bytes()
    ofile = Path('data',url.name)
    osize = ofile.write_bytes(data)
    assert osize == 3365255
    print('passed')

  if False:
    u='https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11'
    url = URL(u)
    files = url.glob('*0.hdf') 
    print(files) 

  if True:
    u='https://e4ftl01.cr.usgs.gov'
    url = URL(u,verbose=True)
    import os
    os.environ['CACHE_DIR'] = '/tmp/modis'
    rlist = url.glob('MOT*/MCD15A3H.006/2003.12.*/*0.hdf')
    print(rlist)
 
if __name__ == "__main__":
    main()

