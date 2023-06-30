#!/bin/sh

# start the wsgi server
gunicorn -w 3 -b 0.0.0.0:5000 --reload authenticator.app_factory:app_instance
