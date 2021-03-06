#!/bin/sh -e

test "$1" && proj=$1 || proj=$(cd $(dirname $0)/..; basename $PWD)
oldprojname=mystoreroom

files_to_rename() {
    grep -rl $oldprojname . 2>/dev/null | grep -v -e ^./.git/ -e .pyc$ -e ./.idea/
}
files_to_rename

printf "Ok to rename ./$oldprojname to ./$proj? [Y/n] "
read answer
if [ ! "$answer" ] || [[ $answer == [yY]* ]]; then
    mv -v ./$oldprojname ./$proj
    if sed --version 2>/dev/null | grep -q ^GNU; then
        files_to_rename | xargs sed -i -e s/$oldprojname/$proj/g
    else
        files_to_rename | xargs sed -i '' -e s/$oldprojname/$proj/g
    fi
fi
