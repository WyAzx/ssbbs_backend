#!/bin/bash
set -e

gunicorn -k gevent -w 1 --bind 0.0.0.0:5000 ssbbs_backend.wsgi:application --chdir=/ssbbs_backend
