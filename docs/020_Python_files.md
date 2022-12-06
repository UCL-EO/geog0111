# 020 Files, Streams and related issues


## Introduction



### Purpose

In this session, we will learn about files and streams. We will introduce the standard Python library [`pathlib`](https://docs.python.org/3/library/pathlib.html) which is how we deal with file paths. We will also cover opening and closing files, and some simple read- and write-operations.

### Prerequisites

You will need some understanding of the following:


* [001 Using Notebooks](001_Notebook_use.md)
* [002 Unix](002_Unix.md) with a good familiarity with the UNIX commands we have been through.
* [003 Getting help](003_Help.md)
* [004_Accounts](004_Accounts.md)
* [005_Packages](005_Packages.md)
* [010 Variables, comments and print()](010_Python_Introduction.md)
* [011 Data types](011_Python_data_types.md) 
* [012 String formatting](012_Python_strings.md)
* [013_Python_string_methods](013_Python_string_methods.md)


## Data resources

### Resource location

We store information on a computer or 'on the web' in files, or file-like resources. We will use the term 'file' below to mean either of these concepts, other than specific issues relating to particular types of file/resource.

To get information from files, we need to be able to specify some **address** for the file/resource location, along with some way of interacting with the file. These concepts are captured in the idea of a [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) (Uniform Resource Indicator). You will most likely have come across the related idea of a [Uniform Resource Locator (URL)](https://en.wikipedia.org/wiki/URL), which is a URL such as [https://www.geog.ucl.ac.uk/people/academic-staff/philip-lewis](https://www.geog.ucl.ac.uk/people/academic-staff/philip-lewis)
that gives:

* the location of the resource: `people/academic-staff/philip-lewis`
* the access and interpretation protocol: [`https`](https://en.wikipedia.org/wiki/HTTPS) (secure [`http`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol))
* the network domain name: [`www.geog.ucl.ac.uk`](https://www.geog.ucl.ac.uk)

When we visit this URL using an appropriate tool such as a browser, the tool can access and interpret the information in the resource: in this case, interpret the [html code](https://www.w3schools.com/html) in the file pointed to by the URL.

Similarly, we will be used to the idea of accessing `files` on the computer. These may be in the local file system, or on some network or cloud storage that might be accessible from the local file system. An example of such a file would be some Python code file such as 
[`geog0111/helloWorld.py`](http://localhost:8888/edit/notebooks/geog0111/helloWorld.py).

Whilst there are low-level tools we can use to access these various types of information, it is better from a programmer's point of view to be able to do this in a consistent and object-oriented manner: as a programmer, shouldn't really need distinguish greatly between a file accessed by a URL and one on the local file system. And if you do, you should be able to use much the same sort of methods to do much the same sort of tasks.

It doesn't quite work like that yet in Python, but the [`pathlib`](https://docs.python.org/3/library/pathlib.html) package goes a long way towards that for local files. This doesn't yet exist for URLs in standard Python, but is implemented to a large extent by the package [`urlpath`](https://github.com/chrono-meter/urlpath). These are the tools we will be learning to use to access and manipulate files and similar objects.

We will first introduce [`pathlib`](https://docs.python.org/3/library/pathlib.html) to learn how to deal with local files.

### binary and text data

It is useful at this point to distinguish text (ASCII) and binary resources. Text resources are in a human-readable format, so you can just directly 'look at' the file contents to see what is there. Examples of this are [csv-format](https://en.wikipedia.org/wiki/Comma-separated_values) files, [html pages](https://en.wikipedia.org/wiki/HTML), [yaml](https://en.wikipedia.org/wiki/YAML) or [json](https://en.wikipedia.org/wiki/JSON) configuration files, and even these [Jupyter notebooks](https://jupyter.org/). 

Information in text files is, as noted, easily readable: you can open the file in any text editor to see the contents. However, for large datasets, and datasets with particular structures (e.g. on grids), it is very inefficient.

Typical **binary** files include (most) image data and compressed data (e.g. [zip](https://en.wikipedia.org/wiki/Zip_(file_format)) files), where size is more important, as well as encrypted data, where human-readability might not be desirable.

Text files designed for different purposes will mostly have some format definition or conventions. This means that although we can easily scan e.g. a [json file](https://json.org/example.html`), there is a set way of laying such files out, so we can interpret them by eye or in software.

Binary files will also have some defined format, but in this case, the user is generally forced to use some software reader to interpret the data correctly.

When you wish to access some file or dataset, you will generally know which format the file will be in, so can target an appropriate reader. Quite often though, we have to we might need to examine a dataset before deciding on some parameters for an interpreter, particularly with text datasets. 

In these notes, we will learn how to access and use binary and text datasets in Python, from the local file system and online from URLs over the next few sessions.  In a URI sense, there is much in common between online and local files


We will be also using `yaml`, `json` and [`pandas`](https://pandas.pydata.org/) packages for reading particular text file types, and introducing [`gdal`](https://gdal.org/python/) for binary image files.

## `Path`, `import`

We have come across the idea of packages in [005 Packages](005_Packages.md). `Path` is part of the `pathlib` package, so in any Python codes, we first must import this into our workspace:


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
|`Path.stat()`| `ls -l`† | return info about the path. File size is `Path.stat().st_size` |
|`Path.chmod()`| `chmod` | change file mode and permissions|
|`Path.glob(pattern)`| `ls *` | Glob the pattern given in the directory that is represented by the path, yielding matching files of any kind|
|`Path.mkdir()`| `mkdir` | to create a new directory at the given path|
|`Path.rename()`| `mv` | Rename a file or directory to the given target|
|`Path.rmdir()`| `rmdir` | Remove the empty directory|
|`Path.unlink()`| `rm`‡ | Remove the file or symbolic link|
|`Path.touch()` | `touch` | create (zero-sized) or update a file |
|`Path.parent` | `..` ✟ | The parent object (one level up in directory tree) |


Some other common utilities:

|command|  purpose|
|---|---|
|`Path.as_posix()`| Return the object as a posix filename string |
|`Path.exists()` | `True` if exists, `False` if not|
|`Path.parent` |  the parent object (one level up in directory tree), or the directory a file is in |
|`Path.name` | the file name |
|`Path.is_file()` | `True` if object is a file |
|`Path.is_dir()` | `True` if object is a directory |

We will also deal with opening and closing files and moving information around, using these functions:


|command|  purpose|
|---|---|
|`Path.open()`| open a file and return a file descriptor|
|`Path.read_text()`|  read text|
|`Path.write_text()`| write text|
|`Path.read_bytes()`| read byte data|
|`Path.write_bytes()`| write byte data|



##### Notes to table

† Really, `Path.stat()` equates to the `unix` command `stat`, but this contains the information we access using `ls -l`.

‡ You can use `shutil.rmtree()` to do recursive delete, if you really need to.

✟ `..` isn't exactly the same as `Path.parent`, but expresses a similar idea. So if you had a directory `foo/bar`, then `foo/bar/..` would be the parent i.e. `foo`.

Since we are already familiar with most of these commands in `unix`, we can get straight into using them:


```python
from pathlib import Path

print(f'I am in directory {Path.cwd()}')
print(f'My home is {Path.home()}')
```

    I am in directory /nfs/cfs/home3/Ucour1/coursd0/geog0111/notebooks
    My home is /home/coursd0


Really, the object `Path.home()` is a `Path` object. When we direct `print()` to print it, it converts it to a string. If you need to convert a `Path` object to a string in any other context (e.g. passing to some function that needs a filename as a string), then use `Path.as_posix()` to convert:


```python
# print posix path as string
myhome=Path.home()
print(f'My home is {myhome.as_posix()}')

# Path object 
print(type(myhome))
# convert to string
print(type(myhome.as_posix()))
```

    My home is /home/coursd0
    <class 'pathlib.PosixPath'>
    <class 'str'>


To keep the filenames generic between different operating systems, we can form a filename from a list using `Path()`, so `Path('bin','README')` would refer to the filename `bin/README` on a `posix` system, and `bin\README` on Windows. However, this is interpreted the same as just using `bin/README` which will often be clearer.


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
from pathlib import Path

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

There is a file called `environment.yml` in the directory `copy`.

* use `Path` to generate the a variable `copy_dir` containing the pathname of the `copy` directory
* create a variable `env_file` which adds add the file `environment.yml` to this 
* check to see if the file exists

### Creating and deleting files and directories

#### Directories

To create a directory, use:

    Path().mkdir()
    
We can use the options:

    Path().mkdir(parents=True,exist_ok=True)
    
which will make all of the sub-directories needed, and also no fail if the directory already exists. This is often the safest way to make a directory in your code, provided you are sure that your path will be reasonable.

To remove an empty directory, use:

    Path().rmdir()
    
If we need to test to see if the object we want to delete really is a directory, we can use `Path.is_dir`. If we want to first check it exists, then use `Path.exists()` to make the code more robust:


```python
# make a temp directory
tmp = Path('tmp')
tmp.mkdir(parents=True,exist_ok=True)

# then delete tmp (if it exists and is a dir)
tmp.exists() and tmp.is_dir() and tmp.rmdir()
```

#### Files

To create a blank (zero-sized) file, we can use `Path.touch()`, and then `Path.unlink()` to remove it. 

We can use `Path.parent` to refer to the parent object, e.g. the directory a file is in, or for a directory, one level up (`..`). So, if we are creating a file for the first time, we might want to make sure that its parent directory exists before doing so (e.g. using `Path.parent.mkdir(parents=True,exist_ok=True)` as above).

If we need to test to see if the object we want to delete really is a file (not a directory), we can use `Path.is_file`:


```python
tmp = Path('tmp','myfile')

# make sure directory (parent) exists
tmp.parent.mkdir(parents=True,exist_ok=True)
# create zero size file
tmp.touch()

# call `Path.exists()`
print("now you see it:",tmp.exists())
```

    now you see it: True



```python
# delete inside if it exists and is a file
tmp.exists() and tmp.is_file() and tmp.unlink()

# let's make a unix call here to check the file size etc
print("now you don't:",tmp.exists())
```

    now you don't: False


####  `rm -r` options

Note that there is no recursive delete in `pathlib` like `rm -r` in linux: you have to delete files and directories explicitly in `pathlib`. Really, `rm -r` is a really dangerous command to have, as you might accidently delete all sorts of things you didn't mean to. So, don't even go there unless you need to.

If you do, you can look on the web, you can find [various solutions to this to make it easier](https://stackoverflow.com/questions/50186904/pathlib-recursively-remove-directory). Maybe the easiest is to use `rmtree` from the package `shutil`, though this doesn't fit so well with our object-oriented principles.

    import shutil
    shutil.rmtree( '/tmp/mydir' )

#### Exercise 2

Create a zero-sized file called `hello.txt` in a directory `mystuff`, using `Path` and show that it exists and is a file. Then delete the file and directory.

### File information

The file permissions format we are used to from `ls -l` is accessed through `filename.stat().st_mode` but needs to be converted to octal to match to `ls`

    oct(filename.stat().st_mode)


```python
from pathlib import Path

# similar information to ls -l
readme=Path('bin','README')
print(f'README file is {readme}')
print(f'       size is {readme.stat().st_size} bytes')
print(f'       mode is {oct(readme.stat().st_mode)}')
print(f'      owner is {readme.owner()}')

# confirm with unix
!ls -lh bin/README
```

    README file is bin/README
           size is 16 bytes
           mode is 0o100644
          owner is coursd0
    -rw-r--r-- 1 coursd0 ucaac2 16 Sep 29 15:46 bin/README


#### Exercise 3

Create a zero-sized file in a new directory, and use `Path.stat()` to show it has size 0 bytes. Then tidy up by deleting the file and directory.

### `datetime` 

You have access to  a wide range of information from [`File.stat()`](https://docs.python.org/3/library/os.html#os.stat_result). Some of this relates to time (e.g. time last viewed, accessed etc). These times are given as Epoch times, in seconds since from 1/1/1970:

For example, to get the last access time:

    st_mtime : Time of most recent content modification expressed in seconds.
    


```python
readme = Path('bin','README')

modified = readme.stat().st_mtime
print(f'Time of most recent modification for {readme} is {modified}')
```

    Time of most recent modification for bin/README is 1664462780.737117


That is not always the most convenient form. So we can use the `datetime.datetime.fromtimestamp` from the `datetime` package to convert it into something more human-readable:


```python
from datetime import datetime

modified = readme.stat().st_mtime
h_modified = datetime.fromtimestamp(modified)

print(f'Time of most recent modification for {readme} is {h_modified}')
```

    Time of most recent modification for bin/README is 2022-09-29 15:46:20.737117


We can also use `datetime` to tell us the time now, with `datetime.now()`, for comparison:


```python
print(f'Time now is {datetime.now()}')
```

    Time now is 2022-10-21 16:19:25.418268


#### Exercise 4

Use `Path.touch()` to update the modification time for the file `bin/README` and demonstrate that you have done this and that is the same as the current time (now).

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

    file 0 is bin/clean0111.sh
    file 1 is bin/database.sh
    file 2 is bin/fixA.sh
    file 3 is bin/get-datasets.sh
    file 4 is bin/git-remove-all.sh
    file 5 is bin/howmany.sh
    file 6 is bin/init.sh
    file 7 is bin/init0111.sh
    file 8 is bin/link-set.sh
    file 9 is bin/notebook-mkdocs.sh
    file 10 is bin/notebook-run.sh
    file 11 is bin/set-course.sh
    file 12 is bin/setup.sh
    file 13 is bin/shellMe.sh
    file 14 is bin/sort-db.sh
    file 15 is bin/tidy.sh


The advantage of a generator is that it will generally need less memory than fully calculating all items in a list. Once we move on to the next item in the generator, any memory used by current item is freed.

But is the size of objects is small, you will not notice much impact if you convert the generator to a list. 


```python
filenames = list(Path('bin').glob('*.sh'))
print(filenames)
```

    [PosixPath('bin/clean0111.sh'), PosixPath('bin/database.sh'), PosixPath('bin/fixA.sh'), PosixPath('bin/get-datasets.sh'), PosixPath('bin/git-remove-all.sh'), PosixPath('bin/howmany.sh'), PosixPath('bin/init.sh'), PosixPath('bin/init0111.sh'), PosixPath('bin/link-set.sh'), PosixPath('bin/notebook-mkdocs.sh'), PosixPath('bin/notebook-run.sh'), PosixPath('bin/set-course.sh'), PosixPath('bin/setup.sh'), PosixPath('bin/shellMe.sh'), PosixPath('bin/sort-db.sh'), PosixPath('bin/tidy.sh')]


Alternatively, you can use the [`*args`](https://www.geeksforgeeks.org/args-kwargs-python/) method to pass the results of the generator through to the print function as a set of arguments:


```python
print(*Path('bin').glob('*.sh'))
```

    bin/clean0111.sh bin/database.sh bin/fixA.sh bin/get-datasets.sh bin/git-remove-all.sh bin/howmany.sh bin/init.sh bin/init0111.sh bin/link-set.sh bin/notebook-mkdocs.sh bin/notebook-run.sh bin/set-course.sh bin/setup.sh bin/shellMe.sh bin/sort-db.sh bin/tidy.sh


Let's use `glob` now to get the file permissions of each file `n*` in the directory `bin`:


```python
# use glob to get a list of filenames in the directory bin 
# that end with .sh -> pattern n* using a wildcard
filenames = Path('bin').glob('n*')
for f in filenames:
    print(f'{str(f):25s}')
```

    bin/notebook-mkdocs.sh   
    bin/notebook-run.sh      


#### Exercise 5

* Use `Path` to show the file permissions of all files that end `.md` in the directory `.` (current directory)

### Reading and writing information

The functions for reading and writing information to and from files are:


|command|  purpose|
|---|---|
|`Path.open()`| open a file and return a file descriptor|
|`Path.read_text()`|  read text|
|`Path.write_text()`| write text|
|`Path.read_bytes()`| read byte data|
|`Path.write_bytes()`| write byte data|


### copy

If we are only dealing with reading and writing information in `Path` objects (and those derived from `Path`), then we will normally use `Path.read_text()` and `Path.read_bytes()` for reading text and binary data respectively, and `Path.write_text()` and `Path.write_bytes()` for writing.


```python
from pathlib import Path

# read a text (json) file
json_file = Path('bin/copy/environment.json')
content = json_file.read_text()

print(f'type: {type(content)}')
print(f'content: {content}')
```

    type: <class 'str'>
    content: {"name": "geog0111", "channels": ["conda-forge", "defaults"], "dependencies": ["git", "python>=3.7", "nomkl", "libgdal", "geopandas", "rasterio", "scipy", "gdal", "beautifulsoup4", "fiona", "numpy", "statsmodels", "cartopy", "scikit-image", "netcdf4", "scikit-learn", "matplotlib-base", "pandas", "shapely", "ipyleaflet", "pytest", "seaborn", "hdf5", "flake8", "ipywidgets", "xarray", "black", "folium", "jupyter_console", "pandocfilters", "nbconvert", "jupyterlab", "pandoc", "pyephem", "libnetcdf", "ipykernel", "ipympl", "pip", "yapf", "autopep8", "geemap", "jupyter", "nbgitpuller", "mkdocs", "pycodestyle", "sphinx", "fsspec", {"pip": ["mkdocs-jupyter", "urlpath", "jupyter_contrib_nbextensions", "mknotebooks", "mkdocs-material", "mkdocs-exclude", "mkdocs-git-revision-date-localized-plugin"]}]}


We see that the whole file contents are returned as a string. Sometimes this might be what we want. 

For example, to make a copy of this file in a directory `mydata`, we can simply use:


```python
ifile = Path('bin/copy/environment.json')
ofile = Path('mydata',ifile.name)

# look at ifile size
print(f'{ifile} size: {ifile.stat().st_size} bytes')

# make sure parent directory exists
ofile.parent.mkdir(parents=True,exist_ok=True)
```

    bin/copy/environment.json size: 801 bytes


Note the use of `ifile.name` to refer to the file name and make sure the output filename is the same as the input here.

Similarly for a binary file:


```python
ifile = Path('images/ucl.png')
ofile = Path('mydata',ifile.name)

# look at ifile size
print(f'{ifile} size: {ifile.stat().st_size} bytes')

# make sure parent directory exists
ofile.parent.mkdir(parents=True,exist_ok=True)
```

    images/ucl.png size: 1956 bytes



```python
# copy using read_bytes and write_bytes
# copy data: write_bytes returns number of bytes written
nbytes = ofile.write_bytes(ifile.read_bytes()) #for binary files
print(f'{nbytes} bytes written for {ofile}')
```

    1956 bytes written for mydata/ucl.png



```python
# tidy up and remove the file
ofile.unlink()
ofile.parent.rmdir()
```

#### Exercise 6

Copy the file [`geog0111/cylog.py`](geog0111/cylog.py) to a new directory `myfile` and confirm the size of the file copied. Tidy up by deleting the copied file.

###  `with ... as ...`, open, yaml, json

Sometimes we want to open a stream to a file and then to pass that open stream on to some other package. A [stream](https://en.wikipedia.org/wiki/Standard_streams) is a channel through which we may send and/or receive information. This is different to a file, which is where information may reside, but we may for instance open a stream to write to a file. In Python, we call the object that we get when opening a stream a *file object*.

For instance, in the json example above, we read the text in as a string, but we didn't do anything to parse (i.e. interpret) the information in the file. 

Quite often then, when we need to interface to some interpreter of information in a file, we will use `Path.open()` to provide a file descriptor to pass through. There are various other reasons we might use `Path.open()`, including when we need some more subtle control on the operations.

The `pathlib` function for opening a stream is `Path.open`.

The usual way of opening a file to get the file object is:

    with Path(filename).open('r') as f:
       # do some reading with f
       pass
       
We use the form `with ... as ...` here, so that the file object `f` only exists within this construct and the file is automatically closed when we finish. Codes are spaced in inside the construct, as we have seen in `if ...` or `for ... in ...` constructs.

To use `Path.open()`, we have to distinguish between [modes of opening a file](https://pathlib.readthedocs.io/en/0.5/#pathlib.Path.open). Mostly we will use `r` (read) and `w` (write) for opening a file for reading and writing respectively. Sometimes, we might also use `a` (write append).

Here, we use a file descriptor method `write` to write data to a file, so we use the mode `w`:


```python
from pathlib import Path

ofile = Path('hello/hello_world.txt')
ofile.parent.mkdir(parents=True,exist_ok=True)

mytext = "hello world"

with ofile.open('w') as f:
    f.write(mytext)

# print it out
print(f'{ofile} content\n{"-"*10}\n{ofile.read_text()}')

# tidy
# tidy up and remove the file
ofile.unlink()
ofile.parent.rmdir()
```

    hello/hello_world.txt content
    ----------
    hello world


Two common text formats for certain types of data representation are [json](https://docs.python.org/3/library/json.html) and [`yaml`](http://zetcode.com/python/yaml/). The Python library functions for input and output of both of these use streams: `yaml.safe_load()`, `yaml.safe_dump()`, `json.load()` and `json.dump()` respectively.


```python
import yaml

help(yaml.safe_load)
help(yaml.safe_dump)
```

    Help on function safe_load in module yaml:
    
    safe_load(stream)
        Parse the first YAML document in a stream
        and produce the corresponding Python object.
        
        Resolve only basic YAML tags. This is known
        to be safe for untrusted input.
    
    Help on function safe_dump in module yaml:
    
    safe_dump(data, stream=None, **kwds)
        Serialize a Python object into a YAML stream.
        Produce only basic YAML tags.
        If stream is None, return the produced string instead.
    


Similar functions (`json.load()` and `json.dump()`) exist for json format.

Here, we use the `yaml` package to interpret data in the file `bin/copy/environment.yml` in the variable `env`, which will be a dictionary:


```python
from pathlib import Path
import yaml

# form the file name
yaml_file = Path('bin/copy/environment.yml')

# open stream object 'read'
with yaml_file.open('r') as f:
    env = yaml.safe_load(f)

print(f'env is type {type(env)}')
print(f'env keys: {env.keys()}')
```

    env is type <class 'dict'>
    env keys: dict_keys(['name', 'channels', 'dependencies'])


Now, we dump that information to a json file, using `Path.open()` with `w` (write) mode:


```python
from pathlib import Path
import json

# form the file name
json_file = Path('bin/copy/environment.json')

with json_file.open('w') as f:
    json.dump(env, f)
```

In the examples above, we have done more than just copy: we have interpreted the information from one file format (yaml), and translated it into a file for another format (json). The intermediate data in the Python script was help as a form of dictionary, rather than just the ASCII text string we had read earlier.

#### Exercise 8

* write code to read from the json-format file `bin/copy/environment.json` into a dictionary called `json_data`.
* print out the dictionary keys.
* print the file size of the json-format file in KB to two decimal places.

### Summary test

Let's try to put several of these things together:

#### Exercise 9

* check that the file `images/ucl.png` exists and print modification time and the file size in KB to two decimal places
* make a directory `myfiles` and copy the file `images/ucl.png` to this directory
* show the file size of `myfiles/ucl.png`, the modification time, and the time now
* after that, tidy up by deleting the file `myfiles/ucl.png` and the directory `myfiles`. Confirm that you have done this.

You will need to know how many Bytes in a Kilobyte, and how to [format a string to two decimal places](012_Python_strings.md#String-formating). You will also need to remember how to use [`if` statements](015_Python_control.md#Comparison-Operators-and-if).

## Summary


In this section, we have considered URLs and filenames in some detail, and made use of functions from [`pathlib`](https://docs.python.org/3/library/pathlib.html) to access them. 

The first batch of `Path` commands we saw had much commonality with the core `unix` commands we had previously come across for moving around the file system and finding file information:


|command| unix-equivalent | purpose|
|---|---|---|
|`Path.cwd()`| `pwd` |Return path object representing the current working directory|
|`Path.home()`| `~`| Return path object representing the home directory|
|`Path.stat()`| `ls -l` | return info about the path. File size is `Path.stat().st_size` |
|`Path.chmod()`| `chmod` | change file mode and permissions|
|`Path.glob(pattern)`| `ls *` | Glob the pattern given in the directory that is represented by the path, yielding matching files of any kind|
|`Path.mkdir()`| `mkdir` | to create a new directory at the given path. We have repeatedly used `ofile.parent.mkdir(parents=True,exist_ok=True)` to make sure the directory for an output file exists|
|`Path.rename()`| `mv` | Rename a file or directory to the given target|
|`Path.rmdir()`| `rmdir` | Remove the empty directory|
|`Path.unlink()`| `rm` | Remove the file or symbolic link|
|`Path.touch()` | `touch` | create (zero-sized) or update a file |
|`Path.parent` | `..` | The parent object (one level up in directory tree) |

Some other common utilities we came across were:

|command|  purpose|
|---|---|
|`Path.as_posix()`| Return the object as a posix filename string |
|`Path.exists()` | `True` if exists, `False` if not|
|`Path.parent` |  the parent object (one level up in directory tree), or the directory a file is in |
|`Path.name` | the file name |
|`Path.is_file()` | `True` if object is a file |
|`Path.is_dir()` | `True` if object is a directory |


We have also seen how to open files, and read and write information from files.

|command|  purpose|
|---|---|
|`Path.open()`| open a file and return a file descriptor|
|`Path.read_text()`|  read text|
|`Path.write_text()`| write text|
|`Path.read_bytes()`| read byte data|
|`Path.write_bytes()`| write byte data|



We have learned how to use these with the object-oriented `Path` object to do some simple things like creating and deleting files and directories, getting listings of files and so on. These are such common tasks in coding that you need to spend some time making sure you know at least the basics here. A number of exercises are given to allow you to practice and test yourself, but you should also try to make up your own examples.

