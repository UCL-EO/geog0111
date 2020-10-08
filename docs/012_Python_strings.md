# 012 String formatting

## Introduction

### Purpose

In this section we will learn some more depth about strings: features and formatting.

### Prerequisites

You will need some understanding of the following:


* [001 Using Notebooks](001_Notebook_use.md)
* [003 Getting help](003_Help.md)
* [010 Variables, comments and print()](010_Python_Introduction.md)
* [011 Data types](011_Python_data_types.md) In particular, you should be understand strings and know how to find the length of a string.



## String features

### Quotes and escapes

We have seen strings before, and noted that they are collections of characters (`a`, `b`, `1`, ...). Strings and characters are input by surrounding the relevant text in either double (`"`) or single (`'`) quotes. You can use this feature to print out a string with quotes, for example:


```python
print ("'a string in single quotes'")
print ('"a string in double quotes"')
```

    'a string in single quotes'
    "a string in double quotes"


Some elements of the string may be special codes for print formatting, such as newline `\n` or tab `\t`. If we insert these in the string, they will add a newline or a tab respectively. Both of these might *look like* multiple characters, but rather are interpreted instead as a single character.

What if we needed to print out `\n` as part of the string, e.g. print the string:

        "beware of \n and \t"
        
we will find that they are (as we probably suspected) interpreted. Using single or double quotes will make no difference:


```python
print("beware of \n and \t")
print('beware of \n and \t')
```

    beware of 
     and 	
    beware of 
     and 	


What we need to do is to present the `print()` with two characters `\` and `n`, instead of the single character `\n`. The problem now is that `\` has special meaning in a string: it *escapes* the following character, i.e. it makes the interpreter ignore the meaning of the following character. If we tried to generate a string:

        "\"
 
 the code would fail, because `\"` means *don't* interpret `"` in its usual sense (i.e. as a quote) and we would have an unclosed string.
 
 The trick then, is to use `\` to escape the meaning of `\`. So, if we want to print `\`, we set the string as `\\`:


```python
print("\\")
```

    \


#### Exercise 1

* insert a new cell below here
* Use what we have learned above to print the phrase `"beware of \n and \t"`, including quotes.

Another time we use the `\` as an escape character is in trying to make long strings in our code more readable. We can do this by putting an escape `\` **just before** we hit the return key (newline!) on the keyboard, and so spread what would be a command or variable over a single long line over multiple lines.

For example:


```python
# from https://www.usgs.gov/faqs/what-remote-sensing-and-what-it-used?
string = \
"Remote sensing is the process of detecting and \
monitoring the physical characteristics of an \
area by measuring its reflected and emitted \
radiation at a distance (typically from \
satellite or aircraft)."

print(string)
```

    Remote sensing is the process of detecting and monitoring the physical characteristics of an area by measuring its reflected and emitted radiation at a distance (typically from satellite or aircraft).


Here, when we type `string = ` on the first line, the Python interpreter expects a string to be specified next. By using instead `\` *just before we hit the return*, we are essentially escaping that newline, and the rest of the command (the string definition here) can take place on the following line. We repeat this idea to spread the string over multiple lines.

This can be really useful. 

In the special case of a string that we want to define over multiple lines though, Python has a special format using triple quotes (single or double):

    '''
    multiple 
    line
    string
    '''
    
that means we don't need to escape each end of line within the text.


```python
# from https://www.usgs.gov/faqs/what-remote-sensing-and-what-it-used?
string = '''
Remote sensing is the process of detecting and 
monitoring the physical characteristics of an 
area by measuring its reflected and emitted 
radiation at a distance (typically from 
satellite or aircraft).
'''

