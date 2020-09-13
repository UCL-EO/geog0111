## 021 Files and other Resources : Answers to exercises

##### Exercise 1

There is a file called `environment.yml` in the directory `copy`.md_checkpoints/

* use `Path` to generate the a variable `copy_dir` containing the pathname of the `copy` directory
* create a variable `env_file` which adds add the file `environment.yml` to this 
* check to see if the file exists


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


##### Exercise 2

* Use `Path` to show the file permissions of all files that end `.sh` in the directory `bin`


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


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-0127f4245e30> in <module>
          5 # use glob to get a list of filenames in the directory bin
          6 # that end with .sh -> pattern *.sh using a wildcard
    ----> 7 filenames = Path('bin').glob('*.sh')
          8 # loop over the filenames
          9 for f in filenames:


    NameError: name 'Path' is not defined


##### Exercise 3

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



```python
# ANSWER
# Using Path.read_text() read the text from the file work/easy.txt 
# and print the text returned.

# set up the filename
infile = Path('work','easy.txt')
# read the text
read_text = infile.read_text()

# split the text into lines of 
# text using str.split() at each newline, 
# and print out the resulting list
lines = read_text.split('\n')
print(lines)
```

    ['', 'It is easy for humans to read and write.', 'It is easy for machines to parse and generate. ', '']


##### Exercise 4

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



```python
# ANSWER
import json

# show the size of the files 
# bin/copy/environment.json and bin/copy/environment.yml

# form the file names
json_file = Path('bin','copy','environment.json')
yaml_file = Path('bin','copy','environment.yml')
# loop and print size
for f in [json_file,yaml_file]:
    print(f'{f} : {f.stat().st_size} bytes')
```

    bin/copy/environment.json : 791 bytes
    bin/copy/environment.yml : 856 bytes



```python
from geog0111.gurlpath import URL

# ANSWER

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
# ANSWER 1
# run a test of your function, and check that 
# the file pointed to in the URL exists and is accessible

args = ['MCD15A3H','h08v06','2020','06', '01']
hdf_urls = modis_dataset(*args,verbose=True)
# test if exist
for u in hdf_urls:
    print(f'{u.name} : {u.exists()}')
```

    --> wildcards in: ['*.h08v06*.hdf']
    --> level 0/1 : *.h08v06*.hdf
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.01


    MCD15A3H.A2020153.h08v06.006.2020160231732.hdf : True



```python
# ANSWER 2
# run a test of your function, and check that 
# mis-specify date and see that it fails
# use '1' instead of '01'

args = ['MCD15A3H','h08v06','2020','06', '1']
hdf_urls = modis_dataset(*args,verbose=True)
# test if exist
for u in hdf_urls:
    print(f'{u.name} : {u.exists()}')
```

    --> wildcards in: ['*.h08v06*.hdf']
    --> level 0/1 : *.h08v06*.hdf
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.1



```python
# ANSWER 3
# what happens if you use a wildcard for the date?
args = ['MCD15A3H','h08v06','2020','06', '*']
hdf_urls = modis_dataset(*args,verbose=True)
# test if exist
for u in hdf_urls:
    print(f'{u.name} : {u.exists()}')
```

    --> wildcards in: ['2020.06.*' '*.h08v06*.hdf']
    --> level 0/2 : 2020.06.*
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006
    --> level 1/2 : *.h08v06*.hdf
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.01
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.05
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.09
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.13
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.17
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.21
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.25
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.29


    MCD15A3H.A2020153.h08v06.006.2020160231732.hdf : True
    MCD15A3H.A2020157.h08v06.006.2020162035120.hdf : True
    MCD15A3H.A2020161.h08v06.006.2020167041028.hdf : True
    MCD15A3H.A2020165.h08v06.006.2020170044117.hdf : True
    MCD15A3H.A2020169.h08v06.006.2020174041553.hdf : True
    MCD15A3H.A2020173.h08v06.006.2020178032155.hdf : True
    MCD15A3H.A2020177.h08v06.006.2020182190226.hdf : True
    MCD15A3H.A2020181.h08v06.006.2020188194909.hdf : True



```python
# ANSWER 4
msg = '''
what happens if you use a wildcard for the date?

It accepts wildcards for anywhere in the directory path.
This is very useful for gathering datasets!
'''
print(msg)
```

    
    what happens if you use a wildcard for the date?
    
    It accepts wildcards for anywhere in the directory path.
    This is very useful for gathering datasets!
    

