#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import gdal
from pathlib import Path
import datetime
import numpy as np
import os
import pandas as pd
import fnmatch

try:
  from geog0111.get_doy import get_doy
  from geog0111.monthdays import monthdays,yeardays
except:
  from get_doy import get_doy
  from monthdays import monthdays,yeardays


def expand(s,etype='year'):
  '''
  expand wildcards
  '''
  # deal with lists and so on
  if (type(s) is list) or (type(s) is np.ndarray):
    ss = np.array([expand(i,etype=etype) for i in s]).flatten()
    retval = ss
  else:
    if etype == 'year':
      this_year = datetime.datetime.now().year
      all_s = np.arange(2000,this_year+1).astype(str)
    elif etype == 'month':
      all_s = np.arange(1,13).astype(str)
    elif etype == 'day':
      all_s = np.arange(1,32).astype(str)
    elif etype == 'doy':
      all_s = np.arange(1,367).astype(str)
    else:
      print(f"FATAL ERROR in expand: unrecognised etype: {etype}")
      print("etype=year|day|month|doy")
      sys.exit(1)
    ins   = str(s)
    matches = np.array([fnmatch.fnmatch(i,ins) for i in all_s])
    retval = all_s[matches]
  if len(retval) > 0:
    retval = retval[retval != None]
    return retval.astype(int)
  return 

def main():
  # test
  # try wildcards
  i = 2018
  r = expand(i)
  print(f'expand: {i} -> {r}')

  i = [1999,2000,2018,2020]
  r = expand(i)
  print(f'expand: {i} -> {r}')

  i = [1999]
  r = expand(i)
  print(f'expand: {i} -> {r}')

  i = 1999
  r = expand(i)
  print(f'expand: {i} -> {r}')

  i = ['201?']
  r = expand(i)
  print(f'expand: {i} -> {r}')

  i = ['201*']
  r = expand(i)
  print(f'expand: {i} -> {r}')

  i = '201*'
  r = expand(i)
  print(f'expand: {i} -> {r}')

  i = '3??'
  r = expand(i,etype='doy')
  print(f'expand doy: {i} -> {r}')

  i = '1*'
  r = expand(i,etype='doy')
  print(f'expand doy: {i} -> {r}')

  i = '1*'
  r = expand(i,etype='month')
  print(f'expand month: {i} -> {r}')

  i = '*'
  r = expand(i,etype='day')
  print(f'expand day: {i} -> {r}')




if __name__ == "__main__":
    main()




