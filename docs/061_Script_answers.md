# Formative Assessment: Scripts : Answers to exercises

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


```bash
%%bash
# ANSWER 1
#

# code between the next line and the 
# End Of File (EOF) marker will be saved in 
# to the file work/greet.py
cat << EOF > work/greet.py
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

'''
greet

Purpose:

  script to print hello from name
  
'''
__author__    = "P Lewis"
__copyright__ = "Copyright 2020 P Lewis"
__license__   = "GPLv3"
__email__     = "p.lewis@ucl.ac.uk"

'''
Instructions:
Create a Python code in a file called work/greet.py that does the following:
define a function greet(name) that prints out a greeting from the name 
  in the argument name
define a function main() that passes a string from the script command 
  line to a function greet(name)
calls main() if the file is run as a Python script
has plentiful commenting and document strings
'''

# define a function greet(name) that prints 
#   out a greeting from the name in the argument name
def greet(name):
    '''
    function to print "greetings from {name}"
    '''
    print(f'greetings from {name}')
    
    
# define a function main() that passes a string 
#   from the script command line to a function greet(name)

# call name with a string 
# name that we pass to greet(name)
def main(name):
    greet(name)

# calls main() if the file is run as a Python script
if __name__ == "__main__":
    # execute only if run as a script
    # we pass the first command line argument argv[1]
    # remembering that argv[0[ is the program name
    main(sys.argv[1])
EOF

# Chmod 755 to make the file executable
chmod 755 work/greet.py
```


```python
msg = '''
As a test, when you run the script:

  %run work/greet.py Fred
you would expect to get a response of the form:

  greetings from Fred
and if you run:

  %run work/greet.py Hermione
then

  greetings from Hermione

'''
print(msg)

print('work/greet.py Fred ->')
%run work/greet.py Fred
print('work/greet.py Hermione ->')
%run work/greet.py Hermione
```

    
    As a test, when you run the script:
    
      %run work/greet.py Fred
    you would expect to get a response of the form:
    
      greetings from Fred
    and if you run:
    
      %run work/greet.py Hermione
    then
    
      greetings from Hermione
    
    
    work/greet.py Fred ->
    greetings from Fred
    work/greet.py Hermione ->
    greetings from Hermione



```bash
%%bash
# ANSWER 2
#
# To go further with this exercise, you might test to see that the length of sys.argv is as long as you expect it to be, 
# so you can tell the user when they forget to include the name

# code between the next line and the 
# End Of File (EOF) marker will be saved in 
# to the file work/greet.py
cat << EOF > work/greet.py
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# import required package(s)
import sys

'''
greet

Purpose:

  script to print hello from name
  
'''
__author__    = "P Lewis"
__copyright__ = "Copyright 2020 P Lewis"
__license__   = "GPLv3"
__email__     = "p.lewis@ucl.ac.uk"



'''
Instructions:

Create a Python code in a file called work/greet.py that does the following:
define a function greet(name) that prints out a greeting from the name 
  in the argument name
define a function main() that passes a string from the script command 
  line to a function greet(name)
calls main() if the file is run as a Python script
has plentiful commenting and document strings
'''

# define a function greet(name) that prints 
#   out a greeting from the name in the argument name
def greet(name):
    '''
    function to print "greetings from {name}"
    '''
    print(f'greetings from {name}')
    
    
# define a function main() that passes a string 
#   from the script command line to a function greet(name)

# call name with a string 
# name that we pass to greet(name)
def main(name):
    greet(name)

# calls main() if the file is run as a Python script
if __name__ == "__main__":
    # execute only if run as a script
    # we pass the first command line argument argv[1]
    # remembering that argv[0[ is the program name
    
    # TEST for string length in here:
    # To go further with this exercise, you might test to see that the length of sys.argv is as long as you expect it to be, 
    # so you can tell the user when they forget to include the name
    if len(sys.argv) > 1:
      main(sys.argv[1])
    else:
      print(f'{sys.argv[0]}: error - no command line name given')
EOF

# Chmod 755 to make the file executable
chmod 755 work/greet.py
```


```python
# test
print('work/greet.py  ->')
%run work/greet.py 
print('work/greet.py Hermione ->')
%run work/greet.py Hermione
```

    work/greet.py  ->
    work/greet.py: error - no command line name given
    work/greet.py Hermione ->
    greetings from Hermione



```bash
%%bash
# ANSWER 3
#
# To go even further with this exercise, you might attempt to 
# make the script function so that if you run it as:
# %run work/greet.py Fred Hermione
# it responds:
#   greetings from Fred
#   greetings from Hermione
# in many ways, this is easier than answer 2
# as we just use a loop

# code between the next line and the 
# End Of File (EOF) marker will be saved in 
# to the file work/greet.py
cat << EOF > work/greet.py
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# import required package(s)
import sys

'''
greet

Purpose:

  script to print hello from name
  
Author: P. Lewis
Email:  p.lewis@ucl.ac.uk
Date:   28 Aug 2020

Instructions:
Create a Python code in a file called work/greet.py that does the following:
define a function greet(name) that prints out a greeting from the name 
  in the argument name
define a function main() that passes a string from the script command 
  line to a function greet(name)
calls main() if the file is run as a Python script
has plentiful commenting and document strings
'''

# define a function greet(name) that prints 
#   out a greeting from the name in the argument name
def greet(name):
    '''
    function to print "greetings from {name}"
    '''
    print(f'greetings from {name}')
    
    
# define a function main() that passes a string 
#   from the script command line to a function greet(name)

# call name with a string 
# name that we pass to greet(name)
def main(name):
    greet(name)

# calls main() if the file is run as a Python script
if __name__ == "__main__":
    # execute only if run as a script
    # we pass the first command line argument argv[1]
    # remembering that argv[0[ is the program name
    
    # To go even further with this exercise, you might attempt to 
    # make the script function so that if you run it as:
    # %run work/greet.py Fred Hermione
    # it responds:
    #   greetings from Fred
    #   greetings from Hermione
    # in many ways, this is easier than answer 2
    # as we just use a loop
    for n in sys.argv[1:]:
      # and call main() with n
      main(n)
EOF

# Chmod 755 to make the file executable
chmod 755 work/greet.py
```


```python
# test
# separate the responses to see them easier
dash = '\n'+'='*10

print(f'{dash}\nwork/greet.py  ->{dash}')
%run work/greet.py 
print(f'{dash}\nwork/greet.py Hermione ->{dash}')
%run work/greet.py Hermione
print(f'{dash}\nwork/greet.py Hermione Fred ->{dash}')
%run work/greet.py Hermione Fred
```

    
    ==========
    work/greet.py  ->
    ==========
    
    ==========
    work/greet.py Hermione ->
    ==========
    greetings from Hermione
    
    ==========
    work/greet.py Hermione Fred ->
    ==========
    greetings from Hermione
    greetings from Fred

