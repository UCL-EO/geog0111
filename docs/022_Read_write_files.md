# 022 Read and Write: URLs and files


## Introduction


### Purpose

In the previous session, we used [`pathlib`](https://docs.python.org/3/library/pathlib.html) and the local package [gurlpath](geog0111/gurlpath) derived from [`urlpath`](https://github.com/chrono-meter/urlpath) to open object streams from URLs and files. 

In this session, we will extend this to deal with reading and writing to text and binary files and URLs.

### Prerequisites

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

### Test

You should run a NASA account test](004_Accounts.md) if you have not already done so.

## Reading and writing

As before, we note that we can conveniently use `pathlib` to deal with file input and output. The main methods we have seen are:


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

Recall that the `write` functions (and `open` when used for write) write to local files, not to the URL. They have a keyword argument `local_file` to set the location to write the file to. If this is not given, the the directory structure of the URL is used (relative to the current directory). Alternatively, you can set the keyword `local_dir`, or set `URL.local_file` or `URL.local_dir` as appropriate. 

Note that `URL` is tolerant of calling with a `Path`: if we call `URL` with a local file, most operations will continue and apply the appropriate `Path` function.

## read and write text

We can read text from a file with `Path.read_text()` or from a URL with `URL.read_text()`, then either `Path.write_text()` or  `URL.write_text()` to write text to a file:


```python
from pathlib import Path
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

    wrote 90 bytes to work/easy.txt


#### Exercise 1

* Using `Path.read_text()` read the text from the file `work/easy.txt` and print the text returned.
* split the text into lines of text using `str.split()` at each newline, and print out the resulting list

You learned how to split strings in [013_Python_string_methods](013_Python_string_methods.md#split()-and-join())

We can show that we get the same result reading the same file locally from [`data/json-en.html`](data/json-en.html) or from the web from [`https://www.json.org/json-en.html`](https://www.json.org/json-en.html):


```python
from geog0111.gurlpath import URL
from pathlib import Path

# first read the data from URL with no cache
# and directory work
u = 'https://www.json.org/json-en.html'
url = URL(u,local_dir='work',verbose=True,noclobber=False)
data_url = url.read_text()

# then from file in directory data
data_file = Path('data/json-en.html').read_text()

assert data_url == data_file
print('files are the same')
```

    --> trying https://www.json.org/json-en.html


    files are the same


## read and write binary data

We can read binary data from a file with `Path.read_bytes()` or from a URL with `URL.read_bytes()`, then either `Path.write_bytes()` or  `URL.write_bytes()` to write the binary data to a file. Other than that, and the fact that we cannot directly visualise the contents of the binary files without some interpreted code, there is no real difference in how we treat them.


### MODIS

