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
  from geog0111.expand import expand
except:
  from get_doy import get_doy
  from monthdays import monthdays,yeardays
  from expand import expand

def list_of_doys(year,doy=None,day=None,month=None,step=1,verbose=False):
   '''
    Return a pandas Df of reconciled year, doy and file name
    id from date inputs. Checks are made for consistency with step.

    args:    
      year  : year

    options: 
      doy   : day in year, or day in month if month specified, or None
              when specified as day in year, or day in month, can be a list
              1-365/366 or 1-28-31 as appropriate
      day   : day in month or None. Can be list.
      month : month index 1-12 or None. Can be list.
      step  : dataset step. Default 1, but set to 4 for 4-day product, i
              8 for 8-day, 365/366 for year etc.
   '''
   msg = []
   if (type(year) is list) or (type(year) is np.ndarray):
      year = list(year)
   else:
      year = [year]
   year = expand(year,etype='year')
   msg.append(f'year: {year}')
   if (year is None) or (len(year) == 0):
     # nothing to do
     d = pd.DataFrame(data={'year': [], 'doy': []})
     if verbose:
       print(*msg)
     return d

   if (type(doy) is list) or (type(doy) is np.ndarray):
     # list of doys so make year, doy list
     doy = list(doy)
   elif (doy is not None):
     doy = [doy]

   if (doy is None) and (month is None):
     # all doys in year
     doy = list(np.arange(1,367,step))


   if (type(doy) is list):
     doy = expand(doy,etype='doy')
     # list of doys
     msg.append(f'doys: {doy}')
     if len(doy) == len(year):
       # this is a year-doy list
       msg.append('found year-doy list')
     else:
       msg.append('meshing year-doy list')
       # make year-doy list
       _years = []
       _doys = []
       yy,dd = np.meshgrid(year,doy,sparse=False)
       year = yy.flatten()
       doy = dd.flatten()

   elif (month is not None):
     month = expand(month,etype="month")
     # no doys given: 
     # check to see if month is given
     if (type(month) is list) or (type(month) is np.ndarray):
       month = list(month)
     else:
       month = [month]
     # see if day in month is given
     if (day is not None):
       day = expand(day,etype="day")
       if (type(day) is list) or (type(day) is np.ndarray):
         day = list(day)
       else:
         day = [day]
       # else all days
     else:
       day = list(np.arange(1,32))

     # bizarre bug in 3D meshgrid
     # where the first 2 are flipped for 3D
     yy,mm,dd = np.meshgrid(year,month,day,sparse=False)
     # get year, day, month sets
     _years = []
     _doys = []
     yy = yy.flatten()
     mm = mm.flatten()
     dd = dd.flatten()
     for y,m,d in zip(yy,mm,dd):
       try:
         this_doy = get_doy(y,m,d)
         _years.append(y)
         _doys.append(this_doy)
       except:
         pass
     year = _years
     doy  = _doys
   else:
     msg.append("Problem specifying dates in list_of_doys:")
     msg.append(f"year={year}")
     msg.append(f"month={month}")
     msg.append(f"doy={doy}")
     msg.append(f"day={day}")
     print(*msg)
     sys.exit(1)

   year = np.array(year)
   doy  = np.array(doy)
   # Now filter for valid days
   uyears = np.unique(year)
   _years = []
   _doys = []
   for y in uyears:
     filt_ydoys = (year == y)
     udoys = doy[filt_ydoys]
     if step > 1:
       mask = np.remainder(udoys,step)
     else:
       # check doy is in year
       mask = udoys <= get_doy(y,12,31)
     udoys= udoys[mask==1]
     if len(udoys):
       yudoys = udoys * 0 + y
       _years.extend(yudoys)
       _doys.extend(udoys)
   msg.append(f" have {len(_years)} entries")
   year = _years
   doy  = _doys
   d = pd.DataFrame(data={'year': year, 'doy': doy},dtype=np.int)
   if verbose:
     print(*msg)
   return d

def main():
  # test
  year,day,month,step = 2018,1,3,1
  dates = list_of_doys(year,verbose=True,doy=None,day=day,month=month,step=step)
  print(f'year: {year}\nday: {day}\nmonth: {month}\nstep :{step}')
  print(dates)

  year,doy,step = 2018,1,1
  dates = list_of_doys(year,verbose=True,doy=doy,day=None,month=None,step=step)
  print(f'year: {year}\nday: {doy}\nstep :{step}')
  print(dates)

  year,doy,step = [2017,2018],[1,4,6,10,8],1
  dates = list_of_doys(year,verbose=True,doy=doy,day=None,month=None,step=step)
  print(f'year : {year}\nday :  {doy}\nstep : {step}')
  print(dates)

  # try wildcards
  # for day in month
  year,day,month,step = 2018,'*',2,1
  dates = list_of_doys(year,verbose=True,doy=None,day=day,month=month,step=step)
  print(f'year: {year}\nday: {day}\nmonth: {month}\nstep :{step}')
  print(dates)

  # for doy 
  year,doy,step = 2018,'3?*',1
  dates = list_of_doys(year,verbose=True,doy=doy,day=None,month=None,step=step)
  print(f'year: {year}\nday: {day}\nmonth: {month}\nstep :{step}')
  print(dates)
 

if __name__ == "__main__":
    main()




