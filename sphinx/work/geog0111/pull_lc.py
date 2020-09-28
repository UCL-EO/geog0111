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
    for tile in ['h17v03', 'h17v04', 'h18v03', 'h18v04','h09v04','h10v04','h11v04','h12v04','h19v03','h19v04','h30v10','h31v10','h19v11','h19v10','h22v10','h23v10']:
      tile = [tile]
      for year in [2018,2019,2020]:
        try:
          # LC
          r = pull('MCD12Q1',year,tile,step=400)
        except:
          pass


if __name__ == "__main__":
    main()




