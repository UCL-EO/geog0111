# Accounts and logins

## login and password

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


```python

```
