# 011 Python data types

## Introduction


### Purpose

In this section we will learn some of the fundamental data types in Python (`int`, `float`, `str`, `bool`), how to convert between data types, and use of the `type()` function.


### Prerequisites

You will need some understanding of the following:

* [001 Using Notebooks](001_Notebook_use.md)
* [003 Getting help](003_Help.md)
* [010 Variables, comments and print()](010_Python_Introduction.md)

Remember that you can 'run' the code in a code block using the 'run' widget (above) or hitting the keys ('typing') <shift> and <return> at the same time. 


## Data types

### Data types: `str`

Recall how we can print out a message by first storing the text in a variable:


```python
# set a variable called message to contain the string hello world
message = 'hello world'

# print the value of the variable message
print(message)
```

    hello world



Above, we set the variable to be a string `str` type, because we wanted to use it to represent a string.

In a string, each character is represented by an [ASCII](http://www.asciitable.com) codes.

So the [string](https://en.wikibooks.org/wiki/Python_Programming/Text) `one` is built up of `o` + `n` + `e`, represented by the ASCII codes `111`, `110` and `101` respectively.


#### Exercise 1

* If the ASCII code for `e` is `101` and the code for `n` is `110`, what is the code for `a`?

### `len()`

We can find the length of the string using the function `len()`, for example:


```python
# set a variable called message to contain the string hello world
message = 'hello world'

# print the value of the variable message
print(message,len(message))
```

    hello world 11


#### Exercise 2

* in a code cell below, create a variable called `name` and set it to your name
* print the string name, and its length
* comment on why the length is the value you find

### `type()`

In a computing language, the *sort of thing* the variable can be set to is called its **data type**.  In Python, we can access this with the function `type()`:




```python
# assign the value 'one' to the variable (key) my_store
my_store = 'one'

# Print the value of my_store
print('this has type', type(my_store))
```

    this has type <class 'str'>


#### Exercise 3

* insert a new cell below here
* set a variable called message to contain the string `hello world`
* print the value and data type of the variable message

### Data types: `float`

Another fundamental data type is `float`, used to store decimal numbers such as `120.23`.

Not surprisingly, we can use floating point numbers (and other number representations) to do arithmetic. We can use `print()` similarly to above to print an integer value. 

Sometimes, such as for very large or very small floating point values, we use [scientific notation](https://en.wikibooks.org/wiki/A-level_Computing/AQA/Paper_2/Fundamentals_of_data_representation/Floating_point_numbers), e.g. to represent Plank's constant:

$$h = 6.62607015 \times 10^{−34} J \dot s $$
    
we would not want to have to write out over zero values after the decimal point. Instead, we use the **mantissa** $6.62607015$ and **exponent** $-34$ directly:

     h = 6.62607015e-34


You will sometimes see float numbers represented in this way. It is of additional interest because it is related more closely to how floating point numbers are [stored on a computer](https://users.cs.fiu.edu/~downeyt/cop2400/float.htm#:~:text=Eight%20digits%20are%20used%20to,means%20negative%2C%200%20means%20positive.).

As an example of floating point arithmetic, let us consider the energy associated with a photon of a given wavelength $\lambda$ (nm) using the [Planck-Einstein equation](https://web.archive.org/web/20160712123152/http://pveducation.org/pvcdrom/2-properties-sunlight/energy-photon):

$$ E = \frac{hc}{\lambda}$$

with:

* $h$ as above, $=6.62607015 \times 10^{−34} J \dot s$
* $c$ the speed of light $= 2.99792458 \times 10^8 m/s$
* $E$ the photon energy (in $J$)

Given light with a wavelength of 1024 nanometers ($nm$), calculate the energy in $J$.

First, since

$$1\ nm = 1 \times 10^{−9} m$$

we calculate the wavelength in $m$:

    l_m = l_nm * 1e-9

Then, implement the Planck-Einstein equation:

    E = h * c / l_m



```python
# values of c and h
# in scientific notation
c = 2.99792458e8       # m/s
h = 6.62607015e-34     # J s

# wavelength in nm
l_nm = 1024.0          # nm

# wavelength in m
l_m = l_nm * 1e-9      # m

# Planck-Einstein in J
E_J = h * c / l_m      # J

print('Photon of wavelength', l_nm, 'nm')
print('has an energy of', E_J, 'J')
```

    Photon of wavelength 1024.0 nm
    has an energy of 1.9398885323720004e-19 J


 We can compare the value of energy we get in $J$ with that using a [web calculator](http://www.calctool.org/CALC/other/converters/e_of_photon) and confirm the value of `1.93989e-19` for Near Infrared light (`1024` nm).

#### Exercise 4

Since the energy level expressed in $J$ is quite small, we might more conveniently express it in units of eV. Given that:

$$
    1\ Electron\ volt\ (eV) = 1.602176565 \times 10^{-19} J
$$

* Insert a new cell below here
* calculate the energy associated with a blue photon at 450 nm, in eV
* confirm your answer using a [web calculator](http://www.calctool.org/CALC/other/converters/e_of_photon)

### Data types: `int`

Another fundamental data type is `int`, used to store integer (whole) numbers (in base 10). We often use them for counting and similar tasks.


```python
i = 0
print(i,'this has type', type(i))

# increment i by 1
# same as i = i + 1
i += 1
print('increment i:',i)
i += 1
print('increment i:',i)
```

    0 this has type <class 'int'>
    increment i: 1
    increment i: 2


Not surprisingly, we can also use integers to do all sorts of arithmetic. Because of potential rounding issues though, we have to pay a little attention to whether we want the result of division to remain an integer or become a floating point number. 

We can use `print()` similarly to above to print an integer value.


```python
# set the variable x,m and c to integer
# values
x = 10
m = 20
c = 6

# calculate y from the formula
y = m * x + c

# print the value of y
print('y =', y)
```

    y = 206


We have seen examples of addition `+` and multiplication `*`. We use `x ** y` to represent `x` to the power of `y`. For division, we use `//` to enforce integer division ([floor division](https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html)).



#### Exercise 5

* insert a new cell below here
* using integer arithmetic, print the result of:
  - 2 to the power of 8
  - 1024 divided by 2
* set a variable called `x` to the result of 7 (floor) divided by 3.
  - print the value of `x`, and confirm its data type is `int`

### Data types: `bool`

The last fundamental data type we will deal with here is the Boolean or 'logical' type `bool`. Here, a variable can represent the value of `True` (equivalent to `1`) or `False` (equivalent to `0`).

There are a great many uses for this in using logic in coding.


```python
# examples of bool type
is_set = True
is_ready = False
```

#### Exercise 6

* Insert a new cell below here
* Set a variable called `is_class_today` to the value `True`
* print the variable name, its value, and its data type

### Logical Operators: `not`, `and`, `or`

Logical operators combine boolean variables. Recall from above:


```python
print (type(True),type(False));
```

    <class 'bool'> <class 'bool'>


The three main logical operators you will use are:

    not, and, or
   
The impact of the `not` operator should be straightforward to understand, though we can first write it in a 'truth table':   



| A  | not A  | 
|:---:|:---:|
|  T | F | 
|   F |  T | 


```python
print('not True is',not True)
print('not False is',not False)
```

    not True is False
    not False is True


#### Exercise 7
   
* Insert a new cell below here
* write a statement to set a variable `x` to `True` and print the value of `x` and `not x` 
* what does `not not x` give? Make sure you understand why 


The operators `and` and `or` should also be quite straightforward to understand: they have the same meaning as in normal english. Note that `or` is 'inclusive' (so, read `A or B` as 'either A or B or both of them').


```python
print('True and True is', True and True)
print('True and False is', True and False)
print('False and True is', False and True)
print('False and False is', False and False)
```

    True and True is True
    True and False is False
    False and True is False
    False and False is False


So, `A and B` is `True`, if and only if both `A` is `True` and `B` is `True`. Otherwise, it is `False`

We can represent this in a 'truth table':


| A  | B  | A and B  | 
|:---:|:---:|:---:|
|  T |  T |  T | 
|  T |  F |  F | 
|  F |  T |  F | 
|  F |  F |  F | 



#### Exercise 8

* draw a truth table *on some paper*, label the columns `A`, `B` and `A and B` and fill in the columns `A` and `B` as above
* without looking at the example above, write the value of `A and B` in the third column.
* draw another truth table *on some paper*, label the columns `A`, `B` and `A and B` and fill in the columns `A` and `B` as above
* write the value of `A or B` in the third column.

If you are unsure, test the response using code, below:

We can apply these principles to more complex compound statements. In building a truth table, we must state all of the possible permutations for the variables.

For two variables (`A` and `B`) we had:


| A  | B  | 
|:---:|:---:
|  T |  T | 
|  T |  F |  
|  F |  T |  
|  F |  F | `



Notice the pattern of alternating `T` and `F` in the columns.

For three variables, the equivalent table is:

| A  | B  | C | 
|:---:|:---:|:---:|
| T|  T |  T |  
| T|  T |  F |  
| T|  F |  T | 
| T |  F |  F |  
| F|  T |  T |  
| F|  T |  F |   
| F|  F |  T |  
| F|  F |  F |  


Again, notice the alternating patterns in the columns so that we cover all permutations.




#### Exercise 9

* Copy the 3 variable truth table from above onto paper 
* fill out a column with `A and B`
* fill out a column with `((A and B) or C) `
* Try some other compound statements

If you are unsure, or to check your answers, test the response using code, below.

## Conversion between data types

You can explicitly convert between ('cast') data types **where this makes sense** using:

    int()
    float()
    str()
    bool()


```python
start_number = 1
print("starting with",start_number)

int_number = int(start_number) 
print('int_number',int_number,type(int_number))

# now convert to float
float_number = float(start_number)
print('float_number',float_number,type(float_number))

# now convert to str
str_number = str(start_number)
print('str_number',str_number,type(str_number))

# now convert to bool
bool_number = bool(start_number)
print('bool_number',bool_number,type(bool_number))

```

    starting with 1
    int_number 1 <class 'int'>
    float_number 1.0 <class 'float'>
    str_number 1 <class 'str'>
    bool_number True <class 'bool'>


#### Exercise 10

* insert a new cell below here
* copy the code in the cell above, set `start_number` to `0`, and run
    * What are the boolean representations of `0` and `1`?
* What would happen if you set `start_number` to the string `'zero'`, and why?

## Summary

In this section, we have been introduced to the core data types in Python:

|core data types| example |
|---|-|
|`int`| `x = 10`|
|`float`| `x = 10.0`|
|`str`| `x = "hello world"`|
|`bool`| `x = False` |

and how to convert ('cast') between then, where this is feasible:

| cast functions |
|---|
|`int()`|
|`float()`|
|`str()`|
|`bool()`|

Other functions:

|  command | purpose  |   
|-|---|
| `type(v)` | data type of object `v`|
| `len(v)` | length of object `v` (e.g. `str`) |

We have learned truth tables to list logical operations:


| A  | B  | A and B  | 
|:---:|:---:|:---:|
|  T |  T |  T | 
|  T |  F |  F | 
|  F |  T |  F | 
|  F |  F |  F | 



| A  | B  | A or B  | 
|:---:|:---:|:---:|
|  T |  T |  T | 
|  T |  F |  T | 
|  F |  T |  T | 
|  F |  F |  F | 

| A  | not A  | 
|:---:|:---:|
|  T | F | 
|   F |  T | 
    
