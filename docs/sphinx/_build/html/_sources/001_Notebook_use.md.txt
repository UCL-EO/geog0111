# 001 Use of Jupyter notebooks

This is a Jupyter notebook designed to let you get used to notebooks, and to test your python and notebooks installation.

You can find much information on using notebooks on the [web](https://jupyter.org/), so you might start by exploring some of that.

You should do the tasks in this notebook before the first class. We need to assume at that class that you have the basic familiarity with notebooks you will gain here.

## Introduction

This is your first Jupyter notebook of the class. Jupyter notebooks will form the primary teaching and learning tool in this course. The format of the notebooks will be similar for all sessions. 

### Course material

You will find full, up to date information on this course GEOG0111 on the [UCL course moodle page](https://moodle.ucl.ac.uk/course/view.php?id=21495). 

### Course load

This course is intended to be 25 % of your course load for the term. You will find fuller information on the [GEOG0111 course moodle page](https://moodle.ucl.ac.uk/course/view.php?id=21495), but that percentage should give you some idea of the amount of effort we are expecting you to put in (on average) per week.

### Learning 

You will be expected to learn from what we present in these notebooks and by following up material referenced and wider resources. 

Learning is mostly blocked into two-week chunks, with a test you need to submit at the end of the block. You will receive feedback from your test submission to help you learn from what you have done well and not so well. It is important that you submit materials for these tests. It is not about 'getting the right answer', but giving us the opportunity to regularly gauge your progress.

There will be two pieces of work that you submit for formal assessment on the course: one half way through, and one at the end. Again, we will provide you with feedback on these.

You will be covering a number of notebooks per week in a learning chunk, and you will need to keep up. If you find you are having problems, or there are reasons you cannot work, you must let us know so we can help you.

We will provide more information on learning in this course and the resources you have access to on the course moodle page.

### Prerequisites

There are no prerequisites for this notebook.

Note that you can 'run' the code in a code block using the 'run' widget (above) or hitting the keys ('typing') <shift> and <return> at the same time. 

### Timing

The session should take around 20 minutes though you will spend longer on follow-up material and exercises. 
    

## Some resources

There is a useful [cheatsheet](https://www.anaconda.com/wp-content/uploads/2019/03/11-2018-JupyterLab-Notebook-Cheatsheet.pdf) on using Jupyter, and [another, on markdown syntax](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf) for you to use.

    
## Anaconda and Jupyter
    
We will be using software from the [anaconda distribution of python](https://anaconda.org/anaconda/python). This should already be installed for you if you are viewing this, but we can run some quick tests. Running the cell below (`>| Run`) should give, the following, or higher:
    
    jupyter core     : 4.6.1
    jupyter-notebook : 6.0.3
    ipython          : 7.12.0
    ipykernel        : 5.1.4
    jupyter client   : 5.3.4
    jupyter lab      : 1.2.6
    nbconvert        : 5.6.1
    ipywidgets       : 7.5.1
    nbformat         : 5.0.4
    traitlets        : 4.3.3
    conda 4.8.2
    Python 3.7.6
    
If that is not the case, then make a copy of what it does produce, and contact the course organisers through [moodle](https://moodle.ucl.ac.uk/course/view.php?id=21495). 




```bash
%%bash 
# tests 
jupyter --version
conda -V
python -V
```

    jupyter core     : 4.6.3
    jupyter-notebook : 6.1.3
    qtconsole        : 4.7.6
    ipython          : 7.18.1
    ipykernel        : 5.3.4
    jupyter client   : 6.1.7
    jupyter lab      : 2.2.6
    nbconvert        : 5.6.1
    ipywidgets       : 7.5.1
    nbformat         : 5.0.7
    traitlets        : 4.3.3
    conda 4.8.4
    Python 3.7.8


The code cell above that we ran is a [`unix` (`bash`) shell](https://en.wikipedia.org/wiki/Bash_(Unix_shell)), indicated by the [cell magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html) `%%bash` on the first line. This is a mechanism that lets us run unix commands in a Python notebook.

## How we will be using notebooks

We will be using Jupyter notebooks to present course notes and view and run exercises. 

### Saving your work
   
The first thing we want you to do when you open a new notebook is to **make a copy of it in the [`work`](work) folder**. 

**You should make a copy of each new notebook when you start.** If you don't, then any work you do may not be there the next time you run the notebook. When you come back to run a notebook again, in a new session, you should run the saved notebook (unless you want to start afresh).


    
### Cells
    
The notebook is made up of a series of [cells](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#:~:text=A%20cell%20is%20a%20multiline,markdown%20cells%2C%20and%20raw%20cells). Some cells, such as the one this is written in, are 'text' cells, where we format the text in a language called [markdown](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html).

Take a few minutes to explore the notebook menu, and note how to do things like:

* save the notebook
* save the notebook with a checkpoint: useful for exercises, as you can go back to previous versions!
* make a copy of the notebook and rename it
* download the notebook as a pdf
* restart the kernel (the 'engine' running this notebook)
* restart the kernel and clear output

#### Exercise 1

We can add new cells to this document via the `Insert -> Insert Cell Below` menu in the menu bar at the top of this document.

Notice that you can double click on a cell to edit its contents.

Add a cell now, below, and use the `Cell -> Cell Type` menu to make this cell type `markdown`. Add some text in there ... lyrics from your favourite song, whatever you like ...


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

## Coding


###  hello world

Next, let's try a code cell below and do our first python coding. You should notice that it indicates this in the cell type box on the menu.

We will use the method `print()` to print out a `string` (a list of characters) called `first_string`.

We *execute* ('run') the code in the cell, either with the `>| Run` button above, or by pressing the `SHIFT RETURN` keys at the same time. 


```python
# comment with a hash

# set a string variable
first_string = "hello world"

# print this
print(first_string)
```

    hello world


The type of cell we use is `Code` (rather than `Markdown` above).

Remember that we *execute* ('run') the code in the cell, either with the `>| Run` button above, or by pressing the `SHIFT RETURN` keys at the same time. 

Try that out, running the code cell above.



#### Exercise 3

Now:

* create a code cell below
* create a string called `second_string` with the text `hello again`
* call the `print()` method with this as an [argument](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
* run the cell 

#### Exercise 4

* create a code cell below
* print the values of `first_string` and `second_string`  that we created above. 
* what does that tell you about information we create in one cell and try to use in another?

#### Exercise 5

* create a code cell below
* try to print a variable `third_string` (that you haven't yet created)
* run the cell
* what does this tell you about trying to print variables we haven't created?

#### Exercise 6

* create a code cell below
* *now* create a string called `third_string` with the text `hello once more`
* run the cell, then the **cell above**
* what does that tell you about information we create in one cell and try to use in another above?

## Summary

This notebook has introduced you to using jupyter notebooks.

To make sure you understand it all, it is worthwhile restarting the kernel with cleared output (`Kernel -> Restart & Clear Output`() and running it all again. Once you are happy with that, you might try (`Kernel -> Restart & Run All`().

We have explored the notebook menu, and seen how to run cells, create new cells, and change the cell type to something appropriate (`Markdown` or `Code` here). 

We have seen how to set a string variable and print the value of that variable. 

We have noticed that variables are persistent between cells, so if we define a variable in one cell, we can use it *later on*. We have seen that if we try to access a variable before we have declared it, it will throw a `NameError`, telling us this. Having seen this type of error once, and understanding why it occurred should prepare us for the next time we see one similar.

We have seen one of the *dangers* of a notebook: it allows you to go back and forth running cells. This can lead to confusion, as the next time you run the same notebook in cell order, you may not get the same result! It is one of the most common mistakes for a beginner to make, so be aware of this, and try to always run the cells in the same order. **You can test for this type of error by restarting the kernel, clearing the output, and running all cells.**

We have written our very first `python` codes!
