# GEOG0111 Scientific Computing

[Course Documentation](https://UCL-EO.github.io/geog0111/)

 [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCL-EO/geog0111/HEAD?urlpath=/tree)
 [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UCL-EO/geog0111/blob/master/HEAD?urlpath=/tree)
 
 For previous versions of the course:
 
 * [Release 1.1.0 for course notes for session 2021/22](https://github.com/UCL-EO/geog0111/releases/tag/1.1.0)
 * [Release 1.1.1 for course notes for session 2022/23](https://github.com/UCL-EO/geog0111/releases/tag/1.1.1)

## Course information

### Course Convenor 

[Dr. Martin Mokros](mailto:m.mokros@ucl.ac.uk)

[Prof P. Lewis](http://www.geog.ucl.ac.uk/~plewis)

### Teaching Staff 2023-2025

|   | 
|---|
|[Dr. Martin Mokros](mailto:m.mokros@ucl.ac.uk)
|[Prof P. Lewis](http://www.geog.ucl.ac.uk/~plewis)|

### Support Staff 2023-2024

|   | 
|---|
|TBA


### Other Contributing Staff

|   |
|---|
|TBA


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

Follow the instructions on [UCL installation and running](notebooks/Install.md)

## Timetable

[class timetable for 2023/24](notebooks/TIMETABLE.md)

The course takes place over 10 weeks in term 1, on Monday 11:00-14:00 in the UCL Computing Lab (G20) in [CHRISTOPHER INGOLD BUILDING, 20 GORDON STREET, LONDON, WC1H 0AJ](https://www.ucl.ac.uk/estates/roombooking/building-location/?id=067), UCL. 

Classes take place from the second week of term to the final week of term, other than Reading week. See UCL [term dates]() for further information.

The timetable is available on the UCL Academic Calendar. Live class sessions will take place in groups on Monday with help sessions on Thursdays.

The Thursday help sessions will be held in room 110 in the [Northwest Wing (Geography Department, first floor)](https://www.ucl.ac.uk/estates/roombooking/building-location/?id=003)

### Assessment

Assessment is through two pieces of coursework, submitted in both paper form and electronically via Moodle. 

See the [Moodle page](https://www.ucl.ac.uk/students/life-ucl/term-dates-and-closures-2023-24) for more details.

### Useful links

[Course Moodle page](https://www.ucl.ac.uk/students/life-ucl/term-dates-and-closures-2023-24)  

### Using the notes

# Using the course notes

We will use `jupyter` notebooks for running interactive Python programs. If you are taking this course at UCL, 
follow the instructions on [UCL installation and running](notebooks/Install.md). 

If you are interested in running the course notes from outside UCL on your own computer, there are several options:

1. Do a local install of the required software to run the notebooks (basically, Anaconda Python and some packages, this is around 15 GB of space on my own setup, but you might get away with a smaller Pythjon install). Its quite easy to set up, particularly on linux or OS X. It is a little more involved on Windows, but quite achievable following [these notes](notebooks/OutsideInstall-Local.md)
2. You can run a [Docker](https://www.docker.com) container on your local computer. That Docker image contains all of the software you need to do the course, so all you have to do is to set up [Docker](https://www.docker.com) on your computer. There are various ways to run it, but we adviuse that you make a copy of the notes on your local computer, then run the notebookjs using Docker. There are full instructions these [here](OutsideInstall-Docker.md), but the basics of what you need are given in the [docker hub](https://hub.docker.com/repository/docker/proflewis/geog0111).
3. You could use [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCL-EO/geog0111/HEAD?urlpath=/tree) or 
 [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UCL-EO/geog0111/blob/master/HEAD?urlpath=/tree) to run the course. These use external resources (so, not UCL and not your own computer) to run the notebooks. The only problem for you is that the sessions are not persistent, so any changes or exercises you do in a notebook would be lost to you the next time you start a binder or colab session. There are ways around that that would work fine for the first half of the course. The simplest is for you to download any notebook that you change to your local computer, then relaod it the next time you run a session. Its a bit of a hassle, but the service is free, and you can run it simply from any browser (e.g. yopur phone or ipad).
 
# Updating the course notes

From time-to-time we will need to provide updates to the notes or software. You need to be aware of how to do that and also what the consequences of pulling a new version are. Please go through [these notes](notebooks/Using-the-course-notes.md) before you start using the notes.
