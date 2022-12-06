# 021 URLs : Answers to exercises

#### Exercise 1

* create a `URL` object for the file `table.html` in the directory `psd/enso/mei/` on the site `http://www.esrl.noaa.gov/`.
* print out the url name and check it is `table.html`


```python
# ANSWER

# create a URL object for the file table.html 
# in the directory psd/enso/mei/ on the site 
# http://www.esrl.noaa.gov/.

site = 'http://www.esrl.noaa.gov/'
site_dir = 'psd/enso/mei'
site_file = 'table.html'
url = URL(site,site_dir,site_file)

# print out the url and check it is table.html
print(url)
assert url.name == site_file
print('passed')
```

    http://www.esrl.noaa.gov/psd/enso/mei/table.html
    passed


#### Exercise 1

* Use the `URL.get()` method to pull data from `https://covid.ourworldindata.org/data/ecdc/archived/full_data.csv` and store in a file called `work/full_data.csv`.
* check the file size
* show the first few lines of data


```python
from pathlib import Path
from urlpath import URL
# ANSWER

# Use the URL.get() method to pull data from 
# https://covid.ourworldindata.org/data/ecdc/full_data.csv 
# and store in a file called work/full_data.csv

# set up URL object
url = URL('https://covid.ourworldindata.org/data/archived/ecdc/full_data.csv')
# set up file for data as Path
ofile = Path('work',url.name)

# get data 
r = url.get()
# check response:
if r.status_code == 200:
    # ok
    data = r.text
    # remember how to write to a file from 
    # previous session on Path
    ofile.write_text(data)
    # check the file size
    print(f'{ofile} size: {ofile.stat().st_size} bytes')
    # show the first few lines of data
    # NB data is a big long string, so split it on \n
    # into lines
    data_lines = data.split('\n')
    for i in range(5):
        print(f'{i}: {data_lines[i]}')
else:
    print(f'failed to pull data from {url}')
```

    work/full_data.csv size: 3215657 bytes
    0: date,location,new_cases,new_deaths,total_cases,total_deaths,weekly_cases,weekly_deaths,biweekly_cases,biweekly_deaths
    1: 2019-12-31,Afghanistan,0,0,,,,,,
    2: 2020-01-01,Afghanistan,0,0,,,,,,
    3: 2020-01-02,Afghanistan,0,0,,,,,,
    4: 2020-01-03,Afghanistan,0,0,,,,,,


#### Exercise 2

* pull the MODIS dataset `MCD15A3H` for 9 January 2019 for tile `h08v06` and confirm that the dataset size is 8.5 MB



```python
from geog0111.modisUtils import modisURL
from geog0111.cylog import Cylog
from urlpath import URL
from pathlib import Path
# ANSWER

# set up control for which MODIS product/date/tile

modinfo = {  
    'product'  : 'MCD15A3H',
    'year'     : 2020,
    'month'    : 1,
    'day'      : 9,
    'tile'     : 'h08v06'
}

# get the URL
url = modisURL(**modinfo,verbose=False)
if url:
    print(f'anchor: {url.anchor}')
    print(f'-> {url}')

    # use url.anchor to get server name for Cylog
    # add the username and password
    print('getting MODIS URL')
    username,password = Cylog(url.anchor).login()
    url = url.with_userinfo(username,password)
    # dont print out the username and password!
    print('/'.join(url.parts[1:]))

    # first call to URL to get auth
    print('getting Auth')
    r = url.get()
    url2 = URL(r.url).with_userinfo(username,password)

    if url2:
    # net call to get data
        r2 = url2.get()
        print(f'response: {r2.status_code}')

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
            print(f'{"/".join(url.parts[1:])} status code {r2.status_code}')
    else:
        print('error getting url')
else:
    print('error in data request')
```

    anchor: https://e4ftl01.cr.usgs.gov
    -> https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.09/MCD15A3H.A2020009.h08v06.006.2020014204616.hdf
    getting MODIS URL
    MOTA/MCD15A3H.006/2020.01.09/MCD15A3H.A2020009.h08v06.006.2020014204616.hdf
    getting Auth
    response: 200
    file work/MCD15A3H.A2020009.h08v06.006.2020014204616.hdf written: 8.5 MB


#### Exercise 3

* pull the MODIS dataset `MCD15A3H` for 13 January 2019 for tile `h08v06` using `modisFile` and confirm that the dataset size is 8.5 MB


```python
from geog0111.modisUtils import modisFile

# set up control for which MODIS product/date/tile

modinfo = {  
    'product'  : 'MCD15A3H',
    'year'     : 2020,
    'month'    : 1,
    'day'      : 13,
    'tile'     : 'h08v06'
}

filename = modisFile(**modinfo,verbose=False)

if filename:
    size_MB = filename.stat().st_size/(1024**2)
    
    # report
    print(f'file {filename} is: {size_MB :.1f} MB')
```

    file /Users/plewis/Documents/GitHub/geog0111/notebooks/.modis_cache/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.13/MCD15A3H.A2020013.h08v06.006.2020018030252.hdf is: 8.4 MB


#### Exercise 4

    name = '[2400x2400] Fpar_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)'

* Take the string variable `name` above, split it to obtain the second field (`Fpar_500m` here) and store this in a variable `sds_name`
* Write a function called `getModisTiledata` that reads an HDF (MODIS) filename, and returns a dictionary of all of the sub-datasets in the file, using `ReadAsArray()`. The dictionary keys should correspond to the items in  `sds_name` above.
* test the code by showing the keys in the dictionary returned and the shape of their dataset

You will need to recall how to split a string, that was covered in [013 Python string methods](013_Python_string_methods.md#split()-and-join()). You will also need to recall how to [loop over a dictionary](016_Python_for.md#looping-over-dictionaries,-and-assert). We saw how to find the shape of the dataset returned above (`.shape`).


```python
# ANSWER 
name = '[2400x2400] Fpar_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)'

# Take the string variable name above, split it to obtain the 
# second field (Fpar_500m here) and store this in a variable sds_name

# use str.split() and take item 1 from the list
sds_name = name.split()[1]
print(sds_name)
```

    Fpar_500m



```python
# ANSWER 
from osgeo import gdal
from geog0111.modisUtils import modisFile

# set up control for which MODIS product/date/tile

modinfo = {  
    'product'  : 'MCD15A3H',
    'year'     : 2020,
    'month'    : 1,
    'day'      : 13,
    'tile'     : 'h08v06'
}


def getModisTiledata(**modinfo):
    '''
    get MODIS data dictionary
    '''
    # set up blank dictionary for output
    odata = {}
    filename = modisFile(**modinfo)
    # error checking
    if not filename:
        return odata
    g = gdal.Open(filename.as_posix())
    if g:
        for filename,name in g.GetSubDatasets():
            # get the SDS
            #print(f'dataset info is: {name}')
            # read the dataset
            gsub = gdal.Open(filename)
            if gsub:
                data = gsub.ReadAsArray()
                sds_name = name.split()[1]
                # load into dictionary
                odata[sds_name] = data
    return odata
    
data = getModisTiledata(**modinfo)
print(*data.keys())
```

    Fpar_500m Lai_500m FparLai_QC FparExtra_QC FparStdDev_500m LaiStdDev_500m

