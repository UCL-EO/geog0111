#!/bin/bash

# in case no home (windows?)
if [ -z "$HOME" ] ; then
  here="$(pwd)"
  cd ~
  HOME="$(pwd)"
  cd "$here"
fi

# install the geog0111 library
echo "--> install geog0111 library using python setup.py install"
python setup.py install

# put source ~/.dockenvrc in rc / profile
# files
# belt and braces!!
for i in "bash" "fish" "zsh" "sh"
do
  for ext in "_profile" "rc"
  do
    RC="${HOME}/.${i}${ext}"
    echo "--> $i : $ext : $RC"
    if [ ! -z "$RC" ] ; then
      touch "$RC"
      ls -l "$RC"
      grep -v dockenvrc < "$RC" > "$RC.bak"
      echo "--> ensuring run of ~/.dockenvrc in $RC"
      echo 'source ~/.dockenvrc' >> $RC.bak
      mv $RC.bak $RC
    else
      echo "no $RC"
    fi
  done
done

echo "----> done bin/postBuild"
