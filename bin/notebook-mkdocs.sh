#!/bin/bash

# shell to sort nb
# documentation
# run bin/notebook-run.sh


here=$(pwd)
base="$(cd $(dirname "$0") &&  cd .. &&  pwd -P && cd "$here")"
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

echo "--> re-making docs"
rm -rf docs
mkdir -p docs

#pip install sphinx
#sphinx-quickstart -q -p "GEOG0111 Scientific Computing" -a "P. Lewis and J. Gomez-Dans" -v "1.0.1" -l "en" --ext-autodoc --ext-doctest --ext-viewcode --ext-githubpages --ext-intersphinx docs

echo "--> re-making notebooks_lab"
rm -rf site
rm -rf */*nbconvert*
rm -rf notebooks_lab/*_files 
# filter notebooks from notebooks into notebooks_lab
geog0111/edit_notebook.py

bin/link-set.sh


echo "--> creating markdown files in notebooks_lab"
# make markdown from the ipynb in notebooks_lab/???_*ipynb
jupyter nbconvert --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.allow_errors=True \
    --nbformat=4 --ExecutePreprocessor.store_widget_state=True --to markdown notebooks_lab/???_*ipynb

echo "--> staging markdown files into docs"
# mv into docs
mv notebooks_lab/*_files docs
mv notebooks_lab/*md docs
rm -f docs/README.md
# scripts
cp bin/README docs/bin.md

for i in docs/*md
do
  sed < $i > /tmp/$$ 's/.ipynb/.md/g'
  mv /tmp/$$ $i
done

# generate docs/index.md 

echo "--> adding to docs/index.md"

cat << EOF >> docs/index.md 

Last update: {{ git_revision_date_localized }}

EOF


echo "--> generating sphinx files for docs"
cp  config/index_head.rst docs/index.rst
awk < mkdocs.yml -F: 'BEGIN{start=0} ($1=="nav"){start=1} ($1=="plugins"){start=0} (start==1 && $1!="nav"){print $NF}' >> docs/index.rst
cat config/index_tail.rst >> docs/index.rst

echo "--> generating mkdocs files for docs"
geog0111/mkdocs_prep.py --dev
echo "--> building mkdocs"
mkdocs build -v
cd docs
cp ../config/requirements.txt .
#sphinx build html latexpdf
cd ..
echo "----> done running $0 from $here"
echo "now run:  mkdocs gh-deploy --force"
