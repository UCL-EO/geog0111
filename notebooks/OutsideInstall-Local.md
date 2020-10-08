
# Instructions for local install of these notes

First, you will need to make sure you have Python (3.6+) installed on your computer. 

We suggest using [Anaconda](https://docs.anaconda.com/anaconda/install), as the package list is set up to work with this. If you choose another version of Python, you will need to convert the environment files and modify the instructions below. 

You will also need to install the tool [git](https://git-scm.com).

These instructions assume that you will run these commands in a bash shell. You might need to modify in places for other shells.

1. Clone this repository and cd to the local directory

        git clone https://github.com/UCL-EO/geog0111.git
        cd geog0111

2. Download/update required Python packages (will take minutes/tens of minutes):

        conda init 
        bin/set-course.sh


2. Set up environment:

        bin/init0111.sh
        
3. Set up your NASA Earthdata login on the site [https://urs.earthdata.nasa.gov/](https://urs.earthdata.nasa.gov/). 

4. Store the Earthdata password locally. Do this by running the following, and entering your Earthdata login and password when prompted:

        ipython -c "from geog0111.cylog import earthdata; earthdata(True);"
        
   The `True` argument to `earthdata` performs a test of the login that will fail if the login fails. Be aware that if you run this test on a Wednesday, it may fail simply because the NASA servers go down for maintenance. If it fails for other reasons,  reset your password cache with:
   
        ipython -c "from geog0111.cylog import earthdata; earthdata(do_test=True,force=True);"

5. Download the majority of the datasets you'll need (this will take an hour or so):

        bin/get-datasets.sh

6. Build database and set CACHE_FILE (this will take a few minutes to run) (assuming you are using bash -- if not change profile accordingly):

        bin/sort-db.sh  > ~/.url_db/.db.yml
        touch ~/.bash_profile 
        grep -v CACHE_FILE < ~/.bash_profile  > /tmp/.profile.$$
        echo "export CACHE_FILE=${HOME}/.url_db/.db.yml" >> /tmp/.bash_profile.$$
        mv /tmp/.profile.$$ ~/.bash_profile

7. Launch jupyter or jupyterlab server

          jupyter notebook
    
    or
  
          jupyter-lab


After this initial setup, just do:

          cd geog0111/notebooks
          jupyter notebook
    
    or
          cd geog0111/
          jupyter-lab
