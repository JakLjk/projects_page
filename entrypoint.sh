#!/bin/sh

set -e 

echo "Running collectstatic..."
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:8000 --workers 2