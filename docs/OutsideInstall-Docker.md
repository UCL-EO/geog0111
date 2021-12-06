
# Instructions for docker install of these notes

## Requirements

### `docker`

One option for running these notes that requires only minimal setup is using [`docker`](https://www.docker.com).

First then, install the [`docker`](https://www.docker.com) software on your computer and test and run it.

### `git`

You will also need to install the tool [git](https://git-scm.com) if you don't already have it. You can check to see if you have it with:

        which git
        
This will give something like:

        /usr/local/bin/git
        
If you don't get that, look at the installation instruction again. **There is little point trying to go further unless you have this sorted!**

You may want to check if you need to update `git`: https://phoenixnap.com/kb/how-to-update-git


## Local install

We will make a local copy of these notes on your computer (assumed in `~/geog0111`) then run the jupyter notebooks using repo2docker.


### Installing the notes in `~`

First, install the notes:

We assume you will setup the repository in your home directory (`~`). If not, then replace `~` below by where you want to setup.

Clone this repository and cd to the local directory

        cd ~ && git clone https://github.com/UCL-EO/geog0111.git
        cd ~/geog0111
        cd notebooks && tar xvzf data/cacheData.tar.Z

### NASA Earthdata login

Set up your NASA Earthdata login on the site [https://urs.earthdata.nasa.gov/](https://urs.earthdata.nasa.gov/). Store the Earthdata password locally when you come across it in the notes.


### running `docker`

Make sure the environment variables `HOME` and `USER` are set:

        env | grep HOME
        env | grep USER

If not (they should be, though may not be on Windows), then try:

        export USER=$(whoami)
        export HOME=$(cd ~ && pwd)
        
Then run the following command to pull the docker and run the Jupyter notebook server locally:

        docker run --rm -i --volume=${HOME}/geog0111:/home/$USER/tmp/geog0111 -w /home/$USER/tmp/geog0111  -p 8888:8888   -t ucleo/geog0111:latest 


It will eventually respond with something like:


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


The main things for you to see from this are:

A. How to stop the jupyter server:
    
    Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    
    
Use Control-C in the shell you started the server. You might try that now to familiarise yourself with it, and then restart `jupyter notebook`

B. The URL of the server (with the security token). In this case:

        http://127.0.0.1:8888/?token=146dbb8eb09948a20f219c69256926ca6ab62c4fae03d0c1
        
Launch a browser that points to that (your one, not te example here!!). That should take you to the Jupyter server homepage.
<!-- #endregion -->

<!-- #region -->
### Test

Now, test things:
 
   * navigate to the coursenotes `geog0111` then `notebooks`
   * select the fist notebook `001_Notebook_use.md`
   * go through the notes and run the code in the cells

   * if that doesn't launch for any reason, try re-stopping and starting the server
   * failing that, ask for help in the Monday class, or come along to office hours or the Thursday help sessions

One issue to look out for is if the notebook kernel doesn't start. That normally means that either you haven't set up the  `geog0111` environment properly, and/or you didn't setup the notebook kernel properly. Look back over sections 3. and 4. above.

You should test that your setup is robust. 

   * Try logging out and in again on your computer and launch jupyter again
   
## Use of the notes and updates

Periodically, we may have to update the notes. 

Before you do this, be aware that any updated files on the server will over-write your local files. **That means that any changes you may have made to the notebooks**, for example, will be lost. It is vital then that you save the notebooks you are working on with a different name. 

You can easily do this by clicking on the notebook name panel at the top of the notebook (the one that says 'OutsideInstall-Local' here) and changing it (e.g. `myOutsideInstall-Local`). You might do this consistently for all notebooks you use as you go through the course, then you won't have to worry about it when you do updates.


To update the notes (and over-write your changes), in a shell (Terminal) type:

    cd ~/geog0111 && git reset --hard HEAD && git pull
    
