#!/bin/sh

cd $(dirname "$0")/..

virtualenv=$(. ./virtualenv.sh; echo $virtualenv)

if test ! "$virtualenv"; then
    projectname=$(basename "$PWD")
    virtualenv=~/virtualenv/$projectname
fi

if test ! -d $virtualenv; then
    echo virtualenv does not exist: $virtualenv
    printf "Create now? [Yn] "
    read ans
    if [ ! "$ans" ] || [[ $ans == [yY]* ]]; then
        virtualenv --distribute $virtualenv || exit 1
    else
        exit 1
    fi
fi

./pip.sh install -r requirements.txt
