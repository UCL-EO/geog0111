#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import numpy as np
import os
try:
  from geog0111.modis import Modis
  from geog0111.course_data import pull
except:
  from modis import Modis
  from course_data import pull

def main():
    for tile in ['h17v03', 'h17v04', 'h18v03', 'h18v04',['h17v03', 'h17v04'],['h18v03', 'h18v04'],['h17v03', 'h17v04', 'h18v03', 'h18v04']]:
      tile = [tile]
      for year in [2018,2019,2020]:
        try:
          # LAI
          r = pull('MCD15A3H',year,tile,step=4)
        except:
          pass


if __name__ == "__main__":
    main()




