#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
helloWorld

Purpose:

  a buggy code to dgub

'''  

__author__    = "P Lewis"
__copyright__ = "Copyright 2020 P Lewis"
__license__   = "GPLv3"
__email__     = "p.lewis@ucl.ac.uk"

def doit(n):
    '''
    function to doit
    
    '''
    for i in range(n):
        print('count {i}')
        print('finmished')
        return
    
    
# example calling the function   
def main(n):
    doit()

if __name__ == "__main__":
    # execute only if run as a script
    
    # pass first cmd lime argument to main
    main(sys.argv[1])
