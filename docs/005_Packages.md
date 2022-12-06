# 005 Packages

## Introduction


### Purpose

In this session, we will learn about importing packages into our code. 

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
    


We will learn in [Python Introduction](010_Python_Introduction.md) that classes start with a capital letter. So, if we see a variable in `Python such as `path`, we should recognise that as a class.

Sometimes we wish to only import certain functions or sub-packages. This is done with the `from` directive. For example to import the class `Path` from the package `pathlib`



```python
from pathlib import Path
```

The class `Path` is now available directly as `Path`, whereas if we had imported it as:

    import pathlib
    
we would have needed to refer to it as `pathlib.Path`. This will over-ride any current definition of the class `Path` in the current code, so be careful not to over-ride things you don't mean to.

#### Exercise 1

Make and run a Python cell that imports the class `Loader` from the package `yaml` and show the help text for this.

## Summary

In this section, we have learned how to import packages using `import` and `from`.
    
|  command | purpose  |   
|---|---|
| `import yaml` | import the package `yaml`|
| `from pathlib import Path`  |  import the method/ class `Path` from the package `pathlib` |  



