#!/bin/sh -e

test "$1" && proj=$1 || proj=$(cd $(dirname $0)/..; basename $PWD)
oldprojpname=djbootstrap

files_to_rename() {
    grep -rl $oldprojpname . 2>/dev/null | grep -v -e ^./.git/ -e .pyc$ -e ./.idea/
}
files_to_rename

echo -ne Ok to rename ./$oldprojpname to ./$proj? '[Y/n] '
read answer
answer=yes
if [[ ! "$answer" || "$answer" =~ [yY] ]]; then
    mv -v ./$oldprojpname ./$proj
    if sed --version 2>/dev/null | grep -q ^GNU; then
        files_to_rename | xargs sed -i -e s/$oldprojpname/$proj/g
    else
        files_to_rename | xargs sed -i '' -e s/$oldprojpname/$proj/g
    fi
fi
