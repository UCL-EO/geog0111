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

