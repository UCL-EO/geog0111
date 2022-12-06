# Installation of these notes on UCL JupyterHub

We expect you to run these notes and do this course using Jupyter notebooks, on the [UCL JupyterHub](https://jupyter.data-science.rc.ucl.ac.uk/).

If you know what you are doing, and have accessed the notes in this way before, then you can go straight to the [UCL JupyterHub](https://jupyter.data-science.rc.ucl.ac.uk/).

<!-- #region -->
# The first time you are using Jupyterhub

The first time you are using these notes, you should go through the items below. These are needed to set up the notes and various course settings.

1. If you are not logged on inside the UCL domain, then you will need to make sure you have the [UCL VPN](https://www.ucl.ac.uk/isd/services/get-connected/ucl-virtual-private-network-vpn) installed and running
2. Log on the the [UCL JupyterHub](https://jupyter.data-science.rc.ucl.ac.uk/).

   You may have to start the server at this point.
   
   * click `start my server` to restart (you may have to also then click `launch my server`)
   * if you are asked to choose an interface, choose `classic`, then click `start`

4. Open a Terminal, from `New->Terminal` on the `Control Panel`
5. In the Terminal (shell), type:

        cd ~ && /shared/ucl/apps/git/2.3.5/gnu-4.9.2/bin/git clone https://github.com/UCL-EO/geog0111
    
   This will clone this repository and set up the Python. 
   
5. Set up anaconda. In the Terminal (shell), type:

        conda init
        conda config --prepend envs_dirs /shared/groups/jrole001/geog0111/envs
        echo "conda activate geog0111" >> ~/.bashrc
        bash
        
  This sets up the conda environment we need for the notebooks in the first two commands. The last two commands make sure that the correct environment is loaded when you log in.
        
 6. Now type:
    
        conda env list
        
    This should now show:
    
        # conda environments:
        #
        base                     /opt/miniconda-jhub/4.8.3
        jhubcode                 /opt/miniconda-jhub/4.8.3/envs/jhubcode
        geog0111              *  /shared/groups/jrole001/geog0111/envs/geog0111
        
If it doesn't, type:

         bash
         
and try again.        

7. Now, set up notebook extensions by running the foillowing in shell (Terminal):

        ~/geog0111/notebooks/bin/postBuild
        
        
8. This should all be good to go now, but you should make sure that the new settings have taken place by stopping and restarting the notebook server. To do this:

   * click on the `Control Panel` button at the top right of the notebook page. 
   * then click the big red button to stop the server
   * next, click `start my server` to restart (you may have to also then click `launch my server`)
   * if you are asked to choose an interface, choose `classic`, then click `start`
  
 9. Now, test things:
 
   * navigate to the coursenotes `geog0111` then `notebooks`
   * select the fist notebook `001_Notebook_use.md`
   * go through the notes and run the code in the cells
   * if that doesn't launch for any reason, try re-stopping and starting the server
   * failing that, ask for help in the Monday class, or come along to office hours or the Thursday help sessions

# Running on UCL JupyterHub

1. Make sure you in the UCL domain OR have the [UCL VPN](https://www.ucl.ac.uk/isd/services/get-connected/ucl-virtual-private-network-vpn) installed and running OR that you are running from [Desktop@UCL](https://www.ucl.ac.uk/isd/services/computers/remote-access/desktopucl-anywhere)
2. Log in to the [UCL JupyterHub](https://jupyter.data-science.rc.ucl.ac.uk/).
3. Navigate to the directory `geog0111/notebooks`
4. Access the notebooks you want directly, or via the index [TIMETABLE.md](TIMETABLE.md).
5. See further information on the course [Moodle page](https://moodle.ucl.ac.uk/course/view.php?id=21495)

# Use of the notes and updates

Periodically, we may have to update the notes. 

Before you do this, be aware that any updated files on the server will over-write your local files. **That means that any changes you may have made to the notebooks**, for example, will be lost. It is vital then that you save the notebooks you are working on with a different name. 

You can easily do this by clicking on the notebook name panel at the top of the notebook (the one that says 'Install' here) and changing it (e.g. `myInstall`). You might do this consistently for all notebooks you use as you go through the course, then you won't have to worry about it when you do updates.


To update the notes (and over-write your changes), in a shell (Terminal) type:

    cd ~/geog0111 && /shared/ucl/apps/git/2.3.5/gnu-4.9.2/bin/git reset --hard HEAD && git pull
    
    
<!-- #endregion -->
