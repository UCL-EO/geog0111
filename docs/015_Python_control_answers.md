# 015 Control in Python: `if` : Answers to exercises

#### Exercise 1
 
* insert a new cell below here. Use f-strings in forming strings.
* copy the code above 
* add a `print` statement to your code that tests for non equivalence of `a` and `b`
* repeat this in a new cell, but now change the values (or type) of the variables `a` and `b` to `float` or `bool`



```python
# ANSWER

# copy the code above 
a = 100
b = 10
#
# These are *not* the same, so we expect 
# a == b : False

# Note the use of \n and \t in here
# from 010 for formatting
print (f'a is {a} and b is {b}')
print (f'a is equivalent to b? {a == b}')

# add a print statement to your code that tests 
# for non equivalence of a and b
print (f'a is not equivalent to b? {a != b}')
```

    a is 100 and b is 10
    a is equivalent to b? False
    a is not equivalent to b? True



```python
# ANSWER

# repeat this in a new cell, but now change the values 
# (or type) of the variables `a` and `b` to `float` or `bool`
# FLOAT

# copy the code above 
a = 100.0
b = 10.0
#
# These are *not* the same, so we expect 
# a == b : False

# Note the use of \n and \t in here
# from 010 for formatting
print (f'a is {a} and b is {b}')
print (f'a is equivalent to b? {a == b}')

# add a print statement to your code that tests 
# for non equivalence of a and b
print (f'a is not equivalent to b? {a != b}')
```

    a is 100.0 and b is 10.0
    a is equivalent to b? False
    a is not equivalent to b? True



```python
# ANSWER

# repeat this in a new cell, but now change the values 
# (or type) of the variables `a` and `b` to `float` or `bool`
# BOOL

# copy the code above 
a = True
b = True
#
# These are *not* the same, so we expect 
# a == b : False

# Note the use of \n and \t in here
# from 010 for formatting
print (f'a is {a} and b is {b}')
print (f'a is equivalent to b? {a == b}')

# add a print statement to your code that tests 
# for non equivalence of a and b
print (f'a is not equivalent to b? {a != b}')
```

    a is True and b is True
    a is equivalent to b? True
    a is not equivalent to b? False


#### Exercise 2

* insert a new cell below here
* create variables `a` and `b` and set them to types and values of your choice
* create a variable called `gt_test` and set it to the result of `a > b`
* print a statement of what you have used, and the value of `gt_test`
* explain why you get the result you do


```python
# ANSWER

# create variables a and b and set them to values of your choice
# here, we choose int values 2 and 4 respectively
a = 2
b = 4

# create a variable called `gt_test` and set it to the result of `a > b`
gt_test = a > b

# print the statement you have used, and the value of `gt_test`
print(f'a > b test for a = {a} and b = {b} :   {gt_test}')

# explain why you get the result you do
msg = '''
  explain why you get the result you do
  
  gt_test is False here, because the statement that a > b
  is not True since a is 2 and b is 4 
'''
print(msg)
```

    a > b test for a = 2 and b = 4 :   False
    
      explain why you get the result you do
      
      gt_test is False here, because the statement that a > b
      is not True since a is 2 and b is 4 
    


#### Exercise 3

* insert a new cell below here
* set a variable `doy` to represent the day of year and initialise it to some integer between 1 and 365 inclusive
* set a variable `month` to be `'January'`
* set a variable `year` to be `'2020'`
* Write a series of conditional statements that set the variable `month` to the correct month for the value of `doy`
* Print the month for the given doy
* Test that you get the right result for several `doy` values

You should assume that `doy` value `1` represents January 1st.

You might find a [DOY calendar](https://www.esrl.noaa.gov/gmd/grad/neubrew/Calendar.jsp) helpful here.

![DOY calendar](images/doycal.png)


```python
# ANSWER
# set a variable doy to represent the day of year and 
# initialise it to some integer between 1 and 365 inclusive
doy = 230

# set a variable month to be 'January'
month = 'January'

# set a variable year to be '2020'
year = '2020'

# Write a series of conditional statements that set the 
# variable month to the correct month for the value of doy
if ( doy < 1 ) or (doy > 366):
    # good to catch errors
    month = f'out of bounds error: doy={doy}'
elif ( doy <= 31 ):
    month = 'January'
elif ( doy <= 60 ):
    month = 'February'
elif ( doy <= 91 ):
    month = 'March'
elif ( doy <= 121 ):
    month = 'April'
elif ( doy <= 152 ):
    month = 'May'
elif ( doy <= 182 ):
    month = 'June'
elif ( doy <= 213 ):
    month = 'July'
elif ( doy <= 244 ):
    month = 'August'
elif ( doy <= 274 ):
    month = 'September'
elif ( doy <= 305 ):
    month = 'October'
elif ( doy <= 335 ):
    month = 'November'
else:
    # it must be December !
    month = 'December'

# Print the month for the given doy
print(f'for doy {doy} year {year} the month is {month}')

# Test that you get the right result for several doy values
```

    for doy 230 year 2020 the month is August

