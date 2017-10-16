#!/usr/bin/sh

./manage.py migrate
./node_modules/.bin/webpack --config webpack.config.js
gunicorn web.wsgi -b 0.0.0.0:8080