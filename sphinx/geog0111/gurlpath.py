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

  def _local_file(self,local_file=None,verbose=False,local_dir=None,nomkdir=True,noclobber=True):
      self.verbose = verbose
      try:
        local_dir = local_dir or self.local_dir
      except:
        local_dir = local_dir
      try:
        local_file = local_file or self.local_file
      except:
        local_file = local_file


      if local_dir:
        local_file = Path(local_dir,self.name) 
      local_file =  Path(local_file or Path(self.components[2][1:]))
      #self.msg(f"local file {local_file}")
      if local_file.exists():
        lsize = local_file.stat().st_size
        self.msg(f"existing file {local_file} {lsize} Bytes")
        self.msg(f'noclobber: {noclobber}')
        # delete the file if noclobber is False
        if not noclobber:
          self.msg("deleting existing file {local_file}")
          local_file.unlink()
        else:
          self.msg(f"keeping existing file {local_file}")
      #self.msg(f"possible local file {local_file}")
      local_dir = local_file.parent
      # dont make it if it doesnt exist
      if not nomkdir:
        self.msg(f"mkdir local dir {local_dir}")
        local_dir.mkdir(parents=True,exist_ok=True)
      
      return local_file

  def open(self,mode='r',cache=False, buffering=-1, encoding=None, errors=None, newline=None,\
                size_check=True,local_dir=None,verbose=False,noclobber=True,local_file=None):
      '''
      Open the file pointed by this URL and return a file object, as
      the built-in open() function does.
      '''
      # append, so dont clobber
      if '+' in mode or 'a' in mode:
        noclobber=True
      self.verbose = verbose
      kwargs = {'mode':mode,'buffering':buffering,'encoding':encoding,\
                'errors':errors,'newline':newline}

      if self._isfile():
        self.msg(f'{self} is not a URL: interpreting as Path')
        return Path(self).open(**kwargs)

      binary = ('b' in mode) and ('t' not in mode) 

      get_download = True
      if cache:
        get_download = self._test_already_local(verbose=verbose,size_check=size_check,\
             local_file=local_file,local_dir=local_dir,noclobber=noclobber)

      if not get_download:
        self.msg(f'opening already downloaded file')
        return Path(self._local_file(verbose=verbose,\
             local_file=local_file,local_dir=local_dir,\
             size_check=True,noclobber=noclobber)).open(**kwargs)

      self.msg(f'opening stream to {self}:') 

      if 'r' in mode:
        self.msg(f"reading data from {self}")
        # cache ?
         
        # read 
        if binary:
          self.msg("open() binary stream")
          return io.BytesIO(self.read_bytes())
        else:
          self.msg("open() text stream")
          return  io.StringIO(self.read_text())
      # if we are here, then we probably 
      # want a real file for writing or whatever
      local_file = self._local_file(verbose=verbose,local_dir=local_dir,local_file=local_file,noclobber=noclobber)  

      self.msg(f"opening file ...")
      return local_file.open(**kwargs)

  def write_text(self,data, encoding=None, errors=None,size_check=True,
                      local_dir=None,verbose=False,noclobber=True,local_file=None):
      '''Open the file in text mode, write to it, and close the file.'''
      self.verbose = verbose 
      kwargs = {'encoding':encoding}
      if self._isfile():
          self.msg(f'{self} is not a URL: interpreting as Path')
          return Path(self).write_text(data)

      #self.msg(f'{self}')
      get_download = self._test_already_local(verbose=verbose,size_check=size_check,\
             local_file=local_file,local_dir=local_dir,noclobber=noclobber)

      self.msg(f'get download? {get_download}')
      if not get_download:
        self.msg(f'opening already downloaded file')
        return Path(self._local_file(verbose=verbose,\
             local_file=local_file,local_dir=local_dir,\
             noclobber=noclobber)).write_text(data,**kwargs)

      local_file = self._local_file(verbose=verbose,local_dir=local_dir,local_file=local_file,noclobber=noclobber)   

      if not local_file.exists():
          kwargs = {'encoding':encoding,'errors':errors}
          self.msg(f"writing data ...")
          retval = local_file.write_text(data,**kwargs)
      else:
          self.msg("file exists so not writing")
          retval = local_file.stat().st_size
      self.msg(f"done : {retval}")
      return retval

  def write_bytes(self,data,verbose=False,size_check=True,
                       local_dir=None,noclobber=True,local_file=None):
      '''Open the file in bytes mode, write to it, and close the file.'''
      self.verbose = verbose   
      if self._isfile():
          self.msg(f'{self} is not a URL: interpreting as Path')
          return Path(self).write_text(data)

      get_download = self._test_already_local(verbose=verbose,size_check=size_check,\
             local_file=local_file,local_dir=local_dir,noclobber=noclobber)

      if not get_download:
        self.msg(f'opening already downloaded file')
        return Path(self._local_file(verbose=verbose,\
             local_file=local_file,local_dir=local_dir,\
             noclobber=noclobber)).write_bytes(data)

      local_file = self._local_file(verbose=verbose,local_dir=local_dir,local_file=local_file,noclobber=noclobber)   
      if not local_file.exists():
          self.msg(f"writing data ...")
          retval = local_file.write_bytes(data)
          self.msg(f"done : {retval}")
      else:
          self.msg("file exists so not writing")
          retval = local_file.stat().st_size
      self.msg(f"done : {retval}")
      return retval

  def _get_login(self,head=True,verbose=False):
      u = self.resolve()
      u.verbose = verbose
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
        if self.verbose:
            print('-->',*args,file=sys.stderr)
    except:
        pass

  def _test_already_local(self,verbose=False,size_check=True,\
             local_file=None,local_dir=None,noclobber=True):
    # get local_filename we would use for output
    # delete it if not noclobber
    # dont greate dir if it doesnt exist
    self.verbose = verbose
    local_file = self._local_file(local_file=local_file,verbose=verbose,\
             nomkdir=True,local_dir=local_dir,noclobber=noclobber)
    self.msg(f'local file: {local_file}')

    if not local_file:
      return True
    # local file doesnt exists
    if not local_file.exists():
      self.msg(f'local file {local_file} does not exist')
      return True

    # simple if no size check
    if (not size_check) and local_file.exists():
      self.msg(f'local file {local_file} exists: no size check')
      return False


    if size_check:
      lsize = local_file.stat().st_size
      rsize = self.stat(verbose=verbose).st_size
      if rsize < 0:
        # then its not available
        self.msg(f'noclobber: {noclobber}')
        self.msg(f'not downloading file')
        # we might not want to download
        return False
      elif lsize == rsize:
        self.msg(f'local and remote file sizes equal {lsize}')
        self.msg(f'noclobber: {noclobber}')
        self.msg(f'not downloading file')
        # we might not want to download
        return False
      self.msg(f'local and remote file sizes not equal {lsize}/{rsize} respectively')
      self.msg(f'so we need to download (or set size_check=False)')
      if not noclobber:
        self.msg(f'deleting local file {local_file}')
        local_file.unlink()
    return True

  def read_text(self, encoding=None, errors=None,noclobber=True,
                      size_check=True,local_file=None,local_dir=None,verbose=False):
    '''Open the URL, read in text mode and return text.'''  
    self.verbose = verbose   
    u = self.resolve()
    if u._isfile():
      self.msg(f'{u} is not a URL: interpreting as Path')
      return Path(u).read_text()
    u.verbose = verbose

    get_download = self._test_already_local(verbose=verbose,size_check=size_check,\
           local_file=local_file,local_dir=local_dir,noclobber=noclobber)

    if not get_download:
      self.msg(f'opening already downloaded file')
      return Path(self._local_file(verbose=verbose,\
             local_file=local_file,local_dir=local_dir,\
             noclobber=noclobber)).read_text()

    try:
      u.msg(f'trying {self}')
      return u.get_text()
    except:
      pass

    u.msg(f'getting login')
    r = u._get_login(head=False,verbose=verbose)
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

  def exists(self, verbose=False):
    '''Whether this URL exists and can be accessed'''
    self.verbose =verbose
    return self.ping(verbose=verbose)

  def stat(self, head=False,verbose=False):
    '''
    Some of the functionality of stat for URLs

    Currently, only stat_result.st_size is used.
    '''
    self.verbose=verbose
    input = [0,0,0,0,0,0,self._st_size(head=head,verbose=verbose),0,0,0]
    stat_result = os.stat_result(input)
    return stat_result

  def absolute(self):
    '''resolve'''
    return self.resolve

  def _isfile(self):
    #self.msg('testing to see if we are a local file')
    if self.scheme == '' or self.scheme == 'file':
      self.msg('we are a file ...')
      return True
    #self.msg('we are not a file ...')
    return False

  def _st_size(self, head=False,verbose=False):
    '''
    retrieve the remote file size

    You should specify any required login/password with
    with_components(username=str,password=str)

    Returns:
      int if data available
    Or:
      -1
    '''
    self.verbose=verbose
    u = self.resolve()
    u.verbose = verbose
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
          r = u._get_login(head=head,verbose=verbose)
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
    return u.st_size(head=False,verbose=verbose)

  def ping(self, head=True,verbose=False):
    '''
    ping the URL data return True if response is 200

    You should specify any required login/password with
    with_components(username=str,password=str)

    Returns:
      True if data available
    Or:
      False
    '''
    self.verbose=verbose
    u = self.resolve()
    u.verbose = verbose
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
          r = u._get_login(head=head,verbose=verbose)
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
    return u.ping(head=False,verbose=verbose)

  def read_bytes(self, local_file=None,size_check=True,local_dir=None,noclobber=True,verbose=False):
    '''
    Open the URL data in bytes mode, read it and return the data

    This first tried self.get() but if the authorisation is more complex
    (e.g. when using NASA server) then a fuller 2-pass session
    is used.

    You should speciufy any required login/password with 
    with_components(username=str,password=str) 

    Returns:
      data from url
    Or:
      None                     : on failure 
      requests.models.Response : on connection problem
    '''
    self.verbose = verbose   
    u = self.resolve()
    u.verbose = verbose
    if u._isfile():
      self.msg(f'{u} is not a URL: interpreting as Path')
      return Path(u).read_bytes()

    get_download = self._test_already_local(verbose=verbose,size_check=size_check,\
           local_file=local_file,local_dir=local_dir,noclobber=noclobber)

    if not get_download:
      self.msg(f'opening already downloaded file')
      return Path(self._local_file(verbose=verbose,\
             local_file=local_file,local_dir=local_dir,\
             noclobber=noclobber)).read_bytes()

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
          r = u._get_login(head=False,verbose=verbose)
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


  def _convert_to_abs(self,list):
    # this url
    this = str(self.resolve())
    olist = []
    for l in list:
      if URL(l).hostname:
        pass
        # ignore absolutes
        #olist.append(str(URL(l).resolve()))
      else:
        if l not in ['about', '/','#'] and l[0] not in ['/','#']:
          olist.append(str(URL(this,l).resolve()))
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

  def glob(self,pattern, verbose=False):
    '''
    Iterate over this subtree and yield all existing files (of any
    kind, including directories) matching the given relative pattern.

    The URL here then needs to return lxml html code.

    Positional arguments:
       patterm  : to search for e.g. */2021.*.01
                  only wildcards * and ? considered at present

    Keyword arguments:
       verbose=False   : verbose feedback
 
    '''
    self.verbose = verbose   
    u = self.resolve()
    u.verbose = verbose
    url = str(u)
    if url[-1] == '/':
      url = urls[:-1]
    url = URL(url,pattern)
    uc = np.array(url.parts)
    is_wild   = np.logical_or(np.array(['*' in i for i in uc]),
                              np.array(['?' in i for i in uc]))
    is_wild_2 = np.logical_or(np.array(['[' in i for i in uc]),
                              np.array([']' in i for i in uc]))
    is_wild = np.logical_or(is_wild,is_wild_2)
    first_wild = np.where(np.cumsum(is_wild)>0)[0][0]
    base_list = [str(URL(*list(uc[:first_wild])).resolve())]
    wilds = uc[first_wild:]
    u.msg(f'wildcards in: {wilds}')
    for i,w in enumerate(wilds):
      u.msg(f'level {i}/{len(wilds)} : {w}')
      new_list = []
      for b in base_list:
        new_list = new_list + URL(b)._glob(w,verbose=verbose)
      base_list = np.array(new_list).flatten()
    olist = list(np.array([URL(i) for i in base_list]).flatten())
    for l in olist:
      l.verbose = self.verbose
    return olist

  def rglob(self, pattern, verbose=False):
    '''
    Recursively yield all existing files (of any kind, including
    directories) matching the given relative pattern, anywhere in
    this subtree.

    Positional arguments:
       patterm  : to search for e.g. 2021.*.01
                  only wildcards * and ? considered at present

    Keyword arguments:
       verbose=False   : verbose feedback

    '''
    self.verbose = verbose
    u = self.resolve()
    u.verbose = verbose
    return u.rglob(pattern, verbose=verbose)


  def _glob(self, pattern, verbose=False):
    '''
    Iterate over this subtree and yield all existing files (of any
    kind, including directories) matching the given relative pattern.

    The URL here then needs to return lxml html code.
    '''
    self.verbose = verbose
    # take off training slash
    if pattern[-1] == '/':
      pattern = pattern[:-1]

    try:
      html = self.read_text(verbose=verbose)
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
    files = url.glob('*0.hdf',verbose=True) 
    print(files) 

  if True:
    u='https://e4ftl01.cr.usgs.gov'
    url = URL(u)
    rlist = url.glob('MOT*/MCD15A3H.006/2003.12.*/*0.hdf',verbose=True)
    print(rlist)
 
if __name__ == "__main__":
    main()

