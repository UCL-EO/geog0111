# 070 Summary

## Introduction

We have now reached the end of the course material, but hopefully not the end of your learning to code and to manipulate geospatial data. At the start of the course, we assumed you had never done any programming. Now, if you have been through the material and able to complete most of the exercises, formative assessments and coursework, you should be a competent (or better!) coder. We use this final section just to reiterate to you what you have learned. You will see that it a vast amount! We hope you will use this basis as a foundation to go further with your coding, to enable you to get the computer to do what you want, to test out your ideas, rather than being limited by what is currently available. If you need to learn a new some new languages such as javascript or matlab, you will find them very similar to Python. The same will apply to learning any other coding language: once you have a good grasp of the basics and what you can do in programming, you are in control. 

We know that there is often a steep learning curve for people new to coding, but we trust you have been able to deal with that and put the effective learning time in to make best use of the course. We also hope that the support from the course tutors and supporting doctoral students has been effective. We hope that you have found the experience enabling.

## Recap

As a brief recap on what you have learned:

### Course Basics

####  001 Using Notebooks

[001 Using Notebooks](001_Notebook_use.md): 
    Use of Jupyter notebooks; code and maskdown cells; use of markdown;  
    
#### 002 Unix

[002 Unix](002_Unix.md): Bash commands in notebooks; bash cells; Unix commands:


| cmd  |  meaning  | example use | 
|---|---|--|
| `~`  |  twiddle / tilde -  home | `cd ~/geog0111` |
| `.`  |  dot  - current directory | `cd .` |
| `..`  |  dot dot  - one level up directory | `cd ..` |
| `*`  | wildcard   | `ls R*` |
| `cd`  | change directory   | `cd ~/geog0111` |
| `pwd`  | print working directory | `pwd` |
| `ls`  | list | `ls README.md` |
| `ls -l`  | long list | `ls -l README.md` |
| `ls -lh`  | human-readable long list |`ls -lh README.md` |
| `chmod`  | change mode (permissions) | `chmod 644 README.md` |
| `rm` | remove | `rm work/n*` |
| `755` | `rwxr-xr-x` | `chmod 755 bin/*` |
| `644` | `rw-r--r--` | `chmod 644 README.md` |    

#### 003 Getting help

[003 Getting help](003_Help.md): How to get and read help document strings; the importance of documentation for methods; some examples of Python, mainly with the type `list`:


|  command | purpose  |   
|---|---|
| `help(m)`  |  print document string for method `m` |  
| `m?`  |  print short document string for method `m` |  
| `list`  |  Python data type for lists |  
| `list.append()`  | append item to list  |   
| `list.clear()`  | clear item from list  |  
| `list.sort`  | in-line list sort  |  
| `range(start,stop,step)`  | list-like generator for integers from `start` to (but not including) `stop` in steps of `step`  |      


#### 004 Accounts

[004 Accounts](004_Accounts.md): Storing / resetting and testing NASA Earthdata login.
    
|  command | purpose  |   
|---|---|
| `l = Cylog(sites); test = l.login()`  |  set / run login for list of URLs `sites` |  
| `cy = Cylog(sites,force=True); test = l.login()`  | reset / run login for list of URLs `sites` |
| `test_login(True)`  |  test the login by pulling a dataset from the NASA site|  


#### 005 Packages

[005 Packages](005_Packages.md); import packages using `import` and `from`.
    
|  command | purpose  |   
|---|---|
| `import yaml` | import the package `yaml`|
| `from pathlib import Path`  |  import the method/ class `Path` from the package `pathlib` |  



### Core Concepts


#### 010 Variables, comments and print
[010 Variables, comments and print()](010_Python_Introduction.md)


Rules and conventions for symbol names.

|  command | purpose  |   
|-|---|
| `#` | hash symbol, followed by comments|
| `print()` | print function|
| `\n` | newline character|
| `\t` | tab character|
| `varname = value` | set variable `varname` to `value`|
|`__doc__, __main__` | special method names |

Variables start with a lower case character and classes start with capitals

Reserved keywords:

                False      class      finally    is         return
                None       continue   for        lambda     try
                True       def        from       nonlocal   while
                and        del        global     not        with
                as         elif       if         or         yield
                assert     else       import     pass
                break      except     in         raise



#### 011 Data types

[011 Data types](011_Python_data_types.md) 


|core data types| example |
|---|-|
|`int`| `x = 10`|
|`float`| `x = 10.0`|
|`str`| `x = "hello world"`|
|`bool`| `x = False` |

    and how to convert ('cast') between then, where this is feasible:

| cast functions |
|---|
|`int()`|
|`float()`|
|`str()`|
|`bool()`|

    Other functions:

