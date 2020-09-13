## 022 Read Files


### Introduction


#### Purpose

In this session, we will learn how to read files and similar resources. We will mainly use [`pathlib`](https://docs.python.org/3/library/pathlib.html) and the local package [gurlpath](geog0111/gurlpath) derived from [`urlpath`](https://github.com/chrono-meter/urlpath). We will also cover opening and closing files, and some simple read- and write-operations.


#### Prerequisites

You will need some understanding of the following:


* [001 Using Notebooks](001_Notebook_use.md)
* [002 Unix](002_Unix.md) with a good familiarity with the UNIX commands we have been through.
* [003 Getting help](003_Help.md)
* [010 Variables, comments and print()](010_Python_Introduction.md)
* [011 Data types](011_Python_data_types.md) 
* [012 String formatting](012_Python_strings.md)
* [013_Python_string_methods](013_Python_string_methods.md)
* [020_Python_files](020_Python_files.md)

You will need to recall details from [020_Python_files](020_Python_files.md) on using the two packages.


#### Test
You will need a web login to NASA Earthdata and to have stored this using `cylog` according to [004_Accounts](004_Accounts.md) for the site `https://e4ftl01.cr.usgs.gov`. We can test this with the following code ius yoiu set do_test to True:


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

If this fails, set `verbose` to `True` to see what is going on, then if you can;'t work it out from there, go back to [004_Accounts](004_Accounts.md) and sort the login for NASA Earthdata the site `https://e4ftl01.cr.usgs.gov`.

### Reading and writing

We can conveniently use `pathlib` to deal with file input and output. The main methods to be aware of are:


|command|  purpose|
|---|---|
|`Path.open()`| open a file and return a file descriptor|
|`Path.read_text()`|  read text|
|`Path.write_text()`| write text|
|`Path.read_bytes()`| read byte data|
|`Path.write_bytes()`| write byte data|


For `gurlpath` we have the following equivalent functions:





|command|  purpose|
|---|---|
|`URL.open()`| open a file descriptor with data from a URL|
|`URL.read_text()`|  read text from URL|
|`URL.write_text()`| write text to file|
|`URL.read_bytes()`| read byte data from URL|
|`URL.write_bytes()`| write byte data to file|

Notice that the `write` functions (and `open` when used for write) write to local files, not to the URL. 

They have a keyword argument `local_file` to set the location to write the file to. If this is not given, the the directory structure of the URL is used (relative to the current directory). Alternatively, you can settrhe keyword `local_dr`, or set `URL.local_file` or `URL.local_dir` as appropriate. 

Note that `URL` is tolerant of calling with a `Path`: if we call `URL` with a local file, most operations will continue and apply the appropriate `Path` function.

#### `with ... as ...`, `Path.open`, `URL.open`, `yaml`, `json`

Quite often, we will use specific packages for reading particular file formats. But often we just need to be able to open a file (to get a file descriptor) or just to read some binary of text data from a file, or write straight binary of text data to a file. We use this suite of functions given above for such taskas. 

The first of these, `Path.open` provides a file descriptor for the open file. This is used to interface to other input/output functions in Python. A typical example of this is reading a configuration file in [`yaml` format](http://zetcode.com/python/yaml/).

The usual way of opening a file to get the file descriptor is:

    with Path(filename).open('r') as f:
       # do some reading with f
       pass
       

We use the form `with ... as ...` here, so that the file descriptor `f` only exists within this construct and the file is automatically closed when we finish. Codes are spaced in inside the construct, as we have seen in `if ...` or `for ... in ...` constructs.

Here, we have set the flag `r` within the `open()` statement (this is the default mode). This means that the file will be opened for *reading* only. Alternatives include `w` for writing, or `w+` for appending.

In the following example, we use `Path` to open the file [`bin/copy/environment.yml`](bin/copy/environment.yml) and read it using the `yaml` library. This file specifies which packages are loaded in our Python environment. It has a simple ascii format, but since it is a `yaml` file, we should read it with code that interprets the format correctly and safely into a dictionary. This is done using `yaml.safe_load(f)` with `f` an open file descriptor.


```python
from pathlib import Path
import yaml

# form the file name
yaml_file = Path('bin','copy','environment.yml')

with yaml_file.open('r') as f:
    env = yaml.safe_load(f)

print(f'env is type {type(env)}')
print(f'env keys: {env.keys()}')
```

The equivalent, reading the data from a URL is:


```python
from geog0111.gurlpath import URL
import yaml

# form the file name
site = 'https://raw.githubusercontent.com'
site_dir = '/UCL-EO/geog0111/master'
site_file = 'copy/environment.yml'
yaml_file = URL(site,site_dir,site_file)

# notice that we can use verbose=True for URL open
with yaml_file.open('r',verbose=True) as f:
    env = yaml.safe_load(f)

print(f'env is type {type(env)}')
print(f'env keys: {env.keys()}')
```

Another common file format for configuration information is [`json`](https://www.json.org/json-en.html). We can use the same form of code as above to write the information in `env` into a `json` format file:


```python
from pathlib import Path
import json

# form the file name
json_file = Path('bin','copy','environment.json')

with json_file.open('w') as f:
    json.dump(env, f)
```

### read and write text

We can read text from a file with `Path.read_text()` or from a URL with `URL.read_text()`, then either `Path.write_text()` or  `URL.write_text()` to write text to a file:


```python
# from https://www.json.org
some_text = '''
It is easy for humans to read and write.
It is easy for machines to parse and generate. 
'''

# set up the filename
outfile = Path('work/easy.txt')
# write the text
nbytes = outfile.write_text(some_text)
# print what we did
print(f'wrote {nbytes} bytes to {outfile}')
```

##### Exercise 1

* Using `Path.read_text()` read the text from the file `work/easy.txt` and print the text returned.
* split the text into lines of text using `str.split()` at each newline, and print out the resulting list

You learned how to split strings in [013_Python_string_methods](013_Python_string_methods.md#split()-and-join())

We can show that we get the same result reading the same file locally or from the web:


```python
from geog0111.gurlpath import URL
from pathlib import Path

# first read the data
u = 'https://www.json.org/json-en.html'
url = URL(u)
# set the output dir
url.local_dir='data'

data = url.read_text(verbose=False)

# write to 'data/json-en.html' with URL
osize = url.write_text(data)
# test the correct number of bytes
assert osize == 26718
print('passed URL')

# write to 'data/json-en.html' with Path
osize = Path('data/json-en.html').write_text(data)
# test the correct number of bytes
assert osize == 26718
print('passed Path')

```

The `URL` class has a few advantages over using `Path` in this way:

* if the output directory doesn't already exist, it will be created
* if we set a `noclobber=True` flag, then we will not try to write the file if it already exists.

For example:


```python
from geog0111.gurlpath import URL
from pathlib import Path

# first read the data
u = 'https://www.json.org/json-en.html'
url = URL(u)
url.local_dir='data'

data = url.read_text()

# write to 'data/json-en.html' with URL
osize = url.write_text(data,verbose=True,noclobber=True)
```

##### Exercise 2

XXX TODO XXX

### read and write binary data

We can read binary data from a file with `Path.read_bytes()` or from a URL with `URL.read_bytes()`, then either `Path.write_bytes()` or  `URL.write_bytes()` to write the binary data to a file.

Let's first access a MODIS file from the web, as we did in [020_Python_files](020_Python_files.md):


```python
from  geog0111.modis import Modis

modis = Modis('MCD15A3H',verbose=True)
url = modis.get_url("2020","01","01")[0]
```

Now, pull the dataset 


```python
# set the output directory
url.local_dir = 'work'
# read the dataset
hdf_data = url.read_bytes()
# and save to a file
obytes = url.write_bytes(hdf_data,verbose=True)
```

##### Exercise 3

Using the code:
    
    from  geog0111.modis import Modis

    # get URL
    modis = Modis('MCD15A3H',verbose=True)
    url = modis.get_url("2020","01","01")[0]
    # set the output directory
    url.local_dir = 'work'
    
    # read the dataset
    hdf_data = url.read_bytes()
    # and save to a file
    obytes = url.write_bytes(hdf_data,verbose=True)    

* write a function that only calls `url.read_bytes()` if the file doesn't already exist
* If it already exists, just read the data from that file
* test your code with the url generated above and show that the file size is 9067184 bytes

You will need to remember how to get the filename from the URL object, and also to test if a file exists. We learned all of these in [020_Python_files](020_Python_files.md).

Note that `len(data)` will give the size of bytes data.

##### Exercise 4

* print out the absolute pathname of the directory that the binary file [`images/ucl.png`](images/ucl.png) is in
* print the size of the file in kilobytes (KB) to two decimal places without reading the datafile. 
* read the datafile, and check you get the same data size

You will need to recall how to find a file size in bytes using `Path`. This was covered in [020_Python_files](020_Python_files.md). You will need to know how many bytes are in a KB. To print to two decimal places, you need to recall the string formatting we did in [012_Python_strings](012_Python_strings.md#String-formating).

### Summary

In this section, we have used `Path` and `URL` classes to read and write text and binary files. We have combined these ideas with earlier work to download and save a MODIS datafile and other text and binary datasets. We have refreshed our memory of some of the earlier material, especially string formatting.

You should now have some confidence in these matters, so that if you were set a task of downloading and saving datasets, as well as other tasks such as finding their size, whether the exists or not, you could do this. 
