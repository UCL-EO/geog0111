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

    /Users/plewis/geog0111/notebooks
    /Users/plewis/geog0111
    /Users/plewis
    /



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

    /Users/plewis/geog0111/notebooks
    /Users/plewis
    /Users/plewis/geog0111/notebooks


#### Exercise 2

* examine the file permissions for files `~/geog0111/notebooks/bin/*` (in the directory `~/geog0111/notebooks/bin`)
* what do you notice about these? 
* why do you think this is so?


```bash
%%bash

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

    /Users/plewis/geog0111/notebooks
    -rw-r--r--  1 plewis  staff   245B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/NASAaccount0111.py
    -rw-r--r--  1 plewis  staff    16B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/README
    -rwxr-xr-x  1 plewis  staff   1.1K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/build-conda-package
    -rwxr-xr-x  1 plewis  staff   220B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/build-pypi-package
    -rwxr-xr-x  1 plewis  staff   1.3K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/clean0111.sh
    lrwxr-xr-x  1 plewis  staff     7B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/copy -> ../copy
    -rwxr-xr-x  1 plewis  staff    43B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/database.sh
    -rwxr-xr-x  1 plewis  staff   217B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/docker-build
    -rwxr-xr-x  1 plewis  staff   428B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/docker-killall
    -rwxr-xr-x  1 plewis  staff   1.0K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/docker-run
    -rwxr-xr-x  1 plewis  staff   534B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/fixA.sh
    -rwxr-xr-x  1 plewis  staff   2.0K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/get-datasets.sh
    -rwxr-xr-x  1 plewis  staff   569B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/git-remove-all.sh
    -rw-r--r--  1 plewis  staff   257B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/howmany.sh
    -rwxr-xr-x  1 plewis  staff   2.2K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/init.sh
    -rwxr-xr-x  1 plewis  staff   2.7K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/init0111.sh
    -rwxr-xr-x  1 plewis  staff   3.2K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/link-set.sh
    -rwxr-xr-x  1 plewis  staff   8.0K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/notebook-mkdocs.sh
    -rwxr-xr-x  1 plewis  staff   2.0K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/notebook-run.sh
    -rwxr-xr-x  1 plewis  staff   1.5K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/postBuild
    -rwxr-xr-x  1 plewis  staff    44B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/pullYou
    -rwxr-xr-x  1 plewis  staff   100B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/pushMe
    -rwxr-xr-x  1 plewis  staff   526B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/set-course.sh
    -rwxr-xr-x  1 plewis  staff   3.4K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/setup.sh
    -rwxr-xr-x  1 plewis  staff   754B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/shellMe.sh
    -rwxr-xr-x  1 plewis  staff   2.6K  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/sort-db.sh
    -rwxr-xr-x  1 plewis  staff   742B  3 Oct 01:14 /Users/plewis/geog0111/notebooks/bin/tidy.sh
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

    -rw-r--r--  1 plewis  staff  73  4 Oct 08:57 work/newfile.dat



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

    -rw-r--r--  1 plewis  staff  73  4 Oct 08:57 work/newfile.dat
    
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
cd ~/geog0111/notebooks

ls -lh geog0111/f*

# interpret the file permissions and sizes of the files in there
# the file sizes are 2.2KB, 4.3KB and 1.9KB respectively
# the file permissions are all 644, so, read and write for the user, 
# and only read for others
```

    -rw-r--r--  1 plewis  wheel   362B  3 Oct 21:28 geog0111/fdict.py
    -rw-r--r--  1 plewis  wheel   1.7K  3 Oct 21:28 geog0111/filter_movies.py
    -rw-r--r--  1 plewis  wheel   2.2K  3 Oct 21:28 geog0111/fire_practical_model.py
    -rw-r--r--  1 plewis  wheel   4.3K  3 Oct 21:28 geog0111/fire_practical_satellite.py
    -rw-r--r--  1 plewis  wheel   1.9K  3 Oct 21:28 geog0111/fire_practical_telecon.py
    -rw-r--r--  1 plewis  wheel    66B  3 Oct 21:28 geog0111/flatten.py

