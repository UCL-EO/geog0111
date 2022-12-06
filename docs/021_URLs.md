# 021 URLs


## Introduction



### Purpose

In this session, we will learn about files and similar resources. We will introduce the standard Python library [`pathlib`](https://docs.python.org/3/library/pathlib.html) which is how we deal with file paths. For URLs, we will use the Python packages: [urlpath](https://github.com/chrono-meter/urlpath).

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

You will need a detailed understanding and familiarity with the `Path` package for dealing with files, as well asd the underlying concepts covered there.

* [020_Python_files](020_Python_files.md)

### Test

In any public information (like these notebooks) we do not want to expose sensitive information such as usernames and passwords.

So here we will make use of stored passwords and usernames using the local [cylog](geog0111/cylog.py) package that was covered in [004_Accounts](004_Accounts.md). 

We will be using the site [`https://e4ftl01.cr.usgs.gov`](https://e4ftl01.cr.usgs.gov) today. You should have already tested that your NASA Earthdata login works for files on that site. 

If you unsure about your login and/or password, test them on [the Earthdata login page](https://urs.earthdata.nasa.gov/home).

We should see that a call to `Cylog(url).login()` returns the username and password.

So, if you like, you can check what you have stored in [cylog](geog0111/cylog.py) by using:

    url='https://e4ftl01.cr.usgs.gov'
    print(Cylog(url).login())
    
If you want to check it, run those commands in the cell below (uncomment the print line).


```python
from geog0111.cylog import Cylog
url='https://e4ftl01.cr.usgs.gov'
#print(Cylog(url).login())
```

If you are prompted for a login and password, this means that you haven't previously entered one for this site (just enter them now, or go back and look at [004_Accounts](004_Accounts.md). 

## Resources from a URL

### `urlpath`

The library [`urlpath`](https://github.com/chrono-meter/urlpath) is designed to operate in a similar manner to `pathlib` for reading data from URLs. It is based on [urllib.parse](https://docs.python.org/3/library/urllib.parse.html) and [requests](https://requests.readthedocs.io/en/master/). It doesn't quite have all of the functionality we will need, but it goes a long way to an object-oriented URL library that is similar to Pathlib. 

The object in `urlpath` corresponding to `Path` is `URL`.

A text file example:


```python
from urlpath import URL
site = 'https://www.metoffice.gov.uk/'
site_dir = 'hadobs/hadukp/data/monthly'
site_file = 'HadSEEP_monthly_totals.txt'
 
url = URL(site,site_dir,site_file)
print(f'remote file {url}')
```

    remote file https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_totals.txt


A binary file example:


```python
from urlpath import URL

site = 'https://e4ftl01.cr.usgs.gov'
site_dir = 'MOTA/MCD15A3H.006/2020.01.01'
site_file = 'MCD15A3H.A2020001.h08v06.006.2020006032951.hdf'

url = URL(site,site_dir,site_file)
print(f'remote file {url}')
```

    remote file https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01/MCD15A3H.A2020001.h08v06.006.2020006032951.hdf


We have similar functionality in `URL` to `Path` for manipulating filenames, but more limited file information:


```python
print(f'URL    : {url}')
print(f'name   : {url.name}')
print(f'parent : {url.parent}')
```

    URL    : https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01/MCD15A3H.A2020001.h08v06.006.2020006032951.hdf
    name   : MCD15A3H.A2020001.h08v06.006.2020006032951.hdf
    parent : https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01


but also some other helpful ones on the URL:


```python
from pathlib import Path

print(f'anchor   : {url.anchor}')
print(f'hostname : {url.hostinfo}')
print(f'scheme   : {url.scheme}')
print(f'name     : {url.name}')
print(f'netloc   : {url.netloc}')
print(f'parts    : {url.parent.parts}') # parent parts
```

    anchor   : https://e4ftl01.cr.usgs.gov
    hostname : e4ftl01.cr.usgs.gov
    scheme   : https
    name     : MCD15A3H.A2020001.h08v06.006.2020006032951.hdf
    netloc   : e4ftl01.cr.usgs.gov
    parts    : ('https://e4ftl01.cr.usgs.gov', 'MOTA', 'MCD15A3H.006', '2020.01.01')


#### Exercise 1

* create a `URL` object for the file `table.html` in the directory `psd/enso/mei/` on the site `http://www.esrl.noaa.gov/`.
* print out the url name and check it is `table.html`

For accessing URLs, will mostly make use of the following functions in `URL` that you will see are very similar to those for `Path`:


|function| purpose|
|---|---|
|`URL.name`|  filename |
|`URL.parent`|  parent |
|`URL.parts`|  parts |
| `URL.as_posix()` | return URL as posix string |
|`URL.with_userinfo()`|  add in username and password |
|`URL.get()`|  URL get. Returns `requests.models.Response`|
| `URL.netloc` | network location e.g. `www.google.com`|
| `URL.path` | full pathname on server (including filename)|

#### `URL.get()`

We can use `URL.get()` to access data. This returns a response (more formally, a type [`requests.models.Response`](https://docs.python-requests.org/en/latest/)):

    r = URL.get()

`requests.models.Response` information table:

|function| purpose|
|---|---|
| `r.status_code` | return code after request. You need to check this in case the call fails. It should be `200` if ok.|
| `r.text` | text content returned |
| `r.json` | text content interpreted as json |
| `r.content` | binary content returned |

If the access has been successful, then `r.status_code` should return `200` (or `requests.codes.ok`). If it is `401` then there has been an access error. You can find the fuller list of possible [http status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) on the web. 

If the data type to be accessed is raw (ASCII) text, then you can access the data with `r.text`. [Similarly](https://docs.python-requests.org/en/latest/), if it is [json](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON), `r.json`, or binary `r.content`



```python
from urlpath import URL

site = 'https://covid.ourworldindata.org'
site_dir = 'data/archived/ecdc'
site_file = 'full_data.csv'
site_file = 'locations.csv'

url = URL(site,site_dir,site_file)
r = url.get()

# check error code: 200 is good
# 
if r.status_code == 200:
    print(f'data access good for {url.as_posix()}')
    
    # get data as text
    data = r.text
    # print first 500 characters
    print('\n==== data as text ====')
    print(data[:500])
    
    # get data as binary
    data = r.content
    # print first 500 characters
    print('\n==== data as binary ====')
    print(data[:500])
```

    data access good for https://covid.ourworldindata.org/data/archived/ecdc/locations.csv
    
    ==== data as text ====
    countriesAndTerritories,location,continent,population_year,population
    Afghanistan,Afghanistan,Asia,2020,38928341
    Albania,Albania,Europe,2020,2877800
    Algeria,Algeria,Africa,2020,43851043
    Andorra,Andorra,Europe,2020,77265
    Angola,Angola,Africa,2020,32866268
    Anguilla,Anguilla,North America,2020,15002
    Antigua_and_Barbuda,Antigua and Barbuda,North America,2020,97928
    Argentina,Argentina,South America,2020,45195777
    Armenia,Armenia,Asia,2020,2963234
    Aruba,Aruba,North America,2020,106766
    Australia,Austral
    
    ==== data as binary ====
    b'countriesAndTerritories,location,continent,population_year,population\nAfghanistan,Afghanistan,Asia,2020,38928341\nAlbania,Albania,Europe,2020,2877800\nAlgeria,Algeria,Africa,2020,43851043\nAndorra,Andorra,Europe,2020,77265\nAngola,Angola,Africa,2020,32866268\nAnguilla,Anguilla,North America,2020,15002\nAntigua_and_Barbuda,Antigua and Barbuda,North America,2020,97928\nArgentina,Argentina,South America,2020,45195777\nArmenia,Armenia,Asia,2020,2963234\nAruba,Aruba,North America,2020,106766\nAustralia,Austral'


#### Exercise 1

* Use the `URL.get()` method to pull data from `https://covid.ourworldindata.org/data/ecdc/archived/full_data.csv` and store in a file called `work/full_data.csv`.
* check the file size
* show the first few lines of data

## MODIS data|

#### Getting a MODIS product URL

If we need to add a username and password to access a URL, we can add this to the URL object with `URL.with_userinfo(USERNAME,PASSWORD)`. We will demonstrate this with accessing data from NASA servers.

One of the deepest sources of geospatial information over the last two decades is that obtained from the NASA [MODIS](https://modis.gsfc.nasa.gov/data/dataprod/) products. We will make use of various MODIS datasets in this course. We can access these via a URL.

The encoding for this is not very complex, but is a bit beyond what we have time to go through at this stage of the course. For that reason, we will be using the local utility [`geog0111.modisUtils.modisURL`](geog0111/modisUtils.py) to access MODIS URLs. Further, accessing the URLs for these data needs a data file to vbe downloaded from the web. This can take some time, so in this code, we provide a cache of files that we have already downloaded. If you access a data product/date for the first time, it will take a minute to access the information. The next time you access, it will be immediate as you will use the cached version. See the help information for more details.

We use the example of the product [`MCD15A3H`](https://lpdaac.usgs.gov/products/mcd15a3hv006/) below. This is the MODIS 4-day Leaf Area Index product.


```python
from geog0111.modisUtils import modisURL

# uncomment this to look at the help for this function
#help(modisURL)
```


```python
from geog0111.modisUtils import modisURL

# set up control for which MODIS product/date/tile

modinfo = {  
    'product'  : 'MCD15A3H',
    'year'     : 2020,
    'month'    : 1,
    'day'      : 5,
    'tile'     : 'h08v06'
}

url = modisURL(**modinfo,verbose=False)
print(f'-> {url}')
```

    -> https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf


#### Pulling MODIS data with password 

We add the username and password with `URL.with_userinfo(USERNAME,PASSWORD)`.

Rather than type this information in here or expose it in stored notebooks, we retrieve it using Cylog: 


```python
from geog0111.modisUtils import modisURL
from geog0111.cylog import Cylog
from urlpath import URL
from pathlib import Path

# set up control for which MODIS product/date/tile

modinfo = {  
    'product'  : 'MCD15A3H',
    'year'     : 2020,
    'month'    : 1,
    'day'      : 1,
    'tile'     : 'h08v06'
}

url = modisURL(**modinfo,verbose=False)
if (url):
    print(f'anchor: {url.anchor}')
    print(f'-> {url}')

    # use url.anchor to get server name for Cylog
    # add the username and password
    username,password = Cylog(url.anchor).login()
    url = url.with_userinfo(username,password)

    # uncomment this line to see how username and password are inserted
    #print(f'-> {url}')
else:
    print(f'error with data request')
```

    anchor: https://e4ftl01.cr.usgs.gov
    -> https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01/MCD15A3H.A2020001.h08v06.006.2020006032951.hdf


Because of the NASA login, we need to make two calls to the server. The first will get a new URL with encoded authentification information. 

`url.get()` returns an object of type `requests.models.Response`. The new URL will be `r.url`, so we take that and add the username and password to it again.


```python
# first call to URL to get auth
r = url.get()
url2 = URL(r.url).with_userinfo(username,password)

```

Now we can make a call to this with `get()` to retrieve the data from the URL. We need to check that the `status_code` returned is 200 to see if the call worked:


```python
r2 = url2.get()
print(f'response: {r2.status_code}')
```

    response: 200


If the response is *not* `200`, then you have a problem of some sort. This could be that you don't have a correct password stored via `cylog`. If you suspect that might be the case, **go back and check the test on [`004_Accounts.md`](004_Accounts.md)**. If it is *Wednesday afternoon*, it is probably just that the NASA servers are down for maintenance. 

If its ok (`200`), we can get the binary data as `r2.content` and use `Path().write_bytes()` to write this to a file:


```python
if r2.status_code == 200:
    
    # setup Path object for output file
    filename = Path('work',url.name)
    
    # write binary data
    filename.write_bytes(r2.content)
    
    # check size:
    size_MB = filename.stat().st_size/(1024**2)
    
    # report
    print(f'file {filename} written: {size_MB :.1f} MB')
else:
    print(f'{url} status code {r2.status_code}')
```

    file work/MCD15A3H.A2020001.h08v06.006.2020006032951.hdf written: 8.6 MB


Occasionally, you will find that the calls to get data from the server will not work, and may produce 401 errors. 

This is typically because:
* it is Wednesday, when the servers are down for maintenance
* the load is too high on the servers, in which case, wait a minute and try again or set the timeout option `URL.get(timeout=200)`.

#### Exercise 2

* pull the MODIS dataset `MCD15A3H` for 9 January 2019 for tile `h08v06` and confirm that the dataset size is 8.5 MB


#### Easier MODIS file access

In fact, we have a related MODIS utility `modisFile` that does all of this for you, and uses the cache to store files we have previously downloaded. You will generally be using that then, but you should know how to get the binary data from the URL directly as above to be a competent programmer.


```python
from geog0111.modisUtils import modisFile

# set up control for which MODIS product/date/tile

modinfo = {  
    'product'  : 'MCD15A3H',
    'year'     : 2020,
    'month'    : 1,
    'day'      : 5,
    'tile'     : 'h08v06'
}

filename = modisFile(**modinfo,verbose=False)

if filename:
    size_MB = filename.stat().st_size/(1024**2)
    
    # report
    print(f'file {filename} is: {size_MB :.1f} MB')
```

    file /Users/plewis/Documents/GitHub/geog0111/notebooks/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf is: 8.9 MB


#### Exercise 3

* pull the MODIS dataset `MCD15A3H` for 13 January 2019 for tile `h08v06` using `modisFile` and confirm that the dataset size is 8.5 MB

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
from osgeo import gdal
from geog0111.modisUtils import modisFile
# settings

modinfo = {  
    'product'  : 'MCD15A3H',
    'year'     : 2019,
    'month'    : 2,
    'day'      : 10,
    'tile'     : 'h08v06'
}

filename = modisFile(**modinfo,verbose=False)

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


#### Exercise 4

    name = '[2400x2400] Fpar_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)'

* Take the string variable `name` above, split it to obtain the second field (`Fpar_500m` here) and store this in a variable `sds_name`
* Write a function called `getModisTiledata` that reads an HDF (MODIS) filename, and returns a dictionary of all of the sub-datasets in the file, using `ReadAsArray()`. The dictionary keys should correspond to the items in  `sds_name` above.
* test the code by showing the keys in the dictionary returned and the shape of their dataset

You will need to recall how to split a string, that was covered in [013 Python string methods](013_Python_string_methods.md#split()-and-join()). You will also need to recall how to [loop over a dictionary](016_Python_for.md#looping-over-dictionaries,-and-assert). We saw how to find the shape of the dataset returned above (`.shape`).

## Summary


In this section, we have considered URLs in some detail in the same way as we did filenames, and made use of functions from [urlpath](https://github.com/chrono-meter/urlpath) to access them. 

|function| purpose|
|---|---|
|`URL.name`|  filename |
|`URL.parent`|  parent |
|`URL.parts`|  parts |
| `URL.as_posix()` | return URL as posix string |
|`URL.with_userinfo()`|  add in username and password |
|`URL.get()`|  URL get. Returns `requests.models.Response`|
| `URL.netloc` | network location e.g. `www.google.com`|
| `URL.path` | full pathname on server (including filename)|

We have seen how to access and download both text and binary files from the web using `URL.get()`. We have seen how to add username and password information to this, and have used that to access MODIS binary datasets. We know how to save the files that we download.

We have seen a simple MODIS file library to make downloading datasets easier. This includes caching of datasets that otherwise can take a long time to download. It also allows for sharing of downloaded datasets through a system-wide cache. 

There will be times when a call to a URL doesn't return as expected. There can be several reasons for this, so you should check that you have formed the URL correctly and that the data you expect to download exists. 


Functions in `modisUtils`:

|function| purpose|
|---|---|
|`modisFile`| get a Path object for a file of the requested MODIS dataset, either from cache, or by downloading |
|`modisURL`| get the URL of a MODIS dataset, possibly using a cache for the filename |

Even then, there can be times when the server load or network traffic mean that your request times out. In such cases, you should try again a short while afterwards, and consider setting a timeout on the `URL.get()` call. In any case, this point illustrates the need for comprehensive error checking: you cannot just assume that you download of data has worked, you must check it. This should also apply when you are using any files: check that any file you want to read exists and perhaps see if it is non-zero sized. You can trap errors, but it is best to try foresee them.

We have learned a little of how to use `gdal` to look at the sub-datasets in an HDF file and also how to read them.


`gdal`

| Command | Comment |
|---|---|
|`g = gdal.Open(filename)` | Open geospatial file `filename` and return `gdal` object `g` (`None` if file not opened correctly)|
|`g.GetSubDatasets()` | Get list of sub-datasets from `gdal` object `g`| 
|`g.ReadAsArray()` | Read dataset from `gdal` object `g` into array |

You should now have some confidence in these matters, so that if you were set a task of downloading and saving datasets, as well as other tasks such as finding their size, whether the exists or not, you could do this. 


