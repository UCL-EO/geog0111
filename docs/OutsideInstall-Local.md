
# Instructions for local install of these notes

## Requirements

### `gdal`

To do the geospatial processing in Python, you will need to install the `gdal` package on your computer. There are specific instructiuons for that [here](InstallGDAL.md). Note that if you are using a windows computer, we suggest using `WSL`, as explained in the link. Then you must also use `WSL` for all of the material below.

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
        
This should show:        
        
        # conda environments:
        #
        base                  *   /Users/plewis/anaconda3


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

        /Users/plewis/anaconda3/bin/python

### `git`

You will also need to install the tool [git](https://git-scm.com) if you don't already have it. You can check to see if you have it with:

        which git
        
This will give something like:

        /usr/local/bin/git
        
If you don't get that, look at the installation instruction again. **There is little point trying to go further unless you have this sorted!**

You may want to check if you need to update `git`: https://phoenixnap.com/kb/how-to-update-git

## mamba

Actually, `conda` is pretty slow and cumbersome. A much better package manager (cross platform) is `mamba`. We advise you to download this and use in place of `conda`. Everywhere you see `conda` mantioned below, use `mamba` (after you have installed it obviously).

see [mamba](https://github.com/mamba-org/mamba) for install. e.g.

        conda install mamba -n base -c conda-forge

## Local install in `~`

These instructions assume that you will run these commands in a bash shell. You might need to modify in places for other shells.

We assume you will setup the repository in your home directory (`~`). If not, then replace `~` below by where you want to setup.

1. Clone this repository and cd to the local directory

        cd ~ && git clone https://github.com/UCL-EO/geog0111.git
        cd ~/geog0111
        cd notebooks && tar xvzf data/cacheData.tar.Z

2. Download/update required Python packages (will take minutes/tens of minutes):

        conda env create --force -n geog0111 -f environment.yml

3. Set up anaconda. In the Terminal (shell), type:

        conda init
        echo "conda activate geog0111" >> ~/.bashrc
        
    Then, open a new shell (or type `bash`) and type:
    
        conda env list
        
    This should now show:
    
        # conda environments:
        #
        base                     /Users/plewis/anaconda3
        geog0111              *  /Users/plewis/anaconda3/envs/geog0111

4. Finally, set up notebook kernel and extensions by running the following in shell (Terminal):

        python -m ipykernel install --name=conda-env-geog0111-geog0111-py --display-name 'conda env:geog0111-geog0111' --user
        ~/geog0111/notebooks/bin/postBuild

5. Set up your NASA Earthdata login on the site [https://urs.earthdata.nasa.gov/](https://urs.earthdata.nasa.gov/). Store the Earthdata password locally when you come across it in the notes.

6. Launch jupyter or jupyterlab server

          jupyter notebook


This will respond with something like:


        [I 06:58:25.120 NotebookApp] Serving notebooks from local directory: /Users/plewis/Documents/GitHub/geog0111
        [I 06:58:25.120 NotebookApp] Jupyter Notebook 6.4.4 is running at:
        [I 06:58:25.120 NotebookApp] http://The-Brain.local:8888/?token=146dbb8eb09948a20f219c69256926ca6ab62c4fae03d0c1
        [I 06:58:25.120 NotebookApp]  or http://127.0.0.1:8888/?token=146dbb8eb09948a20f219c69256926ca6ab62c4fae03d0c1
        [I 06:58:25.120 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
        [C 06:58:25.164 NotebookApp] 

            To access the notebook, open this file in a browser:
                file:///Users/plewis/Library/Jupyter/runtime/nbserver-88431-open.html
            Or copy and paste one of these URLs:
                http://The-Brain.local:8888/?token=146dbb8eb09948a20f219c69256926ca6ab62c4fae03d0c1
             or http://127.0.0.1:8888/?token=146dbb8eb09948a20f219c69256926ca6ab62c4fae03d0c1


The main things for you that o see from this are:

A. How to stop the jupyter server:
    
    Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    
    
Use Control-C in the shell you started the server. You might try that now to familiarise yourself with it, and then restart `jupyter notebook`

B. The URL of the server (with the security token). In this case:

        http://127.0.0.1:8888/?token=146dbb8eb09948a20f219c69256926ca6ab62c4fae03d0c1
        
Launch a browser that points to that (your one, not te example here!!). That should take you to the Jupyter server homepage.

<!-- #region -->
After this initial setup, just do:


          cd ~/geog0111/notebooks
          jupyter notebook

to get to this point.
          

7. Now, test things:
 
   * navigate to the coursenotes `geog0111` then `notebooks`
   * select the fist notebook `001_Notebook_use.md`
   * go through the notes and run the code in the cells

   * if that doesn't launch for any reason, try re-stopping and starting the server
   * failing that, ask for help in the Monday class, or come along to office hours or the Thursday help sessions

One issue to look out for is if the notebook kernel doesn't start. That normally means that either you haven't set up the  `geog0111` environment properly, and/or you didn't setup the notebook kernel properly. Look back over sections 3. and 4. above.

9. You should test that your setup is robust. 

   * Try logging out and in again on your computer and launch jupyter again
   
## Use of the notes and updates

Periodically, we may have to update the notes. 

Before you do this, be aware that any updated files on the server will over-write your local files. **That means that any changes you may have made to the notebooks**, for example, will be lost. It is vital then that you save the notebooks you are working on with a different name. 

You can easily do this by clicking on the notebook name panel at the top of the notebook (the one that says 'OutsideInstall-Local' here) and changing it (e.g. `myOutsideInstall-Local`). You might do this consistently for all notebooks you use as you go through the course, then you won't have to worry about it when you do updates.


To update the notes (and over-write your changes), in a shell (Terminal) type:

    cd ~/geog0111 && git reset --hard HEAD && git pull
    
<!-- #endregion -->