print(string)
```

    
    Remote sensing is the process of detecting and 
    monitoring the physical characteristics of an 
    area by measuring its reflected and emitted 
    radiation at a distance (typically from 
    satellite or aircraft).
    


Notice how this is different to the case when we escaped the newline characters withing the string. In fact, at the end of each line of text, this string contains `\n` newline characters (we just don't see them).

#### Exercise 2

* Insert a new cell below here
* Write Python code that prints a string containing the following text, spaced over four lines as intended. There should be no space at the start of the line.

        The Owl and the Pussy-cat went to sea 
        In a beautiful pea-green boat, 
        They took some honey, and plenty of money, 
        Wrapped up in a five-pound note.

* Write Python code that prints a string containing the above text, all on a single line.

## String arithmetic

We can use some of the arithmetic operators with strings. In particular `*` and `+`.

### `*`

In the context of a string, the operator `*` is used to repeat the string. For example:


```python
# multiplication example
dash = '-'
dash10 = dash * 10
print(dash,len(dash))
print(dash10,len(dash10))
```

    - 1
    ---------- 10


#### Exercise 3

* In a new cell below, generate a string called `base` and set this to the string `Hello` 
* print base and its length
* set a new variable `mult` to `base * 10`
* print `mult` and its length
* comment on why the lengths are the values reported

### `+`

The plus operator `+` adds two strings together, in the sense of [concatenating](https://en.wikipedia.org/wiki/Concatenation) the strings. For example:


```python
# hello world
astring = 'hello'
bstring = 'world'

cstring = astring + bstring
print('I joined',astring,'to',bstring,'with + and got',cstring)
```

    I joined hello to world with + and got helloworld


#### Exercise 4

You may have noticed that when we use `+` to join `hello + world` above, there is no space between the words. This is because we have not told the computer to put any such space in.

* Copy the code from the hello world example above
* create a new string called `gap` containing whitespace: `gap = ' '`
* using `gap`, edit the code so that `cstring` has a gap between the words

## String formating

### `str.format()`

We know that we can join strings together with `+` or, from a list with `str.join()`. 

Whilst we have seen that you can print a string with some variables in it, e.g.:


```python
float_val = 10.6
guess_value = 13.4
print("The number you are thinking of is",float_val,'but I guessed',guess_value)
```

    The number you are thinking of is 10.6 but I guessed 13.4


strings of that nature can soon become unwieldy. We could have converted each item to a string, and then joined the strings:


```python
float_val = 10.6
guess_value = 13.4
# using + & inserting the correct white spaces
string = "The number you are thinking of is " + \
          str(float_val) + \
         ' but I guessed ' + \
          str(guess_value)
print(string)
```

    The number you are thinking of is 10.6 but I guessed 13.4


but neither of these is very readable, or indeed very re-useable.

A neater way to form a string with variable inserts is to use the `format()` method:

    str.format(...)
     |      S.format(*args, **kwargs) -> str
     |      
     |      Return a formatted version of S, using substitutions from args and kwargs.
     |      The substitutions are identified by braces ('{' and '}').
     |  

Using this approach, we would set up a template:

    string_template = \
    "The number you are thinking of is {think} but I guessed {guess}"

with variables `float_val` and `guess_value` defined between braces `{}`.

To insert values into this template, we use the string method `format()`. If the template variables are named (as in `{think}` and `{guess}` here), then we use **keyword arguments** with `format()`. For example:


```python
string_template = \
    "The number you are thinking of is {think} but I guessed {guess}"

float_val = 10.6
guess_value = 13.4

print(string_template.format(think=float_val,\
                             guess=guess_value))
```

    The number you are thinking of is 10.6 but I guessed 13.4


This has the advantage that the template is easily re-useable, that we have been explicit about the variables we insert.

A further refinement on this is to specify some formatting statement for the variables we use. For example, we might want the value `float_val` or `guess_value` to be specified to two decimal places. To do this, we can provide a formatting statement to associate with the variable name in the template. This is done using a `:` qualifier, followed by a description of the format. For example, the format statement of two figures after the decimal point for a `float`is `:.2f`. 


```python
string_template = \
    "The number you are thinking of is {think:.2f} but I guessed {guess:.2f}"

float_val = 10.6
guess_value = 13.4

print(string_template.format(think=float_val,\
                             guess=guess_value))
