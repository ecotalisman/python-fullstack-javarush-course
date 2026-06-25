#!/bin/bash

# Install django-sslserver
pip install django-sslserver

# Generate an SSL certificate
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj '/CN=localhost'

# Run the Django dev server with HTTPS support...
python manage.py runsslserver