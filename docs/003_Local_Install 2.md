# 003 Full native installation  of software and notes


## Introduction

###  Purpose of these notes

These notes describe how to set up a full installation of the software for this course on your computer. You will need access to the internet, both to download software, and to a more limited extent during the course, to download data. We can call this installation a 'full native' installation, as we will be installing all of the software you need to run the course directly. Other options for running include:

* remote running on UCL notebooks
* local installation via Docker

These notes cover installations on:

* Windows 10
* Mac OS X
* Linux

### Sufficient free disk space

You will need to have sufficient free disk space on your computer if you want to run this course locally. We suggest that yopu should have at least **128 GB** of free space to run this conmfortably. If you do not, you will need to free up space on your computer.


## Windows 10

### Windows 10 Student Edition 1909 or higher

To do a full installation of these notes on your Windows 10 computer, you need to be able to install software that doesn't come from the microsoft store. To do this, you should first check what version of windows you are running.

At the prompt at the bottom left of your screen (`Type here to search`), type `About your PC`. This will bring up the settings window, in the `About` section. 

Scroll down to the section `Windows specifications` and note the `Edition` field. If this says `Home edition`, then you will need to upgrade your version of Windows 10. Note also what is in the `Edition` field. It may say `Pro` or `Enterprise`. These is probably ok, but if it says anything else we reccommend you use `Windows 10 Education` edition, verions `1909` or later (e.g. `2004`). Even if you use `Pro` or `Enterprise`, you should update your system to edition to at least `1909`.

To update, navigate in a browser to [UCL software database](http://swdb.ucl.ac.uk/?filter=windows%2010), entering your UCL login and password as prompted. Look under the `Downloads` tab, for `Windows 10 1909` or `Windows 10 2004`. You will most likely want to to use 64-bit, rather than 32-bit versions. Follow the instructions to upgrade to the Student Edition. This will probably only involvce installing a new software key, but you should consider backing up any important files from your system before doing this. 

### Required Software

You will need to install the following software:

* [Anaconda Python](https://docs.anaconda.com/anaconda/install/windows/)
* [GitHub Desktop](https://desktop.github.com/)

Follow the links above to install these before going any further. If you hit a problem, follow any troubleshooting information provided, or uninstall, then try to re-install again. Follow recommendations about any options. Set the local GitHub directory to be `Documents\GitHub`.  **Do not proceed without having these properly installed.**

### Install the notes

Launch GitHub Desktop. If you have a [github account](https://github.com/join?source=login), use `File -> Options` to sign in to your account. 

To install these  notes, use the menu `File -> Clone repository`. Enter `UCL-EO/geog0111` as the github repository to clone, and select `Clone`.

### Install the environment

Type `Anaconda Powershell Prompt` in the `Type here to search` box at the lower left of youyr screen, and open the app. You should *not* need to do this as Adminstrator, so *do not* select that option if you see it.

This will bring up a shell terminal. In the terminal, assuming you puth the `geog0111` repository in `.\Documents\GitHub\geog0111`, type:

    cd .\Documents\GitHub\geog0111

and hit `<return>` to run the command. This will change the directory (folder) youy are in in the terminal to where we have installed the course notes.

![cd](images/windows-cd.png)

Next, we run a script to install all of the libraries we need:

    bash -i .\bin\set_up_system.sh
    
and hit `<return>` to run the command. 
    
![bash](images/windows-setup.png)

This may take some time to run (10s of minutes) as it needs to examine your current setup and download libraries. You should see activity in the window, such as:

![running](images/windows-setup-running.png)

and

![running 2](images/windows-setup-running-2.png)

but eventually it should 





```python

```
