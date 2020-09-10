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
  def read_text(self, encoding=None, errors=None):
    '''Open the URL, read in text mode and return text.'''  
    return self.get_text(self)

  def read_bytes(self):
    '''
    Open the URL data in bytes mode, read it and return the data

    This first tried self.get() but if the authorisation is more complex
    (e.g. when using NASA server) then a fuller 2-pass session
    is used.

    You should speciufy any required login/password with 
    with_components(username=str,password=str) 

    Returns:
      data fromn url
    Or:
      None                     : on failure 
      requests.models.Response : on connection problem
    '''
    try:
      r = self.get()
      if type(r) == requests.models.Response:
        if r.status_code == 200:
          return r.content
    except:
      pass
    # more complex session login and auth
    # e.g. needed for NASA Earthdata login

    uinfo = Cylog(self.anchor).login()
    auth = self.with_components(username=uinfo[0].decode('utf-8'),password=uinfo[1].decode('utf-8'))

    with requests.Session() as session:
      try:
        # get username and password for auth
        session.auth = (auth.username,auth.password)
        r1 = session.request('get',str(auth.resolve()))  
        r2 = session.get(r1.url)
        if type(r2) == requests.models.Response:
           if r2.status_code == 200:
             return r2.content
           else:
             return r2
      except:
        return None
    return None 
 

  def glob(self, pattern):
    '''
    Iterate over this subtree and yield all existing files (of any
    kind, including directories) matching the given relative pattern.
    '''


def main():
  u='https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h09v06.006.2015084002115.hdf'
  x = URL(u)
  data = x.read_bytes()
  import pdb;pdb.set_trace()
  print(data) 
 
if __name__ == "__main__":
    main()

