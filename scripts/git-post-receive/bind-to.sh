#!/bin/sh -e

test "$1" -a "$2" || {
    echo usage $0 REPO BRANCH
    echo example: $0 '~/repos/git/releases/mystock.git beta'
    exit 1
}

repo=$1; shift
branch=$1; shift
remote=releases

test -f manage.py || {
    echo error: run this script from inside a Django project directory
    exit 1
}

scriptsdir=$(dirname "$0")

mkdir -p local
upgrade_sh=$PWD/local/upgrade.sh

git branch | grep -q ^..$branch$ || git checkout -b $branch
git checkout $branch
test -d $repo || git clone . --bare --single-branch $repo

git remote | grep -q $remote && git remote rm $remote
git remote add $remote $repo
git branch --set-upstream $branch $remote/$branch
git pull

cp -v $scriptsdir/post-receive $repo/hooks/
ln -snf $upgrade_sh $repo/upgrade-$branch.sh
