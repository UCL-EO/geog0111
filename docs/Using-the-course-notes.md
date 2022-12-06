

# Simply Updating notes

Periodically, we may have to update the notes. 

Before you do this, be aware that any updated files on the server will over-write your local files. **That means that any changes you may have made to the notebooks**, for example, will be lost. It is vital then that you save the notebooks you are working on with a different name. 

You can easily do this by clicking on the notebook name panel at the top of the notebook (the one that says `OutsideInstall-Local` here) and changing it (e.g. `myOutsideInstall-Local`). You might do this consistently for all notebooks you use as you go through the course, then you won't have to worry about it when you do updates.


The simplest way to update the notes (and over-write your changes), in a shell (Terminal) type:

    cd ~/geog0111 && git reset --hard HEAD && git pull
    
    
but be aware that that will write over any changes you make to notebooks, and make sure to rename the workbooks you modify.
    
# Safely Updating notes

There is a way we can avoid this issue, by storing the changes you make before pulling any modifications to the notes. But this is sligjhtly more complicated. You should decide whoich method you will use.

This is called a [stash](https://www.freecodecamp.org/news/git-stash-explained/).

The way to use it is, when you are told to update the notes, first create a stash with some meaningful name/label, e.g. `my edits on monday'. First, go to the directory your work in in (the working directory):

    cd ~/geog0111/notebooks
    
Then create the stash with your label:

    git stash save "my edits on monday"
    
Now, pull the new notes:

    git pull origin master
    
Suppose this pulled a new version of the file `001_Notebook_use.md`,m but you had edits in that file that you wasnted to keep. Then the pull wouyld overwrite your edits, BUT they would still be available via the stash.

You can see a `diff` (what changed from the last stash entry) by using:

    git stash show -p stash@{0}
    
You have two main options then for using the stash:

apply the changes to the new file:

    git stash apply STASH-NAME
    
    
Or move the old file back in place of the new file:


    git stash pop STASH-NAME
   
   
For anything more complex than that, look at this [explainer](https://www.freecodecamp.org/news/git-stash-explained/).
