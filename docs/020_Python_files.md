# 020 Files and other Resources


## Introduction



### Purpose

In this session, we will learn about files and similar resources. We will introduce the standard Python library [`pathlib`](https://docs.python.org/3/library/pathlib.html) which is how we deal with file paths, as well as the local package [gurlpath](geog0111/gurlpath) derived from [`urlpath`](https://github.com/chrono-meter/urlpath) that allows a similar object-oriented approach with files and other objects on the web. We will also cover opening and closing files, and some simple read- and write-operations.



### Prerequisites

You will need some understanding of the following:


* [001 Using Notebooks](001_Notebook_use.md)
* [002 Unix](002_Unix.md) with a good familiarity with the UNIX commands we have been through.
* [003 Getting help](003_Help.md)
* [010 Variables, comments and print()](010_Python_Introduction.md)
* [011 Data types](011_Python_data_types.md) 
* [012 String formatting](012_Python_strings.md)
* [013_Python_string_methods](013_Python_string_methods.md)



### Timing

The session should take around 40 minutes.

## Data resources

### Resource location

We store information on a computer in files, or file-like resources. We will use the term 'file' below to mean either of these concepts, other than specific issues relating to particular types of file/resource.

To get information from files, we need to be able to specify some **address** for the file/resource location, along with some way of interacting with the file. These concepts are captured in the idea of a [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) (Uniform Resource Indicator). You will most likely have come across the related idea of a [Uniform Resource Locator (URL)](https://en.wikipedia.org/wiki/URL), which is a URL such as [https://www.geog.ucl.ac.uk/people/academic-staff/philip-lewis](https://www.geog.ucl.ac.uk/people/academic-staff/philip-lewis)
that gives:

* the location of the resource: `people/academic-staff/philip-lewis`
* the access and interpretation protocol: [`https`](https://en.wikipedia.org/wiki/HTTPS) (secure [`http`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol))
* the network domain name: [`www.geog.ucl.ac.uk`](https://www.geog.ucl.ac.uk)

When we visit this URL using an appropriate tool such as a browser, the tool can access and interpret the information in the resource: in this case, interpret the [html code](https://www.w3schools.com/html) in the file pointed to by the URL.

Similarly, we will be used to the idea of accessing `files` on the computer. These may be in the local file system, or on some network or cloud storage that might be accessible from the local file system. An example of such a file would be some Python code file such as 
[`geog0111/helloWorld.py`](http://localhost:8888/edit/notebooks/geog0111/helloWorld.py).


### binary and text data

It is useful at this point to distinguish text (ASCII) and binary resources. Text resources are in a human-readable format, so you can just directly 'look at' the file contents to see what is there. Examples of this are [csv-format](https://en.wikipedia.org/wiki/Comma-separated_values) files, [html pages](https://en.wikipedia.org/wiki/HTML), [yaml](https://en.wikipedia.org/wiki/YAML) or [json](https://en.wikipedia.org/wiki/JSON) configuration files, and even these [Jupyter notebooks](https://jupyter.org/). 

Information in text files is, as noted, easily readable: you can open the file in any text editor to see the contents. However, for large datasets, and datasets with particular structures (e.g. on grids), it is very inefficient.

Typical **binary** files include (most) image data and compressed data (e.g. [zip](https://en.wikipedia.org/wiki/Zip_(file_format)) files), where size is more important, as well as encrypted data, where human-readability might not be desirable.

Text files designed for different purposes will mostly have some format definition or conventions. This means that although we can easily scan e.g. a [json file](https://json.org/example.html`), there is a set way of laying such files out, so we can interpret them by eye or in software.

Binary files will also have some defined format, but in this case, the user is generally forced to use some software reader to interpret the data correctly.

When you wish to access some file or dataset, you will generally know which format the file will be in, so can target an appropriate reader. Quite often though, we have to we might need to examine a dataset before deciding on some parameters for an interpreter, particularly with text datasets. 

In these notes, we will learn how to access and use binary and text datasets in Python, but from the local file system, and online from URLs.

We first need to learn some core tools for file and URL access. We will be using the object-oriented [`pathlib`](https://docs.python.org/3/library/pathlib.html) package for local files, and a local variant of [`urlpath`](https://github.com/chrono-meter/urlpath) called [`gurlpath`](geog0111/gurlpath.py).

We will be also using `yaml`, `json` and [`pandas`](https://pandas.pydata.org/) packages for reading particular text file types, and introducing [`gdal`](https://gdal.org/python/) for binary image files.

## `Path` `import`

`Path` is part of the `pathlib` package, so in any Python codes, we first must import this into our workspace:


```python
from pathlib import Path
```

This imports the module `Path` from the library `pathlib`.

We may repeat this `import` in the codes below, for illustration purposes. You need only import it once in any file or session though. 

### `posix`

The main class we will use from `pathlib` is `Path`. This provides an object-oriented way of dealing with files and paths, that is portable to any operating system. Recall from [002 Unix](002_Unix.md) that unix-like operating systems use `posix` filenames, separated by forward slash `/` (or just *slash*). Windows uses a backslash `\`. But *we* want to write Python codes that are generic and shouldn't need to greatly worry about such issues. Using `Path` greatly helps in this regard, though there will always the occasional time we do need to distinguish `posix` and non-`posix` systems.



### Common `Path` methods

We can start with a table of [commonly-used methods](https://stackabuse.com/introduction-to-the-python-pathlib-module/#:~:text=The%20Pathlib%20module%20can%20deal,(usually%20the%20current%20directory).) using `Path` and give their [Unix equivalents](002_Unix.md), most of which we have already learned.

|command| unix-equivalent | purpose|
|---|---|---|
|`Path.cwd()`| `pwd` |Return path object representing the current working directory|
|`Path.home()`| `~`| Return path object representing the home directory|
|`Path.stat()`| `ls -l`* | return info about the path|
|`Path.chmod()`| `chmod` | change file mode and permissions|
|`Path.glob(pattern)`| `ls *` | Glob the pattern given in the directory that is represented by the path, yielding matching files of any kind|
|`Path.mkdir()`| `mkdir` | to create a new directory at the given path|
|`Path.rename()`| `mv` | Rename a file or directory to the given target|
|`Path.rmdir()`| `rmdir` | Remove the empty directory|
|`Path.unlink()`| `rm` | Remove the file or symbolic link|

`*` Really, `Path.stat()` equates to the `unix` command `stat`, but this contains the information we access using `ls -l`.

Since we are already familiar with most of these commands in `unix`, we can get straight into using them:


```python
from pathlib import Path

print(f'I am in directory {Path.cwd()}')
print(f'My home is {Path.home()}')
```

To keep the filenames generic, we form a filename using `Path()`, so `Path('bin','README')` would refer to the filename `bin/README` on a `posix` system, and `bin/README` on Windows.

### File information

The file permissions format we are used to from `ls -l` is accessed through `filename.stat().st_mode` but needs to be converted to octal to match to `ls`

    oct(filename.stat().st_mode)


```python
# similar information to ls -l
readme=Path('bin','README')
print(f'README file is {readme}')
print(f'       size is {readme.stat().st_size} bytes')
print(f'       mode is {oct(readme.stat().st_mode)}')
print(f'      owner is {readme.owner()}')
```

### `glob` generators 

To use a wildcard (or any pattern) to refer to a list of files, we use `Path.glob()` (or `Path.rglob()` for a recursive list). This function returns a generator, which is a special type of list whereby the items in the list are produced on demand (as we use them).


```python
# use glob to get a list of filenames in the directory bin 
# that end with .sh -> pattern *.sh using a wildcard
filenames = Path('bin').glob('*.sh')
```

The generator does not have all of the attributes of a list, so we cannot, for example, know the length, withjout first converting it tot a list. It is intended that you step through it one item at a time. This is usually done in a `for` loop, or similar construct:


```python
for i,f in enumerate(filenames):
    print(f'file {i} is {f}')
```

The advantage of a generator is that it will generally need less memory than fully calculating all items in a list. Once we move on to the next item in the generator, any memory used by current item is freed.

But is the size of objects is small, you will not notice much impact if you convert the generator to a list. 


```python
filenames = list(Path('bin').glob('*.sh'))
print(filenames)
```

    [PosixPath('bin/notebook-mkdocs.sh'), PosixPath('bin/setup.sh'), PosixPath('bin/notebook-run.sh'), PosixPath('bin/link-set.sh'), PosixPath('bin/git-remove-all.sh')]


Let's use `glob` now to get the file permissions of each file `n*` in the directory `bin`:


```python
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


#### Exercise 1

* Use `Path` to show the file permissions of all files that end `.sh` in the directory `bin`

### `absolute` `parts` `name` `parent`

We can use `Path` to convert filenames between relative and absolute representations using `absolute()` and `relative_to()`:


```python
print(f'I am in {Path.cwd()}')

# define a relative path name
readme=Path('bin','README')
print(f'original relative name:\n\t{readme}')

# convert to absolute
readme = readme.absolute()
print(f'absolute name:\n\t{readme}')

# now make a relative pathname, 
# reletive to current working directory
readme = readme.relative_to(Path.cwd())
print(f'name relative to {Path.cwd()}:\n\t{readme}')
```

Quite often we need to split some filename up into its constituent parts. This is achieved with `paths` which gives a list of the file name tree:


```python
readme=Path('bin','README')
print(readme.parts)
```

We could use that to get at the filename `README` from the last item in the list, but a more object-oriented way is to use `name` (and `parent` to get the directory up to that point):


```python
readme=Path('bin','README')
print(f'name   of {readme} is {readme.name}')
print(f'parent of {readme} is {readme.parent}')
```

#### Exercise 2

* print out the absolute pathname of the directory that `images/ucl.png` is in
* print the size of the file in KB to two decimal places

You will need to know how many Bytes in a Kilobyte, and how to [format a string to two decimal places](012_Python_strings.md#String-formating).

## Reading and writing

We can conveniently use `pathlib` to deal with file input and output. The main methods to be aware of are:


|command|  purpose|
|---|---|
|`Path.open()`| open a file and return a file descriptor|
|`Path.read_text()`|  read text|
|`Path.write_text()`| write text|
|`Path.read_bytes()`| read byte data|
|`Path.write_bytes()`| write byte data|


### `with ... as ...` `Path.open` `yaml` `json`

The first of these provides a file descriptor for the open file. This is used to interface to other input/output functions in Python. A typical example of this is reading a configuration file in [`yaml` format](http://zetcode.com/python/yaml/).

The usual way of opening a file to get the file descriptor is:

    with Path(filename).open('r') as f:
       # do some reading with f
       pass
       

We use the form `with ... as ...` here, so that the file descriptor `f` only exists within this construct and the file is automatically closed when we finish. Codes are spaced in inside the construct, as we have seen in `if ...` or `for ... in ...` constructs.

Here, we have set the flag `r` within the `open()` statement (this is the default mode). This means that the file will be opened for *reading* only. Alternatives include `w` for writing, or `w+` for appending.

In the following example, we use `Path` to open the file [`bin/copy/environment.yml`](bin/copy/environment.yml) and read it using the `yaml` library. This file specifies which packages are loaded in our Python environment. It has a simple ascii format, but since it is a `yaml` file, we should read it with code that interprets the format correctly and safely into a dictionary. This is done using `yaml.safe_load(f)` with `f` an open file descriptor.


```python
import yaml

# form the file name
yaml_file = Path('bin','copy','environment.yml')

with yaml_file.open('r') as f:
    env = yaml.safe_load(f)

print(f'env is type {type(env)}')
print(f'env keys: {env.keys()}')
```

Another common file format for configuration information is [`json`](https://www.json.org/json-en.html). We can use the same form of code as above to write the information in `env` into a `json` format file:


```python
import json

# form the file name
json_file = Path('bin','copy','environment.json')

with json_file.open('w') as f:
    json.dump(env, f)
```

This now exists as [`bin/copy/environment.json`](bin/copy/environment.json).

## read and write text

To use `Path.write_text()` to write text to a file `work/easy.txt`, we simply do:


```python
from geog0111.gurlpath import URL
from pathlib import Path

u = 'https://www.json.org/json-en.html'
url = URL(u)
data = url.read_text()
ofile = Path('data',url.name)
print(f'writing to {ofile}')
osize = ofile.write_text(data)
assert osize == 26718
print('passed')
```

Use `Path.write_text()` to write text to a file `work/easy.txt`, we simply do:


```python
r = URL('https://www.json.org').get_text()
```


```python
# from https://www.json.org
some_text = '''
It is easy for humans to read and write.
It is easy for machines to parse and generate. 
'''

# set up the filename
outfile = Path('work','easy.txt')
# write the text
nbytes = outfile.write_text(some_text)
# print what we did
print(f'wrote {nbytes} bytes to {outfile}')
```

#### Exercise 3

* Using `Path.read_text()` read the text from the file `work/easy.txt` and print the text returned.
* split the text into lines of text using `str.split()` at each newline, and print out the resulting list

You learned how to split strings in [013_Python_string_methods](013_Python_string_methods.md#split()-and-join())

A similar approach is taken for reading and writing binary data.

## Reading from a URL

## `pandas`

For many datasets that we want to access in simple text formats, we can use specialised packages such as [`pandas`](https://pandas.pydata.org/). This is designed for data analysis and manipulation, and so (mostly) makes it easy for the user to read such data.



```python
import pandas as pd
import io
url = "https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt"

c=pd.read_csv('https://raw.githubusercontent.com/UCL-EO/geog0111/master/data/2276931.csv')
c
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>STATION</th>
      <th>NAME</th>
      <th>DATE</th>
      <th>PRCP</th>
      <th>SNOW</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-01-01</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-01-02</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-01-03</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-01-04</td>
      <td>0.98</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-01-05</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>240</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-08-29</td>
      <td>0.39</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>241</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-08-30</td>
      <td>0.12</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>242</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-08-31</td>
      <td>0.06</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>243</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-09-01</td>
      <td>0.44</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>244</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-09-02</td>
      <td>0.09</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>245 rows × 5 columns</p>
</div>




```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# choose the item to plot
quantity = 'PRCP'

# generate figure an plot
fig, ax = plt.subplots(figsize=(15,3))
ax.plot(c['DATE'],c[quantity])

# format the ticks: every month
months = mdates.MonthLocator() 
ax.xaxis.set_major_locator(months)

plt.title(c['NAME'][0])
plt.ylabel(quantity)
```




    Text(0, 0.5, 'PRCP')




![png](020_Python_files_files/020_Python_files_47_1.png)


### `gurlpath`

The library [`geog0111`](geog0111/geog0111.py) in [geog0111](geog0111) is designed to operate in a similar manner to `pathlib` for reading data from URLs. 


The object corresponding to `Path` is `URL`:


```python
from geog0111.gurlpath import URL
url = "https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt"

f = URL(url)
```

We have similar functionality for manipulating filenames, but more limited file information:


```python
print(f'URL {f}')
print(f'name   : {f.name}')
print(f'parent : {f.parent}')
```

### Reading text from a URL

It is particularly useful for a simple object-oriented approach to reading text or data from a URL:


|command|  purpose|
|---|---|
|`URL.read_text()`|  read text|
|`URL.read_bytes()`| read byte data|


If we examine the data on the website [HadSEEP_monthly_qc.txt](https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt), we see that the first 3 lines are metedata. The fourth line specifies the data columns, then the rest are datra values, with `-99.9` as invalid.




```python
url = "https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt"
f = URL(url)

text_data = f.read_text()
```

We could do some processing and manipulation of the text data string. For example the following code will split the string on newline `\n` characters into a list, take the first 6 lines of the list, then join it back again into a string:

    '\n'.join(text_data.split('\n')[:6])


```python
print(f'data read is {len(text_data)} bytes of text data')
print('\n'.join(text_data.split('\n')[:6]))
```

    data read is 12915 bytes of text data
    Monthly Southeast England precipitation (mm). Daily automated values used after 1996.
    Wigley & Jones (J.Climatol.,1987), Gregory et al. (Int.J.Clim.,1991)
    Jones & Conway (Int.J.Climatol.,1997), Alexander & Jones (ASL,2001). Values may change after QC.
    YEAR   JAN   FEB   MAR   APR   MAY   JUN   JUL   AUG   SEP   OCT   NOV   DEC   ANN
     1873  87.1  50.4  52.9  19.9  41.1  63.6  53.2  56.4  62.0  86.0  59.4  15.7  647.7
     1874  46.8  44.9  15.8  48.4  24.1  49.9  28.3  43.6  79.4  96.1  63.9  52.3  593.5


This is effective, but normally we would use specialised packages designed for reading tabular data of this sort. 



```python
import pandas as pd
import io
c=pd.read_table(io.StringIO(f.read_text()),skiprows=3,na_values=[-99.9],sep=r"[ ]{1,}",engine='python')
c.head()
```


```python
import matplotlib.pyplot as plt
plt.plot(c['YEAR'],c['JAN'])
```


```python
from geog0111.gurlpath import URL
from pathlib import Path

u='https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h09v06.006.2015084002115.hdf'
url = URL(u)
#cy = Cylog(url.anchor,verbose=True).login()
#print(cy)
data = url.read_bytes(verbose=True)
ofile = Path('data',url.name)
print(f'writing to {ofile}')
osize = ofile.write_bytes(data)
assert osize == 3365255
print('passed')
```

    try again ... or enter 'exit' as username to quit
    --> user login required for https://e4ftl01.cr.usgs.gov/ <--
    Enter your username: plewis@geog.ucl.ac.uk
    please type your password········
    please re-type your password for confirmation········
    password created
    --> logging in to https://e4ftl01.cr.usgs.gov/
    --> data read from https://e4ftl01.cr.usgs.gov/
    writing to data/MCD15A3H.A2003345.h09v06.006.2015084002115.hdf
    passed



```python
from geog0111.gurlpath import URL
from geog0111.cylog import Cylog
from pathlib import Path

u='https://e4ftl01.cr.usgs.gov'
url = URL(u)
rlist = url.glob('MOT*/MCD15A3H.006/2003.12.*/*0.hdf',verbose=True)
```

Suppose we want to download this set of files


```python
hdffile = next(rlist)
```

    wildcards in: ['MOT*' 'MCD15A3H.006' '2003.12.*' '*0.hdf']
    ----> level 0/4 : MOT*
    --> discovered 1 files with pattern MOT* in https://e4ftl01.cr.usgs.gov
    ----> level 1/4 : MCD15A3H.006
    --> discovered 1 files with pattern MCD15A3H.006 in https://e4ftl01.cr.usgs.gov/MOTA
    ----> level 2/4 : 2003.12.*
    --> discovered 7 files with pattern 2003.12.* in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006
    ----> level 3/4 : *0.hdf
    --> discovered 32 files with pattern *0.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03
    --> discovered 30 files with pattern *0.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07
    --> discovered 22 files with pattern *0.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11
    --> discovered 22 files with pattern *0.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15
    --> discovered 18 files with pattern *0.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23
    --> discovered 24 files with pattern *0.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27
    --> discovered 33 files with pattern *0.hdf in https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31



```python
hdffile
```




    [URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h04v10.006.2015083165740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h05v13.006.2015083165740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h08v04.006.2015083171130.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h09v09.006.2015083165730.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h12v02.006.2015083171110.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h12v05.006.2015083165720.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h13v02.006.2015083165540.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h13v03.006.2015083165800.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h14v02.006.2015083165730.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h14v04.006.2015083165740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h15v03.006.2015083171120.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h15v11.006.2015083165730.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h17v08.006.2015083165810.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h20v04.006.2015083165750.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h20v06.006.2015083165730.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h20v11.006.2015083165740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h21v05.006.2015083165700.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h22v02.006.2015083165750.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h22v08.006.2015083165800.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h22v13.006.2015083165740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h22v14.006.2015083165740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h27v05.006.2015083165720.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h27v09.006.2015083165750.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h27v11.006.2015083165720.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h27v12.006.2015083165850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h28v11.006.2015083165730.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h29v06.006.2015083165600.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h29v07.006.2015083165650.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h29v09.006.2015083165710.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h29v12.006.2015083165750.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h31v06.006.2015083165720.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.03/MCD15A3H.A2003337.h31v13.006.2015083165700.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h01v07.006.2015083051520.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h02v10.006.2015083054140.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h05v11.006.2015083054140.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h06v03.006.2015083050240.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h09v02.006.2015083051540.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h10v05.006.2015083051750.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h11v07.006.2015083051730.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h12v02.006.2015083051710.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h13v14.006.2015083053110.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h14v09.006.2015083051100.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h15v11.006.2015083051530.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h16v02.006.2015083052050.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h17v08.006.2015083052040.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h18v08.006.2015083052500.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h19v12.006.2015083053110.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h20v09.006.2015083053150.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h21v02.006.2015083053830.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h21v13.006.2015083052830.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h22v14.006.2015083053110.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h23v05.006.2015083051020.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h23v10.006.2015083051220.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h25v04.006.2015083051640.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h25v06.006.2015083052150.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h26v05.006.2015083051710.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h27v14.006.2015083052730.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h28v04.006.2015083052740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h30v12.006.2015083051520.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h33v09.006.2015083052740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h33v10.006.2015083052440.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.07/MCD15A3H.A2003341.h34v10.006.2015083054140.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h01v07.006.2015084000250.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h06v03.006.2015083235840.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h12v09.006.2015084001540.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h12v12.006.2015084001500.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h12v13.006.2015084002120.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h13v04.006.2015084001500.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h14v04.006.2015084000300.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h14v11.006.2015083235900.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h17v06.006.2015084002050.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h19v02.006.2015084000250.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h20v02.006.2015084000240.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h21v06.006.2015084002100.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h21v10.006.2015084001750.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h22v09.006.2015084002120.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h23v02.006.2015084001530.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h28v09.006.2015084002100.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h28v12.006.2015084002020.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h29v10.006.2015084002130.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h29v12.006.2015084001520.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h30v07.006.2015084003750.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h30v09.006.2015084002850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.11/MCD15A3H.A2003345.h35v10.006.2015083235850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h00v08.006.2015084011510.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h02v08.006.2015084012930.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h08v05.006.2015084012300.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h09v08.006.2015084011510.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h12v08.006.2015084012250.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h13v08.006.2015084012240.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h13v10.006.2015084012300.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h14v03.006.2015084012240.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h15v14.006.2015084012230.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h18v09.006.2015084011520.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h19v06.006.2015084011520.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h19v08.006.2015084012310.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h19v10.006.2015084012300.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h22v11.006.2015084011520.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h24v02.006.2015084012240.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h30v05.006.2015084012230.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h31v06.006.2015084012230.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h31v08.006.2015084011520.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h31v12.006.2015084012230.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h33v10.006.2015084012230.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h34v10.006.2015084011520.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.15/MCD15A3H.A2003349.h35v10.006.2015084011510.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h04v09.006.2015084025450.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h10v04.006.2015084030030.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h10v05.006.2015084030040.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h11v04.006.2015084030030.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h12v04.006.2015084025450.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h12v08.006.2015084025450.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h12v11.006.2015084025500.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h13v13.006.2015084030020.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h14v09.006.2015084030020.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h19v02.006.2015084025440.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h21v09.006.2015084024900.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h22v08.006.2015084025040.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h23v06.006.2015084025440.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h25v08.006.2015084025440.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h26v02.006.2015084025440.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h31v11.006.2015084025500.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h32v08.006.2015084024850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.23/MCD15A3H.A2003357.h35v10.006.2015084024840.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h08v04.006.2015084002830.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h08v11.006.2015084001230.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h09v09.006.2015084004520.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h11v07.006.2015084002130.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h12v02.006.2015084003740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h12v09.006.2015084003750.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h12v11.006.2015084002150.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h13v03.006.2015084002850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h13v08.006.2015084000320.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h13v10.006.2015084002900.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h16v06.006.2015084000230.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h17v02.006.2015084003730.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h18v02.006.2015084002130.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h18v14.006.2015084004520.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h20v05.006.2015084002130.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h24v04.006.2015084003750.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h27v10.006.2015084001510.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h29v06.006.2015084002830.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h29v07.006.2015084002130.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h29v08.006.2015084001000.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h29v11.006.2015084002200.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h30v06.006.2015084000950.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h30v12.006.2015084002840.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.27/MCD15A3H.A2003361.h32v12.006.2015084003740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h01v09.006.2015084192700.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h01v10.006.2015084200740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h02v06.006.2015084194840.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h03v07.006.2015084194850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h04v11.006.2015084194850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h10v03.006.2015084202850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h10v11.006.2015084194840.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h11v11.006.2015084192720.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h11v12.006.2015084200730.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h12v11.006.2015084200820.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h13v08.006.2015084194840.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h14v10.006.2015084192720.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h16v07.006.2015084192800.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h16v09.006.2015084192710.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h17v08.006.2015084194910.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h17v12.006.2015084194850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h20v03.006.2015084200830.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h20v04.006.2015084200740.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h20v08.006.2015084202830.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h21v03.006.2015084200810.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h21v13.006.2015084194850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h22v08.006.2015084194910.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h23v08.006.2015084194850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h24v03.006.2015084194920.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h25v02.006.2015084194900.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h25v06.006.2015084194930.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h26v03.006.2015084194850.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h26v08.006.2015084194900.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h27v11.006.2015084194900.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h28v09.006.2015084194910.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h30v05.006.2015084194900.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h30v07.006.2015084194900.hdf'),
     URL('https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2003.12.31/MCD15A3H.A2003365.h35v09.006.2015084194900.hdf')]



We will use this idea to make a dictionary of our ENSO dataset, using the items in the header for the keys. In this way, we obtain a  more elegant representation of the dataset, and can refer to items by names (keys) instead of column numbers.


```python
import requests
import numpy as np
import io

# copy the useful data
start_head = txt.find('YEAR')
start_data = txt.find('1950\t')
stop_data  = txt.find('2018\t')

header = txt[start_head:start_data].split()
data = np.loadtxt(io.StringIO(txt[start_data:stop_data]),unpack=True)

# use zip to load into a dictionary
data_dict = dict(zip(header, data))

key = 'MAYJUN'
# plot data
plt.figure(0,figsize=(12,7))
plt.title('ENSO data from {0}'.format(url))
plt.plot(data_dict['YEAR'],data_dict[key],label=key)
plt.xlabel('year')
plt.ylabel('ENSO')
plt.legend(loc='best')
```

#### Exercise 1

* copy the code above, and modify so that datasets for months `['MAYJUN','JUNJUL','JULAUG']` are plotted on the graph

Hint: use a for loop

We can also usefully use a dictionary with a printing format statement. In that case, we refer directly to the key in ther format string. This can make printing statements much easier to read. We don;'t directly pass the dictionary to the `fortmat` staterment, but rather `**dict`, where `**dict` means "treat the key-value pairs in the dictionary as additional named arguments to this function call".

So, in the example:


```python
import requests
import numpy as np
import io

# access dataset as above
url = "http://www.esrl.noaa.gov/psd/enso/mei/table.html"
txt = requests.get(url).text

# copy the useful data
start_head = txt.find('YEAR')
start_data = txt.find('1950\t')
stop_data  = txt.find('2018\t')

header = txt[start_head:start_data].split()
data = np.loadtxt(io.StringIO(txt[start_data:stop_data]),unpack=True)

# use zip to load into a dictionary
data_dict = dict(zip(header, data))
print(data_dict.keys())

# print the data for MAYJUN
print('data for MAYJUN: {MAYJUN}'.format(**data_dict))
```

The line `print('data for MAYJUN: {MAYJUN}'.format(**data_dict))` is equivalent to writing:

    print('data for {MAYJUN}'.format(YEAR=data_dict[YEAR],DECJAN=data_dict[DECJAN], ...))
    
In this way, we use the keys in the dictionary as keywords to pass to a method.

Another useful example of such a use of a dictionary is in saving a numpy dataset to file.

If the data are numpy arrays in a dictionary as above, we can store the dataset using:




```python
import requests
import numpy as np
import io

# access dataset as above
url = "http://www.esrl.noaa.gov/psd/enso/mei/table.html"
txt = requests.get(url).text

# copy the useful data
start_head = txt.find('YEAR')
start_data = txt.find('1950\t')
stop_data  = txt.find('2018\t')

header = txt[start_head:start_data].split()
data = np.loadtxt(io.StringIO(txt[start_data:stop_data]),unpack=True)

# use zip to load into a dictionary
data_dict = dict(zip(header, data))

filename = 'enso_mei.npz'

# save the dataset
np.savez_compressed(filename,**data_dict)
```

What we load from the file is a dictionary-like object `<class 'numpy.lib.npyio.NpzFile'>`.

If needed, we can cast this to a dictionary with `dict()`, but it is generally more efficient to keep the original type.


```python
# load the dataset

filename = 'enso_mei.npz'

loaded_data = np.load(filename)

print(type(loaded_data))

# test they are the same using np.array_equal
for k in loaded_data.keys():
    print('\t',k,np.array_equal(data_dict[k], loaded_data[k]))
```

#### Exercise 2

* Using what you have learned above, access the Met Office data file [`https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt`](https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt) and create a 'data package' in a numpy`.npz` file that has keys of `YEAR` and each month in the year, with associated datasets of Monthly Southeast England precipitation (mm).
* confirm that tha data in your `npz` file is the same as in your original dictionary
* produce a plot of October rainfall using these data for the years 1900 onwards

### 1.3.5 Summary

In this section, we have extended the types of data we might come across to include groups . We dealt with ordered groups of various types (`tuple`, `list`), and introduced the numpy package for numpy arrays (`np.array`). We saw dictionaries as collections with which we refer to individual items with a key.

We learned in the previous section how to pull apart a dataset presented as a string using loops and various using methods and to construct a useful dataset 'by hand' in a list or similar structure. It is useful, when learning to program, to know how to do this.

Here, we saw that packages such as numpy provide higher level routines that make reading data easier, and we would generally use these in practice. We saw how we can use `zip()` to help load a dataset from arrays into a dictionary, and also the value of using a dictionary representation when saving numpy files.
