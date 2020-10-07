#!/bin/bash

# This script is the initial setup script for users of geog0111
# on the UCL notebook servers


here=$(pwd)
echo "----> running $0 from $here"
echo "--> making links in ${opdirs[*]}"

base="$(cd $(dirname "$0") &&  cd .. &&  pwd -P && cd "$here")"
echo "--> location: $base"
repo=$(echo $base | awk -F/ '{print $NF}')
echo "--> repo: $repo"

isUCL=$(uname -n | awk -Frstudio '{print $2}' | wc -w)

# HOME may not be set on windows
if [ -z "$HOME" ] ; then
  cd ~
  HOME=$(pwd)
  echo "--> HOME $HOME"
  cd "$here"
fi

# conda env
echo "--> setting conda env in ~/.condarc"
course_name="geog0111"
conda config --prepend envs_dirs /shared/groups/jrole001/${course_name}/envs
echo "--> done setting conda env in ~/.condarc"

echo "--> setting active env to ${course_name}"
touch ~/.profile
grep -v "conda activate" < ~/.profile > /tmp/tmp.${course_name}.$$
echo "conda activate ${course_name}" >> /tmp/tmp.${course_name}.$$
# try it before keeping it
echo "--> activate"
source "/tmp/tmp.${course_name}.$$"
echo "--> activated"
if [ "$?" -eq 0 ]; then
  mv /tmp/tmp.${course_name}.$$ ~/.profile 
else
  echo "---> failure setting active env to ${course_name}"
  exit 1
fi

touch  ~/.zsh_profile
grep -v 'source ~/.profile' < ~/.zsh_profile > /tmp/tmp.$$
echo 'source ~/.profile' >> /tmp/tmp.$$
mv /tmp/tmp.$$ ~/.zsh_profile 

touch  ~/.bash_profile
grep -v 'source ~/.profile' < ~/.bash_profile > /tmp/tmp.$$
echo 'source ~/.profile' >> /tmp/tmp.$$
mv /tmp/tmp.$$ ~/.bash_profile 

echo "--> done setting active env to ${course_name}"

# postBuild to set jupyter extensions
#echo "--> setting up jupyter extensions"
#jupyter contrib nbextensions install --user
#echo "--> done setting up jupyter extensions"

echo "--> setting jupyter extensions"
bin/postBuild 
echo "--> done setting jupyter extensions"


# set up symbolic links
echo "--> setting symbolic links for $repo"
bin/link-set.sh

# UCL data link
cd $base
echo "--> sorting link to UCL data store"
rm -f data/ucl
cd data
ln -s /shared/groups/jrole001/geog0111/work ucl
echo "--> done"

echo "--> system database init"
cd $base
ipython geog0111/sys_init.py
echo "--> done system database init"
# 

echo "----> done running $0 from $here"
