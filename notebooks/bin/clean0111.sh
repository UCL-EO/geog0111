#!/bin/bash

# clean up all settings and files for a user for geog0111

echo "Clean up script for geog0111"
echo "This will clean all settings for users"
echo "beware of unintended consequences"
DATE=`date '+%d%m%Y_%H%M%S'`
echo "A backup of all relevant files is made to ~/BACKUP-$DATE-geog0111.tar.Z"

cd ~
touch geog0111 .url_db .cylog .jupyter .condarc .profile .ipython .bash_profile .bashrc
tar cvzf ~/BACKUP-$DATE-geog0111.tar.Z geog0111 .url_db .cylog .jupyter .condarc .profile .ipython .bash_profile .bashrc

rm -rf geog0111/notebooks/bin
rm -rf geog0111

# clean any changes to bash_profile
if [ -f ~/.bash_profile ]; then
    echo "~/.bash_profile exists... editing out reference to ~/.profile"
    grep -v < ~/.bash_profile 'source ~/.profile' > /tmp/tmp.$$ ; mv /tmp/tmp.$$  ~/.bash_profile

fi

# clean any changes to zsh_profile
if [ -f ~/.zsh_profile ]; then
    echo "~/.zsh_profile exists... editing out reference to ~/.profile"
    grep -v < ~/.zsh_profile 'source ~/.profile' > /tmp/tmp.$$ ; mv /tmp/tmp.$$  ~/.zsh_profile

fi

rm -rf .url_db .cylog .jupyter .condarc .profile .ipython

if [ -f ~/.bashrc ]; then
  echo "You should manually edit ~/.bashrc to remove conda settings for a full reset"
fi
  
if [ -f ~/.zshrc ]; then
  echo "You should manually edit ~/.zshrc to remove conda settings for a full reset"
fi

cd ~
rm -rf geog0111

