#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import numpy as np
import os
import yaml

'''
system init for database default

to be run by all users as part of setup script

'''


__author__    = "P. Lewis"
__email__     = "p.lewis@ucl.ac.uk"
__date__      = "28 Aug 2020"
__copyright__ = "Copyright 2020 P. Lewis"
__license__   = "GPLv3"



gwork = '/shared/groups/jrole001/geog0111/work'
if not Path(gwork).exists():
  gwork = 'work'

db_dir = f'{gwork}'
try:
  Path(db_dir,'test.dat').touch()
  kwrgs = {
    'db_file'   :    [f'{gwork}/database.db'],
    'db_dir'   :    [f'{gwork}'],
    'local_dir' :    f'{gwork}',
  }
except:
  local = Path('work').absolute()
  kwrgs = {
    'db_file'   :    [f'{gwork}/database.db',f'{local.as_posix()}/database.db'],
    'db_dir'    :    [f'{gwork}',f'{local.as_posix()}'],
    'local_dir' :    local.as_posix(),
  }

initfile = Path('~/.url_db/init.yml').expanduser().absolute()
initfile.parent.mkdir(parents=True,exist_ok=True)
with initfile.open("w") as f:
   yaml.dump(kwrgs,f)



