# 010 Introduction to Python : Answers to exercises


```python
# a comment
```

<mark>**ANSWER**
    
<mark>Nothing 'apparently' happened, but really, the code block was interpreted as a set of Python commands and executed. As there is only a comment, there was no output.

#### Exercise 2

* Insert a new cell below here
* Print out the string `Today I am learning Python`.


```python
# ANSWER
print('Today I am learning Python')
```

    Today I am learning Python


#### Exercise 3

* Insert a new cell below here
* print a string `"all the world's a stage and all the men and women merely players"`
* print this same string, but with each word on a new line
* print this same string with two columns of words, for as many lines as needed


```python
#ANSWER

# print a string "all the world's a stage"
print("all the world's a stage and all the men and women merely players")
```

    all the world's a stage and all the men and women merely players



```python
#ANSWER

# print this same string, but with each word on a new line
print("all\nthe\nworld's\na\nstage\nand\nall\nthe\nmen\nand\nwomen\nmerely\nplayers")
```

    all
    the
    world's
    a
    stage
    and
    all
    the
    men
    and
    women
    merely
    players



```python
# ANSWER
# print this same string with two columns of words, for as many lines as needed
# This needs alternating newline and tab
print("all\tthe\nworld's\ta\nstage\tand\nall\tthe\nmen\tand\nwomen\tmerely\nplayers")
```

    all	the
    world's	a
    stage	and
    all	the
    men	and
    women	merely
    players


#### Exercise 4

* Insert a new cell below here
* set a variable called `message` to contain the string `hello world`
* print the value of the variable `message`


```python
# ANSWER

message = 'hello world'
print(message)
```

    hello world


#### Exercise 5

* Make a code cell below
* declare the variable `dash='\n----------'` and print it
* declare your own variables to contain the following values, trying to use a range of allowed names

            1, 2, 'one', 'hello world', '1\n2\n3\t 4 5 6\n😀, 我在这里'
            
* print the variables to see if they contain what you expect, followed in each instance by `dash` (to space the answers out)


```python
# ANSWER

# Make a code cell below
# declare the variable dash='\n----------' and print it
dash='\n----------'
print(dash)

# declare your own variables to contain the following values, trying to use a range of allowed names
#      1, 2, 'one', 'hello world', '1\n2\n3\t 4 5 6\n😀, 我在这里'

avar = 1
bvar = 2
one = 'one'
Hello = 'hello world'
string_thing = '1\n2\n3\t 4 5 6\n😀, 我在这里'

#print the variables to see if they contain what you expect, followed in each instance by dash (to space the answers out)
print(avar,dash)
print(bvar,dash)
print(one,dash)
print(Hello,dash)
print(string_thing,dash)
```

    
    ----------
    1 
    ----------
    2 
    ----------
    one 
    ----------
    hello world 
    ----------
    1
    2
    3	 4 5 6
    😀, 我在这里 
    ----------

