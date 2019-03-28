#!/usr/bin/env bash
python manage.py celery worker -c 1 --loglevel=info -n worker@%h