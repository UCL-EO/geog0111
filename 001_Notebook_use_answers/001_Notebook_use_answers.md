# Use of Jupyter notebooks : Answers to exercises

### Exercise: add a cell

We can add new cells to this document via the `Insert -> Insert Cell Below` menu in the menu bar at the top of this document.

Notice that you can double click on a cell to edit its contents.

Add a cell now, below, and use the `Cell -> Cell Type` menu to make this cell type `markdown`. Add some text in there ... lyrics from your favourite song, whatever you like ...


# ANSWER
This is a markdown cell ...

Hello world is traditionally the first coding you do.

### Exercise: add some cell formatting


Add another cell now, below, and use the Cell -> Cell Type menu to make this cell type markdown. 

Read up on the [features of markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), and this time, include one or more of the following in your cell:

* a heading
* a sub-heading
* and equation
* links to a web page
* a table
* a image
* some html

# ANSWER

# Main Heading

## equation

Equations 

\begin{equation*}
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
\end{equation*}

### link

[click me and I will pop up a google search window](https://www.google.com)

### table

| a | b | c | d | e |
|:-:|:-:|:-:|:-:|-|
| 🙈 | 💥 | 🦧 | 🐇 | 🐪 |
| f | g | h | i | j |
| 🙈 | 💥 | 🦧 | 🐇 | 🐪 |

### image

![ucl logo](images/ucl_logo.png)


### html

<html>
<body>
<h2>HTML</h2>

<p>Hey, I'm a paragraph!</p>


</body>
</html>

### Exercise

Now:

* create a code cell below
* create a string called `second_string` with the text `hello again`
* call the `print()` method with this as an [argument](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
* run the cell 


```python
# ANSWER
# create a code cell below
# create a string called `second_string` with the text `hello again`

second_string = 'hello again'

# call the `print()` method with this as an argument
print(second_string)

# run the cell 
```

    hello again


### Exercise

* create a code cell below
* print the values of `first_string` and `second_string`  that we created above. 
* what does that tell you about information we create in one cell and try to use in another?


```python
# ANSWER
# create a code cell below
# print the values of first_string and second_string that we created above.

print(first_string)
print(second_string)

# or

print(first_string,second_string)

# what does that tell you about information we create in one cell and try to use in another?
# 
# It tells us that the informnation is persistent, i.e. once we have created the 
# variables, we can use them in running any cells later.
```

    hello world
    hello again
    hello world hello again


### Exercise

* create a code cell below
* try to print a variable `third_string` (that you haven't yet created)
* run the cell
* what does this tell you about trying to print variables we haven't created?


```python
# ANSWER
# create a code cell below

# try to print a variable `third_string` that you haven't yet created
print(third_string)

# The first time we run it
# it comes up with an error
# NameError: name 'third_string' is not defined
# telling us that we have tried to access a variable name that
# we have not yet defined. Be aware of this type of error.

# what does that tell you about trying to print variables we haven't created?
#
# if we try to use a variable before we create it, the code will fail and throw
# an error. This is useful information: learn to read the errors and understand what
# it is telling you. 
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-6c032710a348> in <module>
          3 
          4 # try to print a variable `third_string` that you haven't yet created
    ----> 5 print(third_string)
          6 
          7 # The first time we run it


    NameError: name 'third_string' is not defined


### Exercise

* create a code cell below
* *now* create a string called `third_string` with the text `hello once more`
* run the cell, then the **cell above**
* what does that tell you about information we create in one cell and try to use in another above?


```python
# ANSWER
# create a code cell below
# now create a string called third_string with the text hello once more
third_string = 'hello once more'

# run the cell above
# same as ...
print(third_string)

# what does that tell you about information we create in one cell and 
# try to use in another above?
#
# we can run cells in any order. Once we had created third_string, the 
# previous exercise print(third_string) executed as we expected.
# The *Danger* is that the next time we run this notebook in cell order
# the cell above will fail again. Learn from the mistakes we make.
# Remember what this type of error can mean.
```

    hello once more

