#!/bin/sh -e
#
# Put this script in /path/to/project/local/upgrade.sh
# and customize if necessary

cd $(dirname "$0")/..

projectname=$(basename $(pwd))
. ~/virtualenv/$projectname/bin/activate

unset GIT_DIR
git checkout -f

./manage.py collectstatic --noinput

touch ../tmp/restart.txt
