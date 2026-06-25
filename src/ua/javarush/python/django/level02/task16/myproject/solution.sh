#!/bin/bash

# Command to create a new "library" application
python manage.py startapp library

# Command to create a migration based on the Book model
python manage.py makemigrations

# Command to apply the migration
python manage.py migrate

# Instruction for checking the Book model through the Django shell
python -i manage.py shell < shell_commands.py
