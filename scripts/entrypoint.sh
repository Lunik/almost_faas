#!/bin/sh
# Author: Lunik
# LICENCE: GPLv3
#
# Description: Image entrypoint script

GUNICORN_WORKERS=${GUNICORN_WORKERS:-4}
GUNICORN_PORT=${GUNICORN_PORT:-8080}
GUNICORN_OPTS=${GUNICORN_OPTS:-}

set -o xtrace
exec gunicorn \
  --workers="${GUNICORN_WORKERS}" \
  --bind="0.0.0.0:${GUNICORN_PORT}" \
  --access-logfile /dev/stdout \
  --error-logfile /dev/stderr \
  ${GUNICORN_OPTS} \
  main:app