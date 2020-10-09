# 016 More control in Python: `for` : Answers to exercises

#### Exercise 1

* generate a list of strings called `group` with the names of (some of) the items in your pocket or bag (or make some up!)
* set up a `for` loop with `group`, setting the variable `item`
* within the loop, print each value of item in turn
* at the end of the loop, print `I'm done`


```python
'''
# ANSWER 

for loop
'''
# generate a list of strings called `group` with the names 
# of (some of) the items in your pocket or bag (or make some up!)
group = ['keys','hat','💄','🌴']

# set up a `for` loop with `group`, 
# setting the variable `item`
for item in group:
    # within the loop, print 
    # each value of item in turn
    print(item)
    
# at the end of the loop, print done
# note the quote types
print("I'm done")
```

    keys
    hat
    💄
    🌴
    I'm done


#### Exercise 2

* copy the code above
* check to see if the value of `count` at the end of the loop is the same as the length of the list. 
* Why should this be so?


```python
'''
# ANSWER

for loop with enumeration
'''

# copy the code above
group = ['cat', 'fish', '🦄', 'house']

# Before we enter the loop, we initialise the `count` to zero.
count = 0

for item in group:
    # print the count value and item
    print(f'count: {count} : {item}')
    # increment count by 1
    count += 1

# check to see if the value of `count` at the end 
# of the loop is the same as the length of the list. 
print('-'*10)
print(f'count is now {count}')
print(f'the length of the list group is {len(group)}')

msg = '''
    Why should this be so?

    There are 4 items in the list group.
    We initially set count to be 0, then add 1 to it
    after we print each item in the for loop. So, after the 
    first item, it is 1, then 2 etc.

    At the end of all 4 items, count will then be 4, the length
    of the list we looped over
'''
print(msg)
```

    count: 0 : cat
    count: 1 : fish
    count: 2 : 🦄
    count: 3 : house
    ----------
    count is now 4
    the length of the list group is 4
    
        Why should this be so?
    
        There are 4 items in the list group.
        We initially set count to be 0, then add 1 to it
        after we print each item in the for loop. So, after the 
        first item, it is 1, then 2 etc.
    
        At the end of all 4 items, count will then be 4, the length
        of the list we looped over
    


#### Exercise 3

* use `range()` to print numbers counting down from 10 to 1 (**inclusive**)
* include comments to explain your answer


```python
# ANSWER
# use range() to print numbers counting down from 10 to 1 (inclusive)
for i in range(10,0,-1):
    print(i)
# include comments to explain your answer
msg = '''
from the instructions, it is clear that start is 10
end should be 0, since the count is only up to (but not including) 
this value.

To count down, we use a step of -1
'''
print(msg)
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
    
    from the instructions, it is clear that start is 10
    end should be 0, since the count is only up to (but not including) 
    this value.
    
    To count down, we use a step of -1
    


#### Exercise 4

* copy the code above
* as in the previous exercise, check to see if the value of `count` at the end of the loop is the same as the length of the list. 
* Explain why you get the result you do


```python
'''
# ANSWER

for loop with enumerate()
'''

# copy the code above
group = ['hat','dog','keys']


for count,item in enumerate(group):
    # print counter in loop
    print(f'item {count} is {item}')
    
# as in the previous exercise, 
# check to see if the value of `count` 
# at the end of the loop is the same as the length of the list. 
print('-'*10)
print(f'count is now {count}')
print(f'the length of the list group is {len(group)}')

msg = '''
    Explain why you get the result you do

    There are 4 items in the list group. 
    when we use enumerate to loop over the list
    count is incremented by 1 each time we enter the loop.
    In the previous example, in was incremented after
    the print statement.
    
    So now, at the end of all 4 items, count will only be 3, the length
    of the list we looped over, minus 1
'''
print(msg)
```

    item 0 is hat
    item 1 is dog
    item 2 is keys
    ----------
    count is now 2
    the length of the list group is 3
    
        Explain why you get the result you do
    
        There are 4 items in the list group. 
        when we use enumerate to loop over the list
        count is incremented by 1 each time we enter the loop.
        In the previous example, in was incremented after
        the print statement.
        
        So now, at the end of all 4 items, count will only be 3, the length
        of the list we looped over, minus 1
    


#### Exercise 5

* set up  list of numbers (years) from 2008 to 2019 **inclusive**,
* set up a list of corresponding chinese zodiac names as the items (look [online](https://www.chinahighlights.com/travelguide/chinese-zodiac/#:~:text=In%20order%2C%20the%2012%20Chinese,a%20year%20of%20the%20Rat.) for this information). 
* check that the lists have the same length
* form a dictionary from the two lists, using `dict(zip())` as in the examples above
* use `.items()` as above to loop over each year, and print the year name and the zodiac name with an f-string of the form: `f'{y} is the year of the {z}'`, assuming `y` is the key and `z` the item.
* Describe what you are doing at each step


```python
# ANSWER

# Set up list of numbers (years) from 2008 to 2019 inclusive,
years = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
# set up a list of corresponding chinese zodiac names as the items 
# (look online for this information).
zodiac = ['rat', 'ox', 'tiger', 'rabbit', \
          'dragon', 'snake', 'horse', 'goat',\
          'monkey','rooster','dog','pig']

# check that the lists have the same length
assert len(years) == len(zodiac)

# form a dictionary from the two lists, using dict(zip()) as in the examples above
# we want years as the key and zodiac as the items, so we use zip(years,zodiac)
# then convert (cast) it to a dictionary called zodiacYear
zodiacYear = dict(zip(years,zodiac))

# use .items() as above to loop over each year, and 
# print the year name and the zodiac name
# with an f-string of the form: `f'{y} is the year of the {z}'`
# assuming y is the key and z the item.

# do the loop so that y is the key and z the item
for y,z in zodiacYear.items():
    print(f'{y} is the year of the {z}')
    
# it prints the results fine
```

    2008 is the year of the rat
    2009 is the year of the ox
    2010 is the year of the tiger
    2011 is the year of the rabbit
    2012 is the year of the dragon
    2013 is the year of the snake
    2014 is the year of the horse
    2015 is the year of the goat
    2016 is the year of the monkey
    2017 is the year of the rooster
    2018 is the year of the dog
    2019 is the year of the pig


#### Exercise 6

* Use a list comprehension to generate a list of squared numbers from $0^2$ to $10^2$


```python
# ANSWER
# Use a list comprehension to generate a list of squared numbers from 0^2 to 10^2
[i*i for i in range(11)]
```




    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


