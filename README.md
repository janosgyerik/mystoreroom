djbootstrap
===========
Django Bootstrap: my general template for new Django projects

Django version: 1.6

Creating a new clone
--------------------
1. Clone the project with a new name:

        git clone . /path/to/new
        cd /path/to/new

2. Rename `djbootstrap` to your `newproj` everywhere:

        ./scripts/rename-djbootstrap.sh newapp

3. Rename `myapp` to your `newapp` everywhere:

        ./scripts/rename-myapp.sh newapp

4. Restart repo:

        rm -fr .git
        git init
        git remote rm origin
        git remote add origin newurl

Updating a clone
----------------
TODO
