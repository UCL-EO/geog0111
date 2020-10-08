# 014 Groups : Answers to exercises

#### Exercise 1

* create a tuple called `t` that contains the integers `1` to `5` inclusive
* print out the value of `t`
* use the tuple to set variables `a1`,`a2`,`a3`,`a4`,`a5`
* print  `a1`,`a2`,`a3`,`a4`,`a5`


```python
# ANSWER
# create a tuple called t that contains the integers 1 to 5 inclusive
t = (1,2,3,4,5)

# print out the value of t
print(t)

# use the tuple to set variables a1,a2,a3,a4,a5
a1,a2,a3,a4,a5 = t
print(a1,a2,a3,a4,a5)
```

    (1, 2, 3, 4, 5)
    1 2 3 4 5


#### Exercise 2

* copy the code to a new code block below, and test that this works with lists, as well as tuples


```python
# ANSWER

# copy the code to the block below, and test that this works with lists, as well as tuples

# use tuple
l0 = (2,8,4,32,16)

# print the index of the item integer 4 
# in the tuple / list

item_number = 4

# Note the dot . here
# as index is a method of the class list
ind  = l0.index(item_number)

# notice that this is different
# as len() is not a list method, but 
# does operatate on lists/tuples
# Note: do not use len as a variable name!
llen = len(l0)

print(f'the index of {item_number} in {l0} is {ind}')
print(f'the length of the {type(l0)} {l0} is {llen}')
```

    the index of 4 in (2, 8, 4, 32, 16) is 2
    the length of the <class 'tuple'> (2, 8, 4, 32, 16) is 5


#### Exercise 3

* set a list called `l0` with `l0 = [2,8,4,32,16]`
* find the index of the integer 16 in the tuple/list
* what is the index of the first item?
* what is the length of the tuple/list?
* what is the index of the last item?


```python
# ANSWER

# set a list called l0 with l0 = [2,8,4,32,16]
l0 = [2,8,4,32,16]

# find the index of the integer 16 in the tuple/list
value = 16
print(f'index of {value} in {l0} is {l0.index(value)}')

# what is the index of the first item?
value = l0[0]
print(f'index of {value} in {l0} is {l0.index(value)}')

# what is the length of the tuple/list?
print(f'length of {l0} is {len(l0)}')

# what is the index of the last item?
last_item = len(l0) - 1
value = l0[last_item]
print(f'index of {value} in {l0} is {l0.index(value)}')

# or simply use -1l, rememberimg that we can index -ve
value = l0[-1]
print(f'index of {value} in {l0} is {l0.index(value)}')
```

    index of 16 in [2, 8, 4, 32, 16] is 4
    index of 2 in [2, 8, 4, 32, 16] is 0
    length of [2, 8, 4, 32, 16] is 5
    index of 16 in [2, 8, 4, 32, 16] is 4
    index of 16 in [2, 8, 4, 32, 16] is 4


#### Exercise 4

* set a list called `l0` with `l0 = [2,8,4,32,16]`
* find the index of `16` in this list
* use this insert the number `128` between the entries for `32` and `16`
* take a copy of `l0`, call it `l0_test` and insert the string `'hello world'` at index `-2`
* what positive index number could we have used in place of `-2` here?
* why?


```python
# ANSWER

# set a list called `l0` with `l0 = [2,8,4,32,16]`
l0 = [2,8,4,32,16]


# find the index of `16` in this list
index_16 = l0.index(16)

# insert the number `128` between the entries for `32` and `16`
l0.insert(index_16,128)
print(l0)

# take a copy of `l0`, call it `l0_test` 
# and insert the string `'hello world'` at index `-2`
l1 = l0.copy()
l1.insert(-2,'hello world')
print(l1)

# what positive index number could we have used in place of `-2` here
# the answer is 4
l1 = l0.copy()
l1.insert(4,'hello world')
print(l1)

# why?
msg = '''
since the length of l0 is 6 (when we copy it)
then -2 corresponds to the +ve index 6-2 = 4
'''
print(msg)
```

    [2, 8, 4, 32, 128, 16]
    [2, 8, 4, 32, 'hello world', 128, 16]
    [2, 8, 4, 32, 'hello world', 128, 16]
    
    since the length of l0 is 6 (when we copy it)
    then -2 corresponds to the +ve index 6-2 = 4
    

