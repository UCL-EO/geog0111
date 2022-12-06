# 018 Python codes : Answers to exercises

#### Exercise 1

* Create a Python file in your [`work`](work) folder based on the example above and call it `work/myFirstCode.py`
* Modify the code to achieve the following:
    - make a function called `myFirstCode` that prints out a greeting message
    - update the document strings in the file as appropriate


```bash
%%bash
# ANSWER : create the Python file with the code we want

# Instructions:
#
# Create a Python file in your work
# folder based on the example in geog0111/helloWorld.py
# and call it `work/myFirstCode.py`
#
# Modify the code to achieve the following:
# make a function called myFirstCode that prints out a greeting message
# update the document strings in the file as appropriate

# code between the next line and the 
# End Of File (EOF) marker will be saved in 
# to the file work/myFirstCode.py
cat << EOF > work/myFirstCode.py
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
myFirstCode

  function to print a greeting
  
'''
__author__    = "P Lewis"
__copyright__ = "Copyright 2020 P Lewis"
__license__   = "GPLv3"
__email__     = "p.lewis@ucl.ac.uk"

def myFirstCode():
    '''function to print a greeting'''
    print('hello from me')
    
    
# example calling the function    
def main():
    myFirstCode()

if __name__ == "__main__":
    # execute only if run as a script
    main()
EOF

# Chmod 755 to make the file executable
chmod 755 work/myFirstCode.py
```


```python
# ANSWER
%run work/myFirstCode.py
```

    hello from me

