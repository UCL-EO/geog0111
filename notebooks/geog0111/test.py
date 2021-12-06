#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import os

here = str(Path('.').absolute())
if 'PYTHONPATH' not in os.environ:
  os.environ['PYTHONPATH'] = here
else:
  os.environ['PYTHONPATH'] = f"{here}:{os.environ['PYTHONPATH']}"

if 'PATH' not in os.environ:
  os.environ['PATH'] = here
else:
  os.environ['PATH'] = "'{here}:{os.environ['PYTHONPATH']}"

import os
try:
  from geog0111.modis import Modis
except:
  from modis import Modis



