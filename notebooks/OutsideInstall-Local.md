
# Instructions for local install of these notes

First, you will need to make sure you have Python (3.6+) installed on your computer. 

We suggest using [Anaconda](https://docs.anaconda.com/anaconda/install), as the package list is set up to work with this. If you choose another version of Python, you will need to convert the environment files and modify the instructions below.

1. Clone this repository and cd to the local directory

        git clone https://github.com/UCL-EO/geog0111.git
        cd geog0111

2. Set up environment

        bin/init.sh  
        python -m ipykernel install --user --name geog0111 --display-name "conda-env-geog0111-geog0111-py"
    
3. Launch jupyter or jupyterlab server


          jupyter notebook
    
    or
  
          jupyter-lab


After this initial setup, just do:

          cd geog0111/notebooks
          jupyter notebook
    
    or
          cd geog0111/
          jupyter-lab
