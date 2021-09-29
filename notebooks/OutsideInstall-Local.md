
# Instructions for local install of these notes

First, you will need to make sure you have Python (3.6+) installed on your computer. 

We suggest using [Anaconda](https://docs.anaconda.com/anaconda/install), as the package list is set up to work with this. If you choose another version of Python, you will need to convert the environment files and modify the instructions below. 

You will also need to install the tool [git](https://git-scm.com) if you don't already have it.

These instructions assume that you will run these commands in a bash shell. You might need to modify in places for other shells.

1. Clone this repository and cd to the local directory

        git clone https://github.com/UCL-EO/geog0111.git
        cd geog0111

2. Download/update required Python packages (will take minutes/tens of minutes):

        conda init 


2. Set up environment:

        conda activate geog0111
        
   After running this, close the shell, and test that your conda environment is set to `geog0111`. You can do this e.g. with:
   
        conda env list
  
  which should show something like:
  
        # conda environments:
        #
        base                     /Users/plewis/opt/anaconda3
        geog0111              *  /Users/plewis/opt/anaconda3/envs/geog0111

3. Set up your NASA Earthdata login on the site [https://urs.earthdata.nasa.gov/](https://urs.earthdata.nasa.gov/). Store the Earthdata password locally when you come across it in the notes.

4. Launch jupyter or jupyterlab server

          jupyter notebook
    
    or
  
          jupyter-lab


After this initial setup, just do:

          cd geog0111/notebooks
          jupyter notebook
    
    or
          cd geog0111/
          jupyter-lab
