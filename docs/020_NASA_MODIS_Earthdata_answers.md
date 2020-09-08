# NASA MODIS Earthdata : Answers to exercises

### Exercise

The pattern on the tile names is `hXXvYY` where `XX` is the horizontal coordinate and `YY` the vertical.


* use the map above to work out the names of the two tiles that we will need to access data over the UK
* set the variable `tiles` to contain these two names in a list

For example, for the two tiles covering Madagascar, we would set:

    tiles = ['h22v10','h22v11']


```python
# tiles for the UK

tiles = ['h17v03', 'h17v04', 'h18v03', 'h18v04']
```

### Exercise: change the year and DOY

Using the lines of code above, download and visualise the LAI dataset for a different DOY and year. Remember that it is a 4-day synthesis, so there are only datasets on doy 1,5,9, ...

Put comments in your code using `#` to start a comment, to describe what you are doing.

You might want to set `verbose` to `True` to get some feedback on what is going on.


```python
from uclgeog.process_timeseries import mosaic_and_clip, visualise
import numpy as np

#######################
# location: madagascar
#######################
params = {
    'tiles'   :    ['h17v03', 'h17v04', 'h18v03', 'h18v04'],
    'doy'     :    5,
    'year'    :    2010,
    'product' :    'MCD15A3H',
    'layer'   :    'Lai_500m',
    'grid'    :    'MOD_Grid_MCD15A3H',
    'verbose' :    True,
    'base_url':   'https://e4ftl01.cr.usgs.gov/MOTA'
}

try:
    data = mosaic(params)
    assert data is not None
except AssertionError:
    print("\nThis hasn't worked")
else:
    data = data.astype(float)
    data[data>248] = np.nan
    #######################
    # call visualise
    #######################
    title = 'product {product} SDS {layer}\n'.format(**params) + \
            'for day {doy} of year {year} for tiles {tiles}'.format(**params)
    plot=visualise(data,title=title,vmax=3.0)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-10-dd49c35720e8> in <module>
    ----> 1 from uclgeog.process_timeseries import mosaic_and_clip, visualise
          2 import numpy as np
          3 
          4 #######################
          5 # location: madagascar


    ModuleNotFoundError: No module named 'uclgeog'



```python
from uclgeog.process_timeseries import mosaic_and_clip, visualise

#######################
# doy = 1 + 4 * 20 here
#######################
params = {
    'tiles'  :    ['h17v03', 'h17v04', 'h18v03', 'h18v04'],
    'doy'    :    1+4*30,
    'year'   :    2020,
    'product':    'MCD15A3H',
    'layer'  :    'Lai_500m',
    'grid'   :    'MOD_Grid_MCD15A3H',
    'verbose':    True
}

#######################
# download and interpret
#######################
# check to see if it worked
# and trap errors 
try:
    lai = mosaic(params)
    assert lai is not None
except:
    print("\nThis hasn't worked")
else:
    lai = lai.astype(float)
    lai[lai>248] = np.nan
    #######################
    # call visualise
    #######################
    title = 'product {product} SDS {layer}\n'.format(**params) + \
            'for day {doy} of year {year} for tiles {tiles}'.format(**params)
    plot=visualise(lai,title=title,vmax=3.0)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-11-35e188cc27e3> in <module>
    ----> 1 from uclgeog.process_timeseries import mosaic_and_clip, visualise
          2 
          3 #######################
          4 # doy = 1 + 4 * 20 here
          5 #######################


    ModuleNotFoundError: No module named 'uclgeog'


### Exercise: change the location

Using the lines of code above, download and visualise the LAI dataset for a different location.

You will need to specify the tile or tiles that you wish to use.

As before, put comments in your code using `#` to start a comment, to describe what you are doing.

You might want to set `verbose` to `True` to get some feedback on what is going on.


