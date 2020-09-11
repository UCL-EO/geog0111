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

  def _get_login(self,verbose=False):
      u = self.resolve()
      with requests.Session() as session:
        if self.username and self.password:
          session.auth = self.username,self.password
        else:
          uinfo = Cylog(self.anchor).login()
          session.auth = uinfo[0].decode('utf-8'),uinfo[1].decode('utf-8')
          if verbose:
            print(f'--> logging in to {self.anchor}')
        try:
          r1 = session.request('get',u)
          if r1.status_code == 200:
            if verbose:
              print(f'--> data read from {self.anchor}')
            return r1
          # try encoded login
          r2 = session.get(r1.url)
          if r2.status_code == 200 and verbose:
            print(f'--> data read from {self.anchor}')
          if type(r2) == requests.models.Response:
            return r2
        except:
          if verbose:
              print(f'--> failure reading data from {self.anchor}')
          return None
      if verbose:
          print(f'--> failure reading data from {self.anchor}')
      return None

  def read_text(self, encoding=None, errors=None, verbose=False):
    '''Open the URL, read in text mode and return text.'''  
    try:
        return self.get_text()
    except:
      pass

    r = self._get_login(verbose=verbose)
    if r.status_code == 200:
        return r.text
    return r


  def read_bytes(self, login=False,verbose=False):
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
    try:
      r = self.get()
      if type(r) == requests.models.Response:
        if r.status_code == 200:
          return r.content
        if r.status_code == 401:
          # unauthorised
          # more complex session login and auth
          # e.g. needed for NASA Earthdata login
          r = self._get_login(verbose=verbose)
          if r.status_code == 200:
            return r.content
        else:
          return r
    except:
      pass

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
    url = str(self.resolve())
    if url[-1] == '/':
      url = urls[:-1]
    url = URL(self,pattern)
    uc = np.array(url.parts)
    is_wild = np.logical_or(np.array(['*' in i for i in uc]),
                            np.array(['?' in i for i in uc]))
    first_wild = np.where(np.cumsum(is_wild)>0)[0][0]
    base_list = [str(URL(*list(uc[:first_wild])).resolve())]
    wilds = uc[first_wild:]
    if verbose:
      print(f'wildcards in: {wilds}')
    for i,w in enumerate(wilds):
      if verbose:
        print(f'----> level {i}/{len(wilds)} : {w}')
      new_list = []
      for b in base_list:
        new_list = new_list + URL(b)._glob(w,verbose=True)
      base_list = new_list
    yield [URL(i) for i in base_list]  

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
    return self.rglob(pattern, verbose=verbose)


  def _glob(self, pattern, verbose=False):
    '''
    Iterate over this subtree and yield all existing files (of any
    kind, including directories) matching the given relative pattern.

    The URL here then needs to return lxml html code.
    '''

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
    if verbose:
      print(f'--> discovered {len(files)} files with pattern {pattern} in {str(self.resolve())}')
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

