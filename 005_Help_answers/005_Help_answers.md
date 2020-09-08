# 005 Help : Answers to exercises

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



```python
# ANSWERS
alist = ['one', 'three', 'two']
blist = ['four', 'six', 'zero']
print(alist, blist)

# join: 
# extend(self, iterable, /)
#      Extend list by appending elements from the iterable.
alist.extend(blist)
print("extended", alist)

# sort
# sort(self, /, *, key=None, reverse=False)
#       Stable sort *IN PLACE*.
alist.sort()
print("sorted", alist)
```

    ['one', 'three', 'two'] ['four', 'six', 'zero']
    extended ['one', 'three', 'two', 'four', 'six', 'zero']
    sorted ['four', 'one', 'six', 'three', 'two', 'zero']


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


```python
# ANSWERS
# Create a variable called `alist` containing a list of numbers (not in order)
alist = [4,5,-3,7]
# Print `alist`
print(alist)

# Create a variable called `blist` containing another list of numbers (not in order)
blist = [1,2,0,-1]
# Print `blist`
print(blist)

# Join the list `blist` to `alist` using the in-place method `.extend()`
alist.extend(blist)
# Print `alist`
print(alist)

# reverse `alist` 
alist.reverse()
# print alist
print(alist)

info='''
What advantages and disadvantages do you think in-place methods have?

 Using the in-place methods like sort and reverse are memory efficient:
 we do not need to create new variables with the result of the sorting
 or reverseing etc. 
 The downside is that you need to be careful when using them:
 Don't make the mistake of using the returned value as this
 will be 0 if the operation was successful.
 As an example, we might think that

    alist.sort().reverse()
 
 would work, but it wont, because alist.sort() returns 0
 then the second operation we attempt is 0.reverse() which
 is meaningless and will fail. Rather, we ust do:
    
    alist.sort()
    alist.reverse()

 as separate operations
 '''
print(info)
```

    [4, 5, -3, 7]
    [1, 2, 0, -1]
    [4, 5, -3, 7, 1, 2, 0, -1]
    [-1, 0, 2, 1, 7, -3, 5, 4]
    
    What advantages and disadvantages do you think in-place methods have?
    
     Using the in-place methods like sort and reverse are memory efficient:
     we do not need to create new variables with the result of the sorting
     or reverseing etc. 
     The downside is that you need to be careful when using them:
     Don't make the mistake of using the returned value as this
     will be 0 if the operation was successful.
     As an example, we might think that
    
        alist.sort().reverse()
     
     would work, but it wont, because alist.sort() returns 0
     then the second operation we attempt is 0.reverse() which
     is meaningless and will fail. Rather, we ust do:
        
        alist.sort()
        alist.reverse()
    
     as separate operations
     


#### Exercise

* Create a code cell below and assign the variable `my_var` the value of `10` (hint: `my_var = 10`)
* Run `dir()` again and confirm that `my_var` now appears in the list



```python
# ANSWER
# Create a code cell below and assign the variable my_var the value of 10 (hint: my_var = 10)
my_var = 10

# Run dir() again 
print(dir())

# confirm that my_var now appears in the list
msg = '''
I can see my_var in the list printed out
'''
print(msg)
```

    ['In', 'Out', '_', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_i', '_i1', '_i10', '_i11', '_i12', '_i13', '_i14', '_i2', '_i3', '_i4', '_i5', '_i6', '_i7', '_i8', '_i9', '_ih', '_ii', '_iii', '_oh', 'alist', 'blist', 'clist', 'exit', 'get_ipython', 'info', 'my_var', 'quit']
    
    I can see my_var in the list printed out
    


#### Exercise

* Print the value of `my_var` using `print(my_var)`
* Print the value of `my_var` using `print(locals()['my_var'])`
* confirm that they give the same answer


```python
# ANSWER
# Print the value of my_var using print(my_var)
print(my_var)

# Print the value of my_var using print(locals()['my_var'])
print(locals()['my_var'])

# confirm that they give the same answer
msg = '''
I can see they are the same
'''
print(msg)
```

    10
    10
    
    I can see they are the same
    


### Learning new things

Let's use that knowledge to learn something new:

* Use online material from [https://www.w3schools.com](https://www.w3schools.com/python) or elsewhere to learn the basics of `for` loops.

#### Exercise

* Find help for the class `range` to understand how to use this to generate a sequence of integers from 10 to 1 in steps of -1
* Use what you have learned to write a `for` loop below that counts backwards from 10 to 0


```python
# ANSWER
# Use what you have learned to write a 
# `for` loop below that counts backwards from 10 to 0

for i in range(10,0,-1):
    print(i)
```

    10
    9
    8
    7
    6
    5
    4
    3
    2
    1

