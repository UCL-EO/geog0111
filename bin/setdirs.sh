#!/bin/bash

# This script looks for
# sub-directories in notebooks and replicates
# these to any other notebooks directory
# as well as the work directory. This means that if
# you copy trhe notebooks to either
# notebooks/work or notebooks_xx or notebooks_xx/work
# you will have access to the same local directories
#
# P. Lewis p.lewis@ucl.ac.uk
# Thu  3 Sep 2020
#
 
here=$(pwd)
base="$(cd $(dirname "$0") &&  cd .. &&  pwd -P && cd "$here")"

# put a link in at home
# for the unix cmd notebook


cd ~
HOME=$(pwd)
if [ ! $HOME/geog0111 == $here ]
then
  rm -f geog0111
  ln -s $here geog0111 
fi

cd $here
# put links in all notebooks* directories

#subs=$(ls -d notebooks/*/ | cut -d '/' -f 2) 
subs=('data' 'geog0111' 'images')
mkdir -p work 
for notebooks  in notebooks*  docs
do
  for s in $notebooks $notebooks/work
  do
    echo "--> $s"
    echo "--> setting dirs from $base"
    echo "    into ${base}/$s" 
    # make sure work folder setup properly

    echo "--> sorting links in ${base}/$s"
    mkdir -p ${base}/$s
    cd ${base}/$s
    for link in ${subs[@]}
    do
      echo "--> $link"
      rm -f $link
      # dont link work
      if [ $link != "work" ]; then
        ln -s ${base}/$link $link

        # check linked dir exists
        #tofile=$(ls -l data| awk '{print $NF}')
      
      fi
    done
  done

  cd "${here}"

  # if it is not notebooks, put a link in 
  # here too
  

done

