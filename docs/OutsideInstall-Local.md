
# Instructions for local install of these notes

To install these notes, first set up the reaquired software [[requirements](OutsideInstall-Requirements.md#1.-Requirements)]. Do not proceed unless you have set up all of these pieces of software.
These are:

* [`gdal`](OutsideInstall-Requirements.md#11-gdal)
* [`anaconda` `python`](OutsideInstall-Requirements.md#12-Anaconda)
* [`git`](OutsideInstall-Requirements.md#13-git)
* [`mamba`](OutsideInstall-Requirements.md#14-mamba)

Then set up and test the notes in a [[local install](OutsideInstall-Local.md#2-local-install-in-)] following the intsructions below.

These instructions assume that you will run these commands in a `bash` shell. You might need to modify in places for other shells such as `zsh` for OS X. Make sure you asre aware of [which shell you are using](https://github.com/UCL-EO/gdal-install/blob/main/InstallBREW.md#11-what-shell-am-i-using).

We assume you will setup the repository in your home directory (`~`). If not, then replace `~` below by where you want to setup.

# Local install of `GEOG0111` 

## 1. Clone this repository and cd to the local directory

        cd ~ && git clone https://github.com/UCL-EO/geog0111.git
        cd ~/geog0111
        cd notebooks && tar xvzf data/cacheData.tar.Z

## 2. Download/update required Python packages 

This may take minutes/tens of minutes, either (if you have `mamba installed):

        mamba env create --force -n geog0111 -f environment.yml
        

or (if no `mamba`. Warning: this is *much* slower)

        conda env create --force -n geog0111 -f environment.yml

## 3. Set up anaconda. 

In the Terminal (shell), type either, if using windows WSL or linux:

        conda init
        echo "conda activate geog0111" >> ~/.bashrc
        
  Or if using OS X:
  
        conda init
        echo "conda activate geog0111" >> ~/.zshrc
 
 
  Then, open a new shell (or type `bash`) and type:
    
        conda env list
        
  This should now show:
    
        # conda environments:
        #
        base                     /Users/plewis/anaconda3
        geog0111              *  /Users/plewis/anaconda3/envs/geog0111

## 4. Set up notebook kernel and extensions 

Do this by running the following in shell (Terminal):

        python -m ipykernel install --name=conda-env-geog0111-geog0111-py --display-name 'conda env:geog0111-geog0111' --user
        ~/geog0111/notebooks/bin/postBuild

## 5. Set up your NASA Earthdata login 

Go to the site [https://urs.earthdata.nasa.gov/](https://urs.earthdata.nasa.gov/). Make sure you know your Earthdata login and password for when you come across it in the notes.



## 6. Launch jupyter or jupyterlab server

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
          

## 8. Test

Now, test things:
 
   * navigate to the coursenotes `geog0111` then `notebooks`
   * select the fist notebook `001_Notebook_use.md`
   * go through the notes and run the code in the cells

   * if that doesn't launch for any reason, try re-stopping and starting the server
   * failing that, ask for help in the Monday class, or come along to office hours or the Thursday help sessions

One issue to look out for is if the notebook kernel doesn't start. That normally means that either you haven't set up the  `geog0111` environment properly, and/or you didn't setup the notebook kernel properly. Look back over sections 3. and 4. above.

You should test that your setup is robust. 

   * Try logging out and in again on your computer and launch jupyter again
   
## 9. Use of the notes and updates

There are some things to be aware of when using and updating the notes, so make sure to look over [these instructions](Using-the-course-notes.md)


