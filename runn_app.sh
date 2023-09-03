#!/bin/bash
poetry shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
