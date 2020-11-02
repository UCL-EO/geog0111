# 022 Read and Write: URLs and files : Answers to exercises

#### Exercise 1

* Using `Path.read_text()` read the text from the file `work/easy.txt` and print the text returned.
* split the text into lines of text using `str.split()` at each newline, and print out the resulting list

You learned how to split strings in [013_Python_string_methods](013_Python_string_methods.md#split()-and-join())


```python
# ANSWER
# Using `Path.read_text()` read the text from the 
# file `work/easy.txt` and print the text returned.

text = Path('work/easy.txt').read_text()
print(f'I have read:\n{text}')

# split the text into lines of text using `str.split()` 
# at each newline, and print out the resulting list
text_list = text.split('\n')
print(f'lines list:\n{text_list}')
```

    I have read:
    
    It is easy for humans to read and write.
    It is easy for machines to parse and generate. 
    
    lines list:
    ['', 'It is easy for humans to read and write.', 'It is easy for machines to parse and generate. ', '']


#### Exercise 2

Using the code:

    kwargs = {
        'product'    : 'MCD15A3H',
        'db_dir'     : 'work',
        'local_dir'  : 'work',
    }

    modis = Modis(**kwargs)
    # get URLs
    hdf_urls = modis.get_url(year="2020",month="01",day="01")

* write a function called `get_locals` that loops over each entry in the list `hdf_urls` and returns the local filename 
* write code to test the function and print results using data from `modis.get_url("2020","01","*")`


```python
from geog0111.gurlpath import URL

# BETTER ANSWER
# write a function called `get_locals` that loops 
# over each entry in the list `hdf_urls` and returns the local filename 
def get_locals(hdf_urls):
    '''
    get the cached filenames for the URL list
    '''
    return [f.local() for f in hdf_urls]
```


```python
# write code to test the function and print results 
# using data from modis.get_url("2020","01","*")
kwargs = {
    'product'    : 'MCD15A3H',
    'db_dir'     : 'work',
    'local_dir'  : 'work',
}
modis = Modis(**kwargs)
# get URLs
hdf_urls = modis.get_url(year="2020",month="01",day="*")
# test
print(get_locals(hdf_urls))
```

    [PosixPath('/Users/plewis/Documents/GitHub/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.01/MCD15A3H.A2020001.h08v06.006.2020006032951.hdf.store'), PosixPath('/Users/plewis/Documents/GitHub/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.05/MCD15A3H.A2020005.h08v06.006.2020010210940.hdf.store'), PosixPath('/Users/plewis/Documents/GitHub/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.09/MCD15A3H.A2020009.h08v06.006.2020014204616.hdf.store'), PosixPath('/Users/plewis/Documents/GitHub/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.13/MCD15A3H.A2020013.h08v06.006.2020018030252.hdf.store'), PosixPath('/Users/plewis/Documents/GitHub/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.17/MCD15A3H.A2020017.h08v06.006.2020022034013.hdf.store'), PosixPath('/Users/plewis/Documents/GitHub/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.21/MCD15A3H.A2020021.h08v06.006.2020026032135.hdf.store'), PosixPath('/Users/plewis/Documents/GitHub/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.25/MCD15A3H.A2020025.h08v06.006.2020030025757.hdf.store'), PosixPath('/Users/plewis/Documents/GitHub/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.006/2020.01.29/MCD15A3H.A2020029.h08v06.006.2020034165001.hdf.store')]


#### Exercise 3

    name = '[2400x2400] Fpar_500m MOD_Grid_MCD15A3H (8-bit unsigned integer)'

* Take the string variable `name` above, split it to obtain the second field (`Fpar_500m` here) and store this in a variable `sds_name`
* Write a function called `get_data` that reads an HDF (MODIS) filename, and returns a dictionary of all of the sub-datasets in the file, using `ReadAsArray()`. The dictionary keys should correspond to the items in  `sds_name` above.
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
# Write a function called get_data that reads an HDF (MODIS) filename, 
# and returns a dictionary of all of the data in the file,
# using ReadAsArray(). 
# The dictionary keys should correspond to the items in sds_name above.

def get_data(hdf_filename):
    '''
    reads an HDF (MODIS) filename 
    and return a dictionary of all of the sub-datasets in the file,
    '''
    # open file
    g = gdal.Open(hdf_filename)
    # initialise dictionary
    odict = {}
    # return empty-handed
    if g == None:
        return odict
    for filename,name in g.GetSubDatasets():
        sds_name = name.split()[1]
        data = gdal.Open(filename).ReadAsArray()
        odict[sds_name] = data
    return odict
```


```python
# test the code by showing the keys in the dictionary 
# returned and the shape of their dataset
import gdal
from  geog0111.modis import Modis

# as before
kwargs = {
    'product'    : 'MCD15A3H',
    'db_dir'     : 'work',
    'local_dir'  : 'work',
}
modis = Modis(**kwargs)
url = modis.get_url(year="2020",month="01",day="01")[0]

hdf_filename = str(url.local())

# test the code
hdf_dict = get_data(hdf_filename)

# loop over dictionary items
for k,v in hdf_dict.items():
    # do some neat formatting on k
    print(f'{k:<20s}: {v.shape}')
```

    Fpar_500m           : (2400, 2400)
    Lai_500m            : (2400, 2400)
    FparLai_QC          : (2400, 2400)
    FparExtra_QC        : (2400, 2400)
    FparStdDev_500m     : (2400, 2400)
    LaiStdDev_500m      : (2400, 2400)

