#!/usr/bin/env python

import nbformat
import sys
from pathlib import Path
from glob import glob
import subprocess
from nbconvert.preprocessors import ExecutePreprocessor


'''
filter_movies

Purpose:

  modify some notebook cells for different stypes of formatting
  in 042_Weighted_smoothing_and_interpolation, specifically, insert movies
  


Author: P. Lewis
Email:  p.lewis@ucl.ac.uk
Date:   28 Aug 2020
'''

f = "notebooks_lab/042_Weighted_smoothing_and_interpolation.ipynb"
nb = nbformat.read(f,nbformat.NO_CONVERT)
cells = nb.cells.copy()
count = 0
ncells = []
for i,c in enumerate(cells):
    if c['cell_type'] == 'code':
        if ('outputs' in c.keys()) and \
           (len(c['outputs']) == 1) and \
           (c['outputs'][0]['output_type'] == 'execute_result'):
            # found one
            count += 1
            html_file = f'work/demofilt{count}.html'
            print(f"reading {html_file}")
            with open(html_file,'r') as f:
                html = '<video width="100%" controls autoplay loop>' + f.read().split("controls autoplay loop>")[1]
            c["cell_type"] = "markdown"
            c["metadata"] = {}
            insert = f'<html><body>\n{html}\n</body></html>'
            c["source"] = [insert]
            ncells.append(c)
    else:
        ncells.append(c)
nb.cells =  ncells


nout_file = "work/042_Weighted_smoothing_and_interpolation.ipynb"
print(f"writing to {nout_file}")
with open(nout_file,'w') as fout:
    nbformat.write(nb,fout)            
cmd = f'jupyter nbconvert --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.allow_errors=True \
    --nbformat=4 --ExecutePreprocessor.store_widget_state=True --to markdown {nout_file}'
runner = subprocess.run(cmd.split())
           

