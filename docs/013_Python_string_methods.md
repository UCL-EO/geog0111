# 013 String methods

## Introduction

### Purpose

In this section we will learn some about strings, in particular, string methods.


### Prerequisites

You will need some understanding of the following:


* [001 Using Notebooks](001_Notebook_use.md)
* [003 Getting help](003_Help.md)
* [010 Variables, comments and print()](010_Python_Introduction.md)
* [011 Data types](011_Python_data_types.md) In particular, you should be understand strings.
* [012 String formatting](012_Python_strings.md)



## Strings

###  `help(str)`

We can get a list of the string methods and associated information on how to use them from `help(str)`. We will go through some of these in this notebook, but you should be aware of the wider set of methods available. You don't need to go through all of these now, but notice how to get this information.


```python
help(str)
```

    Help on class str in module builtins:
    
    class str(object)
     |  str(object='') -> str
     |  str(bytes_or_buffer[, encoding[, errors]]) -> str
     |  
     |  Create a new string object from the given object. If encoding or
     |  errors is specified, then the object must expose a data buffer
     |  that will be decoded using the given encoding and error handler.
     |  Otherwise, returns the result of object.__str__() (if defined)
     |  or repr(object).
     |  encoding defaults to sys.getdefaultencoding().
     |  errors defaults to 'strict'.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(self, format_spec, /)
     |      Return a formatted version of the string as described by format_spec.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
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
     |  __mod__(self, value, /)
     |      Return self%value.
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
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __sizeof__(self, /)
     |      Return the size of the string in memory, in bytes.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  capitalize(self, /)
     |      Return a capitalized version of the string.
     |      
     |      More specifically, make the first character have upper case and the rest lower
     |      case.
     |  
     |  casefold(self, /)
     |      Return a version of the string suitable for caseless comparisons.
     |  
     |  center(self, width, fillchar=' ', /)
     |      Return a centered string of length width.
     |      
     |      Padding is done using the specified fill character (default is a space).
     |  
     |  count(...)
     |      S.count(sub[, start[, end]]) -> int
     |      
     |      Return the number of non-overlapping occurrences of substring sub in
     |      string S[start:end].  Optional arguments start and end are
     |      interpreted as in slice notation.
     |  
     |  encode(self, /, encoding='utf-8', errors='strict')
     |      Encode the string using the codec registered for encoding.
     |      
     |      encoding
     |        The encoding in which to encode the string.
     |      errors
     |        The error handling scheme to use for encoding errors.
     |        The default is 'strict' meaning that encoding errors raise a
     |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
     |        'xmlcharrefreplace' as well as any other name registered with
     |        codecs.register_error that can handle UnicodeEncodeErrors.
     |  
     |  endswith(...)
     |      S.endswith(suffix[, start[, end]]) -> bool
     |      
     |      Return True if S ends with the specified suffix, False otherwise.
     |      With optional start, test S beginning at that position.
     |      With optional end, stop comparing S at that position.
     |      suffix can also be a tuple of strings to try.
     |  
     |  expandtabs(self, /, tabsize=8)
     |      Return a copy where all tab characters are expanded using spaces.
     |      
     |      If tabsize is not given, a tab size of 8 characters is assumed.
     |  
     |  find(...)
     |      S.find(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  format(...)
     |      S.format(*args, **kwargs) -> str
     |      
     |      Return a formatted version of S, using substitutions from args and kwargs.
     |      The substitutions are identified by braces ('{' and '}').
     |  
     |  format_map(...)
     |      S.format_map(mapping) -> str
     |      
     |      Return a formatted version of S, using substitutions from mapping.
     |      The substitutions are identified by braces ('{' and '}').
     |  
     |  index(...)
     |      S.index(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in S where substring sub is found, 
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raises ValueError when the substring is not found.
     |  
     |  isalnum(self, /)
     |      Return True if the string is an alpha-numeric string, False otherwise.
     |      
     |      A string is alpha-numeric if all characters in the string are alpha-numeric and
     |      there is at least one character in the string.
     |  
     |  isalpha(self, /)
     |      Return True if the string is an alphabetic string, False otherwise.
     |      
     |      A string is alphabetic if all characters in the string are alphabetic and there
     |      is at least one character in the string.
     |  
     |  isascii(self, /)
     |      Return True if all characters in the string are ASCII, False otherwise.
     |      
     |      ASCII characters have code points in the range U+0000-U+007F.
     |      Empty string is ASCII too.
     |  
     |  isdecimal(self, /)
     |      Return True if the string is a decimal string, False otherwise.
     |      
     |      A string is a decimal string if all characters in the string are decimal and
     |      there is at least one character in the string.
     |  
     |  isdigit(self, /)
     |      Return True if the string is a digit string, False otherwise.
     |      
     |      A string is a digit string if all characters in the string are digits and there
     |      is at least one character in the string.
     |  
     |  isidentifier(self, /)
     |      Return True if the string is a valid Python identifier, False otherwise.
     |      
     |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
     |      "class".
     |  
     |  islower(self, /)
     |      Return True if the string is a lowercase string, False otherwise.
     |      
     |      A string is lowercase if all cased characters in the string are lowercase and
     |      there is at least one cased character in the string.
     |  
     |  isnumeric(self, /)
     |      Return True if the string is a numeric string, False otherwise.
     |      
     |      A string is numeric if all characters in the string are numeric and there is at
     |      least one character in the string.
     |  
     |  isprintable(self, /)
     |      Return True if the string is printable, False otherwise.
     |      
     |      A string is printable if all of its characters are considered printable in
     |      repr() or if it is empty.
     |  
     |  isspace(self, /)
     |      Return True if the string is a whitespace string, False otherwise.
     |      
     |      A string is whitespace if all characters in the string are whitespace and there
     |      is at least one character in the string.
     |  
     |  istitle(self, /)
     |      Return True if the string is a title-cased string, False otherwise.
     |      
     |      In a title-cased string, upper- and title-case characters may only
     |      follow uncased characters and lowercase characters only cased ones.
     |  
     |  isupper(self, /)
     |      Return True if the string is an uppercase string, False otherwise.
     |      
     |      A string is uppercase if all cased characters in the string are uppercase and
     |      there is at least one cased character in the string.
     |  
     |  join(self, iterable, /)
     |      Concatenate any number of strings.
     |      
     |      The string whose method is called is inserted in between each given string.
     |      The result is returned as a new string.
     |      
     |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
     |  
     |  ljust(self, width, fillchar=' ', /)
     |      Return a left-justified string of length width.
     |      
     |      Padding is done using the specified fill character (default is a space).
     |  
     |  lower(self, /)
     |      Return a copy of the string converted to lowercase.
     |  
     |  lstrip(self, chars=None, /)
     |      Return a copy of the string with leading whitespace removed.
     |      
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  partition(self, sep, /)
     |      Partition the string into three parts using the given separator.
     |      
     |      This will search for the separator in the string.  If the separator is found,
     |      returns a 3-tuple containing the part before the separator, the separator
     |      itself, and the part after it.
     |      
     |      If the separator is not found, returns a 3-tuple containing the original string
     |      and two empty strings.
     |  
     |  replace(self, old, new, count=-1, /)
     |      Return a copy with all occurrences of substring old replaced by new.
     |      
     |        count
     |          Maximum number of occurrences to replace.
     |          -1 (the default value) means replace all occurrences.
     |      
     |      If the optional argument count is given, only the first count occurrences are
     |      replaced.
     |  
     |  rfind(...)
     |      S.rfind(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  rindex(...)
     |      S.rindex(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raises ValueError when the substring is not found.
     |  
     |  rjust(self, width, fillchar=' ', /)
     |      Return a right-justified string of length width.
     |      
     |      Padding is done using the specified fill character (default is a space).
     |  
     |  rpartition(self, sep, /)
     |      Partition the string into three parts using the given separator.
     |      
     |      This will search for the separator in the string, starting at the end. If
     |      the separator is found, returns a 3-tuple containing the part before the
     |      separator, the separator itself, and the part after it.
     |      
     |      If the separator is not found, returns a 3-tuple containing two empty strings
     |      and the original string.
     |  
     |  rsplit(self, /, sep=None, maxsplit=-1)
     |      Return a list of the words in the string, using sep as the delimiter string.
     |      
     |        sep
     |          The delimiter according which to split the string.
     |          None (the default value) means split according to any whitespace,
     |          and discard empty strings from the result.
     |        maxsplit
     |          Maximum number of splits to do.
     |          -1 (the default value) means no limit.
     |      
     |      Splits are done starting at the end of the string and working to the front.
     |  
     |  rstrip(self, chars=None, /)
     |      Return a copy of the string with trailing whitespace removed.
     |      
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  split(self, /, sep=None, maxsplit=-1)
     |      Return a list of the words in the string, using sep as the delimiter string.
     |      
     |      sep
     |        The delimiter according which to split the string.
     |        None (the default value) means split according to any whitespace,
     |        and discard empty strings from the result.
     |      maxsplit
     |        Maximum number of splits to do.
     |        -1 (the default value) means no limit.
     |  
     |  splitlines(self, /, keepends=False)
     |      Return a list of the lines in the string, breaking at line boundaries.
     |      
     |      Line breaks are not included in the resulting list unless keepends is given and
     |      true.
     |  
     |  startswith(...)
     |      S.startswith(prefix[, start[, end]]) -> bool
     |      
     |      Return True if S starts with the specified prefix, False otherwise.
     |      With optional start, test S beginning at that position.
     |      With optional end, stop comparing S at that position.
     |      prefix can also be a tuple of strings to try.
     |  
     |  strip(self, chars=None, /)
     |      Return a copy of the string with leading and trailing whitespace removed.
     |      
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  swapcase(self, /)
     |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
     |  
     |  title(self, /)
     |      Return a version of the string where each word is titlecased.
     |      
     |      More specifically, words start with uppercased characters and all remaining
     |      cased characters have lower case.
     |  
     |  translate(self, table, /)
     |      Replace each character in the string using the given translation table.
     |      
     |        table
     |          Translation table, which must be a mapping of Unicode ordinals to
     |          Unicode ordinals, strings, or None.
     |      
     |      The table must implement lookup/indexing via __getitem__, for instance a
     |      dictionary or list.  If this operation raises LookupError, the character is
     |      left untouched.  Characters mapped to None are deleted.
     |  
     |  upper(self, /)
     |      Return a copy of the string converted to uppercase.
     |  
     |  zfill(self, width, /)
     |      Pad a numeric string with zeros on the left, to fill a field of the given width.
     |      
     |      The string is never truncated.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  maketrans(x, y=None, z=None, /)
     |      Return a translation table usable for str.translate().
     |      
     |      If there is only one argument, it must be a dictionary mapping Unicode
     |      ordinals (integers) or characters to Unicode ordinals, strings or None.
     |      Character keys will be then converted to ordinals.
     |      If there are two arguments, they must be strings of equal length, and
     |      in the resulting dictionary, each character in x will be mapped to the
     |      character at the same position in y. If there is a third argument, it
     |      must be a string, whose characters will be mapped to None in the result.
    


## Object methods

### Concatenate strings: `+` and `len()`

We can do a number of things with strings which are very useful. These methods are defined on generic objects by Python, but we can use them with strings as an example.

For one, we can concatenate strings using the `+` symbol:


```python
string1 = 'hello'
string2 = 'world'
spacer = ' '

# concatenate these
result = string1 + spacer + string2
print(result)
```

    hello world


Another method we will find useful with strings is the `len()` function.


```python
help(len)
```

    Help on built-in function len in module builtins:
    
    len(obj, /)
        Return the number of items in a container.
    


When the object is a string, the 'number of items' refers to the number of characters, so `len(str)` returns the length of the string.


```python
# generate a string called t
# and see how long it is
# use f-strings for covenience
t = 'hello'
print (f'the length of {t} is {len(t)}')

# generate a string called s
# and see how long it is
s = "Hello" + "there" + "everyone"
print (f'the length of {s} is {len(s)}')
```

    the length of hello is 5
    the length of Hellothereeveryone is 18


#### Exercise 1

* insert a new cell below here
* what might a zero-length string look like? Try to generate one, and check its length.
* the `Hello there everyone` example above has no spaces between the words. Copy the code and modify it to have spaces.
* confirm that you get the expected increase in length.

## String methods

### `replace()` and `strip()`


```python
help(str.replace)
```

    Help on method_descriptor:
    
    replace(self, old, new, count=-1, /)
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
    


The string method `replace()` replaces substrings defined in `old` with those defined in `new`. 

In the example below, we replace the sub-string `"happy"` with a new string containing the emoji "😃": 


```python
original_string = "I'm a very happy string"
print('original:\t',original_string)

new_string = original_string.replace("happy", "😀")
print ('new:\t\t',new_string)
```

    original:	 I'm a very happy string
    new:		 I'm a very 😀 string



```python
help(str.strip)
```

    Help on method_descriptor:
    
    strip(self, chars=None, /)
        Return a copy of the string with leading and trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
    


`strip()` is very useful in string formatting and general tidying up.

Suppose we had the string:

    ":::😀:😀:😀::::::"
    
but what we wanted was:

    "😀:😀:😀"
    
i.e. we want to strip the `:` characters from the right and left ends of the string. We can't easily use `replace()` without affecting the `:` characters we want to keep. We can achieve this with the `strip()` method though.


```python
old_string = ":::😀:😀:😀::::::"
print(old_string)

new_string = old_string.strip(':')
print(new_string)
```

    :::😀:😀:😀::::::
    😀:😀:😀


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
    

### `split()` and `join()`


```python
help(str.split)
```

    Help on method_descriptor:
    
    split(self, /, sep=None, maxsplit=-1)
        Return a list of the words in the string, using sep as the delimiter string.
        
        sep
          The delimiter according which to split the string.
          None (the default value) means split according to any whitespace,
          and discard empty strings from the result.
        maxsplit
          Maximum number of splits to do.
          -1 (the default value) means no limit.
    


`split()` and `join()` are a pair of really useful string methods. The former is used to split a string into a list of sub-strings. For example:


```python
string = \
"   Remote sensing is the process of detecting and \
monitoring the physical characteristics of an \
area by measuring its reflected and emitted \
radiation at a distance (typically from \
satellite or aircraft).   "

string_list = string.split()

print(string_list)
```

    ['Remote', 'sensing', 'is', 'the', 'process', 'of', 'detecting', 'and', 'monitoring', 'the', 'physical', 'characteristics', 'of', 'an', 'area', 'by', 'measuring', 'its', 'reflected', 'and', 'emitted', 'radiation', 'at', 'a', 'distance', '(typically', 'from', 'satellite', 'or', 'aircraft).']


We see that the string is 'parsed' into a list of separate sub-strings, which in this case represent words in the sentence. The default delimiter used to split the string is `' '`, whitespace (space or tab), though we could specify others if we needed.

Any whitespece to the left or right of the string has no impact here, so we do not need to explicitly `strip()` the string.

If we want to generate a string from a set of sub-strings, we use the `join()` method.


```python
help(str.join)
```

    Help on method_descriptor:
    
    join(self, iterable, /)
        Concatenate any number of strings.
        
        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.
        
        Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
    


 For this, we declare the string delimiter we wish to use. For example, to reconstruct the sentence from the string list with whitespace delimitation:


```python
string_list = ['Remote', 'sensing', 'is', 'the', 'process', 
               'of', 'detecting', 'and', 'monitoring', 'the', 
               'physical', 'characteristics', 'of', 'an', 'area', 
               'by', 'measuring', 'its', 'reflected', 'and', 'emitted', 
               'radiation', 'at', 'a', 'distance', '(typically', 'from',
               'satellite', 'or', 'aircraft).']

string = ' '.join(string_list)
print(string)
```

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

### `slice` 

A string can be thought of as an ordered 'array' of characters. 

So, for example the string `hello` can be thought of as a construct containing `h` then `e`, `l`, `l`, and `o`. 

We can index a string, so that e.g. `'hello'[0]` is `h`, `'hello'[1]` is `e` etc. Notice that index `0` is used for the first item.

We have seen above the idea of the 'length' of a string. In this example, the length of the string `hello` is 5. The final item in this case would be `'hello'[4]`, because we count indices from 0.


```python
string = 'hello'

# length
slen = len(string)
print('length of',string,'is',slen)

# select these indices
i = 0
print('character',i,'of',string,'is',string[i])

i = 3
print('character',i,'of',string,'is',string[i])

i = 4
print('character',i,'of',string,'is',string[i])

```

    length of hello is 5
    character 0 of hello is h
    character 3 of hello is l
    character 4 of hello is o


#### Exercise 4

* Insert a new cell below here
* copy the code above, and see what happens if you set `i` to be the value of length of the string. 
* why does it respond in this way?



We can use the idea of a 'slice' to access particular elements within the string.

For a slice, we can specify:

* start index (0 is the first)
* stop index (not including this)
* skip (do every 'skip' character)

When specifying this as array access, this is given as, e.g.:

`array[start:stop:skip]`

* The default start is 0
* The default stop is the length of the array
* The default skip is 1

We can use negative numbers in specifying `start:stop:skip`: in that case, they are counted from the end of the string (`-1` is the last character).

We can specify a slice with the default values by leaving the terms out:

`array[::2]`

would give values in the array `array` from 0 to the end, in steps of 2.

We can do the same by using `None` to indicate the default:

`array[None:None:2]`


This idea is fundamental to array processing in Python. We will see later that the same mechanism applies to all ordered groups.



```python
s = "Hello World"
print (s,len(s))

start = None
stop  = 11
skip  = 2
print (s[start:stop:skip])

# use -ve numbers to specify from the end
# use None to take the default value
start = -3
stop  = None
skip  = 1
print (s[start:stop:skip])
```

    Hello World 11
    HloWrd
    rld


#### Exercise 5

The example above allows us to access an individual character(s) of the array.

* Insert a new cell below here
* based on the example above, print the string starting from the default start value, up to the default stop value, in steps of `2`. This should be `HloWrd`.
* write code to print out the 4$^{th}$ letter (character) of the string `s`. This should be `l`.


## Summary

In this section, we have introduced some more detail on string, especially string methods. There are many more methods you can use, but we have tried to cover the main ones here, but there are many [resources](https://www.w3schools.com/python/python_strings.asp#:~:text=Strings%20are%20Arrays,access%20elements%20of%20the%20string.) you can use to follow up.

You should know how to make a single line or multi-line string. You  should know how to use `replace`, `strip`, `split` and `join` on a string, as well as use concepts of indexing a string array and using ideas of `slice`. You should recognise the `None` character. You shouyld know how to find information on how to use other string methods.

| item | description |
|---| -|
| `str.replace(a,b)` | replace occurrences of `a` with `b` in `str` |
| `str.strip(a)` | strip off any occurrences of `a` on left or right ends of `str` (also `lstrip`,`rstrip`)|
| `str.split(a)` | split `str` into list, using `a` as the separator, e.g. `"1:2".split(":")` -> `["1","2"]`
| `a.join(l)` | join the string items in list `l` into a string with `a` as the separator, e.g. `"x".join(["1","2"])` -> `"1x2"` |
| `str[start:stop:step]` | slice `str` and return characters `start` to (but not including) `stop` skipping `step` values, e.g. `"hello"[1:2]` -> `e`|
