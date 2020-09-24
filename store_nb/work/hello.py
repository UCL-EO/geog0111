#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
hello

Purpose:

  function to print 'hello from {name}'
  
'''
__author__    = "P Lewis"
__copyright__ = "Copyright 2020 P Lewis"
__license__   = "GPLv3"
__email__     = "p.lewis@ucl.ac.uk"

def hello(name):
    '''
    function to print 'hello from {name}'
    '''
    print(f'hello from {name}')
    
# example calling the function    
def main():
    hello('Fred')

if __name__ == "__main__":
    # execute only if run as a script
    main()