```python
from uclgeog.process_timeseries import mosaic_and_clip, visualise
import numpy as np

#######################
# location: madagascar
#######################
params = {
    'tiles'   :    ['h22v10','h22v11'],
    'doy'     :    5,
    'year'    :    2010,
    'product' :    'MCD15A3H',
    'layer'   :    'Lai_500m',
    'grid'    :    'MOD_Grid_MCD15A3H',
    'verbose' :    True,
    'base_url':   'https://e4ftl01.cr.usgs.gov/MOTA'
}
try:
    data = mosaic(params)
    assert data is not None
except AssertionError:
    print("\nThis hasn't worked")
else:
    data = data.astype(float)
    data[data>248] = np.nan
    #######################
    # call visualise
    #######################
    title = 'product {product} SDS {layer}\n'.format(**params) + \
            'for day {doy} of year {year} for tiles {tiles}'.format(**params)
    plot=visualise(data,title=title,vmax=3.0)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-12-fb369b668128> in <module>
    ----> 1 from uclgeog.process_timeseries import mosaic_and_clip, visualise
          2 import numpy as np
          3 
          4 #######################
          5 # location: madagascar


    ModuleNotFoundError: No module named 'uclgeog'


### Exercise: change the SDS

Using the lines of code above, download and visualise the LAI dataset for a different location. 

Now, instead of using the data layer `Lai_500m`, visualise another data layer in the LAI dataset. See the table above of [the product specification](https://lpdaac.usgs.gov/products/mcd15a3hv006/) for details.


```python
from uclgeog.process_timeseries import mosaic_and_clip, visualise
import numpy as np

#######################
# location: madagascar
#######################

params = {
    'tiles'   :    ['h22v10','h22v11'],
    'doy'     :    5,
    'year'    :    2010,
    'product' :    'MCD15A3H',
    'layer'   :    'FparLai_QC',
    'grid'    :    'MOD_Grid_MCD15A3H',
    'verbose' :    True,
    'base_url':   'https://e4ftl01.cr.usgs.gov/MOTA'
}

#######################
# download and interpret
# note the valid range is different
# see the product table above
#######################

try:
    data = mosaic(params)
    assert data is not None
except AssertionError:
    print("\nThis hasn't worked")
else:
    data = data.astype(float)
    data[data>254] = np.nan
    #######################
    # call visualise
    #######################
    title = 'product {product} SDS {layer}\n'.format(**params) + \
            'for day {doy} of year {year} for tiles {tiles}'.format(**params)
    plot=visualise(data,title=title)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-13-7efdd182c7c5> in <module>
    ----> 1 from uclgeog.process_timeseries import mosaic_and_clip, visualise
          2 import numpy as np
          3 
          4 #######################
          5 # location: madagascar


    ModuleNotFoundError: No module named 'uclgeog'


### Exercise: change the product to another on MOTA

Using the lines of code above, download and visualise a different MODIS product.

