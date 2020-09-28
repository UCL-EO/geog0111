# 031 Manipulating data: `numpy`


## Purpose


While Python has a rich set of modules and data types by default, for numerical computing you'll be using two main libraries that conform the backbone of the [Python scientific stack](https://scipy.org/about.html). These libraries implement a great deal of functionality related to mathematical operations and efficient computations on large data volumes. These libraries are [`numpy`](http://numpy.org) and [`scipy`](http://scipy.org). `numpy`, which we will concentrate on in this section, deals with efficient arrays, similar to lists, that simplify many common processing operations. Of course, just doing calculations isn't much fun if you can't plot some results. To do this, we use the [`matplotlib`](http://matplotlib.org) library that we have seen in previous sessions.


### Prerequisites

You will need some understanding of the following:


* [001 Using Notebooks](001_Notebook_use.md)
* [003 Getting help](003_Help.md)
* [010 Variables, comments and print()](010_Python_Introduction.md)
* [011 Data types](011_Python_data_types.md) 
* [012 String formatting](012_Python_strings.md)
* [013_Python_string_methods](013_Python_string_methods.md)
* [020_Python_files](020_Python_files.md)
* [021 Streams](021_Streams.md)
* [022 Read write files](022_Read_write_files.md)
* [023 Plotting](023_Plotting.md)
* [024_Image_display](024_Image_display.md)
* [030_NASA_MODIS_Earthdata](030_NASA_MODIS_Earthdata.md)


## `numpy`

### Introduction to arrays

You import the `numpy` library using

    import numpy as np
    
This means that all the functionality of `numpy` is accessed by the prefix `np.`: e.g. `np.array`. The main element of `numpy` is the numpy array. 

