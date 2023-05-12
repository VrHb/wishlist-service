#!/bin/bash

set -e 

echo "Pulling changes from repository ..."
git pull origin main

echo "Activating virtual environment ..."
source ../env/bin/activate

echo "Installing python libs ..."
pip install -r ../requirements.txt

echo "Making db operations ..."
python manage.py makemigrations --dry-run --check
python manage.py migrate --no-input

echo "Collecting static files ..."
python manage.py collectstatic --no-input

echo "Restarting app unit ..."
sudo systemctl restart wishl.service

echo "All done!"
