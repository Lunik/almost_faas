#!/bin/sh
# Author: Lunik
# LICENCE: GPLv3
#
# Description: Image healthcheck script

GUNICORN_PORT=${GUNICORN_PORT:-8080}

# Check if gunicorn is running
if ! nc -z localhost $GUNICORN_PORT; then
    echo "Gunicorn is not running"
    exit 1
fi

# Check if flask app is running
if ! curl -s http://localhost:$GUNICORN_PORT/healthz | grep -q "OK"; then
    echo "Flask app is not running"
    exit 1
fi