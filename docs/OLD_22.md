# 022 OLD


## Introduction


### Purpose

In the previous sessions, we used [`pathlib`](https://docs.python.org/3/library/pathlib.html) and [`urlpath`](https://github.com/chrono-meter/urlpath) to access files and do basic reading and writing operations. 

Often we need to apply an interpreter to the data we access. This might be text formats such as [`json`](https://docs.python.org/3/library/json.html) or [`yaml`](https://python.land/data-processing/python-yaml) that we have already seen. Or they might be more complex binary formats such as we use for geospatial data. We have come across MODIS files in `hdf` format, for instance. 

In this session, we will extend this to deal with reading and writing such geospatial files.

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

You will need to recall details from [020_Python_files](020_Python_files.md) and [021_URLs](021_URLs.md).

### Test

You should run a [NASA account test](004_Accounts.md) if you have not already done so.

##  MODIS

We have previously come across MODIS data and how to download it to the local system. Let's look deeper into these datasets now.

As a start on this, let's first access a MODIS file from the web, as we did in [021_URLs](021_URLs.md). We will use [`modisFile`](geog0111/modisUtils.py) to access the MODIS files.


```python
from geog0111.modisUtils import modisFile
# settings

modinfo = {  
    'product'  : 'MCD15A3H',
    'year'     : 2020,
    'month'    : 1,
    'day'      : 5,
    'tile'     : 'h08v06'
}

filename = modisFile(year, month, day,tile,verbose=False)
print(filename)
```

    /Users/plewis/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf


### `gdal`


The MODIS files are in `hdf` format, and as we have noted, we do not generally want direct access to the raw (byte) information. Instead we must use some package to interpret the data. 

We can use the package [`gdal`](https://gdal.org/python/) to access information from these and other geospatial files. We will explore the contents of MODIS files in a later session, but for now, we can note that each MODIS file contains a set of sub datasets.

Basic use of `gdal` in this context is:

    g = gdal.Open(filename.as_posix())
    
where `filename.as_posix()` is a string of the filename we want open the file in `gdal`. If this returns None, there has been a problem opening the file, so we might check that.

Then

    g.GetSubDatasets()
   
returns a list of sub-dataset information. Each item in the list is a tuple of two strings. In each, the first is the full name of the sub-dataset, and the second a text descriptor of the dataset. We call these `filename,name` below.

We read the dataset with:

    gsub = gdal.Open(filename)
    data = gsub.ReadAsArray()
    
In the illustration below, we will examine only the first sub-dataset `g.GetSubDatasets()[0]`.


```python
import gdal
from geog0111.modisUtils import modisFile
# settings

modinfo = {  
    'product'  : 'MCD15A3H',
    'year'     : 2020,
    'month'    : 1,
    'day'      : 5,
    'tile'     : 'h08v06'
}

filename = modisFile(year, month, day,tile,verbose=False)

if filename:
# open the local file associated with the dataset
    g = gdal.Open(filename.as_posix())
    if g:
        # get the first SDS only for illustration
        filename,name = g.GetSubDatasets()[0]
        print(f'dataset info is: {name}')
        # read the dataset
        gsub = gdal.Open(filename)
        if gsub:
            data = gsub.ReadAsArray()
        print(f'dataset read is shape {data.shape} and type {type(data)}')
```

    dataset info is: [2400x2400] Fpar_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)
    dataset read is shape (2400, 2400) and type <class 'numpy.ndarray'>


#### Exercise 1

    name = '[2400x2400] Fpar_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)'

* Take the string variable `name` above, split it to obtain the second field (`Fpar_500m` here) and store this in a variable `sds_name`
* Write a function called `get_data` that reads an HDF (MODIS) filename, and returns a dictionary of all of the sub-datasets in the file, using `ReadAsArray()`. The dictionary keys should correspond to the items in  `sds_name` above.
* test the code by showing the keys in the dictionary returned and the shape of their dataset

You will need to recall how to split a string, that was covered in [013 Python string methods](013_Python_string_methods.md#split()-and-join()). You will also need to recall how to [loop over a dictionary](016_Python_for.md#looping-over-dictionaries,-and-assert). We saw how to find the shape of the dataset returned above (`.shape`).

## Summary

In this section, we have used `Path` and `URL` classes to read and write text and binary files. We have combined these ideas with earlier work to access MODIS datafiles and other text and binary datasets. For data we access through a URL, we can do file operations on a cached version of the file. We have refreshed our memory of some of the earlier material, especially string formatting.

We have learned how to use `gdal` to look at the sub-datasets in an HDF file and also how to read them.

You should now have some confidence in these matters, so that if you were set a task of downloading and saving datasets, as well as other tasks such as finding their size, whether the exists or not, you could do this. 

Remember:

Modis library

            from  geog0111.modis import Modis
            modis = Modis(**kwargs)
            

            get_url(**kwargs) method of geog0111.modis.Modis instance
                Get URL object list for NASA MODIS products
                for the specified product, tile, year, month, day

                Keyword Arguments:

                verbose:  bool
                product : str e.g. 'MCD15A3H'
                tile    : str e.g. 'h08v06'
                year    : str valid 2000-present
                month   : str 01-12
                day     : str 01-(28,29,30,31)

`gdal`

| Command | Comment |
|---|---|
|`g = gdal.Open(filename)` | Open geospatial file `filename` and return `gdal` object `g` (`None` if file not opened correctly)|
|`g.GetSubDatasets()` | Get list of sub-datasets from `gdal` object `g`| 
|`g.ReadAsArray()` | Read dataset from `gdal` object `g` into array |
