# 002 Some basic UNIX


## Introduction


### Purpose

Although this course is about coding in Python, it can be of great value to you to learn at least some basic concepts and commands of the operating system. To that end, in this session we will learn some basic `unix` commands. You will be able to use these in almost any modern computing operating system may use: the `unix` shell is a core part of [`linux`](https://www.linux.org/) and [macOS](https://en.wikipedia.org/wiki/MacOS) and is directly available to you even in [Windows 10](https://docs.microsoft.com/en-us/windows/wsl/about). If you use these notes through the [`JupyterLab`](https://jupyterlab.readthedocs.io/en/stable/) interface, even from a mobile device, you will have access to a [`unix` shell](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html?highlight=bash) to run commands.

There are many online tutorials on unix. A good place to start backup material and some more features for the material we will cover today is [software-carpentry.org](https://v4.software-carpentry.org/shell/index.html).


### Prerequisites

You will need some understanding of the following:


* [001 Using Notebooks](001_Notebook_use.md)


Remember that you can 'run' the code in a code block using the 'run' widget (above) or hitting the keys ('typing') <shift> and <return> at the same time. 

### Timing

The session should take around 15 minutes.

## Running unix commands 

The code cells in this notebook take Python commands by default, but we can run `unix` commands either by pre-pending a single command with `!`:


```python
!pwd
```

    /Users/plewis/Documents/GitHub/geog0111/notebooks


or by using the [cell magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html) `%%bash`:


```bash
%%bash

# comment is after #
pwd
```

    /Users/plewis/Documents/GitHub/geog0111/notebooks


If you are using these notes through the [`JupyterLab`](https://jupyterlab.readthedocs.io/en/stable/) interface you have access to a [terminal](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html?highlight=bash) to run unix commands.

This original directory is now given by the shell variable `${here}`.

## Navigating the file system

### `~` `.` `..`

You will be used to the idea of navigating the filesystem from any previous computing you have ever done. You may have done this by clicking your way to a certain 'location' using `File explorer` (in Windows 10) or `Finder` (in MacOS), but you will have some familiarity with the tree-like nature of a filesystem: you go up or down in the system to find your way to the files and directories you want.

When we do this typing command in the `unix` shell, the concepts are exactly the same, but we have some new symbols to learn to help us navigate:

    - ~ (tilde/twiddle)
    - . (dot)
    - .. (dot-dot)
    

The tilde symbol `~` is a shorthand to refer to your home directory (this would generally be `C:\Users\username` on windows, `/Users/username` on MacOS or `/home/username` in linux, where `username` is your username). On windows, the file separator is `\` (backslash), but on [posix](https://en.wikipedia.org/wiki/POSIX#:~:text=The%20Portable%20Operating%20System%20Interface,maintaining%20compatibility%20between%20operating%20systems.) (`unix`-like) systems it is '/', forward slash. This can cause some issues when changing operating system. You should try to use the posix '/' whenever you can as this is more portable.

The symbol `.` means the current directory, and `..` refers to one level up in the directory tree.

### `cd` `pwd`

The command `cd filepath` is used in the shell to change from one directory to another. Typically, when you start a shell, you will be in your home directory. We can explicitly 'go to' (i.e. `cd` to) your home with `cd ~`. We use the command `pwd` to print the current working directory.

So the following sequence:


```bash
%%bash
cd ~
pwd
```

    /Users/plewis


changes directory to our home, and prints the directory name.


```bash
%%bash
pwd
cd ..
pwd
```


    ---------------------------------------------------------------------------

    CalledProcessError                        Traceback (most recent call last)

    <ipython-input-108-beb4c6171dd7> in <module>
    ----> 1 get_ipython().run_cell_magic('bash', '', 'pwd\ncd ..\npwd\n')
    

    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/IPython/core/interactiveshell.py in run_cell_magic(self, magic_name, line, cell)


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/IPython/core/magics/script.py in named_script_magic(line, cell)


    <decorator-gen-110> in shebang(self, line, cell)


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/IPython/core/magic.py in <lambda>(f, *a, **k)


    ~/anaconda3/envs/geog0111/lib/python3.7/site-packages/IPython/core/magics/script.py in shebang(self, line, cell)


    CalledProcessError: Command 'b'pwd\ncd ..\npwd\n'' died with <Signals.SIGKILL: 9>.


### `ls` `ls -lh` `*`

The command `ls` lists the files specified. For example:



```bash
%%bash
cd ~/geog0111
ls R*
```

    README.md


Here, `R*` uses the wildcard `*`, so `R*` means `R` followed by zero or more characters.

If we specify the option `-lh` then it provides a long listing (`-l`) with file size in 'human-readable' format (`-h`):


```bash
%%bash
cd ~/geog0111
ls -lh README.md
```

    -rw-r--r--  1 plewis  staff   321B  6 Sep 22:34 README.md


Here, the file size if `321B` (321 Bytes), and the file is owned by the user `plewis`. The field `-rw-r--r--` provides information on file permissions. Ignoring the first `-`, it is in 3 sets of 3 bits:

    rw-  r--  r--
    
which refer to permissions for the user, group, and everyone, respectively. The permission fields are `rwx`, meaning permissions of read, write, and execute, respectively. Execute here means that we can run the file as a script. In the example above, the no execute permission is set (it is not a script file), the user has read and write permission, and group and everyone have only read permissions. So, only the user can write to this file, but everyone can read it.

These fields `rwx` can be viewed as 3 bits which we can interpret as a [base-8 (octal) number](https://en.wikipedia.org/wiki/Octal) (i.e. between 0 and 7) where:

    --- -> 0
    --x -> 1
    -w- -> 2
    -wx -> 3
    r-- -> 4
    r-x -> 5
    rw- -> 6
    rwx -> 7
    
Following that, we interpret the field `rw-r--r--` from above as `644`. The most common file permissions you will likely see or need are:

    644 -> rw-r--r--
    755 -> rwxr-xr-x
    
 

### `chmod`

We can change file permissions with the command `chmod`. For example:


```bash
%%bash
cd ~/geog0111
ls -lh README.md
chmod 755 README.md
ls -lh README.md
chmod 644 README.md
```

    -rw-r--r--  1 plewis  staff   321B  6 Sep 22:34 README.md
    -rwxr-xr-x  1 plewis  staff   321B  6 Sep 22:34 README.md


First the permissions of the file are 644 as we saw above, then we use `chmod 755` to change to 755, then back again to 644. Most commonly, we will use this later ion to apply execute permission to a file:

    chmod 755 filename


### absolute and relative pathnames

A posix directory name that **starts with** the file separator '/' is called an **absolute** pathname: it is addressed from the root of the file system (`/`). An example of an absolute filename is `/home/jovyan/geog0111/README.md`. If the filename starts with `~`, it is in effect an absolute pathname. For example:



```bash
%%bash
ls -l ~/geog0111/README.md
```

    -rw-r--r--  1 plewis  staff  321  6 Sep 22:34 /Users/plewis/geog0111/README.md



A *relative pathname* is one that does not start with `/`  or `~`. It is specified relative to where we are in the filesystem in the current shell. For example:


```bash
%%bash
cd ~
ls -l geog0111/README.md
```

    -rw-r--r--  1 plewis  staff  321  6 Sep 22:34 geog0111/README.md


Recall that we use `..` to specify 'up one level'. Then:


```bash
%%bash
# cd to absolute path ~/geog0111/images
cd ~/geog0111/images
pwd

# now relatuve cd up one and down to bin
cd ../bin
pwd

# now relative cd up one level
cd ..
pwd
```

    /Users/plewis/geog0111/images
    /Users/plewis/geog0111/bin
    /Users/plewis/geog0111


### Create and delete a file `touch` `cat` `rm`

If a file doesn't exist, we can create a zero-sized file using `touch`:


```bash
%%bash
touch work/newfile.dat work/newerfile.dat
ls -l work/n*
```

    -rw-r--r--  1 plewis  staff  0  7 Sep 15:11 work/newerfile.dat
    -rw-r--r--  1 plewis  staff  0  7 Sep 15:11 work/newfile.dat


If it already exists, `touch` just updates the access time.

We can use the command `cat` to create a text files, for example:


```bash
%%bash

# code between the next line and the 
# End Of File (EOF) marker will be saved in 
# to the file work/newfile.dat
# the symbols << and > involve 
# redirection 
cat << EOF > work/newererfile.dat

# this will go into the file
hello world - this is some text in a file

EOF

# ls -l to see what we have: 73 Bytes here
ls -lh work/n*
```

    -rw-r--r--  1 plewis  staff    73B  7 Sep 15:11 work/newererfile.dat
    -rw-r--r--  1 plewis  staff     0B  7 Sep 15:11 work/newerfile.dat
    -rw-r--r--  1 plewis  staff     0B  7 Sep 15:11 work/newfile.dat


We can also use `cat` to see what is in a file:


```bash
%%bash
cat work/newererfile.dat
```

    
    # this will go into the file
    hello world - this is some text in a file
    


We can use the command `rm` to delete a file:


```bash
%%bash
rm work/newfile.dat
ls -lh work/n*

# now tidy up
rm work/n*
```

    -rw-r--r--  1 plewis  staff    73B  7 Sep 15:11 work/newererfile.dat
    -rw-r--r--  1 plewis  staff     0B  7 Sep 15:11 work/newerfile.dat


### Creating from JupyterLab

If you are using this notebook in JupyterLab, go to the launcher tab and you should see various tools that you can launch:

![JupyterLab tools](images/jl.png)

Among these you will see 'text file'. Launch a text file, write your Python code into the file, and save it (`File -> Save As`) to the Python file name you want in your `work directory` (e.g. `work/test.py`).

Alternatively, use the menu item `File -> New -> Text File` to open a new text file.

### Exercise

* Create a file `work/newfile.dat` using touch and check the new file size.
* Create a file `work/newfile.dat` using cat and check the new file size.
* Use the menu item `File -> Open` to edit the file you have created and print the new file size
* Use `cat` to show the new file content
* delete the file

## Unix

### Exercise

Using the `unix` commands and ideas from above:

* show a listing of the files in the relative directory `geog0111` that start with the letter `f`
* interpret the file permissions and sizes of the files in there

## Summary

In this section, we have learned the following `unix` commands and symbols:

| cmd  |  meaning  | example use | 
|---|---|--|
| `~`  |  twiddle / tilde -  home | `cd ~/geog0111` |
| `.`  |  dot  - current directory | `cd .` |
| `*`  | wildcard   | `ls R*` |
| `cd`  | change directory   | `cd ~/geog0111` |
| `pwd`  | print working directory | `pwd` |
| `ls`  | list | `ls README.md` |
| `ls -l`  | long list | `ls -l README.md` |
| `ls -lh`  | human-readable long list |`ls -lh README.md` |
| `chmod`  | change mode (permissions) | `chmod 644 README.md` |
| `touch` | create zero-size if it doesn't exists else update access time | `touch README.md`|
| `rm` | remove | `rm work/n*` |
| `755` | `rwxr-xr-x` | `chmod 755 bin/*` |
| `644` | `rw-r--r--` | `chmod 644 README.md` |

We have seen that we can use the cell magic `%%bash` or `!` to use `unix` commands in Python code cells in a notebook. This is a very basic introduction to unix, but it will allow you to make better use of the operating system and these notebooks.
