# Formative Assessment: Scripts


*Although we provide access to answers for this exercise, we want you to submit the codes you generate via Moodle, so that we can provide feedback. You should avoid looking at the answers before you submit your work. This submitted work does not count towards your course assessment, it is purely to allow us to provide some rapid feedback to you on how you are doing. You will need to put together a few elements from the notes so far to do all parts of this practical, but you should all be capable of doing it well. Pay attention to writing tidy code, with useful, clear comments and document strings.*

#### Exercise 1

* Create a Python code in a file called `work/greet.py` that does the following:
    - define a function `greet(name)` that prints out a greeting from the name in the argument  `name`
    - define a function `main() that passes a string from the script command line to a function `greet(name)`
    - calls `main()` if the file is run as a Python script 
    - show a test of the script working
    - has plentiful commenting and document strings
   
    - As a test, when you run the script:

            %run work/greet.py Fred

    you would expect to get a response of the form:

            greetings from Fred

    and if you run:
            %run work/greet.py Hermione

    then
            greetings from Hermione
    
* To go further with this exercise, you might test to see that the length of `sys.argv` is as long as you expect it to be, so you can tell the user when they forget toi include the name
* To go even further with this exercise, you might attempt to make the script function so that if you run it as:

        %run work/greet.py Fred Hermione
    
    it responds:

        greetings from Fred
        greetings from Hermione
