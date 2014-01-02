#!/bin/sh -e

test "$1" && proj=$1 || proj=$(cd $(dirname $0)/..; basename $PWD)

echo -ne Ok to rename ./djbootstrap to ./$proj? '[Y/n] '
read answer
answer=yes
if [[ ! "$answer" || "$answer" =~ [yY] ]]; then
    mv -v djbootstrap $proj
    if sed --version 2>/dev/null | grep -q ^GNU; then
        grep -rl djbootstrap . | grep -v -e ^./.git/ -e .pyc$ | xargs sed -i -e s/djbootstrap/$proj/g
    else
        grep -rl djbootstrap . | grep -v -e ^./.git/ -e .pyc$ | xargs sed -i '' -e s/djbootstrap/$proj/g
    fi
fi
