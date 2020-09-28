# 003 Help : Answers to exercises

#### Exercise 1

* In a new code cell, type `help(list)` and look through the information provided.


```python
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


### Learning new things

Let's use that knowledge to learn something new:

* Use online material from [https://www.w3schools.com](https://www.w3schools.com/python) or elsewhere to learn the basics of `for` loops.

#### Exercise 3

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

