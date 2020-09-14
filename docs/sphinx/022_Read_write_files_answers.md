# 021 Read and Write: URLs and files : Answers to exercises

#### Exercise 1

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

    I have read:
    
    It is easy for humans to read and write.
    It is easy for machines to parse and generate. 
    
    lines list:
    ['', 'It is easy for humans to read and write.', 'It is easy for machines to parse and generate. ', '']



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

    ['', 'It is easy for humans to read and write.', 'It is easy for machines to parse and generate. ', '']


#### Exercise 2

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
from geog0111.gurlpath import URL
from pathlib import Path

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
        url.msg('Reading existing file')
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

    passed


#### Exercise 3

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

    /Users/plewis/Documents/GitHub/geog0111/notebooks/images/ucl.png
    the file ucl.png is in /Users/plewis/Documents/GitHub/geog0111/notebooks/images
    ucl.png has size 1956 bytes
    ucl.png has size 1.91 KB
    the size of data read is 1956 bytes ->  1.91 KB

