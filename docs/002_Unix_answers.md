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

    /Users/philiplewis/Documents/GitHub/geog0111/notebooks
    /Users/philiplewis/Documents/GitHub/geog0111
    /Users/philiplewis/Documents/GitHub
    /Users/philiplewis



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

    /Users/philiplewis/Documents/GitHub/geog0111/notebooks
    /Users/philiplewis
    /Users/philiplewis/geog0111/notebooks


#### Exercise 2

* examine the file permissions for files `~/geog0111/notebooks/bin/*` (in the directory `~/geog0111/notebooks/bin`)
* what do you notice about these? 
* why do you think this is so?


```bash
%%bash

# This solution is called a bash script
# it runs a series of bash (unix) commands, one after the other
# It uses a special shell feature cat << EOF ... EOF for convenience
# This is known as the 'here-document' structure that allows
# multi-line input so everything between the EOF markers
# is treated as if it essentially came from a text file. 
# All that does here is to print out everything in the ... 
# to the terminal (sends to the stdin of the cmd cat)

# pwd
pwd

# * examine the file permissions in the directory bin
ls -lh ~/geog0111/notebooks/bin/*

# * what do you notice about these?
cat << EOF
===============================
* what do you notice about these?
===============================
Most of them are -rwxr-xr-x, which is 755 so they have read write 
and execute for the user (7) but only read and execute for others.
The file bin/README has 644: read and write for the user (6) but
just read for others.
EOF

cat << EOF
===============================
* why do you think this is so?
===============================
Most of these are executable commands (scripts to run).
The ones that end with .sh will be sh or bash scripts

The README file is not executable: its just a text file.
EOF
```

    /Users/philiplewis/Documents/GitHub/geog0111/notebooks
    -rw-r--r--  1 philiplewis  staff   245B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/NASAaccount0111.py
    -rw-r--r--  1 philiplewis  staff    16B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/README
    -rwxr-xr-x  1 philiplewis  staff   1.1K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/build-conda-package
    -rwxr-xr-x  1 philiplewis  staff   220B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/build-pypi-package
    -rwxr-xr-x  1 philiplewis  staff   1.3K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/clean0111.sh
    lrwxr-xr-x  1 philiplewis  staff     7B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/copy -> ../copy
    -rwxr-xr-x  1 philiplewis  staff    43B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/database.sh
    -rwxr-xr-x  1 philiplewis  staff   217B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/docker-build
    -rwxr-xr-x  1 philiplewis  staff   428B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/docker-killall
    -rwxr-xr-x  1 philiplewis  staff   1.0K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/docker-run
    -rwxr-xr-x  1 philiplewis  staff   534B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/fixA.sh
    -rwxr-xr-x  1 philiplewis  staff   2.0K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/get-datasets.sh
    -rwxr-xr-x  1 philiplewis  staff   569B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/git-remove-all.sh
    -rw-r--r--  1 philiplewis  staff   257B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/howmany.sh
    -rwxr-xr-x  1 philiplewis  staff   2.2K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/init.sh
    -rwxr-xr-x  1 philiplewis  staff   2.7K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/init0111.sh
    -rwxr-xr-x  1 philiplewis  staff   3.2K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/link-set.sh
    -rwxr-xr-x  1 philiplewis  staff   8.0K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/notebook-mkdocs.sh
    -rwxr-xr-x  1 philiplewis  staff   2.0K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/notebook-run.sh
    -rwxr-xr-x  1 philiplewis  staff   1.5K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/postBuild
    -rwxr-xr-x  1 philiplewis  staff    44B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/pullYou
    -rwxr-xr-x  1 philiplewis  staff    95B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/pushMe
    -rwxr-xr-x  1 philiplewis  staff   526B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/set-course.sh
    -rwxr-xr-x  1 philiplewis  staff   3.4K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/setup.sh
    -rwxr-xr-x  1 philiplewis  staff   754B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/shellMe.sh
    -rwxr-xr-x  1 philiplewis  staff   2.6K 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/sort-db.sh
    -rwxr-xr-x  1 philiplewis  staff   742B 12 Jul 12:18 /Users/philiplewis/geog0111/notebooks/bin/tidy.sh
    ===============================
    * what do you notice about these?
    ===============================
    Most of them are -rwxr-xr-x, which is 755 so they have read write 
    and execute for the user (7) but only read and execute for others.
    The file bin/README has 644: read and write for the user (6) but
    just read for others.
    ===============================
    * why do you think this is so?
    ===============================
    Most of these are executable commands (scripts to run).
    The ones that end with .sh will be sh or bash scripts
    
    The README file is not executable: its just a text file.


#### Exercise 3

* Create a file `work/newfile.dat` using cat and check the new file size.
* Use the menu item `File -> Open` to edit the file you have created and print the new file size
* Use `cat` to show the new file content
* delete the file


```bash
%%bash
cd ~/geog0111/notebooks

# ANSWER
# Create a file `work/newfile.dat` using cat and check the new file size.
cat << EOF > work/newfile.dat

# this will go into the file
hello world - this is some text in a file

EOF
ls -l work/newfile.dat
```

    -rw-r--r--  1 philiplewis  staff  73 30 Sep 13:36 work/newfile.dat



```bash
%%bash
cd ~/geog0111/notebooks

# ANSWER
# Use the menu item File -> Open to edit the 
# file you have created and print the new file size
# --> do interactively <--
ls -l work/newfile.dat

# Use cat to show the new file content
cat work/newfile.dat
```

    -rw-r--r--  1 philiplewis  staff  73 30 Sep 13:36 work/newfile.dat
    
    # this will go into the file
    hello world - this is some text in a file
    



```bash
%%bash
cd ~/geog0111/notebooks

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
cd ~/geog0111/notebooks

ls -lh geog0111/f*

# interpret the file permissions and sizes of the files in there
# the file sizes are 2.2KB, 4.3KB and 1.9KB respectively
# the file permissions are all 644, so, read and write for the user, 
# and only read for others
```

    -rwxr-xr-x  1 philiplewis  staff   362B 12 Jul 12:18 geog0111/fdict.py
    -rwxr-xr-x  1 philiplewis  staff   1.7K 12 Jul 12:18 geog0111/filter_movies.py
    -rwxr-xr-x  1 philiplewis  staff   2.2K 12 Jul 12:18 geog0111/fire_practical_model.py
    -rwxr-xr-x  1 philiplewis  staff   4.3K 12 Jul 12:18 geog0111/fire_practical_satellite.py
    -rwxr-xr-x  1 philiplewis  staff   1.9K 12 Jul 12:18 geog0111/fire_practical_telecon.py
    -rwxr-xr-x  1 philiplewis  staff    66B 12 Jul 12:18 geog0111/flatten.py

