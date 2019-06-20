{% if False %}
# Django 2.x + Wagtail 2.x Base Template #

## About ##

This template is used by developer at RZO & Mirounga

## Features ##

By default, this project template includes:

Wagtail:

- Wagtail 2.x

Migrations:

- Django built-in migrations

Caching:

- python-memcached

Admin:

- Includes django-debug-toolbar for development and production (enabled for superusers)

## How to use this project template to create your project ##

- $ pipenv install Django==2.2.2
- $ pipenv run django-admin.py startproject --template https://github.com/rzo-python/rzo-wagtail-boilerplate/archive/master.zip --extension py,md,rst projectname
- $ cd projectname
- $ pipenv install -r dev-requirements.txt
- $ pipenv shell
- $ cd src
- $ python manage.py migrate
- $ python manage.py runserver

(By default dev environment use SQLite database)

{% endif %}
# The {{ project_name|title }} Project #

## About ##

Describe your project here.

## Prerequisites ##

- Python 3.7 recommended
- pipenv (pipenv + virtualenv)

## Installation ##

Fill out with installation instructions for your project.


License
-------

Indicate your licence here

BSD