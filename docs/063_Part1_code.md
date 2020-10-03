# Assessed Practical Part A

## Introduction

### Task overview

In this task, you will be writing codes that download and interpret (convert units) for two datasets of the Del Norte catchment in Colorado, USA for the years 2015-2019 inclusive. The main coding exercise is a Python script that when you run it, downloads the data and stores them in CSV format files. In a notebook, you run the script and show the results. In a second notebook, you produce plots of the datasets. You save the code and two notebooks to PDF files, and submit the work.

### Submission

The due dates for the two formally assessed pieces of coursework are:

        Part A: 16th Nov, 2020 (50% of final mark) - first Monday after reading week.
        Part B: 11th Jan, 2021 (50% of final mark) - first day of term 2

The practical comes in two parts : (A) data preparation (50%); (B) modelling (50%). 

Submission is through the usual Turnitin link on the [course Moodle page](https://moodle-1819.ucl.ac.uk/course/view.php?id=2796#section-4). You must submit your notebooks and codes as `pdf` files.


### Checklist
    
    * You should be submitting 3 PDF files:
        * work/get_DelNorte_data.py
        * notebook showing running of running work/get_DelNorte_data.py
        * notebook showing graphs of Del Norte data
    * None of these files should be more than a few pages long: we do not want you to print or submit the datasets you download.


##  Background

The hydrology of the Rio Grande Headwaters in Colorado, USA is snowmelt dominated. It varies considerably from year to year and may very further under a changing climate. One of the tools we use to understand monitor processes in such an area is a mathemetical ('environmental') model describing the main physical processes affecting hydrology in the catchment. Such a model could help understand current behaviour and allow some prediction about possible future scenarios. 

In part 2 of your assessment you will be using, calibrating and validating such a model that relates temperature and snow cover in the catchment to river flow. 
![](https://www.blm.gov/sites/blm.gov/files/hero_backgrounds/NM_Rio_Grande_del_Norte_Sign_640.jpg)

We will use the model to describe the streamflow at the Del Norte measurement station, just on the edge of the catchment. You will use environmental (temperature) data and snow cover observations to drive the model. You will perform calibration and testing by comparing model output with observed streamflow data.

### Del Norte

Further general information is available from various [websites](http://www.usclimatedata.com/climate.php?location=USCO0103), including [NOAA](http://www.ncdc.noaa.gov).

![www.coloradofishing.net](http://www.coloradofishing.net/images/fishtails/ft_riogrande3.jpg)



You can visualise the site Del Norte 2E  [here](http://mesonet.agron.iastate.edu/sites/site.php?station=CO2184&network=COCLIMATE).




## Requirements for this submission

In this part of the assessment, you will need to write computer codes to read, interpret and plot the various environmental datasets we will be using in Part 2,


To complete this practical you will need to access, read, save and plot the following datasets:

* **Stream discharge** from the USGS [http://waterdata.usgs.gov](http://waterservices.usgs.gov/nwis/dv/?sites=08220000&format=rdb&startDT=2001-01-01&parameterCd=00060).

* **Temperature**: Temperature data from:
    * [Berkley Earth](http://berkeleyearth.lbl.gov/station-list/stations/32442) OR
    * the Colorado State [Climate data site](http://climate.colostate.edu/data_access.html) OR
    * a [local copy of the data](https://raw.githubusercontent.com/UCL-EO/geog0111/master/data/delNorteT.dat) from the Colorado State Climate data site.
    
The reason for giving multiple access methods for the temperature data is that we have founbf the [Berkley Earth](http://berkeleyearth.lbl.gov/station-list/stations/32442) site to be sometime unresponsive. The problem with the Colorado State [Climate data site](http://climate.colostate.edu/data_access.html) is that you cannot directly query or download the data. Instead you will need to manually save the data, most easily by copying and pasting the data columns into a file. The final option is a copy of the data from the Colorado State [Climate data site](http://climate.colostate.edu/data_access.html). We try to keep this up to date on an annual basis, but cannot guarantee that. You may choose which method you use, but you may find it useful to explore the climate data sites further rather than simply relying on the dataset we have prepared.

## Access

You should examine the data on the site links above and make sure you understand the file format and data characteristics. 

#### Units 

You need to make a note of the units the physical parameters (temperature, discharge etc.) datasets are presented in as you will need to convert them to the units we specify below. The temperature data from the Colorado State [Climate data site](http://climate.colostate.edu/data_access.html) comes in Fahrenheit.

#### Header

Make a note of the number of 'header' lines in the files (if any) and the column headings (if given) as you may need to specify these when reading the dataset.

#### Data access

Before going further, you should use a Jupyter notebook or iPython in a terminal to make sure you can access and interpret these files. There are only two files, so this should not take too long. 

You will most likely want to use `pandas` to do this, and should have gained experience in this already in the course. Try first to use the dataset URL to load into `pandas`, except if you download the Colorado State [Climate data site](http://climate.colostate.edu/data_access.html) to a file (then, read from that file). You may need to try out several options in reading the data into `pandas` if it does not automatically load correctly. In that case, remember that you can skip header lines, and get `pandas` to read only the data lines. You should be able to print the pandas dataframe to see that the data in your table corresponds to what you can see when you access data with a URL.



## Task 1: Data preparation code

In this task, you must write a Python script that you should call `work/get_DelNorte_data.py`. 

* Within this file, create a function called `get_DelNorte_data` that has the following argument:

        year     : integer, between 2000 and the year previous to now (i.e. not this year)
    
  and that returns a dictionary OR `pandas` dataframe containing:

        doy      : array of 365/366 values with the day of year
        flow     : stream flow data for each in units of megalitres/day 
                   (ML/day i.e. units of 1000000 litres a day)
        maxt     : Maximum daily temperature in Celcius (C)

  You can use multiple sub-functions that you call from you function, should you so wish.
  
* Within this file `work/get_DelNorte_data.py` create a function called `write_DelNorte_data` that takes as argument:

        year     : integer, between 2000 and the year previous to now (i.e. not this year)

  then makes a call to `get_DelNorte_data` for the year specified, and saves the dataset in CSV format to a file `work/DelNorte_data_YYYY.csv` each year (replace `YYYY` by the year)

* Within this file `work/get_DelNorte_data.py` create a function called `main` that runs `get_DelNorte_data` for the years 2015 to 2019 inclusive. 

* Construct the Python script so that when you run `work/get_DelNorte_data.py` from a command line, it executes the `main()` function.

* Make the file `work/get_DelNorte_data.py` executable

* In a Python notebook, run the script `work/get_DelNorte_data.py`, and show the size of the files `work/DelNorte_data_*.csv` created.

Hints: Don't forget to include the various packages you need at the top of the file. Don't forget to put docstrings and comments in your file and functions.

## Task 2: Data visualisation

* In a Python notebook, produce plots for the Del Norte site of:

    1. Stream flow data for each year 2015 to 2019 inclusive (in units of megalitres/day - ML/day i.e. units of 1000000 litres a day), as a function of day of year.
    2. Maximum daily temperature in Celcius (C) for each year 2015 to 2019 inclusive as a function of day of year.

You should position the 4 years of data in a 2x2 grid of sub-plots. You code should be well-commented to explain what you are doing. The graphs should be clear, with appropriate titles and axis labels.

### Coursework

You need to submit you coursework in the usual manner by the date given above.

You **must** work individually on this task. If you do not, it will be treated as plagiarism. By reading these instructions for this exercise, we assume that you are aware of the UCL rules on plagiarism. You can find more information on this matter in your student handbook. If in doubt about what might constitute plagiarism, ask one of the course conveners.



### Structure of the Report

The required elements of the report are:

1. Code function `get_DelNorte_data` for temperature and river discharge data download, reading and putting into a dictionary `[40%]`. 
2. Code function `write_DelNorte_data` saves the dataset for a given year to a file in CSV format `[10%]`.
3. Code function `main` that runs get_DelNorte_data for the years 2015 to 2019 inclusive `[10%]`.
4. Additional features of `work/get_DelNorte_data.py` for running as a script `[5%]`.
5. Notebook 1: Demonstration of running the script `work/get_DelNorte_data.py` and the outputs `[15%]`.
6. Notebook 2: Stream flow data plots `[10%]`.
7. Notebook 2: Maximum daily temperature data plots `[10%]`.
    
The figures in brackets indicate the percentage of marks associated with each part. Even if, for some reason, you were unable to generate outputs from your code, you should still be able to pick up marks by attempting all or most of the sections. Most of the marks are given for your computer code, so make sure this is clearly laid out and well-documented. See the comments below regarding what we expect of submitted codes.

### Computer Code

#### General requirements

You will obviously need to submit computer codes as part of this assessment. Some flexibility in the style of these codes is to be expected. For example, when asked to write a function, so students might choose to modularise and test the problem further and have multiple sub-functions that are finally called from the required function. This is fine to do, and can often be a good idea if the problem is complex or there are re-usable modular parts of code you might want to use (e.g. for printing). 

If you want to achieve distinction-level marks, then, on top of the main requirements we lay out here, we would be looking for features such as: maturity and detail in testing your codes; excellent code style; excellent presentation; and flexibility in the code (e.g. don't fix variable you can make variables or keywords).

All codes needed to demonstrate that you have performed the core tasks are required to be included in the submission. 

All codes should be well-commented. Part of the marks you get for code will depend on the adequacy of the document strings and commenting.

#### Degree of original work required and plagiarism

If you use a piece of code verbatim that you have taken from the course pages or any other source, **you must acknowledge this** in comments in your text. **Not to do so is plagiarism**. Where you have taken some part (e.g. a few lines) of someone else's code, **you should also indicate this**. If some of your code is heavily based on code from elsewhere, **you must also indicate that**.

Some examples. 

The first example is guilty of strong plagiarism, it does not seek to acknowledge the source of this code of code from one of the course pages, even though it is just a direct copy, pasted into a method called `model()`:


```python
def model(tempThresh=9.0,K=2000.0,p=0.96):
    '''...'''
    import numpy as np
    meltDays = np.where(temperature > tempThresh)[0]
    accum = snowProportion*0.
    for d in meltDays:
        water = K * snowProportion[d]
        n = np.arange(len(snowProportion)) - d
        m = p ** n
        m[np.where(n<0)]=0
        accum += m * water
    return accum
```

This is **not** acceptable.

This would be better as:


```python
'''
This code is taken directly from
"Modelling delay in a hydrological network"
by P. Lewis http://www2.geog.ucl.ac.uk/~plewis/geogg122/DelNorte.html
and wrapped into a method.
'''
def model(tempThresh=9.0,K=2000.0,p=0.96):
    '''...'''
    # my code: make sure numpy is imported
    import numpy as np

    # code below verbatim from Lewis REF XXX
    meltDays = np.where(temperature > tempThresh)[0]
    accum = snowProportion*0.
    for d in meltDays:
        water = K * snowProportion[d]
        n = np.arange(len(snowProportion)) - d
        m = p ** n
        m[np.where(n<0)]=0
        accum += m * water
    # my code: return accumulator
    return accum
```

Now, we acknowledge that this is in essence a direct copy of someone else’s code, and clearly state this. We do also show that we have added some new lines to the code, and that we have wrapped this into a method.

In the next example, we have seen that the way m is generated is in fact rather inefficient, and have re-structured the code. It is partially developed from the original code, and acknowledges this:


```python
'''
This code after the model developed in
"Modelling delay in a hydrological network"
by P. Lewis
http://www2.geog.ucl.ac.uk/~plewis/geogg122/DelNorte.html

My modifications have been to make the filtering more efficient.
'''
def model(tempThresh=9.0,K=2000.0,p=0.96):
    '''...'''

    # my code: make sure numpy is imported
    import numpy as np

    # code below verbatim from Lewis unless otherwise indicated
    meltDays = np.where(temperature > tempThresh)[0]
    accum = snowProportion*0.

    # my code: pull the filter block out of the loop
    n = np.arange(len(snowProportion))
    m = p ** n

    for d in meltDays:
        water = K * snowProportion[d]

        # my code: shift the filter on by one day
        # ...do something clever to shift it on by one day

        accum += m * water
    # my code: return accumulator
    return accum
```

This example makes it clear that significant modifications have been made to the code structure (and probably to its efficiency) although the basic model and looping comes from an existing piece of code. It clearly highlights what the actual modifications have been. Note that this is not a working example! Note also that this is a poor example of a function, as there is no real document string and little comment on the code operation.

We stress that this must be your own work. We do not want you to get anyone else to significantly helped you to develop the code (e.g. written the main part of it for you & you've just copied that with some minor modifications). This is not acceptable, but if for some reason it does happen, you must acknowledge it in your submission.

If you take a piece of code from somewhere else and all you do is change the variable names and/or other cosmetic changes, you **must** acknowledge the source of the original code (with a URL if available).

Plagiarism in coding is a tricky issue. One reason for that is that often the best way to learn something like this is to find an example that someone else has written and adapt that to your purposes. Equally, if someone has written some tool/library to do what you want to do, it would generally not be worthwhile for you to write your own but to concentrate on using that to achieve something new. Even in general code writing (i.e. when not submitting it as part of your assessment) you and anyone else who ever has to read your code would find it of value to make reference to where you found the material to base what you did on. The key issue to bear in mind in this work, as it is submitted ‘as your own work’ is that, to avoid being accused of plagiarism and to allow a fair assessment of what you have done, you must clearly acknowledge which parts of it are your own, and the degree to which you could claim them to be your own.

For example, based on ... is absolutely fine, and you would certainly be given credit for what you have done. In many circumstances 'taken verbatim from ...' would also be fine (provided it is acknowledged) but then you would be given credit for what you had done with the code that you had taken from elsewhere (e.g. you find some elegant way of doing the graphs that someone has written and you make use of it for presenting your results).

The difference between what you submit here and the code you might write if this were not a piece submitted for assessment is that you the vast majority of the credit you will gain for the code will be based on the degree to which you demonstrate that you can write code to achieve the required tasks. There would obviously be some credit for taking codes from the coursenotes and bolting them together into something that achieves the overall aim: provided that worked, and you had commented it adequately and acknowledge what the extent of your efforts had been, you should be able to achieve a pass in that component of the work. If there was no original input other than vbolting pieces of existing code together though, you be unlikely to achieve more than a pass. If you get less than a pass in another component of the coursework, that then puts you in danger of an overall fail.

Provided you achieve the core tasks, the more original work that you do/show (that is of good quality), the higher the mark you will get. Once you have achieved the core tasks, even if you try something and don’t quite achieve it, is is probably worth including, as you may get marks for what you have done (or that fact that it was a good or interesting thing to try to do).

#### Documentation

Note: All methods/functions and classes must be documented for the code to be adequate. Generally, this will contain:

   - some text on the purpose of the method (/function/class)

   - some text describing the inputs and outputs, including reference to any relevant details such as datatype, shape etc where such things are of relevance to understanding the code.

   - some text on keywords, e.g.:


```python
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)

    Example taken verbatim from:
    http://www.python.org/dev/peps/pep-0257/
    """
    if imag == 0.0 and real == 0.0: return complex_zero

```

You should look at the [document on good docstring conventions](http://www.python.org/dev/peps/pep-0257/) when considering how to document methods, classes etc.

To demonstrate your documentation, you **must** include the help text generated by your code after you include the code. e.g.:


```python
def print_something(this,stderr=False):
    '''This does something.

    Keyword arguments:
    stderr -- set to True to print to stderr (default False)
    '''

    if stderr:
        # import sys.stderr
        from sys import stderr

        # print to stderr channel, converting this to str
        print >> stderr,str(this)

        # job done, return
        return

    # print to stdout, converting this to str
    print (str(this))

    return

```

Then the help text would be:


```python
help(print_something)
```

    Help on function print_something in module __main__:
    
    print_something(this, stderr=False)
        This does something.
        
        Keyword arguments:
        stderr -- set to True to print to stderr (default False)
    


The above example represents a ‘good’ level of commenting as the code broadly adheres to the style suggestions and most of the major features are covered. It is not quite ‘very good/excellent’ as the description of the purpose of the method (rather important) is trivial and it fails to describe the input this in any way. An excellent piece would do all of these things, and might well tell us about any dependencies (e.g. requires sys if stderr set to True).

An inadequate example would be:


```python
def print_something(this,stderr=False):
    '''This prints something'''
    if stderr:
        from sys import stderr
        print >> stderr,str(this)
        return
    print (str(this))
```

It is inadequate because it still only has a trivial description of the purpose of the method, it tells us nothing about inputs/outputs and there is no commenting inside the method.

#### Word limit

There is no word limit per se on the computer codes, though as with all writing, you should try to be succint rather than overly verbose.

#### Code style

A good to excellent piece of code would take into account issues raised in the [style guide](http://www.python.org/dev/peps/pep-0008/). The ‘degree of excellence’ would depend on how well you take those points on board.
