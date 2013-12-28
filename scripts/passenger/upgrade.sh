#!/bin/sh -e
#
# Put this script in /path/to/project/local/upgrade.sh
# and customize if necessary

cd $(dirname "$0")/..

GIT_DIR=.git git pull --force

./manage.sh collectstatic --noinput

touch ../tmp/restart.txt
