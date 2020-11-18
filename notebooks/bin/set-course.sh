#!/bin/bash


# are we on the UCL system?
isUCL=$(uname -n | awk -Frstudio '{print $2}' | wc -w)

course_name="geog0111"
curl -o /tmp/geog0111.yml https://raw.githubusercontent.com/UCL-EO/geog0111/master/Docker/environment.yml

echo "Am I at UCL? $isUCL"

if [ "$isUCL" == 0 ] ; then
  echo "I am at UCL"
  conda config --prepend envs_dirs /shared/groups/jrole001/${course_name}/envs
fi

conda env create -n geog0111 --force -f /tmp/geog0111.yml

if [ $? -ne 0 ] ; then
  conda env update -n geog0111 -f /tmp/geog0111.yml
fi

