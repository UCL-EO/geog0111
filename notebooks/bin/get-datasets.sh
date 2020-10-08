#!/bin/bash

# URLS 
here=$(pwd)

echo "--> Start of get-datasets.sh from ${here}"
echo "    script to download MODIS datasets for GEOG0111"

# Wednesday warning !!!
DOW=$(date +%u)
if [ $DOW -eq 3 ] ; then
  while true; do
    echo "--> ** Be advised that NASA servers go down for maintenance on Wednesday"
    echo "       so you are not advised to run this script today."
    echo "****** Type "y" to confirm you want to go ahead********"
    echo "****** Type "n" to quit                        ********"
    echo -n "  [y|n]? : "
    read response
    if [ "$response" == "y" ] ; then
      echo "--> Don't blame me if things go wrong now!"
      break
    elif [ "$response" == "n" ] ; then
      exit 0
    fi
  done     
fi

echo "--> gathering URLs from  data/database.db -> work/data_urls.txt"
mkdir -p "${here}/work/datasets"
grep store "${here}/data/database.db" | sed 's/.hdf:/.hdf/' | awk '{print $1}' > "${here}/work/datasets/data_urls.txt"
echo "--> testing NASA Earthdata login and password"

ipython -c "from geog0111.cylog import earthdata; earthdata(True);"

if [ $? -eq 0 ] ; then
  echo "--> test for Earthdata succeeded"
else
  echo "--> Earthdata test failed: sort your password/login and retry"
  echo "    Or see warning about Wednesday"
fi

cd "$here"
echo "--> getting NASA Earthdata login and password"
password=$(ipython -c "from geog0111.cylog import modpass; modpass()")
username=$(ipython -c "from geog0111.cylog import modlog; modlog()")
if [ $? -eq 0 ] ; then
  echo "--> got login and password"
else
  echo "--> failed to get login and password"
  exit 1
fi

echo "--> staging datasets to work/datasets"
mkdir -p "${here}/work/datasets"
cd  "${here}/work/datasets"

# run curl to get the file if we need it
while read url; do
  echo "== $url =="
  ofile=$(echo $url | sed 's/https:\/\///')
  if [ ! -f "$ofile" ] ; then
    curl --create-dirs -s -u "$username":"$password" -o ${ofile}.store "$url"
  fi
done <  "${here}/work/datasets/data_urls.txt"

cd ${here}
echo "--> End of get-datasets.sh from ${here}"