One of the deepest sources of geospatial information over the last two decades is that obtained from the NASA [MODIS](https://modis.gsfc.nasa.gov/data/dataprod/) products. We wiull make use of various MODIS datasets in this course.

As a start on this, let's first access a MODIS file from the web, as we did in [020_Python_files](020_Python_files.md). Here, the `kwargs` are passed on to `URL`:


```python
from  geog0111.modis import Modis

kwargs = {
    'verbose'    : True,
    'product'    : 'MCD15A3H',
    'db_dir'     : 'work',
    'local_dir'  : 'work',
}

modis = Modis(**kwargs)
url = modis.get_url(year="2020",month="01",day="01")[0]
```

    --> retrieving SDS MCD15A3H from database
    --> found SDS names in database
    --> ['FparExtra_QC', 'FparLai_QC', 'FparStdDev_500m', 'Fpar_500m', 'LaiStdDev_500m', 'Lai_500m']
    --> product MCD15A3H -> code MOTA
    --> getting database from command line
    --> retrieving query https://e4ftl01.cr.usgs.gov/MOTA from database
    --> got response from database for https://e4ftl01.cr.usgs.gov/MOTA
    --> discovered 1 files with pattern MOTA in https://e4ftl01.cr.usgs.gov/
    --> retrieving query https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006 from database
    --> got response from database for https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006
    --> discovered 1 files with pattern MCD15A3H.006 in https://e4ftl01.cr.usgs.gov/MOTA
    --> retrieving query https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01 from database
    --> got response from database for https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01
    --> discovered 1 files with pattern 2020.01.01 in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01
    --> parsing URLs from html file 1 items
    --> discovered 1 files with pattern MCD15A3H*.h08v06*.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01
    --> reading init file /home/ucfalew/.url_db/init.yml


We can access the binary data with `url.read_bytes()`, although we would normally want to use some package such as [`gdal`](https://gdal.org/) to interpret the data. 

Cached data will be used where available unless we set `noclobber=False`.


```python
b  = url.read_bytes()
print(f'data for {url} cached in {url.local()}')
print(f'dataset is {len(b)} bytes')
```

    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01/MCD15A3H.A2020001.h08v06.006.2020006032951.hdf
    --> code 401
    --> trying another
    --> getting login
    --> logging in to https://e4ftl01.cr.usgs.gov/
    --> data read from https://e4ftl01.cr.usgs.gov/
    --> code 200
    --> updated cache database in /shared/groups/jrole001/geog0111/work/database.db


    data for https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01/MCD15A3H.A2020001.h08v06.006.2020006032951.hdf cached in /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01/MCD15A3H.A2020001.h08v06.006.2020006032951.hdf.store
    dataset is 9067184 bytes


    --> retrieving data https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01/MCD15A3H.A2020001.h08v06.006.2020006032951.hdf from database
    --> local file /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01/MCD15A3H.A2020001.h08v06.006.2020006032951.hdf.store exists


We could explicitly write the data to a file, but since we are using a cache, there is no real point. This means that we can just use the URL to access the dataset. If we do need to specify the filename explicitly for any other codes, we can use `url.local()`.

#### Exercise 2

Using the code:

    kwargs = {
        'product'    : 'MCD15A3H',
        'db_dir'     : 'work',
        'local_dir'  : 'work',
    }

    modis = Modis(**kwargs)
    # get URLs
    hdf_urls = modis.get_url(year="2020",month="01",day="01")

* write a function called `get_locals` that loops over each entry in the list `hdf_urls` and returns the local filename 
* write code to test the function and print results using data from `modis.get_url("2020","01","*")`

### `gdal`


The MODIS files are in `hdf` format, and as we have noted, we do not generally want direct access to the raw (byte) information. Instead we must use some package to interpret the data. 

We can use the package [`gdal`](https://gdal.org/python/) to access information from these and other geospatial files. We will explore the contents of MODIS files in a later session, but for now, we can note that each MODIS file contains a set of sub datasets.

Basic use of `gdal` in this context is:

    g = gdal.Open(str(url.local()))
    
to convert the cached URL filename to a string, then to open the file in `gdal`. If this returns None, there has been a problem opening the file, so we might check that.

Then

    g.GetSubDatasets()
   
returns a list of sub-dataset information. Each item in the list is a tuple of two strings. In each, the first is the full name of the sub-dataset, and the second a text descriptor of the dataset. We call these `filename,name` below.

We read the dataset with:

    gdal.Open(filename).ReadAsArray()
    
In the illustration below, we will examine only the first sub-dataset `g.GetSubDatasets()[0]`.


```python
import gdal
from  geog0111.modis import Modis

# as before
kwargs = {
    'product'    : 'MCD15A3H',
    'db_dir'     : 'work',
    'local_dir'  : 'work',
}
modis = Modis(**kwargs)
url = modis.get_url(year="2020",month="01",day="01")[0]

# open
g = gdal.Open(str(url.local()))

if g:
    # get the first SDS only for illustration
    filename,name = g.GetSubDatasets()[0]
    print(f'dataset info is: {name}')
    # read the dataset
    data = gdal.Open(filename).ReadAsArray()
    print(f'dataset read is shape {data.shape} and type {type(data)}')
```

    dataset info is: [2400x2400] Fpar_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)
    dataset read is shape (2400, 2400) and type <class 'numpy.ndarray'>


#### Exercise 3

    name = '[2400x2400] Fpar_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)'

* Take the string variable `name` above, split it to obtain the second field (`Fpar_500m` here) and store this in a variable `sds_name`
* Write a function called `get_data` that reads an HDF (MODIS) filename, and returns a dictionary of all of the sub-datasets in the file, using `ReadAsArray()`. The dictionary keys should correspond to the items in  `sds_name` above.
* test the code by showing the keys in the dictionary returned and the shape of their dataset

You will need to recall how to split a string, that was covered in [013 Python string methods](013_Python_string_methods.md#split()-and-join()). You will also need to recall how to [loop over a dictionary](016_Python_for.md#looping-over-dictionaries,-and-assert). We saw how to find the shape of the dataset returned above (`.shape`).

## Summary

In this section, we have used `Path` and `URL` classes to read and write text and binary files. We have combined these ideas with earlier work to access MODIS datafiles and other text and binary datasets. For data we access through a URL, we can do file operations on a cached version of the file. We have refreshed our memory of some of the earlier material, especially string formatting.

We have learned how to use `gdal` to look at the sub-datasets in an HDF file and also how to read them.

You should now have some confidence in these matters, so that if you were set a task of downloading and saving datasets, as well as other tasks such as finding their size, whether the exists or not, you could do this. 
