# 3.3 GDAL, and OGR masking

<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#3.3-GDAL,-and-OGR-masking" data-toc-modified-id="3.3-GDAL,-and-OGR-masking-3.1">3.3 GDAL, and OGR masking</a></span><ul class="toc-item"><li><span><a href="#3.3.1-The-MODIS-LAI-data" data-toc-modified-id="3.3.1-The-MODIS-LAI-data-3.1.1">3.3.1 The MODIS LAI data</a></span><ul class="toc-item"><li><span><a href="#3.3.1.1-try-...-except-..." data-toc-modified-id="3.3.1.1-try-...-except-...-3.1.1.1">3.3.1.1 <code>try ... except ...</code></a></span></li><li><span><a href="#3.3.1.2-Get-data" data-toc-modified-id="3.3.1.2-Get-data-3.1.1.2">3.3.1.2 Get data</a></span></li><li><span><a href="#3.3.1.3-File-Naming-Convention" data-toc-modified-id="3.3.1.3-File-Naming-Convention-3.1.1.3">3.3.1.3 File Naming Convention</a></span></li><li><span><a href="#3.3.1.2-Dataset-Naming-Convention" data-toc-modified-id="3.3.1.2-Dataset-Naming-Convention-3.1.1.4">3.3.1.2 Dataset Naming Convention</a></span></li></ul></li><li><span><a href="#3.3.2-MODIS-dataset-access" data-toc-modified-id="3.3.2-MODIS-dataset-access-3.1.2">3.3.2 MODIS dataset access</a></span><ul class="toc-item"><li><span><a href="#3.3.2.1-gdal.ReadAsArray()" data-toc-modified-id="3.3.2.1-gdal.ReadAsArray()-3.1.2.1">3.3.2.1 <code>gdal.ReadAsArray()</code></a></span></li><li><span><a href="#3.3.2.2-Metadata" data-toc-modified-id="3.3.2.2-Metadata-3.1.2.2">3.3.2.2 Metadata</a></span></li></ul></li><li><span><a href="#3.3.3-Reading-and-displaying-data" data-toc-modified-id="3.3.3-Reading-and-displaying-data-3.1.3">3.3.3 Reading and displaying data</a></span><ul class="toc-item"><li><span><a href="#3.3.3.1-glob" data-toc-modified-id="3.3.3.1-glob-3.1.3.1">3.3.3.1 <code>glob</code></a></span></li><li><span><a href="#3.3.3.2-reading-and-displaying-image-data" data-toc-modified-id="3.3.3.2-reading-and-displaying-image-data-3.1.3.2">3.3.3.2 reading and displaying image data</a></span></li><li><span><a href="#3.3.3.3-subplot-plotting" data-toc-modified-id="3.3.3.3-subplot-plotting-3.1.3.3">3.3.3.3 subplot plotting</a></span></li><li><span><a href="#3.3.3.3-tile-stitching" data-toc-modified-id="3.3.3.3-tile-stitching-3.1.3.4">3.3.3.3 tile stitching</a></span></li><li><span><a href="#3.3.3.4-gdal-virtual-file" data-toc-modified-id="3.3.3.4-gdal-virtual-file-3.1.3.5">3.3.3.4 <code>gdal</code> virtual file</a></span></li></ul></li><li><span><a href="#3.3.4-The-country-borders-dataset" data-toc-modified-id="3.3.4-The-country-borders-dataset-3.1.4">3.3.4 The country borders dataset</a></span></li></ul></li></ul></div>


In this section, we'll look at combining both raster and vector data to provide a masked dataset ready to use. We will produce a combined dataset of leaf area index (LAI) over the UK derived from the MODIS sensor. The MODIS LAI product is produced every 4 days and it is provided spatially tiled. Each tile covers around 1200 km x 1200 km of the Earth's surface. Below you can see a map showing the MODIS tiling convention.



## 3.3.1 The MODIS LAI data

Let's first test your NASA login:



```python
import geog0111.nasa_requests as nasa_requests
from geog0111.cylog import cylog
%matplotlib inline

url = 'https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2018.09.30/' 
        
# grab the HTML information
try:
    html = nasa_requests.get(url).text
    # test a few lines of the html
    if html[:20] == '<!DOCTYPE HTML PUBLI':
        print('this seems to be ok ... ')
        print('use cylog().login() anywhere you need to specify the tuple (username,password)')
except:
    print('login error ... try entering your username password again')
    print('then re-run this cell until it works')
    cylog(init=True)
```

    this seems to be ok ... 
    use cylog().login() anywhere you need to specify the tuple (username,password)


### 3.3.1.1 `try ... except ...` 

Note that we have used a `try ... except` structure above to trap any errors.


```python
import sys
try:
    # variable stupid not set
    print("I'm trying this but it will fail",stupid)
except NameError:
    '''
    trap the error
    (and ideally define some sensible behaviour)
    '''
    print("unset variable:",sys.exc_info()[1])
except:
    print("In case of other errors")
    print(sys.exc_info())
    # raise our own exception
    raise Exception('bad code')
```

    unset variable: name 'stupid' is not defined


Generally, you should try to foresee the types of error you might generate, and provide specific traps for these so youy can control the code better.

In the case above, we allow the code execution to continue with a `NameError`, but raise a further exception in case of any other errors.

`sys.exc_info()` provides a tuple of information on what happened.

**Exercise**

* Write some code using `try ... except` to trap a `ZeroDivisionError` 
* provide a sensible result in such a case

**hint**

If you divide by zero, the result will be infinity, which is often not what you want to happen. Instead, try dividing by a small number, such as that provided by `sys.float_info.epsilon`.


```python
# do exercise here
```

### 3.3.1.2 Get data

You should by now be able to download MODIS data, but in this case, the data are provided (or downloaded for you) in the `data` folder as files `MCD15A3H.A2018273.h17v03.006.2018278143630.hdf`  and `MCD15A3H.A2018273.h18v03.006.2018278143633.hdf` (and some files `*v04*hdf` we will need later) by running the code below.


```python
from geog0111.geog_data import *

filenames = ['MCD15A3H.A2018273.h17v03.006.2018278143630.hdf', \
            'MCD15A3H.A2018273.h18v03.006.2018278143633.hdf',\
            'MCD15A3H.A2018273.h17v04.006.2018278143630.hdf',\
            'MCD15A3H.A2018273.h18v04.006.2018278143638.hdf']
destination_folder="data"

for file_name in filenames:
    f = procure_dataset(file_name,verbose=True,\
                        destination_folder=destination_folder)
    print(file_name,f)
```

    MCD15A3H.A2018273.h17v03.006.2018278143630.hdf True
    MCD15A3H.A2018273.h18v03.006.2018278143633.hdf True
    MCD15A3H.A2018273.h17v04.006.2018278143630.hdf True
    MCD15A3H.A2018273.h18v04.006.2018278143638.hdf True


We want to select the LAI layers, so let's have a look at the contents ('sub datasets') of one of the files.

To do this with `gdal`:

* make the full filename (folder name, plus the filename in that folder). Use `Path` for this, but convert to a string.
* open the file, store as `g`
* get the list `g.GetSubDatasets()` and loop over this


```python
import gdal
from pathlib import Path
from geog0111.geog_data import *

filenames = ['MCD15A3H.A2018273.h17v03.006.2018278143630.hdf', \
            'MCD15A3H.A2018273.h18v03.006.2018278143633.hdf']
destination_folder="data"

for file_name in filenames:
    # form full filename as a string
    # and print with an underline of = 
    file_name = Path(destination_folder).joinpath(file_name).as_posix()
    print(file_name)
    print('='*len(file_name))
    
    # open the file as g
    g = gdal.Open(file_name)
    # loop over the subdatasets
    for d in g.GetSubDatasets():
        print(d)
```

    data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf
    ===================================================
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf":MOD_Grid_MCD15A3H:Fpar_500m', '[2400x2400] Fpar_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf":MOD_Grid_MCD15A3H:Lai_500m', '[2400x2400] Lai_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf":MOD_Grid_MCD15A3H:FparLai_QC', '[2400x2400] FparLai_QC MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf":MOD_Grid_MCD15A3H:FparExtra_QC', '[2400x2400] FparExtra_QC MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf":MOD_Grid_MCD15A3H:FparStdDev_500m', '[2400x2400] FparStdDev_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf":MOD_Grid_MCD15A3H:LaiStdDev_500m', '[2400x2400] LaiStdDev_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf
    ===================================================
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf":MOD_Grid_MCD15A3H:Fpar_500m', '[2400x2400] Fpar_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf":MOD_Grid_MCD15A3H:Lai_500m', '[2400x2400] Lai_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf":MOD_Grid_MCD15A3H:FparLai_QC', '[2400x2400] FparLai_QC MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf":MOD_Grid_MCD15A3H:FparExtra_QC', '[2400x2400] FparExtra_QC MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf":MOD_Grid_MCD15A3H:FparStdDev_500m', '[2400x2400] FparStdDev_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)')
    ('HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf":MOD_Grid_MCD15A3H:LaiStdDev_500m', '[2400x2400] LaiStdDev_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)')


So we see that the data is in `HDF4` format, and that it has a number of layers. The dataset/layer we're interested in

`HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf":MOD_Grid_MCD15A3H:Lai_500m`.


### 3.3.1.3 File Naming Convention

