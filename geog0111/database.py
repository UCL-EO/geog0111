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
except:
  from cylog import Cylog

'''
database for URL lookup and other things ...
'''

__author__    = "P. Lewis"
__email__     = "p.lewis@ucl.ac.uk"
__date__      = "28 Aug 2020"
__copyright__ = "Copyright 2020 P. Lewis"
__license__   = "GPLv3"

class Database():
  '''
  URL look up database
  '''
  def __del__(self):
      '''cleanup'''
      try:
        if self.database != {}:
          if self.init_database != self.database:
            self.set_db(self.database,write=True)
      except:
        pass

  def __exit__(self, *exc):
      '''cleanup'''
      try:
        if self.database != {}:
          if self.init_database != self.database:
            self.set_db(self.database,write=True)
      except:
        pass

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

  def name_resolve(self,*filelist,name=None):
      '''resolve filename into filelist'''

      if filelist is None:
        return filelist
      filelist = self.list_resolve(filelist)

      for i,f in enumerate(filelist):
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

  def fdict(self,this):
    '''return partial version of self.__dict__'''
    dellist = []
    for k,v in this.items():
      if k[:len('_cached')] == '_cached':
        dellist.append(k)
    for k in dellist:
      del this[k]
    return this

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


  def call_db(self):
    '''deal with call to access db and setup if needed'''

    if len(self.db_dir) == 0:
      self.db_dir = self.list_resolve(Path.home() / '.url_db')
      self.msg(f'setting db_dir {self.db_dir}')
    if not self.db_file:
      self.db_file = self.name_resolve([f / '.db.yml' for f in self.db_dir])
      self.msg(f'setting db_file {self.db_file}')
    self.set_db({})
    return self.db_file


  def remove_duplicates(self,l):
      '''remove duplicates in list l'''
      if l is None:
        return l
      if len(l) == 0:
        return l
      return list(np.unique(np.array(l,dtype=np.object)).flatten())


  def __init__(self,args,**kwargs):
      '''
      kwargs setup and organisation of local_dir
      and db_dir

      '''
      defaults = {\
         'verbose'    : False,\
         'db_dir'     : self.list_resolve(['~/.url_db']),\
         'db_file'    : None,\
         'store_msg'  : [],\
         'log'        : None,\
         'database'   : None,\
         'stderr'     : sys.stderr,\
      }
      defaults.update(kwargs)
      old_db = defaults['database']
      self.__dict__.update(defaults)
      try:
        # in case database object passed
        self.__dict__.update(self.fdict(self.database.__dict__))
        if type(old_db) is dict:
          self.database.update(old_db) 
      except:
        pass

      self.store_msg = self.remove_duplicates(self.store_msg)
      if self.log is not None:
        try:
          self.stderr = Path(self.log).open("a")
          if self.verbose:
            try:
              msg = f"database: log file {self.log}"
              self.store_msg.append(msg)
              print(msg,file=sys.stderr)
            except:
              pass
        except:
          self.stderr = sys.stderr
          self.msg(f"WARNING: failure to open log file {self.log}")

      # may be a cache
      if 'CACHE_DIR' in os.environ and os.environ['CACHE_DIR'] is not None:
        self.db_dir = self.list_resolve(self.db_dir + self.list_resolve(os.environ['CACHE_DIR']))
        [d.mkdir(parents=True,exist_ok=True) for d in self.db_dir]

      self.db_dir = self.list_resolve([Path(d).parent for d in self.db_file])
      self.db_file = [Path(f) for f in self.db_file]

      if self.database and (len(self.database.keys())):
        self.msg('getting database from command line')
      else:
        self.database = self.set_db(dict(self.get_db()))
      self.init_database = self.database.copy()


  def filter_db(self,old_db):
    '''clean the database'''
    if not 'data' in old_db.keys():
      return old_db
    old_db = dict(old_db)
    data = dict(old_db['data'])

    # cleaning ...
    for k,v in data.items():
      if Path(v).is_dir():
        del data[k]
      else:
        data[k] = str(v)
    old_db['data'] = data
    return old_db


  def set_db(self,new_db,write=False,clean=False):
    '''save dictionary db in cache database'''
    vold_db = self.database or dict(self.get_db())
    if not clean:
      old_db = vold_db.copy()
    else:
      old_db = {}
    new_db = dict(new_db)
    for k in new_db.keys():
      if k in old_db:
        old_db[k].update(new_db[k])
      else:
        old_db[k] = new_db[k]

    old_db = self.filter_db(old_db)
    new_db = self.filter_db(new_db)

    db_files = self.db_file
    readlist,writelist = self.list_info(db_files)

    if (readlist is None) or (old_db is {}):
      return old_db.copy()

    if not write:
      return new_db

    import pdb;pdb.set_trace()
    for dbf in np.array(db_files,dtype=np.object)[writelist]:
      # make a copy first
      try:
        with Path(str(dbf)+'.bak').open('w') as f:
          self.msg(f"updated cache database in {dbf}")
          yaml.safe_dump(vold_db,f)
      except:
        self.msg(f"unable to update cache database in {str(dbf)+'.bak'}")
      try:
        with dbf.open('w') as f:
          self.msg(f"updated cache database in {str(dbf)}")
          yaml.safe_dump(old_db,f)
      except:
        self.msg(f"unable to update cache database in {dbf}")

    return new_db


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


  def get_db(self):
    '''get the cache database dictionary'''
    db_files = self.db_file
    old_db = {}
    readlist,writelist = self.list_info(db_files)
    for dbf in np.array(db_files,dtype=np.object)[readlist]:
      with dbf.open('r') as f:
        #self.msg(f'reading db file {dbf}')
        try:
          fin = dict(yaml.safe_load(f))
        except:
          self.msg(f'WARNING: error reading data from {dbf}')
        try:
          old_db.update(fin)
        except:
          self.msg(f'WARNING: error updating with data {fin} from {dbf}')
    return old_db

  def rm_from_db(self,store_flag,store_url,**kwargs):
    self.database = self.database or self.get_db()
    del self.database[store_flag][str(store_url)]
    self.set_db(self.database,clean=True)
    return self.database

  def get_from_db(self,flag,url):
    '''see if url is in database'''
    url = str(url)
    try:
      self.database = self.database or self.get_db()
    except:
      self.msg(f'db file {self.call_db()}')
      self.database = self.database or self.get_db()
    try:
      keys = self.database.keys()
    except:
      self.database = self.get_db()
      keys = self.database.keys()
    if flag in self.database.keys():
      if url in self.database[flag].keys():
        self.msg(f'retrieving {flag} {url} from database')
        return self.database[flag][url]
    return None

  def msg(self,*args):
    '''msg to self.stderr'''
    try:
      # DONT REPEAT MESSAGES
      if args in self.store_msg:
        return
      self.store_msg.append(*args)
    except:
      self.store_msg = [*args]
    try:
        if self.verbose or (self.log is not None):
            print('-->',*args,file=self.stderr)
    except:
        pass



def main():
  # database fromn file
  kwargs = {
    'verbose'   :    True
  }
  dbs = ['data/database.db','data/new_db.txt','data/lai_filelist_2016.dat.txt','data/lai_filelist_2017.dat.txt']
  db = Database(dbs,**kwargs)
  database = db.database.copy()
  del db

  kwargs = {
    'database'  :    database,   
    'verbose'   :    True
  }
  db = Database(dbs,**kwargs)
  del db

if __name__ == "__main__":
    main()


