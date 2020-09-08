#!/usr/bin/env python

import nbformat
import sys
from pathlib import Path
from glob import glob
import subprocess
from nbconvert.preprocessors import ExecutePreprocessor


'''
edit_notebook

Purpose:

  modify some notebook cells for different stypes of formatting


Author: P. Lewis
Email:  p.lewis@ucl.ac.uk
Date:   28 Aug 2020
'''

README = '''
Do not edit the files in here: they are automatically generated from:

    python geog0111/edit_notebook.py

The script filters notebooks of the form ???_*.ipynb in notebooks to remove:

- headers and tailers
- solution2 answer cells (with `# ANSWER` in code cells)


This results in a simpler notebook form that doesn't need notebook extensions to run.

'''


class EditNotebook():
    '''
    modify some notebook cells for different stypes of formatting
    '''

    def __init__(self,indir,README=README,verbose=True,\
                                kernel_name='geog0111',\
                                subs=['data', 'geog0111', 'images'],\
                                here=False,outdir='_lab',mdout='docs'):

      # dont define the kernel as this should be in the nb
      #self.ep = ExecutePreprocessor(timeout=600,kernel_name=kernel_name)
      self.md_store = None
      self.stderr = sys.stderr
      outdir = indir + outdir
      self.verbose   = verbose
      self.outdir    = Path(outdir)
      self.mdout     = Path(mdout)
      self.indir     = Path(indir)
      self.filters = [self.remove_header_and_tailer_filter,\
                      self.filter_out_solution2_answers,\
                      self.filter_get_title] 
      self.subs = subs
      self.nb_version = 4
      self.notebooks = glob(Path(self.indir,'???_*.ipynb').as_posix())
      self.README = README
      self.here = Path(here or Path.cwd())
      # for nb files
      self.sort_outdir(outdir=self.outdir)
      # for md files
      self.sort_outdir(outdir=self.mdout)

    def log(self,*args,**kwargs):
      '''
      internal logging facility

      if self.verbose, then print to stdout
      otherwise do nothing.
      '''
      if self.verbose:
        print(*args,**kwargs,file=self.stderr)

    def run_nb(self,notebook_filename):
      '''
      run notebook 
      '''
      rundir = Path(notebook_filename).parent.as_posix()
      self.log(f'--> running notebook {notebook_filename}')
      cmd = f'jupyter nbconvert --ExecutePreprocessor.timeout=600 \
                 --ExecutePreprocessor.allow_errors=True \
                 --nbformat=4 \
                 --ExecutePreprocessor.store_widget_state=True \
                 --to notebook --execute {notebook_filename}'
      print(cmd)
      runner = subprocess.run(cmd.split())
      if runner.returncode != 0:
        self.log(f'    ERROR')
        sys.exit(1)
      else:
        self.log(f'    done')
      return True

    def sort_outdir(self,outdir=False,subs=False,here=False,README=False):
      '''
      mkdir outdir and tidy ups
      '''
      subs = subs or self.subs
      outdir = Path(outdir or self.outdir)
      README = README or self.README
      here   = Path(here or self.here)
      
      self.log(f'--> mkdir {outdir.as_posix()}')
      outdir.mkdir(parents=True, exist_ok=True)

      self.log(f'--> creating README.md')
      with open(Path(outdir,'README.md'),'w') as f:
        f.write(self.README)
      
      # sym link for subs to cwd
      #for s in subs:
      #  t = Path(here,s)
      #  if t.exists() and t.is_dir():
      #    p = Path(outdir,s)
      #    if p.exists():
      #      p.unlink()
      #    p.symlink_to(t,target_is_directory=True)
      #    self.log(f'--> link {p.as_posix()} to {t.as_posix()}')  

    def trust_notebook(self,nb_name,run=False):
      '''
      jupyter trust notebook
      '''
      ok = True
      name = Path(nb_name).resolve().as_posix()
      self.log(f'--> trusting {name}')
      cmd = f"jupyter trust {name}"
      runner = subprocess.run(cmd.split(),shell=True,capture_output=True)
      self.log('    done')
      return ok
 
    def loop(self,notebooks=False,filters=False):
      '''
      Loop over notebooks and process
      '''
      notebooks = (notebooks or self.notebooks)
      notebooks.sort()
      nout = None 
      filters = filters = self.filters
      for n in notebooks:
        try:
          # first trust it
          if self.trust_notebook(n,run=True):
            with open(n,'r') as f:

              # read nb file
              self.log(f"--> open file {n}")
              nb = nbformat.read(f,nbformat.NO_CONVERT)
              self.log(f"--> read ...")

              # filters
              nout,d_nb = self.apply_filters(nb,filters=filters)
              for no in [nout, d_nb]:
                no['metadata']['kernelspec'] = nb['metadata']['kernelspec']

              # output directory
              self.log(f"--> updating {n}")
              nout_file = Path(self.outdir,Path(n).name).as_posix()

              # filtered nb output
              self.log(f"--> to {nout_file}")
              with open(nout_file,'w') as fout:
                nbformat.write(nout,fout)
              self.trust_notebook(nout_file)

              # filtered md output
              

              # deal with filtered cells
              if len(d_nb['cells']):
                self.log(f"--> filtered cells exist")
                nout_file_filtered =  Path(nout_file).as_posix().replace('.ipynb','_answers.ipynb')
                self.log(f"--> writing to {nout_file_filtered}")
                with open(nout_file_filtered,'w') as fout:
                  nbformat.write(d_nb,fout)
                self.trust_notebook(nout_file_filtered)
              self.log(f"    done\n--> {'='*20} ")

        except:
          self.log(f"error processing notebook {n}")
      return nout

    def apply_filters(self,nb,filters=[]):

      # new notebook for delete
      d_nb = nbformat.v4.new_notebook()
      for k in nb.keys():
        if k != 'cells':
          d_nb[k] = nb[k]

      for f in filters:
        nb,d_nb = f(nb,d_nb)

      return nb,d_nb

    def filter_get_title(self,nb,d_nb):
      '''
      Get NB title and put it in d_nb
      '''
      # first markdown cell with # 
      item = '# '
      deletes = []
      ncells = len(nb.cells)
      self.log('--> **filter**: filter_get_title')
      self.log(f"----> examining cells ...")
      for i,c in enumerate(nb.cells):
        if c.cell_type == 'markdown' and c.source.find(item) > -1: 
          for ss in c.source.split('\n'):
            if ss.find(item) > -1:
              self.log(f'--> found title {ss}')
              if len(d_nb['cells']):
                self.log(f'--> adding to cells')
                new_cell = nbformat.v4.new_markdown_cell(source=f"{ss} : Answers to exercises")
                d_nb['cells'].insert(0,new_cell)
              return nb,d_nb
      self.log(f'--> no title found')
      # didnt find one
      return nb,d_nb

    def remove_header_and_tailer_filter(self,nb,d_nb):
      '''
      Filter cells to remove any cells that contain header or tailer
      items
      '''
      items = ['<img src="images/noun_post','<img src="images/noun_pre',\
               "<img alt='UCL'"]
      deletes = []
      ncells = len(nb.cells)
      self.log('--> **filter**: remove_header_and_tailer_filter')
      self.log(f"----> examining cells ...")
      for i,c in enumerate(nb.cells):
        if c.cell_type == 'markdown':
          ok = True
          for item in items:
            if c.source.find(item) > -1:
              ok = False
              break
          if not ok:
            deletes.append(c)
      for d in deletes:
        nb.cells.remove(d)
      if len(nb.cells) < ncells:
        self.log(f"--> reduced list of cells from {ncells} to {len(nb.cells)}")

      # we dont want the deletes
      return nb,d_nb

 
    def filter_out_solution2_answers(self,nb,d_nb):
      '''
      Filter cells from notebook with solution2 
      For use when notebook extensions not available
 
      Only keep cells with ## exercise or similar
      '''
      deletes = []
      keep_deletes = []
      ncells = len(nb.cells)
      self.log(f"--> **filter**: filter_out_solution2_answers ")
      self.log(f"----> examining cells ...")
      for i,c in enumerate(nb.cells):
        # keep these for answers notebook
        if 'solution2' in c.metadata:
          for tag in ['solution2', 'solution2_first']:
            if tag in c.metadata:
              del c.metadata[tag]
              nb.cells[i] = c

          keep_deletes.append(c)

          # look for ### Exercise or #### Exercise to keep
          s = c.source.lower().split()
          if (bool(len([s[i+1] for i,ss in enumerate(s[:-1]) \
                       if '##' in ss and 'exercise' in s[i+1]]) == 0)):        
            # dont keep this
            deletes.append(c)

      for d in deletes:
        nb.cells.remove(d)

      for d in keep_deletes:
        d_nb.cells.append(d)  
 
      if len(nb.cells) < ncells:
        self.log(f"--> reduced list of cells from {ncells} to {len(nb.cells)}")
 
      return nb,d_nb

 
# example calling the function    
def main():
  note = EditNotebook('notebooks')
  n = note.loop()

if __name__ == "__main__":
  # execute only if run as a script
  main()


