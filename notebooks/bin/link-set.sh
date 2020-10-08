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

# which dirs
opdirs=$(echo notebooks/work docs docs/work notebooks_lab notebooks_lab/work)

here=$(pwd)
echo "----> running $0 from $here"
echo "--> making links in ${opdirs[*]}"

base="$(cd $(dirname "$0") &&  cd .. &&  pwd -P && cd "$here")"
echo "--> location: $base"
repo=$(echo $base | awk -F/ '{print $NF}') 
echo "--> repo: $repo"

# HOME may not be set on windows
if [ -z "$HOME" ] ; then
  cd ~
  HOME=$(pwd)
  echo "--> HOME $HOME"
  cd "$here"
fi

# link to here from ~ for some scripts
cd $HOME
if [ ! "$HOME/$repo" == "$here" ]
then
  echo "--> linking $here $repo" 
  rm -f "$repo"
  ln -s $here "$repo"
fi
cd $here

# put links in all notebooks* directories
echo "--> linking ${subs[*]}"
subs=('bin' 'data' "$repo" 'images')
mkdir -p notebooks/work ${subs[*]}

# outer loop 
#for n in ${opdirs[@]}
#do
#  cd $base
#  echo "--> sorting links in $n"
#  mkdir -p "$n"
#  cd ${base}/$n
#  for link in ${subs[@]}
#  do
#    echo "--> $link"
#    rm -f $link
#    # dont link work
#    if [ $link != "work" ]; then
#      ln -s ../$link $link
#    fi
#  done
#done
cd "${here}"

echo "--> examining UCLDATA"
if [ -z "$UCLDATA" ] ; then
  echo "--> UCLDATA not set"
  export UCLDATA="/shared/groups/jrole001/geog0111/work"
fi
echo "--> setting UCLDATA=$UCLDATA"
touch ~/.profile
echo "export UCLDATA=$UCLDATA" > /tmp/tmp.geog0111.$$
grep -v 'UCLDATA=' < ~/.profile >> /tmp/tmp.geog0111.$$
echo "--> testing"
source /tmp/tmp.geog0111.$$
if [ "$?" -eq 0 ]; then
  mv /tmp/tmp.geog0111.$$ ~/.profile
  echo "--> done testing"
else
  echo "---> failure setting active env to ${course_name}"
  exit 1
fi
echo "--> done examining UCLDATA"

isUCL=$(uname -n | awk -Frstudio '{print $2}' | wc -w)

echo "--> examining CACHE_FILE"
if [ -z "$CACHE_FILE" ] ; then
  echo "--> CACHE_FILE not set"
  if [ "$isUCL" == 0 ] ; then
    export CACHE_FILE="${HOME}/.url_db/.db.yml"
  else
    export CACHE_FILE="/shared/groups/jrole001/geog0111/work/database.db"
  fi
fi
echo "--> setting CACHE_FILE=$CACHE_FILE"
touch ~/.profile
echo "export CACHE_FILE=$CACHE_FILE" > /tmp/tmp.geog0111.$$
grep -v 'CACHE_FILE=' < ~/.profile >> /tmp/tmp.geog0111.$$
echo "--> testing"
source /tmp/tmp.geog0111.$$
if [ "$?" -eq 0 ]; then
  mv /tmp/tmp.geog0111.$$ ~/.profile
  echo "--> done testing"
else
  echo "---> failure setting active env to ${course_name}"
  exit 1
fi
echo "--> done examining CACHE_FILE"

# UCL data link
#cd $base
#echo "--> sorting link to UCL data store"
#rm -f data/ucl
#cd data
#ln -s $UCLDATA ucl
#echo "--> done"

csubs=('docs' 'bin' 'notebooks' 'notebooks_lab')
# outer loop
for n in ${csubs[@]}
do
  cd $base/$n
  if [ -L bin ] ; then
    rm -f bin
  fi
  echo "linking $n/bin to ../bin"
  ln -s ../bin bin
  if [ -L copy ] ; then
    rm -f copy
  fi
  echo "linking $n/copy to ../copy"
  ln -s ../copy copy
  cd $base
done

# dont want this!
rm -f notebooks/bin/bin
rm -f notebooks/copy/copy

echo "----> done running $0 from $here"
