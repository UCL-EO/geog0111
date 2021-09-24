#!/bin/bash  

# GEOG0111 script to initialise and update
# the student repository on the UCL system

# are we on the UCL system?
isUCL=$(uname -n | awk -Frstudio '{print $2}' | wc -w)
#echo $isUCL
if [ $isUCL == 0 ] ; then
  uname -a
  echo "You do not seem to be on the UCL rstudio/notebook servers"
  echo "FATAL: cannot proceed"
  exit 1
fi
echo "You are in the UCL rstudio/notebook servers"
# check for geog0111 repo and clone if not there
cd ~
if [ -d "geog0111" ] ; then
  echo "--> geog0111 exists ... updating"
  cd ~/geog0111
  for nb in "notebooks" "notebooks_lab"; do
    odir=${nb}_bak
    echo "--> backing up notebooks in ${nb} to ${odir}"
    mkdir -p ${odir}
    mv ${nb}/*ipynb $odir
  done

  echo "--> updating repository"
  git reset --hard HEAD
  git pull
  echo "--> done updating repository"
  
  for nb in "notebooks" "notebooks_lab"; do
    cd ~/geog0111
    odir=${nb}_bak
    # old list of files
    cd ~/geog0111/${odir}
    for f in *.ipynb; do
      #echo "examining $f in ~/geog0111/${odir}"
      other=~/geog0111/"${nb}"
      if [ -f "${other}/$f" ] ; then
        diff $f "${other}/$f" &> /dev/null
        es=$?
        if [ $es -ne 0 ]; then
          newname=$(echo $f | sed 's/.ipynb//').$$.ipynb
          while true; do
            echo "In $nb:"
            echo "  difference found between your notebook $f and latest install"
            echo "Do you want to keep:"
            echo "  [o] - only your old/original version?"
            echo "  [n] - only the newly downloaded version"
            echo "  [b] - both, and rename your old version to ${newname}"
            echo -n "  [o|n|b]? : "
            read response
            if [ "$response" == "o" ] ; then
              # keep the old one
              mv "$f" "$other"
              break
            elif [ "$response" == "n" ] ; then
              # keep the new one -- delte the old
              # but for safety, we'll put it in /tmp ...
              mv "$f" /tmp/$(whoami)_oldfile_"$f"
              break
            elif [ "$response" == "b" ] ; then
              mv "$f" "${other}/$newname"
              break
            fi
          done
        else
          mv "$f" "$other"
        fi
      else
        # no new version if this file
        # so move it back
        mv "$f" "${other}/$f"
      fi
    done
  done

else
  cd ~
  echo "--> cloning geog0111"
  git clone https://github.com/UCL-EO/geog0111.git
  echo "--> done cloning geog0111"
fi 

cd ~/geog0111
echo "--> conda setup"
conda init bash
touch .bashrc
mv .bashrc .profile
echo "--> done conda setup"

echo "--> geog0111 initialisation"
echo 'cd ~/geog0111 && bin/init.sh' | /bin/bash
echo "--> done geog0111 initialisation"

echo "You should close all shells to make sure changes take effect"
