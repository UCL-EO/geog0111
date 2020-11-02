# 017 Functions in Python

## Introduction

### Purpose

In this session, we will learn about Functions in Python. In essence, a function allows us to write better, more compact and re-usable code. This is a concept we will use a lot in later sessions, so make sure you fully familiarise yourself with the material.


### Prerequisites

You will need some understanding of the following:

* [001 Using Notebooks](001_Notebook_use.md)
* [003 Getting help](003_Help.md)
* [010 Variables, comments and print()](010_Python_Introduction.md)
* [011 Data types](011_Python_data_types.md) 
* [012 String formatting](012_Python_strings.md)
* [013_Python_string_methods](013_Python_string_methods.md)
* [014_Python_groups](014_Python_groups.md)
* [015_Python_control](015_Python_control.md)
* [016_Python_for](016_Python_for.md)

In particular, you will need to recall how to use:

   - [`assert`](016_Python_for.md#looping-over-dictionaries,-and-assert)
   - [`str.join()`](013_Python_string_methods.md#split()-and-join())
   - [`zip`](014_Python_groups.md#dict)


## Introduction to Functions

A [function](https://docs.python.org/3/glossary.html#term-function) is a block of code statements that we can use to carry out a specific purpose. 


The simplest form of function has no inputs or outputs, but simply performs some task when we call it:

![function](images/no_in_out.png)


An example of a simple function in Python is:


```python
def hello_world():
    '''
    Purpose:
      print the string 'hello world'
    '''
    print('hello world')
```

This is designed to print the string `hello world` when we call it.

Notice the formatting here: the function is declared:

    def hello_world():

and the *contents* of the function are indented in (by 4 spaces here).

We use the function in Python code as:


```python
hello_world()
```

    hello world


and access the function document string by:


```python
help(hello_world)
```

    Help on function hello_world in module __main__:
    
    hello_world()
        Purpose:
          print the string 'hello world'
    


### Exercise 1

* in a new code cell below, write a function called `my_name` that prints your name
* demonstrate that your code works (i.e. run it in a code cell)
* show the doc string using `help()` 

**Advice**: make sure it has an appropriate document string, based on the example in the notes, and also check that you have the indentation correct for the code in the function. Notice the semicolon `:` at the end of the `def` statement.

## Function specification


More generally, we could think of the the function as **a sort of filter**: it takes some **inputs** (specified in the arguments), makes some calculation based on these, i.e. that is a *function* of these inputs, and returns an **output**.

![function](images/in_out.png)



In this sense:

 * It will generally have one or more [arguments](https://docs.python.org/3/glossary.html#argument): `(arg1, arg2, ...)` that form the **inputs**.
 * It will often return some value (or set of values) as the **output**: `retval`
 * It will have a name: `my_function`

![function io](images/im_funct.png)

### Anatomy of a function

The format of a function in Python is:

    def my_function(arg1,arg2,...):
      '''
      Document string 
      '''

      # comments

      retval =  ... 

      # return
      return retval
      
The keyword `def` defines a function, followed by the function name, a list (actually, a [`tuple`](https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple)) of arguments, then a semicolon `:`.

The contents of the function are indented to a consistent level of spaces.

The function will typically have a document string, generally a multi-line string defined within triple quotes. We use this to document information about the function, such as its author, purpose, and inputs and outputs.

Within the function, we can refer to the arguments (`arg1` and `arg2` here, though they will generally have more meaningful names), make some calculation based on these, and generally, return some value (`retval` here).

### Code design 

This idea of a *filter* can be useful when thinking how to design a function. We can see that we need to define:

    * purpose
    * inputs
    * output

Let's suppose we need to design a function that will take a first name and last name, and combine them into your full name (assuming for now that you have two names).

The *purpose* of our function could be stated as:

    purpose: 
    
        generate a name string from list of strings
    
The inputs could be:

    inputs:
      - name_list : list of names
      
And the output:

    return:
      - the full name
      
Without knowing any real coding then, we could develop the template for this function, along with an initial document string. 

We do need to give the function a name, so let's use `full_name` here.

We have started with the idea of some purpose for our code, then defined what the expected inputs and outputs would be. We can call coding at that level of generalisation [pseudocode](https://en.wikipedia.org/wiki/Pseudocode). We could have written our task is a form of pseudocode such as:

    algorithm full_name is
        input: List of strings in variable name_list
        output: string in variable retval

        purpose: generate a name string from list of strings 
        
        # CODE BLOCK to achieve aim (NOT DONE)
        # test by passing input to output
        retval = name_list
        
 where we have left the `CODE BLOCK` blank at the moment, and replaced it by simply sending the function input to the output so we can test the code structure. It can be of value when designing codes to first develop some pseudocode such as above, but in reality such statements are very closely related to what we would write in high-level codes like Python:


```python
def full_name(name_list):
    '''
    
    purpose: 
      generate a name string from list of strings 

    inputs:
    - name_list : list of names

    return:
    - the full name
    '''
    # CODE BLOCK to achieve aim (NOT DONE)
    # test by passing input to output
    retval = name_list

    # return
    return retval
```

That's a good start, and it allows us to develop a function that we can run and test. 

To test, we can set a list of example strings. We then *call* the function `full_name()` with this argument, and set the value returned in the variable `full`.


```python
names = ['Fred','Bloggs']

full = full_name(names)
print(full)
```

    ['Fred', 'Bloggs']


From our test, we can see that the function doesn't yet achieve what we wanted: it simply returns the input list, rather than the full name.

To proceed, we need to know how to make a combined string. It can be useful to test our understanding of the code we will need to achieve the aim of the function. We do not need to do that inside the function, but can instead try to think of some examples we could use to test the ideas.

One way to achieve the aim of the function this would be to use the string [`join`](https://docs.python.org/3/library/stdtypes.html#str.join) operation that we came across the in [Python string methods](013_Python_string_methods.md#split()-and-join()) notes.

This works by placing a key string between string items in a list. For example, if we want to separate strings by `:`, we would use:

    ':'.join(names)


```python
':'.join(names)
```




    'Fred:Bloggs'



In our function, we want to use a single 'whitespace' value, so `' '` as the key:


```python
' '.join(names)
```




    'Fred Bloggs'



Now we are sure of the coding concept to achieve what we want in the filter, we can write the function:


```python
def full_name(name_list):
    '''
    
    purpose: 
      generate a name string from list of strings 

    inputs:
    - name_list : list of names

    return:
    - the full name
    '''
    # join the names in name_list together
    retval = ' '.join(name_list)

    # return
    return retval
```

we try to make the docstring useful and test what it shows:


```python
help(full_name)
```

    Help on function full_name in module __main__:
    
    full_name(name_list)
        purpose: 
          generate a name string from list of strings 
        
        inputs:
        - name_list : list of names
        
        return:
        - the full name
    


then run our code:


```python
full = full_name(['Fred','Bloggs'])
print(full)
```

    Fred Bloggs


## Test 

It is a good idea if we can write a test for our function. This should cover some typical case or cases, and check that we get the correct output for a particular input. We can use the [assert](https://www.w3schools.com/python/ref_keyword_assert.asp) method that we have seen in the [Python for](016_Python_for.md#looping-over-dictionaries,-and-assert) notes:

    assert True

For example:


```python
assert full_name(['Fred','Bloggs']) == "Fred Bloggs"
print('test passed')
```

    test passed


remember that if this assertion fails, we get an `AssertionError` (you can try that out by putting something incorrect in the assertion above and re-running the cell). If the error is raised, our code will strop running and report the error.  

We will learn more about code testing later, but for the moment, we suggest that you use one or more `assert` statements that try out different inputs-output matches with your function. 

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

## More on arguments

Python functions can take [two types of arguments](https://book.pythontips.com/en/latest/args_and_kwargs.html):

* positional arguments
* keyword arguments

### Positional arguments

The arguments we have used above are positional arguments, in that their definition in the function depends on the order they are specified in. For example:


```python
def hello(s1,s2):
    '''
    Purpose:
      print out positional arguments
      
    Inputs:
      s1 : first argument
      s2 : secopnd argument
    '''
    print(f'argument 0 is {s1}')
    print(f'argument 1 is {s2}')
    
hello('hello','world')
```

    argument 0 is hello
    argument 1 is world


Sometimes in Python documentation, you will see the arguments specified simply as:

    example(*args, **kwargs)
    
This is the most general way of specifying function arguments. The first item in this case `*args` are the positional arguments. Although we generally specify them explicitly as above, we can also use

    *args
    
to specify them, where `args` is a list-like object. In this form, the example above becomes:




```python
def hello(*args):
    '''
    print out positional arguments
    
    Inputs:
        *args : list of positional arguments
    '''
    # loop over the list
    for i,s in enumerate(args):
        print(f'argument {i} is {s}')
    
hello('hello','world','again')
```

    argument 0 is hello
    argument 1 is world
    argument 2 is again



```python
# or using *args where args is a list
l = ['hello','world','again','as','list']
hello(*l)
```

    argument 0 is hello
    argument 1 is world
    argument 2 is again
    argument 3 is as
    argument 4 is list


In this example, we have not specified how many positional arguments there are, but obviously we need to attach some meaning to each of them in the order supplied. Sometimes this is useful in code, where we just want to loop over a list of arguments, but you should mostly be wary about using it unless you really need to. 

A good example of the use of `*args` is the `print()` statement. It will print out however many positional arguments we specify:


```python
print('hello','world','again')

l = ['hello','world','again','as','list']
# print the list, specifying l as a single positional argument
print(l)
# print the list passing each list item as a positional argument
print(*l)
```

    hello world again
    ['hello', 'world', 'again', 'as', 'list']
    hello world again as list


### Keyword arguments

The second type of argument we mentioned above was keyword arguments. These are typically used to modify the behaviour of a function are are of the form:

    verbose=True
    sep=' '


We can see examples of these with the `print` function:


```python
help(print)
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    


where a set of optional keyword arguments are specified. All keyword arguments are specified with a default value (`sep=' ', end='\n', file=sys.stdout, flush=False` above). If we do not specify a keyword when we call the function, this is the value that that variable will take within the function.

Note that keywords must be specified **after** positional arguments. The keywords can be in any order (they are not positional). Keywords can only be given once.

But, if we want, we can override the defaults by setting the keyword when we call the function:


```python
l = ['hello','world','again','as','list']
# print the list passing each list item as a positional argument
# default with sep as ' '
print(*l)
# with sep as 'X'
print(*l,sep='X')
# with sep as ':'
print(*l,sep=':')
```

    hello world again as list
    helloXworldXagainXasXlist
    hello:world:again:as:list


This is a very useful feature for functions: we can set default behaviour, but the user can modify this when they call the function. 

For example, let's add a `verbose` keyword to our `hello()` function. The behaviour we want is that if the verbose flag is set, we print lots of information to the user. In this case:

    print(f'argument {i}:',end=' ')
    
which will print the index `i`. We have used the `kwarg` `end=''` for `print()` so that if this is called, it does not print a newline, but a space instead.


```python
def hello(*args,verbose=False):
    '''
    print out positional arguments
    
    Inputs:
        *args : list of positional arguments
        
    Optional keyword arguments:
        verbose : print the index 
    '''
    # loop over the list
    for i,s in enumerate(args):
        # if the verbose flag is set
        # then print detailed information
        if verbose:
            print(f'argument {i}:',end=' ')
        print(f'{s}')

```


```python
dash='='*5

# call without verbose
print(f'{dash} verbose=False {dash}')
hello('hello','world','again')

# call with verbose
print(f'{dash} verbose=True {dash}')
hello('hello','world','again',verbose=True)
```

    ===== verbose=False =====
    hello
    world
    again
    ===== verbose=True =====
    argument 0: hello
    argument 1: world
    argument 2: again


### Exercise 3

* Starting from the function `list2dict(keys,values)` that you developed above, add keyword arguments to the code to achieve the following:
     - if check=True   : perform checks on the input data
     - if verbose=True : print out information on what is going on in the function
     - set all default keywords to False
* Make sure you perform tests as above, and that you update document strings

As a final point of `kwargs`, you might still be wondering why this was specified as:

       example(*args,**kwargs)
       
above. We have seen what the `*args` part means: if `args` is a list, then each item in the list is passed as a positional argument. The same idea applies to `**kwargs` but instead of a list, `kwargs` refers to a dictionary. If you think about the information you need to pass for keword arguments, you would understand why this is the case. 

By using `**kwargs`, where `kwargs` is a dictionary, the key-value pairs in the dictionary are passed as `key=value`. For example:


```python
args = ['hello','world','again','as','list']
# set up dictionary for kwargs
# with X as sep and a string at the end oif the line
kwargs = {'sep' : 'X', 'end' : '<- end of the line\n'}

print(*args,**kwargs)
```

    helloXworldXagainXasXlist<- end of the line


The use of `**kwargs` can be useful sometimes, as you can more easily keep track of keywords for some particular configuration of running a code. For that reason, and because you will see it sometimes in documentation, you should be aware of it. Most likely you won't be using it a lot in your early code development though.

## `lambda` functions

Sometimes the function we want to write is very simple, and might consist of only a few statements on a single line. As an example, consider the function `y(x)` here:


```python
def y(x):
    '''
    a function y(x) with
    zeros at x=4,x=3
    '''
    return 2.0*(x-3)*(x-4)
```

Whilst it is fine to write a function in this way, and it has the advantage of being quite explicit about what it is doing, it is not very efficient: there is a computational cost to calling a function, especially in a high-level language like Python. 

If we were only ever going to use this function in places in the code where performance is unimportant, then we can go ahead with the above.

If we are worried that it might be used in a case when we would not want to slow it down unnecessarily with as function call, we can use a special type of function, called a [`lambda` function](https://www.w3schools.com/python/python_lambda.asp). The syntax is:

        function_name = lambda args : function_code

where `function_name` is the name of the function, `args` is a list of arguments, and `function_code` here represents the (short!) code inside the function.

Our example above translates to:


```python
y = lambda x : 2.0*(x-3)*(x-4)
```

which is a much *neater* and more efficient code than a full function. Use these when appropriate.

Generally, you are not expected to use a docstring with a `lambda` function, as it should be a simple statement that is self-evident from the code. If you do feel the need, you can add one with:

        y.__doc__ = '''
        a function y(x) with
        zeros at x=4,x=3
        '''


#### Exercise 4

Consider the function:


        def power_of_2(ilist):
            """
            output a list of 2 raised to the power of 
            the values of the input arguments 

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
* Write a more Pythonic version of this, making use of list comprehensions and `lambda` functions

## Summary

In this section, we have learned about writing a function. We have seen that they generally will have zero or more input positional arguments and zero or more keyword arguments. They will typically return some value. We have also seen how we can define a `doc string` to give the user information on how to use the function, and also how we can use `assert` to build tests for our codes. We have been through some design considerations, and seen that it is best to plan you functions by thinking about the purpose, the inputs and the outputs. Then, for the core code, you just need to develop a skeleton code and docstring structure, test that, and insert your core code. You should think about modifications using keyword arguments that you might want to include, but these will often come in a second pass of development.

When we write Python codes from now on, we will often make use of functions.

Remember:

Anatomy of a function:

        def my_function(arg1,arg2,...,kw0=...,kw1=...):
          '''
          Document string 
          '''

          # comments

          retval =  ... 

          # return
          return retval


Also written as:

        def my_function(*args,**kwargs):

We have also seen `lambda` functions, used for short functions:

        function_name = lambda args : function_code

