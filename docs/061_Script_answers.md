# Formative Assessment: Scripts : Answers to exercises

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

 


```bash
%%bash
# ANSWER 1
#

# code between the next line and the 
# End Of File (EOF) marker will be saved in 
# to the file work/greet.py
cat << EOF > work/count.py
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys

'''
count

Purpose:

  script to prints out numbers from 0 to istop
  (inclusive) on the same line.
  
'''
__author__    = "P Lewis"
__copyright__ = "Copyright 2020 P Lewis"
__license__   = "GPLv3"
__email__     = "p.lewis@ucl.ac.uk"

'''
Create a Python code in a file called work/count.py 
that does the following:

- define a function count(istop) that prints out numbers 
  from 0 to istop (inclusive) on the same line. 
  Your function should test that the variable istop is an integer, 
  and if not, try to convert it to one 
  (hint: it might well be a string when you pass it 
  from sys.argv below).
- define a function main(vlist) that loops over each item 
  in the list vlist and sends it to count(...)
- calls main(vlist) if the file is run as a Python 
  script with vlist being all arguments after 
  sys.argv[0] on the  script command line
- show a test of the script working
- has plentiful commenting and document strings

- As a test, when you run the script:

        run work/count.py 4 5 

you would expect to get a response of the form:

        0 1 2 3 4
        0 1 2 3 4 5

'''

# define a function count(istop) that prints out numbers 
#  from 0 to istop (inclusive) on the same line. 
#  Your function should test that the variable istop is an integer, 
#  and if not, try to convert it to one 
def count(istop):
    '''
    print out numbers (integer)
    from 0 to istop (inclusive) on the same line.
    '''
    # force istop to be an integer
    # this will fail if you pass something 
    # that cant be made into an integer, so you could possibly 
    # be neater about trapping that
    istop = int(istop)
    
    # from 0 to istop (inclusive) on the same line.
    # several ways to do this e.g.
    print(' '.join([str(i) for i in range(istop+1)]))
    
    # return from function
    return
    
# - define a function main(vlist) that loops over each item 
#  in the list vlist and sends it to count(...)
def main(values):
    for istop in values:
        count(istop)

# calls main(vlist) if the file is run as a Python 
#  script with vlist being all arguments after 
#  sys.argv[0] on the  script command line
if __name__ == "__main__":
    # execute only if run as a script
    # we pass the first command line argument argv[1]
    # remembering that argv[0] is the program name
    
    # we pass the list *after* argument 0, i.e.
    # the slice argv[1:]
    main(sys.argv[1:])
EOF

# Chmod 755 to make the file executable
chmod 755 work/count.py
```


```python
msg = '''
As a test, when you run the script:

  %run work/count.py 4 5 
you would expect to get a response of the form:

  0 1 2 3 4
  0 1 2 3 4 5
'''
print(msg)

print('work/count.py 4 5 ->')
%run work/count.py 4 5
```

    
    As a test, when you run the script:
    
      %run work/count.py 4 5 
    you would expect to get a response of the form:
    
      0 1 2 3 4
      0 1 2 3 4 5
    
    work/count.py 4 5 ->
    0 1 2 3 4
    0 1 2 3 4 5



```python
istop = 10

msg = '''
some other ways to achieve the printing
'''
print(msg)
# as above: this is quite neat and Pythonic
# make a list of strings, then use join
# to make into a single string
print('1.',' '.join([str(i) for i in range(istop+1)]))


# use an explicit for loop 
# to build the string. Not the most
# Pythonic, but will work.
mystr = ''
# loop over each integer 
for i in range(istop+1):
    # extend the string in an f-string
    mystr = f'{mystr} {i}'    
print('2.',mystr)

# make use of changing end='\n' in print
# which you may recall from help(print)
print('3.',end=' ')
for i in range(istop+1):
    print(i,end=' ') 
```

    
    some other ways to achieve the printing
    
    1. 0 1 2 3 4 5 6 7 8 9 10
    2.  0 1 2 3 4 5 6 7 8 9 10
    3. 0 1 2 3 4 5 6 7 8 9 10 