This section taken from [NASA MODIS product page](https://nsidc.org/data/mod10a1).

Example File Name:

`data/MOD10A1.A2000055.h15v01.006.2016061160800.hdf`



`FOLDER/MOD[PID].A[YYYY][DDD].h[NN]v[NN].[VVV].[yyyy][ddd][hhmmss].hdf`

Refer to Table 3.3.1 for descriptions of the file name variables listed above.



|  Variable | Description  |  
|---|---|
| FOLDER| folder/directory name of file|
| MOD  |  MODIS/Terra  (`MCD` means combined)| 
|  PID |   Product ID|  
| A	|Acquisition date follows|
|YYYY	|Acquisition year|
|DDD	|Acquisition day of year|
|h[NN]v[NN]	|Horizontal tile number and vertical tile number (see Grid for details.)|
|VVV	|Version (Collection) number|
|yyyy	|Production year|
|ddd	|Production day of year|
|hhmmss	|Production hour/minute/second in GMT|
|.hdf	|HDF-EOS formatted data file|
Table 3.3.1. Variables in the MODIS File Naming Convention

![](https://nsidc.org/sites/nsidc.org/files/images/modis-sin-grid.png)


### 3.3.1.2 Dataset Naming Convention

Example Dataset Name:

`HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf":MOD_Grid_MCD15A3H:Lai_500m`


`FORMAT:"FILENAME":MOD_Grid_PRODUCT:LAYER`

|  Variable | Description  |  
|---|---|
|FORMAT| file format, `HDF4_EOS:EOS_GRID`|
|FILENAME| dataset file name, see below|
|PRODUCT| MODIS product code e.g. `MCD15A3H`|
|LAYER| sub-dataset name e.g. `Lai_500m`|
Table 3.3.2. Variables in the MODIS Dataset Naming Convention


**Exercise E3.3.1**

* Check you're happy that the other datasets (e.g. `LaiStdDev_500m`) follow the same convention as `Lai_500m`
* work out what the dataset/layer name would be for the dataset product `MOD10A1` version `6` for the $1^{st}$ January 2018, for tile `h25v06` for the layer `NDSI_Snow_Cover`. You will find product information [on the relevant NASA page](https://nsidc.org/data/mod10a1). You may not be able to access the production date/time, but just put a placeholder for that now.
* phrase the filename and layer name as '`f`' strings, e.g. starting `f'HDF4_EOS:EOS_GRID:"{filename}":MOD_Grid_{}'` etc.

**Hint**:

You can explore the filenames by looking into the [Earthdata link](https://n5eil01u.ecs.nsidc.org/MOSA/).

![](images/BROWSE.MYD10A1.A2018001.h25v05.006.2018003025825.1.jpg)


```python
# do exercise here
```

## 3.3.2 MODIS dataset access

### 3.3.2.1 `gdal.ReadAsArray()`

We can now access the dataset names and open the datasets in `gdal` directly, e.g.:

`HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf":MOD_Grid_MCD15A3H:Lai_500m`

We can read the dataset with `g.ReadAsArray()`, after we have opened it. It returns a numpy array.


```python
import gdal
import numpy as np

filename = 'data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf'
dataset_name = f'HDF4_EOS:EOS_GRID:"{filename:s}":MOD_Grid_MCD15A3H:Lai_500m'
print(f"dataset: {dataset_name}")

g = gdal.Open(dataset_name)
data = g.ReadAsArray()

print(type(data))
print('max:',data.max())
print('max:',data.min())
# get unique values, for interst
print('unique values:',np.unique(data))
```

    dataset: HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf":MOD_Grid_MCD15A3H:Lai_500m
    <class 'numpy.ndarray'>
    max: 255
    max: 0
    unique values: [  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
      18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
      36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
      54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70 250
     253 254 255]


**Exercise E3.3.2**

* print out some further summary statistics of the dataset
* print out the data type and `shape`
* how many rows and columns does the dataset have?


```python
# do exercise here
```

### 3.3.2.2 Metadata

There will generally be a set of metadata associated with a geospatial dataset. This will describe e.g. the processing chain, special codes in the dataset, and projection and other information.

In `gdal`, w access the metedata using `g.GetMetadata()`. A dictionary is returned.


```python
filename = 'data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf'
dataset_name = f'HDF4_EOS:EOS_GRID:"{filename:s}":MOD_Grid_MCD15A3H:Lai_500m'
g = gdal.Open(dataset_name)

print ("\nMetedata Keys:\n")
# get the metadata dictionary keys
for k in g.GetMetadata().keys():
    print(k)
```

    
    Metedata Keys:
    
    add_offset
    add_offset_err
    ALGORITHMPACKAGEACCEPTANCEDATE
    ALGORITHMPACKAGEMATURITYCODE
    ALGORITHMPACKAGENAME
    ALGORITHMPACKAGEVERSION
    ASSOCIATEDINSTRUMENTSHORTNAME.1
    ASSOCIATEDINSTRUMENTSHORTNAME.2
    ASSOCIATEDPLATFORMSHORTNAME.1
    ASSOCIATEDPLATFORMSHORTNAME.2
    ASSOCIATEDSENSORSHORTNAME.1
    ASSOCIATEDSENSORSHORTNAME.2
    AUTOMATICQUALITYFLAG.1
    AUTOMATICQUALITYFLAGEXPLANATION.1
    calibrated_nt
    CHARACTERISTICBINANGULARSIZE500M
    CHARACTERISTICBINSIZE500M
    DATACOLUMNS500M
    DATAROWS500M
    DAYNIGHTFLAG
    DESCRREVISION
    EASTBOUNDINGCOORDINATE
    ENGINEERING_DATA
    EXCLUSIONGRINGFLAG.1
    GEOANYABNORMAL
    GEOESTMAXRMSERROR
    GLOBALGRIDCOLUMNS500M
    GLOBALGRIDROWS500M
    GRANULEBEGINNINGDATETIME
    GRANULEDAYNIGHTFLAG
    GRANULEENDINGDATETIME
    GRINGPOINTLATITUDE.1
    GRINGPOINTLONGITUDE.1
    GRINGPOINTSEQUENCENO.1
    HDFEOSVersion
    HORIZONTALTILENUMBER
    identifier_product_doi
    identifier_product_doi_authority
    INPUTPOINTER
    LOCALGRANULEID
    LOCALVERSIONID
    LONGNAME
    long_name
    MAXIMUMOBSERVATIONS500M
    MOD15A1_ANC_BUILD_CERT
    MOD15A2_FILLVALUE_DOC
    MOD15A2_FparExtra_QC_DOC
    MOD15A2_FparLai_QC_DOC
    MOD15A2_StdDev_QC_DOC
    NADIRDATARESOLUTION500M
    NDAYS_COMPOSITED
    NORTHBOUNDINGCOORDINATE
    NUMBEROFGRANULES
    PARAMETERNAME.1
    PGEVERSION
    PROCESSINGCENTER
    PROCESSINGENVIRONMENT
    PRODUCTIONDATETIME
    QAPERCENTCLOUDCOVER.1
    QAPERCENTEMPIRICALMODEL
    QAPERCENTGOODFPAR
    QAPERCENTGOODLAI
    QAPERCENTGOODQUALITY
    QAPERCENTINTERPOLATEDDATA.1
    QAPERCENTMAINMETHOD
    QAPERCENTMISSINGDATA.1
    QAPERCENTOTHERQUALITY
    QAPERCENTOUTOFBOUNDSDATA.1
    RANGEBEGINNINGDATE
    RANGEBEGINNINGTIME
    RANGEENDINGDATE
    RANGEENDINGTIME
    REPROCESSINGACTUAL
    REPROCESSINGPLANNED
    scale_factor
    scale_factor_err
    SCIENCEQUALITYFLAG.1
    SCIENCEQUALITYFLAGEXPLANATION.1
    SHORTNAME
    SOUTHBOUNDINGCOORDINATE
    SPSOPARAMETERS
    SYSTEMFILENAME
    TileID
    UM_VERSION
    units
    valid_range
    VERSIONID
    VERTICALTILENUMBER
    WESTBOUNDINGCOORDINATE
    _FillValue


Let's look at some of these metadata fields:


```python
import gdal
import numpy as np

filename = 'data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf'
dataset_name = f'HDF4_EOS:EOS_GRID:"{filename:s}":MOD_Grid_MCD15A3H:Lai_500m'
print(f"dataset: {dataset_name}")

g = gdal.Open(dataset_name)
# get the metadata dictionary keys
for k in ["LONGNAME","CHARACTERISTICBINSIZE500M",\
          "MOD15A2_FILLVALUE_DOC",\
          "GRINGPOINTLATITUDE.1","GRINGPOINTLONGITUDE.1",\
          'scale_factor']:
    print(k,g.GetMetadata()[k])
```

    dataset: HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf":MOD_Grid_MCD15A3H:Lai_500m
    LONGNAME MODIS/Terra+Aqua Leaf Area Index/FPAR 4-Day L4 Global 500m SIN Grid
    CHARACTERISTICBINSIZE500M 463.312716527778
    MOD15A2_FILLVALUE_DOC MOD15A2 FILL VALUE LEGEND
    255 = _Fillvalue, assigned when:
        * the MOD09GA suf. reflectance for channel VIS, NIR was assigned its _Fillvalue, or
        * land cover pixel itself was assigned _Fillvalus 255 or 254.
    254 = land cover assigned as perennial salt or inland fresh water.
    253 = land cover assigned as barren, sparse vegetation (rock, tundra, desert.)
    252 = land cover assigned as perennial snow, ice.
    251 = land cover assigned as "permanent" wetlands/inundated marshlands.
    250 = land cover assigned as urban/built-up.
    249 = land cover assigned as "unclassified" or not able to determine.
    
    GRINGPOINTLATITUDE.1 49.7394264948349, 59.9999999946118, 60.0089388384779, 49.7424953501575
    GRINGPOINTLONGITUDE.1 -15.4860189105775, -19.9999999949462, 0.0325645816155362, 0.0125638874822839
    scale_factor 0.1


So we see that the datasets use the MODIS Sinusoidal projection. Also we see that the pixel spacing is around 463m, there is a scale factor of 0.1 to be applied etc.

**Exercise E3.3.3**

look at the metadata to discover:

* the number of rows and columns in the dataset
* the range of valid values


```python
# do exercise here
```

## 3.3.3 Reading and displaying data

### 3.3.3.1 `glob`

Let us now suppose that we want to examine an `hdf` file that we have previously downloaded and stored in the directiory `data`.

How can we get a view into this directory to the the names of the files there?

The answer to this is `glob`, which we can access from the `pathlib` module.

Let's look in the `data` directory:


```python
from pathlib import Path

# look in this directory
in_directory = Path('data')

filenames = in_directory.glob('*')
print('files in the directory',in_directory,':')
for f in filenames:
    print(f.name)
```

    files in the directory data :
    MCD15A3H.A2016213.h18v03.006.2016239132253.hdf
    MCD15A3H.A2017149.h17v04.006.2017164112432.hdf
    MCD15A3H.A2016301.h17v03.006.2016306070409.hdf
    MCD15A3H.A2016337.h17v03.006.2016343064459.hdf
    MCD15A3H.A2017293.h17v03.006.2017300140725.hdf
    MCD15A3H.A2016121.h17v03.006.2016126073150.hdf
    MCD15A3H.A2016253.h18v04.006.2016263190244.hdf
    MCD15A3H.A2017161.h18v04.006.2017171201419.hdf
    MCD15A3H.A2017281.h17v04.006.2017286040855.hdf
    MCD15A3H.A2016197.h18v04.006.2016204134536.hdf
    MCD15A3H.A2016097.h18v03.006.2016110204452.hdf
    MCD15A3H.A2016061.h17v04.006.2016110203339.hdf
    MCD15A3H.A2016293.h18v04.006.2016302003744.hdf
    MCD15A3H.A2016169.h18v03.006.2016180114625.hdf
    MCD15A3H.A2016273.h17v04.006.2016278070708.hdf
    MCD15A3H.A2017157.h17v03.006.2017164112529.hdf
    MCD15A3H.A2016149.h17v03.006.2016159123409.hdf
    MCD15A3H.A2017297.h17v03.006.2017303194711.hdf
    MCD15A3H.A2016273.h18v03.006.2016278070409.hdf
    MCD15A3H.A2016253.h17v04.006.2016263190229.hdf
    MCD15A3H.A2017301.h17v04.006.2017310191339.hdf
    MCD15A3H.A2016265.h18v03.006.2016274181913.hdf
    MCD15A3H.A2017325.h17v03.006.2017333160951.hdf
    MCD15A3H.A2016181.h18v04.006.2016189192751.hdf
    MCD15A3H.A2016365.h18v03.006.2017014005308.hdf
    MCD15A3H.A2016165.h17v03.006.2016173050525.hdf
    MCD15A3H.A2017037.h18v03.006.2017045204444.hdf
    MCD15A3H.A2017301.h17v03.006.2017310191336.hdf
    MCD15A3H.A2016277.h17v04.006.2016285121826.hdf
    MCD15A3H.A2016009.h18v04.006.2016014074158.hdf
    MCD15A3H.A2016365.h18v04.006.2017014005312.hdf
    MCD15A3H.A2017065.h17v03.006.2017073193156.hdf
    MCD15A3H.A2016073.h18v03.006.2016110203721.hdf
    MCD15A3H.A2017h1_78_v0_34_LU.006.149_clip.FparLai_QC.vrt
    MCD15A3H.A2016057.h17v03.006.2016111145933.hdf
    MCD15A3H.A2017129.h17v03.006.2017137220918.hdf
    MCD15A3H.A2016013.h17v04.006.2016020020246.hdf
    MCD15A3H.A2017153.h18v03.006.2017164112502.hdf
    MCD15A3H.A2017121.h17v03.006.2017126042343.hdf
    MCD15A3H.A2017173.h17v03.006.2017178120232.hdf
    MCD15A3H.A2017193.h18v03.006.2017198204128.hdf
    MCD15A3H.A2016125.h18v03.006.2016130152323.hdf
    MCD15A3H.A2017181.h18v04.006.2017191193813.hdf
    MCD15A3H.A2016057.h18v04.006.2016111145944.hdf
    MCD15A3H.A2016045.h17v03.006.2016054001450.hdf
    MCD15A3H.A2016129.h17v04.006.2016135025251.hdf
    MCD15A3H.A2017225.h18v04.006.2017230033412.hdf
    MCD15A3H.A2016241.h18v03.006.2016246075613.hdf
    MCD15A3H.A2017357.h18v03.006.2018002133701.hdf
    MCD15A3H.A2016217.h18v04.006.2016239132347.hdf
    MCD15A3H.A2017201.h17v04.006.2017212170610.hdf
    MCD15A3H.A2016297.h17v03.006.2016302145250.hdf
    MCD15A3H.A2016049.h17v04.006.2016111145800.hdf
    MCD15A3H.A2016221.h17v04.006.2016239132433.hdf
    MCD15A3H.A2017249.h18v03.006.2017254031612.hdf
    MCD15A3H.A2017201.h17v03.006.2017212170608.hdf
    MCD15A3H.A2016153.h17v04.006.2016159123436.hdf
    MCD15A3H.A2017161.h18v03.006.2017171202109.hdf
    MCD15A3H.A2016193.h17v03.006.2016198083739.hdf
    MCD15A3H.A2016333.h18v04.006.2016340191400.hdf
    MCD15A3H.A2016345.h17v03.006.2016350220356.hdf
    MCD15A3H.A2017281.h18v04.006.2017286041648.hdf
    delnorte.dat
    MCD15A3H.A2017213.h18v03.006.2017227125009.hdf
    MCD15A3H.A2016025.h17v03.006.2016034034334.hdf
    MCD15A3H.A2016029.h18v04.006.2016043140353.hdf
    MCD15A3H.A2016305.h17v03.006.2016310071300.hdf
    MCD15A3H.A2016329.h17v04.006.2016340191259.hdf
    MCD15A3H.A2017093.h18v04.006.2017104154933.hdf
    MCD15A3H.A2016037.h18v04.006.2016043140911.hdf
    MCD15A3H.A2017345.h17v04.006.2017353214204.hdf
    MCD15A3H.A2016149.h17v04.006.2016159123404.hdf
    MCD15A3H.A2016093.h18v04.006.2016110204342.hdf
    MCD15A3H.A2016121.h17v04.006.2016126072647.hdf
    MCD15A3H.A2017137.h17v04.006.2017142040116.hdf
    MCD15A3H.A2017329.h18v04.006.2017334154345.hdf
    MCD15A3H.A2018273.h18v04.006.2018278143638.hdf
    MCD15A3H.A2017125.h18v04.006.2017135141218.hdf
    MCD15A3H.A2017293.h18v04.006.2017300140745.hdf
    MCD15A3H.A2016153.h18v03.006.2016159123441.hdf
    MCD15A3H.A2017253.h17v03.006.2017258030241.hdf
    MCD15A3H.A2016145.h18v03.006.2016159123336.hdf
    MCD15A3H.A2016017.h17v03.006.2016027192752.hdf
    MCD15A3H.A2017197.h17v03.006.2017202030505.hdf
    MCD15A3H.A2017233.h18v03.006.2017248101414.hdf
    MCD15A3H.A2016217.h17v03.006.2016239132333.hdf
    MCD15A3H.A2016265.h18v04.006.2016274181937.hdf
    MCD15A3H.A2017181.h18v03.006.2017191195658.hdf
    MCD15A3H.A2016185.h18v03.006.2016190065408.hdf
    MCD15A3H.A2016137.h18v03.006.2016142085230.hdf
    NOAA.csv
    MCD15A3H.A2016109.h17v04.006.2016116204817.hdf
    MCD15A3H.A2017353.h17v03.006.2017361223000.hdf
    MCD15A3H.A2017273.h18v04.006.2017278031535.hdf
    MCD15A3H.A2016065.h18v04.006.2016110203503.hdf
    MCD15A3H.A2016293.h17v04.006.2016302004722.hdf
    MCD15A3H.A2016097.h18v04.006.2016110204502.hdf
    MCD15A3H.A2016129.h18v03.006.2016135025557.hdf
    lai_filelist_2017.dat.txt
    MCD15A3H.A2017213.h18v04.006.2017227125012.hdf
    MCD15A3H.A2017277.h17v04.006.2017283110749.hdf
    MCD15A3H.A2016189.h17v03.006.2016194191636.hdf
    MCD15A3H.A2017h1_78_v0_34_LU.006.149_clip.Lai_500m.vrt
    MCD15A3H.A2017261.h18v03.006.2017266034710.hdf
    MCD15A3H.A2016013.h18v03.006.2016020014424.hdf
    huc250k_shp.zip
    MCD15A3H.A2016269.h18v03.006.2016274182022.hdf
    MCD15A3H.A2017361.h18v04.006.2018002204003.hdf
    MCD15A3H.A2016289.h17v04.006.2016294095620.hdf
    MCD15A3H.A2016269.h18v04.006.2016274182028.hdf
    MCD15A3H.A2016225.h17v03.006.2016239132521.hdf
    MCD15A3H.A2016061.h17v03.006.2016110203331.hdf
    MCD15A3H.A2016161.h17v03.006.2016167030656.hdf
    MCD15A3H.A2016041.h17v04.006.2016049125048.hdf
    MCD15A3H.A2017329.h17v03.006.2017334154337.hdf
    MCD15A3H.A2017217.h17v03.006.2017227125026.hdf
    MCD15A3H.A2017113.h18v03.006.2017118201450.hdf
    MCD15A3H.A2017157.h17v04.006.2017164112535.hdf
    MCD15A3H.A2016061.h18v04.006.2016110203352.hdf
    airtravel.csv
    MCD15A3H.A2017333.h18v03.006.2017341183458.hdf
    MCD15A3H.A2016245.h18v03.006.2016250072631.hdf
    MCD15A3H.A2016101.h18v04.006.2016110204612.hdf
    MCD15A3H.A2016305.h18v03.006.2016310071630.hdf
    MCD15A3H.A2016237.h18v04.006.2016243035643.hdf
    MCD15A3H.A2017077.h17v04.006.2017082115811.hdf
    MCD15A3H.A2016177.h17v03.006.2016184043337.hdf
    MCD15A3H.A2016005.h17v03.006.2016013012017.hdf
    MCD15A3H.A2016257.h17v04.006.2016265021329.hdf
    MCD15A3H.A2016021.h18v04.006.2016026124707.hdf
    MCD15A3H.A2017305.h18v04.006.2017312184820.hdf
    MCD15A3H.A2016173.h18v03.006.2016184015826.hdf
    MCD15A3H.A2018273.h18v03.006.2018278143633.hdf
    MCD15A3H.A2016321.h18v04.006.2016334064823.hdf
    MCD15A3H.A2017305.h18v03.006.2017312184812.hdf
    MCD15A3H.A2016141.h18v03.006.2016159123228.hdf
    MCD15A3H.A2017245.h18v03.006.2017250143542.hdf
    MCD15A3H.A2016113.h17v04.006.2016118071149.hdf
    MCD15A3H.A2016089.h18v03.006.2016110204226.hdf
    MCD15A3H.A2017061.h17v04.006.2017066071510.hdf
    MCD15A3H.A2017333.h17v03.006.2017341183030.hdf
    MCD15A3H.A2016017.h17v04.006.2016027192758.hdf
    MCD15A3H.A2017341.h17v04.006.2017346031815.hdf
    MCD15A3H.A2017033.h17v04.006.2017040180855.hdf
    MCD15A3H.A2017125.h17v03.006.2017135145623.hdf
    MCD15A3H.A2016309.h17v03.006.2016314071411.hdf
    MCD15A3H.A2017117.h17v04.006.2017122033600.hdf
    MCD15A3H.A2016329.h17v03.006.2016340191253.hdf
    MCD15A3H.A2017005.h17v03.006.2017017141758.hdf
    MCD15A3H.A2017113.h17v03.006.2017118202135.hdf
    MCD15A3H.A2017285.h18v03.006.2017290125920.hdf
    MCD15A3H.A2017041.h18v04.006.2017047163923.hdf
    MCD15A3H.A2017345.h18v04.006.2017353214523.hdf
    MCD15A3H.A2017005.h17v04.006.2017017141805.hdf
    MCD15A3H.A2017177.h17v04.006.2017187180149.hdf
    MCD15A3H.A2017185.h18v03.006.2017192121412.hdf
    MCD15A3H.A2017205.h17v04.006.2017212200246.hdf
    MCD15A3H.A2017309.h18v03.006.2017314035352.hdf
    MCD15A3H.A2017245.h17v04.006.2017250143535.hdf
    lai_filelist_2016.dat.txt
    MCD15A3H.A2016349.h17v04.006.2016357070812.hdf
    MCD15A3H.A2017277.h17v03.006.2017283110554.hdf
    MCD15A3H.A2016141.h17v03.006.2016159123250.hdf
    MCD15A3H.A2016209.h17v04.006.2016222122242.hdf
    MCD15A3H.A2017237.h18v04.006.2017242030810.hdf
    MCD15A3H.A2017169.h17v04.006.2017174032256.hdf
    MCD15A3H.A2017317.h17v04.006.2017331160712.hdf
    MCD15A3H.A2016081.h17v04.006.2016110203941.hdf
    MCD15A3H.A2017265.h18v03.006.2017271135320.hdf
    MCD15A3H.A2017249.h18v04.006.2017254030909.hdf
    MCD15A3H.A2017041.h18v03.006.2017047163913.hdf
    MCD15A3H.A2016069.h17v04.006.2016110203600.hdf
    MCD15A3H.A2017261.h18v04.006.2017266034533.hdf
    MCD15A3H.A2017069.h17v04.006.2017080124353.hdf
    grb.wkt
    MCD15A3H.A2017001.h17v03.006.2017014005341.hdf
    MCD15A3H.A2017337.h18v04.006.2017342030439.hdf
    MCD15A3H.A2016345.h17v04.006.2016350220821.hdf
    MCD15A3H.A2017221.h18v03.006.2017227172755.hdf
    MCD15A3H.A2016313.h18v03.006.2016320203216.hdf
    MCD15A3H.A2017061.h18v03.006.2017066071820.hdf
    MCD15A3H.A2016193.h18v04.006.2016198083748.hdf
    MCD15A3H.A2016213.h17v04.006.2016239132235.hdf
    MCD15A3H.A2016285.h17v04.006.2016291205844.hdf
    MCD15A3H.A2017017.h18v04.006.2017024072610.hdf
    MCD15A3H.A2017209.h17v03.006.2017214185419.hdf
    MCD15A3H.A2016049.h17v03.006.2016111145759.hdf
    MCD15A3H.A2016085.h17v03.006.2016110204055.hdf
    MCD15A3H.A2017337.h17v04.006.2017342030858.hdf
    MCD15A3H.A2017021.h18v03.006.2017031131458.hdf
    MCD15A3H.A2017025.h17v04.006.2017031144746.hdf
    MCD15A3H.A2017085.h17v03.006.2017094173906.hdf
    test_image.bin
    MCD15A3H.A2016285.h18v03.006.2016291210152.hdf
    MCD15A3H.A2016029.h17v03.006.2016043140323.hdf
    MCD15A3H.A2016237.h18v03.006.2016243035317.hdf
    MCD15A3H.A2017261.h17v04.006.2017266034239.hdf
    MCD15A3H.A2017313.h18v03.006.2017325161830.hdf
    TM_WORLD_BORDERS-0.3.dbf
    MCD15A3H.A2016325.h17v03.006.2016340191111.hdf
    MCD15A3H.A2017189.h18v04.006.2017194104724.hdf
    MCD15A3H.A2017169.h17v03.006.2017174032729.hdf
    MCD15A3H.A2016337.h17v04.006.2016343064123.hdf
    MCD15A3H.A2017281.h17v03.006.2017286041228.hdf
    MCD15A3H.A2016161.h17v04.006.2016167025525.hdf
    MCD15A3H.A2017325.h18v04.006.2017333160922.hdf
    MCD15A3H.A2016313.h17v04.006.2016320201852.hdf
    MCD15A3H.A2016181.h17v03.006.2016189192722.hdf
    MCD15A3H.A2017333.h18v04.006.2017341183037.hdf
    MCD15A3H.A2017105.h17v04.006.2017118140110.hdf
    TM_WORLD_BORDERS-0.3.shp
    MCD15A3H.A2017021.h17v03.006.2017031131446.hdf
    MCD15A3H.A2017349.h17v03.006.2017354030323.hdf
    MCD15A3H.A2017173.h18v04.006.2017178115707.hdf
    MCD15A3H.A2016033.h17v04.006.2016043140634.hdf
    MCD15A3H.A2017229.h17v03.006.2017234150110.hdf
    MCD15A3H.A2016273.h18v04.006.2016278070712.hdf
    MCD15A3H.A2017253.h18v03.006.2017258030728.hdf
    MCD15A3H.A2017313.h17v04.006.2017325161820.hdf
    MCD15A3H.A2016113.h17v03.006.2016118071447.hdf
    MCD15A3H.A2017005.h18v04.006.2017017141824.hdf
    MCD15A3H.A2016269.h17v04.006.2016274182008.hdf
    ?C=M;O=A
    MCD15A3H.A2017361.h18v03.006.2018002204108.hdf
    MCD15A3H.A2016201.h17v04.006.2016207215015.hdf
    MCD15A3H.A2016177.h17v04.006.2016184043348.hdf
    MCD15A3H.A2017089.h17v04.006.2017095140658.hdf
    MCD15A3H.A2016269.h17v03.006.2016274182007.hdf
    MCD15A3H.A2016317.h17v03.006.2016329045540.hdf
    MCD15A3H.A2016049.h18v04.006.2016111145832.hdf
    MCD15A3H.A2017297.h17v04.006.2017303195107.hdf
    MCD15A3H.A2017217.h18v04.006.2017227125035.hdf
    MCD15A3H.A2016321.h18v03.006.2016334064336.hdf
    satellites-1957-2019.gz
    MCD15A3H.A2017101.h17v04.006.2017116175131.hdf
    MCD15A3H.A2017185.h17v04.006.2017192121428.hdf
    MCD15A3H.A2017013.h18v03.006.2017021013754.hdf
    MCD15A3H.A2017353.h17v04.006.2017361223126.hdf
    MCD15A3H.A2017269.h18v04.006.2017276172441.hdf
    MCD15A3H.A2017065.h18v03.006.2017073193400.hdf
    MCD15A3H.A2017157.h18v03.006.2017164112532.hdf
    MCD15A3H.A2017277.h18v03.006.2017283110825.hdf
    MCD15A3H.A2016337.h18v03.006.2016343064522.hdf
    MCD15A3H.A2017341.h18v03.006.2017346032329.hdf
    MCD15A3H.A2016009.h18v03.006.2016014073048.hdf
    MCD15A3H.A2017225.h17v03.006.2017230033016.hdf
    MCD15A3H.A2016345.h18v03.006.2016350221132.hdf
    MCD15A3H.A2016229.h17v03.006.2016239132612.hdf
    MCD15A3H.A2017337.h17v03.006.2017342030946.hdf
    MCD15A3H.A2016073.h17v03.006.2016110203711.hdf
    MCD15A3H.A2016257.h18v04.006.2016265021336.hdf
    TM_WORLD_BORDERS-0.3.shx
    MCD15A3H.A2016141.h17v04.006.2016159123205.hdf
    MCD15A3H.A2017093.h17v03.006.2017104154927.hdf
    delNorteT_2005.dat
    MCD15A3H.A2016121.h18v03.006.2016126073203.hdf
    MCD15A3H.A2016137.h17v03.006.2016142085015.hdf
    MCD15A3H.A2016129.h17v03.006.2016135030155.hdf
    MCD15A3H.A2017285.h17v03.006.2017290125916.hdf
    MCD15A3H.A2016261.h17v03.006.2016267014113.hdf
    MCD15A3H.A2017297.h18v04.006.2017303195020.hdf
    MCD15A3H.A2016125.h17v03.006.2016130152307.hdf
    MCD15A3H.A2017049.h17v03.006.2017059114616.hdf
    MCD15A3H.A2017117.h18v03.006.2017122032334.hdf
    MCD15A3H.A2017.h1_78_v0_34_LU.006.gif
    MCD15A3H.A2017285.h17v04.006.2017290125918.hdf
    MCD15A3H.A2016365.h17v03.006.2017014005258.hdf
    MCD15A3H.A2017321.h17v03.006.2017331211621.hdf
    MCD15A3H.A2017201.h18v03.006.2017212170612.hdf
    MCD15A3H.A2016261.h17v04.006.2016267013302.hdf
    MCD15A3H.A2016289.h17v03.006.2016294100243.hdf
    MCD15A3H.A2017025.h18v04.006.2017031145243.hdf
    MCD15A3H.A2017293.h18v03.006.2017300140729.hdf
    MCD15A3H.A2016297.h18v04.006.2016302145253.hdf
    MCD15A3H.A2017141.h18v03.006.2017146025030.hdf
    MCD15A3H.A2016241.h17v03.006.2016246080654.hdf
    MCD15A3H.A2016209.h18v03.006.2016222122251.hdf
    MCD15A3H.A2017269.h17v03.006.2017276172421.hdf
    MCD15A3H.A2016065.h17v04.006.2016110203445.hdf
    MCD15A3H.A2017185.h17v03.006.2017192121419.hdf
    MCD15A3H.A2016105.h18v04.006.2016111235856.hdf
    MCD15A3H.A2016097.h17v04.006.2016110204450.hdf
    MCD15A3H.A2017089.h17v03.006.2017095141007.hdf
    MCD15A3H.A2016329.h18v03.006.2016340191304.hdf
    MCD15A3H.A2016033.h18v03.006.2016043140641.hdf
    MCD15A3H.A2017193.h17v04.006.2017198204739.hdf
    MCD15A3H.A2017073.h17v03.006.2017082030659.hdf
    MCD15A3H.A2016045.h18v04.006.2016054001527.hdf
    MCD15A3H.A2017101.h18v03.006.2017116175145.hdf
    MCD15A3H.A2017009.h18v04.006.2017018072848.hdf
    MCD15A3H.A2016361.h18v04.006.2017010020640.hdf
    MCD15A3H.A2016169.h17v04.006.2016180114633.hdf
    MCD15A3H.A2017057.h18v04.006.2017065220406.hdf
    MCD15A3H.A2016273.h17v03.006.2016278065752.hdf
    MCD15A3H.A2016145.h17v04.006.2016159123337.hdf
    MCD15A3H.A2016117.h17v04.006.2016123133231.hdf
    MCD15A3H.A2016353.h18v04.006.2016358104526.hdf
    MCD15A3H.A2016089.h17v03.006.2016110204215.hdf
    MCD15A3H.A2016313.h18v04.006.2016320201902.hdf
    MCD15A3H.A2016305.h17v04.006.2016310071624.hdf
    MCD15A3H.A2016077.h17v04.006.2016110203826.hdf
    MCD15A3H.A2016173.h18v04.006.2016184015903.hdf
    MCD15A3H.A2017133.h18v04.006.2017138030907.hdf
    MCD15A3H.A2016137.h17v04.006.2016142085022.hdf
    MCD15A3H.A2016185.h17v03.006.2016190065600.hdf
    MCD15A3H.A2017133.h18v03.006.2017138030706.hdf
    MCD15A3H.A2016281.h17v04.006.2016286204432.hdf
    MCD15A3H.A2017109.h18v03.006.2017118140142.hdf
    MCD15A3H.A2016169.h17v03.006.2016180114611.hdf
    MCD15A3H.A2017041.h17v03.006.2017047163856.hdf
    MCD15A3H.A2017029.h18v04.006.2017040040319.hdf
    saved_daymet.csv
    MCD15A3H.A2017265.h17v04.006.2017271135323.hdf
    MCD15A3H.A2017329.h18v03.006.2017334154339.hdf
    MCD15A3H.A2016205.h17v03.006.2016222121935.hdf
    MCD15A3H.A2016333.h17v04.006.2016340191351.hdf
    MCD15A3H.A2016021.h18v03.006.2016026124743.hdf
    MCD15A3H.A2016245.h17v04.006.2016250072220.hdf
    MCD15A3H.A2017097.h18v04.006.2017104155012.hdf
    MCD15A3H.A2017113.h17v04.006.2017118184030.hdf
    MCD15A3H.A2017149.h18v03.006.2017164112435.hdf
    MCD15A3H.A2016101.h17v04.006.2016110204557.hdf
    MCD15A3H.A2016221.h18v03.006.2016239132435.hdf
    MCD15A3H.A2017161.h17v04.006.2017171195752.hdf
    MCD15A3H.A2017029.h17v04.006.2017040035852.hdf
    MCD15A3H.A2017273.h17v04.006.2017278031310.hdf
    MCD15A3H.A2017213.h17v03.006.2017227125003.hdf
    MCD15A3H.A2017097.h17v04.006.2017104154956.hdf
    MCD15A3H.A2017097.h17v03.006.2017104154958.hdf
    MCD15A3H.A2017365.h17v04.006.2018005032653.hdf
    MCD15A3H.A2016001.h18v04.006.2016007073726.hdf
    MCD15A3H.A2016233.h17v04.006.2016239160839.hdf
    MCD15A3H.A2017177.h18v03.006.2017187174619.hdf
    MCD15A3H.A2017137.h18v03.006.2017142041218.hdf
    MCD15A3H.A2017045.h18v03.006.2017053101154.hdf
    MCD15A3H.A2017165.h18v03.006.2017171120907.hdf
    MCD15A3H.A2017241.h17v03.006.2017249173811.hdf
    MCD15A3H.A2017257.h17v04.006.2017262125145.hdf
    MCD15A3H.A2016161.h18v03.006.2016167030705.hdf
    Hydrologic_Units.zip
    MCD15A3H.A2016005.h17v04.006.2016013011406.hdf
    MCD15A3H.A2016089.h17v04.006.2016110204226.hdf
    MCD15A3H.A2016345.h18v04.006.2016350221138.hdf
    MCD15A3H.A2016185.h18v04.006.2016190064636.hdf
    MCD15A3H.A2017053.h18v03.006.2017059114705.hdf
    MCD15A3H.A2017061.h18v04.006.2017066071522.hdf
    MCD15A3H.A2017197.h17v04.006.2017202030356.hdf
    MCD15A3H.A2016265.h17v04.006.2016274181914.hdf
    MCD15A3H.A2016021.h17v03.006.2016026124738.hdf
    MCD15A3H.A2017137.h17v03.006.2017142035858.hdf
    MCD15A3H.A2017009.h17v03.006.2017018072233.hdf
    MCD15A3H.A2017053.h18v04.006.2017059114709.hdf
    MCD15A3H.A2017081.h17v04.006.2017087022119.hdf
    MCD15A3H.A2018273.h17v04.006.2018278143630.hdf
    MCD15A3H.A2017045.h17v03.006.2017053101326.hdf.aux.xml
    MCD15A3H.A2017033.h18v04.006.2017040180859.hdf
    MCD15A3H.A2017273.h18v03.006.2017278030912.hdf
    MCD15A3H.A2016041.h17v03.006.2016049125032.hdf
    MCD15A3H.A2017353.h18v03.006.2017361223009.hdf
    MCD15A3H.A2016237.h17v04.006.2016243035316.hdf
    MCD15A3H.A2017141.h17v03.006.2017146032650.hdf
    MCD15A3H.A2017225.h18v03.006.2017230032836.hdf
    MCD15A3H.A2017085.h17v04.006.2017094173942.hdf
    MCD15A3H.A2017005.h18v03.006.2017017141813.hdf
    MCD15A3H.A2017001.h18v03.006.2017014005401.hdf
    MCD15A3H.A2017153.h17v03.006.2017164112454.hdf
    MCD15A3H.A2017017.h17v04.006.2017024074333.hdf
    MCD15A3H.A2017261.h17v03.006.2017266033704.hdf
    lai_data_2017_UK.npz
    MCD15A3H.A2017169.h18v03.006.2017174032256.hdf
    MCD15A3H.A2017357.h18v04.006.2018002133807.hdf
    MCD15A3H.A2016177.h18v03.006.2016184045617.hdf
    MCD15A3H.A2017309.h17v04.006.2017314035345.hdf
    MCD15A3H.A2017349.h18v04.006.2017354030436.hdf
    MCD15A3H.A2016085.h18v03.006.2016110204107.hdf
    MCD15A3H.A2016165.h18v03.006.2016173045725.hdf
    MCD15A3H.A2017309.h17v03.006.2017314035405.hdf
    MCD15A3H.A2017193.h18v04.006.2017198210928.hdf
    MCD15A3H.A2017109.h17v03.006.2017118140139.hdf
    MCD15A3H.A2017269.h17v04.006.2017276172429.hdf
    MCD15A3H.A2017057.h17v04.006.2017065215830.hdf
    MCD15A3H.A2016013.h17v03.006.2016020015242.hdf
    MCD15A3H.A2016205.h17v04.006.2016222121939.hdf
    MCD15A3H.A2016205.h18v04.006.2016222121954.hdf
    MCD15A3H.A2017289.h18v03.006.2017297185623.hdf
    MCD15A3H.A2016193.h17v04.006.2016198083237.hdf
    MCD15A3H.A2017189.h17v03.006.2017194104917.hdf
    MCD15A3H.A2016161.h18v04.006.2016167030708.hdf
    MCD15A3H.A2017209.h18v04.006.2017214191653.hdf
    MCD15A3H.A2017313.h17v03.006.2017325161816.hdf
    MCD15A3H.A2017273.h17v03.006.2017278031533.hdf
    MCD15A3H.A2017305.h17v04.006.2017312184421.hdf
    MCD15A3H.A2017101.h17v03.006.2017116175258.hdf
    MCD15A3H.A2016109.h17v03.006.2016116205141.hdf
    MCD15A3H.A2017233.h17v04.006.2017248101412.hdf
    MCD15A3H.A2016365.h17v04.006.2017014005300.hdf
    MCD15A3H.A2017041.h17v04.006.2017047163857.hdf
    MCD15A3H.A2017061.h17v03.006.2017066071759.hdf
    MCD15A3H.A2017217.h18v03.006.2017227125027.hdf
    MCD15A3H.A2017001.h18v04.006.2017014005359.hdf
    MCD15A3H.A2017073.h17v04.006.2017082030700.hdf
    MCD15A3H.A2016281.h17v03.006.2016286210532.hdf
    MCD15A3H.A2016005.h18v03.006.2016013012348.hdf
    MCD15A3H.A2017265.h17v03.006.2017271135322.hdf
    MCD15A3H.A2016037.h17v04.006.2016043140849.hdf
    ?C=D;O=A
    MCD15A3H.A2016297.h18v03.006.2016302145256.hdf
    ?C=S;O=A
    MCD15A3H.A2017009.h18v03.006.2017018072246.hdf
    MCD15A3H.A2017145.h18v03.006.2017151151534.hdf
    MCD15A3H.A2016101.h17v03.006.2016110204557.hdf
    MCD15A3H.A2016341.h17v04.006.2016348174258.hdf
    MCD15A3H.A2017357.h17v04.006.2018002133721.hdf
    MCD15A3H.A2017133.h17v03.006.2017138035345.hdf
    MCD15A3H.A2017017.h17v03.006.2017024074330.hdf
    delNorteT.dat
    MCD15A3H.A2016085.h18v04.006.2016110204111.hdf
    daymet_tmax.csv
    MCD15A3H.A2016081.h18v04.006.2016110203956.hdf
    MCD15A3H.A2017181.h17v03.006.2017191190136.hdf
    data2006.pkl
    MCD15A3H.A2016293.h18v03.006.2016302004112.hdf
    MCD15A3H.A2017253.h17v04.006.2017258030637.hdf
    MCD15A3H.A2017277.h18v04.006.2017283110822.hdf
    MCD15A3H.A2017109.h18v04.006.2017118140142.hdf
    MCD15A3H.A2016245.h17v03.006.2016250072631.hdf
    MCD15A3H.A2017329.h17v04.006.2017334154340.hdf
    MCD15A3H.A2016325.h18v04.006.2016340191121.hdf
    MCD15A3H.A2017145.h17v03.006.2017151145707.hdf
    MCD15A3H.A2016157.h18v04.006.2016166093925.hdf
    MCD15A3H.A2017297.h18v03.006.2017303194717.hdf
    MCD15A3H.A2017233.h17v03.006.2017248101404.hdf
    MCD15A3H.A2016073.h17v04.006.2016110203728.hdf
    MCD15A3H.A2016141.h18v04.006.2016159123303.hdf
    MCD15A3H.A2016337.h18v04.006.2016343064525.hdf
    MCD15A3H.A2017125.h18v03.006.2017135140955.hdf
    MCD15A3H.A2017241.h18v03.006.2017249173536.hdf
    MCD15A3H.A2016077.h17v03.006.2016110203826.hdf
    MCD15A3H.A2016005.h18v04.006.2016013012025.hdf
    MCD15A3H.A2016289.h18v04.006.2016294095959.hdf
    MCD15A3H.A2016145.h17v03.006.2016159123331.hdf
    MCD15A3H.A2017229.h17v04.006.2017234145900.hdf
    Lai_500m_2017_149_LU.tif
    MCD15A3H.A2016229.h17v04.006.2016239132615.hdf
    MCD15A3H.A2017029.h17v03.006.2017040040835.hdf
    MCD15A3H.A2017037.h17v03.006.2017045204125.hdf
    MCD15A3H.A2016309.h18v04.006.2016314071420.hdf
    MCD15A3H.A2016109.h18v04.006.2016116205500.hdf
    MCD15A3H.A2017257.h17v03.006.2017262125146.hdf
    MCD15A3H.A2016301.h18v03.006.2016306070747.hdf
    MCD15A3H.A2017365.h18v04.006.2018005032627.hdf
    MCD15A3H.A2017057.h17v03.006.2017065214509.hdf
    MCD15A3H.A2016037.h17v03.006.2016043140850.hdf
    MCD15A3H.A2016201.h18v04.006.2016207215338.hdf
    MCD15A3H.A2017321.h18v04.006.2017331211501.hdf
    MCD15A3H.A2016065.h17v03.006.2016110203443.hdf
    MCD15A3H.A2016069.h18v04.006.2016110203615.hdf
    MCD15A3H.A2016249.h18v04.006.2016263190223.hdf
    MCD15A3H.A2016041.h18v03.006.2016049125050.hdf
    MCD15A3H.A2017017.h18v03.006.2017024073222.hdf
    MCD15A3H.A2017357.h17v03.006.2018002133710.hdf
    MCD15A3H.A2016117.h18v04.006.2016123133254.hdf
    MCD15A3H.A2017045.h17v04.006.2017053101338.hdf
    MCD15A3H.A2017317.h18v03.006.2017331160709.hdf
    MCD15A3H.A2017h1_78_v0_34_LU.006.149.FparLai_QC.vrt
    MCD15A3H.A2016209.h18v04.006.2016222122257.hdf
    Mauna_Loa
    MCD15A3H.A2016349.h18v04.006.2016357070838.hdf
    MCD15A3H.A2017201.h18v04.006.2017212170614.hdf
    MCD15A3H.A2016077.h18v04.006.2016110203846.hdf
    MCD15A3H.A2016233.h17v03.006.2016239154552.hdf
    MCD15A3H.A2016197.h17v03.006.2016204134529.hdf
    MCD15A3H.A2017069.h18v04.006.2017080124409.hdf
    data2005.pkl
    MCD15A3H.A2016001.h18v03.006.2016007073724.hdf
    MCD15A3H.A2017249.h17v03.006.2017254031358.hdf
    MCD15A3H.A2016061.h18v03.006.2016110203332.hdf
    MCD15A3H.A2017109.h17v04.006.2017118140138.hdf
    MCD15A3H.A2017205.h18v04.006.2017212195556.hdf
    MCD15A3H.A2016001.h17v04.006.2016007074809.hdf
    MCD15A3H.A2017153.h17v04.006.2017164112454.hdf
    MCD15A3H.A2016349.h17v03.006.2016357073003.hdf
    MCD15A3H.A2016197.h17v04.006.2016204134527.hdf
    MCD15A3H.A2017049.h17v04.006.2017059114610.hdf
    MCD15A3H.A2017157.h18v04.006.2017164112536.hdf
    MCD15A3H.A2017125.h17v04.006.2017135151227.hdf
    MCD15A3H.A2017241.h17v04.006.2017249173608.hdf
    MCD15A3H.A2017237.h17v03.006.2017242030759.hdf
    MCD15A3H.A2017169.h18v04.006.2017174031818.hdf
    MCD15A3H.A2016009.h17v03.006.2016014071957.hdf
    MCD15A3H.A2018273.h17v03.006.2018278143630.hdf
    MCD15A3H.A2017065.h18v04.006.2017073193612.hdf
    MCD15A3H.A2017253.h18v04.006.2017258030249.hdf
    MCD15A3H.A2017009.h17v04.006.2017018072237.hdf
    MCD15A3H.A2017365.h18v03.006.2018005032348.hdf
    MCD15A3H.A2017193.h17v03.006.2017198204504.hdf
    MCD15A3H.A2016277.h18v03.006.2016285121828.hdf
    MCD15A3H.A2016265.h17v03.006.2016274181912.hdf
    MCD15A3H.A2016189.h18v04.006.2016194192044.hdf
    MCD15A3H.A2017161.h17v03.006.2017171200126.hdf
    MCD15A3H.A2017133.h17v04.006.2017138033305.hdf
    MCD15A3H.A2017269.h18v03.006.2017276172441.hdf
    MCD15A3H.A2017165.h18v04.006.2017171120915.hdf
    MCD15A3H.A2016133.h17v04.006.2016140155030.hdf
    MCD15A3H.A2017093.h17v04.006.2017104154919.hdf
    MCD15A3H.A2017213.h17v04.006.2017227125011.hdf
    MCD15A3H.A2016329.h18v04.006.2016340191313.hdf
    MCD15A3H.A2016045.h18v03.006.2016054001450.hdf
    MCD15A3H.A2017229.h18v04.006.2017234150154.hdf
    MCD15A3H.A2016201.h18v03.006.2016207215333.hdf
    MCD15A3H.A2016349.h18v03.006.2016357070826.hdf
    MCD15A3H.A2017341.h18v04.006.2017346031740.hdf
    MCD15A3H.A2017197.h18v03.006.2017202033146.hdf
    MCD15A3H.A2017241.h18v04.006.2017249173311.hdf
    MCD15A3H.A2016137.h18v04.006.2016142090113.hdf
    MCD15A3H.A2016025.h18v04.006.2016034034846.hdf
    MCD15A3H.A2016225.h18v04.006.2016239132529.hdf
    MCD15A3H.A2016333.h17v03.006.2016340191343.hdf
    MCD15A3H.A2017121.h18v04.006.2017126042012.hdf
    MCD15A3H.A2016145.h18v04.006.2016159123342.hdf
    MCD15A3H.A2016225.h18v03.006.2016239132527.hdf
    MCD15A3H.A2016081.h18v03.006.2016110204002.hdf
    MCD15A3H.A2017045.h17v03.006.2017053101326.hdf
    MCD15A3H.A2017209.h18v03.006.2017214191509.hdf
    MCD15A3H.A2016133.h18v04.006.2016140155048.hdf
    MCD15A3H.A2017237.h17v04.006.2017242030424.hdf
    MCD15A3H.A2017077.h18v03.006.2017082120524.hdf
    MCD15A3H.A2017141.h18v04.006.2017146025218.hdf
    MCD15A3H.A2017221.h17v04.006.2017227170001.hdf
    MCD15A3H.A2016357.h17v03.006.2016362100705.hdf
    MCD15A3H.A2017305.h17v03.006.2017312184425.hdf
    MCD15A3H.A2016149.h18v03.006.2016159123409.hdf
    MCD15A3H.A2016289.h18v03.006.2016294095953.hdf
    MCD15A3H.A2016281.h18v03.006.2016286204934.hdf
    MCD15A3H.A2017221.h17v03.006.2017227170437.hdf
    MCD15A3H.A2017141.h17v04.006.2017146031758.hdf
    MCD15A3H.A2016189.h17v04.006.2016194191327.hdf
    MCD15A3H.A2017045.h18v04.006.2017053101351.hdf
    MCD15A3H.A2017205.h17v03.006.2017212195915.hdf
    MCD15A3H.A2017113.h18v04.006.2017118184056.hdf
    MCD15A3H.A2016353.h18v03.006.2016358104522.hdf
    MCD15A3H.A2017021.h17v04.006.2017031131450.hdf
    MCD15A3H.A2016117.h17v03.006.2016123133231.hdf
    MCD15A3H.A2016357.h17v04.006.2016362100709.hdf
    MCD15A3H.A2017081.h17v03.006.2017087022308.hdf
    MCD15A3H.A2016149.h18v04.006.2016159123411.hdf
    MCD15A3H.A2016241.h18v04.006.2016246075129.hdf
    MCD15A3H.A2016033.h18v04.006.2016043140709.hdf
    MCD15A3H.A2016033.h17v03.006.2016043140622.hdf
    MCD15A3H.A2016133.h17v03.006.2016140155029.hdf
    MCD15A3H.A2016325.h18v03.006.2016340191117.hdf
    MCD15A3H.A2017117.h18v04.006.2017122031947.hdf
    MCD15A3H.A2017177.h17v03.006.2017187174125.hdf
    MCD15A3H.A2016133.h18v03.006.2016140155050.hdf
    MCD15A3H.A2016245.h18v04.006.2016250072642.hdf
    MCD15A3H.A2016097.h17v03.006.2016110204444.hdf
    MCD15A3H.A2016249.h18v03.006.2016263190217.hdf
    MCD15A3H.A2017077.h18v04.006.2017082120528.hdf
    MCD15A3H.A2017013.h18v04.006.2017021013757.hdf
    MCD15A3H.A2016173.h17v03.006.2016184020251.hdf
    MCD15A3H.A2016121.h18v04.006.2016126072929.hdf
    MCD15A3H.A2017317.h18v04.006.2017331160715.hdf
    MCD15A3H.A2016117.h18v03.006.2016123133248.hdf
    MCD15A3H.A2016201.h17v03.006.2016207215017.hdf
    MCD15A3H.A2016313.h17v03.006.2016320202245.hdf
    MCD15A3H.A2016241.h17v04.006.2016246080640.hdf
    MCD15A3H.A2016049.h18v03.006.2016111145825.hdf
    MCD15A3H.A2017321.h18v03.006.2017331211508.hdf
    MCD15A3H.A2017029.h18v03.006.2017040040308.hdf
    MCD15A3H.A2016125.h17v04.006.2016130152307.hdf
    MCD15A3H.A2017197.h18v04.006.2017202034355.hdf
    MCD15A3H.A2017173.h18v03.006.2017178115328.hdf
    data.pkl
    MCD15A3H.A2017069.h18v03.006.2017080124401.hdf
    MCD15A3H.A2016113.h18v04.006.2016118071207.hdf
    MCD15A3H.A2016041.h18v04.006.2016049125059.hdf
    MCD15A3H.A2017289.h17v04.006.2017297185846.hdf
    MCD15A3H.A2016069.h18v03.006.2016110203608.hdf
    MCD15A3H.A2016093.h17v04.006.2016110204342.hdf
    MCD15A3H.A2016237.h17v03.006.2016243035304.hdf
    MCD15A3H.A2017221.h18v04.006.2017227170912.hdf
    MCD15A3H.A2016205.h18v03.006.2016222121947.hdf
    MCD15A3H.A2017085.h18v03.006.2017094173929.hdf
    MCD15A3H.A2017105.h17v03.006.2017118140107.hdf
    MCD15A3H.A2016277.h18v04.006.2016285121830.hdf
    MCD15A3H.A2016321.h17v04.006.2016334063807.hdf
    MCD15A3H.A2016013.h18v04.006.2016020014435.hdf
    MCD15A3H.A2016217.h18v03.006.2016239132341.hdf
    test.bin
    MCD15A3H.A2016189.h18v03.006.2016194192007.hdf
    TM_WORLD_BORDERS-0.3.prj
    MCD15A3H.A2016153.h17v03.006.2016159123426.hdf
    MCD15A3H.A2017301.h18v04.006.2017310191349.hdf
    MCD15A3H.A2016209.h17v03.006.2016222122240.hdf
    MCD15A3H.A2017101.h18v04.006.2017116175453.hdf
    MCD15A3H.A2017217.h17v04.006.2017227125027.hdf
    MCD15A3H.A2017173.h17v04.006.2017178115338.hdf
    MCD15A3H.A2017285.h18v04.006.2017290125934.hdf
    MCD15A3H.A2016045.h17v04.006.2016054001456.hdf
    MCD15A3H.A2017189.h18v03.006.2017194104914.hdf
    MCD15A3H.A2017081.h18v03.006.2017087021811.hdf
    MCD15A3H.A2016257.h18v03.006.2016265021755.hdf
    MCD15A3H.A2016173.h17v04.006.2016184033245.hdf
    MCD15A3H.A2017313.h18v04.006.2017325161833.hdf
    MCD15A3H.A2017365.h17v03.006.2018005032624.hdf
    MCD15A3H.A2016057.h17v04.006.2016111145935.hdf
    modis_6974.wkt
    MCD15A3H.A2017325.h17v04.006.2017333160942.hdf
    MCD15A3H.A2016085.h17v04.006.2016110204056.hdf
    MCD15A3H.A2016229.h18v04.006.2016239132624.hdf
    MCD15A3H.A2016089.h18v04.006.2016110204226.hdf
    MCD15A3H.A2017245.h18v04.006.2017250143542.hdf
    MCD15A3H.A2016073.h18v04.006.2016110203727.hdf
    MCD15A3H.A2016285.h17v03.006.2016291205846.hdf
    MCD15A3H.A2016213.h17v03.006.2016239132222.hdf
    MCD15A3H.A2016281.h18v04.006.2016286210123.hdf
    ?C=N;O=D
    MCD15A3H.A2016217.h17v04.006.2016239132337.hdf
    MCD15A3H.A2016301.h18v04.006.2016306071032.hdf
    MCD15A3H.A2016341.h18v03.006.2016348175231.hdf
    MCD15A3H.A2017165.h17v04.006.2017171120908.hdf
    MCD15A3H.A2016165.h18v04.006.2016173045552.hdf
    MCD15A3H.A2017081.h18v04.006.2017087022318.hdf
    MCD15A3H.A2017177.h18v04.006.2017187173712.hdf
    MCD15A3H.A2017057.h18v03.006.2017065214511.hdf
    MCD15A3H.A2016249.h17v03.006.2016263190209.hdf
    MCD15A3H.A2017077.h17v03.006.2017082120504.hdf
    MCD15A3H.A2017069.h17v03.006.2017080124350.hdf
    MCD15A3H.A2017097.h18v03.006.2017104154959.hdf
    MCD15A3H.A2017089.h18v03.006.2017095135755.hdf
    MCD15A3H.A2016361.h17v04.006.2017010015748.hdf
    MCD15A3H.A2017053.h17v03.006.2017059114658.hdf
    MCD15A3H.A2017065.h17v04.006.2017073192307.hdf
    MCD15A3H.A2016001.h17v03.006.2016007075833.hdf
    MCD15A3H.A2016017.h18v04.006.2016027193356.hdf
    MCD15A3H.A2016213.h18v04.006.2016239132255.hdf
    MCD15A3H.A2017317.h17v03.006.2017331160711.hdf
    MCD15A3H.A2016301.h17v04.006.2016306065943.hdf
    MCD15A3H.A2017309.h18v04.006.2017314035353.hdf
    MCD15A3H.A2016253.h18v03.006.2016263190242.hdf
    MCD15A3H.A2017053.h17v04.006.2017059114656.hdf
    MCD15A3H.A2017325.h18v03.006.2017333160920.hdf
    MCD15A3H.A2016261.h18v04.006.2016267013305.hdf
    MCD15A3H.A2017021.h18v04.006.2017031131510.hdf
    MCD15A3H.A2017289.h17v03.006.2017297190158.hdf
    MCD15A3H.A2017341.h17v03.006.2017346032258.hdf
    MCD15A3H.A2017117.h17v03.006.2017122032131.hdf
    MCD15A3H.A2016285.h18v04.006.2016291211648.hdf
    MCD15A3H.A2017205.h18v03.006.2017212195658.hdf
    MCD15A3H.A2016081.h17v03.006.2016110203940.hdf
    MCD15A3H.A2017289.h18v04.006.2017297185318.hdf
    MCD15A3H.A2017145.h18v04.006.2017151144037.hdf
    MCD15A3H.A2016177.h18v04.006.2016184044437.hdf
    MCD15A3H.A2017145.h17v04.006.2017151144648.hdf
    MCD15A3H.A2017149.h17v03.006.2017164112436.hdf
    MCD15A3H.A2016249.h17v04.006.2016263190211.hdf
    MCD15A3H.A2017037.h18v04.006.2017045203931.hdf
    MCD15A3H.A2016057.h18v03.006.2016111145941.hdf
    MCD15A3H.A2016129.h18v04.006.2016135032944.hdf
    MCD15A3H.A2017349.h17v04.006.2017354030754.hdf
    MCD15A3H.A2017321.h17v04.006.2017331211453.hdf
    MCD15A3H.A2016277.h17v03.006.2016285121823.hdf
    MCD15A3H.A2016357.h18v03.006.2016362103038.hdf
    MCD15A3H.A2017149.h18v04.006.2017164112441.hdf
    MCD15A3H.A2016109.h18v03.006.2016116205828.hdf
    MCD15A3H.A2016157.h18v03.006.2016166094604.hdf
    MCD15A3H.A2017121.h18v03.006.2017126042047.hdf
    MCD15A3H.A2017013.h17v03.006.2017021013427.hdf
    MCD15A3H.A2016357.h18v04.006.2016362101147.hdf
    MCD15A3H.A2016317.h17v04.006.2016329045532.hdf
    MCD15A3H.A2016257.h17v03.006.2016265021317.hdf
    MCD15A3H.A2016221.h18v04.006.2016239132440.hdf
    MCD15A3H.A2016229.h18v03.006.2016239132614.hdf
    MCD15A3H.A2016309.h18v03.006.2016314071935.hdf
    MCD15A3H.A2017037.h17v04.006.2017045203544.hdf
    MCD15A3H.A2017209.h17v04.006.2017214185419.hdf
    MCD15A3H.A2016105.h17v04.006.2016112000523.hdf
    MCD15A3H.A2016293.h17v03.006.2016302004719.hdf
    MCD15A3H.A2017121.h17v04.006.2017126042347.hdf
    MCD15A3H.A2016037.h18v03.006.2016043140917.hdf
    MCD15A3H.A2017333.h17v04.006.2017341183224.hdf
    MCD15A3H.A2017165.h17v03.006.2017171120905.hdf
    MCD15A3H.A2016309.h17v04.006.2016314071413.hdf
    MCD15A3H.A2017089.h18v04.006.2017095135837.hdf
    MCD15A3H.A2017361.h17v04.006.2018002204315.hdf
    MCD15A3H.A2016361.h17v03.006.2017010015745.hdf
    MCD15A3H.A2017073.h18v04.006.2017082030724.hdf
    MCD15A3H.A2016185.h17v04.006.2016190064224.hdf
    MCD15A3H.A2017049.h18v04.006.2017059114622.hdf
    MCD15A3H.A2016093.h17v03.006.2016110204329.hdf
    MCD15A3H.A2017049.h18v03.006.2017059114610.hdf
    MCD15A3H.A2016029.h18v03.006.2016043140341.hdf
    MCD15A3H.A2017237.h18v03.006.2017242030804.hdf
    MCD15A3H.A2016157.h17v03.006.2016166093852.hdf
    MCD15A3H.A2016233.h18v03.006.2016239161901.hdf
    MCD15A3H.A2016333.h18v03.006.2016340191348.hdf
    MCD15A2.A2011185.h09v05.005.2011213154534.hdf
    MCD15A3H.A2016297.h17v04.006.2016302145240.hdf
    MCD15A3H.A2016181.h17v04.006.2016189192727.hdf
    MCD15A3H.A2017337.h18v03.006.2017342030824.hdf
    MCD15A3H.A2016113.h18v03.006.2016118072403.hdf
    MCD15A3H.A2017257.h18v04.006.2017262125209.hdf
    MCD15A3H.A2016009.h17v04.006.2016014072006.hdf
    MCD15A3H.A2017013.h17v04.006.2017021013955.hdf
    MCD15A3H.A2017225.h17v04.006.2017230032627.hdf
    MCD15A3H.A2017265.h18v04.006.2017271135324.hdf
    MCD15A3H.A2017025.h18v03.006.2017031145746.hdf
    MCD15A3H.A2016105.h17v03.006.2016112000529.hdf
    MCD15A3H.A2016341.h18v04.006.2016348175238.hdf
    MCD15A3H.A2017257.h18v03.006.2017262125159.hdf
    MCD15A3H.A2017345.h18v03.006.2017353215001.hdf
    MCD15A3H.A2016353.h17v04.006.2016358104045.hdf
    MCD15A3H.A2016065.h18v03.006.2016110203500.hdf
    MCD15A3H.A2016025.h18v03.006.2016034034341.hdf
    MCD15A3H.A2017153.h18v04.006.2017164112502.hdf
    MCD15A3H.A2016325.h17v04.006.2016340191114.hdf
    MCD15A3H.A2016181.h18v03.006.2016189192744.hdf
    MCD15A3H.A2016341.h17v03.006.2016348175105.hdf
    MCD15A3H.A2017233.h18v04.006.2017248101417.hdf
    MCD15A3H.A2016305.h18v04.006.2016310071637.hdf
    MCD15A3H.A2016233.h18v04.006.2016239154620.hdf
    MCD15A3H.A2016153.h18v04.006.2016159123443.hdf
    MCD15A3H.A2017025.h17v03.006.2017031144743.hdf
    MCD15A3H.A2017229.h18v03.006.2017234145904.hdf
    MCD15A3H.A2017105.h18v04.006.2017118140110.hdf
    MCD15A3H.A2016253.h17v03.006.2016263190229.hdf
    MCD15A3H.A2017349.h18v03.006.2017354031001.hdf
    MCD15A3H.A2017137.h18v04.006.2017142041122.hdf
    MCD15A3H.A2016017.h18v03.006.2016027193558.hdf
    MCD15A3H.A2017093.h18v03.006.2017104154924.hdf
    MCD15A3H.A2017h1_78_v0_34_LU.006.149.Lai_500m.vrt
    MCD15A3H.A2016169.h18v04.006.2016180114625.hdf
    MCD15A3H.A2016021.h17v04.006.2016026124414.hdf
    MCD15A3H.A2017189.h17v04.006.2017194104804.hdf
    MCD15A3H.A2017073.h18v03.006.2017082031545.hdf
    MCD15A3H.A2017353.h18v04.006.2017361223133.hdf
    MCD15A3H.A2016317.h18v04.006.2016329045605.hdf
    Lai_500m_2017_001_UK.tif
    MCD15A3H.A2017085.h18v04.006.2017094173947.hdf
    MCD15A3H.A2017001.h17v04.006.2017014005344.hdf
    MCD15A3H.A2017185.h18v04.006.2017192121429.hdf
    MCD15A3H.A2016125.h18v04.006.2016130152322.hdf
    MCD15A3H.A2017129.h18v04.006.2017137215059.hdf
    MCD15A3H.A2017033.h17v03.006.2017040180926.hdf
    MCD15A3H.A2017293.h17v04.006.2017300140731.hdf
    MCD15A3H.A2016193.h18v03.006.2016198085248.hdf
    MCD15A3H.A2016221.h17v03.006.2016239132432.hdf
    MCD15A3H.A2017361.h17v03.006.2018002204120.hdf
    MCD15A3H.A2016157.h17v04.006.2016166093859.hdf
    MCD15A3H.A2017249.h17v04.006.2017254031050.hdf
    MCD15A3H.A2016225.h17v04.006.2016239132525.hdf
    MCD15A3H.A2017345.h17v03.006.2017353214417.hdf
    MCD15A3H.A2017129.h17v04.006.2017137220847.hdf
    MCD15A3H.A2017129.h18v03.006.2017137215055.hdf
    MCD15A3H.A2016165.h17v04.006.2016173045301.hdf
    MCD15A3H.A2016261.h18v03.006.2016267015350.hdf
    MCD15A3H.A2016353.h17v03.006.2016358104510.hdf
    MCD15A3H.A2017105.h18v03.006.2017118140108.hdf
    MCD15A3H.A2016069.h17v03.006.2016110203559.hdf
    MCD15A3H.A2016105.h18v03.006.2016112000619.hdf
    MCD15A3H.A2016077.h18v03.006.2016110203839.hdf
    MCD15A3H.A2017033.h18v03.006.2017040180948.hdf
    MCD15A3H.A2016093.h18v03.006.2016110204342.hdf
    MCD15A3H.A2016101.h18v03.006.2016110204603.hdf
    MCD15A3H.A2016029.h17v04.006.2016043140330.hdf
    MCD15A3H.A2016025.h17v04.006.2016034035837.hdf
    MCD15A3H.A2016361.h18v03.006.2017010020636.hdf
    FparLai_QC_2017_149_LU.tif
    MCD15A3H.A2016197.h18v03.006.2016204134521.hdf
    MCD15A3H.A2016321.h17v03.006.2016334064334.hdf
    MCD15A3H.A2017181.h17v04.006.2017191185802.hdf
    MCD15A3H.A2017281.h18v03.006.2017286041304.hdf
    TM_WORLD_BORDERS-0.3.zip
    MCD15A3H.A2016317.h18v03.006.2016329045542.hdf
    GlobAlbedo.merge.albedo.05.200901.nc
    MCD15A3H.A2017301.h18v03.006.2017310191343.hdf
    MCD15A3H.A2017245.h17v03.006.2017250143531.hdf


We use the argument `'data/*'` where `*` is a wildcard. Any filenames that match this pattern will be returned as a list.

If we want the list sorted, we need to use the `sorted()` method. This is similar to the list `sort` we have seen previously, but returns the sorted list.

The wildcard `*` here means a match to zero or more characters, so this is matching all names in the directory `data`. The wildcard `**` would mean [all files here and all sub-directories](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob).



We could be more subtle with this, e.g. matching only files ending `hdf`:


```python
from pathlib import Path

filenames = sorted(Path('data').glob('*'))

for f in filenames:
    print(f.name)
```

    ?C=D;O=A
    ?C=M;O=A
    ?C=N;O=D
    ?C=S;O=A
    FparLai_QC_2017_149_LU.tif
    GlobAlbedo.merge.albedo.05.200901.nc
    Hydrologic_Units.zip
    Lai_500m_2017_001_UK.tif
    Lai_500m_2017_149_LU.tif
    MCD15A2.A2011185.h09v05.005.2011213154534.hdf
    MCD15A3H.A2016001.h17v03.006.2016007075833.hdf
    MCD15A3H.A2016001.h17v04.006.2016007074809.hdf
    MCD15A3H.A2016001.h18v03.006.2016007073724.hdf
    MCD15A3H.A2016001.h18v04.006.2016007073726.hdf
    MCD15A3H.A2016005.h17v03.006.2016013012017.hdf
    MCD15A3H.A2016005.h17v04.006.2016013011406.hdf
    MCD15A3H.A2016005.h18v03.006.2016013012348.hdf
    MCD15A3H.A2016005.h18v04.006.2016013012025.hdf
    MCD15A3H.A2016009.h17v03.006.2016014071957.hdf
    MCD15A3H.A2016009.h17v04.006.2016014072006.hdf
    MCD15A3H.A2016009.h18v03.006.2016014073048.hdf
    MCD15A3H.A2016009.h18v04.006.2016014074158.hdf
    MCD15A3H.A2016013.h17v03.006.2016020015242.hdf
    MCD15A3H.A2016013.h17v04.006.2016020020246.hdf
    MCD15A3H.A2016013.h18v03.006.2016020014424.hdf
    MCD15A3H.A2016013.h18v04.006.2016020014435.hdf
    MCD15A3H.A2016017.h17v03.006.2016027192752.hdf
    MCD15A3H.A2016017.h17v04.006.2016027192758.hdf
    MCD15A3H.A2016017.h18v03.006.2016027193558.hdf
    MCD15A3H.A2016017.h18v04.006.2016027193356.hdf
    MCD15A3H.A2016021.h17v03.006.2016026124738.hdf
    MCD15A3H.A2016021.h17v04.006.2016026124414.hdf
    MCD15A3H.A2016021.h18v03.006.2016026124743.hdf
    MCD15A3H.A2016021.h18v04.006.2016026124707.hdf
    MCD15A3H.A2016025.h17v03.006.2016034034334.hdf
    MCD15A3H.A2016025.h17v04.006.2016034035837.hdf
    MCD15A3H.A2016025.h18v03.006.2016034034341.hdf
    MCD15A3H.A2016025.h18v04.006.2016034034846.hdf
    MCD15A3H.A2016029.h17v03.006.2016043140323.hdf
    MCD15A3H.A2016029.h17v04.006.2016043140330.hdf
    MCD15A3H.A2016029.h18v03.006.2016043140341.hdf
    MCD15A3H.A2016029.h18v04.006.2016043140353.hdf
    MCD15A3H.A2016033.h17v03.006.2016043140622.hdf
    MCD15A3H.A2016033.h17v04.006.2016043140634.hdf
    MCD15A3H.A2016033.h18v03.006.2016043140641.hdf
    MCD15A3H.A2016033.h18v04.006.2016043140709.hdf
    MCD15A3H.A2016037.h17v03.006.2016043140850.hdf
    MCD15A3H.A2016037.h17v04.006.2016043140849.hdf
    MCD15A3H.A2016037.h18v03.006.2016043140917.hdf
    MCD15A3H.A2016037.h18v04.006.2016043140911.hdf
    MCD15A3H.A2016041.h17v03.006.2016049125032.hdf
    MCD15A3H.A2016041.h17v04.006.2016049125048.hdf
    MCD15A3H.A2016041.h18v03.006.2016049125050.hdf
    MCD15A3H.A2016041.h18v04.006.2016049125059.hdf
    MCD15A3H.A2016045.h17v03.006.2016054001450.hdf
    MCD15A3H.A2016045.h17v04.006.2016054001456.hdf
    MCD15A3H.A2016045.h18v03.006.2016054001450.hdf
    MCD15A3H.A2016045.h18v04.006.2016054001527.hdf
    MCD15A3H.A2016049.h17v03.006.2016111145759.hdf
    MCD15A3H.A2016049.h17v04.006.2016111145800.hdf
    MCD15A3H.A2016049.h18v03.006.2016111145825.hdf
    MCD15A3H.A2016049.h18v04.006.2016111145832.hdf
    MCD15A3H.A2016057.h17v03.006.2016111145933.hdf
    MCD15A3H.A2016057.h17v04.006.2016111145935.hdf
    MCD15A3H.A2016057.h18v03.006.2016111145941.hdf
    MCD15A3H.A2016057.h18v04.006.2016111145944.hdf
    MCD15A3H.A2016061.h17v03.006.2016110203331.hdf
    MCD15A3H.A2016061.h17v04.006.2016110203339.hdf
    MCD15A3H.A2016061.h18v03.006.2016110203332.hdf
    MCD15A3H.A2016061.h18v04.006.2016110203352.hdf
    MCD15A3H.A2016065.h17v03.006.2016110203443.hdf
    MCD15A3H.A2016065.h17v04.006.2016110203445.hdf
    MCD15A3H.A2016065.h18v03.006.2016110203500.hdf
    MCD15A3H.A2016065.h18v04.006.2016110203503.hdf
    MCD15A3H.A2016069.h17v03.006.2016110203559.hdf
    MCD15A3H.A2016069.h17v04.006.2016110203600.hdf
    MCD15A3H.A2016069.h18v03.006.2016110203608.hdf
    MCD15A3H.A2016069.h18v04.006.2016110203615.hdf
    MCD15A3H.A2016073.h17v03.006.2016110203711.hdf
    MCD15A3H.A2016073.h17v04.006.2016110203728.hdf
    MCD15A3H.A2016073.h18v03.006.2016110203721.hdf
    MCD15A3H.A2016073.h18v04.006.2016110203727.hdf
    MCD15A3H.A2016077.h17v03.006.2016110203826.hdf
    MCD15A3H.A2016077.h17v04.006.2016110203826.hdf
    MCD15A3H.A2016077.h18v03.006.2016110203839.hdf
    MCD15A3H.A2016077.h18v04.006.2016110203846.hdf
    MCD15A3H.A2016081.h17v03.006.2016110203940.hdf
    MCD15A3H.A2016081.h17v04.006.2016110203941.hdf
    MCD15A3H.A2016081.h18v03.006.2016110204002.hdf
    MCD15A3H.A2016081.h18v04.006.2016110203956.hdf
    MCD15A3H.A2016085.h17v03.006.2016110204055.hdf
    MCD15A3H.A2016085.h17v04.006.2016110204056.hdf
    MCD15A3H.A2016085.h18v03.006.2016110204107.hdf
    MCD15A3H.A2016085.h18v04.006.2016110204111.hdf
    MCD15A3H.A2016089.h17v03.006.2016110204215.hdf
    MCD15A3H.A2016089.h17v04.006.2016110204226.hdf
    MCD15A3H.A2016089.h18v03.006.2016110204226.hdf
    MCD15A3H.A2016089.h18v04.006.2016110204226.hdf
    MCD15A3H.A2016093.h17v03.006.2016110204329.hdf
    MCD15A3H.A2016093.h17v04.006.2016110204342.hdf
    MCD15A3H.A2016093.h18v03.006.2016110204342.hdf
    MCD15A3H.A2016093.h18v04.006.2016110204342.hdf
    MCD15A3H.A2016097.h17v03.006.2016110204444.hdf
    MCD15A3H.A2016097.h17v04.006.2016110204450.hdf
    MCD15A3H.A2016097.h18v03.006.2016110204452.hdf
    MCD15A3H.A2016097.h18v04.006.2016110204502.hdf
    MCD15A3H.A2016101.h17v03.006.2016110204557.hdf
    MCD15A3H.A2016101.h17v04.006.2016110204557.hdf
    MCD15A3H.A2016101.h18v03.006.2016110204603.hdf
    MCD15A3H.A2016101.h18v04.006.2016110204612.hdf
    MCD15A3H.A2016105.h17v03.006.2016112000529.hdf
    MCD15A3H.A2016105.h17v04.006.2016112000523.hdf
    MCD15A3H.A2016105.h18v03.006.2016112000619.hdf
    MCD15A3H.A2016105.h18v04.006.2016111235856.hdf
    MCD15A3H.A2016109.h17v03.006.2016116205141.hdf
    MCD15A3H.A2016109.h17v04.006.2016116204817.hdf
    MCD15A3H.A2016109.h18v03.006.2016116205828.hdf
    MCD15A3H.A2016109.h18v04.006.2016116205500.hdf
    MCD15A3H.A2016113.h17v03.006.2016118071447.hdf
    MCD15A3H.A2016113.h17v04.006.2016118071149.hdf
    MCD15A3H.A2016113.h18v03.006.2016118072403.hdf
    MCD15A3H.A2016113.h18v04.006.2016118071207.hdf
    MCD15A3H.A2016117.h17v03.006.2016123133231.hdf
    MCD15A3H.A2016117.h17v04.006.2016123133231.hdf
    MCD15A3H.A2016117.h18v03.006.2016123133248.hdf
    MCD15A3H.A2016117.h18v04.006.2016123133254.hdf
    MCD15A3H.A2016121.h17v03.006.2016126073150.hdf
    MCD15A3H.A2016121.h17v04.006.2016126072647.hdf
    MCD15A3H.A2016121.h18v03.006.2016126073203.hdf
    MCD15A3H.A2016121.h18v04.006.2016126072929.hdf
    MCD15A3H.A2016125.h17v03.006.2016130152307.hdf
    MCD15A3H.A2016125.h17v04.006.2016130152307.hdf
    MCD15A3H.A2016125.h18v03.006.2016130152323.hdf
    MCD15A3H.A2016125.h18v04.006.2016130152322.hdf
    MCD15A3H.A2016129.h17v03.006.2016135030155.hdf
    MCD15A3H.A2016129.h17v04.006.2016135025251.hdf
    MCD15A3H.A2016129.h18v03.006.2016135025557.hdf
    MCD15A3H.A2016129.h18v04.006.2016135032944.hdf
    MCD15A3H.A2016133.h17v03.006.2016140155029.hdf
    MCD15A3H.A2016133.h17v04.006.2016140155030.hdf
    MCD15A3H.A2016133.h18v03.006.2016140155050.hdf
    MCD15A3H.A2016133.h18v04.006.2016140155048.hdf
    MCD15A3H.A2016137.h17v03.006.2016142085015.hdf
    MCD15A3H.A2016137.h17v04.006.2016142085022.hdf
    MCD15A3H.A2016137.h18v03.006.2016142085230.hdf
    MCD15A3H.A2016137.h18v04.006.2016142090113.hdf
    MCD15A3H.A2016141.h17v03.006.2016159123250.hdf
    MCD15A3H.A2016141.h17v04.006.2016159123205.hdf
    MCD15A3H.A2016141.h18v03.006.2016159123228.hdf
    MCD15A3H.A2016141.h18v04.006.2016159123303.hdf
    MCD15A3H.A2016145.h17v03.006.2016159123331.hdf
    MCD15A3H.A2016145.h17v04.006.2016159123337.hdf
    MCD15A3H.A2016145.h18v03.006.2016159123336.hdf
    MCD15A3H.A2016145.h18v04.006.2016159123342.hdf
    MCD15A3H.A2016149.h17v03.006.2016159123409.hdf
    MCD15A3H.A2016149.h17v04.006.2016159123404.hdf
    MCD15A3H.A2016149.h18v03.006.2016159123409.hdf
    MCD15A3H.A2016149.h18v04.006.2016159123411.hdf
    MCD15A3H.A2016153.h17v03.006.2016159123426.hdf
    MCD15A3H.A2016153.h17v04.006.2016159123436.hdf
    MCD15A3H.A2016153.h18v03.006.2016159123441.hdf
    MCD15A3H.A2016153.h18v04.006.2016159123443.hdf
    MCD15A3H.A2016157.h17v03.006.2016166093852.hdf
    MCD15A3H.A2016157.h17v04.006.2016166093859.hdf
    MCD15A3H.A2016157.h18v03.006.2016166094604.hdf
    MCD15A3H.A2016157.h18v04.006.2016166093925.hdf
    MCD15A3H.A2016161.h17v03.006.2016167030656.hdf
    MCD15A3H.A2016161.h17v04.006.2016167025525.hdf
    MCD15A3H.A2016161.h18v03.006.2016167030705.hdf
    MCD15A3H.A2016161.h18v04.006.2016167030708.hdf
    MCD15A3H.A2016165.h17v03.006.2016173050525.hdf
    MCD15A3H.A2016165.h17v04.006.2016173045301.hdf
    MCD15A3H.A2016165.h18v03.006.2016173045725.hdf
    MCD15A3H.A2016165.h18v04.006.2016173045552.hdf
    MCD15A3H.A2016169.h17v03.006.2016180114611.hdf
    MCD15A3H.A2016169.h17v04.006.2016180114633.hdf
    MCD15A3H.A2016169.h18v03.006.2016180114625.hdf
    MCD15A3H.A2016169.h18v04.006.2016180114625.hdf
    MCD15A3H.A2016173.h17v03.006.2016184020251.hdf
    MCD15A3H.A2016173.h17v04.006.2016184033245.hdf
    MCD15A3H.A2016173.h18v03.006.2016184015826.hdf
    MCD15A3H.A2016173.h18v04.006.2016184015903.hdf
    MCD15A3H.A2016177.h17v03.006.2016184043337.hdf
    MCD15A3H.A2016177.h17v04.006.2016184043348.hdf
    MCD15A3H.A2016177.h18v03.006.2016184045617.hdf
    MCD15A3H.A2016177.h18v04.006.2016184044437.hdf
    MCD15A3H.A2016181.h17v03.006.2016189192722.hdf
    MCD15A3H.A2016181.h17v04.006.2016189192727.hdf
    MCD15A3H.A2016181.h18v03.006.2016189192744.hdf
    MCD15A3H.A2016181.h18v04.006.2016189192751.hdf
    MCD15A3H.A2016185.h17v03.006.2016190065600.hdf
    MCD15A3H.A2016185.h17v04.006.2016190064224.hdf
    MCD15A3H.A2016185.h18v03.006.2016190065408.hdf
    MCD15A3H.A2016185.h18v04.006.2016190064636.hdf
    MCD15A3H.A2016189.h17v03.006.2016194191636.hdf
    MCD15A3H.A2016189.h17v04.006.2016194191327.hdf
    MCD15A3H.A2016189.h18v03.006.2016194192007.hdf
    MCD15A3H.A2016189.h18v04.006.2016194192044.hdf
    MCD15A3H.A2016193.h17v03.006.2016198083739.hdf
    MCD15A3H.A2016193.h17v04.006.2016198083237.hdf
    MCD15A3H.A2016193.h18v03.006.2016198085248.hdf
    MCD15A3H.A2016193.h18v04.006.2016198083748.hdf
    MCD15A3H.A2016197.h17v03.006.2016204134529.hdf
    MCD15A3H.A2016197.h17v04.006.2016204134527.hdf
    MCD15A3H.A2016197.h18v03.006.2016204134521.hdf
    MCD15A3H.A2016197.h18v04.006.2016204134536.hdf
    MCD15A3H.A2016201.h17v03.006.2016207215017.hdf
    MCD15A3H.A2016201.h17v04.006.2016207215015.hdf
    MCD15A3H.A2016201.h18v03.006.2016207215333.hdf
    MCD15A3H.A2016201.h18v04.006.2016207215338.hdf
    MCD15A3H.A2016205.h17v03.006.2016222121935.hdf
    MCD15A3H.A2016205.h17v04.006.2016222121939.hdf
    MCD15A3H.A2016205.h18v03.006.2016222121947.hdf
    MCD15A3H.A2016205.h18v04.006.2016222121954.hdf
    MCD15A3H.A2016209.h17v03.006.2016222122240.hdf
    MCD15A3H.A2016209.h17v04.006.2016222122242.hdf
    MCD15A3H.A2016209.h18v03.006.2016222122251.hdf
    MCD15A3H.A2016209.h18v04.006.2016222122257.hdf
    MCD15A3H.A2016213.h17v03.006.2016239132222.hdf
    MCD15A3H.A2016213.h17v04.006.2016239132235.hdf
    MCD15A3H.A2016213.h18v03.006.2016239132253.hdf
    MCD15A3H.A2016213.h18v04.006.2016239132255.hdf
    MCD15A3H.A2016217.h17v03.006.2016239132333.hdf
    MCD15A3H.A2016217.h17v04.006.2016239132337.hdf
    MCD15A3H.A2016217.h18v03.006.2016239132341.hdf
    MCD15A3H.A2016217.h18v04.006.2016239132347.hdf
    MCD15A3H.A2016221.h17v03.006.2016239132432.hdf
    MCD15A3H.A2016221.h17v04.006.2016239132433.hdf
    MCD15A3H.A2016221.h18v03.006.2016239132435.hdf
    MCD15A3H.A2016221.h18v04.006.2016239132440.hdf
    MCD15A3H.A2016225.h17v03.006.2016239132521.hdf
    MCD15A3H.A2016225.h17v04.006.2016239132525.hdf
    MCD15A3H.A2016225.h18v03.006.2016239132527.hdf
    MCD15A3H.A2016225.h18v04.006.2016239132529.hdf
    MCD15A3H.A2016229.h17v03.006.2016239132612.hdf
    MCD15A3H.A2016229.h17v04.006.2016239132615.hdf
    MCD15A3H.A2016229.h18v03.006.2016239132614.hdf
    MCD15A3H.A2016229.h18v04.006.2016239132624.hdf
    MCD15A3H.A2016233.h17v03.006.2016239154552.hdf
    MCD15A3H.A2016233.h17v04.006.2016239160839.hdf
    MCD15A3H.A2016233.h18v03.006.2016239161901.hdf
    MCD15A3H.A2016233.h18v04.006.2016239154620.hdf
    MCD15A3H.A2016237.h17v03.006.2016243035304.hdf
    MCD15A3H.A2016237.h17v04.006.2016243035316.hdf
    MCD15A3H.A2016237.h18v03.006.2016243035317.hdf
    MCD15A3H.A2016237.h18v04.006.2016243035643.hdf
    MCD15A3H.A2016241.h17v03.006.2016246080654.hdf
    MCD15A3H.A2016241.h17v04.006.2016246080640.hdf
    MCD15A3H.A2016241.h18v03.006.2016246075613.hdf
    MCD15A3H.A2016241.h18v04.006.2016246075129.hdf
    MCD15A3H.A2016245.h17v03.006.2016250072631.hdf
    MCD15A3H.A2016245.h17v04.006.2016250072220.hdf
    MCD15A3H.A2016245.h18v03.006.2016250072631.hdf
    MCD15A3H.A2016245.h18v04.006.2016250072642.hdf
    MCD15A3H.A2016249.h17v03.006.2016263190209.hdf
    MCD15A3H.A2016249.h17v04.006.2016263190211.hdf
    MCD15A3H.A2016249.h18v03.006.2016263190217.hdf
    MCD15A3H.A2016249.h18v04.006.2016263190223.hdf
    MCD15A3H.A2016253.h17v03.006.2016263190229.hdf
    MCD15A3H.A2016253.h17v04.006.2016263190229.hdf
    MCD15A3H.A2016253.h18v03.006.2016263190242.hdf
    MCD15A3H.A2016253.h18v04.006.2016263190244.hdf
    MCD15A3H.A2016257.h17v03.006.2016265021317.hdf
    MCD15A3H.A2016257.h17v04.006.2016265021329.hdf
    MCD15A3H.A2016257.h18v03.006.2016265021755.hdf
    MCD15A3H.A2016257.h18v04.006.2016265021336.hdf
    MCD15A3H.A2016261.h17v03.006.2016267014113.hdf
    MCD15A3H.A2016261.h17v04.006.2016267013302.hdf
    MCD15A3H.A2016261.h18v03.006.2016267015350.hdf
    MCD15A3H.A2016261.h18v04.006.2016267013305.hdf
    MCD15A3H.A2016265.h17v03.006.2016274181912.hdf
    MCD15A3H.A2016265.h17v04.006.2016274181914.hdf
    MCD15A3H.A2016265.h18v03.006.2016274181913.hdf
    MCD15A3H.A2016265.h18v04.006.2016274181937.hdf
    MCD15A3H.A2016269.h17v03.006.2016274182007.hdf
    MCD15A3H.A2016269.h17v04.006.2016274182008.hdf
    MCD15A3H.A2016269.h18v03.006.2016274182022.hdf
    MCD15A3H.A2016269.h18v04.006.2016274182028.hdf
    MCD15A3H.A2016273.h17v03.006.2016278065752.hdf
    MCD15A3H.A2016273.h17v04.006.2016278070708.hdf
    MCD15A3H.A2016273.h18v03.006.2016278070409.hdf
    MCD15A3H.A2016273.h18v04.006.2016278070712.hdf
    MCD15A3H.A2016277.h17v03.006.2016285121823.hdf
    MCD15A3H.A2016277.h17v04.006.2016285121826.hdf
    MCD15A3H.A2016277.h18v03.006.2016285121828.hdf
    MCD15A3H.A2016277.h18v04.006.2016285121830.hdf
    MCD15A3H.A2016281.h17v03.006.2016286210532.hdf
    MCD15A3H.A2016281.h17v04.006.2016286204432.hdf
    MCD15A3H.A2016281.h18v03.006.2016286204934.hdf
    MCD15A3H.A2016281.h18v04.006.2016286210123.hdf
    MCD15A3H.A2016285.h17v03.006.2016291205846.hdf
    MCD15A3H.A2016285.h17v04.006.2016291205844.hdf
    MCD15A3H.A2016285.h18v03.006.2016291210152.hdf
    MCD15A3H.A2016285.h18v04.006.2016291211648.hdf
    MCD15A3H.A2016289.h17v03.006.2016294100243.hdf
    MCD15A3H.A2016289.h17v04.006.2016294095620.hdf
    MCD15A3H.A2016289.h18v03.006.2016294095953.hdf
    MCD15A3H.A2016289.h18v04.006.2016294095959.hdf
    MCD15A3H.A2016293.h17v03.006.2016302004719.hdf
    MCD15A3H.A2016293.h17v04.006.2016302004722.hdf
    MCD15A3H.A2016293.h18v03.006.2016302004112.hdf
    MCD15A3H.A2016293.h18v04.006.2016302003744.hdf
    MCD15A3H.A2016297.h17v03.006.2016302145250.hdf
    MCD15A3H.A2016297.h17v04.006.2016302145240.hdf
    MCD15A3H.A2016297.h18v03.006.2016302145256.hdf
    MCD15A3H.A2016297.h18v04.006.2016302145253.hdf
    MCD15A3H.A2016301.h17v03.006.2016306070409.hdf
    MCD15A3H.A2016301.h17v04.006.2016306065943.hdf
    MCD15A3H.A2016301.h18v03.006.2016306070747.hdf
    MCD15A3H.A2016301.h18v04.006.2016306071032.hdf
    MCD15A3H.A2016305.h17v03.006.2016310071300.hdf
    MCD15A3H.A2016305.h17v04.006.2016310071624.hdf
    MCD15A3H.A2016305.h18v03.006.2016310071630.hdf
    MCD15A3H.A2016305.h18v04.006.2016310071637.hdf
    MCD15A3H.A2016309.h17v03.006.2016314071411.hdf
    MCD15A3H.A2016309.h17v04.006.2016314071413.hdf
    MCD15A3H.A2016309.h18v03.006.2016314071935.hdf
    MCD15A3H.A2016309.h18v04.006.2016314071420.hdf
    MCD15A3H.A2016313.h17v03.006.2016320202245.hdf
    MCD15A3H.A2016313.h17v04.006.2016320201852.hdf
    MCD15A3H.A2016313.h18v03.006.2016320203216.hdf
    MCD15A3H.A2016313.h18v04.006.2016320201902.hdf
    MCD15A3H.A2016317.h17v03.006.2016329045540.hdf
    MCD15A3H.A2016317.h17v04.006.2016329045532.hdf
    MCD15A3H.A2016317.h18v03.006.2016329045542.hdf
    MCD15A3H.A2016317.h18v04.006.2016329045605.hdf
    MCD15A3H.A2016321.h17v03.006.2016334064334.hdf
    MCD15A3H.A2016321.h17v04.006.2016334063807.hdf
    MCD15A3H.A2016321.h18v03.006.2016334064336.hdf
    MCD15A3H.A2016321.h18v04.006.2016334064823.hdf
    MCD15A3H.A2016325.h17v03.006.2016340191111.hdf
    MCD15A3H.A2016325.h17v04.006.2016340191114.hdf
    MCD15A3H.A2016325.h18v03.006.2016340191117.hdf
    MCD15A3H.A2016325.h18v04.006.2016340191121.hdf
    MCD15A3H.A2016329.h17v03.006.2016340191253.hdf
    MCD15A3H.A2016329.h17v04.006.2016340191259.hdf
    MCD15A3H.A2016329.h18v03.006.2016340191304.hdf
    MCD15A3H.A2016329.h18v04.006.2016340191313.hdf
    MCD15A3H.A2016333.h17v03.006.2016340191343.hdf
    MCD15A3H.A2016333.h17v04.006.2016340191351.hdf
    MCD15A3H.A2016333.h18v03.006.2016340191348.hdf
    MCD15A3H.A2016333.h18v04.006.2016340191400.hdf
    MCD15A3H.A2016337.h17v03.006.2016343064459.hdf
    MCD15A3H.A2016337.h17v04.006.2016343064123.hdf
    MCD15A3H.A2016337.h18v03.006.2016343064522.hdf
    MCD15A3H.A2016337.h18v04.006.2016343064525.hdf
    MCD15A3H.A2016341.h17v03.006.2016348175105.hdf
    MCD15A3H.A2016341.h17v04.006.2016348174258.hdf
    MCD15A3H.A2016341.h18v03.006.2016348175231.hdf
    MCD15A3H.A2016341.h18v04.006.2016348175238.hdf
    MCD15A3H.A2016345.h17v03.006.2016350220356.hdf
    MCD15A3H.A2016345.h17v04.006.2016350220821.hdf
    MCD15A3H.A2016345.h18v03.006.2016350221132.hdf
    MCD15A3H.A2016345.h18v04.006.2016350221138.hdf
    MCD15A3H.A2016349.h17v03.006.2016357073003.hdf
    MCD15A3H.A2016349.h17v04.006.2016357070812.hdf
    MCD15A3H.A2016349.h18v03.006.2016357070826.hdf
    MCD15A3H.A2016349.h18v04.006.2016357070838.hdf
    MCD15A3H.A2016353.h17v03.006.2016358104510.hdf
    MCD15A3H.A2016353.h17v04.006.2016358104045.hdf
    MCD15A3H.A2016353.h18v03.006.2016358104522.hdf
    MCD15A3H.A2016353.h18v04.006.2016358104526.hdf
    MCD15A3H.A2016357.h17v03.006.2016362100705.hdf
    MCD15A3H.A2016357.h17v04.006.2016362100709.hdf
    MCD15A3H.A2016357.h18v03.006.2016362103038.hdf
    MCD15A3H.A2016357.h18v04.006.2016362101147.hdf
    MCD15A3H.A2016361.h17v03.006.2017010015745.hdf
    MCD15A3H.A2016361.h17v04.006.2017010015748.hdf
    MCD15A3H.A2016361.h18v03.006.2017010020636.hdf
    MCD15A3H.A2016361.h18v04.006.2017010020640.hdf
    MCD15A3H.A2016365.h17v03.006.2017014005258.hdf
    MCD15A3H.A2016365.h17v04.006.2017014005300.hdf
    MCD15A3H.A2016365.h18v03.006.2017014005308.hdf
    MCD15A3H.A2016365.h18v04.006.2017014005312.hdf
    MCD15A3H.A2017.h1_78_v0_34_LU.006.gif
    MCD15A3H.A2017001.h17v03.006.2017014005341.hdf
    MCD15A3H.A2017001.h17v04.006.2017014005344.hdf
    MCD15A3H.A2017001.h18v03.006.2017014005401.hdf
    MCD15A3H.A2017001.h18v04.006.2017014005359.hdf
    MCD15A3H.A2017005.h17v03.006.2017017141758.hdf
    MCD15A3H.A2017005.h17v04.006.2017017141805.hdf
    MCD15A3H.A2017005.h18v03.006.2017017141813.hdf
    MCD15A3H.A2017005.h18v04.006.2017017141824.hdf
    MCD15A3H.A2017009.h17v03.006.2017018072233.hdf
    MCD15A3H.A2017009.h17v04.006.2017018072237.hdf
    MCD15A3H.A2017009.h18v03.006.2017018072246.hdf
    MCD15A3H.A2017009.h18v04.006.2017018072848.hdf
    MCD15A3H.A2017013.h17v03.006.2017021013427.hdf
    MCD15A3H.A2017013.h17v04.006.2017021013955.hdf
    MCD15A3H.A2017013.h18v03.006.2017021013754.hdf
    MCD15A3H.A2017013.h18v04.006.2017021013757.hdf
    MCD15A3H.A2017017.h17v03.006.2017024074330.hdf
    MCD15A3H.A2017017.h17v04.006.2017024074333.hdf
    MCD15A3H.A2017017.h18v03.006.2017024073222.hdf
    MCD15A3H.A2017017.h18v04.006.2017024072610.hdf
    MCD15A3H.A2017021.h17v03.006.2017031131446.hdf
    MCD15A3H.A2017021.h17v04.006.2017031131450.hdf
    MCD15A3H.A2017021.h18v03.006.2017031131458.hdf
    MCD15A3H.A2017021.h18v04.006.2017031131510.hdf
    MCD15A3H.A2017025.h17v03.006.2017031144743.hdf
    MCD15A3H.A2017025.h17v04.006.2017031144746.hdf
    MCD15A3H.A2017025.h18v03.006.2017031145746.hdf
    MCD15A3H.A2017025.h18v04.006.2017031145243.hdf
    MCD15A3H.A2017029.h17v03.006.2017040040835.hdf
    MCD15A3H.A2017029.h17v04.006.2017040035852.hdf
    MCD15A3H.A2017029.h18v03.006.2017040040308.hdf
    MCD15A3H.A2017029.h18v04.006.2017040040319.hdf
    MCD15A3H.A2017033.h17v03.006.2017040180926.hdf
    MCD15A3H.A2017033.h17v04.006.2017040180855.hdf
    MCD15A3H.A2017033.h18v03.006.2017040180948.hdf
    MCD15A3H.A2017033.h18v04.006.2017040180859.hdf
    MCD15A3H.A2017037.h17v03.006.2017045204125.hdf
    MCD15A3H.A2017037.h17v04.006.2017045203544.hdf
    MCD15A3H.A2017037.h18v03.006.2017045204444.hdf
    MCD15A3H.A2017037.h18v04.006.2017045203931.hdf
    MCD15A3H.A2017041.h17v03.006.2017047163856.hdf
    MCD15A3H.A2017041.h17v04.006.2017047163857.hdf
    MCD15A3H.A2017041.h18v03.006.2017047163913.hdf
    MCD15A3H.A2017041.h18v04.006.2017047163923.hdf
    MCD15A3H.A2017045.h17v03.006.2017053101326.hdf
    MCD15A3H.A2017045.h17v03.006.2017053101326.hdf.aux.xml
    MCD15A3H.A2017045.h17v04.006.2017053101338.hdf
    MCD15A3H.A2017045.h18v03.006.2017053101154.hdf
    MCD15A3H.A2017045.h18v04.006.2017053101351.hdf
    MCD15A3H.A2017049.h17v03.006.2017059114616.hdf
    MCD15A3H.A2017049.h17v04.006.2017059114610.hdf
    MCD15A3H.A2017049.h18v03.006.2017059114610.hdf
    MCD15A3H.A2017049.h18v04.006.2017059114622.hdf
    MCD15A3H.A2017053.h17v03.006.2017059114658.hdf
    MCD15A3H.A2017053.h17v04.006.2017059114656.hdf
    MCD15A3H.A2017053.h18v03.006.2017059114705.hdf
    MCD15A3H.A2017053.h18v04.006.2017059114709.hdf
    MCD15A3H.A2017057.h17v03.006.2017065214509.hdf
    MCD15A3H.A2017057.h17v04.006.2017065215830.hdf
    MCD15A3H.A2017057.h18v03.006.2017065214511.hdf
    MCD15A3H.A2017057.h18v04.006.2017065220406.hdf
    MCD15A3H.A2017061.h17v03.006.2017066071759.hdf
    MCD15A3H.A2017061.h17v04.006.2017066071510.hdf
    MCD15A3H.A2017061.h18v03.006.2017066071820.hdf
    MCD15A3H.A2017061.h18v04.006.2017066071522.hdf
    MCD15A3H.A2017065.h17v03.006.2017073193156.hdf
    MCD15A3H.A2017065.h17v04.006.2017073192307.hdf
    MCD15A3H.A2017065.h18v03.006.2017073193400.hdf
    MCD15A3H.A2017065.h18v04.006.2017073193612.hdf
    MCD15A3H.A2017069.h17v03.006.2017080124350.hdf
    MCD15A3H.A2017069.h17v04.006.2017080124353.hdf
    MCD15A3H.A2017069.h18v03.006.2017080124401.hdf
    MCD15A3H.A2017069.h18v04.006.2017080124409.hdf
    MCD15A3H.A2017073.h17v03.006.2017082030659.hdf
    MCD15A3H.A2017073.h17v04.006.2017082030700.hdf
    MCD15A3H.A2017073.h18v03.006.2017082031545.hdf
    MCD15A3H.A2017073.h18v04.006.2017082030724.hdf
    MCD15A3H.A2017077.h17v03.006.2017082120504.hdf
    MCD15A3H.A2017077.h17v04.006.2017082115811.hdf
    MCD15A3H.A2017077.h18v03.006.2017082120524.hdf
    MCD15A3H.A2017077.h18v04.006.2017082120528.hdf
    MCD15A3H.A2017081.h17v03.006.2017087022308.hdf
    MCD15A3H.A2017081.h17v04.006.2017087022119.hdf
    MCD15A3H.A2017081.h18v03.006.2017087021811.hdf
    MCD15A3H.A2017081.h18v04.006.2017087022318.hdf
    MCD15A3H.A2017085.h17v03.006.2017094173906.hdf
    MCD15A3H.A2017085.h17v04.006.2017094173942.hdf
    MCD15A3H.A2017085.h18v03.006.2017094173929.hdf
    MCD15A3H.A2017085.h18v04.006.2017094173947.hdf
    MCD15A3H.A2017089.h17v03.006.2017095141007.hdf
    MCD15A3H.A2017089.h17v04.006.2017095140658.hdf
    MCD15A3H.A2017089.h18v03.006.2017095135755.hdf
    MCD15A3H.A2017089.h18v04.006.2017095135837.hdf
    MCD15A3H.A2017093.h17v03.006.2017104154927.hdf
    MCD15A3H.A2017093.h17v04.006.2017104154919.hdf
    MCD15A3H.A2017093.h18v03.006.2017104154924.hdf
    MCD15A3H.A2017093.h18v04.006.2017104154933.hdf
    MCD15A3H.A2017097.h17v03.006.2017104154958.hdf
    MCD15A3H.A2017097.h17v04.006.2017104154956.hdf
    MCD15A3H.A2017097.h18v03.006.2017104154959.hdf
    MCD15A3H.A2017097.h18v04.006.2017104155012.hdf
    MCD15A3H.A2017101.h17v03.006.2017116175258.hdf
    MCD15A3H.A2017101.h17v04.006.2017116175131.hdf
    MCD15A3H.A2017101.h18v03.006.2017116175145.hdf
    MCD15A3H.A2017101.h18v04.006.2017116175453.hdf
    MCD15A3H.A2017105.h17v03.006.2017118140107.hdf
    MCD15A3H.A2017105.h17v04.006.2017118140110.hdf
    MCD15A3H.A2017105.h18v03.006.2017118140108.hdf
    MCD15A3H.A2017105.h18v04.006.2017118140110.hdf
    MCD15A3H.A2017109.h17v03.006.2017118140139.hdf
    MCD15A3H.A2017109.h17v04.006.2017118140138.hdf
    MCD15A3H.A2017109.h18v03.006.2017118140142.hdf
    MCD15A3H.A2017109.h18v04.006.2017118140142.hdf
    MCD15A3H.A2017113.h17v03.006.2017118202135.hdf
    MCD15A3H.A2017113.h17v04.006.2017118184030.hdf
    MCD15A3H.A2017113.h18v03.006.2017118201450.hdf
    MCD15A3H.A2017113.h18v04.006.2017118184056.hdf
    MCD15A3H.A2017117.h17v03.006.2017122032131.hdf
    MCD15A3H.A2017117.h17v04.006.2017122033600.hdf
    MCD15A3H.A2017117.h18v03.006.2017122032334.hdf
    MCD15A3H.A2017117.h18v04.006.2017122031947.hdf
    MCD15A3H.A2017121.h17v03.006.2017126042343.hdf
    MCD15A3H.A2017121.h17v04.006.2017126042347.hdf
    MCD15A3H.A2017121.h18v03.006.2017126042047.hdf
    MCD15A3H.A2017121.h18v04.006.2017126042012.hdf
    MCD15A3H.A2017125.h17v03.006.2017135145623.hdf
    MCD15A3H.A2017125.h17v04.006.2017135151227.hdf
    MCD15A3H.A2017125.h18v03.006.2017135140955.hdf
    MCD15A3H.A2017125.h18v04.006.2017135141218.hdf
    MCD15A3H.A2017129.h17v03.006.2017137220918.hdf
    MCD15A3H.A2017129.h17v04.006.2017137220847.hdf
    MCD15A3H.A2017129.h18v03.006.2017137215055.hdf
    MCD15A3H.A2017129.h18v04.006.2017137215059.hdf
    MCD15A3H.A2017133.h17v03.006.2017138035345.hdf
    MCD15A3H.A2017133.h17v04.006.2017138033305.hdf
    MCD15A3H.A2017133.h18v03.006.2017138030706.hdf
    MCD15A3H.A2017133.h18v04.006.2017138030907.hdf
    MCD15A3H.A2017137.h17v03.006.2017142035858.hdf
    MCD15A3H.A2017137.h17v04.006.2017142040116.hdf
    MCD15A3H.A2017137.h18v03.006.2017142041218.hdf
    MCD15A3H.A2017137.h18v04.006.2017142041122.hdf
    MCD15A3H.A2017141.h17v03.006.2017146032650.hdf
    MCD15A3H.A2017141.h17v04.006.2017146031758.hdf
    MCD15A3H.A2017141.h18v03.006.2017146025030.hdf
    MCD15A3H.A2017141.h18v04.006.2017146025218.hdf
    MCD15A3H.A2017145.h17v03.006.2017151145707.hdf
    MCD15A3H.A2017145.h17v04.006.2017151144648.hdf
    MCD15A3H.A2017145.h18v03.006.2017151151534.hdf
    MCD15A3H.A2017145.h18v04.006.2017151144037.hdf
    MCD15A3H.A2017149.h17v03.006.2017164112436.hdf
    MCD15A3H.A2017149.h17v04.006.2017164112432.hdf
    MCD15A3H.A2017149.h18v03.006.2017164112435.hdf
    MCD15A3H.A2017149.h18v04.006.2017164112441.hdf
    MCD15A3H.A2017153.h17v03.006.2017164112454.hdf
    MCD15A3H.A2017153.h17v04.006.2017164112454.hdf
    MCD15A3H.A2017153.h18v03.006.2017164112502.hdf
    MCD15A3H.A2017153.h18v04.006.2017164112502.hdf
    MCD15A3H.A2017157.h17v03.006.2017164112529.hdf
    MCD15A3H.A2017157.h17v04.006.2017164112535.hdf
    MCD15A3H.A2017157.h18v03.006.2017164112532.hdf
    MCD15A3H.A2017157.h18v04.006.2017164112536.hdf
    MCD15A3H.A2017161.h17v03.006.2017171200126.hdf
    MCD15A3H.A2017161.h17v04.006.2017171195752.hdf
    MCD15A3H.A2017161.h18v03.006.2017171202109.hdf
    MCD15A3H.A2017161.h18v04.006.2017171201419.hdf
    MCD15A3H.A2017165.h17v03.006.2017171120905.hdf
    MCD15A3H.A2017165.h17v04.006.2017171120908.hdf
    MCD15A3H.A2017165.h18v03.006.2017171120907.hdf
    MCD15A3H.A2017165.h18v04.006.2017171120915.hdf
    MCD15A3H.A2017169.h17v03.006.2017174032729.hdf
    MCD15A3H.A2017169.h17v04.006.2017174032256.hdf
    MCD15A3H.A2017169.h18v03.006.2017174032256.hdf
    MCD15A3H.A2017169.h18v04.006.2017174031818.hdf
    MCD15A3H.A2017173.h17v03.006.2017178120232.hdf
    MCD15A3H.A2017173.h17v04.006.2017178115338.hdf
    MCD15A3H.A2017173.h18v03.006.2017178115328.hdf
    MCD15A3H.A2017173.h18v04.006.2017178115707.hdf
    MCD15A3H.A2017177.h17v03.006.2017187174125.hdf
    MCD15A3H.A2017177.h17v04.006.2017187180149.hdf
    MCD15A3H.A2017177.h18v03.006.2017187174619.hdf
    MCD15A3H.A2017177.h18v04.006.2017187173712.hdf
    MCD15A3H.A2017181.h17v03.006.2017191190136.hdf
    MCD15A3H.A2017181.h17v04.006.2017191185802.hdf
    MCD15A3H.A2017181.h18v03.006.2017191195658.hdf
    MCD15A3H.A2017181.h18v04.006.2017191193813.hdf
    MCD15A3H.A2017185.h17v03.006.2017192121419.hdf
    MCD15A3H.A2017185.h17v04.006.2017192121428.hdf
    MCD15A3H.A2017185.h18v03.006.2017192121412.hdf
    MCD15A3H.A2017185.h18v04.006.2017192121429.hdf
    MCD15A3H.A2017189.h17v03.006.2017194104917.hdf
    MCD15A3H.A2017189.h17v04.006.2017194104804.hdf
    MCD15A3H.A2017189.h18v03.006.2017194104914.hdf
    MCD15A3H.A2017189.h18v04.006.2017194104724.hdf
    MCD15A3H.A2017193.h17v03.006.2017198204504.hdf
    MCD15A3H.A2017193.h17v04.006.2017198204739.hdf
    MCD15A3H.A2017193.h18v03.006.2017198204128.hdf
    MCD15A3H.A2017193.h18v04.006.2017198210928.hdf
    MCD15A3H.A2017197.h17v03.006.2017202030505.hdf
    MCD15A3H.A2017197.h17v04.006.2017202030356.hdf
    MCD15A3H.A2017197.h18v03.006.2017202033146.hdf
    MCD15A3H.A2017197.h18v04.006.2017202034355.hdf
    MCD15A3H.A2017201.h17v03.006.2017212170608.hdf
    MCD15A3H.A2017201.h17v04.006.2017212170610.hdf
    MCD15A3H.A2017201.h18v03.006.2017212170612.hdf
    MCD15A3H.A2017201.h18v04.006.2017212170614.hdf
    MCD15A3H.A2017205.h17v03.006.2017212195915.hdf
    MCD15A3H.A2017205.h17v04.006.2017212200246.hdf
    MCD15A3H.A2017205.h18v03.006.2017212195658.hdf
    MCD15A3H.A2017205.h18v04.006.2017212195556.hdf
    MCD15A3H.A2017209.h17v03.006.2017214185419.hdf
    MCD15A3H.A2017209.h17v04.006.2017214185419.hdf
    MCD15A3H.A2017209.h18v03.006.2017214191509.hdf
    MCD15A3H.A2017209.h18v04.006.2017214191653.hdf
    MCD15A3H.A2017213.h17v03.006.2017227125003.hdf
    MCD15A3H.A2017213.h17v04.006.2017227125011.hdf
    MCD15A3H.A2017213.h18v03.006.2017227125009.hdf
    MCD15A3H.A2017213.h18v04.006.2017227125012.hdf
    MCD15A3H.A2017217.h17v03.006.2017227125026.hdf
    MCD15A3H.A2017217.h17v04.006.2017227125027.hdf
    MCD15A3H.A2017217.h18v03.006.2017227125027.hdf
    MCD15A3H.A2017217.h18v04.006.2017227125035.hdf
    MCD15A3H.A2017221.h17v03.006.2017227170437.hdf
    MCD15A3H.A2017221.h17v04.006.2017227170001.hdf
    MCD15A3H.A2017221.h18v03.006.2017227172755.hdf
    MCD15A3H.A2017221.h18v04.006.2017227170912.hdf
    MCD15A3H.A2017225.h17v03.006.2017230033016.hdf
    MCD15A3H.A2017225.h17v04.006.2017230032627.hdf
    MCD15A3H.A2017225.h18v03.006.2017230032836.hdf
    MCD15A3H.A2017225.h18v04.006.2017230033412.hdf
    MCD15A3H.A2017229.h17v03.006.2017234150110.hdf
    MCD15A3H.A2017229.h17v04.006.2017234145900.hdf
    MCD15A3H.A2017229.h18v03.006.2017234145904.hdf
    MCD15A3H.A2017229.h18v04.006.2017234150154.hdf
    MCD15A3H.A2017233.h17v03.006.2017248101404.hdf
    MCD15A3H.A2017233.h17v04.006.2017248101412.hdf
    MCD15A3H.A2017233.h18v03.006.2017248101414.hdf
    MCD15A3H.A2017233.h18v04.006.2017248101417.hdf
    MCD15A3H.A2017237.h17v03.006.2017242030759.hdf
    MCD15A3H.A2017237.h17v04.006.2017242030424.hdf
    MCD15A3H.A2017237.h18v03.006.2017242030804.hdf
    MCD15A3H.A2017237.h18v04.006.2017242030810.hdf
    MCD15A3H.A2017241.h17v03.006.2017249173811.hdf
    MCD15A3H.A2017241.h17v04.006.2017249173608.hdf
    MCD15A3H.A2017241.h18v03.006.2017249173536.hdf
    MCD15A3H.A2017241.h18v04.006.2017249173311.hdf
    MCD15A3H.A2017245.h17v03.006.2017250143531.hdf
    MCD15A3H.A2017245.h17v04.006.2017250143535.hdf
    MCD15A3H.A2017245.h18v03.006.2017250143542.hdf
    MCD15A3H.A2017245.h18v04.006.2017250143542.hdf
    MCD15A3H.A2017249.h17v03.006.2017254031358.hdf
    MCD15A3H.A2017249.h17v04.006.2017254031050.hdf
    MCD15A3H.A2017249.h18v03.006.2017254031612.hdf
    MCD15A3H.A2017249.h18v04.006.2017254030909.hdf
    MCD15A3H.A2017253.h17v03.006.2017258030241.hdf
    MCD15A3H.A2017253.h17v04.006.2017258030637.hdf
    MCD15A3H.A2017253.h18v03.006.2017258030728.hdf
    MCD15A3H.A2017253.h18v04.006.2017258030249.hdf
    MCD15A3H.A2017257.h17v03.006.2017262125146.hdf
    MCD15A3H.A2017257.h17v04.006.2017262125145.hdf
    MCD15A3H.A2017257.h18v03.006.2017262125159.hdf
    MCD15A3H.A2017257.h18v04.006.2017262125209.hdf
    MCD15A3H.A2017261.h17v03.006.2017266033704.hdf
    MCD15A3H.A2017261.h17v04.006.2017266034239.hdf
    MCD15A3H.A2017261.h18v03.006.2017266034710.hdf
    MCD15A3H.A2017261.h18v04.006.2017266034533.hdf
    MCD15A3H.A2017265.h17v03.006.2017271135322.hdf
    MCD15A3H.A2017265.h17v04.006.2017271135323.hdf
    MCD15A3H.A2017265.h18v03.006.2017271135320.hdf
    MCD15A3H.A2017265.h18v04.006.2017271135324.hdf
    MCD15A3H.A2017269.h17v03.006.2017276172421.hdf
    MCD15A3H.A2017269.h17v04.006.2017276172429.hdf
    MCD15A3H.A2017269.h18v03.006.2017276172441.hdf
    MCD15A3H.A2017269.h18v04.006.2017276172441.hdf
    MCD15A3H.A2017273.h17v03.006.2017278031533.hdf
    MCD15A3H.A2017273.h17v04.006.2017278031310.hdf
    MCD15A3H.A2017273.h18v03.006.2017278030912.hdf
    MCD15A3H.A2017273.h18v04.006.2017278031535.hdf
    MCD15A3H.A2017277.h17v03.006.2017283110554.hdf
    MCD15A3H.A2017277.h17v04.006.2017283110749.hdf
    MCD15A3H.A2017277.h18v03.006.2017283110825.hdf
    MCD15A3H.A2017277.h18v04.006.2017283110822.hdf
    MCD15A3H.A2017281.h17v03.006.2017286041228.hdf
    MCD15A3H.A2017281.h17v04.006.2017286040855.hdf
    MCD15A3H.A2017281.h18v03.006.2017286041304.hdf
    MCD15A3H.A2017281.h18v04.006.2017286041648.hdf
    MCD15A3H.A2017285.h17v03.006.2017290125916.hdf
    MCD15A3H.A2017285.h17v04.006.2017290125918.hdf
    MCD15A3H.A2017285.h18v03.006.2017290125920.hdf
    MCD15A3H.A2017285.h18v04.006.2017290125934.hdf
    MCD15A3H.A2017289.h17v03.006.2017297190158.hdf
    MCD15A3H.A2017289.h17v04.006.2017297185846.hdf
    MCD15A3H.A2017289.h18v03.006.2017297185623.hdf
    MCD15A3H.A2017289.h18v04.006.2017297185318.hdf
    MCD15A3H.A2017293.h17v03.006.2017300140725.hdf
    MCD15A3H.A2017293.h17v04.006.2017300140731.hdf
    MCD15A3H.A2017293.h18v03.006.2017300140729.hdf
    MCD15A3H.A2017293.h18v04.006.2017300140745.hdf
    MCD15A3H.A2017297.h17v03.006.2017303194711.hdf
    MCD15A3H.A2017297.h17v04.006.2017303195107.hdf
    MCD15A3H.A2017297.h18v03.006.2017303194717.hdf
    MCD15A3H.A2017297.h18v04.006.2017303195020.hdf
    MCD15A3H.A2017301.h17v03.006.2017310191336.hdf
    MCD15A3H.A2017301.h17v04.006.2017310191339.hdf
    MCD15A3H.A2017301.h18v03.006.2017310191343.hdf
    MCD15A3H.A2017301.h18v04.006.2017310191349.hdf
    MCD15A3H.A2017305.h17v03.006.2017312184425.hdf
    MCD15A3H.A2017305.h17v04.006.2017312184421.hdf
    MCD15A3H.A2017305.h18v03.006.2017312184812.hdf
    MCD15A3H.A2017305.h18v04.006.2017312184820.hdf
    MCD15A3H.A2017309.h17v03.006.2017314035405.hdf
    MCD15A3H.A2017309.h17v04.006.2017314035345.hdf
    MCD15A3H.A2017309.h18v03.006.2017314035352.hdf
    MCD15A3H.A2017309.h18v04.006.2017314035353.hdf
    MCD15A3H.A2017313.h17v03.006.2017325161816.hdf
    MCD15A3H.A2017313.h17v04.006.2017325161820.hdf
    MCD15A3H.A2017313.h18v03.006.2017325161830.hdf
    MCD15A3H.A2017313.h18v04.006.2017325161833.hdf
    MCD15A3H.A2017317.h17v03.006.2017331160711.hdf
    MCD15A3H.A2017317.h17v04.006.2017331160712.hdf
    MCD15A3H.A2017317.h18v03.006.2017331160709.hdf
    MCD15A3H.A2017317.h18v04.006.2017331160715.hdf
    MCD15A3H.A2017321.h17v03.006.2017331211621.hdf
    MCD15A3H.A2017321.h17v04.006.2017331211453.hdf
    MCD15A3H.A2017321.h18v03.006.2017331211508.hdf
    MCD15A3H.A2017321.h18v04.006.2017331211501.hdf
    MCD15A3H.A2017325.h17v03.006.2017333160951.hdf
    MCD15A3H.A2017325.h17v04.006.2017333160942.hdf
    MCD15A3H.A2017325.h18v03.006.2017333160920.hdf
    MCD15A3H.A2017325.h18v04.006.2017333160922.hdf
    MCD15A3H.A2017329.h17v03.006.2017334154337.hdf
    MCD15A3H.A2017329.h17v04.006.2017334154340.hdf
    MCD15A3H.A2017329.h18v03.006.2017334154339.hdf
    MCD15A3H.A2017329.h18v04.006.2017334154345.hdf
    MCD15A3H.A2017333.h17v03.006.2017341183030.hdf
    MCD15A3H.A2017333.h17v04.006.2017341183224.hdf
    MCD15A3H.A2017333.h18v03.006.2017341183458.hdf
    MCD15A3H.A2017333.h18v04.006.2017341183037.hdf
    MCD15A3H.A2017337.h17v03.006.2017342030946.hdf
    MCD15A3H.A2017337.h17v04.006.2017342030858.hdf
    MCD15A3H.A2017337.h18v03.006.2017342030824.hdf
    MCD15A3H.A2017337.h18v04.006.2017342030439.hdf
    MCD15A3H.A2017341.h17v03.006.2017346032258.hdf
    MCD15A3H.A2017341.h17v04.006.2017346031815.hdf
    MCD15A3H.A2017341.h18v03.006.2017346032329.hdf
    MCD15A3H.A2017341.h18v04.006.2017346031740.hdf
    MCD15A3H.A2017345.h17v03.006.2017353214417.hdf
    MCD15A3H.A2017345.h17v04.006.2017353214204.hdf
    MCD15A3H.A2017345.h18v03.006.2017353215001.hdf
    MCD15A3H.A2017345.h18v04.006.2017353214523.hdf
    MCD15A3H.A2017349.h17v03.006.2017354030323.hdf
    MCD15A3H.A2017349.h17v04.006.2017354030754.hdf
    MCD15A3H.A2017349.h18v03.006.2017354031001.hdf
    MCD15A3H.A2017349.h18v04.006.2017354030436.hdf
    MCD15A3H.A2017353.h17v03.006.2017361223000.hdf
    MCD15A3H.A2017353.h17v04.006.2017361223126.hdf
    MCD15A3H.A2017353.h18v03.006.2017361223009.hdf
    MCD15A3H.A2017353.h18v04.006.2017361223133.hdf
    MCD15A3H.A2017357.h17v03.006.2018002133710.hdf
    MCD15A3H.A2017357.h17v04.006.2018002133721.hdf
    MCD15A3H.A2017357.h18v03.006.2018002133701.hdf
    MCD15A3H.A2017357.h18v04.006.2018002133807.hdf
    MCD15A3H.A2017361.h17v03.006.2018002204120.hdf
    MCD15A3H.A2017361.h17v04.006.2018002204315.hdf
    MCD15A3H.A2017361.h18v03.006.2018002204108.hdf
    MCD15A3H.A2017361.h18v04.006.2018002204003.hdf
    MCD15A3H.A2017365.h17v03.006.2018005032624.hdf
    MCD15A3H.A2017365.h17v04.006.2018005032653.hdf
    MCD15A3H.A2017365.h18v03.006.2018005032348.hdf
    MCD15A3H.A2017365.h18v04.006.2018005032627.hdf
    MCD15A3H.A2017h1_78_v0_34_LU.006.149.FparLai_QC.vrt
    MCD15A3H.A2017h1_78_v0_34_LU.006.149.Lai_500m.vrt
    MCD15A3H.A2017h1_78_v0_34_LU.006.149_clip.FparLai_QC.vrt
    MCD15A3H.A2017h1_78_v0_34_LU.006.149_clip.Lai_500m.vrt
    MCD15A3H.A2018273.h17v03.006.2018278143630.hdf
    MCD15A3H.A2018273.h17v04.006.2018278143630.hdf
    MCD15A3H.A2018273.h18v03.006.2018278143633.hdf
    MCD15A3H.A2018273.h18v04.006.2018278143638.hdf
    Mauna_Loa
    NOAA.csv
    TM_WORLD_BORDERS-0.3.dbf
    TM_WORLD_BORDERS-0.3.prj
    TM_WORLD_BORDERS-0.3.shp
    TM_WORLD_BORDERS-0.3.shx
    TM_WORLD_BORDERS-0.3.zip
    airtravel.csv
    data.pkl
    data2005.pkl
    data2006.pkl
    daymet_tmax.csv
    delNorteT.dat
    delNorteT_2005.dat
    delnorte.dat
    grb.wkt
    huc250k_shp.zip
    lai_data_2017_UK.npz
    lai_filelist_2016.dat.txt
    lai_filelist_2017.dat.txt
    modis_6974.wkt
    satellites-1957-2019.gz
    saved_daymet.csv
    test.bin
    test_image.bin


**Exercise 3.3.4**

* adapt the code above to return only hdf filenames for the tile `h18v03`


```python
# do exercise here
```

### 3.3.3.2 reading and displaying image data

Let's now read some data as above.

we do this with:

    g.Open(gdal_fname)
    data = g.ReadAsArray()
    
Originally the data are `uint8` (unsigned 8 bit data), but we need to multiply them by `scale_factor` (0.1 here) to convert to physical units. This also casts the data type to `float`.

We can straightforwardly plot the images using `matplotlib`. We first importt the library:

    import matplotlib.pylab as plt
    
Then set up the figure size:

    plt.figure(figsize=(10,10))
    
Plot the image:

    plt.imshow( data, vmin=0, vmax=6,cmap=plt.cm.inferno_r)
    
where here `data` is a 2-D dataset. We can set limits to the image scaling (`vmin`, `vmax`), so that we emphasise a particular range of values, and we can apply custom colourmaps (`cmap=plt.cm.inferno_r`).

Finally here, we set a title, and plot a colour wedge to show the data scale. The `scale=0.8` here allows us to align the size of the scale with the plotted image size.

    plt.title(dataset_name)
    plt.colorbar(shrink=0.8)
    
If we want to save the plotted image to a file, e.g. in the directory `images`, we use:

    plt.savefig(out_filename)
    
    


```python
import gdal
from pathlib import Path
import matplotlib.pylab as plt

# get only v03 hdf names
filenames = sorted(Path('data').glob('*2018*v03*.hdf'))


out_directory = Path('images')

for filename in filenames:
    # pull the tile name from the filename
    # to use as plot title
    tile = filename.name.split('.')[2]
    
    dataset_name = f'HDF4_EOS:EOS_GRID:"{str(filename):s}\":MOD_Grid_MCD15A3H:Lai_500m'
    g = gdal.Open(dataset_name)
    data = g.ReadAsArray()
    scale_factor = float(g.GetMetadata()['scale_factor'])
    
    print(dataset_name,scale_factor)
    print('*'*len(dataset_name))
    print(type(data),data.dtype,data.shape,'\n')
    
    data = data * scale_factor
    print(type(data),data.dtype,data.shape,'\n')
    plt.figure(figsize=(10,10))
    plt.imshow( data, vmin=0, vmax=6,cmap=plt.cm.inferno_r)
    plt.title(tile)
    plt.colorbar(shrink=0.8)
    
    # save figure as png
    plot_name = filename.stem + '.png'
    print(plot_name)
    out_filename = out_directory.joinpath(plot_name)
    plt.savefig(out_filename)
```

    HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h17v03.006.2018278143630.hdf":MOD_Grid_MCD15A3H:Lai_500m 0.1
    **************************************************************************************************
    <class 'numpy.ndarray'> uint8 (2400, 2400) 
    
    <class 'numpy.ndarray'> float64 (2400, 2400) 
    
    MCD15A3H.A2018273.h17v03.006.2018278143630.png
    HDF4_EOS:EOS_GRID:"data/MCD15A3H.A2018273.h18v03.006.2018278143633.hdf":MOD_Grid_MCD15A3H:Lai_500m 0.1
    **************************************************************************************************
    <class 'numpy.ndarray'> uint8 (2400, 2400) 
    
    <class 'numpy.ndarray'> float64 (2400, 2400) 
    
    MCD15A3H.A2018273.h18v03.006.2018278143633.png



![png](034_GDAL_masking_files/034_GDAL_masking_34_1.png)



![png](034_GDAL_masking_files/034_GDAL_masking_34_2.png)



```python
# Let's check the images we saved are there!
# and access some file info while we are here
# using pathlib
from pathlib import Path
from datetime import datetime

for f in Path('images').glob('MCD*2018*v03*.png'):
    
    # get the file size in bytes 
    size_in_B = f.stat().st_size
    
    # get the file modification time (ns)
    mod_date_ns = f.stat().st_mtime_ns
    mod_date = datetime.fromtimestamp(mod_date_ns // 1000000000)
    
    print(f'{f} {size_in_B} Bytes {mod_date}')
```

    images/MCD15A3H.A2018273.h18v03.006.2018278143633.png 318419 Bytes 2020-09-05 07:46:11
    images/MCD15A3H.A2018273.h17v03.006.2018278143630.png 152076 Bytes 2020-09-05 07:46:10


### 3.3.3.3 subplot plotting

Often, we want to have several figures on the same plot. We can do this with `plt.subplots()`:

The way we set the title and other features is slightly diifferent, but there are many example of different plot types on the web we can follow as examples.


```python
import gdal
from pathlib import Path
import matplotlib.pylab as plt
import numpy as np

filenames = sorted(Path('data').glob('*2018*v03*.hdf'))

out_directory = Path('images')

'''
Set up subplots of 1 row x 2 columns
'''
fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True,
                       figsize=(10,5))
# need to force axs collapse to a 2D array
# for indexing to be easy T here is transpose
# to get row/col the right way around
axs = np.array(axs).T.flatten()

for i,filename in enumerate(filenames):
    # pull the tile name from the filename
    # to use as plot title
    tile = filename.name.split('.')[2]
    
    
    dataset_name = f'HDF4_EOS:EOS_GRID:"{str(filename):s}\":MOD_Grid_MCD15A3H:Lai_500m'
    g = gdal.Open(dataset_name)
    data = g.ReadAsArray() * float(g.GetMetadata()['scale_factor'])

    img = axs[i].imshow(data, interpolation="nearest", vmin=0, vmax=4,
                 cmap=plt.cm.inferno_r)
    axs[i].set_title(tile)
    plt.colorbar(img,ax=axs[i],shrink=0.7)
    
# save figure as pdf this time
plot_name = 'joinedup.pdf'
print(plot_name)
out_filename = out_directory.joinpath(plot_name)
plt.savefig(out_filename)
```

    joinedup.pdf



![png](034_GDAL_masking_files/034_GDAL_masking_37_1.png)


**Exercise 3.3.5**

We now want to use the additional files:

    MCD15A3H.A2018273.h17v04.006.2018278143630.hdf	
    MCD15A3H.A2018273.h18v04.006.2018278143638.hdf

* copy and change the code above to use files of the pattern `*v0[3,4]*.hdf`
* use subplot as above to plot a 2x2 set of subplots of these data.


**Hint**

The code should look much like that above, but you need to give the fiuller list of filenames and set the subplot shape.

The code `[3,4]` in the pattern `*v0[3,4]*.hdf` means match either `3` or `4`, so the pattern must be `*v03*.hdf` or `*v03*.hdf`.

The result should look like:

![](images/joinedup4.pdf)


```python
# do exercise here
```

### 3.3.3.3 tile stitching

You may want to generate a single view of the 4 tiles.

We could achieve this by stitching things together "by hand"...

**recipe:**

* First, lets generate a 3D dataset with all 4 tiles, so we have the images stored as members of a list `data[0]`,`data[1]`,`data[2]` and `data[3]`:

        data = []
        for filename in filenames:
            dataname = f'HDF4_EOS:EOS_GRID:"{str(filename):s}":MOD_Grid_MCD15A3H:Lai_500m'
            g = gdal.Open(dataname)
            data.append(g.ReadAsArray() * scale)

* then, we produce vertical stacks of the first two and last two files. This can be done in various ways, but it is perhaps clearest to use `np.vstack()`

        top = np.vstack([data[0],data[1]])
        bot = np.vstack([data[2],data[3]])
        
* then, produce a horizontal stack of these stacks:

        lai_stich = np.hstack([top,bot])
        
and plot the dataset


```python
import gdal
from pathlib import Path
import matplotlib.pylab as plt

scale = 0.1

filenames = sorted(Path('data').glob('*2018*v0*.hdf'))

data = []
for filename in filenames:
    dataname = f'HDF4_EOS:EOS_GRID:"{str(filename)}":MOD_Grid_MCD15A3H:Lai_500m'
    g = gdal.Open(dataname)
    # append each image to the data list
    data.append(g.ReadAsArray() * scale)

top = np.vstack([data[0],data[1]])
bot = np.vstack([data[2],data[3]])

lai_stich = np.hstack([top,bot])

plt.figure(figsize=(10,10))
plt.imshow(lai_stich, interpolation="nearest", vmin=0, vmax=4,
          cmap=plt.cm.inferno_r)
plt.colorbar(shrink=0.8)
```




    <matplotlib.colorbar.Colorbar at 0x7fe650a6ecd0>




![png](034_GDAL_masking_files/034_GDAL_masking_41_1.png)


**Exercise 3.3.6**

* examine how the `vstack` and `hstack` methods work. Print out the shape of the array after stacking to appreciate this.
* how big (in pixels) is the whole dataset now? 
* If a `float` is 64 bits, how many bytes is this data array likely to be?


```python
# do exercise here
```

### 3.3.3.4 `gdal` virtual file

However, stitching in this way is problematic if you want to mosaic many tiles, as you need to read in all the data in memory. Also,some tiles may be missing. GDAL allows you to create a mosaic as [virtual file format](https://www.gdal.org/gdal_vrttut.html), using gdal.BuildVRT (check the documentation). 

This function takes two inputs: the output filename (`stitch_up.vrt`) and a set of GDAL format filenames. It returns the open output dataset, so that we can check what it looks like with e.g. `gdal.Info`


```python
import gdal
from pathlib import Path

# need to convert filenames to strings
# which we can do with p.as_posix() or str(p)
filenames = sorted([p.as_posix() for p in Path('data').glob('*273*v0[3,4]*.hdf')])
datanames = [f'HDF4_EOS:EOS_GRID:"{str(filename)}":MOD_Grid_MCD15A3H:Lai_500m' \
                for filename in filenames]
stitch_vrt = gdal.BuildVRT("stitch_up.vrt", datanames)

print(gdal.Info(stitch_vrt))
```

    Driver: VRT/Virtual Raster
    Files: stitch_up.vrt
    Size is 4800, 4800
    Coordinate System is:
    PROJCRS["unnamed",
        BASEGEOGCRS["Unknown datum based upon the custom spheroid",
            DATUM["Not specified (based on custom spheroid)",
                ELLIPSOID["Custom spheroid",6371007.181,0,
                    LENGTHUNIT["metre",1,
                        ID["EPSG",9001]]]],
            PRIMEM["Greenwich",0,
                ANGLEUNIT["degree",0.0174532925199433,
                    ID["EPSG",9122]]]],
        CONVERSION["unnamed",
            METHOD["Sinusoidal"],
            PARAMETER["Longitude of natural origin",0,
                ANGLEUNIT["degree",0.0174532925199433],
                ID["EPSG",8802]],
            PARAMETER["False easting",0,
                LENGTHUNIT["Meter",1],
                ID["EPSG",8806]],
            PARAMETER["False northing",0,
                LENGTHUNIT["Meter",1],
                ID["EPSG",8807]]],
        CS[Cartesian,2],
            AXIS["easting",east,
                ORDER[1],
                LENGTHUNIT["Meter",1]],
            AXIS["northing",north,
                ORDER[2],
                LENGTHUNIT["Meter",1]]]
    Data axis to CRS axis mapping: 1,2
    Origin = (-1111950.519667000044137,6671703.117999999783933)
    Pixel Size = (463.312716527916621,-463.312716527708290)
    Corner Coordinates:
    Upper Left  (-1111950.520, 6671703.118) ( 20d 0' 0.00"W, 60d 0' 0.00"N)
    Lower Left  (-1111950.520, 4447802.079) ( 13d 3'14.66"W, 40d 0' 0.00"N)
    Upper Right ( 1111950.520, 6671703.118) ( 20d 0' 0.00"E, 60d 0' 0.00"N)
    Lower Right ( 1111950.520, 4447802.079) ( 13d 3'14.66"E, 40d 0' 0.00"N)
    Center      (      -0.000, 5559752.598) (  0d 0' 0.00"W, 50d 0' 0.00"N)
    Band 1 Block=128x128 Type=Byte, ColorInterp=Gray
      NoData Value=255
      Offset: 0,   Scale:0.1
    


So we see that we now have 4800 columns by 4800 rows dataset, centered around 0 degrees North, 0 degrees W. Let's plot the data...


```python
# stitch_vrt is an already opened GDAL dataset, needs to be read in
plt.figure(figsize=(10,10))
plt.imshow(stitch_vrt.ReadAsArray()*0.1,
           interpolation="nearest", vmin=0, vmax=6, 
          cmap=plt.cm.inferno_r)
```




    <matplotlib.image.AxesImage at 0x7fe648f037d0>




![png](034_GDAL_masking_files/034_GDAL_masking_47_1.png)


## 3.3.4 The country borders dataset

A number of vectors with countries and administrative subdivisions are available. The [TM_WORLD_BORDERS shapefile](http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip) is popular and in the public domain. You can see it, and have a look at the data [here](https://koordinates.com/layer/7354-tm-world-borders-03/). We need to download and unzip this file... We'll use requests as before, and we'll unpack the zip file using [`shutil.unpack_archive`](https://docs.python.org/3/library/shutil.html#shutil.unpack_archive)


```python
import requests
import shutil 

tm_borders_url = "http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip"

r = requests.get(tm_borders_url)
with open("data/TM_WORLD_BORDERS-0.3.zip", 'wb') as fp:
    fp.write (r.content)

shutil.unpack_archive("data/TM_WORLD_BORDERS-0.3.zip",
                     extract_dir="data/")
```


    ---------------------------------------------------------------------------

    ReadError                                 Traceback (most recent call last)

    <ipython-input-23-58a2ee86d0b5> in <module>
          9 
         10 shutil.unpack_archive("data/TM_WORLD_BORDERS-0.3.zip",
    ---> 11                      extract_dir="data/")
    

    ~/anaconda3/envs/geog0111/lib/python3.7/shutil.py in unpack_archive(filename, extract_dir, format)
       1000         func = _UNPACK_FORMATS[format][1]
       1001         kwargs = dict(_UNPACK_FORMATS[format][2])
    -> 1002         func(filename, extract_dir, **kwargs)
       1003 
       1004 


    ~/anaconda3/envs/geog0111/lib/python3.7/shutil.py in _unpack_zipfile(filename, extract_dir)
        897 
        898     if not zipfile.is_zipfile(filename):
    --> 899         raise ReadError("%s is not a zip file" % filename)
        900 
        901     zip = zipfile.ZipFile(filename)


    ReadError: data/TM_WORLD_BORDERS-0.3.zip is not a zip file


Make sure you have the relevant files available in your `data` folder! We can then inspect the dataset using the command line tool `ogrinfo`. We can call it from the shell by appending the `!` symbol, and select that we want to check only the data for the UK (stored in the `FIPS` field with value `UK`):


It is worth noting that using OGR's queries trying to match a string, the string needs to be surrounded by `'`. You can also use more complicated SQL queries if you wanted to.


```python
!ogrinfo -nomd -geom=NO -where "FIPS='UK'"  data/TM_WORLD_BORDERS-0.3.shp TM_WORLD_BORDERS-0.3 
```

    INFO: Open of `data/TM_WORLD_BORDERS-0.3.shp'
          using driver `ESRI Shapefile' successful.
    
    Layer name: TM_WORLD_BORDERS-0.3
    Geometry: Polygon
    Feature Count: 1
    Extent: (-180.000000, -90.000000) - (180.000000, 83.623596)
    Layer SRS WKT:
    GEOGCRS["WGS 84",
        DATUM["World Geodetic System 1984",
            ELLIPSOID["WGS 84",6378137,298.257223563,
                LENGTHUNIT["metre",1]]],
        PRIMEM["Greenwich",0,
            ANGLEUNIT["degree",0.0174532925199433]],
        CS[ellipsoidal,2],
            AXIS["latitude",north,
                ORDER[1],
                ANGLEUNIT["degree",0.0174532925199433]],
            AXIS["longitude",east,
                ORDER[2],
                ANGLEUNIT["degree",0.0174532925199433]],
        ID["EPSG",4326]]
    Data axis to CRS axis mapping: 2,1
    FIPS: String (2.0)
    ISO2: String (2.0)
    ISO3: String (3.0)
    UN: Integer (3.0)
    NAME: String (50.0)
    AREA: Integer (7.0)
    POP2005: Integer64 (10.0)
    REGION: Integer (3.0)
    SUBREGION: Integer (3.0)
    LON: Real (8.3)
    LAT: Real (7.3)
    OGRFeature(TM_WORLD_BORDERS-0.3):206
      FIPS (String) = UK
      ISO2 (String) = GB
      ISO3 (String) = GBR
      UN (Integer) = 826
      NAME (String) = United Kingdom
      AREA (Integer) = 24193
      POP2005 (Integer64) = 60244834
      REGION (Integer) = 150
      SUBREGION (Integer) = 154
      LON (Real) = -1.600
      LAT (Real) = 53.000
    


We inmediately see that the coordinates for the UK are in several polygons, and in WGS84 (Latitude and Longitude in decimal degrees). This is incompatible with the MODIS data (SIN projection), but fortunately GDAL understands about coordinate systems.

We can use GDAL to quickly apply the vector feature for the UK as a mask. There are several ways of doing this, but the simplest is to use [gdal.Warp](https://www.gdal.org/gdalwarp.html) (the link is to the command line tool). In this case, we just want to create:

* an in-memory (i.e. not saved to a file) dataset. We can use the format `MEM`, so no file is written out.
* where the `FIPS` field is equal to `'UK'`, we want the LAI to show, elsewhere, we set it to some value to indicate "no data" (e.g. -999)

The mosaicked version of the MODIS LAI product is in called `stitch_up.vrt`. Since we're not saving the output to a file (`MEM` output option), we can leave the output as an empty string `""`. The shapefile comes with the `cutline` options:

* `cutlineDSName` that's the name of the vector file we want to use as a cutline
* `cutlineWhere` that's the selection statement for the attribute table in the dataset. 

To set the no data value to 200, we can use the option `dstNodata=200`. This is because very large values in the LAI product are already indicated to be invalid.

We can then just very quickly perform this and check...


```python
import gdal
import matplotlib.pylab as plt
from pathlib import Path

filenames = sorted([p.as_posix() for p in Path('data').glob('*2018*v0*.hdf')])
datanames = [f'HDF4_EOS:EOS_GRID:"{str(filename)}":MOD_Grid_MCD15A3H:Lai_500m' \
                for filename in filenames]
stitch_vrt = gdal.BuildVRT("stitch_up.vrt", datanames)


g = gdal.Warp("", "stitch_up.vrt",
         format = 'MEM',dstNodata=200,
          cutlineDSName = 'data/TM_WORLD_BORDERS-0.3.shp', cutlineWhere = "FIPS='UK'")

# read and plot data
masked_lai = g.ReadAsArray()*0.1
plt.figure(figsize=(10,10))
plt.title('Red white and blue: Brexit UK')
plt.imshow(masked_lai, interpolation="nearest", vmin=1, vmax=3, 
          cmap=plt.cm.RdBu)
```




    <matplotlib.image.AxesImage at 0x7fe641ad4ad0>




![png](034_GDAL_masking_files/034_GDAL_masking_53_1.png)


So that works as expected, but since we haven't actually told GDAL anything about the output (other than apply the mask), we still have a 4800 pixel wide dataset. 

You may want to crop it by looking for where the original dataset is  valid (0 to 100 here). This will generally save a lot of computer memory. You'll be pleased to know that this is a great slicing application!


```python
import numpy as np

lai = g.ReadAsArray()

# data valid where lai <= 100 here
valid_mask = np.where(lai <= 100)

# work out the bounds of valid_mask
min_y      = valid_mask[0].min()
max_y      = valid_mask[0].max() + 1

min_x      = valid_mask[1].min()
max_x      = valid_mask[1].max() + 1

# now slice, and scale LAI
lai = lai[min_y:max_y,
          min_x:max_x]*0.1

plt.figure(figsize=(10,10))
plt.imshow(lai, vmin=0, vmax=6,
           cmap=plt.cm.inferno_r)
plt.title('UK')
plt.colorbar()

```




    <matplotlib.colorbar.Colorbar at 0x7fe660f77a10>




![png](034_GDAL_masking_files/034_GDAL_masking_55_1.png)


**Exercise 3.3.7** **Homework**

* Develop a function that takes the list of dataset names and the information you passed to `gdal.Warp` (or a subset of this) and returns a cropped image of valid data.
* Use this function to show separate images of: France, Belgium, the Netherlands


```python
# do exercise here
```

**Exercise 3.3.8** **Homework**

* Download data for these same four tiles from the **MODIS snow cover** dataset for some particular date (in winter). Check the related quicklooks to see that the dataset isn't all covered in cloud.
* show the snow cover for one or more selected countries.
* calculate summary statistics for the datasets.

**Hint** the codes would be very similar to above, but watch out for the scaling factor not being the same (no scaling for the snow cover!). Also, watch out for the dataset being on a different NASA server to the LAI data (as in exercise above).

When you calculate summary statistics, make sure you ignore all invalid pixels. You could do that by generating a mask of the dataset (after you have clipped it) using `np.where()`, and only process those pixels, e.g.:

    image[np.where(image<=100)].mean()
    
rather than

    image.mean()
    
as the latter would include invalid pixels.


```python
# do exercise here
```
