#!/bin/sh

cd $(dirname "$0")/..

grep -rl '' . | grep -v -e ^./.git/ -e png$ -e pyc$ -e gif$ -e /libraries/ -e $0
