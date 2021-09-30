# Installation of these notes on UCL JupyterHub

We expect you to run these notes and do this course using Jupyter notebooks, on the [UCL JupyterHub](https://jupyter.data-science.rc.ucl.ac.uk/).

If you know what you are doing, and have accessed the notes in this way before, then you can go straight to the [UCL JupyterHub](https://jupyter.data-science.rc.ucl.ac.uk/).

1. If you are not logged on inside the UCL domain, then you will need to make sure you have the [UCL VPN](https://www.ucl.ac.uk/isd/services/get-connected/ucl-virtual-private-network-vpn) installed and running
2. Log on the the [UCL JupyterHub](https://jupyter.data-science.rc.ucl.ac.uk/).
3. Open a Terminal, from `New->Terminal` on the `Control Panel`
4. In the Terminal (shell), type:

        cd ~ && git clone https://github.com/UCL-EO/geog0111
        cd ~/geog0111/notebooks && tar xvzf data/cacheData.tar.Z
    
   This will clone this repository and set up the Python. It also sets up a partial data cache (in `.modis_cache`).
   
5. Set up anaconda. In the Terminal (shell), type:

        conda init
        conda config --prepend envs_dirs /shared/groups/jrole001/geog0111/envs
        echo "conda activate geog0111" >> ~/.bashrc
        
    Then, open a new shell (or type `bash`) and type:
    
        conda env list
        
    This should now show:
    
        # conda environments:
        #
        base                     /opt/miniconda-jhub/4.8.3
        jhubcode                 /opt/miniconda-jhub/4.8.3/envs/jhubcode
        geog0111              *  /shared/groups/jrole001/geog0111/envs/geog0111


# Running on UCL JupyterHub

1. Make sure you in the UCL domain OR have the [UCL VPN](https://www.ucl.ac.uk/isd/services/get-connected/ucl-virtual-private-network-vpn) installed and running OR that you are running from [Desktop@UCL](https://www.ucl.ac.uk/isd/services/computers/remote-access/desktopucl-anywhere)
2. Log on the the [UCL JupyterHub](https://jupyter.data-science.rc.ucl.ac.uk/).
3. Navigate to the directory `geog0111/notebooks`
4. Access the notebooks you want directly, or via the [index](TIMETABLE.md).
5. See further information on the course [Moodle page](https://moodle.ucl.ac.uk/course/view.php?id=21495)
