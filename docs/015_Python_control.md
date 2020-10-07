# 015 Control in Python: `if`

## Introduction

### Purpose

In this section we will learn how to add conditional control to our codes. We will cover the conditional statement: `if`.

### Prerequisites

You will need some understanding of the following:


* [001 Using Notebooks](001_Notebook_use.md)
* [003 Getting help](003_Help.md)
* [010 Variables, comments and print()](010_Python_Introduction.md)
* [011 Data types](011_Python_data_types.md) 
* [012 String formatting](012_Python_strings.md)
* [013_Python_string_methods](013_Python_string_methods.md)
* [014_Python_groups](014_Python_groups.md)


## Comparison Operators and `if`

### Comparison Operators

A comparison operator 'compares' two terms (e.g. the contents of variables) and returns a boolean data type (`True` or `False`).

For example, to see if the value of some variable `a` has 'the same value as' ('equivalent to') the value of some variable `b`, we use the equivalence operator (`==`). To test for non equivalence, we use the not equivalent operator `!=` (read the `!` as 'not'):



```python
a = 100
b = 10
#
# These are *not* the same, so we expect 
# a == b : False

# Note the use of \n and \t in here
# from 010 for formatting
print (f'a is {a} and b is {b}')
print (f'a is equivalent to b? {a == b}')
```

    a is 100 and b is 10
    a is equivalent to b? False


#### Exercise 1
 
* insert a new cell below here. Use f-strings in forming strings.
* copy the code above 
* add a `print` statement to your code that tests for non equivalence of `a` and `b`
* repeat this in a new cell, but now change the values (or type) of the variables `a` and `b` to `float` or `bool`


A fuller set of comparison operators allows greater or less than tests:

|symbol| meaning|
|:---:|:---:|
| == | is equivalent to |
| != | is not equivalent to |
| > | greater than |
|>= | greater than or equal to|
|<  | less than|
|<=  | less than or equal to    |

so that, for example:


```python
# Comparison examples

# is one plus one list equal to two list?
print (f'1 + 1 == 2    : {1 + 1 == 2}')

# is one less than or equal to 0.999?
print (f'1 <= 0.999    : {1 <= 0.999}')

# is one plus one not equal to two?
print (f'1 + 1 != 2    : {1 + 1 != 2}')

# "is 100 less than 2?"
print (f'100 < 2       : {100 < 2}')

```

    1 + 1 == 2    : True
    1 <= 0.999    : False
    1 + 1 != 2    : False
    100 < 2       : False


#### Exercise 2

* insert a new cell below here
* create variables `a` and `b` and set them to types and values of your choice
* create a variable called `gt_test` and set it to the result of `a > b`
* print a statement of what you have used, and the value of `gt_test`
* explain why you get the result you do

### Conditional test: `if ... elif ... else ...`

A common use of comparisons is for program control, using an `if` statement of the form:

    if condition1:
        # do this 1
        doit1()
        ...
    elif condition2:
        # do this 2
        doit2()
        ...
    else:
        # do this 3
        doit3()
        ...
        

Implicit in these statements is that the conditions return `True` to pass the tests, i.e. we could more fully write:

    if condition1 == True:
        # do this 1
        ...

This form of conditional statement allows us to run blocks of code *only under a particular condition* (or set of conditions).

In Python, the statement(s) we run on condition are *indented*. 

The indent can be one or more spaces or a `<tab>` character, the choice is up to the programmer. However, it **must be consistent**. It is generally best to use spaces rather than tab characters, it is all too easy to mistake one for the other.

<span class="burk">Pay attention to indentation in conditional statements. Getting it wrong is one of the more common errors new Python coders make.</span> 


```python
test = 3
print('test result is',test)

# initialise retval
retval = None

# conduct some tests, and set the 
# variable retval to True if we pass
# any test

if test >= 1:
    retval = True
    print('passed test 1: "if test >= 1"')
elif test == 0:
    retval = True
    print('passed test 2: "if test == 0"')
else:
    retval = False
    print('failed both tests')
    
print('retval is',retval)
```

    test result is 3
    passed test 1: "if test >= 1"
    retval is True


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

We will see later that this is not the best way to do calculations of this sort. First, it is all too easy to make mistakes in typing in both the `doy` boundaries and the month names. Second, it is not very flexible: for instance, consider how would you need to change it for leap or non-leap years. Third, it is not at all [pythonic](https://stackoverflow.com/questions/25011078/what-does-pythonic-mean#:~:text=Pythonic%20means%20code%20that%20doesn,is%20intended%20to%20be%20used.), i.e. doesn't make use of the features of Python that could make it clear and concise.

That said, it is an easily-understandable exercise to try out using conditional statements.

## Summary

We should know know how to use `if` statements in Python to control program flow. We can make choices as to what happens in the code, depending on whether or not one or more tests are passed. This is a common feature of all coding languages, but it is important here that you get used to doing this in Python.

We know that conditions inside `if` statements use indentation in Python, and we know to be careful in our use of this.

There are additional notes in [docs.python.org](https://docs.python.org/3/tutorial/controlflow.html#the-range-function) you can follow up to deepen your understanding of these topics. 

Summary of material in this notebook:

Comparison operators:

|symbol| meaning|
|:---:|:---:|
| == | is equivalent to |
| != | is not equivalent to |
| > | greater than |
|>= | greater than or equal to|
|<  | less than|
|<=  | less than or equal to    |


`If ... elif ... else`:


        if condition1:
            # do this 1
            doit1()
            ...
        elif condition2:
            # do this 2
            doit2()
            ...
        else:
            # do this 3
            doit3()
            ...


