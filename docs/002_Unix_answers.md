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


#### Exercise 2

* examine the file permissions for files `bin/*` (in the directory `bin`)
* what do you notice about these? 
* why do you think this is so?


```bash
%%bash

# pwd
pwd

# * examine the file permissions in the directory bin
ls -lh bin/*

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

    /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks
    -rwxr-xr-x 1 ucfalew ucfa 1.2K Sep 28 21:37 bin/build-conda-package
    -rwxr-xr-x 1 ucfalew ucfa  220 Sep 28 21:37 bin/build-pypi-package
    -rwxr-xr-x 1 ucfalew ucfa 1.4K Sep 28 21:37 bin/clean0111.sh
    lrwxrwxrwx 1 ucfalew ucfa    7 Sep 28 22:17 bin/copy -> ../copy
    -rwxr-xr-x 1 ucfalew ucfa   43 Sep 28 21:37 bin/database.sh
    -rwxr-xr-x 1 ucfalew ucfa  217 Sep 28 21:37 bin/docker-build
    -rwxr-xr-x 1 ucfalew ucfa  428 Sep 28 21:37 bin/docker-killall
    -rwxr-xr-x 1 ucfalew ucfa 1022 Sep 28 21:37 bin/docker-run
    -rwxr-xr-x 1 ucfalew ucfa  534 Sep 28 21:37 bin/fixA.sh
    -rwxr-xr-x 1 ucfalew ucfa 2.0K Sep 28 22:16 bin/get-datasets.sh
    -rwxr-xr-x 1 ucfalew ucfa  569 Sep 28 21:37 bin/git-remove-all.sh
    -rw-r--r-- 1 ucfalew ucfa  257 Sep 28 21:37 bin/howmany.sh
    -rwxr-xr-x 1 ucfalew ucfa 2.8K Sep 28 21:37 bin/init0111.sh
    -rwxr-xr-x 1 ucfalew ucfa 2.2K Sep 28 21:37 bin/init.sh
    -rwxr-xr-x 1 ucfalew ucfa 3.3K Sep 28 21:37 bin/link-set.sh
    -rw-r--r-- 1 ucfalew ucfa  245 Sep 28 21:37 bin/NASAaccount0111.py
    -rwxr-xr-x 1 ucfalew ucfa 8.0K Sep 28 21:37 bin/notebook-mkdocs.sh
    -rwxr-xr-x 1 ucfalew ucfa 2.0K Sep 28 21:37 bin/notebook-run.sh
    -rwxr-xr-x 1 ucfalew ucfa 1.5K Sep 28 21:37 bin/postBuild
    -rwxr-xr-x 1 ucfalew ucfa   44 Sep 28 21:37 bin/pullYou
    -rwxr-xr-x 1 ucfalew ucfa  100 Sep 28 21:37 bin/pushMe
    -rw-r--r-- 1 ucfalew ucfa   16 Sep 28 21:37 bin/README
    -rwxr-xr-x 1 ucfalew ucfa  526 Sep 28 21:37 bin/set-course.sh
    -rwxr-xr-x 1 ucfalew ucfa 3.4K Sep 28 21:37 bin/setup.sh
    -rwxr-xr-x 1 ucfalew ucfa  754 Sep 28 21:37 bin/shellMe.sh
    -rwxr-xr-x 1 ucfalew ucfa 2.7K Sep 28 21:37 bin/sort-db.sh
    -rwxr-xr-x 1 ucfalew ucfa  742 Sep 28 21:37 bin/tidy.sh
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
# ANSWER
# Create a file `work/newfile.dat` using cat and check the new file size.
cat << EOF > work/newfile.dat

# this will go into the file
hello world - this is some text in a file

EOF
ls -l work/newfile.dat
```

    -rw-r--r-- 1 ucfalew ucfa 73 Sep 29 08:11 work/newfile.dat



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

    -rw-r--r-- 1 ucfalew ucfa 73 Sep 29 08:11 work/newfile.dat
    
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

    -rw-r--r-- 1 ucfalew ucfa  362 Sep 28 21:37 geog0111/fdict.py
    -rwxr-xr-x 1 ucfalew ucfa 1.8K Sep 28 21:37 geog0111/filter_movies.py
    -rw-r--r-- 1 ucfalew ucfa 2.2K Sep 28 21:37 geog0111/fire_practical_model.py
    -rw-r--r-- 1 ucfalew ucfa 4.3K Sep 28 21:37 geog0111/fire_practical_satellite.py
    -rw-r--r-- 1 ucfalew ucfa 1.9K Sep 28 21:37 geog0111/fire_practical_telecon.py
    -rw-r--r-- 1 ucfalew ucfa   66 Sep 28 21:37 geog0111/flatten.py

