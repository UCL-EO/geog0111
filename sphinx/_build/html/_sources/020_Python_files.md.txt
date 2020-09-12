# 020 Files and other Resources


## Introduction



### Purpose

In this session, we will learn about files and similar resources. We will introduce the standard Python library [`pathlib`](https://docs.python.org/3/library/pathlib.html) which is how we deal with file paths, as well as the local package [gurlpath](geog0111/gurlpath.py) that allows a similar object-oriented approach with files and other objects on the web. We will also cover opening and closing files, and some simple read- and write-operations.



### Prerequisites

You will need some understanding of the following:


* [001 Using Notebooks](001_Notebook_use.md)
* [002 Unix](002_Unix.md) with a good familiarity with the UNIX commands we have been through.
* [003 Getting help](003_Help.md)
* [004_Accounts](004_Accounts.md)
* [010 Variables, comments and print()](010_Python_Introduction.md)
* [011 Data types](011_Python_data_types.md) 
* [012 String formatting](012_Python_strings.md)
* [013_Python_string_methods](013_Python_string_methods.md)
* [018_Packages](018_Packages.md)


### Test
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

### Timing

The session should take around 30 minutes.

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

## `Path`, `import`

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

    I am in directory /Users/plewis/Documents/GitHub/geog0111/notebooks
    My home is /Users/plewis


To keep the filenames generic, we can form a filename from a list using `Path()`, so `Path('bin','README')` would refer to the filename `bin/README` on a `posix` system, and `bin/README` on Windows. However, this is interpreted the same as just using `bin/README` which will often be clearer.


```python
assert Path('bin','README') == Path('bin/README')
print('they are the same')
```

    they are the same


We can use the function `exists` to check if a file exists:


```python
readme_file = Path('bin/README')
print(f'Does {readme_file} exist? {readme_file.exists()}')
```

    Does bin/README exist? True


To add a sub-directory or file to a `Path` object, we can use the list form, or we can just specify the separator '/' between the components, provided the first term is a `Path` object:


```python
# the relative directory bin
bindir = Path('bin')
print(f'starting from the relative directory "bin": {bindir}')

# add README to the path
readme_file = Path(bindir,'README')
print(f'README file is: {readme_file}')

# another way to do it using /
readme_file = bindir/'README'
print(f'README file is: {readme_file}')
```

    starting from the relative directory "bin": bin
    README file is: bin/README
    README file is: bin/README


#### Exercise 1

There is a file called `environment.yml` in the directory `copy`.md_checkpoints/

* use `Path` to generate the a variable `copy_dir` containing the pathname of the `copy` directory
* create a variable `env_file` which adds add the file `environment.yml` to this 
* check to see if the file exists

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

    README file is bin/README
           size is 16 bytes
           mode is 0o100644
          owner is plewis


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

    file 0 is bin/notebook-mkdocs.sh
    file 1 is bin/setup.sh
    file 2 is bin/notebook-run.sh
    file 3 is bin/link-set.sh
    file 4 is bin/git-remove-all.sh


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


#### Exercise 2

* Use `Path` to show the file permissions of all files that end `.sh` in the directory `bin`

### `absolute`, `parts`, `name`, `parent`

We can use `Path` to convert filenames between relative and absolute representations using `absolute()` and `relative_to()`:


```python
print(f'I am in {Path.cwd()}')

# define a relative path name
readme=Path('bin/README')
print(f'original relative name:\n\t{readme}')

# convert to absolute
readme = readme.absolute()
print(f'absolute name:\n\t{readme}')

# now make a relative pathname, 
# reletive to current working directory
readme = readme.relative_to(Path.cwd())
print(f'name relative to {Path.cwd()}:\n\t{readme}')
```

    I am in /Users/plewis/Documents/GitHub/geog0111/notebooks
    original relative name:
    	bin/README
    absolute name:
    	/Users/plewis/Documents/GitHub/geog0111/notebooks/bin/README
    name relative to /Users/plewis/Documents/GitHub/geog0111/notebooks:
    	bin/README


Quite often we need to split some filename up into its constituent parts. This is achieved with `paths` which gives a list of the file name tree:


```python
readme=Path('bin/README')
print(readme.parts)
```

    ('bin', 'README')


We could use that to get at the filename `README` from the last item in the list, but a more object-oriented way is to use `name` (and `parent` to get the directory up to that point):


```python
readme=Path('bin','README')
print(f'name   of {readme} is {readme.name}')
print(f'parent of {readme} is {readme.parent}')
```

    name   of bin/README is README
    parent of bin/README is bin


#### Exercise 3

* print out the absolute pathname of the directory that `images/ucl.png` is in
* check that the file exists
* if it does, print the size of the file in KB to two decimal places

You will need to know how many Bytes in a Kilobyte, and how to [format a string to two decimal places](012_Python_strings.md#String-formating). You will also need to remember how to use [`if` statements](015_Python_control.md#Comparison-Operators-and-if).

## Resources from a URL

### `gurlpath`

The library [`gurlpath`](geog0111/gurlpath.py) in [geog0111](geog0111) is designed to operate in a similar manner to `pathlib` for reading data from URLs. It is derived from [`urlpath`](https://github.com/chrono-meter/urlpath)  which in turn is based on [urllib.parse](https://docs.python.org/3/library/urllib.parse.html) and [requests](https://requests.readthedocs.io/en/master/). It uses [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/) for parsing `html` data. At some point you may wish to learn how to use these lower-level packages, but for learning on this course, you will find it convenient to use this higher-level package.

The object in `gurlpath` corresponding to `Path` is `URL`:


```python
from geog0111.gurlpath import URL
site = 'https://www.metoffice.gov.uk/'
site_dir = 'hadobs/hadukp/data/monthly'
site_file = 'HadSEEP_monthly_qc.txt'

url = URL(site,site_dir,site_file)
print(url)
```

    https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt


We have similar functionality for manipulating filenames, but more limited file information:


```python
print(f'URL    : {url}')
print(f'name   : {url.name}')
print(f'parent : {url.parent}')
```

    URL    : https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt
    name   : HadSEEP_monthly_qc.txt
    parent : https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly


#### Exercise 4

* create a `URL` object for the file `table.html` in the directory `psd/enso/mei/` on the site `http://www.esrl.noaa.gov/`.
* print out the url and check it is `table.html`

For accessing URLs, will mostly make use of the following functions in `URL` that you will see are similat to those for `Path`:


|function| purpose|
|---|---|
|`URL.name`|  filename |
|`URL.parent`|  parent |
|`URL.parts`|  parts |
|`URL.glob(pattern)`| Glob the pattern given in the URL directory, yielding matching files of any kind| 
|`URL.exists()`|  test to see if a url is accessible |
|`URL.with_userinfo()` | add username and password |

### login and password

Some web resources require you to use a login and password. This can be specified for the `URL` class by with the functiuon `with_userinfo`:


```python
help(URL.with_userinfo)
```

    Help on function with_userinfo in module urlpath:
    
    with_userinfo(self, username, password)
        Return a new url with the userinfo changed.
    


This is the main way you can pass your username and password to the relevant functions. However, in any public information (like these notebooks) we do not want to expose sensitive information such as usernames and passwords.

To that end `URL` can make use of stored passwords and usernames using the local [cylog](geog0111/cylog.py) package that was covered in [004_Accounts](004_Accounts.md). You should have already tested that your NASA Earthdata login works for files on the site `https://e4ftl01.cr.usgs.gov`.

### `exists`

We can use the function `URL.exists()` to test to see if some URL is accessible to us. The function first tries without a password, but if that fails, tries to find an appropriate password and username in the `cyclog` database.

Several of the URL functions have `verbose` options (unlike those from `Path`). This is to allow the user to gain more insight into what is going on in accessing the URL. We will use `exists()` with `verbose=True` below:


```python
from geog0111.gurlpath import URL
from pathlib import Path

site = 'https://e4ftl01.cr.usgs.gov'
site_dir = '/MOLA/MYD11_L2.006/2002.07.04'
site_file = 'MYD11_L2.A2002185.0325.006.2015142192613.hdf'

url = URL(site,site_dir,site_file)
if url.exists(verbose=True):
    print(f'I can access {url}')
else:
    print(f'I cannot access {url}')
```

    --> trying https://e4ftl01.cr.usgs.gov/MOLA/MYD11_L2.006/2002.07.04/MYD11_L2.A2002185.0325.006.2015142192613.hdf
    --> code 401
    --> trying another
    --> getting login
    --> logging in to https://e4ftl01.cr.usgs.gov/


    I cannot access https://e4ftl01.cr.usgs.gov/MOLA/MYD11_L2.006/2002.07.04/MYD11_L2.A2002185.0325.006.2015142192613.hdf


    --> failure reading data from https://e4ftl01.cr.usgs.gov/
    --> failed to connect


When we try to access a datafile on the site [`https://e4ftl01.cr.usgs.gov`](https://e4ftl01.cr.usgs.gov) we need to use our NASA Earthdata login and password. This is done automatically withing the call to `url.exists()` or for any function requiring passwords.

### `glob` and NASA datasets

The `glob` function is particularly useful for finding datasets on websites, as we might not always know the full file specification. Using `rglob()` (recursive glob) on a website is generally too slow to be worthwhile, so we will avoid using it.

Suppose we want to access some NASA hdf files for the product `MCD15A3H` for the data tile `h08v06`. On the site `https://e4ftl01.cr.usgs.gov` the data will be in the folder `'MOTA/MCD15A3H.006`. Data for a particular date then are in a directory of the form `/{year}.{month}.{day}/` where `month` and `day` must be a 2-digit string, left zero-padded (e.g. `02` instead of `2`). Files in there will have the form `*.h08v06*.hdf`. This is a perfect case for the use of `glob`:

If we specify a date (1-based for month, so `1` is January):

    year, month, day = '2020', '06', '01'
    
then the directory will be given by:

    site_dir = f'MOTA/MCD15A3H.006/{year:4d}.{month:02d}.{day:02d}'
    
and the file, with wildcard `*` by:

    site_file = '*.h08v06*.hdf'

we can use `glob` to discover the full URL specification:


```python
from geog0111.gurlpath import URL

# settings
product = 'MCD15A3H'
year, month, day = '2020', '06', '01'
tile = 'h08v06'

# url with wildcards
site = 'https://e4ftl01.cr.usgs.gov'
site_dir = f'MOTA/{product}.006/{year}.{month}.{day}'
site_file = f'*.{tile}*.hdf'

# get the information
url = URL(site,site_dir)\
# convert generator to list to make it easier to understand
hdf_urls = url.glob(site_file,verbose=True)
for u in hdf_urls:
    print(u)
```

    --> wildcards in: ['*.h08v06*.hdf']
    --> level 0/1 : *.h08v06*.hdf
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.01


    https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.01/MCD15A3H.A2020153.h08v06.006.2020160231732.hdf


This is extremely useful for dataset discovery.

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
 * run a test of your function, and check that the file pointed to in the URL exists and is accessible
 * what happens if you use a wildcard for the date?

The utility function 


The utility function `modis_dataset` we have developed here is available as `get_url` in the `Modis` class in  `geog0111.modis`:


```python
from  geog0111.modis import Modis

help(Modis.get_url)
```

    Help on function get_url in module geog0111.modis:
    
    get_url(self, year=False, month=False, day=False, product=False, tile=False, verbose=False, site=False)
        Get URL object list for NASA MODIS products
        for the specified product, tile, year, month, day
        
        Keyword Arguments:
        
        verbose:  bool
        site    : str 
        product : str e.g. 'MCD15A3H'
        tile    : str e.g. 'h08v06'
        year    : str valid 2000-present
        month   : str 01-12
        day     : str 01-(28,29,30,31)
    



```python
from  geog0111.modis import Modis

modis = Modis('MCD15A3H',verbose=True)
hdf_urls = modis.get_url("2020","*","0[1-4]")
for u in hdf_urls:
    print(f'{u.name} : {u.exists()}')
```

    --> wildcards in: ['2020.*.0[1-4]' '*.h08v06*.hdf']
    --> level 0/2 : 2020.*.0[1-4]
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006
    --> level 1/2 : *.h08v06*.hdf
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.02.02
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.03.01
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.04.02
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.05.04
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.06.01
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.07.03
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.08.04
    --> trying https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.09.01


    MCD15A3H.A2020001.h08v06.006.2020006032951.hdf : True
    MCD15A3H.A2020033.h08v06.006.2020038231141.hdf : True
    MCD15A3H.A2020061.h08v06.006.2020066032716.hdf : True
    MCD15A3H.A2020093.h08v06.006.2020099025238.hdf : True
    MCD15A3H.A2020125.h08v06.006.2020130031836.hdf : True
    MCD15A3H.A2020153.h08v06.006.2020160231732.hdf : True
    MCD15A3H.A2020185.h08v06.006.2020190031222.hdf : True
    MCD15A3H.A2020217.h08v06.006.2020223212414.hdf : True
    MCD15A3H.A2020245.h08v06.006.2020253152835.hdf : True


## Summary


In this section, we have considered URLs and filenames in some detail, and made use of functions from [`pathlib`](https://docs.python.org/3/library/pathlib.html) and [gurlpath](geog0111/gurlpath.py) to access them. 

The first batch of `Path` commands we saw had much commonality with the core `unix` commands we had previously come across for moving around the file system and finding file information:


|command| unix-equivalent | purpose|
|---|---|---|
|`Path.cwd()`| `pwd` |Return path object representing the current working directory|
|`Path.home()`| `~`| Return path object representing the home directory|
|`Path.stat()`| `ls -l`* | return info about the path|
|`Path.chmod()`| `chmod` | change file mode and permissions|
|`Path.mkdir()`| `mkdir` | to create a new directory at the given path|
|`Path.rename()`| `mv` | Rename a file or directory to the given target|
|`Path.rmdir()`| `rmdir` | Remove the empty directory|
|`Path.unlink()`| `rm` | Remove the file or symbolic link|

The second set is common to both `Path` and `URL`, and involves queries on the `Path` (`URL`) name, testing for file existence, and using wildcards to access a list of files matching a pattern:

|function| purpose|
|---|---|
|`Path.name`|  filename |
|`Path.parent`|  parent |
|`Path.parts`|  parts |
|`Path.glob(pattern)`| Glob the pattern given in the URL directory, yielding matching files of any kind| 
|`Path.exists()`|  test to see if a url is accessible |

|function| purpose|
|---|---|
|`URL.name`|  filename |
|`URL.parent`|  parent |
|`URL.parts`|  parts |
|`URL.glob(pattern)`| Glob the pattern given in the URL directory, yielding matching files of any kind| 
|`URL.exists()`|  test to see if a url is accessible |

