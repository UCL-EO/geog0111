# 004 Setup, Accounts and logins

## Introduction

### Google Earth Engine


You will also need to make sure you have a [google account](https://support.google.com/accounts/answer/27441?hl=en) to be able to use GEE, and will need to know your username and password. In addition, you will need to sign up for a GEE account. You need to request this by filling out the form at [signup.earthengine.google.com]( https://signup.earthengine.google.com/). **You will need to do this before we start the class** as you will need to wait for approval from Google.


### NASA Earthdata login and password


Before you can use the material in these notebooks, you will need to register as a user at the [`NASA EarthData`](https://urs.earthdata.nasa.gov/users/new).

Once you have done that, make sure you know your `username` and `password` ready for below.

Some web resources require you to use a login and password. In any publicly available files (like these notebooks) we do not want to expose sensitive information such information.

To that in these notes we can make use of stored passwords and usernames using the local [cylog](geog0111/cylog.py) package. 

Information is encrypted in a user read-only file in your home directory (mode `400`) and accessed through the `Cylog`  `login` function.


```python
from geog0111.cylog import Cylog
help(Cylog.login)
```

    Help on function login in module geog0111.cylog:
    
    login(self, site=False, force=False)
        Reads encrypted information from ~/{dest_path}/.cylog.npz
        
        Keyword arguments
        ----------
        site = False (so self.site is default)
               string of anchor URL for site to associate with username and
               password
        force = False
               force password re-entry for site
        
        Returns
        --------
        A tuple containing plain text (username,password) for (site or self.site)
    


https://e4ftl01.cr.usgs.gov
   

https://urs.earthdata.nasa.gov/users/new


```python
from geog0111.gurlpath import URL
# ping small (1.3 M) test file
site='https://e4ftl01.cr.usgs.gov/'
test_dir='MOLA/MYD11_L2.006/2002.07.04'
test_file='MYD11_L2*0325*.hdf'
# this glob interprets the wildcards to get at a suitable test file
url = URL(site,test_dir).glob(test_file,verbose=False)[0]
# test ping returns True
assert url.ping(verbose=False) == True
```


```python

```

    
### Anaconda and Jupyter
    
We will be using software from the [anaconda distribution of python](https://anaconda.org/anaconda/python). This should already be installed for you if you are viewing this, but we can run some quick tests. Running the cell below (`>| Run`) should give, the following, or higher:
    
    jupyter core     : 4.6.1
    jupyter-notebook : 6.0.3
    ipython          : 7.12.0
    ipykernel        : 5.1.4
    jupyter client   : 5.3.4
    jupyter lab      : 1.2.6
    nbconvert        : 5.6.1
    ipywidgets       : 7.5.1
    nbformat         : 5.0.4
    traitlets        : 4.3.3
    conda 4.8.2
    Python 3.7.6
    
If that is not the case, then make a copy of what it does produce, and contact the course organisers through [moodle](https://moodle.ucl.ac.uk/course/view.php?id=21495). 




```bash
%%bash 
# tests 
jupyter --version
conda -V
python -V
```

    jupyter core     : 4.6.3
    jupyter-notebook : 6.1.3
    qtconsole        : 4.7.7
    ipython          : 7.18.1
    ipykernel        : 5.3.4
    jupyter client   : 6.1.7
    jupyter lab      : 2.2.7
    nbconvert        : 5.6.1
    ipywidgets       : 7.5.1
    nbformat         : 5.0.7
    traitlets        : 4.3.3
    conda 4.8.4
    Python 3.7.8


The code cell above that we ran is a [`unix` (`bash`) shell](https://en.wikipedia.org/wiki/Bash_(Unix_shell)), indicated by the [cell magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html) `%%bash` on the first line. This is a mechanism that lets us run unix commands in a Python notebook.

### Test

You will need a web login to NASA Earthdata and to have stored this using `cylog` according to [004_Accounts](004_Accounts.md) for the site `https://e4ftl01.cr.usgs.gov`. We can test this with the following code if you set do_test to True:


```python
from geog0111.modis import test_login
do_test = False
assert test_login(do_test,verbose=False)
```

If this fails, set `verbose` to `True` to see what is going on, then if you can;'t work it out from there, go back to [004_Accounts](004_Accounts.md) and sort the login for NASA Earthdata the site `https://e4ftl01.cr.usgs.gov`.

If you want to force the code to let you re-enter your credentials (e.g. you got it wrong before, or have changed them, or the test fails), then change the call to:

    cy = cylog(site,force=True)
    
and re-run.


```python

```