You can see the option codes on the server we have been using by [looking in the directory https://e4ftl01.cr.usgs.gov/MOTA](https://e4ftl01.cr.usgs.gov/MOTA).

You get get the meanings of the codes from simply googling them, or you can look them up on the [MODIS data product page](https://modis.gsfc.nasa.gov/data/dataprod/).


```python
from uclgeog.process_timeseries import mosaic_and_clip, visualise
import numpy as np

#######################
# location: madagascar
# product MCD64A1 Burned Area
# see product page on
# https://lpdaac.usgs.gov/products/mcd64a1v006/
# we see one of the SDS layers is 'Burn Date'
# and that 1 to 366 are valid
#
# get the grid from 
# https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD64A1
#######################
params = {
    'tiles'   :    ['h22v10'],
    'doy'     :    1,
    'year'    :    2020,
    'product' :    'MCD64A1',
    'layer'   :    'Burn Date',
    'grid'    :    'MOD_Grid_Monthly_500m_DB_BA',
    'verbose' :    True,
    'base_url':   'https://e4ftl01.cr.usgs.gov/MOTA'
}

#######################
# download and interpret
# note the valid range is different
# see the product table above
# Use a different variable name: 
# its not lai any more!
#######################
try:
    data = mosaic(params)
    assert data is not None
except:
    print("\nThis hasn't worked")
else:
    data = data.astype(float)
    data[np.logical_or(data>366,data<1)] = np.nan
    #######################
    # call visualise
    #######################
    title = 'product {product} SDS {layer}\n'.format(**params) + \
            'for day {doy} of year {year} for tiles {tiles}'.format(**params)
    plot=visualise(data,title=title)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-14-4ddca96bce5f> in <module>
    ----> 1 from uclgeog.process_timeseries import mosaic_and_clip, visualise
          2 import numpy as np
          3 
          4 #######################
          5 # location: madagascar


    ModuleNotFoundError: No module named 'uclgeog'


### Exercise: Snow
    
The MODIS snow products are on a different server to the one we used above, [`https://n5eil01u.ecs.nsidc.org/MOST`](https://n5eil01u.ecs.nsidc.org/MOST) for MODIS Terra data and [`https://n5eil01u.ecs.nsidc.org/MOSA`](https://n5eil01u.ecs.nsidc.org/MOSA) for MODIS Aqua. Product information is available on the [product website](https://nsidc.org/data/myd10a1). Note that there is not combined Terra and Aqua product.

Use the codes above to explore, download, and plot a snow dataset from the `MOD10A1` product.


```python
from uclgeog.process_timeseries import mosaic_and_clip, visualise
import numpy as np

#######################
# location: E Europe
# product 
# see product page on
# https://nsidc.org/data/MYD10A1/versions/6
# 0-100 is valid
# NDSI_Snow_Cover
# grid is MOD_Grid_Snow_500m
#######################
params = {
    'tiles'   :    ['h19v03'],
    'doy'     :    1,
    'year'    :    2010,
    'product' :    'MOD10A1',
    'layer'   :    'NDSI_Snow_Cover',
    'grid'    :    'MOD_Grid_Snow_500m',
    'verbose' :    True,
    'base_url':   'https://n5eil01u.ecs.nsidc.org/MOST'
}

#######################
# download and interpret
# note the valid range is different
# see the product table above
# Use a different variable name: 
# its not lai any more!
#######################
try:
    data = mosaic(params)
    assert data is not None
except:
    print("\nThis hasn't worked")
else:
    data = data.astype(float)
    data[np.logical_or(data>100,data<1)] = np.nan
    #######################
    # call visualise
    #######################
    title = 'product {product} SDS {layer}\n'.format(**params) + \
            'for day {doy} of year {year} for tiles {tiles}'.format(**params)
    plot=visualise(data,title=title)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-15-bd5d26ad50dd> in <module>
    ----> 1 from uclgeog.process_timeseries import mosaic_and_clip, visualise
          2 import numpy as np
          3 
          4 #######################
          5 # location: E Europe


    ModuleNotFoundError: No module named 'uclgeog'



```python
# check for grid info ...
!gdalinfo data/MOD10A1.A2010001.h19v03.006.2016083014706.hdf | grep NDSI_Snow_Cover
```

    ERROR 4: data/MOD10A1.A2010001.h19v03.006.2016083014706.hdf: No such file or directory
    gdalinfo failed - unable to open 'data/MOD10A1.A2010001.h19v03.006.2016083014706.hdf'.


### Exercise: Land Cover
    
The MODIS land cover product is `MCD12Q1`.

Use the codes above to explore, download, and plot a  land cover dataset from the `MCD12Q1` product.


```python
from uclgeog.process_timeseries import mosaic_and_clip, visualise
import numpy as np

#######################
# location: madagascar
# product MCD64A1 Burned Area
# see product page on
# https://lpdaac.usgs.gov/products/mcd12q1v006/
# we see one of the SDS layers is 'LC_Type1'
# and that 1 to 17 are valid
#
# get the grid from 
# https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD64A1
#######################
params = {
    'tiles'   :    ['h22v10'],
    'doy'     :    1,
    'year'    :    2018,
    'product' :    'MCD12Q1',
    'layer'   :    'LC_Type1',
    'grid'    :    'MCD12Q1',
    'verbose' :    True,
    'base_url':   'https://e4ftl01.cr.usgs.gov/MOTA'
}

#######################
# download and interpret
# note the valid range is different
# see the product table above
# Use a different variable name: 
# its not lai any more!
#######################
try:
    data = mosaic(params)
    assert data is not None
except:
    print("\nThis hasn't worked")
else:
    data = data.astype(float)
    data[np.logical_or(data>17,data<1)] = np.nan
    #######################
    # call visualise
    #######################
    title = 'product {product} SDS {layer}\n'.format(**params) + \
            'for day {doy} of year {year} for tiles {tiles}'.format(**params)
    plot=visualise(data,title=title)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-17-e2f28b046795> in <module>
    ----> 1 from uclgeog.process_timeseries import mosaic_and_clip, visualise
          2 import numpy as np
          3 
          4 #######################
          5 # location: madagascar


    ModuleNotFoundError: No module named 'uclgeog'



```python
from uclgeog.process_timeseries import mosaic_and_clip, visualise

#######################
# location: madagascar
# product MCD12C1 yearly Land cover
# see product page on
# https://lpdaac.usgs.gov/products/mcd12q1v006/
# we see one of the SDS layers is 'Majority_Land_Cover_Type_1'
# and that 255 is invalid
#
# get the grid from 
# https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD12Q1
#
# Note that date for dataset is 2001.01.01
# from https://e4ftl01.cr.usgs.gov/MOTA/MCD12Q1.006/
# year 2019 & 2020 not there yet!!
#######################
params = {
    'tiles'  :    ['h22v10'],
    'doy'    :    1,
    'year'   :    2018,
    'product':    'MCD12Q1',
    'layer'  :    'LC_Type1',
    'grid'   :    None,
    'verbose':    True
}

#######################
# download and interpret
# note the valid range is different
# see the product table above
# Use a different variable name: 
# its not lai any more!
#######################
try:
    data = mosaic(params)
    assert data is not None
except:
    print("\nThis hasn't worked")
else:
    data = data.astype(float)
    data[data>254] = np.nan
    #######################
    # call visualise
    #######################
    title = 'product {product} SDS {layer}\n'.format(**params) + \
            'for day {doy} of year {year} for tiles {tiles}'.format(**params)
    plot=visualise(data,title=title)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-18-73e04bf09463> in <module>
    ----> 1 from uclgeog.process_timeseries import mosaic_and_clip, visualise
          2 
          3 #######################
          4 # location: madagascar
          5 # product MCD12C1 yearly Land cover


    ModuleNotFoundError: No module named 'uclgeog'



```python
from uclgeog.process_timeseries import mosaic_and_clip, visualise

#############
# FparLai_QC
#############

#######################
# single tile here
# for SDS FparLai_QC
# note that valid values different here
#######################
params = {
    'tiles'  :    ['h18v03'],
    'doy'    :    1+4*30,
    'year'   :    2020,
    'product':    'MCD15A3H',
    'layer'  :    'FparLai_QC',
    'verbose':    True
}

#######################
# download and interpret
#######################
lai = mosaic_and_clip(**params).astype(float)
lai[lai>254] = np.nan
#######################
# call visualise
# Don't' set vmax now 
# as we want to see the 
# full range of values
#######################
title = 'product {product} SDS {layer}\n'.format(**params) + \
        'for day {doy} of year {year} for tiles {tiles}'.format(**params)
plot=visualise(lai,title=title)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-19-8a100b6b0936> in <module>
    ----> 1 from uclgeog.process_timeseries import mosaic_and_clip, visualise
          2 
          3 #############
          4 # FparLai_QC
          5 #############


    ModuleNotFoundError: No module named 'uclgeog'

