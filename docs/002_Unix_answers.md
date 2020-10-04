# 002 Some basic UNIX : Answers to exercises

#### Exercise 1

* Use `cd` and `..` to move one directory at a time to your home directory. Check where you are at each stage using `pwd`.
* Use `cd` and `~` to go straight to your home directory. Then go from there back to the notebook directory. Check where you are at each stage using `pwd`.


```bash
%%bash
# ANSWER

# Use cd and .. to move one directory at a time to your home directory. 
# Check where you are at each stage using pwd.

# we start e.g. in /Users/plewis/Documents/GitHub/geog0111/notebooks
pwd

# go to /Users/plewis/Documents/GitHub/geog0111
cd ..
pwd

# go to /Users/plewis/Documents/GitHub
cd ..
pwd

# go to /Users/plewis
cd ../..
pwd
```

    /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks
    /nfs/cfs/home3/Uucfa6/ucfalew/geog0111
    /nfs/cfs/home3/Uucfa6/ucfalew
    /nfs/cfs/home3



```bash
%%bash
# ANSWER

# Use cd and ~ to go straight to your home directory. 
# Check where you are at each stage using pwd.
pwd
cd ~
pwd

# Then go from there back to the notebook directory. 
# This is e.g. in Documents/GitHub/geog0111/notebooks
# relative to where we are
cd geog0111/notebooks
pwd
```

    /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks
    /home/ucfalew
    /home/ucfalew/geog0111/notebooks


#### Exercise 3

* Create a file `work/newfile.dat` using cat and check the new file size.
* Use the menu item `File -> Open` to edit the file you have created and print the new file size
* Use `cat` to show the new file content
* delete the file


```bash
%%bash
# ANSWER
# Create a file `work/newfile.dat` using cat and check the new file size.
cat << EOF > work/newfile.dat

# this will go into the file
hello world - this is some text in a file

EOF
ls -l work/newfile.dat
```

    -rw-r--r-- 1 ucfalew ucfa 73 Oct  3 17:49 work/newfile.dat



```bash
%%bash
# ANSWER
# Use the menu item File -> Open to edit the 
# file you have created and print the new file size
# --> do interactively <--
ls -l work/newfile.dat

# Use cat to show the new file content
cat work/newfile.dat
```

    -rw-r--r-- 1 ucfalew ucfa 73 Oct  3 17:49 work/newfile.dat
    
    # this will go into the file
    hello world - this is some text in a file
    



```bash
%%bash
# ANSWER
# delete the file
rm work/newfile.dat
```

#### Exercise 4

Using the `unix` commands and ideas from above:

* show a listing of the files in the relative directory `geog0111` that start with the letter `f`
* interpret the file permissions and sizes of the files in there


```bash
%%bash
# ANSWER
# show a listing of the files in the relative 
# directory geog0111 that start with the letter f
# so
#     geog0111/f*
ls -lh geog0111/f*

# interpret the file permissions and sizes of the files in there
# the file sizes are 2.2KB, 4.3KB and 1.9KB respectively
# the file permissions are all 644, so, read and write for the user, 
# and only read for others
```

    -rw------- 1 ucfalew ucfa  362 Oct  1 13:10 geog0111/fdict.py
    -rw-r--r-- 1 ucfalew ucfa 2.2K Oct  1 13:10 geog0111/fire_practical_model.py
    -rw-r--r-- 1 ucfalew ucfa 4.3K Oct  1 13:10 geog0111/fire_practical_satellite.py
    -rw-r--r-- 1 ucfalew ucfa 1.9K Oct  1 13:10 geog0111/fire_practical_telecon.py
    -rw-r--r-- 1 ucfalew ucfa   66 Oct  1 13:10 geog0111/flatten.py

