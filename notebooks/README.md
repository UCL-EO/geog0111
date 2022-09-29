# GEOG0111 Scientific Computing

[Course Documentation](https://UCL-EO.github.io/geog0111/)

 [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCL-EO/geog0111/HEAD?urlpath=/tree)
 [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UCL-EO/geog0111/blob/master/HEAD?urlpath=/tree)

## Course information

### Course Convenor 

[Prof P. Lewis](http://www.geog.ucl.ac.uk/~plewis)

### Teaching Staff 2021-2022

|   | 
|---|
|[Prof P. Lewis](http://www.geog.ucl.ac.uk/~plewis)|

### Support Staff 2021-2022

|   | 
|---|
|[Wanxin Yang](https://www.geog.ucl.ac.uk/people/research-students/wanxin-yang)|

### Contributing Staff

|   |   |   |
|---|---|---|
|[Dr Qingling Wu](http://www.geog.ucl.ac.uk/about-the-department/people/research-staff/qingling-wu/)| [Dr. Jose Gomez-Dans](http://www.geog.ucl.ac.uk/about-the-department/people/research-staff/jose-gomez-dans/)|[Feng Yin](https://www.geog.ucl.ac.uk/people/research-students/feng-yin)|


### Purpose of this course

This course, GEOG0111 Scientific Computing, is a term 1 MSc module worth 15 credits (25% of the term 1 credits) that aims to:

* impart an understanding of scientific computing
* give students a grounding in the basic principles of algorithm development and program construction
* to introduce principles of computer-based image analysis and model development

It is open to students from a number of MSc courses run by the Department of Geography UCL, but the material should be of wider value to others wishing to make use of scientific computing. 

The module will cover:

* Computing in Python
* Computing for image analysis
* Computing for environmental modelling
* Data visualisation for scientific applications

### Learning Outcomes

At the end of the module, students should:

* have an understanding of the Python programmibng language and experience of its use
* have an understanding of algorithm development and be able to use widely used scientific computing software to manipulate datasets and accomplish analytical tasks
* have an understanding of the technical issues specific to image-based analysis, model implementation and scientific visualisation

### Running on UCL JupyterHub

Follow the instructions on [UCL installation and running](Install.md)

## Timetable

[class timetable for 2021/22](TIMETABLE.ipynb)

The course takes place over 10 weeks in term 1, on Monday in the UCL Computing Lab (113) in [Torrington (1-19)](https://www.ucl.ac.uk/estates/roombooking/building-location/?id=086), UCL. 

Classes take place from the second week of term to the final week of term, other than Reading week. See UCL [term dates](https://www.ucl.ac.uk/estates/sites/estates/files/cal_term_times_2021_2022.pdf) for further information.

The timetable is available on the UCL Academic Calendar. Live class sessions will take place in groups on Monday with help sessions on Thursdays.

The Thursday help sessions will be held in room 110 in the [Northwest Wing (Geography Department, first floor)](https://www.ucl.ac.uk/estates/roombooking/building-location/?id=003)

### Assessment

Assessment is through two pieces of coursework, submitted in both paper form and electronically via Moodle. 

See the [Moodle page](https://moodle.ucl.ac.uk/course/view.php?id=21495) for more details.

### Useful links

[Course Moodle page](https://moodle.ucl.ac.uk/course/view.php?id=21495)  

### Using the course notes

We will generally use `jupyter` notebooks for running interactive Python programs. If you are taking this course at UCL, 
follow the instructions on [UCL installation and running](Install.md). 

If you are interested in running the course notes from outside UCL on your own computer, there are several options:

1. Do a local install of the required software to run the notebooks (basically, Anaconda Python and some packages, this is around 15 GB of space on my own setup, but you might get away with a smaller Pythjon install). Its quite easy to set up, particularly on linux or OS X. It is a little more involved on Windows, but quite achievable following [these notes](notebooks/OutsideInstall-Local.md)
2. You can run a [Docker](https://www.docker.com) container on your local computer. That Docker image contains all of the software you need to do the course, so all you have to do is to set up [Docker](https://www.docker.com) on your computer. There are various ways to run it, but we adviuse that you make a copy of the notes on your local computer, then run the notebookjs using Docker. There are full instructions these [here](OutsideInstall-Docker.md), but the basics of what you need are given in the [docker hub](https://hub.docker.com/repository/docker/proflewis/geog0111).
3. You could use [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCL-EO/geog0111/HEAD?urlpath=/tree) or 
 [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UCL-EO/geog0111/blob/master/HEAD?urlpath=/tree) to run the course. These use external resources (so, not UCL and not your own computer) to run the notebooks. The only problem for you is that the sessions are not persistent, so any changes or exercises you do in a notebook would be lost to you the next time you start a binder or colab session. There are ways around that that would work fine for the first half of the course. The simplest is for you to download any notebook that you change to your local computer, then relaod it the next time you run a session. Its a bit of a hassle, but the service is free, and you can run it simply from any browser (e.g. yopur phone or ipad).

### Updating notes

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
   
