# 005 Help

## Introduction

### Purpose

In this notebook, we will learn how to get useful information on python commands using `help()` and associated methods.

We will use `help(list)` as an example to learn about the class `list` from the help material. You are not expected to learn everything about `lists` here, as we will return to it later in the course. But you should find this useful in learning how to learn.

We will learn how completion can help us understand our options.

We will learn how to access some on-line resources.

### Prerequisites

You will need some understanding of the following:

* [001 Using Notebooks](001_Notebook_use.md)


We will use some technical vocabulary that you should familiarize yourself: 

* [functions and method](https://www.tutorialspoint.com/difference-between-method-and-function-in-python)
* [list](https://www.w3schools.com/python/python_lists.asp)
* [class](https://docs.python.org/3/tutorial/classes.html)
* [in place](https://www.geeksforgeeks.org/inplace-vs-standard-operators-python/)
* [Completion](#Completion)

### Timing

The session should take around 30 minutes.

## Help Method

### help()

You can get help on an object using the `help()` method. This will return a full manual page of the class documentation. You need to gain some experience in reading these and understanding some of the terminology. 



```python
#the method help()
help(list)
```

    Help on class list in module builtins:
    
    class list(object)
     |  list(iterable=(), /)
     |  
     |  Built-in mutable sequence.
     |  
     |  If no argument is given, the constructor creates a new empty list.
     |  The argument must be an iterable if specified.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |  
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(self, /)
     |      Return a reverse iterator over the list.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(self, /)
     |      Return the size of the list in memory, in bytes.
     |  
     |  append(self, object, /)
     |      Append object to the end of the list.
     |  
     |  clear(self, /)
     |      Remove all items from list.
     |  
     |  copy(self, /)
     |      Return a shallow copy of the list.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  extend(self, iterable, /)
     |      Extend list by appending elements from the iterable.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  insert(self, index, object, /)
     |      Insert object before index.
     |  
     |  pop(self, index=-1, /)
     |      Remove and return item at index (default last).
     |      
     |      Raises IndexError if list is empty or index is out of range.
     |  
     |  remove(self, value, /)
     |      Remove first occurrence of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  reverse(self, /)
     |      Reverse *IN PLACE*.
     |  
     |  sort(self, /, *, key=None, reverse=False)
     |      Stable sort *IN PLACE*.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    


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


#### Exercise

* Read through the help information for list, above.
* In a new cell, create lists called `alist` and `blist`:

        alist = ['one','three','two']
        blist = ['four','six','zero']
    
* print the lists with:

        print(alist,blist)
    
Using the help information, work out how to:

* extend `alist` with `blist` to create `['one','three','two','four','six','zero']`. N.B. This is not quite the same as our use of `append()` above.
* sort the new `alist` into **alpabetical order** and print the results


You may have noticed that the help (e.g. for `sort()` mentions [`IN PLACE`](https://www.geeksforgeeks.org/inplace-vs-standard-operators-python/) in the help information. This means that the operation affects the contents of the variable. So, a standard operation would be e.g.:

    alist = ['one','three','two']
    blist = ['four','six','zero']

    c = alist + blist
    print(alist)
    
where the results from the `+` operation is returned, and the contents of `c` set to this.

We can demonstrate the effect of `IN PLACE` with the following examples:


```python
# NOT In-Place (standard)
alist = ['one','three','two']
blist = ['four','six','zero']

clist = alist + blist
print(clist)
```

    ['one', 'three', 'two', 'four', 'six', 'zero']



For in-place, e.g. list `alist.extend()`, the contents of `alist` are altered:


```python
# In-Place:
alist = ['one','three','two']
blist = ['four','six','zero']

alist.extend(blist)
print(alist)
```

    ['one', 'three', 'two', 'four', 'six', 'zero']


#### Exercise

* Create a code cell below
* Create a variable called `alist` containing a list of numbers (not in order)
* Print `alist`
* Create a variable called `blist` containing another list of numbers (not in order)
* Print `blist`
* Join the list `blist` to `alist` using the in-place method `.extend()`
* Print `alist`
* reverse `alist` 
* print alist
* What advantages and disadvantages do you think in-place methods have?

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

    ['In', 'Out', '_', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_i', '_i1', '_i10', '_i2', '_i3', '_i4', '_i5', '_i6', '_i7', '_i8', '_i9', '_ih', '_ii', '_iii', '_oh', 'alist', 'blist', 'clist', 'exit', 'get_ipython', 'info', 'quit']


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

    [-1, 0, 2, 1, 7, -3, 5, 4]


but sometimes, we want to access the variable through its name `alias`. In this case, we can type:


```python
print(locals()['alist'])
```

    [-1, 0, 2, 1, 7, -3, 5, 4]


Use of `dir()` and `locals()` in this way can be very useful if you want to see what variables have been set to.

#### Exercise

* Create a code cell below and assign the variable `my_var` the value of `10` (hint: `my_var = 10`)
* Run `dir()` again and confirm that `my_var` now appears in the list


#### Exercise

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

If you are using a jupyter hub server (or similar)

      place the cursor after the `.` below
      hit the <tab> key, rather than <return> in this cell
      Dont run this cell


```python
# Dont run this cell
list.
```


      File "<ipython-input-17-76fc35eb1242>", line 2
        list.
             ^
    SyntaxError: invalid syntax



Really, this is just using the fact that `<tab>` key performs variable name completion.

This means that if you e.g. have variables called `the_long_one` and `the_long_two` set:


```python
the_long_one = 1
the_long_two = 2
```

The next time you want to refer to this string in code, you need only type as many letters needed to distinguish this from other variable names, then hit `<tab>` to complete the name as far as possible.

#### Exercise

* in the cell below, place the cursor after the letter t and hit `<tab>`. It should show you a list of things that begin with `t`. 
* Use this to write the line of code `the_long_one = 1000`
* in the cell below, place the cursor after the letters `th` and hit `<tab>`. It should show you a list of things that begin with `th`. In this case it should just give you the options of `the_long_one` or `the_long_two`. 
* If you hit `<tab>` again, the variable name will be completed as far as it can, here, up to `the_long_`. Use this to write the line of code `the_long_two = 2000`


```python
# do exercise here ... put the cursor after the t or th and
# use <tab> for completion. Dont run this cell
t
th
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-4003a56208cf> in <module>
          1 # do exercise here ... put the cursor after the t or th and
          2 # use <tab> for completion. Dont run this cell
    ----> 3 t
          4 th


    NameError: name 't' is not defined


### Learning new things

Let's use that knowledge to learn something new:

* Use online material from [https://www.w3schools.com](https://www.w3schools.com/python) or elsewhere to learn the basics of `for` loops.

#### Exercise

* Find help for the class `range` to understand how to use this to generate a sequence of integers from 10 to 1 in steps of -1
* Use what you have learned to write a `for` loop below that counts backwards from 10 to 0

## Summary

In this session, we  have learned some different ways to access help on the operation and options for python commands. These include: `help()`, use of `?`, completion, and using online help. Practically, you may use one or more of these methods to find out how something works, or get some examples. 

You might notice that there are many online forums you can post to to get advice on coding, and we mention  [https://stackoverflow.com](https://stackoverflow.com) as an example. Remember that not all posts are equally useful: pay attention to comments from other users on any answer, as well as post votes. Do not look on `stackoverflow` until you have exhausted simpler help methods. You should *not* generally be posting on these in this course. You will find answers to all that you need in these notes or on existing online pages. You most certainly must *not* post on forums asking questions about anyt exercises you need to complete or work you need to submit. The course administrators may monitor this

