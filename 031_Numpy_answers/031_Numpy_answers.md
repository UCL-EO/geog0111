# 031 Manipulating data: `numpy` : Answers to exercises

#### Exercise 1

* Using code similar to the above and a `for` loop, write the times tables for 2 to 10. The solution you're looking for should look a bit like this:

        [ 2  4  6  8 10 12 14 16 18 20]
        [ 3  6  9 12 15 18 21 24 27 30]
        [ 4  8 12 16 20 24 28 32 36 40]
        [ 5 10 15 20 25 30 35 40 45 50]
        [ 6 12 18 24 30 36 42 48 54 60]
        [ 7 14 21 28 35 42 49 56 63 70]
        [ 8 16 24 32 40 48 56 64 72 80]
        [ 9 18 27 36 45 54 63 72 81 90]
        [ 10  20  30  40  50  60  70  80  90 100]


```python
# ANSWER
# dont forget to import numpy
import numpy as np

msg = '''
Using code similar to the above and a `for` loop, 
write the times tables for 2 to 10. 
The solution you're looking for should look a bit like this:

        [ 2  4  6  8 10 12 14 16 18 20]
        [ 3  6  9 12 15 18 21 24 27 30]
        [ 4  8 12 16 20 24 28 32 36 40]
        [ 5 10 15 20 25 30 35 40 45 50]
        [ 6 12 18 24 30 36 42 48 54 60]
        [ 7 14 21 28 35 42 49 56 63 70]
        [ 8 16 24 32 40 48 56 64 72 80]
        [ 9 18 27 36 45 54 63 72 81 90]
        [ 10  20  30  40  50  60  70  80  90 100]
'''
print(msg)

# set up the core array as integers
arr1 = np.ones(10).astype(int)

# for over 2 to 10
for n in np.arange(1,11):
    print(f'{n:2d} x . -> {arr1*n}')
```

    
    Using code similar to the above and a `for` loop, 
    write the times tables for 2 to 10. 
    The solution you're looking for should look a bit like this:
    
            [ 2  4  6  8 10 12 14 16 18 20]
            [ 3  6  9 12 15 18 21 24 27 30]
            [ 4  8 12 16 20 24 28 32 36 40]
            [ 5 10 15 20 25 30 35 40 45 50]
            [ 6 12 18 24 30 36 42 48 54 60]
            [ 7 14 21 28 35 42 49 56 63 70]
            [ 8 16 24 32 40 48 56 64 72 80]
            [ 9 18 27 36 45 54 63 72 81 90]
            [ 10  20  30  40  50  60  70  80  90 100]
    
     1 x . -> [1 1 1 1 1 1 1 1 1 1]
     2 x . -> [2 2 2 2 2 2 2 2 2 2]
     3 x . -> [3 3 3 3 3 3 3 3 3 3]
     4 x . -> [4 4 4 4 4 4 4 4 4 4]
     5 x . -> [5 5 5 5 5 5 5 5 5 5]
     6 x . -> [6 6 6 6 6 6 6 6 6 6]
     7 x . -> [7 7 7 7 7 7 7 7 7 7]
     8 x . -> [8 8 8 8 8 8 8 8 8 8]
     9 x . -> [9 9 9 9 9 9 9 9 9 9]
    10 x . -> [10 10 10 10 10 10 10 10 10 10]


#### Exercise 2

* write a function that does the following:
    * create a 2-D tuple called `indices` containing the integers `((0, 1, 2, 3, 4),(5, 6, 7, 8, 9))`
    * create a 2-D numpy array called `data` of shape `(5,10)`, data type `int`, initialised with zero
    * set the value of `data[r,c]` to be `1` for each of the 5 row,column pairs specified in `indices`.
    * return the data array
* print out the result returned

The result should look like:

    [[0 0 0 0 0 1 0 0 0 0]
     [0 0 0 0 0 0 1 0 0 0]
     [0 0 0 0 0 0 0 1 0 0]
     [0 0 0 0 0 0 0 0 1 0]
     [0 0 0 0 0 0 0 0 0 1]]

**Hint**: You could use a `for` loop, but what does `data[indices]` give?


