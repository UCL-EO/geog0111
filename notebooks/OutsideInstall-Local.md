
# Instructions for local install of these notes

## Requirements

### Anaconda

First, you will need to make sure you have Python (3.6+) installed on your computer. We suggest using [Anaconda](https://docs.anaconda.com/anaconda/install), as the package list is set up to work with this. We suggest you get the most up to date version of Python available. We won't be using the additional tools such as PyCharm, so you don't need to install those for this course (you can if you want to). 

The Anaconda package manager is called `conda`. You should make use of that for managing packages.

If you think you may have Anaconda installed, look at the material on https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-conda.html to see if you need to update.
        

### Installing Anaconda

If you choose another version of Python, you will need to convert the environment files and modify the instructions below. 

Follow the instructions on https://docs.anaconda.com/anaconda/install to install Anaconda on your local computer. 

When prompted:

        Do you wish the installer to initialize Anaconda3
        by running conda init? [yes|no]
        [yes] >>> yes

respond `yes`

You must check you have these installed. **There is little point trying to go further unless you have this sorted!**

Open a new shell (Terminal) and type:

        conda env list
        
        # conda environments:
        #
                                 /Users/plewis/anaconda3
        base                  *  /Users/plewis/opt/anaconda3

The `*` indicates that you have the base environment set.

If you want to use Anaconda Python as your default, look at information on https://docs.anaconda.com/anaconda/user-guide/faq/. 

In a shell, type`:

        conda activate

Then you may need to type:

        conda init
        
though that was probably done in the setup.

You can check where you are getting your Python command from with:

        which python
        
This should give something with `anaconda3` in the name:

        /Users/plewis/opt/anaconda3/bin/python

### `git`

You will also need to install the tool [git](https://git-scm.com) if you don't already have it. You can check to see if you have it with:

        which git
        
This will give something like:

        /usr/local/bin/git
        
If you don't get that, look at the installation instruction again. **There is little point trying to go further unless you have this sorted!**

You may want to check if you need to update `git`: https://phoenixnap.com/kb/how-to-update-git

## Local install in `~`

These instructions assume that you will run these commands in a bash shell. You might need to modify in places for other shells.

We assume you will setup the repository in your home directory (`~`). If not, then replace `~` below by where you want to setup.

1. Clone this repository and cd to the local directory

        cd ~ && git clone https://github.com/UCL-EO/geog0111.git
        cd ~/geog0111
        cd notebooks && tar xvzf data/cacheData.tar.Z

2. Download/update required Python packages (will take minutes/tens of minutes):

        conda env create --force -n geog0111 -f environment.yml

3. Set up environment:

        conda activate geog0111
        
   After running this, close the shell, and test that your conda environment is set to `geog0111`. You can do this e.g. with:
   
        conda env list
  
  which should show something like:
  
        # conda environments:
        #
        base                     /Users/plewis/opt/anaconda3
        geog0111              *  /Users/plewis/opt/anaconda3/envs/geog0111

  You many need to set the notebook environment:

        python -m ipykernel install --name=conda-env-geog0111-geog0111-py --display-name 'conda env:geog0111-geog0111'

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


## Update of the repository

To update your `geog0111` repository, first make sure you take copies of any files (e.g. notebooks) that you may have changed. **If you don't they will be over-written when you pull new versions.**

Then type:

        cd ~/geog0111 && git pull
