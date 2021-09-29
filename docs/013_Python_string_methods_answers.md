# 013 String methods : Answers to exercises

#### Exercise 1

* insert a new cell below here
* what might a zero-length string look like? Try to generate one, and check its length.
* the `Hello there everyone` example above has no spaces between the words. Copy the code and modify it to have spaces.
* confirm that you get the expected increase in length.


```python
# ANSWER

# insert a new cell below here
# what might a zero-length string look like? Try to generate one, and check its length.

t = ''
print (f'the length of {t} is {len(t)}')

# the `Hello there everyone` example above has no spaces between the words. Copy the code and modify it to have spaces.

space = ' '
s = "Hello" + space + "there" + space + "everyone"
print (f'the length of {s} is {len(s)}')

# confirm that you get the expected increase in length.
msg = '''
The old string had length 18
now, with two spaces, this has length 20 as expected
'''
print(msg)
```

    the length of  is 0
    the length of Hello there everyone is 20
    
    The old string had length 18
    now, with two spaces, this has length 20 as expected
    


#### Exercise 2

* Insert a new cell below here
* Take the multi-line string:

`'''
----Remote sensing is the process of detecting and 
monitoring the physical characteristics of an 
area by measuring its reflected and emitted 
radiation at a distance (typically from 
satellite or aircraft).----
'''`

  and use it to generate a single line string, without the `-` characters at either end.
    


```python
# ANSWER

old_string = '''
----Remote sensing is the process of detecting and 
monitoring the physical characteristics of an 
area by measuring its reflected and emitted 
radiation at a distance (typically from 
satellite or aircraft).----
'''
print(old_string)

# replace newline with empty string!
# and strip the result after
new_string = old_string.replace('\n','').strip('-')
print(new_string)
```

    
    ----Remote sensing is the process of detecting and 
    monitoring the physical characteristics of an 
    area by measuring its reflected and emitted 
    radiation at a distance (typically from 
    satellite or aircraft).----
    
    Remote sensing is the process of detecting and monitoring the physical characteristics of an area by measuring its reflected and emitted radiation at a distance (typically from satellite or aircraft).


#### Exercise 3
 
* Insert a new cell below here
* Take the string 

      The Owl and the Pussy-cat went to sea 
      In a beautiful pea-green boat, 
      They took some honey, and plenty of money, 
      Wrapped up in a five-pound note.
    
  and split it into a list of sub-strings.
* Then re-construct the string, separating each word by a colon character `':'`
* Print out the list of sub-strings and the re-constructed string


```python
# Answer

# Take the string
string = '''
The Owl and the Pussy-cat went to sea 
In a beautiful pea-green boat, 
They took some honey, and plenty of money, 
Wrapped up in a five-pound note.
'''

# and split it into a list of sub-strings.
list_string = string.split()
# print this out
print(list_string)

# Then re-construct the string, separating each word by a colon character ':'
recon_string = ':'.join(list_string)
# print this out
print(recon_string)
```

    ['The', 'Owl', 'and', 'the', 'Pussy-cat', 'went', 'to', 'sea', 'In', 'a', 'beautiful', 'pea-green', 'boat,', 'They', 'took', 'some', 'honey,', 'and', 'plenty', 'of', 'money,', 'Wrapped', 'up', 'in', 'a', 'five-pound', 'note.']
    The:Owl:and:the:Pussy-cat:went:to:sea:In:a:beautiful:pea-green:boat,:They:took:some:honey,:and:plenty:of:money,:Wrapped:up:in:a:five-pound:note.



```python
# Answer
# the Hello there everyone example above has no spaces between the words. 
# copy the code and modify it to have spaces.

# generate a string called s
# and see how long it is

# lets have a spacer variable
spacer = ' '
quote = '"'
# add the spaces in
s = "Hello" + spacer + "there" + spacer + "everyone"
print ('the length of',quote+s+quote,'is',len(s))

# confirm that you get the expected increase in length.
# It is now 20 rather than 18 above
```

    the length of "Hello there everyone" is 20


#### Exercise 4

* Insert a new cell below here
* copy the code above, and see what happens if you set `i` to be the value of length of the string. 
* why does it respond in this way?


```python
# ANSWER

# copy the code
string = 'hello'

# length
slen = len(string)
print('length of', string, 'is', slen)

# copy the code above, and see what happens if you set `i` to be the value of length of the string. 
i = slen
print('character', i, 'of', string, 'is', string[i])
```

    length of hello is 5



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-18-c41bb38893d7> in <module>
         10 # copy the code above, and see what happens if you set `i` to be the value of length of the string.
         11 i = slen
    ---> 12 print('character', i, 'of', string, 'is', string[i])
    

    IndexError: string index out of range



```python
# ANSWER

# Why does it respond in this way?
msg = '''
 This fails with:
 
     IndexError: string index out of range

 because string[5] does not exist
 as the length of string is 5: we can
 only idex from 0 to 4
'''
print(msg)

```

    
     This fails with:
     
         IndexError: string index out of range
    
     because string[5] does not exist
     as the length of string is 5: we can
     only idex from 0 to 4
    


#### Exercise 5

The example above allows us to access an individual character(s) of the array.

* Insert a new cell below here
* based on the example above, print the string starting from the default start value, up to the default stop value, in steps of `2`. This should be `HloWrd`.
* write code to print out the 4$^{th}$ letter (character) of the string `s`. This should be `l`.



```python
# ANSWER

s = "Hello World"
print (s,len(s))

# based on the example above, print the string starting 
# from the default start value, up to the default stop value, in steps of `2`.

# default start -> None
start = None
# default stop -> None
stop  = None
skip  = 2
print (s[start:stop:skip])
```


```python
# ANSWER

s = "Hello World"
# write code to print out the 4 𝑡ℎ  letter (character) of the string s.
# index 3 is the 4th character !!!
print(s[3])
```
