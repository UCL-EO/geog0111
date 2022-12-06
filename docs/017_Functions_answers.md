# 017 Functions in Python : Answers to exercises

### Exercise 1

* in a new code cell below, write a function called `my_name` that prints your name
* demonstrate that your code works (i.e. run it in a code cell)
* show the doc string using `help()` 

**Advice**: make sure it has an appropriate document string, based on the example in the notes, and also check that you have the indentation correct for the code in the function. Notice the semicolon `:` at the end of the `def` statement.


```python
# ANSWER 1

# in a new code cell below, write a function called my_name that prints your name
def my_name():
    '''print my name'''
    print('Lewis')
```


```python
# ANSWER 2
# demonstrate that your code works (i.e. run it in a code cell)
my_name()
```

    Lewis



```python
# ANSWER 3
# show the doc string using help()
help(my_name)
```

    Help on function my_name in module __main__:
    
    my_name()
        print my name
    


### Exercise 2

We assume for this exercise that you know how to create a dictionary from two lists of the same length. This was covered in the [Python_Groups](014_Python_groups.md#dict) notes.

In this exercise, we suggest that you follow the design approach we took above:

- Think first what you will use as inputs and outputs to the function, and come up with some examples of inputs and outputs
- Then consider the Python code you would need to go from the inputs to the outputs
    * Develop and test the core code to achieve the function purpose in a notebook cell with an example input
    * Consider what you might use as a test for your code
- Develop skeleton
    * Write a skeleton function defining the purpose, inputs and outputs. In the skeleton code, you can just pass the inputs straight to the outputs. 
    * Confirm that that works before going further.
    * Confirm that your document string is useful.
    * Write a test
- Implement the core code in the function 
    * Confirm that that works
    * Confirm that your document string is useful.
    * Write a test
- Consider any flaws in your code and how you might improve it

**Your task for the exercise is:**

* design a function to convert two lists of the same length into a dictionary
* the design must include relevant comments, document strings and tests


```python
# Answer 1

# design a function to convert two lists of 
# the same length into a dictionary

# Think first what you will use as inputs and 
# outputs to the function, and come up with some 
# examples of inputs and outputs

msg = '''

The output is a dictionary, with keys and values

example output from a previous exercise, with 
month names as keys and days in month as values. 
Note that we dont need a long example, just one 
complex enough to test

retval =  {
     'January':31,
     'February':29
}
 

The associated input lists for this would be
something like:

month_names = ['January','February']
month_days  = [31,29]

'''
print(msg)
```

    
    
    The output is a dictionary, with keys and values
    
    example output from a previous exercise, with 
    month names as keys and days in month as values. 
    Note that we dont need a long example, just one 
    complex enough to test
    
    retval =  {
         'January':31,
         'February':29
    }
     
    
    The associated input lists for this would be
    something like:
    
    month_names = ['January','February']
    month_days  = [31,29]
    
    



```python
# Answer 2

# design a function to convert two lists of 
# the same length into a dictionary

# Then consider the Python code you would need to 
# go from the inputs to the outputs
#  - Develop and test the core code to achieve 
#    the function purpose in a notebook cell with an example input

# set up example inputs from. ideas above
month_names = ['January','February']
month_days  = [31,29]

# recalling the code about how to create a dictionary from
# two lists:
retval = dict(zip(month_names,month_days))

# print this
print(retval)

# Consider what you might use as a test for your code
# this will be an assert statement of the form
# assert retval == {'January': 31, 'February': 29}
assert retval == {'January': 31, 'February': 29}
print('test passed')
```

    {'January': 31, 'February': 29}
    test passed



```python
# Answer 3
# Develop skeleton
# - Write a skeleton function defining the purpose, inputs and outputs. 
# In the skeleton code, you can just pass the inputs straight to the outputs.

# we call our function list2dict
# and use relevanmt names for the two lists
def list2dict(keys,values):
    '''generate a dictionary from lists of keys and values
      
    Note:
      the length of the lists must be the same

    Inputs:
      - keys   : list of values for the keys
      - values : list of values to associate with the keys
      
    Output:
      - retval : dictionary with keys and values derived
                 from the input lists
    '''
    # for skeleton ,just set output = input
    # but use a tuple to make it explicit that a single
    # item is returned
    return (keys,values)
    
# - Confirm that that works before going further.

# we need some test keys and values to do this
month_names = ['January','February']
month_days  = [31,29]

# run and check that something is returned
print(f'function returns: {list2dict(month_names,month_days)}')

# - Confirm that your document string is useful.
help(list2dict)

# - Write a test 
# with the input and output the same for now!!
assert list2dict(['January','February'],[31,29]) == (['January', 'February'], [31, 29])
print('test passed')
```

    function returns: (['January', 'February'], [31, 29])
    Help on function list2dict in module __main__:
    
    list2dict(keys, values)
        generate a dictionary from lists of keys and values
          
        Note:
          the length of the lists must be the same
        
        Inputs:
          - keys   : list of values for the keys
          - values : list of values to associate with the keys
          
        Output:
          - retval : dictionary with keys and values derived
                     from the input lists
    
    test passed



```python
# Answer 4
# Implement the core code in the function

# we call our function list2dict
# and use relevanmt names for the two lists
def list2dict(keys,values):
    '''generate a dictionary from lists of keys and values
      
    Note:
      the length of the lists must be the same

    Inputs:
      - keys   : list of values for the keys
      - values : list of values to associate with the keys
      
    Output:
      - retval : dictionary with keys and values derived
                 from the input lists
    '''
    # for the dictionary from the lists
    # and set variable retval to the response
    retval = dict(zip(keys,values))
    
    # remember to output!!
    return retval

# Confirm that that works

# we need some test keys and values to do this
month_names = ['January','February']
month_days  = [31,29]

# run and check that something is returned
print(f'function returns: {list2dict(month_names,month_days)}')

# - Confirm that your document string is useful.
help(list2dict)

# - Write a test 
assert list2dict(['January','February'],[31,29]) == {'January': 31, 'February': 29}
print('test passed')
```

    function returns: {'January': 31, 'February': 29}
    Help on function list2dict in module __main__:
    
    list2dict(keys, values)
        generate a dictionary from lists of keys and values
          
        Note:
          the length of the lists must be the same
        
        Inputs:
          - keys   : list of values for the keys
          - values : list of values to associate with the keys
          
        Output:
          - retval : dictionary with keys and values derived
                     from the input lists
    
    test passed



```python
# Answer 5
# Consider any flaws in your code and how you might improve it

msg = '''
# Consider any flaws in your code and how you might improve it

Since we require the inputs to be lists, we could ensure this
by using

    keys = list(keys)
    values = list(values)

or we might examine the data types

An obvious improvement would be to test that the input 
lists are of the same length.

This is done with:

assert len(keys) == len(values)
'''
print(msg)

# we call our function list2dict
# and use relevanmt names for the two lists
def list2dict(keys,values):
    '''generate a dictionary from lists of keys and values
      
    Note:
      the length of the lists must be the same

    Inputs:
      - keys   : list of values for the keys
      - values : list of values to associate with the keys
      
    Output:
      - retval : dictionary with keys and values derived
                 from the input lists
    '''
    # Since we require the inputs to be lists, 
    # we ensure this
    keys = list(keys)
    values = list(values)
    
    # test the inpouts are the same length
    assert len(keys) == len(values)
    
    # for the dictionary from the lists
    # and set variable retval to the response
    retval = dict(zip(keys,values))
    
    # remember to output!!
    return retval

# Confirm that that works

# we need some test keys and values to do this
month_names = ['January','February']
month_days  = [31,29]

# run and check that something is returned
print(f'function returns: {list2dict(month_names,month_days)}')

# - Confirm that your document string is useful.
help(list2dict)

# - Write a test 
assert list2dict(['January','February'],[31,29]) == {'January': 31, 'February': 29}
print('test passed')
```

    
    # Consider any flaws in your code and how you might improve it
    
    Since we require the inputs to be lists, we could ensure this
    by using
    
        keys = list(keys)
        values = list(values)
    
    or we might examine the data types
    
    An obvious improvement would be to test that the input 
    lists are of the same length.
    
    This is done with:
    
    assert len(keys) == len(values)
    
    function returns: {'January': 31, 'February': 29}
    Help on function list2dict in module __main__:
    
    list2dict(keys, values)
        generate a dictionary from lists of keys and values
          
        Note:
          the length of the lists must be the same
        
        Inputs:
          - keys   : list of values for the keys
          - values : list of values to associate with the keys
          
        Output:
          - retval : dictionary with keys and values derived
                     from the input lists
    
    test passed


### Exercise 3

* Starting from the function `list2dict(keys,values)` that you developed above, add keyword arguments to the code to achieve the following:
     - if check=True   : perform checks on the input data
     - if verbose=True : print out information on what is going on in the function
     - set all default keywords to False
* Make sure you perform tests as above, and that you update document strings


```python
# ANSWER
# Starting from the function list2dict(keys,values) 
# that you developed above, add keyword arguments 
# to the code to achieve the following:
#  if check=True : perform checks on the input data
#  if verbose=True : print out information on what is going on in the function
#  set all default keywords to False

# we call our function list2dict
# and use relevanmt names for the two lists

# KWARGS
#  if check=True : perform checks on the input data
#  if verbose=True : print out information on what is going on in the function
#  set all default keywords to False
def list2dict(keys,values,check=False,verbose=False):
    '''generate a dictionary from lists of keys and values
      
    Note:
      the length of the lists must be the same

    Inputs:
      - keys   : list of values for the keys
      - values : list of values to associate with the keys
      
    Output:
      - retval : dictionary with keys and values derived
                 from the input lists
                 
    Optional keyword arguments:
        verbose : print detailed information, default False
        check   : perform internal tests
    '''
    # NB updated doc string ^
    
    # test the inputs are the same length
    # if check flag set True
    if check:
        # verbose comments
        if verbose:
            print('--> perfoming sanity check on array lengths')
        assert len(keys) == len(values)
    
    # for the dictionary from the lists
    # and set variable retval to the response
    
    # verbose comments
    if verbose:
        print(f'--> zipping dictionary for lists of length {len(keys)}')
    retval = dict(zip(keys,values))
    
    # remember to output!!
    return retval

# Confirm that that works

# we need some test keys and values to do this
month_names = ['January','February']
month_days  = [31,29]

# run and check that something is returned
print(f'function returns: {list2dict(month_names,month_days)}')

```

    function returns: {'January': 31, 'February': 29}



```python
# ANSWER
# - Confirm that your document string is useful.
help(list2dict)

```

    Help on function list2dict in module __main__:
    
    list2dict(keys, values, check=False, verbose=False)
        generate a dictionary from lists of keys and values
          
        Note:
          the length of the lists must be the same
        
        Inputs:
          - keys   : list of values for the keys
          - values : list of values to associate with the keys
          
        Output:
          - retval : dictionary with keys and values derived
                     from the input lists
                     
        Optional keyword arguments:
            verbose : print detailed information, default False
            check   : perform internal tests
    



```python
#answer
# tests for the KWARGS

dash='='*5
# - Write tests that also show the kwargs
# no kwargs
print(f'{dash} no kwargs {dash}')
assert list2dict(['January','February'],[31,29]) == {'January': 31, 'February': 29}
print('test passed')

print(f'{dash} verbose=True {dash}')
assert list2dict(['January','February'],[31,29],\
                          verbose=True) \
              == {'January': 31, 'February': 29}

print(f'{dash} check=True {dash}')
assert list2dict(['January','February'],[31,29],\
                          check=True) \
              == {'January': 31, 'February': 29}

print(f'{dash} check=True and verbose=True {dash}')
assert list2dict(['January','February'],[31,29],\
                          check=True,verbose=True) \
              == {'January': 31, 'February': 29}
print('tests passed')
```

    ===== no kwargs =====
    test passed
    ===== verbose=True =====
    --> zipping dictionary for lists of length 2
    ===== check=True =====
    ===== check=True and verbose=True =====
    --> perfoming sanity check on array lengths
    --> zipping dictionary for lists of length 2
    tests passed


#### Exercise 4

Consider the function:


        def power_of_2(ilist):
            """return a list of 2 to the power of the values of the arguments 

            Inputs:
                ilist : list of integers

            Output:
                list of [2**arg[0],2**arg[1],...]
            """

            # initialise list
            olist = []

            # loop over the arg list
            for i in ilist:
                # append the 2**i value
                olist.append(2**i)
            # return the list
            return olist


* Test this function, inputting a list of integers from 0 to 4 inclusive
* Write a more Pythonic version of this, making use of list comprehensions, `map`, `reduce` or `lambda` functions as appropriate.


```python
# ANSWER

msg = '''
Consider the function:

        def power_of_2(ilist):
            """return a list of 2 to the power of the values of the arguments 

            Inputs:
                ilist : list of integers

            Output:
                list of [2**arg[0],2**arg[1],...]
            """

            # initialise list
            olist = []

            # loop over the arg list
            for i in ilist:
                # append the 2**i value
                olist.append(2**i)
            # return the list
            return olist

'''
print(msg)

def power_of_2(ilist):
    """return a list of 2 raised to the power of the values of the arguments 

    Inputs:
        ilist : list of integers

    Output:
        list of [2**arg[0],2**arg[1],...]
    """

    # initialise list
    olist = []

    # loop over the arg list
    for i in ilist:
        # append the 2**i value
        olist.append(2**i)
    # return the list
    return olist
msg = '''
* Test this function, inputting a list of integers from 0 to 4 inclusive
'''
print(msg)

ilist = [0,1,2,3,4]
olist = power_of_2(ilist)
print(f'inputs:    {ilist}\noutputs: ->{olist}')
```

    
    Consider the function:
    
            def power_of_2(ilist):
                """return a list of 2 to the power of the values of the arguments 
    
                Inputs:
                    ilist : list of integers
    
                Output:
                    list of [2**arg[0],2**arg[1],...]
                """
    
                # initialise list
                olist = []
    
                # loop over the arg list
                for i in ilist:
                    # append the 2**i value
                    olist.append(2**i)
                # return the list
                return olist
    
    
    
    * Test this function, inputting a list of integers from 0 to 4 inclusive
    
    inputs:    [0, 1, 2, 3, 4]
    outputs: ->[1, 2, 4, 8, 16]



```python
msg='''
* Write a more Pythonic version of this, 
  making use of list comprehensions and lambda functions
'''
print(msg)

# lambda function
twop = lambda x : 2**x

ilist = [0,1,2,3,4]
# list comp using lambda
olist = [twop(i) for i in ilist]
print(f'inputs:    {ilist}\noutputs: ->{olist}')
```

    
    * Write a more Pythonic version of this, 
      making use of list comprehensions and lambda functions
    
    inputs:    [0, 1, 2, 3, 4]
    outputs: ->[1, 2, 4, 8, 16]



```python
# ANSWER

# probably a map function is most appropriate here
# with a lambda function to define the 2**x

ilist = [1,2,3,4]

print(f'2**{ilist} = {list(map(lambda x: 2**x,ilist))}')

## but a list comprehension would do very well too
print(f'2**{ilist} = {[2**x for x in ilist]}')
```

    2**[1, 2, 3, 4] = [2, 4, 8, 16]
    2**[1, 2, 3, 4] = [2, 4, 8, 16]

