#!/bin/bash
  
here=$(pwd)
base="$(cd $(dirname "$0") &&  cd .. &&  pwd -P && cd "$here")"
repo=$(echo $base | awk -F/ '{print $NF}')


cmddir=$(dirname $0)

export OS=$(uname|cut -d '-' -f 1)
export conda=conda
THIS=`basename $0`
echo "----> running $THIS from $here"

if [[ "$OS" == "Windows_NT" || "$OS" == "MSYS_NT" ]]
then
  export conda=conda.bat
  echo "--> Using windows"
fi
force=FALSE
remove=FALSE

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    -r|--remove)
    remove=TRUE
    force=TRUE
    shift # past argument
    ;;
    -f|--force)
    force=TRUE
    shift # past argument
    ;;
    -n|--no_force)
    force=FALSE
    shift # past argument
    ;;
    -h|--help)
    echo "$THIS [-r | --remove] [-f|--force] | [-n|--no_force]"
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
echo "--> remove : $remove"

# already exists
if [ ! -z "$existsenv" ] ; then
  if [ $remove == TRUE ] ; then
    echo "--> remove $conda_env" 
    conda remove -y -n uclgeog --all
  fi
  if [ $force == TRUE ] ; then
    echo "--> forcing create env $conda_env from environment.yml"
    $conda env create  -n "$conda_env" --force  -f environment.yml
  else
    echo "--> update env $conda_env from environment.yml"
    $conda env update  -n "$conda_env" -f environment.yml
  fi
fi

if [ -z "$existsenv" ] ; then
  echo "--> create env $conda_env from environment.yml"
  $conda env create  -n "$conda_env" --force  -f environment.yml
fi

# so they can carry through
echo "--> create put 'conda activate $conda_env' in ~/.dockenvrc'"
echo 'if [ -f "/opt/conda/etc/profile.d/conda.sh" ]; then' >>  ~/.dockenvrc
echo '    . "/opt/conda/etc/profile.d/conda.sh"' >>  ~/.dockenvrc
echo 'fi' >>  ~/.dockenvrc
echo "$conda activate $conda_env" >> ~/.dockenvrc

echo "-> copy files to ${base}/copy"
mkdir -p $base/copy
cp ~/.dockenvrc ${base}/copy/dockenvrc
cp ${base}/setup.py ${base}/copy
cp ${base}/Docker/environment.yml ${base}/copy

echo "----> cd back to ${here}" 
cd "${here}"

echo "--> run bin/link-set.sh"
bin/link-set.sh

# tidy
echo "--> tidy up"
rm -rf ${tmp} ${HOME}/tmp

echo "----> finished running $THIS from $here"
