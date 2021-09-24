#!/bin/bash



here=$(pwd)
base="$(cd $(dirname "$0") &&  cd ../.. &&  pwd -P && cd "$here")"
repo=$(echo $base | awk -F/ '{print $NF}')

cd $base
here=$base
echo "----> running $0 from $here"
echo "--> location: $base"
echo "--> repo: $repo"

# HOME may not be set on windows
if [ -z "$HOME" ] ; then
  cd ~
  HOME=$(pwd)
  echo "--> HOME $HOME"
  cd "$here"
fi

rm -f notebooks_lab/*ipynb
mkdir -p backup.$$
cp notebooks/* backup.$$
echo "backups in backup.$$"

# shell to run notebooks 

# run all notebooks -> note*/*nbconvert.ipynb
rm -f note*/*nbconvert.ipynb
jupyter nbconvert --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.allow_errors=True \
    --nbformat=4 --ExecutePreprocessor.store_widget_state=True --to notebook --execute notebooks/???_*ipynb


# if you have files note*/*nbconvert.ipynb
# this script will rename them without the
# nbconvert
# It is a little dangerous as you might accidently delete
# your notebooks, so only do this and confirm when
# you have checked the conversions
# have all worked

echo "back up first!"
echo "compare these files ... the nbconvert convert file"
echo "should be slightly larger than the original"
echo "If thats not the case (ie smaller or very different)"
echo "then you need to check it in more detail and should"
echo "probably respond No"

for i in notebooks
do

  for f in $i/*nbconvert.ipynb
  do 
    outf=$(echo $f|sed 's/.nbconvert.ipynb/.ipynb/g')
    #mv $outf /tmp/tmp.$$
    #mv $f $outf
    echo "========"
    ls -l $f $outf
    d=$(diff $f $outf)
    # dont test if they are identical
    if [ ! -z "$d" ] ; then
      while true; do
        read -p "confirm mv $f $outf?" yn
        case $yn in
          [Yy]* ) mv $f $outf; break;; 
          [Nn]* ) break;;
          * ) echo "Please answer yes or no.";;
        esac
      done
    fi
  done
done
# delete the ones we dont save
rm note*/*nbconvert.ipynb

echo "----> done running $0 from $here"

echo "backups in backup.$$ : delete manually"

echo "now run bin/notebook-mkdocs.sh"
