# 001 Use of Jupyter notebooks : Answers to exercises

#### Exercise 1
 This is a test exercise


```python
# and this is a test answer
```

#### Exercise 1

We can add new cells to this document via the `Insert -> Insert Cell Below` menu in the menu bar at the top of this document.

Notice that you can double click on a cell to edit its contents.

Add a cell now, below, and use the `Cell -> Cell Type` menu to make this cell type `markdown`. Add some text in there ... lyrics from your favourite song, whatever you like ...


    
The markdown will be text, something like:
    
    This is a markdown cell ...

    Hello world is traditionally the first coding you do.
    
to produce:

This is a markdown cell ...

Hello world is traditionally the first coding you do.

#### Exercise 2


Add another cell now, below, and use the Cell -> Cell Type menu to make this cell type markdown. 

Read up on the [features of markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), and this time, include one or more of the following in your cell:

* a heading
* a sub-heading
* and equation
* links to a web page
* a table
* a image
* some html

Use:

        # Main Heading

for a heading called 'Main Heading'

Use:

        ## equation

For a sub-heading called 'equation' etc

Equations are of the form:

For example:

        \begin{equation*}
        \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
        \end{equation*}

A link is specified for link text in square brackets, followed by the the link URL in round brackets. For example:

        [click me and I will pop up a google search window](https://www.google.com)


A table  is formatted in columns defined by `|`. The first line of the table gives headings (e.g. `| a | b | `).  The second defines alignment (e.g. `|:-:|-|`). The rest if data columns separated by `|`. An example is:

        | a | b | c | d | e |
        |:-:|:-:|:-:|:-:|-|
        | 🙈 | 💥 | 🦧 | 🐇 | 🐪 |
        | f | g | h | i | j |
        | 🙈 | 💥 | 🦧 | 🐇 | 🐪 |

An image is similar syntax to a link, but with `!` in front. The text in the square bracket is `alt` text, and the link in round brackets points to the image, as a file or URL.

        ![ucl logo](images/ucl_logo.png)


You can enter blocks of HTML code, such as:

        <html>
        <body>
        <h2>HTML</h2>

        <p>Hey, I'm a paragraph!</p>


        </body>
        </html>


\begin{equation*}
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
\end{equation*}


[click me and I will pop up a google search window](https://www.google.com)


| a | b | c | d | e |
|:-:|:-:|:-:|:-:|-|
| 🙈 | 💥 | 🦧 | 🐇 | 🐪 |
| f | g | h | i | j |
| 🙈 | 💥 | 🦧 | 🐇 | 🐪 |


![ucl logo](images/ucl_logo.png)


<html>
<body>
<h2>HTML</h2>

<p>Hey, I'm a paragraph!</p>


</body>
</html>

#### Exercise 3

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


#### Exercise 4

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


#### Exercise 5

* create a code cell below
* try to print a variable `third_string` (that you haven't yet created)
* run the cell
* what does this tell you about trying to print variables we haven't created?


```python
# ANSWER
# create a code cell below

msg='''
The first time we run it, it comes up with an error
NameError: name 'third_string' is not defined
telling us that we have tried to access a variable name that
we have not yet defined. Be aware of this type of error.

what does that tell you about trying to print variables we haven't created?

if we try to use a variable before we create it, the code will fail and throw
an error. This is useful information: learn to read the errors and understand what
it is telling you. 
'''
print(msg)


# try to print a variable `third_string` that you haven't yet created
print(third_string)
```

    
    The first time we run it, it comes up with an error
    NameError: name 'third_string' is not defined
    telling us that we have tried to access a variable name that
    we have not yet defined. Be aware of this type of error.
    
    what does that tell you about trying to print variables we haven't created?
    
    if we try to use a variable before we create it, the code will fail and throw
    an error. This is useful information: learn to read the errors and understand what
    it is telling you. 
    



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /var/folders/p6/pjj7dk1j5hq9y5jw_z8qwg0w0000gp/T/ipykernel_93979/758698420.py in <module>
         18 
         19 # try to print a variable `third_string` that you haven't yet created
    ---> 20 print(third_string)
    

    NameError: name 'third_string' is not defined


#### Exercise 6

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

msg = '''
what does that tell you about information we create in one cell and 
try to use in another above?

we can run cells in any order. Once we had created third_string, the 
previous exercise print(third_string) executed as we expected.
The *Danger* is that the next time we run this notebook in cell order
the cell above will fail again. Learn from the mistakes we make.
Remember what this type of error can mean.
'''
print(msg)
```

    hello once more
    
    what does that tell you about information we create in one cell and 
    try to use in another above?
    
    we can run cells in any order. Once we had created third_string, the 
    previous exercise print(third_string) executed as we expected.
    The *Danger* is that the next time we run this notebook in cell order
    the cell above will fail again. Learn from the mistakes we make.
    Remember what this type of error can mean.
    

