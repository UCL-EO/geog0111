#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
tester2

Purpose:

  a test code to demonstrate debugging

'''  
import sys


__author__    = "P Lewis"
__copyright__ = "Copyright 2020 P Lewis"
__license__   = "GPLv3"
__email__     = "p.lewis@ucl.ac.uk"

def doit(n):
    '''
    function to count from 0 to n
    
    positional arguments:
    
        n : integer
    
    '''
    for i in range(n):
        print(f'count {i}')
    print('finished')
    return 
    
    
# example calling the function   
def main(n):
    doit(n)

if __name__ == "__main__":
    # execute only if run as a script
    
    # pass first cmd lime argument to main
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
