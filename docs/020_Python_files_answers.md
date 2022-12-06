# 020 Files, Streams and related issues : Answers to exercises

#### Exercise 1

There is a file called `environment.yml` in the directory `copy`.

* use `Path` to generate the a variable `copy_dir` containing the pathname of the `copy` directory
* create a variable `env_file` which adds add the file `environment.yml` to this 
* check to see if the file exists


```python
from pathlib import Path
# ANSWER

# There is a file called environment.yml in the directory copy.
# use Path to generate the a variable copy_dir containing the 
# pathname of the copy directory
copy_dir = Path('copy')

# create a variable env_file which adds add the file 
# environment.yml to this
env_file = copy_dir / 'environment.yml'
# or
env_file = Path(copy_dir,'environment.yml')

# check to see if the file exists
print(f'does {env_file} exist? {env_file.exists()}')
```

    does copy/environment.yml exist? True


#### Exercise 2

Create a zero-sized file called `hello.txt` in a directory `mystuff`, using `Path` and show that it exists and is a file. Then delete the file and directory.


```python
from pathlib import Path
# ANSWER
# import package

# Form the Path object for the file
myfile = Path('mystuff','hello.txt')

# Make sure the parent directory exists
myfile.parent.mkdir(parents=True,exist_ok=True)

# Create the zero-sized file
myfile.touch()

# Check it exists and is a file
print('=== now you see it ===')
print(f'Does {myfile.as_posix()} exist? {myfile.exists()}')
print(f'Is {myfile.as_posix()} a file? {myfile.is_file()}')

# delete the file 
myfile.exists() and myfile.is_file() and myfile.unlink()
# Check it exists and is a file
print("=== now you don't ===")
print(f'Does {myfile.as_posix()} exist? {myfile.exists()}')
print(f'Is {myfile.as_posix()} a file? {myfile.is_file()}')

# delete the directory -- the parent
mydir = myfile.parent
mydir.exists() and mydir.is_dir() and mydir.rmdir()
# Check it exists and is a dir
print("=== now you don't ===")
print(f'Does {mydir.as_posix()} exist? {mydir.exists()}')
print(f'Is {mydir.as_posix()} a file? {mydir.is_dir()}')
```

    === now you see it ===
    Does mystuff/hello.txt exist? True
    Is mystuff/hello.txt a file? True
    === now you don't ===
    Does mystuff/hello.txt exist? False
    Is mystuff/hello.txt a file? False
    === now you don't ===
    Does mystuff exist? False
    Is mystuff a file? False


#### Exercise 3

Create a zero-sized file in a new directory, and use `Path.stat()` to show it has size 0 bytes. Then tidy up by deleting the file and directory.


```python
from pathlib import Path
# ANSWER
# import package
# very similar to exercise 2 but now we need to check the size

# Form the Path object for the file
myfile = Path('mystuff','hello.txt')

# Make sure the parent directory exists
myfile.parent.mkdir(parents=True,exist_ok=True)

# Create the zero-sized file
myfile.touch()

# print the file size
print(f'The file size of {myfile.as_posix()} is {myfile.stat().st_size} bytes')

# delete the file 
myfile.exists() and myfile.is_file() and myfile.unlink()
# delete the directory -- the parent
mydir = myfile.parent
mydir.exists() and mydir.is_dir() and mydir.rmdir()
```

    The file size of mystuff/hello.txt is 0 bytes


#### Exercise 4

Use `Path.touch()` to update the modification time for the file `bin/README` and demonstrate that you have done this and that is the same as the current time (now).


```python
from pathlib import Path
from datetime import datetime
# ANSWER
# import packages

readme = Path('bin','README')

modified = readme.stat().st_mtime
h_modified = datetime.fromtimestamp(modified)

print(f'Before touch: time of most recent modification for {readme} is {h_modified}')

# touch the file
readme.touch()
modified = readme.stat().st_mtime
h_modified = datetime.fromtimestamp(modified)

print(f'After touch: time of most recent modification for {readme} is {h_modified}')
print(f'Now it is {datetime.now()}')
```

    Before touch: time of most recent modification for bin/README is 2022-09-29 15:46:20.737117
    After touch: time of most recent modification for bin/README is 2022-10-21 16:19:25.448961
    Now it is 2022-10-21 16:19:25.452844


#### Exercise 5

* Use `Path` to show the file permissions of all files that end `.md` in the directory `.` (current directory)


```python
from pathlib import Path
# ANSWER
# import packages

# Use Path to show the file 
# permissions of all files that end .md 
# in the directory . (current directory)

# Path().cwd() gives the current directory (.)
here = Path().cwd()

# clearly, this needs glob the pattern will be *.md
# use * to put output as list of arguments
print(*here.glob('*.md'))
```

    /nfs/cfs/home3/Ucour1/coursd0/geog0111/notebooks/Install.md /nfs/cfs/home3/Ucour1/coursd0/geog0111/notebooks/InstallGDAL.md /nfs/cfs/home3/Ucour1/coursd0/geog0111/notebooks/OutsideInstall-Docker-owner.md /nfs/cfs/home3/Ucour1/coursd0/geog0111/notebooks/OutsideInstall-Docker.md /nfs/cfs/home3/Ucour1/coursd0/geog0111/notebooks/OutsideInstall-Local.md /nfs/cfs/home3/Ucour1/coursd0/geog0111/notebooks/OutsideInstall-Requirements.md /nfs/cfs/home3/Ucour1/coursd0/geog0111/notebooks/README.md /nfs/cfs/home3/Ucour1/coursd0/geog0111/notebooks/TIMETABLE.md /nfs/cfs/home3/Ucour1/coursd0/geog0111/notebooks/Using-the-course-notes.md


