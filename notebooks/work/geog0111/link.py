#!/usr/bin/env python

'''
Put links to required directories in place where copies are
'''
import pathlib
from pathlib import Path
import os
import sys

__author__ = "P Lewis"
__copyright__ = "Copyright 2020 P. Lewis"
__version__ = "1.0 (01.08.2020)"
__email__ = "pl.lewis@ucl.ac.uk"


class Link():
  '''
  Put a symbolic link in dest to src 
  '''
  def __init__(self,dest='OneDrive',src='images',force=True):
      self.dest = dest
      self.src = src
      self.force = force

  def run(self):
      dest = self.dest
      src = self.src
      force = self.force  
      # test if src exists
      if not Path(src).exists():
        print(f"source directory {src} doesn't exist")  
        sys.exit(-1)
      if Path(src).is_absolute():
        print(f"source directory {src} must be a relative path")
        sys.exit(-1)
      new = Path(Path.cwd(),dest,src)
      old = Path(Path.cwd(),src)
      if force:
          try:
            os.remove(new)
          except:
            pass
      if Path(new).exists():
        if force==False:
          print(f"source directory {new} exists")
          sys.exit(-1)
      print(f'{new} -> {old}')
      new.symlink_to(old)
  
def main():
  Link(dest='OneDrive',src='images',force=True).run()

if __name__ == "__main__":
  main(sys.argv[1:])


