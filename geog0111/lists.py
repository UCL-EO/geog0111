import numpy as np
from pathlib import PosixPath, _PosixFlavour, PurePath
from pathlib import Path
import sys
import stat
import yaml

try:
  from geog0111.cylog import Cylog
  from geog0111.fdict import fdict
except:
  from cylog import Cylog
  from fdict import fdict

def list_resolve(filelist,files=False):
      '''resolve filelist'''
      if (filelist is None) or (filelist == []):
        return []

      if type(filelist) is list:
        filelist = [str(f) for f in filelist if f]
      elif type(filelist) is  str:
        filelist = [filelist]
      elif type(filelist) is PosixPath:
        filelist = [str(filelist)]

      filelist = [str(f) for f in filelist]

      filelist  = remove_duplicates(filelist)

      filelist = [Path(f).expanduser().absolute().resolve() for f in filelist]
      return filelist

def name_resolve(*filelist,name=None):
      '''resolve filename into filelist'''
      if filelist is None:
        return filelist
      filelist = list_resolve(*filelist)

      for i,f in enumerate(filelist):
        # in case its a dir accidently
        if f.exists() and f.is_dir():
          f = Path(f,name)

        parent = f.parent
        if parent.exists() and (not parent.is_dir()):
          try:
            parent.unlink()
          except:
            sys.exit(1)
        try:
          parent.mkdir(parents=True,exist_ok=True)
        except:
          pass
        filelist[i]  = f
      return filelist

def list_info(filelist):
      '''resolve filelist and get read and write permissions'''
      if filelist is None:
        return None,None

      filelist  = np.array(list_resolve(filelist,files=True),dtype=np.object)
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


def remove_duplicates(l):
      '''remove duplicates in list l'''
      if l is None:
        return l
      if len(l) == 0:
        return l
      return list(np.unique(np.array(l,dtype=np.object)).flatten())


def ginit(self,**kwargs):
      '''
      kwargs setup and organisation of local_dir
      and db_dir

      '''
      if not 'defaults' in kwargs:
        defaults = {\
         'verbose'    : False,\
         'noclobber'  : True,\
         'size_check' : False,\
         'store_msg'  : [],\
         'log'        : None,\
         'database'   : None,\
         'stderr'     : sys.stderr,\
        }
      else:
        defaults = kwargs['defaults']
        del kwargs['defaults']

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
      self.__dict__.update(defaults)

      self.store_msg = remove_duplicates(self.store_msg)
      if self.log is not None:
        try:
          self.stderr = Path(self.log).open("a")
          if self.verbose:
            try:
              msg = f"{str(self)}: log file {self.log}"
              self.store_msg.append(msg)
              #print(msg,file=sys.stderr)
            except:
              pass
        except:
          self.stderr = sys.stderr
          self.msg(f"WARNING: failure to open log file {self.log}")

      if 'local_dir' not in self.__dict__:
        self.local_dir = ["work"]

      self.local_dir = list_resolve(self.local_dir)

      self.local_dir  = list_resolve(self.local_dir)
      [d.mkdir(parents=True,exist_ok=True) for d in self.local_dir]
      try:
        self.local_file = name_resolve(self.local_file)
      except:
        self.local_file = name_resolve(self.local_dir,name=self.name)
      try:
        self.db_dir     = list_resolve(self.db_dir)
      except:
        self.db_dir     = list_resolve(['work'])
      [d.mkdir(parents=True,exist_ok=True) for d in self.db_dir]
      try:
        self.db_file    = self.db_file or name_resolve(self.db_dir,name='.db.yml')
      except:
        # fallback 
        self.db_file    = ['work/.db.yml']
      return self.__dict__
