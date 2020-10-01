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
  from geog0111.fdict import fdict
  from geog0111.lists import list_resolve,name_resolve,list_info
except:
  from cylog import Cylog
  from fdict import fdict
  from lists import list_resolve,name_resolve,list_info

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

  def call_db(self):
    '''deal with call to access db and setup if needed'''

    if len(self.db_dir) == 0:
      self.db_dir = list_resolve(Path.home() / '.url_db')
      self.msg(f'setting db_dir {self.db_dir}')
    if not self.db_file:
      self.db_file = name_resolve([f / '.db.yml' for f in self.db_dir])
      self.msg(f'setting db_file {self.db_file}')
    self.set_db({})
    return self.db_file

  def __init__(self,args,**kwargs):
      '''
      kwargs setup and organisation of local_dir
      and db_dir

      args are database files
      '''

      defaults = {\
         'verbose'    : False,\
         'db_dir'     : None,\
         'db_file'    : None,\
         'log'        : None,\
         'database'   : None,\
         'stderr'     : sys.stderr,\
      }
      # try to read from ~/.url_db/.init
      initfile = Path('~/.url_db/init.yml').expanduser().absolute()
      if initfile.exists():
        #self.msg(f'reading init file {initfile.as_posix()}')
        with initfile.open('r') as f:
          info = yaml.safe_load(f)
      else:
        info = {}

      defaults.update(info)
      defaults.update(kwargs)
      old_db = defaults['database']
      self.__dict__.update(defaults)

      if ('database' in self.__dict__) and (type(self.database) is Database):
        try:
          print("WARNING: shouldnt be here  ... ")
          this = self.database.__dict__
          # in case database object passed
          self.__dict__.update(fdict(this))
          if type(old_db) is dict:
            self.database.update(old_db) 
        except:
          pass

      if self.log is not None:
        try:
          self.stderr = Path(self.log).open("a")
          if self.verbose:
            try:
              #msg = f"database: log file {self.log}"
              self.store_msg.append(msg)
              print(msg,file=sys.stderr)
            except:
              pass
        except:
          self.stderr = sys.stderr
          self.msg(f"WARNING: failure to open log file {self.log}")
 
      if type(self.db_file) is str:
        self.db_file = [self.db_file]

      # database files
      if (self.db_file is None):
        self.db_file = args
      #else:
      #  if type(self.db_file) is not list:
      #    self.db_file = [self.db_file]
      #  self.db_file.append(args)

      if (self.db_file is not None) and type(self.db_file) is not list:
        self.db_file = [self.db_file]
      if (self.db_dir is not None) and type(self.db_dir) is not list:
        self.db_dir = [self.db_dir]

      # may be a cache
      #cache=Path("/shared/groups/jrole001/geog0111/work/database.db")
      #if cache.exists():
      #  cache = cache.as_posix()
      #  self.msg(f'using cache {cache}')
      #  if "db_file" not in self.__dict__:
      #    self.db_file = cache
      # 
      #  if (self.db_file is None):
      #    self.db_file = cache 
      #  else:
      #    self.db_file = list_resolve([cache] + self.db_file)
      if info == {} and 'CACHE_FILE' in os.environ and os.environ['CACHE_FILE'] is not None:
        db_file = [str(l) for l in list_resolve(os.environ['CACHE_FILE'])]
        #self.msg(f'using cache {db_file}')
        if (self.db_file is None):
          self.db_file = db_file
        else:
          self.db_file = list_resolve(self.db_file + db_file)

      if ((type(self.db_dir) is list) and len(self.db_dir) == 0):
        self.db_dir = None

      if ((type(self.db_file) is list) and len(self.db_file) == 0):
        self.db_file = None

      if type(self.db_file) is str:
        self.db_file = [self.db_file] 

      if type(self.db_dir) is str:
        self.db_dir = [self.db_dir] 

      # writeable db_files
      if (self.db_file is not None):
        # ie we apparently have something
        can_write = False
        for d in self.db_file:
          try:
            Path(d).touch()
            can_write = True
          except:
            pass

      # in case still none or no writeable     
      if (not can_write) or (self.db_file is None):
        # in case self.db_dir is none
        if (self.db_dir is None):
          self.db_dir = list_resolve([Path('~','.url_db')])
        if (self.db_file is None):
          self.db_file = [Path(d,'.db.yml') for d in self.db_dir] 
        else:
          self.db_file.extend([Path(d,'.db.yml') for d in self.db_dir])

      self.db_file = list_resolve([Path(f) for f in self.db_file])
      self.db_dir = [Path(d).parent for d in self.db_file]

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
    try:
      for k,v in data.items():
        if v is None:
          # error in dba
          print(f"WARNING: database None error {k}:{v}")
          del data[k]
        elif type(v) is list:
          v = v[0]
        if Path(v).is_dir():
          del data[k]
        else:
          data[k] = str(v)
      old_db['data'] = data
    except:
      print(f"WARNING: database error {k}:{v}")  
    return old_db


  def set_db(self,new_db,write=False,clean=False):
    '''save dictionary db in cache database'''
    if write:
      vold_db = self.database or dict(self.get_db())
      if not clean:
        old_db = vold_db.copy()
      else:
        old_db = {}

    new_db = dict(new_db)

    if write:
      for k in new_db.keys():
        if k in old_db:
          try:
            old_db[k].update(new_db[k])
          except:
            # format error
            self.msg(f"WARNING fixing database format error for {self.db_file}")
            old_db[k] = new_db[k]
        else:
          old_db[k] = new_db[k]
      old_db = self.filter_db(old_db)

    new_db = self.filter_db(new_db)

    db_files = self.db_file
    readlist,writelist = list_info(db_files)

    if write and ((readlist is None) or (old_db is {})):
      return old_db.copy()

    if not write:
      return new_db

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

  def get_db(self):
    '''get the cache database dictionary'''
    db_files = self.db_file
    old_db = {}
    readlist,writelist = list_info(db_files)
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
          try:
            self.msg(f'WARNING: error updating with data {fin} from {dbf}')
          except:
            pass
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
      try:
        if url in self.database[flag].keys():
          self.msg(f'retrieving {flag} {url} from database')
          return list(np.unique(np.array(self.database[flag][url],dtype=np.object)))
      except:
        pass
    return None

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



def main():
  # database fromn file
  kwargs = {
    'verbose'   :    True
  }
  dbs = ['data/database.db','data/new_db.txt','data/lai_filelist_2016.dat.txt','data/lai_filelist_2017.dat.txt']
  db = Database(dbs,**kwargs)
  # this is how to pass on a database 
  database = db.database.copy()
  del db

  kwargs = {
    'database'  :    database,   
    'verbose'   :    True
  }
  db = Database(dbs,**kwargs)
  del db

  # try no arg: default
  kwargs = {
    'verbose'   :    True
  }
  db = Database(None,**kwargs)

if __name__ == "__main__":
    main()


