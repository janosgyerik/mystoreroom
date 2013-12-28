#!/bin/sh

projectname=$(basename "$PWD")
virtualenv=~/virtualenv/$projectname
test -d $virtualenv && . $virtualenv/bin/activate || {
    echo virtualenv does not exist: $virtualenv >&2
    echo Create it with: virtualenv --distribute $virtualenv >&2
    echo Better yet, run ./scripts/init.sh >&2
    exit 1
}
. $virtualenv/bin/activate
