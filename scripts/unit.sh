#!/bin/sh -e

cd $(dirname "$0")/..

./manage.sh test store
