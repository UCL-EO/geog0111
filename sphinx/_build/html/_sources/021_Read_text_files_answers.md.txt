# 021 Read and Write: Streams : Answers to exercises

#### Exercise 1

* write code to read from the json-format file `bin/copy/environment.json` into a dictionary called `json_data`.
* print out the dictionary keys.
* print the file size of the json-format file in KB to two decimal places.


```python
# ANSWER
# write code to read from the json-format file 
# bin/copy/environment.json 
# into a dictionary called json_data.
json_file = Path('bin/copy/environment.json')

# use with ... as ... as we have been shown
with json_file.open('r') as f:
    json_data = json.load(f)
    
# print out the dictionary keys.
print(json_data.keys())

# print the file size of the 
# json-format file in KB to two decimal places.
print(f'file {json_file} size {json_file.stat().st_size / 1024 : .2f}')
```

    dict_keys(['name', 'channels', 'dependencies'])
    file bin/copy/environment.json size  0.78


#### Exercise 2

The file [2276931.csv](https://raw.githubusercontent.com/UCL-EO/geog0111/master/data/2276931.csv) contains precipitation data for an [NOAA weather station](https://www.ncdc.noaa.gov/cdo-web/datasets#GSOY) `HAVANA 4.2 SW, FL US` for the year 2020 to date.

The dataset URL is:

https://raw.githubusercontent.com/UCL-EO/geog0111/master/data/2276931.csv

* Inspect the file to discover any issues you must account for.
* Read the file into `pandas` using `url.open('r')`.
* print the first 5 lines of data


```python
# ANSWER
msg = '''
Inspect the file to discover any issues you must account for.

The file is straightforward CVS format, with the first column
the data column titles
'''
print(msg)

import pandas as pd
from geog0111.gurlpath import URL

site = 'https://raw.githubusercontent.com'
site_dir = '/UCL-EO/geog0111/master/data'
site_file = '2276931.csv'

# form the URL
url = URL(site,site_dir,site_file)

# Read the file into pandas using url.open('r').
df=pd.read_csv(url.open('r'))

# print the first 5 lines of data
df.head(5)
```

    
    Inspect the file to discover any issues you must account for.
    
    The file is straightforward CVS format, with the first column
    the data column titles
    





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>STATION</th>
      <th>NAME</th>
      <th>DATE</th>
      <th>PRCP</th>
      <th>SNOW</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-01-01</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-01-02</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-01-03</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-01-04</td>
      <td>0.98</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-01-05</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ANSWER 

# print out the absolute pathname of the 
# directory that images/ucl.png is in
abs_name = Path('images/ucl.png').absolute()
print(abs_name)

# we want the parent!
print(f'the file {abs_name.name} is in {abs_name.parent}')

# print the size of the file in bytes without reading the datafile. 
print(f'{abs_name.name} has size {abs_name.stat().st_size} bytes')

# 1 KB is 1024 Bytes
# .2f is 2 d.p. format
print(f'{abs_name.name} has size ' +\
      f'{abs_name.stat().st_size/1024:.2f} KB')

# read the datafile, and check you get the same data size
dataset = abs_name.read_bytes()
# size
s = len(dataset)
print(f'the size of data read is {s} bytes -> {s/1024 : .2f} KB')
```

    /Users/plewis/Documents/GitHub/geog0111/notebooks/images/ucl.png
    the file ucl.png is in /Users/plewis/Documents/GitHub/geog0111/notebooks/images
    ucl.png has size 1956 bytes
    ucl.png has size 1.91 KB
    the size of data read is 1956 bytes ->  1.91 KB

