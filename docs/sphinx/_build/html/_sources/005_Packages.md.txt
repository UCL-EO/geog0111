# 005 Packages

## Introduction


### Purpose

In this session, we will learn about importing packages into our code. We will also learn how to install `conda` and `pip` packages.


### Prerequisites

You will need some understanding of the following:


* [001 Using Notebooks](001_Notebook_use.md)


## `import`

Python comes with a good deal of built-in functionality, and that is what we have mainly been using to date. Often though, we need to classes or functions from other packages. Provided these packages are installed in our distribution, we can use them.

The system you should have setup for you includes the packages listed in [`environment.yml`](copy/environment.yml).

When we want to use a non-standard Python package, we must first import it into our codebase. This is done with the `import` directive, e.g.:

    import yaml
    
to import a library called `yaml`. We can then access some function `XX` functions in the package as `yaml.XX`. 


```python
import yaml

help(yaml.safe_load)
```

    Help on function safe_load in module yaml:
    
    safe_load(stream)
        Parse the first YAML document in a stream
        and produce the corresponding Python object.
        
        Resolve only basic YAML tags. This is known
        to be safe for untrusted input.
    


Recall from [Python Introduction](010_Python_Introduction.md) that classes start with a capital letter. So, if we see a variable in `Python such as `path`, we recognise that as a class.

Sometimes we wish to only import certain functions or sub-packages. This is done with the `from` directive. For example to import the class `Path` from the package `pathlib`



```python
from pathlib import Path
```

The class `Path` is now available directly as `Path`, whereas if we had imported it as:

    import pathlib
    
we would have needed to refer to it as `pathlib.Path`. This will over-ride any current definition of the class `Path` in the current code, so be careful not to over-ride things you don't mean to.

## `conda` and `pip`


The Python code you are using is from the [Anaconda](https://docs.anaconda.com/) distribution, and has a package manager [`conda`](https://docs.conda.io/en/latest/). 


You can access `conda` commands in the notebook with the `%conda` directive. For example, to list the environments available to you, run:


```python
%conda env list
```

    # conda environments:
    #
    david                    /shared/groups/jrole001/david/envs/david
    geog0111              *  /shared/groups/jrole001/geog0111/envs/geog0111
    base                     /shared/ucl/apps/miniconda-jhub/4.8.3
    jhubcode                 /shared/ucl/apps/miniconda-jhub/4.8.3/envs/jhubcode
    
    
    Note: you may need to restart the kernel to use updated packages.


The environment you are using will be given with a `*`, along with its location on the file system. It may be either user-owned, in which case it will be somewhere in your own file space, or system-wide. If it is user-owned

If you want to see if a particular package and particular version exists in your distribution, e.g. `gdal`, you can check with:


```python
%conda search -f gdal=3.0.2
```

    Loading channels: done
    # Name                       Version           Build  Channel             
    gdal                           3.0.2  py27hbb2a789_0  pkgs/main           
    gdal                           3.0.2  py36hbb2a789_0  pkgs/main           
    gdal                           3.0.2  py37hbb2a789_0  pkgs/main           
    gdal                           3.0.2  py38hbb2a789_0  pkgs/main           
    
    Note: you may need to restart the kernel to use updated packages.


If you don't want to specify the version, just leave off the `=3.0.2` part.

If a package you need doesn't exist, you can [search for it on the anaconda site](https://anaconda.org/search?q=gdal). 
If it exists as a conda package, you can install it with `conda install`:

    %conda install gdal
    
We will not run this now, as it can take some time to complete, but be aware that this is how to install `conda` packages. In any case, if you are using a system-wide environment, you will not be able to modify the distribution.

Some packages only exist as [`pip` distributions](https://pypi.org/). Before taking a `pip` package, you should make sure that no equivalent anaconda package exists. But in case you need to, you can use:

    %pip install urlpath
    
to install a pip package. You should check that the package will be suitable for your operating system before installing. Use `--user` to do a user install.


```python
%pip install urlpath --user
```

    Requirement already satisfied: urlpath in /shared/groups/jrole001/geog0111/envs/geog0111/lib/python3.7/site-packages (1.1.7)
    Requirement already satisfied: requests in /shared/groups/jrole001/geog0111/envs/geog0111/lib/python3.7/site-packages (from urlpath) (2.24.0)
    Requirement already satisfied: idna<3,>=2.5 in /shared/groups/jrole001/geog0111/envs/geog0111/lib/python3.7/site-packages (from requests->urlpath) (2.10)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /shared/groups/jrole001/geog0111/envs/geog0111/lib/python3.7/site-packages (from requests->urlpath) (1.25.10)
    Requirement already satisfied: certifi>=2017.4.17 in /shared/groups/jrole001/geog0111/envs/geog0111/lib/python3.7/site-packages (from requests->urlpath) (2020.6.20)
    Requirement already satisfied: chardet<4,>=3.0.2 in /shared/groups/jrole001/geog0111/envs/geog0111/lib/python3.7/site-packages (from requests->urlpath) (3.0.4)
    Note: you may need to restart the kernel to use updated packages.


## Summary

In this section, we have learned how to import packages using `import` and `from`. We have seen how to check if a package exists in our conda distribution, and how we can install `conda` and `pip` packages if we need to.
