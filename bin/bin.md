
## Docker

The Docker file is in [`Docker/Dockerfile`](copy/Dockerfile). This is a minimal setup for running notebooks for this course, being based on [`jgomezdans/uclgeog`](https://hub.docker.com/r/jgomezdans/uclgeog) which is derived from [`geog_docker`](https://github.com/jgomezdans/geog_docker). 

This docker is stored on dockerhub as [`ucleo/geog0111`](https://hub.docker.com/r/ucleo/geog0111) and derived from this repo [`UCL-EO/geog0111`](https://github.com/UCL-EO/geog0111).

It is automatically run from [travis](https://travis-ci.com/github/UCL-EO/geog0111) on a new load, so you shouldn't need to generate the docker manually.

The docker cleans out the environment for `uclgeog`, as we want opne called `geog0111`, clones [this repository](https://github.com/UCL-EO/geog0111) and runs [`bin/setup.sh`](bin/setup.sh) to install the `geog0111` environment. It activates the environment and runs [`bin/postBuild`](bin/postBuild). 

### Clean up docker files

The script [`bin/docker-killall`](bin/docker-killall) cleans up any cached dockers, kills running dockers, and cleans it all out. Use this only to make a clean slate for your docker in the repoi.
Otherwise, use more subtle `docker` commands. It is intended onbly for developers, but is run as user.

### Build docker

The script [`bin/docker-build`](bin/docker-build) will build and upload the docker. This is again intended just for developers, and requires a login to dockerhub.

### Run docker

The script [`bin/docker-run`](bin/docker-run) can be used to run the docker and launch a notebook. It will attempt to map the `work` directory to the current directory or `${HOME}/OneDrive*`. It will try to re-use an existing docker image.

Normal use then would be something like:

   cd /Users/plewis/work
   ~/geog0111/bin/docker-run


The first time you use this, it will show something like:

    --> running bin/docker-run from /Users/plewis/work
    --> mount /Users/plewis/work
    --> bin/docker-run: no existing docker image found
    --> bin/docker-run: running docker with /Users/plewis/work as /home/jovyan/notebooks/work

So anything we save into `/home/jovyan/notebooks/work` in the notebook will go into `/Users/plewis/work`.

The notebook will start with a message such as:

    Serving notebooks from local directory: /home/jovyan/geog0111/notebooks
    1 active kernel
    The Jupyter Notebook is running at:
    http://8fbac34af2bc:8888/?token=42897db02a8f1168ae2d7fb37aa2acdfcba51d47560a96dc
     or http://127.0.0.1:8888/?token=42897db02a8f1168ae2d7fb37aa2acdfcba51d47560a96dc

and you can access the notebooks from this address in a browser.

To end the session, type `^C` (`CONTROL + c`) in the teminal you ran the command from.

If you now type:

    docker ps -l 

You should see an existing image e.g.:

    docker ps -l 
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                     PORTS               NAMES
    8fbac34af2bc        ucleo/geog0111      "tini -g -- start-no…"   28 minutes ago      Exited (0) 2 minutes ago                       jolly_maxwell

If  you really want to delete that (start again with yoiur notebooks), you can with:

    docker container rm jolly_maxwell

but it should normally be fine to re-use.

The next time you run thiis command, it should recognise an existing docker image and respind with something like:

    --> running bin/docker-run from /Users/plewis/work
    --> mount /Users/plewis/work
    --> bin/docker-run: using docker image jolly_maxwell

## Scripts

### `bin/setup.sh`

[`bin/setup.sh`](bin/setup.sh) is the core setup script. It is run for example from [`Docker/Dockerfile`](copy/Dockerfile)
but may also be run on the repository. It should usually be run by the user and should work from any operating system.

    setup.sh [-r | --remove] [-f|--force] | [-n|--no_force] 

The main purpose of the script is to run the `conda` setup to make the conda environment `geog0111` from [Docker/environment.yml](copy/environment.yml).
It will detect if windows is being used (so run `conda.bat`) and test to see if the environment `geog0111` already exists. If it does, it can be removed (`--remove`) or a foce install done (`--force`). Otherwise, it will try to update the environment from [Docker/environment.yml](copy/environment.yml).

It generates a file [`~/.dockenvrc`](copy/dockenvrc) to be run on shell startup to activate the environment.

After running this script, you should manually activate the environment:

    conda activcate geog0111

### `bin/postBuild`

[`bin/postBuild`](bin/postBuild) is run after [`bin/setup.sh`](bin/setup.sh) and does jobs such as setting up the jupyter notebook extensions, installing the `geog0111` package locally (using [`setup.py`](copy/setup.py)) and ensuring shell initialisation is properly done for subsequent sessions. It should be run the the user, and woul;d normally be run after any new run of [`bin/setup.sh`](bin/setup.sh).

### `bin/link-set.sh`

[`bin/link-set.sh`](bin/link-set.sh) is the directory linking script. 
It should usually be run by the user.

Users may work in any of several directories, so we need to put in symbolic links
from common directories (`data` `$repo` `images`) in each of these to ensure
correct operation. This script does that: It goes into each of `notebooks` 
`notebooks/work` `docs` `notebooks_lab` `notebooks_lab/work` `docs/work` and puts a 
symbolic link to `data` `$repo` `images` in `..`. Since relative paths are used,
this is portable.

In addition, it puts a link in from `~/$repo` to `$repo` for convenience (unless this 
already exists). It also puts a link in from `$UCLDATA` to `data/ucl` (default `${HOME}/geog0111/work`)
so that a system-wide data directory can be put in, and referred to asd `data/ucl` from
scripts.

This is called [`bin/setup.sh`](bin/setup.sh), but may be run independently to fix any broken links.

### `bin/notebook-run.sh`

This script runs all notebooks in [`notebooks`](notebooks) using `jupyter nbconvert`. The files are saved as `*.nbconvert.md`. The running is tolerant to errors. If the file is no different to the original, the original is kept. Otherwise the user is prompted to see if you want to replace the original notebook with the one that has been executed. You are provided with information on file sizes, which should help with this decision: you might not want to save a notebook that is (much) smaller than the original. Backups are stored in `backup.$$` which you need to manually clear.

You might run this as a pre-cursor to [`bin/notebook-mkdocs.sh`](bin/notebook-mkdocs.sh).

### `bin/notebook-mkdocs.sh`

This script [`bin/notebook-mkdocs.sh`](bin/notebook-mkdocs.sh) filters notebooks in [`notebooks`](notebooks) into [`notebooks_lab`](notebooks_lab) using [`geog0111/edit_notebook.py`](geog0111/edit_notebook.py). This filters out noteboom extensions and other features, and makes the notebooks suitable for running in [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), rather than just `jupyter noteboook`. It strips out exercises defiuned in `exercise2` cells, into new notebooks with the pattern `_answers.md`.

It can use sphinx or mkdocs (set on cmd line)

         notebook-mkdocs.sh [-h|--help] [[-s | --sphinx]|[-m|--mkdocs] 
             [-r|--run] [[-v|--verbose]|[-q|--quiet]] [-d|--dev]


The script takes the [`notebooks_lab`](notebooks_lab) notebooks, and converts to markdown in [`docs`](docs) and prepares the environment for the document generator `mkdocs` using [`geog0111/mkdocs_prep.py`](geog0111/mkdocs_prep.py). 
It runs `mkdocs build` locally. The documents can be viewed with:

	mkdocs serve

and/or uploaded to the document server (by the developer) using:

	mkdocs gh-deploy --force


