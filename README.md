djbootstrap
===========
Django Bootstrap: my general template for new Django projects

Django version: 1.6


Creating a new clone
--------------------
1. Clone the project with a new name, as newproj:

        git clone . /path/to/newproj
        cd /path/to/newproj

2. Rename `djbootstrap` to your `newproj` everywhere:

        ./helper/rename-project.sh

3. Rename `bs3app` to your `newapp` everywhere:

        ./helper/rename-app.sh newapp

4. Get rid of helper scripts:

        rm -r ./helper/

5. Setup project

        # create virtualenv and run install requirements
        ./scripts/init.sh
        ./manage.sh syncdb --noinput
        ./manage.sh whitelist --add-admin you@example.com


Keep link with upstream project
-------------------------------
It can be a good idea to keep a link with the upstream project
to be able to merge future improvements in the common scripts.

    git remote add upstream url_to_upstream

To merge the upstream changes:

    git fetch upstream
    git merge upstream/master


Restart repo
------------
If you don't ever want to merge again from upstream to the new clone,
you can reset the repository and get rid of all past history:

    rm -fr .git
    git init
    git remote rm origin
    git remote add origin newurl


Setup deployment with passenger
-------------------------------
TODO


Setup remote upgrades by git push
---------------------------------
TODO
