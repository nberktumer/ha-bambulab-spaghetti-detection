#!/usr/bin/env bashio
set -e

ML_API_TOKEN=$(bashio::config 'obico_api_secret')

venv/bin/gunicorn --bind 0.0.0.0:3333 --workers 1 wsgi
