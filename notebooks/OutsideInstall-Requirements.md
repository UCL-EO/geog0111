
# Instructions for local install of these notes

For a local install of these notes, you need to follow the instructions below to make sure that various pieces of software you will need are set up on your computer.

These are:

* [`gdal`](OutsideInstall-Requirements.md#11-gdal)
* [`anaconda` `python`](OutsideInstall-Requirements.md#12-Anaconda)
* [`git`](OutsideInstall-Requirements.md#13-git)
* [`mamba`](OutsideInstall-Requirements.md#14-mamba)

## 1. Requirements

### 1.1 `gdal`

To do the geospatial processing in Python, you will need to install the `gdal` package on your computer. There are specific instructiuons for that [`gdal`](https://github.com/UCL-EO/gdal-install) that youy should follow first. Note that if you are using a windows computer, we suggest using `WSL`, as explained in the link. Then you must also use `WSL` for all of the material below.

### 1.2. Anaconda

First, you will need to make sure you have Python (3.6+) installed on your computer. We suggest using [Anaconda](https://docs.anaconda.com/anaconda/install), as the package list is set up to work with this. We suggest you get the most up to date version of Python available. We won't be using the additional tools such as PyCharm, so you don't need to install those for this course (you can if you want to). 

The Anaconda package manager is called `conda`. You should make use of that for managing packages.

If you think you may have Anaconda installed, look at the material on https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-conda.html to see if you need to update.


### 1.2.1 Installing Anaconda

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

### 1.3. `git`

You will also need to install the tool [git](https://git-scm.com) if you don't already have it. You can check to see if you have it with:

        which git
        
This will give something like:

        /usr/local/bin/git
        
If you don't get that, look at the installation instruction again. **There is little point trying to go further unless you have this sorted!**

You may want to check if you need to update `git`: https://phoenixnap.com/kb/how-to-update-git

## 1.4. `mamba`

Actually, `conda` is pretty slow and cumbersome. A much better package manager (cross platform) is `mamba`. We advise you to download this and use in place of `conda`. Everywhere you see `conda` mantioned below, use `mamba` (after you have installed it obviously).

see [mamba](https://github.com/mamba-org/mamba) for install. e.g.

        conda install mamba -n base -c conda-forge

