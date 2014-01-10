#!/bin/sh -e

test "$1" && app=$1 || { echo usage: $0 newappname; exit 1; }
oldappname=store

files_to_rename() {
    grep -rl $oldappname . 2>/dev/null | grep -v -e ^./.git/ -e .pyc$ -e ./.idea/
}
files_to_rename

printf "Ok to rename ./$oldappname to ./$app? [Y/n] "
read answer
if [ ! "$answer" ] || [[ $answer == [yY]* ]]; then
    mv -v ./$oldappname ./$app
    if sed --version 2>/dev/null | grep -q ^GNU; then
        files_to_rename | xargs sed -i -e s/$oldappname/$app/g
    else
        files_to_rename | xargs sed -i '' -e s/$oldappname/$app/g
    fi
fi
