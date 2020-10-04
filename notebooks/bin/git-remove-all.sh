#!/bin/bash 

# from https://github.com/18F/C2/issues/439
# a complete re-base

# This script is used to clean all git commit
if [[ "$1" = 'all' ]];then
    echo "Clean all git commit"
    git checkout --orphan latest_branch
    git add -A
    git commit -am "Delete all previous commit"
    git branch -D master
    git branch -m master
fi

echo "Cleanup refs and logs"
rm -Rf .git/refs/original
rm -Rf .git/logs/

echo "Cleanup unnecessary files"
git gc --aggressive --prune=now

echo "Prune all unreachable objects"
git prune --expire now

git push -f origin master
