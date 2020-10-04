# 010 Introduction to Python

## Introduction

[Python](http://www.python.org/) is a high level programming language that is freely available, relatively easy to learn and portable across different computing systems. In Python, you can rapidly develop solutions for the sorts of problems you might need to solve in your MSc courses and in the world beyond. Code written in Python is also easy to maintain, is (or should be) self-documented, and can easily be linked to code written in other languages.

Relevant features include: 

- it is automatically compiled and executed 
- code is portable provided you have the appropriate Python modules. 
- for compute intensive tasks, you can easily make calls to methods written in (faster) lower-level languages such as C or FORTRAN 
- there is an active user and development community, which means that new capabilities appear over time and there are many existing extensions and enhancements easily available to you.

For further background on Python, look over the material on [Advanced Scientific Programming in Python](https://python.g-node.org/wiki/schedule) and/or the [software-carpentry.org](http://software-carpentry.org/v3/py01.html) and [python.org](http://www.python.org/) web sites.


### Purpose

In this section we will learn some of the fundamental concepts in Python concerning variables, as well as writing comments and the use of the function `print()` and newline and tab characters.

### Prerequisites

You will need some understanding of the following:

* [001 Using Notebooks](001_Notebook_use.md)
* [003 Getting help](003_Help.md)

Remember that you can 'run' the code in a code block using the 'run' widget (above) or hitting the keys ('typing') <shift> and <return> at the same time. 


## Some basics

### Comments 

Comments are statements ignored by the language interpreter.

Any text after a `#` in a *code block* is a comment.

#### Exercise 1

* Try running the code block below
* Explain what happened ('what the computer did')

### `print()`



```python
help(print)
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    


To print some value (by default, to the terminal you are using, knows as the standard output `stdout`), use the `print(...)` function.




```python
# For example, to print the string 'hello world':
print('hello world')

# to print the list ('hello','world'):
print('hello', 'world')
```

    hello world
    hello world


#### Exercise 2

* Insert a new cell below here
* Print out the string `Today I am learning Python`.

### newline and tab

We can gain more control over our printing by understanding some special characters we use in print formatting:

    newline \n
    tab     \t
    
When we specify these characters in a print statement, they have the impact of starting text on the following time, and aligning text the next tab location respectively. These are concepts you will be familiar with from word processing, although you may not have thought about them explicitly.

Any time we place these characters in a string that we print out, they will affect the formatting out our printed statement:


```python
# For example, to print the string 'hello world'
# with a simple space
print('hello world')

# with a newline in the middle
print('hello\nworld')

# with a tab in the middle
print('hello\tworld')
```

    hello world
    hello
    world
    hello	world


#### Exercise 3

* Insert a new cell below here
* print a string `"all the world's a stage and all the men and women merely players"`
* print this same string, but with each word on a new line
* print this same string with two columns of words, for as many lines as needed

## Variables and Values 

### Variables and values

The idea of **variables** is fundamental to any programming. 

You can think of this as the *name* of *something*, so it is a way of allowing us to refer to some object in the language. A related idea we will find useful is to think of the variable name as a **key**. What the variable *is* set to is called its **value**. 

Putting these ideas together, we can think of the variable name and its value as a `key: value` pair:

    key: value

We can say that the `value` is **assigned to** the `key`.

**Remember: the `key` is the name of the variable, the `value` is what is stored in the variable.**

So let's start with a variable we will call (*declare to be*) `my_store`.

We will give a *value* of the string `'one'` to this variable:


```python
# assign the value 'one' to the variable (key) my_store
my_store = 'one'

# Print the value of my_store
print(my_store)
```

    one


#### Exercise 4

* Insert a new cell below here
* set a variable called `message` to contain the string `hello world`
* print the value of the variable `message`

### Symbol names and conventions

Symbol names, such as those used for variables, in Python can contain the usual character set `a-z`, `A-Z`, `0-9`, as well as `_`. 

Symbol names cannot start with a number. 

Normal variables start with a letter. Those starting and ending with double underscore `_` have [special meaning](https://docs.python.org/3.8/reference/lexical_analysis.html#reserved-classes-of-identifiers) and should only be used in those special contexts (e.g. `__doc__`, or `__main__`).

The convention is that variables start with a lower case character and [classes](https://docs.python.org/3/tutorial/classes.html) start with capitals. e.g.:

            my_var = 10

            class ClassName:
                <statement-1>
                .
                .
                .
                <statement-N>

### Invalid names

The following are *not* valid in names and will result in an error:

   * characters liable to intepretation (`SyntaxError: invalid syntax`), including (comma! `,`) and:
   
           +, -, *, **, =, $, !  etc.
   
   * extended characters (`SyntaxError: invalid character in identifier`) such as emojis
   
           😀, 我在这里 etc.
 
[Reserved keywords](https://docs.python.org/3.8/reference/lexical_analysis.html#keywords) cannot be used as variable names:

            False      class      finally    is         return
            None       continue   for        lambda     try
            True       def        from       nonlocal   while
            and        del        global     not        with
            as         elif       if         or         yield
            assert     else       import     pass
            break      except     in         raise
            
as these have particular meanings in Python syntax.

All of these can obviously be used as `values` in strings, just not as `key` names.

See [https://docs.python.org/3.4/reference/lexical_analysis.html](https://docs.python.org/3.4/reference/lexical_analysis.html) for further details.

#### Exercise 5

* Make a code cell below
* declare the variable `dash='\n----------'` and print it
* declare your own variables to contain the following values, trying to use a range of allowed names

            1, 2, 'one', 'hello world', '1\n2\n3\t 4 5 6\n😀, 我在这里'
            
* print the variables to see if they contain what you expect, followed in each instance by `dash` (to space the answers out)

## Summary

In this section, you have had an introduction to the Python programming language, running in a [`jupyter notebook`](http://jupyter.org) environment.

You have seen how to write comments in code, how to form `print` statements, `\n` and `\t` and basic concepts of variables and values.

* Rules and conventions for symbol names.

|  command | purpose  |   
|-|---|
| `#` | hash symbol, followed by comments|
| `print()` | print function|
| `\n` | newline character|
| `\t` | tab character|
| `varname = value` | set variable `varname` to `value`|
|`__doc__, __main__` | special method names |

* variables start with a lower case character and classes start with capitals
* Reserved keywords:

            False      class      finally    is         return
            None       continue   for        lambda     try
            True       def        from       nonlocal   while
            and        del        global     not        with
            as         elif       if         or         yield
            assert     else       import     pass
            break      except     in         raise
            