```python
# ANSWER 1

# write a function that does the following:

# First we will test out the statements we want

# create a 2-D tuple called indices containing the 
# integers ((0, 1, 2, 3, 4),(5, 6, 7, 8, 9))
indices = ((0, 1, 2, 3, 4),(5, 6, 7, 8, 9))
print(f'indices ->\n{indices}')

# create a 2-D numpy array called data 
# of shape (5,10), data type int, initialised with zero
data = np.zeros((5,10),dtype=np.int)
print(f'data       ->\n{data}')
print(f'data.shape -> {data.shape}')

# set the value of data[r,c] to be 1 
# for each of the 5 row,column pairs specified in indices.
data[indices] = 1
print(f'data now   ->\n{data}')

# return the data array
# print out the result returned


```

    indices ->
    ((0, 1, 2, 3, 4), (5, 6, 7, 8, 9))
    data       ->
    [[0 0 0 0 0 0 0 0 0 0]
     [0 0 0 0 0 0 0 0 0 0]
     [0 0 0 0 0 0 0 0 0 0]
     [0 0 0 0 0 0 0 0 0 0]
     [0 0 0 0 0 0 0 0 0 0]]
    data.shape -> (5, 10)
    data now   ->
    [[0 0 0 0 0 1 0 0 0 0]
     [0 0 0 0 0 0 1 0 0 0]
     [0 0 0 0 0 0 0 1 0 0]
     [0 0 0 0 0 0 0 0 1 0]
     [0 0 0 0 0 0 0 0 0 1]]



```python
# ANSWER 2

# write a function that does the following:

def doit():
    '''
    return (5,10) zero-value integer array 
    with ((0, 1, 2, 3, 4),(5, 6, 7, 8, 9))
    set to 1
    '''
    # create a 2-D tuple called indices containing the 
    # integers ((0, 1, 2, 3, 4),(5, 6, 7, 8, 9))
    indices = ((0, 1, 2, 3, 4),(5, 6, 7, 8, 9))
    
    # create a 2-D numpy array called data 
    # of shape (5,10), data type int, initialised with zero
    data = np.zeros((5,10),dtype=np.int)

    # set the value of data[r,c] to be 1 
    # for each of the 5 row,column pairs specified in indices.
    data[indices] = 1
    
    # return the data array
    return data

# print out the result returned
print(doit())

```

    [[0 0 0 0 0 1 0 0 0 0]
     [0 0 0 0 0 0 1 0 0 0]
     [0 0 0 0 0 0 0 1 0 0]
     [0 0 0 0 0 0 0 0 1 0]
     [0 0 0 0 0 0 0 0 0 1]]


#### Exercise 3

* write a more flexible version of you function above where `indices`, the value you want to set (`1` above) and the desired shape of `data` are specified through function keyword arguments (e.g. `indices=((0, 1, 2, 3, 4),(5, 6, 7, 8, 9)),value=1`) with the shape set as a required argument.




```python
# ANSWER 3

# write a more flexible version of you function 
# above where `indices`, the value you want to 
# set (`1` above) and the desired shape of `data` 
# are specified through function keyword arguments 
# (e.g. `indices=((0, 1, 2, 3, 4),(5, 6, 7, 8, 9)),
# value=1`) with the shape set as a required argument.

'''
set_value
'''
def set_value(shape,indices=None,\
         value=0):
    '''
    return zero-value integer array of shape shape
    with indices set to value
    
    arguments:
        shape.  : desired array shape
    
    keywords:
        indices : tuple of indices to set. default None
        value   : integer value to set. default 0
    '''
    # create a 2-D numpy array called data 
    # of shape , data type int, initialised with zero
    data = np.zeros(shape,dtype=np.int)

    # set the value of data[r,c] to be 1 
    # for each of the 5 row,column pairs specified in indices.
    data[indices] = value
    
    # return the data array
    return data

# print out the result returned
print(f'set_value((5,5))\n->\n{set_value((5,5))}')
print(f'set_value((4,6),value=1,indices=((1,2,3),(0,1,2)))\n->\n',\
      f'{set_value((4,6),value=1,indices=((1,2,3),(0,1,2)))}')

```

    set_value((5,5))
    ->
    [[0 0 0 0 0]
     [0 0 0 0 0]
     [0 0 0 0 0]
     [0 0 0 0 0]
     [0 0 0 0 0]]
    set_value((4,6),value=1,indices=((1,2,3),(0,1,2)))
    ->
     [[0 0 0 0 0 0]
     [1 0 0 0 0 0]
     [0 1 0 0 0 0]
     [0 0 1 0 0 0]]


#### Exercise 4

* print an array of integer numbers from 100 to 1
* print an array with 9 numbers equally spaced between 100 and 1

Hint: what value of skip would be appropriate here? what about `start` and `stop`?


```python
# ANSWER
import numpy as np
# print an array of integer numbers from 100 to 1
print(np.linspace(100,1,100,dtype=np.int))
# OR use np.arange
print(np.arange(100,1,-1))

