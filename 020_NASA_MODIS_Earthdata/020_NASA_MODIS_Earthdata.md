# NASA MODIS Earthdata


## Introduction

### Purpose 

In this notebook, we will use high-level codes from `geog0111` to familiarise ourselves with downloading and interpreting NASA MODIS datasets from [`NASA EarthData`](https://urs.earthdata.nasa.gov). We will also be visualising these data in this notebook.

We will be **introducing NASA MODIS land products**, and viewing the MODIS LAI product as an example. This notebook should serve as an introduction to accessing similar products from Earthdata.

The aim of the codes here is not to provide an exhaustive interface to MODIS data products, although the same scripts should be useable for most, if not all similar products. Rather, it is to use these high-level codes to easily access and visualise the data to understand their properties. 

Neither is it to develop or use an [API](https://en.wikipedia.org/wiki/Application_programming_interface) to access the data. If all you want is to get hold of some data product for some defined location and time, then you might use an API such as [Appeears](https://lpdaacsvc.cr.usgs.gov/appeears/).

Students who take the [GEOG0111 course](https://github.com/UCL-EO/geog0111) will develop codes along similar lines to this later in the term, so for them, these notes also illustrate some of the things they will be able to do when you have finished this course. For them, we will *look under the bonnet* of such codes, and learn how to develop them. For others, they can use these codes as they stand to access MODIS data via Earthdata.

### Prerequisites

Before you can use the material in this notebook, you will need to register as a user at the [`NASA EarthData`](https://urs.earthdata.nasa.gov/users/new).

Once you have done that, make sure you know your `username` and `password` ready for below.

The are no assumptions that you know any python code at this point: the use of code should be high enough level that you can easily understand what is going on, and use the constructs shown to modify the codes to your purpose.

For completeness, we list the python and other codes below.

We do assume that you have basic familiarity with using [Jupyter notebooks](001_Notebook_use.md).

You should run through the [Credentials](#Credentials) section below before proceeding further with these notes.

### Credentials

We will store your credentials for [`NASA EarthData`] (https://urs.earthdata.nasa.gov/users/new) to allow easier data downloading. 

**N.B. using `cylog().login()` is only intended to work with access to NASA Earthdata and to prevent you having to expose your username and password in these notes**.


In the `geog0111` library, we have a Python class called `cylog`, written to allow easier persistent interface to NASA download servers.

First, we import `cylog` from the `geog0111` library.

Run the cell below:


### Test
You will need a web login to NASA Earthdata and to have stored this using `cylog` according to [004_Accounts](004_Accounts.md) for the site `https://e4ftl01.cr.usgs.gov`. We can test this with the following code ius yoiu set do_test to True:


```python
from geog0111.gurlpath import URL
# ping small (1.3 M) test file
site='https://e4ftl01.cr.usgs.gov'
test_dir='MOLA/MYD11_L2.006/2002.07.04'
test_file='MYD11_L2*0325*.hdf'
# this interprets the wildcards to get at a suitable test file
url = next(URL(site,test_dir).glob(test_file))[0]
# test ping returns True
assert url.ping(verbose=False) == True
```

If this fails, set `verbose` to `True` to see what is going on, then if you can;'t work it out from there, go back to [004_Accounts](004_Accounts.md) and sort the login for NASA Earthdata the site `https://e4ftl01.cr.usgs.gov`.

### Earthdata login

Run the cell below, and enter your `username` and `password` if prompted.


```python
site='https://e4ftl01.cr.usgs.gov'
cy = Cylog(site,init=True,verbose=True)

# check this has worked
print('has this worked?',test())
```

    None
    has this worked? True


    --> generating key file in /Users/plewis/.cylog
    --> --> saving key file to /Users/plewis/.cylog/.cylog.npz



```python
site='https://e4ftl01.cr.usgs.gov'
# uncomment this line to force re-entry
#done=cy.login(force=True)
```

    --> forcing re-entry of password for https://e4ftl01.cr.usgs.gov


    --> user login required for https://e4ftl01.cr.usgs.gov <--
    Enter your username: lewis0585
    please type your password········
    please re-type your password for confirmation········
    password created


    --> ciphering key from key file /Users/plewis/.cylog/.cylog.npz
    --> --> writing ciphers to file
    --> --> done writing ciphers to file


If you want to force the code to let you re-enter your credentials (e.g. you got it wrong before, or have changed them, or the test fails), then change the call to:

    cy = cylog(force=True)
    
and re-run.

`cylog` stores your username and password in a file that only you can read. We can use this as a convenient way to pull some NASA MODIS data.

### Code used



In the code below, we use the following python constructs:

* [`import` modules](https://www.w3schools.com/python/python_modules.asp)
* [Error trapping: `try ... except`](https://www.w3schools.com/python/python_try_except.asp#:~:text=The%20try%20block%20lets%20you,the%20try%2D%20and%20except%20blocks.)
* [`assert`](https://www.w3schools.com/python/ref_keyword_assert.asp)
* [`dictionary`](https://www.w3schools.com/python/python_dictionaries.asp)
* [`print()`](https://www.w3schools.com/python/ref_func_print.asp)
* [string `format()`](https://www.w3schools.com/python/ref_string_format.asp)
* [variables](https://www.w3schools.com/python/python_variables.asp)
* [keyword arguments](https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp)
* [np.logical_or](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html)

Their meaning should be quite obvious from their context, but we provide links here to materiual at [https://www.w3schools.com/](https://www.w3schools.com/) should you wish to understand them further here.

## MODIS LAI product 

To introduce geospatial processing, we will use a dataset from the MODIS LAI product over the UK. 

The data product [MOD15](https://modis.gsfc.nasa.gov/data/dataprod/mod15.php) LAI/FPAR has been generated from NASA MODIS sensors Terra and Aqua data since 2002. We are now in dataset collection 6 (the data version to use).

    LAI is defined as the one-sided green leaf area per unit ground area in broadleaf canopies and as half the total needle surface area per unit ground area in coniferous canopies. FPAR is the fraction of photosynthetically active radiation (400-700 nm) absorbed by green vegetation. Both variables are used for calculating surface photosynthesis, evapotranspiration, and net primary production, which in turn are used to calculate terrestrial energy, carbon, water cycle processes, and biogeochemistry of vegetation. Algorithm refinements have improved quality of retrievals and consistency with field measurements over all biomes, with a focus on woody vegetation.
    
We use such data to map and understand about the dynamics of terrestrial vegetation / carbon, for example, for climate studies.

The raster data are arranged in tiles, indexed by row and column, to cover the globe:


![MODIS tiles](https://www.researchgate.net/profile/J_Townshend/publication/220473201/figure/fig5/AS:277546596880390@1443183673583/The-global-MODIS-Sinusoidal-tile-grid.png)


### Exercise

The pattern on the tile names is `hXXvYY` where `XX` is the horizontal coordinate and `YY` the vertical.


* use the map above to work out the names of the two tiles that we will need to access data over the UK
* set the variable `tiles` to contain these two names in a list

For example, for the two tiles covering Madagascar, we would set:

    tiles = ['h22v10','h22v11']


### Accessing NASA MODIS URLs

<span class="burk">**Warning: The NASA data servers tend to be down for maintainance on Wednesday morning EST**</span>

Although you can access MODIS datasets through the [NASA Earthdata](https://urs.earthdata.nasa.gov/home) interface, there are many occasions that we would want to just automatically pull datasets. As we note above, we could use some existing API for this, such as [Appeears](https://lpdaacsvc.cr.usgs.gov/appeears/), but we are aiming here at being able to ultimately develop codes that do this from a lower-level perspective. 

Automation has many roles, and is particularly useful when you want a time series of data that might involve many files. For example, for analysing LAI or other variables over space/time) we will want to write code that pulls the time series of data. 

If you visit the site [https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006](https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006), you will see 'date' style links (e.g. `2018.09.30`) through to sub-directories. 

In these, e.g. [https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2018.09.30/](https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2018.09.30/) you will find URLs of a set of files. 

The files pointed to by the URLs are the MODIS MOD15 4-day composite 500 m LAI/FPAR product [MCD15A3H](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd15a3h_v006).

There are links to several datasets on the page, including 'quicklook files' that are jpeg format images of the datasets, e.g.:

![MCD15A3H.A2018273.h17v03](https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2018.09.30/BROWSE.MCD15A3H.A2018273.h17v03.006.2018278143630.1.jpg)

as well as `xml` files and `hdf` datasets. 



### Data Products

If we look at the dataserver we hae specified [https://e4ftl01.cr.usgs.gov](https://e4ftl01.cr.usgs.gov), we will see that a number of sub-directories exist. Each of these 'server directories' points to a different data stream:

    [DIR] ASTT/                   2019-08-05 07:54    -   
    [DIR] COMMUNITY/              2020-06-02 08:45    -   
    [DIR] ECOSTRESS/              2020-04-09 10:30    -   
    [DIR] GEDI/                   2020-02-10 09:58    -   
    [DIR] MEASURES/               2020-03-17 10:55    -   
    [DIR] MOLA/                   2020-06-01 09:20    -   
    [DIR] MOLT/                   2020-04-14 08:06    -   
    [DIR] MOTA/                   2019-12-27 06:49    -   
    [DIR] VIIRS/                  2020-06-23 10:26    -   

For example, we might notice [VIIRS](https://e4ftl01.cr.usgs.gov/VIIRS) which takes us to the [VIIRS data products](https://viirsland.gsfc.nasa.gov), or [GEDI](https://e4ftl01.cr.usgs.gov/GEDI) [spaceborne lidar](https://gedi.umd.edu/) data. Each of these data streams will have their own properties that we need to appreciate before using them.

### MOTA

The URL we have used above, [https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2018.09.30/](https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2018.09.30/) starts with a call to the server directory `MOTA`, so we can think of `https://e4ftl01.cr.usgs.gov/MOTA` as the base level URL.

MOTA refers to combined MODIS Terra and Aqua datasets. Similarly, MOLA and MOLT refer to datasets generated from single MODIS sensors of Aqua and Terra, respectively.

The rest of the directory information `MCD15A3H.006/2018.09.30` tells us:

* the product name `MCD15A3H`
* the product version `006`
* the date of the dataset `2018.09.30`

There are several ways we could specify the date information. The most 'human readable' is probably `YYYY.MM.DD` as given here. 

### MODIS filename format

If we vist the link to a particular date for this dataset  [https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2018.09.30/](https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2018.09.30/), we see some files that have the suffix `hdf`.

The `hdf` filenames are of the form:

    MCD15A3H.A2018273.h35v10.006.2018278143650.hdf
    
where:

* the first field (`MCD15A3H`) gives the product code
* the second (`A2018273`) gives the observation date: day of year `273`, `2018` here
* the third (`h35v10`) gives the 'MODIS tile' code for the data location
* the remaining fields specify the product version number (`006`) and a code representing the processing date.

If we look at the [product specification page](https://lpdaac.usgs.gov/products/mcd15a3hv006/) we see that the data product has multiple data layers. In the case of MCD15A3H, this is:

|SDS Name	|Description	| Units	|Data Type	|Fill Value|	No Data Value	|Valid Range|	Scale Factor
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|-|
| Fpar_500m |	Fraction of Photosynthetically Active Radiation	|Percent|	8-bit unsigned integer	|249 to 255	|N/A	|0 to 100	|0.01
|Lai_500m	|Leaf Area Index|	m²/m²|	8-bit unsigned integer|	249 to 255	|N/A|	0 to 100|	0.1|
|FparLai_QC	|Quality for  FPAR and LAI	|Class Flag	|8-bit unsigned integer	|255|	N/A	|0 to 254	|N/A
| FparExtra_QC	|Extra detail Quality for  FPAR and LAI	|Class Flag|	8-bit unsigned integer|	255	|N/A	|0 to 254	|N/A
|FparStdDev_500m|	Standard deviation of  FPAR	|Percent|	8-bit unsigned integer|	248 to 255	|N/A|	0 to 100	|0.01
|LaiStdDev_500m|	Standard deviation of LAI	|m²/m²|	8-bit unsigned integer|	248 to 255|	N/A	|0 to 100	|0.1


## Getting and visualising the data

### Grid

One thing we might need sometimes is to specify the `grid` used by the data product. Mostly, this is just the same as the product name (this is the default in our codes by just setting `grid` to the same as the product name). 

For the product `MCD15A3H` that we use here though, the grid is `MOD_Grid_MCD15A3H`, so we need to specify this. This issue is something to look out for when you specify a MODIS product you haven't use before. This is not specified in the product user guides or specifications, but you will *mostly* find it the associated [file specifications document](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD15A3H). When you use a new proiduct then, don't forget to check the appropriate [file specifications](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6) to find the grid object used!

If you can't find it, just try to use the default (set `grid` to `None`).

If that fails to return anything useful, the easiest thinbg to do is to examine the SDS datasets in the file itself.

For example, lets try using the default grid: 


```python
from uclgeog.process_timeseries import mosaic, visualise
# libraries we need

#######################
# specify what we want
# in a dictionary
#######################
# UK tiles
# specify day of year (DOY) and year

params = {
    'tiles'   :    ['h17v03', 'h17v04', 'h18v03', 'h18v04'],
    'doy'     :    1,
    'year'    :    2020,
    'product' :    'MCD15A3H',
    'layer'   :    'Lai_500m',
    'grid'    :    None,
    'base_url':   'https://e4ftl01.cr.usgs.gov/MOTA'
}

# check to see if it worked
# and trap errors 
try:
    data = mosaic(params)
    assert data is not None
except AssertionError:
    print("\nThis hasn't worked")
else:
    print("\nThis worked")
```

The code exits with the message:
    
        failed to warp ['HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2020001.h17v03.006.2020006031702.hdf":MCD15A3H:Lai_500m', 'HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2020001.h17v04.006.2020006031910.hdf":MCD15A3H:Lai_500m', 'HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2020001.h18v03.006.2020006033540.hdf":MCD15A3H:Lai_500m', 'HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2020001.h18v04.006.2020006032422.hdf":MCD15A3H:Lai_500m'] 2020, 1, ['h17v03', 'h17v04', 'h18v03', 'h18v04'], data/
        
This is telling us that it has tried to access a dataset

    HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2020001.h17v03.006.2020006031702.hdf":MCD15A3H:Lai_500m
 
and this is where it has failed.

We could use python calls to check what this should be, but we mostly find it easier to use system tool, `gdalinfo` in this case. [`gdal`](https://gdal.org/) is software for geospatial processing that can deal with a wide range of formats. We will make a lot of use of it later on.

For now, we can run a system command below to see what the SDS `Lai_500m` looks like in one of the files it has downloaded (we get the filename from the list reported above).


```python
!gdalinfo data/MCD15A3H.A2020001.h17v03.006.2020006031702.hdf | grep Lai_500m
```

From this, we see that the dataset specification is really 

    HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2020001.h17v03.006.2020006031702.hdf":MOD_Grid_MCD15A3H:Lai_500m
    
and not what we previously assumed:

    HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2020001.h17v03.006.2020006031702.hdf":MCD15A3H:Lai_500m

We have most of the specification correct, but have used `MCD15A3H:Lai_500m` instead of `MOD_Grid_MCD15A3H:Lai_500m`. Let's fix this now:


```python
from uclgeog.process_timeseries import mosaic, visualise
# libraries we need

#######################
# specify what we want
# in a dictionary
#######################
# UK tiles
# specify day of year (DOY) and year

params = {
    'tiles'   :    ['h17v03', 'h17v04', 'h18v03', 'h18v04'],
    'doy'     :    1,
    'year'    :    2020,
    'product' :    'MCD15A3H',
    'layer'   :    'Lai_500m',
    'grid'    :    'MOD_Grid_MCD15A3H',
    'base_url':   'https://e4ftl01.cr.usgs.gov/MOTA'

}

# check to see if it worked
# and trap errors 
try:
    data = mosaic(params)
    assert data is not None
except AssertionError:
    print("\nThis hasn't worked")
else:
    print("\nThis worked")
```

### Download

So, other than some terms (e.g. version number) we can take as defaults, when we want to access a MODIS product as tile data, we need to specify:

* product code
* SDS Name (scientific dataset name)
* tile(s)
* day of year (DOY)
* year

Now we have some appreciation of the MODIS dataset description requirements, we can use the method `mosaic_and_clip()` in `uclgeog` to download some example datasets:

    # UK tiles
    tiles = ['h17v03', 'h17v04', 'h18v03', 'h18v04']
    # specify day of year (DOY) and year
    doy,year = 1,2020
    # product
    product = 'MCD15A3H'
    # SDS
    layer = "Lai_500m"
    # grid
    grid = 'MOD_Grid_MCD15A3H'

One useful thing we have implemented in `mosaic_and_clip()` is to mosaic data from different tiles together into one contiguous dataset. So, although we will have data specified over four tiles, we will mosaic it together into a single array.


```python
from uclgeog.process_timeseries import mosaic_and_clip, visualise
import numpy as np
# libraries we need

#######################
# specify what we want
# in a dictionary
#######################
# UK tiles
# specify day of year (DOY) and year

params = {
    'tiles'   :    ['h17v03', 'h17v04', 'h18v03', 'h18v04'],
    'doy'     :    1,
    'year'    :    2020,
    'product' :    'MCD15A3H',
    'layer'   :    'Lai_500m',
    'grid'    :    'MOD_Grid_MCD15A3H',
    'verbose' :    True,
    'base_url':   'https://e4ftl01.cr.usgs.gov/MOTA'
}

#######################
# download and interpret
# and mask non-valid numbers by setting to NaN
# see data table above
#######################
try:
    data = mosaic(params)
    assert data is not None
except AssertionError:
    print("\nThis hasn't worked")
else:
    data = data.astype(float)
    data[data>248] = np.nan
    #######################
    # print some feedback
    #######################
    print(f'the variable lai contains a dataset of dimension {data.shape}')
    print('for product {product} SDS {layer}'.format(**params))
    print('for day {doy} of year {year} for tiles {tiles}'.format(**params))

```

### Visualise

We have now generated a dataset, stored in a variable `lai`. We are likely to want to perform some analysis on this, but we might also like to visualise the dataset.

We can do this using a python package [matplotlib](https://matplotlib.org) that we will gain more experience with later.

For now, we will simply implement a typical image visualisation, with a dataset title, and scale bar. We will use a method `visualise()` from our `uclgeog` library to do this.


```python
# call visualise
title = 'product {product} SDS {layer}\n'.format(**params) + \
        'for day {doy} of year {year} for tiles {tiles}'.format(**params)
# set the max value to 3.0 to be able to see whats going on
plot=visualise(data,title=title,vmax=3.0)
```

# Exercises

### Exercise: change the year and DOY

Using the lines of code above, download and visualise the LAI dataset for a different DOY and year. Remember that it is a 4-day synthesis, so there are only datasets on doy 1,5,9, ...

Put comments in your code using `#` to start a comment, to describe what you are doing.

You might want to set `verbose` to `True` to get some feedback on what is going on.

### Exercise: change the location

Using the lines of code above, download and visualise the LAI dataset for a different location.

You will need to specify the tile or tiles that you wish to use.

As before, put comments in your code using `#` to start a comment, to describe what you are doing.

You might want to set `verbose` to `True` to get some feedback on what is going on.

### Exercise: change the SDS

Using the lines of code above, download and visualise the LAI dataset for a different location. 

Now, instead of using the data layer `Lai_500m`, visualise another data layer in the LAI dataset. See the table above of [the product specification](https://lpdaac.usgs.gov/products/mcd15a3hv006/) for details.

### Exercise: change the product to another on MOTA

Using the lines of code above, download and visualise a different MODIS product.

You can see the option codes on the server we have been using by [looking in the directory https://e4ftl01.cr.usgs.gov/MOTA](https://e4ftl01.cr.usgs.gov/MOTA).

You get get the meanings of the codes from simply googling them, or you can look them up on the [MODIS data product page](https://modis.gsfc.nasa.gov/data/dataprod/).

### Exercise: Snow
    
The MODIS snow products are on a different server to the one we used above, [`https://n5eil01u.ecs.nsidc.org/MOST`](https://n5eil01u.ecs.nsidc.org/MOST) for MODIS Terra data and [`https://n5eil01u.ecs.nsidc.org/MOSA`](https://n5eil01u.ecs.nsidc.org/MOSA) for MODIS Aqua. Product information is available on the [product website](https://nsidc.org/data/myd10a1). Note that there is not combined Terra and Aqua product.

Use the codes above to explore, download, and plot a snow dataset from the `MOD10A1` product.

### Exercise: Land Cover
    
The MODIS land cover product is `MCD12Q1`.

Use the codes above to explore, download, and plot a  land cover dataset from the `MCD12Q1` product.

# Summary

In these notes, we have introduced the characteristics of MODIS data products, and learned how to specify, access, and display them for a few servers. You will have accessed a number of products under a number of conditions in the exercises, but you are encouraged to explore this further.

The main item to do with using data products of this sort, that we haven't covered yet, is the interpretation of Quality Assurance (QA) data. This is often packed information into bits, and can be a little tricky at first. However, as with above, once you have a little familiarisation with a few cases, you will be able to applky this more widely.

You should spend some time going through the various links to explore the different datasets, and try out the exercises above for various products. The familiarity you gain from this will help when it comes to building our own codes later on.
