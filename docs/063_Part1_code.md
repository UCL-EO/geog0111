# Code Advice

You need to submit you coursework in the usual manner by the date given above.

You **must** work individually on this task. If you do not, it will be treated as plagiarism. By reading these instructions for this exercise, we assume that you are aware of the UCL rules on plagiarism. You can find more information on this matter in your student handbook. If in doubt about what might constitute plagiarism, ask one of the course conveners.



### Computer Code

#### General requirements

You will obviously need to submit computer codes as part of this assessment. Some flexibility in the style of these codes is to be expected. For example, when asked to write a function, so students might choose to modularise and test the problem further and have multiple sub-functions that are finally called from the required function. This is fine to do, and can often be a good idea if the problem is complex or there are re-usable modular parts of code you might want to use (e.g. for printing). 

If you want to achieve distinction-level marks, then, on top of the main requirements we lay out here, we would be looking for features such as: maturity and detail in testing your codes; excellent code style; excellent presentation; and flexibility in the code (e.g. don't fix variable you can make variables or keywords).

All codes needed to demonstrate that you have performed the core tasks are required to be included in the submission. 

All codes should be well-commented. Part of the marks you get for code will depend on the adequacy of the document strings and commenting.

#### Degree of original work required and plagiarism

If you use a piece of code verbatim that you have taken from the course pages or any other source, **you must acknowledge this** in comments in your text. **Not to do so is plagiarism**. Where you have taken some part (e.g. a few lines) of someone else's code, **you should also indicate this**. If some of your code is heavily based on code from elsewhere, **you must also indicate that**.

Some examples. 

The first example is guilty of strong plagiarism, it does not seek to acknowledge the source of this code of code from one of the course pages, even though it is just a direct copy, pasted into a method called `model()`:


```python
def model(tempThresh=9.0,K=2000.0,p=0.96):
    '''...'''
    import numpy as np
    meltDays = np.where(temperature > tempThresh)[0]
    accum = snowProportion*0.
    for d in meltDays:
        water = K * snowProportion[d]
        n = np.arange(len(snowProportion)) - d
        m = p ** n
        m[np.where(n<0)]=0
        accum += m * water
    return accum
```

This is **not** acceptable.

This would be better as:


```python
'''
This code is taken directly from
"Modelling delay in a hydrological network"
by P. Lewis http://www2.geog.ucl.ac.uk/~plewis/geogg122/DelNorte.html
and wrapped into a method.
'''
def model(tempThresh=9.0,K=2000.0,p=0.96):
    '''...'''
    # my code: make sure numpy is imported
    import numpy as np

    # code below verbatim from Lewis REF XXX
    meltDays = np.where(temperature > tempThresh)[0]
    accum = snowProportion*0.
    for d in meltDays:
        water = K * snowProportion[d]
        n = np.arange(len(snowProportion)) - d
        m = p ** n
        m[np.where(n<0)]=0
        accum += m * water
    # my code: return accumulator
    return accum
```

Now, we acknowledge that this is in essence a direct copy of someone else’s code, and clearly state this. We do also show that we have added some new lines to the code, and that we have wrapped this into a method.

In the next example, we have seen that the way m is generated is in fact rather inefficient, and have re-structured the code. It is partially developed from the original code, and acknowledges this:


```python
'''
This code after the model developed in
"Modelling delay in a hydrological network"
by P. Lewis
http://www2.geog.ucl.ac.uk/~plewis/geogg122/DelNorte.html

My modifications have been to make the filtering more efficient.
'''
def model(tempThresh=9.0,K=2000.0,p=0.96):
    '''...'''

    # my code: make sure numpy is imported
    import numpy as np

    # code below verbatim from Lewis unless otherwise indicated
    meltDays = np.where(temperature > tempThresh)[0]
    accum = snowProportion*0.

    # my code: pull the filter block out of the loop
    n = np.arange(len(snowProportion))
    m = p ** n

    for d in meltDays:
        water = K * snowProportion[d]

        # my code: shift the filter on by one day
        # ...do something clever to shift it on by one day

        accum += m * water
    # my code: return accumulator
    return accum
```

This example makes it clear that significant modifications have been made to the code structure (and probably to its efficiency) although the basic model and looping comes from an existing piece of code. It clearly highlights what the actual modifications have been. Note that this is not a working example! 

**Note also that this is a poor example of a function, as there is no real document string and little comment on the code operation.**

We stress that this must be your own work. We do not want you to get anyone else to significantly helped you to develop the code (e.g. written the main part of it for you & you've just copied that with some minor modifications). This is not acceptable, but if for some reason it does happen, you must acknowledge it in your submission.

If you take a piece of code from somewhere else and all you do is change the variable names and/or other cosmetic changes, you **must** acknowledge the source of the original code (with a URL if available).

Plagiarism in coding is a tricky issue. One reason for that is that often the best way to learn something like this is to find an example that someone else has written and adapt that to your purposes. Equally, if someone has written some tool/library to do what you want to do, it would generally not be worthwhile for you to write your own but to concentrate on using that to achieve something new. Even in general code writing (i.e. when not submitting it as part of your assessment) you and anyone else who ever has to read your code would find it of value to make reference to where you found the material to base what you did on. The key issue to bear in mind in this work, as it is submitted ‘as your own work’ is that, to avoid being accused of plagiarism and to allow a fair assessment of what you have done, you must clearly acknowledge which parts of it are your own, and the degree to which you could claim them to be your own.

For example, based on ... is absolutely fine, and you would certainly be given credit for what you have done. In many circumstances 'taken verbatim from ...' would also be fine (provided it is acknowledged) but then you would be given credit for what you had done with the code that you had taken from elsewhere (e.g. you find some elegant way of doing the graphs that someone has written and you make use of it for presenting your results).

The difference between what you submit here and the code you might write if this were not a piece submitted for assessment is that you the vast majority of the credit you will gain for the code will be based on the degree to which you demonstrate that you can write code to achieve the required tasks. There would obviously be some credit for taking codes from the coursenotes and bolting them together into something that achieves the overall aim: provided that worked, and you had commented it adequately and acknowledge what the extent of your efforts had been, you should be able to achieve a pass in that component of the work. If there was no original input other than vbolting pieces of existing code together though, you be unlikely to achieve more than a pass. If you get less than a pass in another component of the coursework, that then puts you in danger of an overall fail.

Provided you achieve the core tasks, the more original work that you do/show (that is of good quality), the higher the mark you will get. Once you have achieved the core tasks, even if you try something and don’t quite achieve it, is is probably worth including, as you may get marks for what you have done (or that fact that it was a good or interesting thing to try to do).

#### Documentation

Note: All methods/functions and classes must be documented for the code to be adequate. Generally, this will contain:

   - some text on the purpose of the method (/function/class)

   - some text describing the inputs and outputs, including reference to any relevant details such as datatype, shape etc where such things are of relevance to understanding the code.

   - some text on keywords, e.g.:


```python
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)

    Example taken verbatim from:
    http://www.python.org/dev/peps/pep-0257/
    """
    if imag == 0.0 and real == 0.0: return complex_zero

```

You should look at the [document on good docstring conventions](http://www.python.org/dev/peps/pep-0257/) when considering how to document methods, classes etc.

To demonstrate your documentation, you **must** include the help text generated by your code after you include the code. e.g.:


```python
def print_something(this,stderr=False):
    '''This does something.

    Keyword arguments:
    stderr -- set to True to print to stderr (default False)
    '''

    if stderr:
        # import sys.stderr
        from sys import stderr

        # print to stderr channel, converting this to str
        print >> stderr,str(this)

        # job done, return
        return

    # print to stdout, converting this to str
    print (str(this))

    return

```

Then the help text would be:


```python
help(print_something)
```

    Help on function print_something in module __main__:
    
    print_something(this, stderr=False)
        This does something.
        
        Keyword arguments:
        stderr -- set to True to print to stderr (default False)
    


The above example represents a ‘good’ level of commenting as the code broadly adheres to the style suggestions and most of the major features are covered. It is not quite ‘very good/excellent’ as the description of the purpose of the method (rather important) is trivial and it fails to describe the input this in any way. An excellent piece would do all of these things, and might well tell us about any dependencies (e.g. requires sys if stderr set to True).

An inadequate example would be:


```python
def print_something(this,stderr=False):
    '''This prints something'''
    if stderr:
        from sys import stderr
        print >> stderr,str(this)
        return
    print (str(this))
```

It is inadequate because it still only has a trivial description of the purpose of the method, it tells us nothing about inputs/outputs and there is no commenting inside the method.