# print an array with 9 numbers equally spaced between 100 and 1
print(np.linspace(100,1,9))
```

    [100  99  98  97  96  95  94  93  92  91  90  89  88  87  86  85  84  83
      82  81  80  79  78  77  76  75  74  73  72  71  70  69  68  67  66  65
      64  63  62  61  60  59  58  57  56  55  54  53  52  51  50  49  48  47
      46  45  44  43  42  41  40  39  38  37  36  35  34  33  32  31  30  29
      28  27  26  25  24  23  22  21  20  19  18  17  16  15  14  13  12  11
      10   9   8   7   6   5   4   3   2   1]
    [100  99  98  97  96  95  94  93  92  91  90  89  88  87  86  85  84  83
      82  81  80  79  78  77  76  75  74  73  72  71  70  69  68  67  66  65
      64  63  62  61  60  59  58  57  56  55  54  53  52  51  50  49  48  47
      46  45  44  43  42  41  40  39  38  37  36  35  34  33  32  31  30  29
      28  27  26  25  24  23  22  21  20  19  18  17  16  15  14  13  12  11
      10   9   8   7   6   5   4   3   2]
    [100.     87.625  75.25   62.875  50.5    38.125  25.75   13.375   1.   ]


#### Exercise 5

* Print out the total number of launches per month, for each month.
* Print out the total number of launches per year, for the years 2010 to 2020 inclusive


```python
# ANSWER
import numpy as np

filename = 'data/satellites-1957-2021.gz'
data=np.loadtxt(filename).astype(np.int)

# Print out the total number of launches 
# per month, for each month.
# use sum() to sum over data[m] and loop over m
# get length of m from data.shape[0]
for m in range(data.shape[0]):
    print(f'{data[m].sum()} launches in month {m}')
```

    2173 launches in month 0
    3745 launches in month 1
    2895 launches in month 2
    3183 launches in month 3
    6606 launches in month 4
    5772 launches in month 5
    3279 launches in month 6
    2481 launches in month 7
    4402 launches in month 8
    4035 launches in month 9
    3273 launches in month 10
    3845 launches in month 11



```python
# ANSWER
import numpy as np

filename = 'data/satellites-1957-2021.gz'
data=np.loadtxt(filename).astype(np.int)

# Print out the total number of launches 
# per year, for the years 2010 to 2020
# use sum() to sum over data[y] and loop over y
# translate year to index by subtracting 1957

# its best to be explicit about this
# this answer more clearly relates to the qn
years = np.arange(2010,2020+1) - 1957
for y in years:
    print(f'{data[:,y].sum()} launches in year {y+1957}')

```

    373 launches in year 2010
    315 launches in year 2011
    435 launches in year 2012
    352 launches in year 2013
    355 launches in year 2014
    335 launches in year 2015
    308 launches in year 2016
    512 launches in year 2017
    741 launches in year 2018
    735 launches in year 2019
    922 launches in year 2020


#### Exercise 6

* Plot the total number of satellite launches per year, as a function of year

You will need to remember how to [plot line graphs](023_Plotting.md#Plotting-Graphs)


```python
# ANSWER

import numpy as np
import matplotlib.pyplot as plt

filename = 'data/satellites-1957-2021.gz'
data=np.loadtxt(filename).astype(np.int)

# total for all years, so sum over all months (axis 0)
n = data.sum(axis=0)
# clean way to do years
years = np.arange(1957,1957+data.shape[1])

name = f'Number of satellite launches per year {years[0]} to {years[-1]}'

# plot size 
x_size,y_size = 12,4
fig, axs = plt.subplots(1,1,figsize=(x_size,y_size))
fig.suptitle(name)
# plot y-data and set the label
axs.plot(years,n)
# set x-limits to get a neat graph
axs.set_xlim(years[0],years[-1])

axs.set_ylabel(f'Number of launches')
# x-label
axs.set_xlabel(f'year')
```




    Text(0.5, 0, 'year')




![png](031_Numpy_answers_files/031_Numpy_answers_14_1.png)



```python
# ANSWER
# Print out the total number of 
# launches per month, for each month.

