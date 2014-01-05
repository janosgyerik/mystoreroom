#!/bin/bash -e

test "$1" -a "$2" || {
    echo usage: $0 DOCROOT RELEASENAME
    echo example: $0 '~/webapps/beta.inventoryman.com beta'
    exit 1
}

docroot=$1; shift
releasename=$1; shift

[[ $docroot == /* ]] || docroot=$PWD/$docroot

scriptsdir=$(dirname "$0")
. $scriptsdir/../../virtualenv.sh || exit 1


mkdir -p $docroot
cp -va $scriptsdir/template/* $docroot/ || :
cat $scriptsdir/template/passenger_wsgi.py | sed \
    -e "s/^\(projectname =\).*/\1 '$projectname'/" \
    -e "s/^\(releasename =\).*/\1 '$releasename'/" \
    -e "s?^\(virtualenv_root =\).*?\1 '$virtualenv'?" \
    > $docroot/passenger_wsgi.py