An array is in some ways like the [list object we have seen before](014_Python_groups.md#list), but unlike a list, all the elements are of the same type, for example floating point numbers. Further, the range of things we can do with a `numpy` list is much greater than with the basic list.


```python
import numpy as np  # Import the numpy library

# Example 1
# An array with 5 ones
arr = np.ones(5)
print(f'--> Array with 5 ones:\n{arr}')

# type
print(f'--> type of array:\n{type(arr)}')
assert type(arr) == np.ndarray

# Example 2
arr = np.array([1, 2, 3, 4])
print(f'--> Array started from a list of integers:\n{arr}')

# Example 3
# An array started from a list of numbers, what's the difference??
arr = np.array([1., 2, 3, 4])
print(f'--> Array started from a list of floats (some implicit):\n{arr}')

```

    --> Array with 5 ones:
    [1. 1. 1. 1. 1.]
    --> type of array:
    <class 'numpy.ndarray'>
    --> Array started from a list of integers:
    [1 2 3 4]
    --> Array started from a list of floats (some implicit):
    [1. 2. 3. 4.]


In the example above we have generated an array where all the elements are `1.0`, using [`np.ones`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ones.html), and then we have been able to generate arrays from lists using the [`np.array`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html) function. The difference between the 2nd and 3rd examples is that in the 2nd example, all the elements of the list are integers, and in the 3rd example, one is a floating point number. `numpy` automatically makes the array floating point by converting the integers to floating point numbers.



We saw in an [earlier session](011_Python_data_types.md#Conversion-between-data-types) how we could convert a floating point number to integer with:



```python
float_version = 10.5
print(f'float version: {float_version}')

# convert individual number to int
int_version = int(float_version)
print(f'int version  : {int_version}')
```

    float version: 10.5
    int version  : 10


We can similarly convert between numpy data types (where appropriate) with `np.astype()`:


```python
# An array started from a list of numbers, what's the difference??
float_version = np.array([1., 2., 3., 4.])
print(f'float version: {float_version}')

# convert whole array to int
int_version = float_version.astype(np.int)
print(f'int version  : {int_version}')
```

    float version: [1. 2. 3. 4.]
    int version  : [1 2 3 4]


### Array arithmetic

What else can we do with arrays? Perhaps the most significant thing is that can efficiently operate all array elements without loops, by treating the array as an object:


```python
arr = np.ones(10)
print(f'2 x {arr} \n  = {2 * arr}')
```

    2 x [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.] 
      = [2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]


`numpy` is clever enough to figure out that the 2 multiplying the array is applied to all elements of the array, and returns an array of the same size as `arr` with the elements of `arr` multiplied by 2. We can also multiply two arrays of the same size. So let's create an array with the numbers 0 to 9 and one with the numbers 9 to 0 and do a times table:


```python
arr1 = 9 * np.ones(10).astype(np.int)
arr2 = np.arange(1, 11)  # arange gives an array from 1 to 11, 11 not included

print(arr1)
print(arr2)

print(arr1 * arr2)
```

    [9 9 9 9 9 9 9 9 9 9]
    [ 1  2  3  4  5  6  7  8  9 10]
    [ 9 18 27 36 45 54 63 72 81 90]


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

We can get a tuple of the array shape with `array.shape`.

If the arrays are of the same shape, you can do standard operations between them **element-wise**:


```python
arr1 = np.array([3, 4, 5, 6.])
arr2 = np.array([30, 40, 50, 60.])

print(arr2 - arr1)
print(arr1 * arr2)

print("Array shapes:")
print(f"arr1: {arr1.shape}")
print(f"arr2: {arr2.shape}")
```

    [27. 36. 45. 54.]
    [ 90. 160. 250. 360.]
    Array shapes:
    arr1: (4,)
    arr2: (4,)


The `numpy` documenation is huge. There's an [user's guide](https://docs.scipy.org/doc/numpy/user/index.html), as well as a reference to all the [contents of the library](https://docs.scipy.org/doc/numpy/reference/index.html). There's even [a tutorial availabe](https://docs.scipy.org/doc/numpy/user/quickstart.html) if you get bored with this one.

### More detail on `numpy.arrays` 

So far, we have seen a 1D array, which is the equivalent to a vector. But arrays can have more dimensions: a 2D array would be equivalent to a matrix (or an image, with rows and columns), and a 3D array would be a volume split into voxels, as seen below


[![numpy arrays](images/1*Ikn1J6siiiCSk4ivYUhdgw.png)](https://cdn-images-1.medium.com/max/1120/1*Ikn1J6siiiCSk4ivYUhdgw.png)


So a 1D array has one axis, a 2D array has 2 axes, a 3D array 3, and so on. The `shape` of the array provides a tuple with the number of elements along each axis. Let's see this with some generally useful array creation options:


```python
# Create a 2D array from a list of rows. 
# Note that the 3 rows have the same number of elements!
arr1 = np.array([[0,  1,  2,  3,  4],\
                 [5,  6,  7,  8,  9],\
                 [10, 11, 12, 13, 14]])

# A 2D array from a list of tuples.
# We're specifically asking for floating point numbers
arr2 = np.array([(1.5, 2, 3),\
                 (4  , 5, 6)], dtype=np.float)
print("3*5 array:")
print(arr1)
print("2*3 array:")
print(arr2)
```

    3*5 array:
    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]]
    2*3 array:
    [[1.5 2.  3. ]
     [4.  5.  6. ]]


### Array creators

Quite often, we will want to initialise an array to be all the same number. The methods for doing this as 0,1 in `numpy` are `np.zeros()` and `np.ones()` respectively.

We specify the shape of the array we want with an appropriate tuple.

We can specify the data type of the array with the keyword `dtype=np.int` (for integer). This would have the same effect as using `array.astype(np.int)` as above, but is shorter, clearer and neater. 


```python
# Creates a 3*4 array of 0s
arr = np.zeros((3, 4))
print("3*4 array of 0s")
print(arr)

# Creates a 2x3x4 array of int 1's
print("2*3*4 array of 1s (integers)")
arr = np.ones((2, 3, 4), dtype=np.int)
print(arr)
```

    3*4 array of 0s
    [[0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]]
    2*3*4 array of 1s (integers)
    [[[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]
    
     [[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]]


A similar useful set of functions are `np.ones_like` and `np.zeros_like`. These create a copy of an array, with the values set to 1 or 0 respectively:


```python
base = np.array([[1,2,3],[4,7,0]])
print(f'base:\n{base}')

z = np.zeros_like(base)
print(f'z:\n{z}')
```

    base:
    [[1 2 3]
     [4 7 0]]
    z:
    [[0 0 0]
     [0 0 0]]


### Indexing arrays

We can refer to a particular value within an array with a tuple describing an index. 

For example:


```python
import numpy as np

arr = np.array([[0,  1,  2,  3,  4],\
                 [5,  6,  7,  8,  9],\
                 [10, 11, 12, 13, 14]])

# row 2, column 3
# so index is (2,3)
print(arr[2,3])
```

    13


In the example above, the index was implicitly a tuple, but we can also be explicit:


```python
# row 2, column 3
# so index is (2,3)
# make an index tuple
index = (2,3)
print(arr[index])
```

    13


If we want to refer to a set of indices, we can use a 2D index tuple:


```python
import numpy as np

arr = np.array([[0,  1,  2,  3,  4],\
                 [5,  6,  7,  8,  9],\
                 [10, 11, 12, 13, 14]])

print(f'shape is {arr.shape}')
# make sure we dont index outside of this shape!
# row 2, column 3
# row 0, column 4
# row 1, column 2

# so 2D index is ((2,0,1),(3,4,1))
# make an index tuple
print(f'data:\n{arr}')
index = ((2,0,1),(3,4,1))
print(f'values at {index} are {arr[index]}')
```

    shape is (3, 5)
    data:
    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]]
    values at ((2, 0, 1), (3, 4, 1)) are [13  4  6]


We will see below that there are other options for referring to elements of an array, but this 2D tuple of indices is important in showing how to select individual elements from an array.

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

#### Exercise 3

* write a more flexible version of you function above where `indices`, the value you want to set (`1` above) and the desired shape of `data` are specified through function keyword arguments (e.g. `indices=((0, 1, 2, 3, 4),(5, 6, 7, 8, 9)),value=1`) with the shape set as a required argument.



### `np.linspace`, `np.arange`

As well as initialising arrays with the same number as above, we often also want to initialise with common data patterns. This includes simple integer ranges `(start, stop, step)` in a similar fashion to [slicing we saw earlier](013_Python_string_methods.md#slice).

For example:

    np.arange(start, stop, step)
    
will produce a list of integer numbers from `start` to `stop` in steps of `step`. It is similar to the [`range` function we have seen perviously](016_Python_for.md#range()).

We will introduce the function `np.linspace(start, stop, nsamp)` that creates an array of equally-spaced numbers according to the pattern `(start, stop, nsamp)`.


```python
# array creators

print("1D array of numbers from 0 to 2 in increments of 0.3")
start = 0
stop = 2.0
step = 0.3

arr = np.arange(start, stop, step)
print(f'arr of shape {arr.shape}:\n\t{arr}')

start = 0
stop = 34
nsamp = 9
arr = np.linspace(start, stop, nsamp)
print(
    f"array of shape {arr.shape} numbers equally spaced from {start} to {stop}:\n\t{arr}")

np.linspace(stop, start, 9)
```

    1D array of numbers from 0 to 2 in increments of 0.3
    arr of shape (7,):
    	[0.  0.3 0.6 0.9 1.2 1.5 1.8]
    array of shape (9,) numbers equally spaced from 0 to 34:
    	[ 0.    4.25  8.5  12.75 17.   21.25 25.5  29.75 34.  ]





    array([34.  , 29.75, 25.5 , 21.25, 17.  , 12.75,  8.5 ,  4.25,  0.  ])



#### Exercise 4

* print an array of integer numbers from 100 to 1
* print an array with 9 numbers equally spaced between 100 and 1

Hint: what value of skip would be appropriate here? what about `start` and `stop`?

## Summary statistics

Below are some representative arithmetic operations that you can use on arrays. Remember that they happen **elementwise** (i.e. to the whole array):


```python
# initialise some numbers
b = np.arange(4)
print(f'{b}^2 = {b**2}\n')

a = np.array([20, 30, 40, 50])
print(f"assuming in radians,\n10*sin({a}) = {10 * np.sin(a)}")

print("\nSome useful numpy array methods for summary statistics...\n")
print(f"Find the maximum of an array: a.max():   {a.max()}")
print(f"Find the minimum of an array: a.min():   {a.min()}")
print(f"Find the sum of an array: a.sum():       {a.sum()}")
print(f"Find the mean of an array: a.mean():     {a.mean(): >5.2f}")
print(f"Find the std dev of an array: a.std():   {a.std() : >5.2f}")
```

    [0 1 2 3]^2 = [0 1 4 9]
    
    assuming in radians,
    10*sin([20 30 40 50]) = [ 9.12945251 -9.88031624  7.4511316  -2.62374854]
    
    Some useful numpy array methods for summary statistics...
    
    Find the maximum of an array: a.max():   50
    Find the minimum of an array: a.min():   20
    Find the sum of an array: a.sum():       140
    Find the mean of an array: a.mean():     35.00
    Find the std dev of an array: a.std():   11.18



```python
# variance and standard deviation:
#
# try var and see if it is the same as std * std
var = a.var()
std = a.std()

# use np.sqrt for square root
print(f'sqrt({np.sqrt(var)}) should equal {std}')
```

    sqrt(11.180339887498949) should equal 11.180339887498949


### `np.loadtxt`

Let's access an interesting dataset on the frequency of satellite launches to illustrate this.

[![SpaceX landing](images/giphy.gif)](https://media.giphy.com/media/26DNbCqVfLJbYrXIA/giphy.gif)

The library code `geog0111.nsat` accesses a database at [https://www.n2yo.com](https://www.n2yo.com) and gets a table satellite launch data.

Data from this is stored in the datafile [data/satellites-1957-2021.gz](data/satellites-1957-2021.gz). This is a compressed text file.

We can use `np.loadtxt` to read files of this nature into numpy arrays in a similar way to how we [read into panadas](021_Streams.md#Reading-data-into-pandas). If the dataset is not `CSV` but simply a whitespaced text file, it is often easier to use `np.loadtxt` than `pandas`.

In the case of this dataset, we wish to interpret the launch counts as integers, so we convert the data we read to integers.


```python
import numpy as np

filename = 'data/satellites-1957-2021.gz'
data=np.loadtxt(filename).astype(np.int)

# shape of data
print(data.shape)
```

    (12, 64)


The dataset dimensions are to `(month,year)`. Indices into the array are zero-based, so we can relate month number (1 being January) and year number to index `(i,j)` through:

    i = month - 1
    j = year - 1957
    
We can print some summary statistics:


```python
print(f'data shape {data.shape}')

print(f'some summary statistics over the period 1957 to 2021:')
print(f'The total number of launches is {data.sum()}')
print(f'The mean number of launches is {data.mean() : .2f} per month')
```

    data shape (12, 64)
    some summary statistics over the period 1957 to 2021:
    The total number of launches is 45689
    The mean number of launches is  59.49 per month


### slicing

We have seen [above](026_Numpy.md#Indexing-arrays) how we can provide a tuple of indices to access particular array elements. Often we want to access 'blocks' of an array. A set of indices would be inefficient for that. Instead, we use the idea of slices `(from:to:step)` that we have come across before for [strings](013_Python_string_methods.md#slice) . Remember that `to` is "up to but not including" the to number.

If we specify `:` or `::` in the slice, it means we take the defaults for `(from:to:step)`. If we specify only one number, that is `from`. If we specify two, it is `from:to`.

So:

    data[0]
    
is the data for month index 0 (January), `data[1]` for February etc. Or:

    data[0:2]
   
is the data for month index 0 (January) **and** 1 (February)  etc. 

We can get more specific statistics then such as:


```python
import numpy as np

filename = 'data/satellites-1957-2021.gz'
data=np.loadtxt(filename).astype(np.int)

print(f'mean launches in month 0: {data[0].mean() :.2f}')
print(f'max  launches in month 0: {data[0].max()}')
```

    mean launches in month 0: 33.95
    max  launches in month 0: 237


We can refer to items in the second dimension of the array, by using a code for *all* values of the first dimension. So:

    data[:,0]
    
refers to all elements in dimension 0 (i.e. all months here) by only year 0 (1957).


```python
print(f'mean launches in year 1957: {data[:,0].sum()}')
print(f'max  launches in year 1957: {data[:,0].max()}')
```

    mean launches in year 1957: 3
    max  launches in year 1957: 2


#### Exercise 5

* Print out the total number of launches per month, for each month.
* Print out the total number of launches per year, for the years 2010 to 2020 inclusive

### axis

Whilst it is perfectly possibly to loop over one dimension of an array and calculate statistics over the other dimension, it is not very [Pythonic](https://docs.python-guide.org/writing/style/) to do it that way. 

Instead. we can specify the array axes over which we want the operation to occur.

For example, in our satellite launch dataset, the dimension 0 is month index and the dimension 1 is year index. To calculate the mean over all years then, we apply the `mean` function to axis 1:


```python
import numpy as np

filename = 'data/satellites-1957-2021.gz'
data=np.loadtxt(filename).astype(np.int)

# mean over all months
data.mean(axis=1)
```




    array([ 33.953125,  58.515625,  45.234375,  49.734375, 103.21875 ,
            90.1875  ,  51.234375,  38.765625,  68.78125 ,  63.046875,
            51.140625,  60.078125])



This is much more convenient than the loop we did above. The axis keyword is widely used in `numpy`, and you can apply most operations over one or more axis. 

#### Exercise 6

* Plot the total number of satellite launches per year, as a function of year

You will need to remember how to [plot line graphs](023_Plotting.md#Plotting-Graphs)

### `argmin`, `argmax` and masking

Whilst we have generated some initial summary statistics on the dataset, it's not really enough to give us a good idea of the data characteristics.

To do that, we want to be able to ask somewhat more complex questions of the data, such as:

* which *year* has the most/least launches? 
* which month do most launches happen in? 
* which month in which year had the most launches? 
* which years had more than 100 launches?

Whilst we could do some of these with loops and slicing, we expect a more convenient approach for `numpy`.

To be able to address these, we need some new concepts:

* methods `argmin()` and `argmax()` that provide the *index* where the min/max occurs
* masking out array elements that meet some condition

The first set of these, `argmin()` and `argmax()` are straightforward to visualise and use:


```python
import numpy as np

# read data as before
filename = 'data/satellites-1957-2021.gz'
data=np.loadtxt(filename).astype(np.int)

# sum the data over all months (axis 0)
sum_per_year = data.sum(axis=0)
# Construct an array of years
year_array = 1957 + np.arange(data.shape[1])

# Find the location (year) with **most** launches
# Find the index of sum_per_year with highest number (argmmax)
imax = np.argmax(sum_per_year)

# Find the location (year) with **least** launches
# Find the index of sum_per_year with lowest number (argmmax)
imin = np.argmin(sum_per_year)

print(f'the year with most   launches was',\
      f'{year_array[imax]} with {sum_per_year[imax]}')
print(f'the year with fewest launches was',\
      f'{year_array[imin]} with {sum_per_year[imin]}')
```

    the year with most   launches was 1999 with 4195
    the year with fewest launches was 1957 with 3


#### Exercise 7

* Write code to print the months with highest and lowest number of launches

In section [011_Python_data_types](011_Python_data_types.md#Data-types:-bool) we came across the boolean (binary) data type that can take the states `True` or `False`.

Boolean arrays in `numpy` are important in the efficient use of arrays, as they can act as a mask on an array. 

For example:

The form of filtering above (`high = sum_per_year >= 1000`) produces a numpy array of the same shape as that operated on (`sum_per_year` here) of `bool` data type.  It has entries of `True` where the condition is met, and `False` where it is not met.


```python
import numpy as np

# read data as before
filename = 'data/satellites-1957-2021.gz'
data=np.loadtxt(filename).astype(np.int)
# sum over all months (axis 0)
sum_per_year = data.sum(axis=0)

high = sum_per_year >= 1000
print(high)
```

    [False False False False False False False False  True False False False
     False False False False False False  True  True False False False False
      True False False False False  True  True False False False False False
      True  True False False False False  True False False False False False
     False  True False False False False False False False False False False
     False False False False]


We can think of this logical array as a 'data mask' that we use to select (filter) entries:


```python
# form the data mask
high = (sum_per_year >= 1000)
# form an attau of years
years = 1957 + np.arange(data.shape[1])
# select only elements where mask is True
print(f'years with 1000 or more launches {years[high]}')
```

    years with 1000 or more launches [1965 1975 1976 1981 1986 1987 1993 1994 1999 2006]


We can apply logical operators to boolean arrays:


```python
low = np.logical_not(high)
print(low)
```

    [ True  True  True  True  True  True  True  True False  True  True  True
      True  True  True  True  True  True False False  True  True  True  True
     False  True  True  True  True False False  True  True  True  True  True
     False False  True  True  True  True False  True  True  True  True  True
      True False  True  True  True  True  True  True  True  True  True  True
      True  True  True  True]


including combinations of logical arrays. 

Suppose we want to know the years after the year 2000 that have 1000 or greater launches. We can form two boolean arrays:
    
    years > 2000
    sum_per_year >= 1000
    
Since these arrays are of the same shape, we can combine them element-wise:


```python
c1 = (years > 2000)
c2 = (sum_per_year >= 1000)
combined = np.logical_and(c1,c2)
print(years[combined])
```

    [2006]


### `where`

Sometimes, instead of just applying the filter as above, we want to know the indices of the filtered values.

To do this, we can use the `np.where()` method. This takes a `bool` array as its argument (such as our data masks or other conditions) and returns a tuple of the indices where this is set `True`. 

As an example, lets find month, year pairs where the number of launches is greater than 500. 

For a final flourish, we load the dataset into `pandas` to print it in a table:


```python
# find month, year where launches > 500
import numpy as np
import pandas as pd

# read data as before
filename = 'data/satellites-1957-2021.gz'
data=np.loadtxt(filename).astype(np.int)

month_index,year_index = np.where(data > 500)
# This gives array indices

# convert index to real month and year
# and *transpose* (swap rows and columns)
# using .T
high_launches = np.array([month_index+1,year_index+1957]).T

# load into pandas data frame 
df = pd.DataFrame(high_launches,columns=['month','year'])
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
      <th>month</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1986</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>1994</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>1999</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>1981</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>1993</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>1976</td>
    </tr>
    <tr>
      <th>7</th>
      <td>9</td>
      <td>1997</td>
    </tr>
  </tbody>
</table>
</div>



So `np.where()` is one way  we can derive a set of tuples such as those we saw [above](026_Numpy.md#Indexing-arrays).

#### Exercise 8

Recall from [previous sections](025_NASA_MODIS_Earthdata.md#MOTA) how to retrieve a MODIS LAI dataset for a particular date. Recall also values of greater than 100 are invalid, and that a scaling of 0.1 should be applied to the LAI.

* Load a MODIS LAI dataset SDS `Lai_500m` for tile `h17v03` day of year 41, 2019. 
* Call the 2D array `data` and confirm that it has a shape (2400, 2400)
* build a mask called `mask` of invalid pixels 
* print the percentage of invalid pixels to 2 decimal places (hint: sum with `sum`)
* scale the data array as appropriate to obtain LAI
* set invalid data values to 'not a number' `np.nan`
* display the resulting image

### Summary

In this section, you have been introduced to the `numpy` package and more detail on arrays. The big advantages of `numpy` are that you can easily perform array operators (such as adding two arrays together), and that `numpy` has a large number of useful functions for manipulating N-dimensional data in array form. This makes it particularly appropriate for raster geospatial data processing.

We have seen how to create various forms of array (e.g. `np.ones()`, `np.arange()`), how to calculate some basic statistics (`min()`, `max()` etc), and finding the array index where some pattern occurs (e.g. `argmin()`, `argsort()` or `where()`) and how to generate and use masks for selecting data. 
