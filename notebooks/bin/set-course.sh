#!/bin/bash

course_name="geog0111"
curl -o /tmp/geog0111.yml https://raw.githubusercontent.com/UCL-EO/geog0111/master/Docker/environment.yml
conda config --prepend envs_dirs /shared/groups/jrole001/${course_name}/envs
conda env create -n geog0111 -f /tmp/geog0111.yml


