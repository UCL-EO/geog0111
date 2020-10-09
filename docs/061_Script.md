# Formative Assessment: Scripts


*Although we provide access to answers for this exercise, we want you to submit the codes you generate via Moodle, so that we can provide feedback. You should avoid looking at the answers before you submit your work. This submitted work does not count towards your course assessment, it is purely to allow us to provide some rapid feedback to you on how you are doing. You will need to put together a few elements from the notes so far to do all parts of this practical, but you should all be capable of doing it well. Pay attention to writing tidy code, with useful, clear comments and document strings.*

#### Exercise 1

* Create a Python code in a file called `work/count.py` that does the following:

    - define a function `count(istop)` that prints out numbers from 0 to `istop` **(inclusive)** on the same line. Your function should test that the variable `istop` is an integer, and if not, try to convert it to one (hint: it might well be a string when you pass it from `sys.argv` below).
    - define a function `main(vlist)` that loops over each item in the list `vlist` and sends it to `count(...)`
    - calls `main(vlist)` if the file is run as a Python script with `vlist` being **all arguments** after `sys.argv[0]` on the  script command line
    - show a test of the script working
    - has plentiful commenting and document strings
   
    - As a test, when you run the script:

            %run work/count.py 4 5 

    you would expect to get a response of the form:

            0 1 2 3 4
            0 1 2 3 4 5

 
