# Using the course notes

We will use `jupyter` notebooks for running interactive Python programs. If you are taking this course at UCL, 
follow the instructions on [UCL installation and running](notebooks/Install.md). 

If you are interested in running the course notes from outside UCL on your own computer, there are several options:

1. Do a local install of the required software to run the notebooks (basically, Anaconda Python and some packages, this is around 15 GB of space on my own setup, but you might get away with a smaller Pythjon install). Its quite easy to set up, particularly on linux or OS X. It is a little more involved on Windows, but quite achievable following [these notes](notebooks/OutsideInstall-Local.md)
2. You can run a [Docker](https://www.docker.com) container on your local computer. That Docker image contains all of the software you need to do the course, so all you have to do is to set up [Docker](https://www.docker.com) on your computer. There are various ways to run it, but we adviuse that you make a copy of the notes on your local computer, then run the notebookjs using Docker. There are full instructions these [here](OutsideInstall-Docker.md), but the basics of what you need are given in the [docker hub](https://hub.docker.com/repository/docker/proflewis/geog0111).
3. You could use [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCL-EO/geog0111/HEAD?urlpath=/tree) or 
 [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UCL-EO/geog0111/blob/master/HEAD?urlpath=/tree) to run the course. These use external resources (so, not UCL and not your own computer) to run the notebooks. The only problem for you is that the sessions are not persistent, so any changes or exercises you do in a notebook would be lost to you the next time you start a binder or colab session. There are ways around that that would work fine for the first half of the course. The simplest is for you to download any notebook that you change to your local computer, then relaod it the next time you run a session. Its a bit of a hassle, but the service is free, and you can run it simply from any browser (e.g. yopur phone or ipad).

# Updating notes

From time to time, we need to update the notes because of a bug or some other change. That's great, because we are using `git` which allows and controls all of that.

At the same time, we don't want any update to mess up any work you may have already done, for example in a notebook.

There is a mechanism in `git` that allows this sort of thing, called a [stash](https://www.freecodecamp.org/news/git-stash-explained/).

The way to use it is, when you are told to update the notes, first create a stash with some meaningful name/label, e.g. `my edits on monday'. First, go to the directory your work in in (the working directory):

    cd ~/geog0111/notebooks
    
Then create the stash with your label:

    git stash save "my edits on monday"
    
Now, pull the new notes:

    git pull origin master
    
Suppose this pulled a new version of the file `001_Notebook_use.ipynb`,m but you had edits in that file that you wasnted to keep. Then the pull wouyld overwrite your edits, BUT they would still be available via the stash.

You can see a `diff` (what changed from the last stash entry) by using:

    git stash show -p stash@{0}
    
You have two main options then for using the stash:

apply the changes to the new file:

    git stash apply STASH-NAME
    
    
Or move the old file back in place of the new file:


    git stash pop STASH-NAME
   
   
For anything more complex than that, look at this [explainer](https://www.freecodecamp.org/news/git-stash-explained/).