|  command | purpose  |   
|-|---|
| `type(v)` | data type of object `v`|
| `len(v)` | length of object `v` (e.g. `str`) |

    We have learned truth tables to list logical operations:


| A  | B  | A and B  | 
|:---:|:---:|:---:|
|  T |  T |  T | 
|  T |  F |  F | 
|  F |  T |  F | 
|  F |  F |  F | 



| A  | B  | A or B  | 
|:---:|:---:|:---:|
|  T |  T |  T | 
|  T |  F |  T | 
|  F |  T |  T | 
|  F |  F |  F | 

| A  | not A  | 
|:---:|:---:|
|  T | F | 
|   F |  T | 
    
#### 012 String formatting
    
[012 String formatting](012_Python_strings.md)

| item | description |
|---|-|
| `"'"` | single quote as a string |
| `'"'` | double quote as a string |
| `"\\"` | backslash as a string (escaped) in string|
| ''' ... ''' | multiple line string |
| `*` | string multiplication e.g. `"0"*2` -> `"00"` |
| `+` | string addition e.g. `"0" + "1"` -> `"01"`|
| `str.format()` | insert items in string e.g. `"{x}".format(x=1)` -> "1"|
| `f"..."`| f-string, e.g. `x=1`, `f"{x}"` -> `"1"|

#### 013 Python string methods

[013 String methods](013_Python_string_methods.md)


| item | description |
|---| -|
| `str.replace(a,b)` | replace occurrences of `a` with `b` in `str` |
| `str.strip(a)` | strip off any occurrences of `a` on left or right ends of `str` (also `lstrip`,`rstrip`)|
| `str.split(a)` | split `str` into list, using `a` as the separator, e.g. `"1:2".split(":")` -> `["1","2"]`
| `a.join(l)` | join the string items in list `l` into a string with `a` as the separator, e.g. `"x".join(["1","2"])` -> `"1x2"` |
| `str[start:stop:step]` | slice `str` and return characters `start` to (but not including) `stop` skipping `step` values, e.g. `"hello"[1:2]` -> `e`|



#### 104 Groups

[014 Python groups](014_Python_groups.md)

| symbol | description | example| access example |
| ---|---|---|---|
| `()` | `tuple`: low level group of items accessed by index. Cannot change once set| `(1,2,3)` | `(1,2)[1]` -> `[2]`|
| `[]`| `list`: group of items accessed by index with range of methods. Can change, sort etc. | `[1,2,3]`| `[1,2][1]` -> `[2]` |
| `{}` | `dict`: dictionary, a group of items accessed by key | `{"a" : 1}` | `{"a" : 1}["a"]` -> `1`|
| `[[],[]]` | hierarchical (multi-dimensional) list | 
| `[{},{}]` | list of dictionaries |
| `{"a":[],"b":[]}` | dictionary of lists|

List methods:

| method | description | example | result |
|---|---|---|---|
|`list.index(i)`|find index of value `i` in `list` |`[9,10,11].index(10)`| `1`|
| `list.extend(l)` | in-place extend `list` with list `l` | `x = [9,10,11]; x.extend([12,13])`| `x` -> `[9,10,11,12,13]`|
| `list.append(l)` | in-place append `list` with list `l` | `x = [9,10,11]; x.append([12,13])`| `x` -> `[9,10,11,[12,13]]`|
| `list.sort(l)` | in-place sort `list`  | `x = [10,9,11]; x.sort()`| `x` -> `[9,10,11]`|


Dictionary methods:

| method | description | example | result |
|---|---|---|---|
| `a.keys()` | keys in dictionary `a` | `d={"a":1,"b":2};d.keys()` | `['a', 'b']`|
| `a.values()` | values in dictionary `a` | `d={"a":1,"b":2};d.values()` | `[1, 2]`|
| `a.items()` | items `(key,value)` in dictionary `a` | `d={"a":1,"b":2};d.items()` | `[('a', 1), ('b', 2)])`|
| `dict(zip(a,b))` | form a dictionary from keys in list `a` and items in list `b` | `dict(zip(["a","b"],[1,2]))` | `{'a': 1, 'b': 2}`|
| `a.update(d)` | update dictionary `a` with dictionary `d`| `a={"a":1};d={"b":2};a.update(d)` | `a` -> `{'a': 1, 'b': 2}`|

## A few items to complete ... wait for update
* [020_Python_files](020_Python_files.md)
* [021 Streams](021_Streams.md)
* [022 Read write files](022_Read_write_files.md)
* [023 Plotting](023_Plotting.md)
* [024_Image_display](024_Image_display.md)
* [030_NASA_MODIS_Earthdata](030_NASA_MODIS_Earthdata.md)
