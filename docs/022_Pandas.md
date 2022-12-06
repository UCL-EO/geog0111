# Pandas

## Reading data from into Pandas


The Python package `pandas` is widely-used to read and manipulate data in tabular or similar form. One of the most common tabular data formats is [CSV](https://en.wikipedia.org/wiki/Comma-separated_values).

An interesting CSV-format dataset is that containing the [successive pulses](https://gist.githubusercontent.com/borgar/31c1e476b8e92a11d7e9/raw/0fae97dab6830ecee185a63c1cee0008f6778ff6/pulsar.csv) of the oscillation signal coming from the [Pulsar PSR B1919+21](https://www.joydivisionofficial.com/reimagined/) discovered by [Jocelyn Bell](https://en.wikipedia.org/wiki/Jocelyn_Bell_Burnell) in 1967. Some of you might also recognise it from  a [famous album cover](https://en.wikipedia.org/wiki/Unknown_Pleasures)

![Joy Division](images/small_unknown_pleasures.png)

[By inspection](https://raw.githubusercontent.com/igorol/unknown_pleasures_plot/master/pulsar.csv) we can see the data are 80 lines of 300 columns of data. The data format is simple, with no missing values or metadata. We can straightforwardly use the `pandas` function `pd.read_csv`, specifying the URL, to read this dataset (specifying only `header=None` so that the first line is not interpreted as data column names).


```python
import pandas as pd
from urlpath import URL

site = 'https://raw.githubusercontent.com'
site_dir = 'igorol/unknown_pleasures_plot/master'
site_file = 'pulsar.csv'

url = URL(site,site_dir,site_file)

df=pd.read_csv(url.as_posix(),header=None)
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



### `pandas` transpose

In this format, we have time as columns and sample number in the rows. In many cases, we may wish to view the dataset 'the other way around', i.e. with rows as time and columns as sample number. This is achieved with the `transpose` operation:


```python
import pandas as pd
from urlpath import URL

site = 'https://raw.githubusercontent.com'
site_dir = 'igorol/unknown_pleasures_plot/master'
site_file = 'pulsar.csv'

url = URL(site,site_dir,site_file)

# transpose the dataset
df=pd.read_csv(url.as_posix(),header=None).transpose()
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

## `pandas` format and `read_table`

Not all data files we find on the web may be so straightforward to read though (Hint: **one of the files you will use in Part A of your assessed practical is like this!**). In [020_Python_files](020_Python_files.md) we saw data of Monthly Southeast England precipitation (mm) in a tabular form on the [Met Office website](https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt). We would commonly use the Python package [`pandas`](https://pandas.pydata.org/) to read and analyse such data. 

But the data format is actually quite complex and we can't specify complex formats for reading directly from a URL in pandas.

Instead, in such cases, we need to download the file first, in much the same way we did for MODIS data earlier (but a text file this time, and no password needed).


```python
from urlpath import URL
from pathlib import Path

# NB -- avoid trailing / on these
# i.e. dont put 
# site_dir = 'hadobs/hadukp/data/monthly/' 
# or it wont work!
site = 'https://www.metoffice.gov.uk/'
site_dir = 'hadobs/hadukp/data/monthly'
site_file = 'HadSEEP_monthly_totals.txt'

url = URL(site,site_dir,site_file)

r = url.get()
if r.status_code == 200:
    # setup Path object for output file
    filename = Path('work',url.name)
    # write text data
    filename.write_text(r.text)
    # check size and report
    print(f'file {filename} written: {filename.stat().st_size} bytes')
else:
    print(f'failed to get {url}')
```

    file work/HadSEEP_monthly_totals.txt written: 15209 bytes


Now we want to read this file `work/HadSEEP_monthly_totals.txt` into `pandas`.

[By inspection](https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_totals.txt), the dataset is seen to have a variable number of spaces between the data columns. This is known as 'whitespace' (i.e. ` ` or `\t` characters). This makes it more complex to read into `pandas` than a CSV format, and we need to specify a [regular expression](https://en.wikipedia.org/wiki/Regular_expression) meaning 'one or more space'. This is `r"[ ]{1,}"` and we give the keyword `sep` for `pandas` as `sep=r"[ ]{1,}"`. Further for `pandas` in this case we must specify that we should use the Python engine to interpret `engine='python'`. Other features of the dataset are that the first 3 rows of data are metadata and should be skipped in reading the dataset: `skiprows=3`, with the 4th line the data column headers. Finally, we see that 'no data' values are given here as the value `-99.9`: `na_values=[-99.9]`. 

Since there are quite a few keyword options to use, we might find it convenient to gather these into a dictionary:


```python
import pandas as pd

panda_format = {
    'skiprows'   :  3,
    'na_values'  :  [-99.9],
    'sep'        :  r"[ ]{1,}",
    'engine'     :  'python'
}

filename = Path('work','HadSEEP_monthly_totals.txt')
df=pd.read_table(filename,**panda_format)

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
      <th>Year</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
      <th>Apr</th>
      <th>May</th>
      <th>Jun</th>
      <th>Jul</th>
      <th>Aug</th>
      <th>Sep</th>
      <th>Oct</th>
      <th>Nov</th>
      <th>Dec</th>
      <th>Annual</th>
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



#### Exercise 1

The file [2276931.csv](https://raw.githubusercontent.com/UCL-EO/geog0111/master/notebooks/data/2276931.csv) contains precipitation data for an [NOAA weather station](https://www.ncdc.noaa.gov/cdo-web/datasets#GSOY) `HAVANA 4.2 SW, FL US` for the year 2020 to date.

The dataset URL is:

https://raw.githubusercontent.com/UCL-EO/geog0111/master/notebooks/data/2276931.csv

* Inspect the file to discover any issues you must account for.
* Download the file and read into `pandas`
* print the first 5 lines of data

## Selecting data in `pandas`, and `datetime`

Whilst it is a good start to be able to load a dataset into a dataFrame using `pandas`, we need to be able to select data from this.


```python
import pandas as pd
from urlpath import URL
from pathlib import Path

site = 'https://www.metoffice.gov.uk/'
site_dir = 'hadobs/hadukp/data/monthly'
site_file = 'HadSEEP_monthly_totals.txt'

url = URL(site,site_dir,site_file)

r = url.get()
if r.status_code == 200:
    # setup Path object for output file
    filename = Path('work',url.name)
    # write text data
    filename.write_text(r.text)
    # check size and report
    print(f'file {filename} written: {filename.stat().st_size} bytes')
else:
    print(f'failed to get {url}')

panda_format = {
    'skiprows'   :  3,
    'na_values'  :  [-99.9],
    'sep'        :  r"[ ]{1,}",
    'engine'     :  'python'
}

df_had=pd.read_table(filename,**panda_format)

# df.head: first n lines
df_had.head()
```

    file work/HadSEEP_monthly_totals.txt written: 15209 bytes





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
      <th>Year</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
      <th>Apr</th>
      <th>May</th>
      <th>Jun</th>
      <th>Jul</th>
      <th>Aug</th>
      <th>Sep</th>
      <th>Oct</th>
      <th>Nov</th>
      <th>Dec</th>
      <th>Annual</th>
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



This dataset has column titles `Year	Jan	Feb	Mar	Apr ... Annual`. We can get the list of column titles as `df_had.columns`:


```python
print(df_had.columns)
```

    Index(['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
           'Oct', 'Nov', 'Dec', 'Annual'],
          dtype='object')


Sometimes it is useful to convert this to a `list`, for list selection in this example:


```python
cols = list(df_had.columns)
for c in cols[1:-1]:
    print(c)
```

    Jan
    Feb
    Mar
    Apr
    May
    Jun
    Jul
    Aug
    Sep
    Oct
    Nov
    Dec


To select a column, we can use any of these column names as a key, in the same way as in using a dictionary:


```python
df_had['Jan']
```




    0       87.1
    1       46.8
    2       96.9
    3       31.8
    4      146.0
           ...  
    145     80.9
    146     34.0
    147     66.9
    148    115.6
    149     24.3
    Name: Jan, Length: 150, dtype: float64



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
      <th>Year</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
      <th>Apr</th>
      <th>May</th>
      <th>Jun</th>
      <th>Jul</th>
      <th>Aug</th>
      <th>Sep</th>
      <th>Oct</th>
      <th>Nov</th>
      <th>Dec</th>
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
df_had_m[df_had_m['Year'] > 2000].head()
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
      <th>Year</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
      <th>Apr</th>
      <th>May</th>
      <th>Jun</th>
      <th>Jul</th>
      <th>Aug</th>
      <th>Sep</th>
      <th>Oct</th>
      <th>Nov</th>
      <th>Dec</th>
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
# put in DataFrame
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

#### Exercise 2

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

