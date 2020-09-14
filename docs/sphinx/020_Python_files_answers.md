# 020 Files and other Resources : Answers to exercises

#### Exercise 1

There is a file called `environment.yml` in the directory `copy`.

* use `Path` to generate the a variable `copy_dir` containing the pathname of the `copy` directory
* create a variable `env_file` which adds add the file `environment.yml` to this 
* check to see if the file exists


```python
from pathlib import Path
# ANSWER

# There is a file called environment.yml in the directory copy.
# use Path to generate the a variable copy_dir containing the 
# pathname of the copy directory
copy_dir = Path('copy')

# create a variable env_file which adds add the file 
# environment.yml to this
env_file = copy_dir / 'environment.yml'
# or
env_file = Path(copy_dir,'environment.yml')

# check to see if the file exists
print(f'does {env_file} exist? {env_file.exists()}')
```

    does copy/environment.yml exist? True



```python
# ANSWER

# There is a file called environment.yml 
# in the directory copy.md_checkpoints/

# use `Path` to generate the a variable `copy_dir` 
# containing the pathname of the `copy` directory
copy_dir = Path('copy')

# create a variable `env_file` which adds add the file 
# `environment.yml` to this 
env_file = Path(copy_dir,'environment.yml')
# or
env_file = copy_dir/'environment.yml'

# check to see if the file exists
print(f'Does {env_file} exist? {env_file.exists()}')
```

    Does copy/environment.yml exist? True


#### Exercise 2

* Use `Path` to show the file permissions of all files that end `.sh` in the directory `bin`


```python
# ANSWER
# use glob to get a list of filenames in the directory bin 
# that end with .sh -> pattern n* using a wildcard
filenames = Path('bin').glob('n*')

# loop over the filenames and print the permissions
# as octal. Note how we use :25s to line items up
for f in filenames:
    print(f'{str(f):25s} : {oct(f.stat().st_mode)}')
```

    bin/notebook-mkdocs.sh    : 0o100755
    bin/notebook-run.sh       : 0o100755



```python
# ANSWER
# Use Path to show the file permissions of
# all files that end .sh in the directory bin

# use glob to get a list of filenames in the directory bin 
# that end with .sh -> pattern *.sh using a wildcard
filenames = Path('bin').glob('*.sh')
# loop over the filenames
for f in filenames:
    print(f)
```

    bin/notebook-mkdocs.sh
    bin/setup.sh
    bin/notebook-run.sh
    bin/link-set.sh
    bin/git-remove-all.sh


#### Exercise 3

* print out the absolute pathname of the directory that `images/ucl.png` is in
* check that the file exists
* if it does, print the size of the file in KB to two decimal places

