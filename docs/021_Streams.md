# 021 Streams


## Introduction


### Purpose

In this session, we will learn how to read files and similar resources. We will mainly use [`pathlib`](https://docs.python.org/3/library/pathlib.html) and the local package [gurlpath](geog0111/gurlpath) derived from [`urlpath`](https://github.com/chrono-meter/urlpath). We will also cover opening and closing files, and some simple read- and write-operations.


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

You will need to recall details from [020_Python_files](020_Python_files.md) on using the two packages.


## Reading and writing

We can conveniently use `pathlib` to deal with file input and output. The main methods to be aware of are:


|command|  purpose|
|---|---|
|`Path.open()`| open a file and return a file descriptor|
|`Path.read_text()`|  read text|
|`Path.write_text()`| write text|
|`Path.read_bytes()`| read byte data|
|`Path.write_bytes()`| write byte data|


For `gurlpath` we have the following equivalent functions:





|command|  purpose|
|---|---|
|`URL.open()`| open a file descriptor with data from a URL|
|`URL.read_text()`|  read text from URL|
|`URL.write_text()`| write text to file|
|`URL.read_bytes()`| read byte data from URL|
|`URL.write_bytes()`| write byte data to file|

Notice that the `write` functions (and `open` when used for write) write to local files, not to the URL. 



### caching

The `URL` class is capable of caching information. This means that is you make repeated calls to the same URL, the information is retrieved from a local cache instead of pulling it from the network. This mean, for instance, that we do not need to repeatedly pull large files from the internet. The 'cost' is of course that the amount of local storage increases.

The default cache directory is `~/.url_db`, with the cache database in `~/.url_db/.db.yml`. This can be changed by using the `db_dir=` and `db_file=` keywords when setting up a `URL` object. In case the database gets corrupted, a backup is held in `~/.url_db/.db.yml.bak`.

The cached filename can be accessed as `url.local()`.

There are times you would not want to use caching, for example, if a dataset that you want to look at is regularly updated (e.g. [COVID statistrics](https://covid.ourworldindata.org/data/ecdc/full_data.csv). In that case, use the `noclobber=False` keyword.

Our first example uses `noclobber=False` to ignore any cached versions of the file and force a re-download. Note that we also set `verbose=True` here to give the user feedback on the internal processes:


```python
from geog0111.gurlpath import URL
site = 'https://covid.ourworldindata.org'
site_dir = 'data/ecdc'
site_file = 'full_data.csv'

url = URL(site,site_dir,site_file,verbose=True,noclobber=False)
f = url.open()
print(f'remote file {url}\ncached file {url.local()}')
```

    --> reading data from https://covid.ourworldindata.org/data/ecdc/full_data.csv
    --> open() text stream
    --> trying https://covid.ourworldindata.org/data/ecdc/full_data.csv


    remote file https://covid.ourworldindata.org/data/ecdc/full_data.csv
    cached file /shared/groups/jrole001/geog0111/work/covid.ourworldindata.org/data/ecdc/full_data.csv.store


    --> deleting existing file /shared/groups/jrole001/geog0111/work/covid.ourworldindata.org/data/ecdc/full_data.csv.store


The call to `url.local()` returns `None` here. No cached file is used. If we re-run the code block, then the data is re-downloaded.

We now remove `noclobber=False` (the same as setting the default `noclobber=True`):


```python
from geog0111.gurlpath import URL
site = 'https://covid.ourworldindata.org'
site_dir = 'data/ecdc'
site_file = 'full_data.csv'
site_file = 'locations.csv'

url = URL(site,site_dir,site_file,verbose=True)
data = url.open()
print(f'remote file {url}\ncached file {url.local()}')
```

    remote file https://covid.ourworldindata.org/data/ecdc/locations.csv
    cached file /shared/groups/jrole001/geog0111/work/covid.ourworldindata.org/data/ecdc/locations.csv.store


    --> keeping existing file /shared/groups/jrole001/geog0111/work/covid.ourworldindata.org/data/ecdc/locations.csv.store
    --> keeping existing file /shared/groups/jrole001/geog0111/work/covid.ourworldindata.org/data/ecdc/locations.csv.store


Now, we use the local cached version of the file.

Mostly, you will want to use caching, so just use the default settings for `URL`. But be aware that you can switch it off if you need to.



### `with ... as ...`, `Path.open`, `URL.open`

Sometimes, we pass a filename or URL to some reading routine. But other times, we need to pass a stream. A [stream](https://en.wikipedia.org/wiki/Standard_streams) is a channel through which we may send and/or receive information. This is different to a file, which is where information may reside, but we may for instance open a stream to write to a file. In Python, we call the object that we get when opening a stream a *file object*.

A example of when we would use a stream is for instance when we want to take some information from a URL and pass it directly on to some Python function. A more long-winded way of doing that would be to save the information from the URL into a file on the local file system, then to read from that file into the function. Using a stream, we avoid the need to save a file. 

Of course sometimes, it may be convenient to store a temporary file for such a process, especially if we might want to re-use the file information. This is called building a **cache**. Each time we try to pull data from the original stream then, we would instead read from the local cache. You will notice that web browsers make extensive use of such ideas in trying to speed up the display of web pages: they try only to pull a new version of some data if it has changed.

The `pathlib` function for opening a stream is `Path.open`, with `URL.open` the corresponding function for URLs in our library.

The usual way of opening a file (or URL) to get the file object is:

    with Path(filename).open('r') as f:
       # do some reading with f
       pass
       

We use the form `with ... as ...` here, so that the file object `f` only exists within this construct and the file is automatically closed when we finish. Codes are spaced in inside the construct, as we have seen in `if ...` or `for ... in ...` constructs.

We have set the flag `r` within the `open()` function (this is the default mode). This means that the file will be opened for *reading* only. Alternatives include `w` for writing, or `w+` for appending.


### Using streams with `yaml`, `json`

Two common text formats for certain types of data representation are [json](https://docs.python.org/3/library/json.html) and [`yaml`](http://zetcode.com/python/yaml/). The Python library functions for input and output of both of these use streams: `yaml.safe_load()`, `yaml.safe_dump()`, `json.load()` and `json.dump()` respectively.


```python
import yaml

help(yaml.safe_load)
help(yaml.safe_dump)
```

    Help on function safe_load in module yaml:
    
    safe_load(stream)
        Parse the first YAML document in a stream
        and produce the corresponding Python object.
        
        Resolve only basic YAML tags. This is known
        to be safe for untrusted input.
    
    Help on function safe_dump in module yaml:
    
    safe_dump(data, stream=None, **kwds)
        Serialize a Python object into a YAML stream.
        Produce only basic YAML tags.
        If stream is None, return the produced string instead.
    


In the following example, we use `Path` to open the file [`bin/copy/environment.yml`](bin/copy/environment.yml) and read the open stream using the `yaml.safe_load()` function. 

This file, [`bin/copy/environment.yml`](bin/copy/environment.yml), specifies which packages are loaded in our Python environment. It has a simple ASCII format, but since it is a `yaml` file, we should read it with code that interprets the format correctly and safely into a dictionary. 


```python
from pathlib import Path
import yaml

# form the file name
yaml_file = Path('bin/copy/environment.yml')

# open stream object 'read'
with yaml_file.open('r') as f:
    env = yaml.safe_load(f)

print(f'env is type {type(env)}')
print(f'env keys: {env.keys()}')
```

    env is type <class 'dict'>
    env keys: dict_keys(['name', 'channels', 'dependencies'])


We can access this same file from a URL in the course code repository on GitHub. The  equivalent, reading the data from a URL is:


```python
from geog0111.gurlpath import URL
import yaml

# form the file name
site = 'https://raw.githubusercontent.com'
site_dir = '/UCL-EO/geog0111/master'
site_file = 'copy/environment.yml'
yaml_file = URL(site,site_dir,site_file,verbose=True)

# notice that we can use verbose=True for URL open
with yaml_file.open('r') as f:
    env = yaml.safe_load(f)

print(f'env is type {type(env)}')
print(f'env keys: {env.keys()}')
```

    env is type <class 'dict'>
    env keys: dict_keys(['name', 'channels', 'dependencies'])


    --> keeping existing file /shared/groups/jrole001/geog0111/work/raw.githubusercontent.com/UCL-EO/geog0111/master/copy/environment.yml.store


We can similarly use a stream to write the information in `env` into a `json` format file:


```python
from pathlib import Path
import json

# form the file name
json_file = Path('bin/copy/environment.json')

with json_file.open('w') as f:
    json.dump(env, f)
    
```

#### Exercise 1

* write code to read from the json-format file `bin/copy/environment.json` into a dictionary called `json_data`.
* print out the dictionary keys.
* print the file size of the json-format file in KB to two decimal places.

### Reading data into `pandas`

The Python package `pandas` is widely-used to read and manipulate data in tabular or similar form. One of the most common tabular data formats is [CSV](https://en.wikipedia.org/wiki/Comma-separated_values).

An interesting CSV-format dataset is that containing the [successive pulses](https://gist.githubusercontent.com/borgar/31c1e476b8e92a11d7e9/raw/0fae97dab6830ecee185a63c1cee0008f6778ff6/pulsar.csv) of the oscillation signal coming from the [Pulsar PSR B1919+21](https://www.joydivisionofficial.com/reimagined/) discovered by [Jocelyn Bell](https://en.wikipedia.org/wiki/Jocelyn_Bell_Burnell) in 1967. Some of you might also recognise it from  a [famous album cover](https://en.wikipedia.org/wiki/Unknown_Pleasures)

![Joy Division](images/small_unknown_pleasures.png)

[By inspection](https://raw.githubusercontent.com/igorol/unknown_pleasures_plot/master/pulsar.csv) we can see the data are 80 lines of 300 columns of data. The data format is simple, with no missing values or metadata. We can straightforwardly use the `pandas` function `pd.read_csv`, specifying the URL, to read this dataset (specifying only `header=None` so that the first line is not interpreted as data column names).


```python
import pandas as pd
from geog0111.gurlpath import URL

site = 'https://raw.githubusercontent.com'
site_dir = 'igorol/unknown_pleasures_plot/master'
site_file = 'pulsar.csv'

url = URL(site,site_dir,site_file)

df=pd.read_csv(url,header=None)
df
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>290</th>
      <th>291</th>
      <th>292</th>
      <th>293</th>
      <th>294</th>
      <th>295</th>
      <th>296</th>
      <th>297</th>
      <th>298</th>
      <th>299</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.81</td>
      <td>-0.91</td>
      <td>-1.09</td>
      <td>-1.00</td>
      <td>-0.59</td>
      <td>-0.82</td>
      <td>-0.43</td>
      <td>-0.68</td>
      <td>-0.71</td>
      <td>-0.27</td>
      <td>...</td>
      <td>-0.08</td>
      <td>0.19</td>
      <td>-0.19</td>
      <td>-0.18</td>
      <td>-0.20</td>
      <td>-0.26</td>
      <td>-0.52</td>
      <td>-0.44</td>
      <td>-0.58</td>
      <td>-0.54</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.61</td>
      <td>-0.40</td>
      <td>-0.42</td>
      <td>-0.38</td>
      <td>-0.55</td>
      <td>-0.51</td>
      <td>-0.71</td>
      <td>-0.79</td>
      <td>-0.52</td>
      <td>-0.40</td>
      <td>...</td>
      <td>-0.34</td>
      <td>-0.58</td>
      <td>-0.26</td>
      <td>-0.64</td>
      <td>-1.05</td>
      <td>-0.83</td>
      <td>-0.80</td>
      <td>-0.47</td>
      <td>-0.13</td>
      <td>-0.12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.43</td>
      <td>-1.15</td>
      <td>-1.25</td>
      <td>-1.13</td>
      <td>-0.76</td>
      <td>-0.25</td>
      <td>0.40</td>
      <td>0.26</td>
      <td>0.30</td>
      <td>0.36</td>
      <td>...</td>
      <td>-0.29</td>
      <td>0.16</td>
      <td>0.83</td>
      <td>0.99</td>
      <td>1.28</td>
      <td>0.11</td>
      <td>-0.77</td>
      <td>-0.88</td>
      <td>-0.45</td>
      <td>-1.01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.09</td>
      <td>-0.85</td>
      <td>-0.72</td>
      <td>-0.74</td>
      <td>-0.26</td>
      <td>-0.04</td>
      <td>-0.19</td>
      <td>0.18</td>
      <td>0.03</td>
      <td>0.19</td>
      <td>...</td>
      <td>0.48</td>
      <td>0.52</td>
      <td>-0.14</td>
      <td>-1.13</td>
      <td>-1.07</td>
      <td>-1.03</td>
      <td>-0.78</td>
      <td>-0.40</td>
      <td>0.18</td>
      <td>0.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.13</td>
      <td>-0.98</td>
      <td>-0.93</td>
      <td>-0.90</td>
      <td>-1.14</td>
      <td>-1.00</td>
      <td>-0.90</td>
      <td>-1.18</td>
      <td>-1.30</td>
      <td>-1.07</td>
      <td>...</td>
      <td>-0.27</td>
      <td>-0.47</td>
      <td>-0.49</td>
      <td>-0.23</td>
      <td>-0.75</td>
      <td>-0.29</td>
      <td>-0.54</td>
      <td>-0.65</td>
      <td>-0.64</td>
      <td>-0.94</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>75</th>
      <td>0.62</td>
      <td>0.64</td>
      <td>0.59</td>
      <td>0.30</td>
      <td>0.01</td>
      <td>0.05</td>
      <td>-0.63</td>
      <td>0.07</td>
      <td>0.36</td>
      <td>0.78</td>
      <td>...</td>
      <td>0.20</td>
      <td>0.22</td>
      <td>0.23</td>
      <td>0.27</td>
      <td>-0.10</td>
      <td>-0.21</td>
      <td>-0.09</td>
      <td>-0.24</td>
      <td>-0.17</td>
      <td>-0.62</td>
    </tr>
    <tr>
      <th>76</th>
      <td>0.32</td>
      <td>0.31</td>
      <td>0.28</td>
      <td>0.42</td>
      <td>-0.24</td>
      <td>-0.48</td>
      <td>-0.73</td>
      <td>-0.64</td>
      <td>0.04</td>
      <td>0.02</td>
      <td>...</td>
      <td>-0.44</td>
      <td>-0.53</td>
      <td>-0.50</td>
      <td>-0.49</td>
      <td>-0.63</td>
      <td>-0.56</td>
      <td>-0.50</td>
      <td>-0.38</td>
      <td>-0.58</td>
      <td>-0.43</td>
    </tr>
    <tr>
      <th>77</th>
      <td>-0.09</td>
      <td>-0.14</td>
      <td>-0.24</td>
      <td>-0.24</td>
      <td>-0.66</td>
      <td>0.00</td>
      <td>0.29</td>
      <td>0.29</td>
      <td>0.60</td>
      <td>0.86</td>
      <td>...</td>
      <td>0.08</td>
      <td>-0.88</td>
      <td>-1.17</td>
      <td>-0.36</td>
      <td>-0.31</td>
      <td>-0.12</td>
      <td>0.29</td>
      <td>-0.02</td>
      <td>0.21</td>
      <td>0.44</td>
    </tr>
    <tr>
      <th>78</th>
      <td>0.11</td>
      <td>0.05</td>
      <td>0.05</td>
      <td>-0.05</td>
      <td>-0.03</td>
      <td>-0.29</td>
      <td>-0.08</td>
      <td>-0.54</td>
      <td>-0.01</td>
      <td>0.01</td>
      <td>...</td>
      <td>-0.73</td>
      <td>-0.54</td>
      <td>-0.53</td>
      <td>-0.92</td>
      <td>-0.68</td>
      <td>-0.87</td>
      <td>-1.31</td>
      <td>-1.02</td>
      <td>-1.10</td>
      <td>-1.62</td>
    </tr>
    <tr>
      <th>79</th>
      <td>0.12</td>
      <td>-0.12</td>
      <td>-0.12</td>
      <td>-0.45</td>
      <td>-0.24</td>
      <td>-0.48</td>
      <td>-0.57</td>
      <td>-0.19</td>
      <td>-0.07</td>
      <td>-0.59</td>
      <td>...</td>
      <td>0.12</td>
      <td>0.03</td>
      <td>-0.28</td>
      <td>0.02</td>
      <td>-0.01</td>
      <td>0.13</td>
      <td>0.09</td>
      <td>-0.01</td>
      <td>-0.03</td>
      <td>-0.23</td>
    </tr>
  </tbody>
</table>
<p>80 rows × 300 columns</p>
</div>



#### `pandas` transpose

In this format, we have time as columns and sample number in the rows. In many cases, we may wish to view the dataset 'the other way around', i.e. with rows as time and columns as sample number. This is achieved with the `transpose` operation:


```python
import pandas as pd
from geog0111.gurlpath import URL

site = 'https://raw.githubusercontent.com'
site_dir = 'igorol/unknown_pleasures_plot/master'
site_file = 'pulsar.csv'

url = URL(site,site_dir,site_file)

# transpose the dataset
df=pd.read_csv(url,header=None).transpose()
df
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>70</th>
      <th>71</th>
      <th>72</th>
      <th>73</th>
      <th>74</th>
      <th>75</th>
      <th>76</th>
      <th>77</th>
      <th>78</th>
      <th>79</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.81</td>
      <td>-0.61</td>
      <td>-1.43</td>
      <td>-1.09</td>
      <td>-1.13</td>
      <td>-0.66</td>
      <td>-0.36</td>
      <td>-0.73</td>
      <td>-0.89</td>
      <td>-0.69</td>
      <td>...</td>
      <td>0.00</td>
      <td>-0.16</td>
      <td>0.19</td>
      <td>-0.32</td>
      <td>-0.16</td>
      <td>0.62</td>
      <td>0.32</td>
      <td>-0.09</td>
      <td>0.11</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.91</td>
      <td>-0.40</td>
      <td>-1.15</td>
      <td>-0.85</td>
      <td>-0.98</td>
      <td>-0.89</td>
      <td>-0.21</td>
      <td>-0.83</td>
      <td>-0.61</td>
      <td>-0.54</td>
      <td>...</td>
      <td>-0.12</td>
      <td>-0.15</td>
      <td>0.06</td>
      <td>-0.83</td>
      <td>-0.26</td>
      <td>0.64</td>
      <td>0.31</td>
      <td>-0.14</td>
      <td>0.05</td>
      <td>-0.12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.09</td>
      <td>-0.42</td>
      <td>-1.25</td>
      <td>-0.72</td>
      <td>-0.93</td>
      <td>-0.87</td>
      <td>-0.44</td>
      <td>-0.91</td>
      <td>-0.74</td>
      <td>-0.84</td>
      <td>...</td>
      <td>0.10</td>
      <td>0.25</td>
      <td>-0.27</td>
      <td>-0.69</td>
      <td>-0.36</td>
      <td>0.59</td>
      <td>0.28</td>
      <td>-0.24</td>
      <td>0.05</td>
      <td>-0.12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.00</td>
      <td>-0.38</td>
      <td>-1.13</td>
      <td>-0.74</td>
      <td>-0.90</td>
      <td>-0.87</td>
      <td>-0.20</td>
      <td>-1.10</td>
      <td>-0.85</td>
      <td>-0.89</td>
      <td>...</td>
      <td>-0.01</td>
      <td>0.37</td>
      <td>-0.11</td>
      <td>-0.80</td>
      <td>-0.49</td>
      <td>0.30</td>
      <td>0.42</td>
      <td>-0.24</td>
      <td>-0.05</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.59</td>
      <td>-0.55</td>
      <td>-0.76</td>
      <td>-0.26</td>
      <td>-1.14</td>
      <td>-1.07</td>
      <td>-0.31</td>
      <td>-0.87</td>
      <td>-0.77</td>
      <td>-0.45</td>
      <td>...</td>
      <td>-0.15</td>
      <td>-0.13</td>
      <td>0.09</td>
      <td>-0.76</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>-0.24</td>
      <td>-0.66</td>
      <td>-0.03</td>
      <td>-0.24</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>295</th>
      <td>-0.26</td>
      <td>-0.83</td>
      <td>0.11</td>
      <td>-1.03</td>
      <td>-0.29</td>
      <td>-0.55</td>
      <td>-1.45</td>
      <td>-1.20</td>
      <td>-0.94</td>
      <td>-0.16</td>
      <td>...</td>
      <td>0.47</td>
      <td>0.10</td>
      <td>-0.06</td>
      <td>0.08</td>
      <td>0.28</td>
      <td>-0.21</td>
      <td>-0.56</td>
      <td>-0.12</td>
      <td>-0.87</td>
      <td>0.13</td>
    </tr>
    <tr>
      <th>296</th>
      <td>-0.52</td>
      <td>-0.80</td>
      <td>-0.77</td>
      <td>-0.78</td>
      <td>-0.54</td>
      <td>-0.62</td>
      <td>-0.77</td>
      <td>-1.40</td>
      <td>-1.05</td>
      <td>0.24</td>
      <td>...</td>
      <td>0.41</td>
      <td>0.02</td>
      <td>-0.08</td>
      <td>-0.15</td>
      <td>-0.01</td>
      <td>-0.09</td>
      <td>-0.50</td>
      <td>0.29</td>
      <td>-1.31</td>
      <td>0.09</td>
    </tr>
    <tr>
      <th>297</th>
      <td>-0.44</td>
      <td>-0.47</td>
      <td>-0.88</td>
      <td>-0.40</td>
      <td>-0.65</td>
      <td>-0.71</td>
      <td>0.03</td>
      <td>-0.51</td>
      <td>-0.51</td>
      <td>-0.17</td>
      <td>...</td>
      <td>0.32</td>
      <td>-0.10</td>
      <td>-0.04</td>
      <td>0.03</td>
      <td>-0.67</td>
      <td>-0.24</td>
      <td>-0.38</td>
      <td>-0.02</td>
      <td>-1.02</td>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>298</th>
      <td>-0.58</td>
      <td>-0.13</td>
      <td>-0.45</td>
      <td>0.18</td>
      <td>-0.64</td>
      <td>-0.88</td>
      <td>0.47</td>
      <td>0.25</td>
      <td>-0.47</td>
      <td>-0.09</td>
      <td>...</td>
      <td>0.57</td>
      <td>-0.16</td>
      <td>0.23</td>
      <td>0.03</td>
      <td>-0.86</td>
      <td>-0.17</td>
      <td>-0.58</td>
      <td>0.21</td>
      <td>-1.10</td>
      <td>-0.03</td>
    </tr>
    <tr>
      <th>299</th>
      <td>-0.54</td>
      <td>-0.12</td>
      <td>-1.01</td>
      <td>0.27</td>
      <td>-0.94</td>
      <td>-0.70</td>
      <td>1.33</td>
      <td>0.74</td>
      <td>-0.79</td>
      <td>0.01</td>
      <td>...</td>
      <td>0.48</td>
      <td>-0.06</td>
      <td>-0.10</td>
      <td>-0.54</td>
      <td>-1.66</td>
      <td>-0.62</td>
      <td>-0.43</td>
      <td>0.44</td>
      <td>-1.62</td>
      <td>-0.23</td>
    </tr>
  </tbody>
</table>
<p>300 rows × 80 columns</p>
</div>



We will use this transposed dataset in future exercises. so make sure you remember how to do this operation.

#### `pandas` format and `read_table`

Not all data files we find on the web may be so straightforward to read though (Hint: **one of the files you will use in Part A of your assessed practical is like this!**). In [020_Python_files](020_Python_files.md) we saw data of Monthly Southeast England precipitation (mm) in a tabular form on the [Met Office website](https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt). We would commonly use the Python package [`pandas`](https://pandas.pydata.org/) to read and analyses such data. 

A more general and reliable method with `pandas` then is to provide a stream to read from. We demonstrate that here with the Met Office data of . [By inspection](https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt), the dataset is seen to have a variable number of spaces between the data columns. This is known as 'whitespace' (i.e. ` ` or `\t` characters). This makes it more complex to read into `pandas` than a CSV format, and we need to specify a [regular expression](https://en.wikipedia.org/wiki/Regular_expression) meaning 'one or more space'. This is `r"[ ]{1,}"` and we give the keyword `sep` for `pandas` as `sep=r"[ ]{1,}"`. Further for `pandas` in this case we must specify that we should use the Python engine to interpret `engine='python'`. Other features of the dataset are that the first 3 rows of data are metadata and should be skipped in reading the dataset: `skiprows=3`, with the 4th line the data column headers. Finally, we see that 'no data' values are given here as the value `-99.9`: `na_values=[-99.9]`. 

Since there are quite a few keyword options to use, we might find it convenient to gather these into a dictionary:

    panda_format = {
        'skiprows'   :  3,
        'na_values'  :  [-99.9],
        'sep'        :  r"[ ]{1,}",
        'engine'     :  'python'
    }


With these file-formatting specifications, we can read this dataset directly into a `pandas` data frame using a stream that we open from the URL with:

    url.open('r')


```python
import pandas as pd
from geog0111.gurlpath import URL

# NB -- avoid trailing / on these
# i.e. dont put 
# site_dir = 'hadobs/hadukp/data/monthly/'
site = 'https://www.metoffice.gov.uk/'
site_dir = 'hadobs/hadukp/data/monthly'
site_file = 'HadSEEP_monthly_qc.txt'

url = URL(site,site_dir,site_file)

panda_format = {
    'skiprows'   :  3,
    'na_values'  :  [-99.9],
    'sep'        :  r"[ ]{1,}",
    'engine'     :  'python'
}

df=pd.read_table(url.open('r'),**panda_format)

# df.head: first n lines
df.head()
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
      <th>YEAR</th>
      <th>JAN</th>
      <th>FEB</th>
      <th>MAR</th>
      <th>APR</th>
      <th>MAY</th>
      <th>JUN</th>
      <th>JUL</th>
      <th>AUG</th>
      <th>SEP</th>
      <th>OCT</th>
      <th>NOV</th>
      <th>DEC</th>
      <th>ANN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1873</td>
      <td>87.1</td>
      <td>50.4</td>
      <td>52.9</td>
      <td>19.9</td>
      <td>41.1</td>
      <td>63.6</td>
      <td>53.2</td>
      <td>56.4</td>
      <td>62.0</td>
      <td>86.0</td>
      <td>59.4</td>
      <td>15.7</td>
      <td>647.7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1874</td>
      <td>46.8</td>
      <td>44.9</td>
      <td>15.8</td>
      <td>48.4</td>
      <td>24.1</td>
      <td>49.9</td>
      <td>28.3</td>
      <td>43.6</td>
      <td>79.4</td>
      <td>96.1</td>
      <td>63.9</td>
      <td>52.3</td>
      <td>593.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1875</td>
      <td>96.9</td>
      <td>39.7</td>
      <td>22.9</td>
      <td>37.0</td>
      <td>39.1</td>
      <td>76.1</td>
      <td>125.1</td>
      <td>40.8</td>
      <td>54.7</td>
      <td>137.7</td>
      <td>106.4</td>
      <td>27.1</td>
      <td>803.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1876</td>
      <td>31.8</td>
      <td>71.9</td>
      <td>79.5</td>
      <td>63.6</td>
      <td>16.5</td>
      <td>37.2</td>
      <td>22.3</td>
      <td>66.3</td>
      <td>118.2</td>
      <td>34.1</td>
      <td>89.0</td>
      <td>162.9</td>
      <td>793.3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1877</td>
      <td>146.0</td>
      <td>47.7</td>
      <td>56.2</td>
      <td>66.4</td>
      <td>62.3</td>
      <td>24.9</td>
      <td>78.5</td>
      <td>82.4</td>
      <td>38.4</td>
      <td>58.1</td>
      <td>144.5</td>
      <td>54.2</td>
      <td>859.6</td>
    </tr>
  </tbody>
</table>
</div>



#### Exercise 2

The file [2276931.csv](https://raw.githubusercontent.com/UCL-EO/geog0111/master/data/2276931.csv) contains precipitation data for an [NOAA weather station](https://www.ncdc.noaa.gov/cdo-web/datasets#GSOY) `HAVANA 4.2 SW, FL US` for the year 2020 to date.

The dataset URL is:

https://raw.githubusercontent.com/UCL-EO/geog0111/master/data/2276931.csv

* Inspect the file to discover any issues you must account for.
* Read the file into `pandas` using `url.open('r')`.
* print the first 5 lines of data

## Selecting data in `pandas`, and `datetime`

Whilst it is a good start to be able to load a dataset into a dataFrame using `pandas`, we need to be able to select data from this.


```python
import pandas as pd
from geog0111.gurlpath import URL

site = 'https://www.metoffice.gov.uk/'
site_dir = 'hadobs/hadukp/data/monthly'
site_file = 'HadSEEP_monthly_qc.txt'

url = URL(site,site_dir,site_file)

panda_format = {
    'skiprows'   :  3,
    'na_values'  :  [-99.9],
    'sep'        :  r"[ ]{1,}",
    'engine'     :  'python'
}

df_had=pd.read_table(url.open('r'),**panda_format)

# df.head: first n lines
df_had.head()
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
      <th>YEAR</th>
      <th>JAN</th>
      <th>FEB</th>
      <th>MAR</th>
      <th>APR</th>
      <th>MAY</th>
      <th>JUN</th>
      <th>JUL</th>
      <th>AUG</th>
      <th>SEP</th>
      <th>OCT</th>
      <th>NOV</th>
      <th>DEC</th>
      <th>ANN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1873</td>
      <td>87.1</td>
      <td>50.4</td>
      <td>52.9</td>
      <td>19.9</td>
      <td>41.1</td>
      <td>63.6</td>
      <td>53.2</td>
      <td>56.4</td>
      <td>62.0</td>
      <td>86.0</td>
      <td>59.4</td>
      <td>15.7</td>
      <td>647.7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1874</td>
      <td>46.8</td>
      <td>44.9</td>
      <td>15.8</td>
      <td>48.4</td>
      <td>24.1</td>
      <td>49.9</td>
      <td>28.3</td>
      <td>43.6</td>
      <td>79.4</td>
      <td>96.1</td>
      <td>63.9</td>
      <td>52.3</td>
      <td>593.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1875</td>
      <td>96.9</td>
      <td>39.7</td>
      <td>22.9</td>
      <td>37.0</td>
      <td>39.1</td>
      <td>76.1</td>
      <td>125.1</td>
      <td>40.8</td>
      <td>54.7</td>
      <td>137.7</td>
      <td>106.4</td>
      <td>27.1</td>
      <td>803.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1876</td>
      <td>31.8</td>
      <td>71.9</td>
      <td>79.5</td>
      <td>63.6</td>
      <td>16.5</td>
      <td>37.2</td>
      <td>22.3</td>
      <td>66.3</td>
      <td>118.2</td>
      <td>34.1</td>
      <td>89.0</td>
      <td>162.9</td>
      <td>793.3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1877</td>
      <td>146.0</td>
      <td>47.7</td>
      <td>56.2</td>
      <td>66.4</td>
      <td>62.3</td>
      <td>24.9</td>
      <td>78.5</td>
      <td>82.4</td>
      <td>38.4</td>
      <td>58.1</td>
      <td>144.5</td>
      <td>54.2</td>
      <td>859.6</td>
    </tr>
  </tbody>
</table>
</div>



This dataset has column titles `YEAR	JAN	FEB	MAR	APR ... ANN`. We can get the list of column titles as `df_had.columns`:


```python
print(df_had.columns)
```

    Index(['YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP',
           'OCT', 'NOV', 'DEC', 'ANN'],
          dtype='object')


Sometimes it is useful to convert this to a `list`, for list selection in this example:


```python
cols = list(df_had.columns)
for c in cols[1:-1]:
    print(c)
```

    JAN
    FEB
    MAR
    APR
    MAY
    JUN
    JUL
    AUG
    SEP
    OCT
    NOV
    DEC


To select a column, we can use any of these column names as a key, in the same way as in using a dictionary:


```python
df_had['JAN']
```




    0       87.1
    1       46.8
    2       96.9
    3       31.8
    4      146.0
           ...  
    143    114.1
    144     84.8
    145     80.9
    146     34.0
    147     66.9
    Name: JAN, Length: 148, dtype: float64



Or multiple columns, for example only the month datasets here:
    


```python
months = list(df_had.columns)[:-1]
df_had_m = df_had[months]
df_had_m.head()
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
      <th>YEAR</th>
      <th>JAN</th>
      <th>FEB</th>
      <th>MAR</th>
      <th>APR</th>
      <th>MAY</th>
      <th>JUN</th>
      <th>JUL</th>
      <th>AUG</th>
      <th>SEP</th>
      <th>OCT</th>
      <th>NOV</th>
      <th>DEC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1873</td>
      <td>87.1</td>
      <td>50.4</td>
      <td>52.9</td>
      <td>19.9</td>
      <td>41.1</td>
      <td>63.6</td>
      <td>53.2</td>
      <td>56.4</td>
      <td>62.0</td>
      <td>86.0</td>
      <td>59.4</td>
      <td>15.7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1874</td>
      <td>46.8</td>
      <td>44.9</td>
      <td>15.8</td>
      <td>48.4</td>
      <td>24.1</td>
      <td>49.9</td>
      <td>28.3</td>
      <td>43.6</td>
      <td>79.4</td>
      <td>96.1</td>
      <td>63.9</td>
      <td>52.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1875</td>
      <td>96.9</td>
      <td>39.7</td>
      <td>22.9</td>
      <td>37.0</td>
      <td>39.1</td>
      <td>76.1</td>
      <td>125.1</td>
      <td>40.8</td>
      <td>54.7</td>
      <td>137.7</td>
      <td>106.4</td>
      <td>27.1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1876</td>
      <td>31.8</td>
      <td>71.9</td>
      <td>79.5</td>
      <td>63.6</td>
      <td>16.5</td>
      <td>37.2</td>
      <td>22.3</td>
      <td>66.3</td>
      <td>118.2</td>
      <td>34.1</td>
      <td>89.0</td>
      <td>162.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1877</td>
      <td>146.0</td>
      <td>47.7</td>
      <td>56.2</td>
      <td>66.4</td>
      <td>62.3</td>
      <td>24.9</td>
      <td>78.5</td>
      <td>82.4</td>
      <td>38.4</td>
      <td>58.1</td>
      <td>144.5</td>
      <td>54.2</td>
    </tr>
  </tbody>
</table>
</div>



To select data rows, we can set some condition as a mask. 


```python
df_had_m[df_had_m['YEAR'] > 2000].head()
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
      <th>YEAR</th>
      <th>JAN</th>
      <th>FEB</th>
      <th>MAR</th>
      <th>APR</th>
      <th>MAY</th>
      <th>JUN</th>
      <th>JUL</th>
      <th>AUG</th>
      <th>SEP</th>
      <th>OCT</th>
      <th>NOV</th>
      <th>DEC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>128</th>
      <td>2001</td>
      <td>93.1</td>
      <td>92.9</td>
      <td>122.4</td>
      <td>75.7</td>
      <td>32.2</td>
      <td>25.8</td>
      <td>51.5</td>
      <td>83.4</td>
      <td>70.1</td>
      <td>133.0</td>
      <td>43.0</td>
      <td>25.2</td>
    </tr>
    <tr>
      <th>129</th>
      <td>2002</td>
      <td>69.4</td>
      <td>79.1</td>
      <td>44.6</td>
      <td>42.9</td>
      <td>78.4</td>
      <td>58.1</td>
      <td>69.5</td>
      <td>43.2</td>
      <td>37.5</td>
      <td>88.4</td>
      <td>175.4</td>
      <td>137.3</td>
    </tr>
    <tr>
      <th>130</th>
      <td>2003</td>
      <td>80.1</td>
      <td>27.6</td>
      <td>25.6</td>
      <td>35.6</td>
      <td>45.3</td>
      <td>49.5</td>
      <td>46.4</td>
      <td>16.2</td>
      <td>11.0</td>
      <td>52.8</td>
      <td>142.6</td>
      <td>74.3</td>
    </tr>
    <tr>
      <th>131</th>
      <td>2004</td>
      <td>86.3</td>
      <td>29.7</td>
      <td>40.5</td>
      <td>81.8</td>
      <td>48.7</td>
      <td>31.1</td>
      <td>52.0</td>
      <td>101.8</td>
      <td>26.7</td>
      <td>121.0</td>
      <td>33.4</td>
      <td>55.9</td>
    </tr>
    <tr>
      <th>132</th>
      <td>2005</td>
      <td>34.4</td>
      <td>21.0</td>
      <td>48.8</td>
      <td>46.5</td>
      <td>28.2</td>
      <td>35.7</td>
      <td>57.3</td>
      <td>49.9</td>
      <td>48.5</td>
      <td>91.5</td>
      <td>50.0</td>
      <td>64.9</td>
    </tr>
  </tbody>
</table>
</div>



The selection of years was straightforward in that example, but sometimes the date can be encoded differently.

Let's generate a test example to see this where we encode the date as 


```python
# generate date strings
dates = [f'2000-{m:>02d}-01' for m in range(1,13)]
# put in DataFrmae
df = pd.DataFrame(dates,columns=["YY-MM-DD"])

# add a column of some values
values = [m*m for m in range(1,13)]
df["VALUES"] = values

df
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
      <th>YY-MM-DD</th>
      <th>VALUES</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000-01-01</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000-02-01</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000-03-01</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000-04-01</td>
      <td>16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000-05-01</td>
      <td>25</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2000-06-01</td>
      <td>36</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2000-07-01</td>
      <td>49</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2000-08-01</td>
      <td>64</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2000-09-01</td>
      <td>81</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2000-10-01</td>
      <td>100</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2000-11-01</td>
      <td>121</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2000-12-01</td>
      <td>144</td>
    </tr>
  </tbody>
</table>
</div>



To filter this form of date description, we need to use [`pd.to_datetime`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html). The easiest way to do this is to create an additional column with the `datetime` object:


```python
df['DATE'] =  pd.to_datetime(df["YY-MM-DD"])
```

Now we can access `datetime` fields such as` df['DATE'].dt.year,df['DATE'].dt.month` from this, and use these to select rows of data. We combine multiple selection criteria with logical operators `and` : `&`, `or` : `|` and `not` : `~`:


```python
# print months with index > 4 and <= 7
df[(df['DATE'].dt.month > 4) & (df['DATE'].dt.month <= 7)]
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
      <th>YY-MM-DD</th>
      <th>VALUES</th>
      <th>DATE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>2000-05-01</td>
      <td>25</td>
      <td>2000-05-01</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2000-06-01</td>
      <td>36</td>
      <td>2000-06-01</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2000-07-01</td>
      <td>49</td>
      <td>2000-07-01</td>
    </tr>
  </tbody>
</table>
</div>



Hint: Take note of how to filter `datetime` fields here. You may find you need it for your assessment.

There are many more functions and approaches for data manipulation in [`pandas`](https://pandas.pydata.org/) that you can read up on later. We have covered the main ones here that you will need in this course and to submit the coursework.

## Writing a CSV file in `pandas`

As well as reading a CSV file, it would be useful to know how to write such a file using `pandas`. All you need to, once the data are in a `pandas` dataframe, is to call `to_csv`:


```python
import pandas as pd

x = list(range(100))
# loop to generate y = x*x
y = [xi * xi for xi in x]

# load into pandas
df = pd.DataFrame({'x data':x,'y data':y})
df.head()
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




```python
from pathlib import Path
# save as csv without the index
df.to_csv(Path('work/dataset.csv'),index=False)
```

#### Exercise 3

Read and print the data in the file '`work/dataset.csv`

## Summary

In this section, we have used `Path` and `URL` classes to open streams from files and URLs. We have seen how to use this to read the stream into packages that can interpret various formats of data, such as `yaml`, `json`, and CSV and tabular data. 

We have seen that using these object-oriented classes to deal with files and URLs means that we can use essentially the same functions throughout. 

We have come across the `pandas` package for reading tabular and similar datasets.


`pandas`:

| Command | Comment | 
| --:|---|
|`pd.read_csv(f)`| Read CSV data from file or URL `f`|
|`pd.read_table(f)`| Read table data from file or URL `f`|
| `skiprows=N` | Keyword to skip `N` rows in reading for `pd.read_table`|
| `na_values=[-99.9]` | Keyword to set list of values to ignore (`-99.9` here) |
| `sep` | Keyword to define field separator |
| `engine='python'` or `engine='C'` | Keyword to set reading engine. `python` is more flexible, but `C` is faster. |
|`df.transpose()` | Transpose (rows->columns, columns->rows) pandas dataframe `df`|
|`df.head(N)` | first `N` lines of data (default 5) |
|`df.columns` | list-like object of column headings |
|`df[cname]` | Select column with name `cname`|
|`df[[c1,c2,c3]]` | Select columns with names `c1`, `c2` and `c3`|
| `pd.DataFrame(list,columns=cnames)` | Create `pandas` dataframe from information in list-like structures `list` with names from list `cnames`|
|`pd.to_datetime(str_list)` | convert list of date strings (e.g. of form `YYYY-MM-DD`) to `datetime` representation |
| `df[datetimes].dt.month` | month from `datetime` field fromn `datetime`-format column with name `datetimes`|
| `df[datetimes].dt.year` | year from `datetime` field fromn `datetime`-format column with name `datetimes`|
| `df[datetimes].dt.day` | day from `datetime` field fromn `datetime`-format column with name `datetimes`|
|`df.to_csv(filename,index=False)` |Write dataframe `df` to CSV format file, with no index column|

