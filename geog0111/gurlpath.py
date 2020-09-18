#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import yaml
import os
import urlpath
import stat

import urllib
from pathlib import PosixPath, _PosixFlavour, PurePath
from pathlib import Path

import collections.abc
import functools
import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
import fnmatch
import numpy as np
import io
import tempfile


try:
  from geog0111.cylog import Cylog
  from geog0111.database import Database
except:
  from cylog import Cylog
  from database import Database

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
      self.init(**kwargs)
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

  def __del__(self):
      try:
        del self.database
      except:
        pass

  def __exit__(self, exc_type, exc_value, traceback):
      '''cleanup'''
      try:
        del self.database
      except:
        pass
      tempfile.clean()

  def list_resolve(self,filelist,files=False):
      '''resolve filelist'''
      if (filelist is None) or (filelist == []):
        return []

      if type(filelist) is list:
        filelist = [str(f) for f in filelist if f]
      elif type(filelist) is  str:
        filelist = [filelist]
      elif type(filelist) is PosixPath:
        filelist = [str(filelist)]

      filelist  = self.remove_duplicates(filelist)

      filelist = [Path(f).expanduser().absolute().resolve() for f in filelist]
      return filelist

  def name_resolve(self,filelist,name=None):
      '''resolve filename into filelist'''

      if filelist is None:
        return filelist
      if name == None:
        name = self.name
      filelist = self.list_resolve(filelist)

      for i,f in enumerate(filelist):
        # needs to be dir
        #f = Path(f).expanduser().absolute().resolve()

        # in case its a dir accidently
        if f.exists() and f.is_dir():
          self.msg(f"filename {f} is a directory ...")
          f = Path(f,name)
          self.msg(f"using {f}")

        parent = f.parent
        if parent.exists() and (not parent.is_dir()):
          try:
            self.msg(f'requested file name {f} parent directory {parent} is file: deleting')
            parent.unlink()
          except:
            self.msg(f'failed to deal with file name {f} parent directory {parent} being file: check permissions')
            sys.exit(1)
        try:
          parent.mkdir(parents=True,exist_ok=True)
        except:
          pass
        filelist[i]  = f
      return filelist

  def list_info(self,filelist):
      '''resolve filelist and get read and write permissions'''
      if filelist is None:
        return None,None

      filelist  = np.array(self.list_resolve(filelist,files=True),dtype=np.object)
      readlist  = np.zeros_like(filelist).astype(np.bool)
      writelist = np.zeros_like(filelist).astype(np.bool)

      # get permissions
      for i,f in enumerate(filelist):
        f = Path(f)
        if f.exists() and (not f.is_dir()):
          st_mode = f.stat().st_mode
          readlist[i]  = bool((st_mode & stat.S_IRUSR) /stat.S_IRUSR )
          writelist[i] = bool((st_mode & stat.S_IWUSR) /stat.S_IWUSR )
        else:
          writelist[i] = True
      return list(readlist),list(writelist) 

  def call_local(self):
    '''sort out and return local_file'''
    kwargs = self.kwargs
    if 'local_dir' in kwargs and \
        (kwargs['local_dir'] is not None) and \
        len(kwargs['local_dir']) > 0:
      self.local_dir = self.list_resolve(kwargs['local_dir'])

    if 'local_file' in kwargs and kwargs['local_file'] is not None:
      self.local_file = self.list_resolve(kwargs['local_file'],files=True)

    if (self.local_dir is None) or (len(self.local_dir) == 0):
      self.local_dir = self.list_resolve(self.db_dir)

    is_good_name = (self.name != '') and (not self.has_wildness([self.name])[0])

    if (self.local_file == None) and is_good_name:
      if len(self.local_dir):
        self.local_file = self.name_resolve(self.local_dir,self.name)
    elif self.local_file:
      self.local_file = self.name_resolve(self.local_file)
    return self.local_file

  def remove_duplicates(self,l):
      '''remove duplicates in list l'''
      if l is None:
        return l
      if len(l) == 0:
        return l
      return list(np.unique(np.array(l,dtype=np.object)).flatten())

  def init(self,**kwargs):
      '''
      kwargs setup and organisation of local_dir
      and db_dir

      '''
      if 'verbose' not in kwargs:
        self.verbose         = False
      if ('local_dir' not in kwargs):
        self.local_dir       = self.list_resolve([])
      if 'db_dir' not in kwargs:
        self.db_dir          = self.list_resolve([])
      if 'local_file' not in kwargs:
        self.local_file      = None
      if 'noclobber' not in kwargs:
        self.noclobber       = True
      if 'size_check' not in kwargs:
        self.size_check      = False
      if 'db_file' not in kwargs:
        self.db_file         = None
      if 'store_msg'  not in kwargs:
        self.store_msg       = []
      if 'log'        not in kwargs:
        self.log             = None
      if 'database'         not in kwargs:
        self.database        = None

      self.stderr  = sys.stderr

      try:
        if self.store_msg is None:
          self.store_msg = []
      except:
        self.store_msg = []

      # extra arguments
      keys = kwargs.keys()
      if 'verbose' in keys:
        self.verbose = kwargs['verbose']
      if 'noclobber' in keys:
        self.noclobber = kwargs['noclobber']
      if 'size_check' in keys:
        self.size_check = kwargs['size_check']
      if 'store_msg' in keys:
        self.store_msg = self.store_msg.append(kwargs['store_msg'])
      if 'log' in keys and (kwargs['log'] is not None):
        self.log = kwargs['log'] 
      if 'database' in keys and (kwargs['database'] is not None):
        self.database = kwargs['database']

      self.store_msg = self.remove_duplicates(self.store_msg)
      if self.log is not None:
        try:
          self.stderr = Path(self.log).open("a")
          if self.verbose:
            try:
              msg = f"{str(self)}: log file {self.log}"
              self.store_msg.append(msg)
              print(msg,file=sys.stderr)
            except:
              pass
        except:
          self.stderr = sys.stderr
          self.msg(f"WARNING: failure to open log file {self.log}")

      
      if 'local_dir' in keys and (kwargs['local_dir'] is not None):
        try:
          self.local_dir = self.list_resolve(self.local_dir + self.list_resolve(kwargs['local_dir']))
        except:
          self.local_dir = self.list_resolve(kwargs['local_dir'])
        [d.mkdir(parents=True,exist_ok=True) for d in self.local_dir]
      if 'local_file' in keys and (kwargs['local_file'] is not None):
        self.local_file = self.name_resolve(kwargs['local_file'])

      # update arg list for new creations
      kwargs['verbose']    = self.verbose
      kwargs['local_dir']  = self.local_dir 
      kwargs['local_file'] = self.name_resolve(self.local_file)
      kwargs['noclobber']  = self.noclobber
      kwargs['size_check'] = self.size_check
      kwargs['db_dir']     = self.db_dir

      import pdb;pdb.set_trace()

      try:
        kwargs['db_file']  = self.name_resolve(self.db_file,name='.db.yml')
      except:
        kwargs['db_file']  = None
      kwargs['store_msg']  = self.store_msg
      kwargs['log']        = self.log
      kwargs['database']   = self.database
      
      try:
        self.kwargs.update(kwargs)
      except:
        self.kwargs = kwargs

      import pdb;pdb.set_trace()
      self.db_file = self.kwargs['db_file'] 
      self.database = Database(self.db_file,**kwarg)


  def get_read_file(self,filelist):
    filelist = self.name_resolve(filelist)
    readlist,writelist = self.list_info(filelist)
    filelist = np.array(filelist,dtype=np.object)[readlist]
    return (filelist.size and filelist[-1]) or None

  def get_write_file(self,filelist):
    filelist = self.name_resolve(filelist)
    readlist,writelist = self.list_info(filelist)
    filelist = np.array(filelist,dtype=np.object)[writelist]
    return (filelist.size and filelist[-1]) or None

  def get_readwrite_file(self,filelist):
    filelist = self.name_resolve(filelist)
    readlist,writelist = self.list_info(filelist)
    filelist = np.array(filelist,dtype=np.object)[np.logical_and(np.array(writelist),np.array(readlist))]
    return (filelist.size and filelist[-1]) or None

  def _local_file(self,mode="r"):
    '''get local file name'''
    self.call_local()
    # clobber
    if not self.noclobber:
      local_file  = self.get_readwrite_file(self.local_file)
      # file name for writing
    elif mode == "r":
      local_file = self.get_read_file(self.local_file)
      if local_file and not local_file.exists():
        self.msg("read file {local_file} doesnt exist")
        self.local_file = self.local_file[self.local_file != local_file]
        return self._local_file(mode="r")
    else:
      # file name for writing
      local_file = self.get_write_file(self.local_file)

    if local_file == None:
      return local_file

    # local_file is real
    if local_file.exists():
      if local_file.is_dir():
        try:
          local_file.rmdir()
          return None
        except:
          pass

      #self.msg(f'noclobber: {self.noclobber}')
      # delete the file if noclobber is False
      if not self.noclobber:
        try:
          self.msg(f"deleting existing file {local_file}")
          local_file.unlink()
        except:
          pass
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

      # check in database
      store_url  = str(self)
      store_flag = 'data'

      binary = ('b' in mode) and ('t' not in mode) 

      get_download,ifile,ofile = self._test_already_local()

      # get from ofile
      if ofile and Path(ofile).exists():
        ofile = Path(ofile)
        if binary:
          data = io.BytesIO(ofile.read_bytes())
        else:
          data = io.StringIO(ofile.read_text())
        cache = {store_flag : { str(store_url) : str(ofile) }}
        self.set_db(cache)
        return data

      # get from ifile
      if ifile and Path(ifile).exists():
        ifile = Path(ifile)
        if binary:
          data = io.BytesIO(ifile.read_bytes())
        else:
          data = io.StringIO(ifile.read_text())
        ifile.parent.mkdir(parents=True,exist_ok=True)
        if ofile:
          ofile = Path(ofile)
          if binary:
            ofile.write_bytes(data)
          else:
            ofile.write_text(data)
        cache = {store_flag : { str(store_url) : str(ifile) }}
        self.set_db(cache)
        return data

      if 'r' in mode:
        self.msg(f"reading data from {self}")
        # read 
        if binary:
          self.msg("open() binary stream")
          idata = self.read_bytes()
          data = io.BytesIO(idata)
        else:
          self.msg("open() text stream")
          idata = self.read_text()
          data = io.StringIO(idata)
        if ofile:
          try:
            ofile = Path(ofile)
            if binary:
              ofile.write_bytes(idata)
            else:
              ofile.write_text(idata)
            cache = {store_flag : { str(store_url) : str(ifile) }}
            self.set_db(cache)
          except:
            pass
        return data

      if ofile:
        return Path(ofile).open(**kwargs)

  def write_text(self,data, encoding=None, errors=None):
      '''Open the file in text mode, write to it, and close the file.'''
      kwargs = {'encoding':encoding}
      if self._isfile():
          self.msg(f'{self} is not a URL: interpreting as Path')
          return Path(self).write_text(data)

      get_download,ifile,ofile = self._test_already_local()

      if ofile and Path(ofile).exists():
         self.msg("file exists so not writing")
         return Path(ofile).stat().st_size

      if ofile:
        self.msg(f'opening output file {ofile}')
        return Path(ofile).write_text(data,**kwargs)

  def write_bytes(self,data):
      '''Open the file in bytes mode, write to it, and close the file.'''

      if self._isfile():
          self.msg(f'{self} is not a URL: interpreting as Path')
          return Path(self).write_bytes(data)

      get_download,ifile,ofile = self._test_already_local()

      if ofile and Path(ofile).exists():
         self.msg("file exists so not writing")
         return Path(ofile).stat().st_size

      if ofile:
        self.msg(f'opening output file {ofile}')
        return Path(ofile).write_bytes(data)

  def _get_login(self,head=True):
      u = self
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
    '''msg to self.stderr'''
    try:
      # DONT REPEAT MESSAGES
      if args in self.store_msg:
        return
      self.store_msg.append(args)
    except:
      self.store_msg = [args]
    try:
        if self.verbose or (self.log is not None):
            print('-->',*args,file=self.stderr)
    except:
        pass

  def _test_already_local(self):
    # get local_filename we would use for output
    # delete it if not noclobber
    # dont greate dir if it doesnt exist

    # return False if already downloaded

    # check in database
    store_url  = str(self)
    store_flag = 'data'

    # input file
    ifile = self.database.get_from_db(store_flag,store_url)

    if ifile is not None:
      ifile = Path(ifile)
      if not ifile.exists():
        # otherwise incorrect db entry
        self.database.rm_from_db(store_flag,store_url)
      if not self.noclobber and ifile.exists():   
        # clobber
        self.msg(f'deleting local file {ifile}')
        ifile.unlink()
        ifile = None

    ofile = self._local_file("w")

    if ifile is None:
      return True,ifile,ofile

    if not ifile.exists():
      return True,None,ofile

    # simple if no size check
    if (not self.size_check) and ifile.exists():
      self.msg(f'local file {ifile} exists') #: no size check')
      # cache this in case we want to re-use it
      cache = {store_flag : { str(store_url) : str(ifile) }}
      self.set_db(cache)
      return False,ifile,ofile

    if self.size_check:
      lsize = ifile.stat().st_size
      rsize = self.stat().st_size
      if rsize < 0:
        # then its not available
        self.msg(f'not downloading file')
        # we might not want to download

        # cache this in case we want to re-use it
        cache = {store_flag : { str(store_url) : ifile }}
        self.set_db(cache)
        return False,ifile,ofile

      elif lsize == rsize:
        self.msg(f'local and remote file sizes equal {lsize}')
        self.msg(f'not downloading file')
        # we might not want to download
        # cache this in case we want to re-use it
        cache = {store_flag : { str(store_url) : ifile }}
        self.set_db(cache)
        return False,ifile,ofile
      self.msg(f'local and remote file sizes not equal {lsize}/{rsize} respectively')
      self.msg(f'so we need to download (or set size_check=False)')
      if not self.noclobber:
        if ifile and ifile.exists():
          self.msg(f'deleting local ifile {local_file}')
          ifile.unlink()
          ifile = None
        if ofile and ofile.exists():
          self.msg(f'deleting local ofile {local_file}')
          ofile.unlink()
          ofile = None

    return True,ifile,ofile


  def read_text(self, encoding=None, errors=None):
    '''Open the URL, read in text mode and return text.'''  

    kwargs = {'encoding':encoding}
    u = self
    store_url  = str(u)
    store_flag = 'data'

    if u._isfile():
      self.msg(f'{u} is not a URL: interpreting as Path')
      return Path(u).read_text()

    get_download,ifile,ofile = self._test_already_local()

    text = None

    # get it from ofile
    if ofile and Path(ofile).exists():
      text = Path(ofile).read_text(**kwargs)
      cache = {store_flag : { str(store_url) : str(ofile) }}
      self.set_db(cache)
      return text

    # get it from ifile 
    if ifile and Path(ifile).exists():
      self.msg(f'opening already downloaded file {ifile}')
      text = Path(ifile).read_text(**kwargs)
      if ofile:
        ofile = Path(ofile)
        ofile.write_text(text)
        cache = {store_flag : { str(store_url) : str(ofile) }}
      else:
        cache = {store_flag : { str(store_url) : str(ifile) }}
      self.set_db(cache)
      return text

    if text is not None:
      return text

    try:
      u.msg(f'trying {self}')
      text = u.get_text()
      if text and ofile:
        try:
          ofile = Path(ofile)
          ofile.parent.mkdir(parents=True,exist_ok=True)
          ofile.write_text(text)
          cache = {store_flag : { str(store_url) : str(ofile) }}
          self.set_db(cache)
          return text
        except:
          pass
      if text:
        return text
    except:
      pass

    u.msg(f'getting login')
    r = u._get_login(head=False)
    if type(r) != requests.models.Response:
      return None
    if r.status_code == 200:
      u.msg(f'code {r.status_code}')
      text = r.text
      if ofile:
         ofile = Path(ofile)
         ofile.parent.mkdir(parents=True,exist_ok=True)
         ofile.write_text(text)
         cache = {store_flag : { str(store_url) : str(ofile) }}
         self.set_db(cache)
      return text

    if type(r) == requests.models.Response:
        u.msg(f'code {r.status_code}')
        return r
    u.msg(f'failed to connect')
    return None

  def local(self):
    ''' local filename'''
    u = self
    get_download,ifile,ofile = u._test_already_local()
    for f in [ifile,ofile]:
      if f:
        return Path(f)
    return None

  def exists(self):
    '''Whether this URL exists and can be accessed'''

    u = self
    store_url  = str(u)
    store_flag = 'exists' 
 
    ex = self.database.get_from_db(store_flag,store_url)
    if ex is not None:
      return ex
 
    ex = False 
    get_download,ifile,ofile = u._test_already_local()
    if ofile and Path(ofile).exists():
      ex = True
      cache = {store_flag : { str(store_url) : True }}
    if not ex:
      ex = self.ping()
    if ex:
      cache = {store_flag : { str(store_url) : True }}
      self.set_db(cache)
      
    return ex

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
    u = self
    # check in database
    store_url  = u
    store_flag = 'st_size'
    remote_size = self.database.get_from_db(store_flag,store_url)
    if remote_size is not None:
      return remote_size

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
            # cache this in case we want to re-use it
            cache = {store_flag : { str(store_url) : remote_size }}
            self.set_db(cache)
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
              # cache this in case we want to re-use it
              cache = {store_flag : { str(store_url) : remote_size }}
              self.set_db(cache)
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
      # give up
      remote_size = -2
      # cache this in case we want to re-use it even if its -1
      cache = {store_flag : { str(store_url) : remote_size }}
      self.set_db(cache)
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
    u = self
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
    u = self
    store_url  = str(u)
    store_flag = 'data'
    if u._isfile():
      self.msg(f'{u} is not a URL: interpreting as Path')
      return Path(u).read_bytes()

    get_download,ifile,ofile = self._test_already_local()

    # get from ofile
    if ofile and Path(ofile).exists():
      data = ofile.read_bytes()
      ofile = Path(ofile)
      cache = {store_flag : { str(store_url) : str(ofile) }}
      self.set_db(cache)
      return data

    # get from ifile
    if ifile and Path(ifile).exists():
      ifile = Path(ifile)
      self.msg(f'opening already downloaded file {ifile}')
      data = ifile.read_bytes()
      if ofile: 
        ofile = Path(ofile)
        ofile.parent.mkdir(parents=True,exist_ok=True)
        ofile.write_bytes(data)
        cache = {store_flag : { str(store_url) : str(ofile) }}
      else:
        cache = {store_flag : { str(store_url) : str(ifile) }}
      self.set_db(cache)
      return data

    try:
      u.msg(f'trying {u}')
      r = u.get()
      if type(r) == requests.models.Response:
        if r.status_code == 200:
          u.msg(f'code {r.status_code}')
          data = r.content
          if ofile:
            ofile = Path(ofile)
            ofile.parent.mkdir(parents=True,exist_ok=True)
            ofile.write_bytes(data)
            cache = {store_flag : { str(store_url) : str(ofile) }}
            self.set_db(cache)
          return data
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
            data = r.content
            if ofile:
              ofile = Path(ofile)
              ofile.parent.mkdir(parents=True,exist_ok=True)
              ofile.write_bytes(data)
              cache = {store_flag : { str(store_url) : str(ofile) }}
              self.set_db(cache)
            return data
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

  def has_wildness(self,uc):
    is_wild   = np.logical_or(np.array(['*' in i for i in uc]),
                              np.array(['?' in i for i in uc]))
    is_wild_2 = np.logical_or(np.array(['[' in i for i in uc]),
                              np.array([']' in i for i in uc]))
    is_wild = np.logical_or(is_wild,is_wild_2)
    return is_wild

  def glob(self,pattern):
    '''
    Iterate over this subtree and yield all existing files (of any
    kind, including directories) matching the given relative pattern.

    The URL here then needs to return lxml html code.

    Positional arguments:
       patterm  : to search for e.g. */2021.*.01
                  only wildcards * and ? considered at present

    '''
    u = self
    url = str(u)
    if url[-1] == '/':
      url = urls[:-1]
    url = URL(url,pattern,**(self.kwargs))

    # check in database
    store_url  = url
    store_flag = 'glob' 
    olist = self.database.get_from_db(store_flag,store_url)
    if olist is not None:
      if type(olist) is list:
        return [URL(o,**self.kwargs) for o in olist]
      return [URL(olist,**self.kwargs)]

    uc = np.array(url.parts)
    is_wild = self.has_wildness(uc)
    
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
      l.init(**(self.kwargs))

    # cache this in case we want to re-use it
    cache = {store_flag : { str(store_url) : [str(i) for i in olist] }}
    self.set_db(cache)
    if type(olist) is list: 
      return [URL(o,**self.kwargs) for o in olist]
    return [URL(olist,**self.kwargs)]

  def rglob(self, pattern):
    '''
    Recursively yield all existing files (of any kind, including
    directories) matching the given relative pattern, anywhere in
    this subtree.

    Positional arguments:
       patterm  : to search for e.g. 2021.*.01
                  only wildcards * and ? considered at present


    '''
    return self.glob(pattern)


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

  import pdb;pdb.set_trace()
  if True:
    u='https://e4ftl01.cr.usgs.gov'
    import os
    os.environ['CACHE_DIR'] = 'data'

    url = URL(u,verbose=True,db_file='data/new_db.txt',local_dir='work')
    rlist = url.glob('MOT*/MCD15A3H.006/2003.12.11/*0.hdf')
    for r in rlist:
      u = URL(r,**url.kwargs)
      data=u.read_bytes()
      u.write_bytes(data)

if __name__ == "__main__":
    main()

