# 021 Streams : Answers to exercises

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

The file [2276931.csv](https://raw.githubusercontent.com/UCL-EO/geog0111/master/notebooks/data/2276931.csv) contains precipitation data for an [NOAA weather station](https://www.ncdc.noaa.gov/cdo-web/datasets#GSOY) `HAVANA 4.2 SW, FL US` for the year 2020 to date.

The dataset URL is:

https://raw.githubusercontent.com/UCL-EO/geog0111/master/notebooks/data/2276931.csv

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
site_dir = '/UCL-EO/geog0111/master/notebooks/data'
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



#### Exercise 3

Read and print the data in the file '`work/dataset.csv`


```python
# ANSWER
df1=pd.read_csv(Path('work/dataset.csv'))
df1.head()
```




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
      <th>x data</th>
      <th>y data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>


