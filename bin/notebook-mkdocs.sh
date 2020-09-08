#!/bin/bash

# shell to sort nb
# documentation
# run bin/notebook-run.sh

rm -rf docs
mkdir -p docs
rm -rf site
rm -rf */*nbconvert*
rm -rf notebooks_*/*_files 
# filter notebooks from notebooks into notebooks_lab
geog0111/edit_notebook.py


# make markdown from the ipynb in notebooks_lab/???_*ipynb
jupyter nbconvert --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.allow_errors=True \
    --nbformat=4 --ExecutePreprocessor.store_widget_state=True --to markdown notebooks_lab/???_*ipynb

# mv into docs
mv notebooks_lab/*_files docs
mv notebooks_lab/*md docs
rm -f docs/README.md

for i in docs/*md
do
  sed < $i > /tmp/$$ 's/.ipynb/.md/g'
  mv /tmp/$$ $i
done

# generate docs/index.md 

cat << EOF >> docs/index.md 

Last update: {{ git_revision_date_localized }}

EOF

cp  data/index_head.rst docs/index.rst
awk < ../mkdocs.yml -F: 'BEGIN{start=0} ($1=="nav"){start=1} ($1=="plugins"){start=0} (start==1 && $1!="nav"){print $NF}' >> docs/index.rst
cat data/index_tail.rst >> docs/index.rst

geog0111/mkdocs_prep.py 
mkdocs build -v
cd docs
cp ../data/requirements.txt .
sphinx-quickstart -P "GEOG0111 Scientific Computing" -a "P. Lewis and J. Gomez-Dans" -v "1.0.1" -l "en" --ext-autodoc --ext-doctest --ext-viewcode --ext-githubpages --ext-intersphinx
#sphinx build html latexpdf
cd ..
echo "now run:  mkdocs gh-deploy --force"
