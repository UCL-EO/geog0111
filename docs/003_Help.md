# 003 Help

## Introduction

#### Purpose

In this notebook, we will learn how to get useful information on python commands using `help()` and associated methods.

We will use `help(list)` as an example to learn about the class `list` from the help material. You are not expected to learn everything about `lists` here, as we will return to it later in the course. But you should find this useful in learning how to learn.

We will learn how to access some on-line resources.

#### Prerequisites

You will need some understanding of the following:

* [001 Using Notebooks](001_Notebook_use.md)


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

### Learning new things

Let's use that knowledge to learn something new:

* Use online material from [https://www.w3schools.com](https://www.w3schools.com/python) or elsewhere to learn the basics of `for` loops.

#### Exercise 3

* Find help for the class `range` to understand how to use this to generate a sequence of integers from 10 to 1 in steps of -1
* Use what you have learned to write a `for` loop below that counts backwards from 10 to 0

## Summary

In this session, we  have learned some different ways to access help on the operation and options for python commands. These include: `help()`, use of `?` and using online help. Practically, you may use one or more of these methods to find out how something works, or get some examples. We have come across the following commands:


|  command | purpose  |   
|---|---|
| `help(m)`  |  print document string for method `m` |  
| `m?`  |  print short document string for method `m` |  


We have also touched upon the following commands in the exercises:


|  command | purpose  |   
|---|---|
| `list`  |  Python data type for lists |  
| `list.append()`  | append item to list  |   
| `list.clear()`  | clear item from list  |  
| `list.sort`  | in-line list sort  |  
| `range(start,stop,step)`  | list-like generator for integers from `start` to (but not including) `stop` in steps of `step`  |  





You might notice that there are many online forums you can post to to get advice on coding, and we mention  [https://stackoverflow.com](https://stackoverflow.com) as an example. Remember that not all posts are equally useful: pay attention to comments from other users on any answer, as well as post votes. Do not look on `stackoverflow` until you have exhausted simpler help methods. You should *not* generally be posting on these in this course. You will find answers to all that you need in these notes or on existing online pages. You most certainly must *not* post on forums asking questions about anyt exercises you need to complete or work you need to submit. The course administrators may monitor this.

### You should know how to get help on Python functions 

You should know how to learn about how to use a particular function, through reading the help information. Take notice of the formatting of this, as you will need to be writing your own help statements later in the course.

You should know how to use the Python function `range()` and understand teh basics of how to use the Python `list` data type.

If you are unsure of any of these, then try going over the material again, explore other resources you may find, and/or come to the Thursday help sessions and ask for help.