#### Exercise 6

Copy the file [`geog0111/cylog.py`](geog0111/cylog.py) to a new directory `myfile` and confirm the size of the file copied. Tidy up by deleting the copied file.


```python
from pathlib import Path
# ANSWER
# import packages

# Copy the file geog0111/cylog.py to a new directory 
# myfile and confirm the size of the file copied. 
# Tidy up by deleting the copied file.

# setup Path object for ifile 
ifile = Path('geog0111','cylog.py')

# setup Path object for ofile 
ofile = Path('myfile',ifile.name)
# create directory 
ofile.parent.mkdir(parents=True,exist_ok=True)

# read ifile, write to ofile (text)
nbytes = ofile.write_text(ifile.read_text()) #for binary files
print(f'{nbytes} bytes written for {ofile}')

# tidy up and remove the file
ofile.unlink()
ofile.parent.rmdir()
```

    9249 bytes written for myfile/cylog.py


#### Exercise 8

* write code to read from the json-format file `bin/copy/environment.json` into a dictionary called `json_data`.
* print out the dictionary keys.
* print the file size of the json-format file in KB to two decimal places.


```python
# ANSWER
# write code to read from the json-format file 
# bin/copy/environment.json 
# into a dictionary called json_data.
json_file = Path('bin/copy/environment.json')

# use with ... as ... as we have been shown
with json_file.open('r') as f:
    json_data = json.load(f)
    
# print out the dictionary keys.
print(json_data.keys())

# print the file size of the 
# json-format file in KB to two decimal places.
print(f'file {json_file} size {json_file.stat().st_size / 1024 : .2f} KB')
```

    dict_keys(['name', 'channels', 'dependencies'])
    file bin/copy/environment.json size  0.78 KB


#### Exercise 9

* check that the file `images/ucl.png` exists and print modification time and the file size in KB to two decimal places
* make a directory `myfiles` and copy the file `images/ucl.png` to this directory
* show the file size of `myfiles/ucl.png`, the modification time, and the time now
* after that, tidy up by deleting the file `myfiles/ucl.png` and the directory `myfiles`. Confirm that you have done this.

You will need to know how many Bytes in a Kilobyte, and how to [format a string to two decimal places](012_Python_strings.md#String-formating). You will also need to remember how to use [`if` statements](015_Python_control.md#Comparison-Operators-and-if).


```python
from pathlib import Path
from datetime import datetime
# ANSWER
# import packages

# check that the file images/ucl.png exists and 
# print modification time and the file size in KB to two decimal places

# make a directory myfiles and copy the file images/ucl.png 
# to this directory
# show the file size of myfiles/ucl.png, the 
# modification time, and the time now
# after that, tidy up by deleting the file 
# myfiles/ucl.png and the directory myfiles. 
# Confirm that you have done this.

# check that the file images/ucl.png exists and 
# print modification time and the file size in KB to two decimal places

ifile = Path('images','ucl.png')
# check that the file images/ucl.png exists and 
print(f'The file {ifile} exists?: {ifile.exists()}')
# print the file in KB to two decimal places
# 1 KB = 1024 bytes
ifile_bytes = ifile.stat().st_size
print(f'The file {ifile} size: {ifile_bytes} B')
# in KB using .2f format for 2 dp
ifile_size_kb = ifile.stat().st_size / 1024
print(f'The file {ifile} size: {ifile_size_kb : .2f} KB')

# show the file size of myfiles/ucl.png, the 
# modification time, and the time now

modified = ifile.stat().st_mtime
h_modified = datetime.fromtimestamp(modified)
print(f'The file {ifile} modification time: {h_modified}')

print("\nconfirm with ls -lh")
!ls -lh {ifile}

# make a directory myfiles and copy the file images/ucl.png to this directory
ofile = Path('myfiles',ifile.name)
# mkdir the parent
ofile.parent.mkdir(parents=True,exist_ok=True)
# copy text file with read_text() and write_text()
ofile.write_bytes(ifile.read_bytes()) #for binary files

print('\n==== After copying')
# confirm size
print(f'The file {ofile} size: {ofile.stat().st_size / 1024 : .2f} KB')

# mod time
modified = ofile.stat().st_mtime
h_modified = datetime.fromtimestamp(modified)
print(f'The file {ofile} modification time: {h_modified}')
# now time
print(f'Time now is {datetime.now()}')

# tidy up
ofile.unlink()
ofile.parent.rmdir()
```

    The file images/ucl.png exists?: True
    The file images/ucl.png size: 1956 B
    The file images/ucl.png size:  1.91 KB
    The file images/ucl.png modification time: 2022-09-29 15:46:26.616106
    
    confirm with ls -lh
    -rw-r--r-- 1 coursd0 ucaac2 2.0K Sep 29 15:46 images/ucl.png
    
    ==== After copying
    The file myfiles/ucl.png size:  1.91 KB
    The file myfiles/ucl.png modification time: 2022-10-21 16:19:26.415919
    Time now is 2022-10-21 16:19:26.425067

