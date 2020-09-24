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
