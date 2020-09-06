#!/bin/bash

# shell to sort nb
# documentation
# run bin/notebook-run-1.sh

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

geog0111/mkdocs_prep.py 
mkdocs build -v
echo "now run:  mkdocs gh-deploy --force"
