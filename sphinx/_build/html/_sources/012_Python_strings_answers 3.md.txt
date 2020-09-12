# 012 String formatting : Answers to exercises

#### Exercise 1

* insert a new cell below here
* Use what we have learned above to print the phrase `"beware of \n and \t"`, including quotes.


```python
# ANSWER
# Use what we have learned above to print the phrase
# "beware of \n and \t", including quotes.

# try this first
string = "beware of \n and \t"
print('wrong:\t\t',string)

# now escape the \ characters
string = "beware of \\n and \\t"
print('good:\t\t',string,'\t\tbut no quotes')

# now escape the \ characters
# and add quotes
string = '"beware of \\n and \\t"'
print('great:\t\t',string)

# now escape the \ characters
# and add quotes by escaping
string = "\"beware of \\n and \\t\""
print('great:\t\t',string)
```

    wrong:		 beware of 
     and 	
    good:		 beware of \n and \t 		but no quotes
    great:		 "beware of \n and \t"
    great:		 "beware of \n and \t"


#### Exercise 2

* Insert a new cell below here
* Write Python code that prints a string containing the following text, spaced over four lines as intended. There should be no space at the start of the line.

        The Owl and the Pussy-cat went to sea 
        In a beautiful pea-green boat, 
        They took some honey, and plenty of money, 
        Wrapped up in a five-pound note.

* Write Python code that prints a string containing the above text, all on a single line.


```python
# ANSWER

# Write Python code that prints a string containing 
# the following text, spaced over four lines as intended.

lear = '''
The Owl and the Pussy-cat went to sea
In a beautiful pea-green boat,
They took some honey, and plenty of money,
Wrapped up in a five-pound note.
  '''
print(lear)
```

    
    The Owl and the Pussy-cat went to sea
    In a beautiful pea-green boat,
    They took some honey, and plenty of money,
    Wrapped up in a five-pound note.
      



```python
# ANSWER

# Write Python code that prints a string 
# containing the above text, all on a single line.


# we can still space it out clearly, but 
# now escape the new lines
lear = \
"The Owl and the Pussy-cat went to sea \
In a beautiful pea-green boat, \
They took some honey, and plenty of money, \
Wrapped up in a five-pound note."
print(lear)
```

    The Owl and the Pussy-cat went to sea In a beautiful pea-green boat, They took some honey, and plenty of money, Wrapped up in a five-pound note.


#### Exercise 3

* In a new cell below, generate a string called `base` and set this to the string `Hello` 
* print base and its length
* set a new variable `mult` to `base * 10`
* print `mult` and its length
* comment on why the lengths are the values reported


```python
# ANSWER
# In a new cell below, generate a string called base and set this to the string Hello
base = 'Hello'

#print base and its length
print(base,len(base))

#set a new variable mult to base * 10
mult = base * 10

#print mult and its length
print (mult,len(mult))

#comment on why the lengths are the values reported
msg = '''
The string 'Hello' has 5 characters. We set the evariable base
to be this, so the length of the string base is 5.

We set mult to be base * 10. For a string, * repeats the string,
so we end up with a string the same as base but repeated 10 times.
Since th length of base was 5, the length of mult will be 5 * 10 = 50
'''
print(msg)
```

    Hello 5
    HelloHelloHelloHelloHelloHelloHelloHelloHelloHello 50
    
    The string 'Hello' has 5 characters. We set the evariable base
    to be this, so the length of the string base is 5.
    
    We set mult to be base * 10. For a string, * repeats the string,
    so we end up with a string the same as base but repeated 10 times.
    Since th length of base was 5, the length of mult will be 5 * 10 = 50
    


#### Exercise 4

You may have noticed that when we use `+` to join `hello + world` above, there is no space between the words. This is because we have not told the computer to put any such space in.

* Copy the code from the hello world example above
* create a new string called `gap` containing whitespace: `gap = ' '`
* using `gap`, edit the code so that `cstring` has a gap between the words


```python
# ANSWER

# Copy the code from the hello world example above
astring = 'hello'
bstring = 'world'

# create a new string called `gap` containing whitespace: `gap = ' '`
gap = ' '

# using `gap`, edit the code so that `cstring` has a gap between the words
cstring = astring + gap + bstring
print('I joined',astring,'to',gap,'to',bstring,'with + and got',cstring)
```

    I joined hello to   to world with + and got hello world



```python
# ANSWER

# in a new cell below, generate a string called base and set this to the string Hello
base = 'Hello'

# print base and its length
print(base,len(base))

# set a new variable mult to base * 10
mult = base * 10

# print mult and its length
print(mult,len(mult))

# comment on why the lengths are the values reported
msg = '''
    comment on why the lengths are the values reported
 
    The string called base had length 5
    The new string called mult was a repeat of the string
    base, 10 times, using the multiplication operator *

    As we would expect, the new string had length 10 * 5 = 50
'''
print(msg)
```

    Hello 5
    HelloHelloHelloHelloHelloHelloHelloHelloHelloHello 50
    
        comment on why the lengths are the values reported
     
        The string called base had length 5
        The new string called mult was a repeat of the string
        base, 10 times, using the multiplication operator *
    
        As we would expect, the new string had length 10 * 5 = 50
    


#### Exercise 5

* set a variable `index` to be an integer between `0` and `99999999`.
* use this to generate a zero-padded filename of the form `00000010.dat`
* print out the filename




```python
# ANSWER

# set a variable index to be an integer between 0 and 99999999.
index = 1265

# use this to generate a zero-padded filename of the form 00000010.dat
# Note that we use 8d here as we want at the string part with
# the number to be of length 8
filename = "{:0>8d}.dat".format(index)

# print out the filename
print(filename)
```

    00001265.dat


#### Exercise 6

* Insert a new cell below here
* create a template string of the form:

        "what have the {people} ever done for us?"
        
* assign the word `Romans` to the variable `people` and print the formatted template: hint: use the `str.format()` method to insert this into the template.
* repeat this using an f-string directly.


```python
# ANSWER
# Insert a new cell below here
# create a template string of the form:

template="what have the {people} ever done for us?"
        
# assign the word Romans to the variable people and print 
# the formatted template: hint: use the str.format() 
# method to insert this into the template.

print(template.format(people='Romans'))

# repeat this using an f-string directly.
people='Romans'
print(f"what have the {people} ever done for us?")
```

    what have the Romans ever done for us?
    what have the Romans ever done for us?

