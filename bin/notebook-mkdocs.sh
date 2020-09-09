#!/bin/bash

# shell to sort nb
# documentation
# run bin/notebook-run.sh


here=$(pwd)
base="$(cd $(dirname "$0") &&  cd .. &&  pwd -P && cd "$here")"
repo=$(echo $base | awk -F/ '{print $NF}')

cd $base
here=$base

# HOME may not be set on windows
if [ -z "$HOME" ] ; then
  cd ~
  HOME=$(pwd)
  echo "--> HOME $HOME"
  cd "$here"
fi

dev=""
verbose=TRUE
do_run=FALSE
mode="MKDOCS"
#mode="SPHINX"

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    -v|--verbose)
    verbose=TRUE
    shift # past argument
    ;;
    -q|--quiet)
    verbose=FALSE
    shift # past argument
    ;;
    -s|--sphinx)
    mode="SPHINX" 
    shift # past argument
    ;;
    -m|--mkdocs)
    mode="MKDOCS"
    shift # past argument
    ;;
    -d|--dev)
    dev="--dev"
    shift # past argument
    ;;
    -r|--run)
    do_run=TRUE
    shift # past argument
    ;;
    -h|--help)
    echo "${0}:"
    echo "     [-h|--help] [[-s | --sphinx]|[-m|--mkdocs]"
    echo "     [-r|--run] [[-v|--verbose]|[-q|--quiet]] [-d|--dev]"
    shift # past argument
    exit
esac
done
set -- "${POSITIONAL[@]}"

# intro
if [ "$verbose" == TRUE ]  ; then
  echo "----> running $0 from ${here}"
  echo "--> location: ${base}"
  echo "--> repo: ${repo}"
fi

# dirs
if [ "$verbose" == TRUE ]  ; then
  echo "--> cleaning and re-making docs"
fi

cd "${base}"
rm -rf docs
mkdir -p docs

# install required sw
if [ "$mode" == "SPHINX" ] ; then
  cd "${base}"
  if [ "$verbose" == TRUE ]  ; then
    echo "--> installing sphinx"
  fi
  pip install sphinx
  sphinx-quickstart -q -p "GEOG0111 Scientific Computing" -a "P. Lewis and J. Gomez-Dans" -v "1.0.1" -l "en" --ext-autodoc --ext-doctest --ext-viewcode --ext-githubpages --ext-intersphinx docs
fi

if [ "$mode" == "MKDOCS" ] ; then
  if [ "$verbose" == TRUE ]  ; then
    echo "--> installing mkdocs"
  fi
  pip install mkdocs mkdocs-jupyter mknotebooks mkdocs-material mkdocs-exclude mkdocs-git-revision-date-localized-plugin
fi

if [ "$verbose" == TRUE ]  ; then
  echo "--> cleaning and re-making notebooks_lab"
fi
cd "${base}"
rm -rf site
rm -rf */*nbconvert*
rm -rf notebooks_lab/*_files 
# filter notebooks from notebooks into notebooks_lab
geog0111/edit_notebook.py
bin/link-set.sh

cd "${base}"
if [ "$verbose" == TRUE ]  ; then
  echo "--> creating markdown files in notebooks_lab"
fi
# make markdown from the ipynb in notebooks_lab/???_*ipynb
jupyter nbconvert --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.allow_errors=True \
    --nbformat=4 --ExecutePreprocessor.store_widget_state=True --to markdown notebooks_lab/???_*ipynb

if [ "$verbose" == TRUE ]  ; then
  echo "--> staging markdown files into docs"
fi
cd "${base}"
# mv into docs
mv notebooks_lab/*_files docs
mv notebooks_lab/*md docs
rm -f docs/README.md
if [ "$verbose" == TRUE ]  ; then
  echo "--> done staging markdown files into docs"
fi

# dev scripts
if [ $dev == "--dev" ] ; then
  if [ "$verbose" == TRUE ]  ; then
    echo "--> installing dev docs from ${base}/bin/README"
  fi
  cp "${base}"/bin/README "${base}"/docs/bin.md
fi


# filter ipynb to md
if [ "$verbose" == TRUE ] ; then
  echo "--> filtering ipynb to md"
fi
cd "${base}"
for i in docs/*md
do
  sed < $i > /tmp/$$ 's/.ipynb/.md/g'
  mv /tmp/$$ $i
done

# generate tail for docs/index.md 
if [ "$verbose" == TRUE ] ; then
  echo "--> adding to docs/index.md"
fi
cat << EOF >> "${base}"/docs/index.md 

Last update: {{ git_revision_date_localized }}

EOF

if [ "$mode" == "SPHINX" ] ; then
  cd "${base}"
  if [ "$verbose" == TRUE ] ; then
    echo "--> generating sphinx files for docs"
  fi
  cp  config/index_head.rst docs/index.rst
  awk < mkdocs.yml -F: 'BEGIN{start=0} ($1=="nav"){start=1} ($1=="plugins"){start=0} (start==1 && $1!="nav"){print $NF}' >> docs/index.rst
  cat config/index_tail.rst >> docs/index.rst
fi

if [ "$mode" == "MKDOCS" ] ; then
  cd "${base}"
  if [ "$verbose" == TRUE ] ; then
    echo "--> generating mkdocs files for docs"
    echo "--> building mkdocs"
  fi
  geog0111/mkdocs_prep.py "$dev"
fi


cd "${here}"
if [ "$mode" == "SPHINX" ] ; then
  if [ "$verbose" == TRUE ] ; then
    echo "--> copying requirements.txt from ${base}/config"
  fi
  cp "${base}"/config/requirements.txt "${base}"/docs
fi

if [ "$verbose" == TRUE ] ; then
  echo "----> done running $0 from $here"
fi

# advice
if [ "$mode" == "MKDOCS" ] ; then
  if [ "$do_run" == TRUE ] ; then
     cd "${base}"
     mkdocs build -v
     mkdocs gh-deploy --force
  elif [ "$verbose" == TRUE ] ; then
        echo "----> now run:  mkdocs build -v && mkdocs gh-deploy --force"
  fi
elif [ "$mode" == "SPHINX" ] ; then
  if [ "$do_run" == TRUE ] ; then
     cd "${base}"
     sphinx build html latexpdf
  elif [ "$verbose" == TRUE ] ; then
        echo "----> now run: sphinx build html latexpdf"
  fi
fi

cd "${here}"