You will need to know how many Bytes in a Kilobyte, and how to [format a string to two decimal places](012_Python_strings.md#String-formating). You will also need to remember how to use [`if` statements](015_Python_control.md#Comparison-Operators-and-if).


```python
# ANSWER

# print out the absolute pathname of the 
# directory that images/ucl.png is in
ucl = Path('images','ucl.png')

# use absolute and parent
# Use name to show how that is helpful
print(f'The directory {ucl.name} is in is: {ucl.absolute().parent}')

# check that the file exists
# if it does ...
if ucl.exists():
    # print the size of the file in KB to two decimal places

    # from above, use stat().st_size
    size_in_bytes = ucl.stat().st_size
    # 1024 Bytes -> 1 KB
    size_in_KB = size_in_bytes/1024
    # 2 dp -> : .2f
    print(f'file size {size_in_bytes} Bytes -> {size_in_KB : .2f} KB')
else:
    print(f'file does not exist')
```

    The directory ucl.png is in is: /Users/plewis/Documents/GitHub/geog0111/notebooks/images
    file size 1956 Bytes ->  1.91 KB


#### Exercise 4

* create a `URL` object for the file `table.html` in the directory `psd/enso/mei/` on the site `http://www.esrl.noaa.gov/`.
* print out the url and check it is `table.html`


```python
# ANSWER

# create a URL object for the file table.html 
# in the directory psd/enso/mei/ on the site 
# http://www.esrl.noaa.gov/.

site = 'http://www.esrl.noaa.gov/'
site_dir = 'psd/enso/mei'
site_file = 'table.html'
url = URL(site,site_dir,site_file)

# print out the url and check it is table.html
print(url)
assert url.name == site_file
print('passed')
```

    http://www.esrl.noaa.gov/psd/enso/mei/table.html
    passed


#### Exercise 5

based on the code from above:

    # settings
    product = 'MCD15A3H'
    year, month, day = '2020', '06', '01'
    tile = 'h08v06'

    # url with wildcards
    site = 'https://e4ftl01.cr.usgs.gov'
    site_dir = f'MOTA/{product}.006/{year}.{month}.{day}'
    site_file = f'*.{tile}*.hdf'

    # get the information
    url = URL(site,site_dir)
    hdf_urls = list(url.glob(site_file,verbose=True))[0]
    
 * write a function called `modis_dataset` with arguments corresponding to the settings above
 * the function should return the URL objects of the NASA datasets specified by your arguments
 * your function should be fully documented and include some error checks
 * run a test of your function, and print the file size in MB for the file pointed to in the URL to 2 decimal places
 * what happens if you use a wildcard for the date?


```python
from geog0111.gurlpath import URL

# ANSWER 1

# write a function called `modis_dataset` 
# with arguments corresponding to the settings above
#
# the function should return the URL objects of 
# the NASA datasets specified by your arguments
#
def modis_dataset(product, tile, year, month, day,
                  verbose=False,
                  site='https://e4ftl01.cr.usgs.gov'):
    '''
    Get URL object list for NASA MODIS products
    for the specified product, tile, year, month, day
    
    Positional Arguments:
     
    product : str e.g. 'MCD15A3H'
    tile    : str e.g. 'h08v06'
    year    : str valid 2000-present
    month   : str 01-12
    day     : str 01-(28,29,30,31)
    
    Keyword Arguments:
    
    site     =  'https://e4ftl01.cr.usgs.gov'
    verbose  =  False
    '''
    # you should put some tests in
    site_dir = f'MOTA/{product}.006/{year}.{month}.{day}'

    site_file = f'*.{tile}*.hdf'

    url = URL(site,site_dir)
    hdf_urls = url.glob(site_file,verbose=verbose)
    return hdf_urls 
```


```python
# ANSWER 2
# run a test of your function, 
# and print the file size in MB 
# for the file pointed to in the URL
# to 2 decimal places

msg = '''
Note: 1 MB = 1024 * 1024 Bytes
'''
print(msg)

args = ['MCD15A3H','h08v06','2020','06', '01']
hdf_urls = modis_dataset(*args,verbose=True)
# test if exist
for u in hdf_urls:
    print(f'{u.name} : {u.stat().st_size/(1024*1024): .2f} MB')
```

    --> wildcards in: ['*.h08v06*.hdf']
    --> level 0/1 : *.h08v06*.hdf
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.01


    
    Note: 1 MB = 1024 * 1024 Bytes
    


    --> discovered 1 files with pattern *.h08v06*.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.01


    MCD15A3H.A2020153.h08v06.006.2020160231732.hdf :  9.66 MB



```python
# ANSWER 3
# what happens if you use a wildcard for the date?
msg = '''
Note: 1 MB = 1024 * 1024 Bytes
'''
print(msg)

args = ['MCD15A3H','h08v06','2020','*', '01']
hdf_urls = modis_dataset(*args,verbose=True)
# test if exist
for u in hdf_urls:
    print(f'{u.name} : {u.stat().st_size/(1024*1024): .2f} MB')
```

    
    Note: 1 MB = 1024 * 1024 Bytes
    


    --> wildcards in: ['2020.*.01' '*.h08v06*.hdf']
    --> level 0/2 : 2020.*.01
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006
    --> discovered 4 files with pattern 2020.*.01 in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006
    --> level 1/2 : *.h08v06*.hdf
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01
    --> discovered 1 files with pattern *.h08v06*.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.03.01
    --> discovered 1 files with pattern *.h08v06*.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.03.01
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.01
    --> discovered 1 files with pattern *.h08v06*.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.01
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.09.01
    --> discovered 1 files with pattern *.h08v06*.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.09.01


    MCD15A3H.A2020001.h08v06.006.2020006032951.hdf :  8.65 MB
    MCD15A3H.A2020061.h08v06.006.2020066032716.hdf :  8.63 MB
    MCD15A3H.A2020153.h08v06.006.2020160231732.hdf :  9.66 MB
    MCD15A3H.A2020245.h08v06.006.2020253152835.hdf :  10.46 MB

