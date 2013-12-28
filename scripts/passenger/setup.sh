#!/bin/bash -e

test "$1" -a "$2" || {
    echo usage: $0 DOCROOT RELEASENAME
    echo example: $0 '~/webapps/beta.bashoneliners.com beta'
    exit 1
}

docroot=$1; shift
releasename=$1; shift

[[ $docroot == /* ]] || docroot=$PWD/$docroot

scriptsdir=$(dirname "$0")
. $scriptsdir/../../virtualenv.sh


mkdir -p $docroot
cp -va $scriptsdir/template/* $docroot/ || :
cat $scriptsdir/template/passenger_wsgi.py | sed \
    -e "s/^\(projectname =\).*/\1 '$projectname'/" \
    -e "s/.prod_settings/.$releasename"_settings/ \
    -e "s?^\(virtualenv_root =\).*?\1 '$virtualenv'?" \
    > $docroot/passenger_wsgi.py
