# 021 Read and Write: URLs and files


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

You should run a [NASA account test](notebooks/004_Accounts.md#Test) if you have not already done so.

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


#### Exercise 1

* Using `Path.read_text()` read the text from the file `work/easy.txt` and print the text returned.
* split the text into lines of text using `str.split()` at each newline, and print out the resulting list

You learned how to split strings in [013_Python_string_methods](013_Python_string_methods.md#split()-and-join())

We can show that we get the same result reading the same file locally from [`data/json-en.html`](data/json-en.html) or from the web from [`https://www.json.org/json-en.html`](https://www.json.org/json-en.html):


```python
from geog0111.gurlpath import URL
from pathlib import Path

# first read the data
u = 'https://www.json.org/json-en.html'
url = URL(u)
# set the output dir
url.local_dir='data'

data = url.read_text()
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

    passed URL
    passed Path


The `URL` class has a few advantages over using `Path` in this way:

* if the output directory doesn't already exist, it will be created
* by default, it caches files. 

This latter point means that if were intending to read some file from a URL and store it, then the next time we make the same call, it will read from the saved (cached) file instead of trying to download it. To avoid the problem where cached files may have been partially downloaded or otherwise corrupted, the library checks the local file size against what it expects from the URL.

Caching can be turned off by specifying:

    `noclobber=Fakse`
    
and file size testing can be disabled with:

    `size_check=False`
    
It is generally a good idea to keep `size_check=True`, although for some files (e.g. large, password-protected files) getting the file size can take a not inconsiderable amount of time. Further, we cannot easily determine the remote file size in all cases (e.g. for compressed files that are uncompressed on download).

You can specify a location for cached files by setting e.g.:

    url.local_dir='data'
    
as above. 

We can follow the logic of the file check if we switch on `verbose=True`:


```python
from geog0111.gurlpath import URL
from pathlib import Path

# first read the data
u = 'https://www.json.org/json-en.html'
url = URL(u)
# cache file here when read
url.local_dir='data'

data = url.read_text(verbose=True)

# write to 'data/json-en.html' with URL
# but this is where we cached it on reading
osize = url.write_text(data,verbose=True)
```

    --> existing file data/json-en.html 26880 Bytes
    --> noclobber: True
    --> keeping existing file data/json-en.html
    --> local file: data/json-en.html
    --> trying https://www.json.org/json-en.html
    --> code 200
    --> file is compressed, remote size not directly available
    --> code 200
    --> noclobber: True
    --> not downloading file
    --> opening already downloaded file
    --> existing file data/json-en.html 26880 Bytes
    --> noclobber: True
    --> keeping existing file data/json-en.html
    --> existing file data/json-en.html 26880 Bytes
    --> noclobber: True
    --> keeping existing file data/json-en.html
    --> local file: data/json-en.html
    --> trying https://www.json.org/json-en.html
    --> code 200
    --> file is compressed, remote size not directly available
    --> code 200
    --> noclobber: True
    --> not downloading file
    --> get download? False
    --> opening already downloaded file
    --> existing file data/json-en.html 26880 Bytes
    --> noclobber: True
    --> keeping existing file data/json-en.html


## read and write binary data

We can read binary data from a file with `Path.read_bytes()` or from a URL with `URL.read_bytes()`, then either `Path.write_bytes()` or  `URL.write_bytes()` to write the binary data to a file. Other than that, and the fact that we cannot directly visualise the contents of the binary files without some interpreted code, there is no real difference in how we treat them.

Let's first access a MODIS file from the web, as we did in [020_Python_files](020_Python_files.md):


```python
from  geog0111.modis import Modis

modis = Modis('MCD15A3H',verbose=True)
url = modis.get_url("2020","01","01")[0]
```

    --> wildcards in: ['*.h08v06*.hdf']
    --> level 0/1 : *.h08v06*.hdf
    --> local file: MOTA/MCD15A3H.006/2020.01.01
    --> local file MOTA/MCD15A3H.006/2020.01.01 does not exist
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01
    --> discovered 1 files with pattern *.h08v06*.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01


Now, pull the dataset (or keep the cached version)


```python
# set the output directory
url.local_dir = 'work'
# read the dataset
hdf_data = url.read_bytes(size_check=False)
# and save to a file
obytes = url.write_bytes(hdf_data,size_check=False)
print(f'{obytes} Bytes')
```

    9067184 Bytes


#### Exercise 2

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

#### Exercise 3

* print out the absolute pathname of the directory that the binary file [`images/ucl.png`](images/ucl.png) is in
* print the size of the file in kilobytes (KB) to two decimal places without reading the datafile. 
* read the datafile, and check you get the same data size

You will need to recall how to find a file size in bytes using `Path`. This was covered in [020_Python_files](020_Python_files.md). You will need to know how many bytes are in a KB. To print to two decimal places, you need to recall the string formatting we did in [012_Python_strings](012_Python_strings.md#String-formating).

## Summary

In this section, we have used `Path` and `URL` classes to read and write text and binary files. We have combined these ideas with earlier work to download and save a MODIS datafile and other text and binary datasets. We have refreshed our memory of some of the earlier material, especially string formatting.

You should now have some confidence in these matters, so that if you were set a task of downloading and saving datasets, as well as other tasks such as finding their size, whether the exists or not, you could do this. 
