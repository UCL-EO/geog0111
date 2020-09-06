#!/bin/bash
  
here=$(pwd)
cmddir=$(dirname $0)

export OS=$(uname|cut -d '-' -f 1)
export conda=conda

if [[ "$OS" == "Windows_NT" || "$OS" == "MSYS_NT" ]]
then
  export conda=conda.bat
  echo "Using windows"
fi
force=FALSE

THIS=`basename $0`
POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    -f|--force)
    force=TRUE
    shift # past argument
    ;;
    -n|--no_force)
    force=FALSE
    shift # past argument
    ;;
    -h|--help)
    echo "$THIS [-f|--force] | [-n|--no_force] ']"
    shift # past argument
    exit
esac
done
set -- "${POSITIONAL[@]}"

here=$(pwd)
# generate tmp dir to work in
tmp="${HOME}/tmp.$$"
rm -rf "${tmp}"
mkdir -p "${tmp}"
if [ $? -eq 0 ]; then
   pwd
   echo "--> tmp working directory made in ${tmp}"
else
   echo '--> tmp working directory failed <--'
   pwd
   exit 1
fi

echo "--> copy Docker/environment.yml to install directory ${tmp}"
cp Docker/environment.yml ${tmp}

echo "----> cd to install directory ${tmp}"
cd "${tmp}"
conda_env=$(grep 'name:' environment.yml  | awk '{print $NF}')
echo "--> ENVIRONMENT: $conda_env" 
conda_rc=$(conda info | grep 'populated config files' | awk '{print $NF}')
CONDA_DIR=$conda_rc

echo "--> create ~/.dockenvrc :"
# get these env variables
cat << EOF > ~/.dockenvrc
#!/bin/bash
export CONDA=$conda
export OS=$OS
export CONDA_DEFAULT_ENV=$conda_env
export conda_env=$conda_env
export DEBIAN_FRONTEND=noninteractive
export PATH=\$CONDA_DIR/bin:\$PATH
export PATH=\$CONDA_DIR/envs/${conda_env}/bin:\$PATH
EOF

echo "======== ~/.dockenvrc ========"
cat ~/.dockenvrc
echo "=============================="

echo "--> source ~/.dockenvrc"
source ~/.dockenvrc

# set up a user environment to work from
# in case we only have system
#$conda activate base
existsenv=$($conda env list | grep "$conda_env" |awk '{print $1}')
echo "environment: $conda_env"
echo "--> exists : $existsenv"
echo "--> force  : $force"

# already exists
if [ ! -z "$existsenv" ] ; then
  if [ $force == TRUE ] ; then
    echo "--> forcing create env $conda_env from environment.yml"
    $conda env create  -n "$conda_env" --force  -f environment.yml
  else
    echo "--> Use --force flag to ensure re-creation"
  fi
fi

if [ -z "$existsenv" ] ; then
#  echo "--> try to remove env"
#  $conda remove -n "$conda_env" -y --all
  echo "--> create env $conda_env from environment.yml"
  $conda env create  -n "$conda_env" --force  -f environment.yml
fi

#echo "--> activate $conda_env"
#$conda activate "$conda_env"

#echo "--> update $conda_env with conda git anaconda"
#$conda update -y -n "$conda_env"  -c defaults conda git anaconda

# so they can carry through
echo "--> create put 'conda activate $conda_env' in ~/.dockenvrc'"
echo "$conda activate $conda_env" >> ~/.dockenvrc


if [ -z "$SHELL" ]
then
  SHELL=$(ps -p $$ | tail -1 | awk '{print $NF}')
fi
THISSHELLY=$(echo $SHELL| awk -F/ '{print $NF}')
echo "--> Shell : $THISSHELLY"

for i in  "$THISSHELLY" "bash" "fish" "zsh" "sh"
do
  RC=~/.${i}_profile
  touch $RC
  grep -v dockenvrc <  $RC > $RC.bak
   echo "--> ensuring run of ~/.dockenvrc in $RC"
  echo 'source ~/.dockenvrc' >> $RC.bak
  mv $RC.bak $RC
done

echo "----> cd back to ${here}" 
cd "${here}"

#echo "--> install jupyter_contrib_nbextensions using pip"
#pip3 install --user jupyter_contrib_nbextensions

cat << EOF > bin/postBuild
#!/bin/bash

echo "--> enabling jupyter nbextensions"
jupyter nbextension enable contrib_nbextensions_help_item/main 
jupyter nbextension enable autosavetime/main 
jupyter nbextension enable codefolding/main 
jupyter nbextension enable code_font_size/code_font_size 
jupyter nbextension enable code_prettify/code_prettify 
jupyter nbextension enable collapsible_headings/main 
jupyter nbextension enable comment-uncomment/main 
jupyter nbextension enable equation-numbering/main 
#jupyter nbextension enable execute_time/ExecuteTime 
jupyter nbextension enable gist_it/main 
jupyter nbextension enable hide_input/main 
jupyter nbextension enable spellchecker/main 
#jupyter nbextension enable toc2/main 
jupyter nbextension enable toggle_all_line_numbers/main 
jupyter nbextension enable exercise2/main  
jupyter nbextension disable toc2/main 
jupyter nbextension disable execute_time/ExecuteTime
jupyter nbextension enable hinterland/hinterland
jupyter nbextension enable printview/main
jupyter nbextension enable execution_dependencies/execution_dependencies
jupyter nbextension enable python-markdown/main

#echo "--> clearing pip cache"
#rm -rf "${HOME}"/.cache/pip 

echo "--> ensuring $HOME/.jupyter/nbconfig exists"
mkdir -p $HOME/.jupyter/nbconfig 

echo "--> fixing $HOME/.jupyter/nbconfig/common.json"
echo '{"nbext_hide_incompat": true}' > $HOME/.jupyter/nbconfig/common.json

# install the geog0111 library
echo "--> install geog0111 library using python setup.py install"
python setup.py install
EOF
chmod +x bin/postBuild

echo "--> run bin/setdirs.sh"
bin/setdirs.sh

# tidy
echo "--> tidy up"
rm -rf ${tmp} ${HOME}/tmp

#echo "--> run bin/postBuild"
#bin/postBuild

echo "--> finished"
