#!/bin/bash

# Prepare log files and start outputting logs to stdout
mkdir -p ./log
touch ./log/gunicorn.log
touch ./log/gunicorn-access.log
tail -n 0 -f ./log/gunicorn*.log &

export DJANGO_SETTINGS_MODULE=tennagraph.settings

exec gunicorn tennagraph.wsgi:application \
    --name tennagraph_django \
    --bind 0.0.0.0:8000 \
    --workers 5 \
    --worker-class gevent \
    --log-level=info \
    --log-file=./log/gunicorn.log \
    --access-logfile=./log/gunicorn-access.log
"$@"