```

    The number you are thinking of is 10.60 but I guessed 13.40


Other useful format statements examples include:

                              : >10.2f 
                                 ^^ ^
     10, so length 10 in total  <-| ||-> f is code for float
                                    |-> .4 so length of 4 after decimal
                                    
                              : 0>8d
             pad space with 0 <-||||-> d is code for integer
                                 ||-> 8 is length of string
                                 |-> use > for right align 
                                  
                              : _>10s
            pad space with _ <- || ||-> s is code for string
       use > for right align   <-| |-> 10 is length of string 
                                  
                              : _<10s
            pad space with _ <- || ||-> s is code for string
        use < for left align   <-| |-> 10 is length of string 
                                                                        
 The syntax might seem a little awkward at first, but its is [very powerful](https://docs.python.org/3/library/string.html#formatstrings). So long as you are aware that it exists and know of some examples, you should be able to pick it up.


```python
print("  : >.2f  -> {x: >.2f}".format(x=10.3))
print("  :0>8d    -> {x:0>8d}".format(x=10))
print("  :_>10s   -> {x:_>10s}".format(x='hello'))
print("  :_<10s   -> {x:_<10s}".format(x='hello'))
```

      : >.2f  -> 10.30
      :0>8d    -> 00000010
      :_>10s   -> _____hello
      :_<10s   -> hello_____


Suppose we want to write a set of results to a different file for each job, where the identifier of the job is an integer number between 0 and 99999999.

We want the file names associated with these results to appear in a logical order.

We could just use file names `0.dat`, `1.dat`, `2.dat`, `3.dat` ... `10.dat`, `11.dat` etc. but we would find that when we list the files, they will be in the order `0.dat`, `1.dat`, `10.dat`, `11.dat`, ...  `2.dat`, `3.dat`, because this is the natural ['lexicographic' order](https://www.tutorialspoint.com/Sort-the-words-in-lexicographical-order-in-Python#:~:text=Sorting%20words%20in%20lexicographical%20order,(not%20the%20data%20structure).) generally used by computers. We could define some awkward way of getting around this, but it would be much simpler if we simply padded the filenames with `0` characters, so that they appeared as `00000000.dat`, `00000001.dat`, `00000002.dat`, `00000003.dat` ... `00000010.dat`, `00000011.dat`. Then, lexigraphically, they will appear in the order we intended.



#### Exercise 5

* set a variable `index` to be an integer between `0` and `99999999`.
* use this to generate a zero-padded filename of the form `00000010.dat`
* print out the filename



### `f-string`

An alternative way of formatting a string that can be useful is the use of the `f-string`. In this, we place an `f` character at the start of the string. It is a sort of short-hand for what we do with the format statement, where the variables given in the braces are directly inserted.

Note that we can use the same sort of formatting statements for the f-string as when using `.format()` above.


```python
string = f'The number you are thinking of is {float_val} but I guessed {guess_value}'
print(string)
```

    The number you are thinking of is 10.6 but I guessed 13.4


#### Exercise 6

* Insert a new cell below here
* create a template string of the form:

        "what have the {people} ever done for us?"
        
* assign the word `Romans` to the variable `people` and print the formatted template: hint: use the `str.format()` method to insert this into the template.
* repeat this using an f-string directly.

Actually, there are a lot more [useful things](https://realpython.com/python-f-strings/#simple-syntax) we can do with an `f` string, but we will leave it here at this point.

## Summary

In this section, we have introduced some more detail on strings, especially string formatting. You should have agained an understanding of the use of quotes and escape code, as well as using `f-string`, `string.format()`.

| item | description |
|---|-|
| `"'"` | single quote as a string |
| `'"'` | double quote as a string |
| `"\\"` | backslash as a string (escaped) in string|
| ''' ... ''' | multiple line string |
| `*` | string multiplication e.g. `"0"*2` -> `"00"` |
| `+` | string addition e.g. `"0" + "1"` -> `"01"`|
| `str.format()` | insert items in string e.g. `"{x}".format(x=1)` -> "1"|
| `f"..."`| f-string, e.g. `x=1`, `f"{x}"` -> `"1"|
