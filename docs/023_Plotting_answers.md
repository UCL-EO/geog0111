#  023 Plotting Graphs : Answers to exercises

#### Exercise 1

We have seen how to access the dataset labels using:

    headings = df.columns[1:-1]
  
* Copy the code to read the HadSEEP monthly datasets above
* Write and run code that plots the precipitation data for all months separate subplots.


```python
# ANSWER 
# Copy the code to read the HadSEEP monthly datasets above
import pandas as pd
from urlpath import URL
from pathlib import Path

# Monthly Southeast England precipitation (mm) 
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
    
    df=pd.read_table(filename,**panda_format)
    # df.head: first n lines
    ok= True
else:
    print(f'failed to get {url}')

panda_format = {
    'skiprows'   :  3,
    'na_values'  :  [-99.9],
    'sep'        :  r"[ ]{1,}",
    'engine'     :  'python'
}

df=pd.read_table(filename,**panda_format)

# df.head: first n lines
df.head()
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




```python
# ANSWER 2
# Write and run code that plots the 
# precipitation data for all months separate subplots.
import matplotlib.pyplot as plt

# plot size > in y
# need to play with this to get it right
x_size,y_size = 20,30

# get the m onth names from columns
months = df.columns[1:-1]

fig, axs = plt.subplots(12,1,figsize=(x_size,y_size))

# use enumerate in the loop, to get the index
for i,m in enumerate(months):
    # plot y-data and set the label for the first panel
    axs[i].plot(df["Year"],df[m],'k',label=m)
    axs[i].set_ylabel(f'{m} Precipitation (mm)')
    axs[i].set_xlim(year0,year1)

# x-label
_=axs[-1].set_xlabel(f'year')
```


    
![png](023_Plotting_answers_files/023_Plotting_answers_3_0.png)
    


#### Exercise 2
* Read the `2276931.csv` dataset into a pandas dataframe called `df`
* Convert the field `df["DATE"]` to a list called `dates`
* Use your understanding of `datetime` to convert the data `dates[0]` to a `datetime` object called `start_date`
* Convert the data `date[-1]` to a `datetime` object called `end_date`
* Find how many days between start_date and end_date
* Use a loop structure to convert the all elements in `dates` to be the n umber of days after the start date


```python
# ANSWER
# Read the `2276931.csv` dataset into a 
# pandas dataframe called `df`
import pandas as pd
from urlpath import URL
from pathlib import Path

site = 'https://raw.githubusercontent.com'
site_dir = '/UCL-EO/geog0111/master/notebooks/data'
site_file = '2276931.csv'

# form the URL
url = URL(site,site_dir,site_file)

r = url.get()
if r.status_code == 200:
    # setup Path object for output file
    filename = Path('work',url.name)
    # write text data
    filename.write_text(r.text)
    # check size and report
    print(f'file {filename} written: {filename.stat().st_size} bytes')
    
    df=pd.read_table(filename,**panda_format)
    # df.head: first n lines
    ok= True
else:
    print(f'failed to get {url}')

# Read the file into pandas using url.open('r').
df=pd.read_csv(filename)

# print the first 5 lines of data
df.head(5)
```

    file work/2276931.csv written: 15078 bytes





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
from datetime import datetime
# ANSWER
# Convert the field `df["DATE"]` to 
# a list called `dates`
dates = list(df["DATE"])

# Use your understanding of `datetime` to convert 
# the data `dates[0]` to a `datetime` object called `start_date`
# use datetime.strptime(d,"%Y-%m-%d") to read a date in the format 2020-09-02
start_date = datetime.strptime(dates[0], "%Y-%m-%d")
print(f'{dates[0]} -> {start_date}')

# Convert the data `date[-1]` to a 
# `datetime` object called `end_date`
end_date = datetime.strptime(dates[-1], "%Y-%m-%d")
print(f'{dates[-1]} -> {end_date}')

# find how many days between start_date and end_date
# ndays is number of days in date minus start date
ndays = (end_date - start_date).days
print(f'ndays: {start_date} to {end_date}: {ndays}')

# Use a loop structure to convert the all 
# elements in `dates` to be the number of days after the start date
ndays = [(datetime.strptime(d,"%Y-%m-%d")-start_date).days for d in dates]
print(ndays)
```

    2020-01-01 -> 2020-01-01 00:00:00
    2020-09-02 -> 2020-09-02 00:00:00
    ndays: 2020-01-01 00:00:00 to 2020-09-02 00:00:00: 245
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245]


#### Exercise 3

We examined a pulsar time series in a [previous section of notes](022_Pandas.md#pandas-transpose). It contains the [successive pulses](https://gist.githubusercontent.com/borgar/31c1e476b8e92a11d7e9/raw/0fae97dab6830ecee185a63c1cee0008f6778ff6/pulsar.csv) of the oscillation signal coming from the [Pulsar PSR B1919+21](https://www.joydivisionofficial.com/reimagined/) discovered by [Jocelyn Bell](https://en.wikipedia.org/wiki/Jocelyn_Bell_Burnell) in 1967.

The dataset as presented contains samples in columns, so that sample `0` is df[0], up to df[79] (80 samples).

* Plot the pulsar samples in a series of 80 sub-plots. 

**Advice**: 

For the figure, do not label the axes as it will get too cluttered. In any professional figure of that sort, you would need to explain the axes in accompanying text. 

For further 'effects' consider switching off the plotting of axes in each subplot, with:

    ax.axis('off')

for axis `ax` (this may be something like `axs[i]` in your code).

The results should be reminiscent of:

[![pulsar image](images/smallfig537.jpg)](https://blogs.scientificamerican.com/blogs/assets/sa-visual/Image/fig537.jpg)

and 

[![Joy Division](https://images-na.ssl-images-amazon.com/images/I/812FS2R2v6L._AC_SL1500_.jpg)](https://www.amazon.co.uk/Pleasures-VINYL-Joy-Division/dp/B00XILAIWI)

If you want to go further towards re-creating this, you consult [the matplotlib gallery](https://matplotlib.org/3.1.0/gallery/animation/unchained.html) for ideas.


```python
# ANSWER 1

import pandas as pd
from urlpath import URL
from pathlib import Path

site = 'https://raw.githubusercontent.com'
site_dir = 'igorol/unknown_pleasures_plot/master'
site_file = 'pulsar.csv'

url = URL(site,site_dir,site_file)

r = url.get()
if r.status_code == 200:
    # setup Path object for output file
    filename = Path('work',url.name)
    # write text data
    filename.write_text(r.text)
    # check size and report
    print(f'file {filename} written: {filename.stat().st_size} bytes')
    
    df=pd.read_table(filename,**panda_format)
    # df.head: first n lines
    ok= True
else:
    print(f'failed to get {url}')

# transposed version
df=pd.read_csv(filename,header=None).transpose()
df
```

    file work/pulsar.csv written: 130465 bytes





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




```python
# ANSWER 2
# Plot the pulsar samples in a series of 80 sub-plots.
import matplotlib.pyplot as plt

# need to play with this to get it right
x_size,y_size = 15,20

# get the m onth names from columns
samples = df.columns
fig,axs = plt.subplots(len(df.columns),1,figsize=(x_size,y_size))

# use enumerate in the loop, to get the index
for i,m in enumerate(samples):
    axs[i].plot(df[m],'k')
    axs[i].axis('off')
```


    
![png](023_Plotting_answers_files/023_Plotting_answers_9_0.png)
    

