# 002 Some basic UNIX : Answers to exercises

### Exercise

* Create a file `work/newfile.dat` using touch and check the new file size.
* Create a file `work/newfile.dat` using cat and check the new file size.
* Use the menu item `File -> Open` to edit the file you have created and print the new file size
* Use `cat` to show the new file content
* delete the file


```bash
%%bash
# ANSWER
# Create a file `work/newfile.dat` using touch and check the new file size.
touch work/newfile.dat
ls -l work/newfile.dat
```

    -rw-r--r--  1 plewis  staff  73  7 Sep 15:08 work/newfile.dat



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

    -rw-r--r--  1 plewis  staff  73  7 Sep 15:08 work/newfile.dat



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

    -rw-r--r--  1 plewis  staff  73  7 Sep 15:08 work/newfile.dat
    
    # this will go into the file
    hello world - this is some text in a file
    



```bash
%%bash
# ANSWER
# delete the file
rm work/newfile.dat
```

## Unix

### Exercise

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

    -rw-r--r--  1 plewis  staff   2.2K  6 Sep 22:34 geog0111/fire_practical_model.py
    -rw-r--r--  1 plewis  staff   4.3K  6 Sep 22:34 geog0111/fire_practical_satellite.py
    -rw-r--r--  1 plewis  staff   1.9K  6 Sep 22:34 geog0111/fire_practical_telecon.py

