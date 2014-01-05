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

        ./scripts/rename-djbootstrap.sh

3. Rename `myapp` to your `newapp` everywhere:

        ./scripts/rename-myapp.sh newapp

4. Restart repo:

        rm -fr .git
        git init
        git remote rm origin
        git remote add origin newurl

5. Setup project

        ./pip.sh install -r requirements.txt
        ./manage.sh syncdb --noinput
        ./manage.sh whitelist --add-admin you@example.com


Updating a clone
----------------
TODO
