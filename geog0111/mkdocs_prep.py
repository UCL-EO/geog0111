#!/usr/bin/env python
import sys
import yaml
import os
from pathlib import Path
import numpy as np

'''
Run this script to set up mkdocs.yml
from information in mkdocs.yml, setup.py and
README.md.

It inserts md files of the form notebooks_lab/???_*.md
and filters answers
'''
dev = False
if '--dev' in sys.argv:
  dev = True

# load mkdocs.yml
with open('config/mkdocs.yml','r') as f:
  info = yaml.safe_load(f)

# filter setup.py
cmd=f"grep -v setuptools < setup.py > {Path(Path(sys.argv[0]).parent,'info.py').as_posix()}"
os.system(cmd)
from info import *
cmd="rm -f info.py"
os.system(cmd)

# we have info and sd
try:
  info.update(setup)
except:
  pass

# write to docs/index.md
files = list(Path('docs').glob('???_*.md'))
answers = list(Path('docs').glob('???_*_answers.md'))

answers.sort()
files = [f for f in files if f not in answers]
files.sort()

#defaults make sure one exists for all we need
defaults = {
  'icon':'images/ucl_logo.png'
  'theme':{'favicon':'images/ucl.png'},
  'site_name':'GEOG0111',
  'description':'',
  'author':'A. Nonymous',
  'author_email':'Not known',
  'version':'0.0.1',
  'long_description':''
}
defaults.update(info)
info=defaults


index = f'''
![UCL]({info['icon']})

# {info['site_name']}

{info['description']}.

|   |   |   |   |   |
|---|---|---|---|---|
|Author: [{info['author']}](mailto:{info['author_email']})|version {info['version']}||||

{info['long_description']}

# Notes

'''


with open('docs/index.md','w') as f:
  f.write(index)

# edit mkdocs.yml
# load mkdocs.yml
with open('config/mkdocs.yml','r') as f:
  mkd = yaml.safe_load(f)
print(files)

filenames = np.array([f.name for f in files])
answernames = np.array([f.name for f in answers])

num_filenames = np.sort(np.array([f.split('_')[0] for f in filenames]))
num_answernames = np.sort(np.array([f.split('_')[0] for f in answernames]))

# work out the chapter numbers
level = np.array([[i[j] for i in num_filenames] for j in range(3)])

#u_levels = np.unique(levels)
#t_levels = np.arange(len(u_levels))
#chapter_number = levels.copy()
#for i in t_levels:
#  chapter_number[levels == u_levels[i]] = i


with open('config/sections.dat','r') as f:
  section_names = f.readlines()

with open('config/chapters.dat','r') as f:
  chapter_names = f.readlines()

# nav is a list
nav = []

for j,i in enumerate(np.sort(np.unique(level[1]))):
  other = []
  for s in filenames[level[1] == str(i)].tolist():
    k = ' '.join(s.strip('.md').split('_')[1:]).title()
    k = k.replace('Googleearthengine','Google Earth Engine').\
          replace('Nasa','NASA').\
          replace('Gdal','GDAL').\
          replace('Modis','MODIS').\
          replace('Downloa','Download')
    v = s
    that = dict(zip([k],[v]))
    other.append(that)

  this = {chapter_names[j].strip().title():other}
  nav.append(this)

# put in dev notes?
if dev:
  k,v = "Scripts","bin.md"
  other=[dict(zip([k],[v]))]
  this = {"Developer Notes":other}
  nav.append(this)

mkd['nav'] = nav

with open('mkdocs.yml','w') as f:
  yaml.dump(mkd,f)


