## 022 Read Files : Answers to exercises


```python
# ANSWER

# print out the absolute pathname of the 
# directory that images/ucl.png is in
ucl = Path('images','ucl.png')

# use absolute and parent
# Use name to show how that is helpful
print(f'The directory {ucl.name} is in is: {ucl.absolute().parent}')

# check that the file exists
# if it does ...
if ucl.exists():
    # print the size of the file in KB to two decimal places

    # from above, use stat().st_size
    size_in_bytes = ucl.stat().st_size
    # 1024 Bytes -> 1 KB
    size_in_KB = size_in_bytes/1024
    # 2 dp -> : .2f
    print(f'file size {size_in_bytes} Bytes -> {size_in_KB : .2f} KB')
else:
    print(f'file does not exist')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-705fcb765e4e> in <module>
          3 # print out the absolute pathname of the
          4 # directory that images/ucl.png is in
    ----> 5 ucl = Path('images','ucl.png')
          6 
          7 # use absolute and parent


    NameError: name 'Path' is not defined


##### Exercise 1

* Using `Path.read_text()` read the text from the file `work/easy.txt` and print the text returned.
* split the text into lines of text using `str.split()` at each newline, and print out the resulting list

You learned how to split strings in [013_Python_string_methods](013_Python_string_methods.md#split()-and-join())


```python
# ANSWER
# Using `Path.read_text()` read the text from the 
# file `work/easy.txt` and print the text returned.

text = Path('work/easy.txt').read_text()
print(f'I have read:\n{text}')

# split the text into lines of text using `str.split()` 
# at each newline, and print out the resulting list
text_list = text.split('\n')
print(f'lines list:\n{text_list}')
```

##### Exercise 2

XXX TODO XXX


```python
# ANSWER
```


```python
# ANSWER
# Using Path.read_text() read the text from the file work/easy.txt 
# and print the text returned.

# set up the filename
infile = Path('work','easy.txt')
# read the text
read_text = infile.read_text()

# split the text into lines of 
# text using str.split() at each newline, 
# and print out the resulting list
lines = read_text.split('\n')
print(lines)
```

##### Exercise 3

Using the code:
    
    from  geog0111.modis import Modis

    # get URL
    modis = Modis('MCD15A3H',verbose=True)
    url = modis.get_url("2020","01","01")[0]
    # set the output directory
    url.local_dir = 'work'
    
    # read the dataset
    hdf_data = url.read_bytes()
    # and save to a file
    obytes = url.write_bytes(hdf_data,verbose=True)    

* write a function that only calls `url.read_bytes()` if the file doesn't already exist
* If it already exists, just read the data from that file
* test your code with the url generated above and show that the file size is 9067184 bytes

You will need to remember how to get the filename from the URL object, and also to test if a file exists. We learned all of these in [020_Python_files](020_Python_files.md).

Note that `len(data)` will give the size of bytes data.


```python
# ANSWER

# write a function that only calls url.read_bytes() 
# if the file doesn't already exist
def get_data(url,verbose=False,local_dir='work'):
    '''
    Get the binary data from url if the 
    output file doesnt exist
    
    Positional Arguments:
    url  : a URL object
    
    Keyword Arguments:
    verbose  : Bool -> False
    local_dir : str -> work
    '''
    # get the output file name
    # url.name gives the file name from the URL
    ofile = Path(local_dir,url.name)
    
    # test exists
    if ofile.exists():
        # If it already exists, 
        # just read the data from that file
        return ofile.read_bytes()
    
    # otherwise read data from url:
    # set output dir
    url.local_dir = local_dir
    # pass on verbose flag
    hdf_data = url.read_bytes(verbose=verbose)
    # 
    obytes = url.write_bytes(hdf_data,verbose=True)
    return hdf_data
```


```python
# ANSWER

from  geog0111.modis import Modis
modis = Modis('MCD15A3H',verbose=False)
url = modis.get_url("2020","01","01")[0]

hdf_data = get_data(url,verbose=True,local_dir='work')
assert len(hdf_data) ==  9067184
print('passed')
```

##### Exercise 4

* print out the absolute pathname of the directory that the binary file [`images/ucl.png`](images/ucl.png) is in
* print the size of the file in kilobytes (KB) to two decimal places without reading the datafile. 
* read the datafile, and check you get the same data size

You will need to recall how to find a file size in bytes using `Path`. This was covered in [020_Python_files](020_Python_files.md). You will need to know how many bytes are in a KB. To print to two decimal places, you need to recall the string formatting we did in [012_Python_strings](012_Python_strings.md#String-formating).


```python
# ANSWER 

# print out the absolute pathname of the 
# directory that images/ucl.png is in
abs_name = Path('images/ucl.png').absolute()
print(abs_name)

# we want the parent!
print(f'the file {abs_name.name} is in {abs_name.parent}')

# print the size of the file in bytes without reading the datafile. 
print(f'{abs_name.name} has size {abs_name.stat().st_size} bytes')

# 1 KB is 1024 Bytes
# .2f is 2 d.p. format
print(f'{abs_name.name} has size ' +\
      f'{abs_name.stat().st_size/1024:.2f} KB')

# read the datafile, and check you get the same data size
dataset = abs_name.read_bytes()
# size
s = len(dataset)
print(f'the size of data read is {s} bytes -> {s/1024 : .2f} KB')
```