# use sum for total
# we can use data.shape[0] for the size of the 1st dimension
for m in range(data.shape[0]):
    print(f'{data[m].sum()} launches in month index {m}')
    
```

    2173 launches in month index 0
    3745 launches in month index 1
    2895 launches in month index 2
    3183 launches in month index 3
    6606 launches in month index 4
    5772 launches in month index 5
    3279 launches in month index 6
    2481 launches in month index 7
    4402 launches in month index 8
    4035 launches in month index 9
    3273 launches in month index 10
    3845 launches in month index 11



```python
# ANSWER
# Print out the total number of 
# launches per year, for the years 2010 to 2020 inclusive

# use sum for total
for y in range(2010,2020+1):
    # y is a year, but we need index
    j = y - 1957
    print(f'{data[:,j].sum()} launches in year {y}')
```

    373 launches in year 2010
    315 launches in year 2011
    435 launches in year 2012
    352 launches in year 2013
    355 launches in year 2014
    335 launches in year 2015
    308 launches in year 2016
    512 launches in year 2017
    741 launches in year 2018
    735 launches in year 2019
    922 launches in year 2020


#### Exercise 7

* Write code to print the months with highest and lowest number of launches


```python
import numpy as np
# ANSWER
# Write code to print the months with 
# highest and lowest number of launches

# read data as before
filename = 'data/satellites-1957-2021.gz'
data=np.loadtxt(filename).astype(np.int)

# sum the data over all years (axis 1)
sum_per_month = data.sum(axis=1)
# Construct an array of months
month_array = 1 + np.arange(data.shape[0])

# Find the location (month) with **most** launches
# Find the index of sum_per_month with highest number (argmmax)
imax = np.argmax(sum_per_month)

# Find the location (month) with **least** launches
# Find the index of sum_per_month with lowest number (argmmax)
imin = np.argmin(sum_per_month)

print(f'the month with most   launches was',\
      f'{month_array[imax]} with {sum_per_month[imax]}')
print(f'the month with fewest launches was',\
      f'{month_array[imin]} with {sum_per_month[imin]}')
```

    the month with most   launches was 5 with 6606
    the month with fewest launches was 1 with 2173


#### Exercise 8

Recall from [previous sections](025_NASA_MODIS_Earthdata.md#MOTA) how to retrieve a MODIS LAI dataset for a particular date. Recall also values of greater than 100 are invalid, and that a scaling of 0.1 should be applied to the LAI.

* Load a MODIS LAI dataset SDS `Lai_500m` for tile `h17v03` day of year 41, 2019. 
* Call the 2D array `data` and confirm that it has a shape (2400, 2400)
* build a mask called `mask` of invalid pixels 
* print the percentage of invalid pixels to 2 decimal places (hint: sum with `sum`)
* scale the data array as appropriate to obtain LAI
* set invalid data values to 'not a number' `np.nan`
* display the resulting image


```python
# ANSWER
from geog0111.modis import Modis
# Load a MODIS LAI dataset SDS 
# `Lai_500m` for tile `h17v03` day of year 41, 2019
kwargs = {
    'tile'      :    ['h17v03'],
    'product'   :    'MCD15A3H',
    'sds'       :    'Lai_500m',
}
modis = Modis(**kwargs)
# specify day of year (DOY) and year
data_MCD15A3H = modis.get_data(2019,doy=1+4*10)

# Call the 2D array `data` and 
# confirm that it has a shape (2400, 2400)
data = data_MCD15A3H['Lai_500m']
assert data.shape == (2400,2400)

# build a mask called `mask` of invalid pixels
mask = (data > 100)

# count how many invalid pixels there are (`sum`)
perc = 100 * mask.sum()/(mask.shape[0] * mask.shape[1])
print(f'{perc : .2f}% invalid pixels')

# scale the data array as appropriate to obtain LAI
data = data * 0.1

# set invalid data values to 'not a number' np.nan
data[mask] = np.nan
```

     77.22% invalid pixels



```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1,1,figsize=(16,8))
# plot image data: use vmin and vmax to set limits
im = axs.imshow(data,vmax=10,interpolation=None)
fig.colorbar(im, ax=axs)

```




    <matplotlib.colorbar.Colorbar at 0x7f29c1ccf950>




![png](031_Numpy_answers_files/031_Numpy_answers_21_1.png)

