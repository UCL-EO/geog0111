# 003 Help

## Introduction

### Purpose

In this notebook, we will learn how to get useful information on python commands using `help()` and associated methods.

We will use `help(list)` as an example to learn about the class `list` from the help material. You are not expected to learn everything about `lists` here, as we will return to it later in the course. But you should find this useful in learning how to learn.

We will learn how completion can help us understand our options.

We will learn how to access some on-line resources.

### Prerequisites

You will need some understanding of the following:

* [001 Using Notebooks](001_Notebook_use.md)


### Timing

The session should take around 20 minutes.

## Help Method

### help()

You can get help on an object using the `help()` method. This will return a full manual page of the class documentation. You need to gain some experience in reading these and understanding some of the terminology. 



```python
#the method help()
help(list.append)
```

    Help on method_descriptor:
    
    append(self, object, /)
        Append object to the end of the list.
    


#### Exercise 1

* In a new code cell, type `help(list)` and look through the information provided.

You need to have some practice in interpreting this sort of information.



Scanning the above, we notice for example:

* `list` is a class in python
* It has some methods such as `append(self, object, /)` and `clear(self, /)`.

We now create two object instances of a list class:


```python
alist = [1, 2, 3]
blist = [4, 5, 6]
```

and apply methods we see in the Help documentation, here: `append()` and `clear()`:


```python
alist = [1, 2, 3]
blist = [4, 5, 6]

# append blist as the last element of alist
alist.append(blist)
print('alist =', alist)

# clear blist
blist.clear()
print('blist =', blist)
```

    alist = [1, 2, 3, [4, 5, 6]]
    blist = []


#### Exercise 2

* Read through the help information for list, above.
* In a new cell, create lists called `alist` and `blist`:

        alist = ['one','three','two']
        blist = ['four','six','zero']
    
* print the lists with:

        print(alist,blist)
    
Using the help information, work out how to:

* extend `alist` with `blist` to create `['one','three','two','four','six','zero']`. N.B. This is not quite the same as our use of `append()` above.
* sort the new `alist` into **alpabetical order** and print the results


## online help

