# 020 Files and other Resources : Answers to exercises

#### Exercise 1

* Use `Path` to show the file permissions of all files that end `.sh` in the directory `bin`


```python
# ANSWER
# Use Path to show the file permissions of
# all files that end .sh in the directory bin

# use glob to get a list of filenames in the directory bin 
# that end with .sh -> pattern *.sh using a wildcard
filenames = Path('bin').glob('*.sh')
# loop over the filenames
for f in filenames:
    print(f)
```

#### Exercise 2

* print out the absolute pathname of the directory that `images/ucl.png` is in
* print the size of the file in KB to two decimal places

You will need to know how many Bytes in a Kilobyte, and how to [format a string to two decimal places](012_Python_strings.md#String-formating).

#### Exercise 3

* Using `Path.read_text()` read the text from the file `work/easy.txt` and print the text returned.
* split the text into lines of text using `str.split()` at each newline, and print out the resulting list

You learned how to split strings in [013_Python_string_methods](013_Python_string_methods.md#split()-and-join())


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


```python
# ANSWER 
# following from above

# set up the filename
infile = Path('work','easy.txt')
# read the text
read_text = infile.read_text()

# print what we did
print(f'read\n"""{read_text}"""\nfrom {infile}')
```


```python
# ANSWER
import json

# show the size of the files 
# bin/copy/environment.json and bin/copy/environment.yml

# form the file names
json_file = Path('bin','copy','environment.json')
yaml_file = Path('bin','copy','environment.yml')
# loop and print size
for f in [json_file,yaml_file]:
    print(f'{f} : {f.stat().st_size} bytes')
```


```python
# ANSWER

# read the information from bin/copy/environment.json using Path and json.load() into a variable called 
# jenv and print the keys of the dictionary jenv

# open file for read
with json_file.open('r') as f:
    jenv = json.load(f)
    
print(f'jenv keys: {jenv.keys()}')

# use assert to check if the keys are the same
assert jenv.keys() == env.keys()
print('passed assertion')
```


```python
# ANSWER 

# print out the absolute pathname of the 
# directory that images/ucl.png is in
abs_name = Path('images/ucl.png').absolute()
print(abs_name)

# we want the parent!
print(f'the file {abs_name.name} is in {abs_name.parent}')

# print the size of the file in bytes
print(f'{abs_name.name} has size {abs_name.stat().st_size} bytes')

# 1 KB is 1024 Bytes
# .2f is 2 d.p. format
print(f'{abs_name.name} has size ' +\
      f'{abs_name.stat().st_size/1024:.2f} KB')
```

#### Exercise 1

* copy the code above, and modify so that datasets for months `['MAYJUN','JUNJUL','JULAUG']` are plotted on the graph

Hint: use a for loop


```python
# do exercise here
# ANSWER

import requests
import numpy as np
import io

# access dataset as above
url = "http://www.esrl.noaa.gov/psd/enso/mei.old/table.html"
txt = requests.get(url).text

# copy the useful data
start_head = txt.find('YEAR')
start_data = txt.find('1950\t')
stop_data  = txt.find('2018\t')

header = txt[start_head:start_data].split()
data = np.loadtxt(io.StringIO(txt[start_data:stop_data]),unpack=True)

# use zip to load into a dictionary
data_dict = dict(zip(header, data))


'''
Do the loop here
'''
for i,key in enumerate(['MAYJUN','JUNJUL','JULAUG']):
    # plot data
    '''
    Use enumeration i as figure number
    '''
    plt.figure(i,figsize=(12,7))
    plt.title('ENSO data from {0}'.format(url))
    plt.plot(data_dict['YEAR'],data_dict[key],label=key)
    plt.xlabel('year')
    plt.ylabel('ENSO')
    plt.legend(loc='best')
```

#### Exercise 2

* Using what you have learned above, access the Met Office data file [`https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt`](https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt) and create a 'data package' in a numpy`.npz` file that has keys of `YEAR` and each month in the year, with associated datasets of Monthly Southeast England precipitation (mm).
* confirm that tha data in your `npz` file is the same as in your original dictionary
* produce a plot of October rainfall using these data for the years 1900 onwards


```python
# do exercise here
# ANSWER

'''
Exploration of dataset shows:


Monthly Southeast England precipitation (mm). Daily automated values used after 1996.
Wigley & Jones (J.Climatol.,1987), Gregory et al. (Int.J.Clim.,1991)
Jones & Conway (Int.J.Climatol.,1997), Alexander & Jones (ASL,2001). Values may change after QC.
YEAR   JAN   FEB   MAR   APR   MAY   JUN   JUL   AUG   SEP   OCT   NOV   DEC   ANN
 1873  87.1  50.4  52.9  19.9  41.1  63.6  53.2  56.4  62.0  86.0  59.4  15.7  647.7
 1874  46.8  44.9  15.8  48.4  24.1  49.9  28.3  43.6  79.4  96.1  63.9  52.3  593.5

so we have 3 lines of header
then the column titles
then the data

we can define these as before using

txt.find('YEAR')
start_data = txt.find('1873')
stop_data = None


Other than the filenames then, the code
is identical
'''

import requests
import numpy as np
import io

# access dataset as above
url = "https://www.metoffice.gov.uk/hadobs/hadukp/data/monthly/HadSEEP_monthly_qc.txt"
txt = requests.get(url).text

# copy the useful data
start_head = txt.find('YEAR')
start_data = txt.find('1873')
stop_data  = None

header = txt[start_head:start_data].split()
data = np.loadtxt(io.StringIO(txt[start_data:stop_data]),unpack=True)

# use zip to load into a dictionary
data_dict = dict(zip(header, data))

filename = 'HadSEEP_monthly_qc.npz'

# save the dataset
np.savez_compressed(filename,**data_dict)
```


```python
# ANSWER

loaded_data = np.load(filename)

print(type(loaded_data))

# test they are the same using np.array_equal
for k in loaded_data.keys():
    print('\t',k,np.array_equal(data_dict[k], loaded_data[k]))
```


```python
# ANSWER

'''
October rainfall, 1900+
'''

year = loaded_data['YEAR']

# mask where years match
mask = year  >= 1900

oct = loaded_data['OCT']

# set invalid data points to nan
oct[oct<0] = np.nan

plt.plot(year[mask],oct[mask])
```
