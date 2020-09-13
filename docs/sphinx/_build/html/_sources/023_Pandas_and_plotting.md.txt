## 023 `pandas` and plotting

For many datasets that we want to access in simple text formats, we can use specialised packages such as [`pandas`](https://pandas.pydata.org/). This is designed for data analysis and manipulation, and so (mostly) makes it easy for the user to read such data.



```python
import pandas as pd
import io
url = "https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt"

c=pd.read_csv('https://raw.githubusercontent.com/UCL-EO/geog0111/master/data/2276931.csv')
c
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
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>240</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-08-29</td>
      <td>0.39</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>241</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-08-30</td>
      <td>0.12</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>242</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-08-31</td>
      <td>0.06</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>243</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-09-01</td>
      <td>0.44</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>244</th>
      <td>US1FLGD0002</td>
      <td>HAVANA 4.2 SW, FL US</td>
      <td>2020-09-02</td>
      <td>0.09</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>245 rows × 5 columns</p>
</div>




```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# choose the item to plot
quantity = 'PRCP'

# generate figure an plot
fig, ax = plt.subplots(figsize=(15,3))
ax.plot(c['DATE'],c[quantity])

# format the ticks: every month
months = mdates.MonthLocator() 
ax.xaxis.set_major_locator(months)

plt.title(c['NAME'][0])
plt.ylabel(quantity)
```




    Text(0, 0.5, 'PRCP')




![png](023_Pandas_and_plotting_files/023_Pandas_and_plotting_2_1.png)



```python
from geog0111.gurlpath import URL
url = "https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt"

f = URL(url)
```

If we examine the data on the website [HadSEEP_monthly_qc.txt](https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt), we see that the first 3 lines are metedata. The fourth line specifies the data columns, then the rest are datra values, with `-99.9` as invalid.




```python
from geog0111.gurlpath import URL
import io

url = "https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt"
f = URL(url)

text_data = f.read_text()

```

We could do some processing and manipulation of the text data string. For example the following code will split the string on newline `\n` characters into a list, take the first 6 lines of the list, then join it back again into a string:

    '\n'.join(text_data.split('\n')[:6])


```python
print(f'data read is {len(text_data)} bytes of text data')
print('\n'.join(text_data.split('\n')[:6]))
```

    data read is 12915 bytes of text data
    Monthly Southeast England precipitation (mm). Daily automated values used after 1996.
    Wigley & Jones (J.Climatol.,1987), Gregory et al. (Int.J.Clim.,1991)
    Jones & Conway (Int.J.Climatol.,1997), Alexander & Jones (ASL,2001). Values may change after QC.
    YEAR   JAN   FEB   MAR   APR   MAY   JUN   JUL   AUG   SEP   OCT   NOV   DEC   ANN
     1873  87.1  50.4  52.9  19.9  41.1  63.6  53.2  56.4  62.0  86.0  59.4  15.7  647.7
     1874  46.8  44.9  15.8  48.4  24.1  49.9  28.3  43.6  79.4  96.1  63.9  52.3  593.5


This is effective, but normally we would use specialised packages designed for reading tabular data of this sort. 



```python
import pandas as pd
import io
c=pd.read_table(io.StringIO(f.read_text()),skiprows=3,na_values=[-99.9],sep=r"[ ]{1,}",engine='python')
c.head()
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




```python
import matplotlib.pyplot as plt
plt.plot(c['YEAR'],c['JAN'])
```




    [<matplotlib.lines.Line2D at 0x7fc2294edc90>]




![png](023_Pandas_and_plotting_files/023_Pandas_and_plotting_10_1.png)


The iconic cover shows the oscillation signal coming from the Pulsar PSR B1919+21 https://en.wikipedia.org/wiki/PSR_B1919%2B21

derived from https://github.com/igorol/unknown_pleasures_plot and https://matplotlib.org/3.1.1/gallery/animation/unchained.html


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc

from IPython.display import HTML

```


```python
url='https://raw.githubusercontent.com/igorol/unknown_pleasures_plot/master/pulsar.csv'
df=pd.read_csv(url,header=None)
```


```python
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




```python
vertical_margin = 20
horizontal_margin = 100
x_size = 28
y_size = 25
linewidth = 4
plot_name='images/new_order.png'


plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(x_size,y_size),frameon=False)

data = np.array(df)

n_lines = data.shape[0]
x = range(data.shape[1])

ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(min(x)-horizontal_margin, max(x)+horizontal_margin)
ax.set_ylim(-vertical_margin, df.shape[0] + vertical_margin)

def init():
    lines = []
    fills = []
    for i in range(n_lines):
        line = data[i]/3 + (n_lines - i)
        pltline = ax.plot(x, line, lw=linewidth, c='white', alpha=1, zorder=i/n_lines)
        pltfill = ax.fill_between(x, -5,line,  facecolor='black', zorder=i/n_lines)
        lines.append(pltline)
        fills.append(pltfill)
    return (lines,fills)

xx=init()
```


![png](023_Pandas_and_plotting_files/023_Pandas_and_plotting_15_0.png)