Not surprisingly, there is lots of help online. A key resource is [www.python.org](https://www.python.org/). Another useful one is [www.w3schools.com/python](https://www.w3schools.com/python):

* [list](https://www.w3schools.com/python/python_ref_list.asp)
* [list sort](https://www.w3schools.com/python/ref_list_sort.asp)
* [list sort: try it yourself](https://www.w3schools.com/python/trypython.asp?filename=demo_ref_list_sort)

A useful forum you can search for help on coding problems is [https://stackoverflow.com](https://stackoverflow.com), for example [https://stackoverflow.com/search?q=help+on+python+lists](https://stackoverflow.com/search?q=help+on+python+lists), but not all posts are equally useful: pay attention to comments from other users on any answer, as well as post votes. Do not look on `stackoverflow` until you have exhausted simpler help methods.

## help?

You can get a shorter set of basic help by putting `?` after the object. 

In a notebook, this will show in a new window at the bottom of the book. You can get rid of this by clicking the `x`.


```python
list?
```

## `dir()` and `locals()`

### `dir`

We can use the function `dir` to get a list of attributes for some class. 


```python
help(dir)
```

    Help on built-in function dir in module builtins:
    
    dir(...)
        dir([object]) -> list of strings
        
        If called without an argument, return the names in the current scope.
        Else, return an alphabetized list of names comprising (some of) the attributes
        of the given object, and of attributes reachable from it.
        If the object supplies a method named __dir__, it will be used; otherwise
        the default dir() logic is used and returns:
          for a module object: the module's attributes.
          for a class object:  its attributes, and recursively the attributes
            of its bases.
          for any other object: its attributes, its class's attributes, and
            recursively the attributes of its class's base classes.
    


If we use `dir()` with no arguments, we will see a list of the names of variables defined in this notebook:


```python
print(dir())
```

    ['In', 'Out', '_', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_i', '_i1', '_i2', '_i3', '_i4', '_i5', '_i6', '_i7', '_i8', '_ih', '_ii', '_iii', '_oh', 'alist', 'blist', 'exit', 'get_ipython', 'json', 'quit', 'yapf_reformat']


You might notice that we see the variable names `alist` and `blist` in here, as we created them in an earlier cell.

### `locals()`

The function `locals()` is similar to `dir()` used as above, but it contains the *values* that the variables are set to. So, we recall that there is a variable with the name `alist` from above.



```python
help(locals)
```

    Help on built-in function locals in module builtins:
    
    locals()
        Return a dictionary containing the current scope's local variables.
        
        NOTE: Whether or not updates to this dictionary will affect name lookups in
        the local scope and vice-versa is *implementation dependent* and not
        covered by any backwards compatibility guarantees.
    


We could of course just print this as above via:


```python
print(alist)
```

    ['four', 'one', 'six', 'three', 'two', 'zero']


but sometimes, we want to access the variable through its name `alias`. In this case, we can type:


```python
print(locals()['alist'])
```

    ['four', 'one', 'six', 'three', 'two', 'zero']


Use of `dir()` and `locals()` in this way can be very useful if you want to see what variables have been set to.

#### Exercise 3

* Create a code cell below and assign the variable `my_var` the value of `10` (hint: `my_var = 10`)
* Run `dir()` again and confirm that `my_var` now appears in the list


#### Exercise 4

* Print the value of `my_var` using `print(my_var)`
* Print the value of `my_var` using `print(locals()['my_var'])`
* confirm that they give the same answer

## Completion


### `dir(list)`

If we type `dir(list)` you will see that it gives the list of methods we can use for the class `list`. You should notice that this is the same as the list of methods we saw when we used `help(list)`:


```python
print(dir(list))
```

    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


### Completion

Another useful thing is to see a list of potential methods in a class or e.g. to know what variables already declared start with `f`.

Modern editors, [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment) and related tools often have features for completion of filenames, variables etc. This can help you minimise typing errors (especially for variables), and also help you to keep track of filenames, functions etc.

The Jupyter notebooks we are using have this sort of completion feature. Exactly how it works depends on the browser and the server used, but it will usually involve using the `<TAB>` key (either once or twice), and/or spacebar and/or hovering over the text.

The information this gives is similar to what youy get using `dir` as above.

Try this out now, broadly following the guidelines below. Note down what works for you and get used to using it.

If you are using a jupyter hub server (or similar), copy the information in the cell below.
Then place the cursor after the `.` below. hit the <tab> key, rather than <return> in this cell.

    # Dont run this cell: use for completion
    list.

Really, this is just using the fact that `<tab>` key performs variable name completion.

This means that if you e.g. have variables called `the_long_one` and `the_long_two` set:


```python
the_long_one = 1
the_long_two = 2
```

The next time you want to refer to this string in code, you need only type as many letters needed to distinguish this from other variable names, then hit `<tab>` to complete the name as far as possible.


* copy the information in the cell below into a new code cell
* place the cursor after the letter t and hit `<tab>`. It should show you a list of things that begin with `t`. 
* Use this to write the line of code `the_long_one = 1000`
* in the cell below, place the cursor after the letters `th` and hit `<tab>`. It should show you a list of things that begin with `th`. In this case it should just give you the options of `the_long_one` or `the_long_two`. 
* If you hit `<tab>` again, the variable name will be completed as far as it can, here, up to `the_long_`. Use this to write the line of code `the_long_two = 2000`

    # do exercise here ... put the cursor after the t or th and
    # use <tab> for completion. Dont run this cell
    t
    th

### Learning new things

Let's use that knowledge to learn something new:

* Use online material from [https://www.w3schools.com](https://www.w3schools.com/python) or elsewhere to learn the basics of `for` loops.

#### Exercise 5

* Find help for the class `range` to understand how to use this to generate a sequence of integers from 10 to 1 in steps of -1
* Use what you have learned to write a `for` loop below that counts backwards from 10 to 0

## Summary

In this session, we  have learned some different ways to access help on the operation and options for python commands. These include: `help()`, use of `?`, completion, and using online help. Practically, you may use one or more of these methods to find out how something works, or get some examples. 

You might notice that there are many online forums you can post to to get advice on coding, and we mention  [https://stackoverflow.com](https://stackoverflow.com) as an example. Remember that not all posts are equally useful: pay attention to comments from other users on any answer, as well as post votes. Do not look on `stackoverflow` until you have exhausted simpler help methods. You should *not* generally be posting on these in this course. You will find answers to all that you need in these notes or on existing online pages. You most certainly must *not* post on forums asking questions about anyt exercises you need to complete or work you need to submit. The course administrators may monitor this

