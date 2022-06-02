#!/bin/sh

VENV_DIR="venv"


# setup venv
python3.10 -m venv $VENV_DIR
source $VENV_DIR/bin/activate

pip install -r requirements.txt

# run as daemon
gunicorn -c gunicorn.conf.py d08.wsgi --pid logs/gunicorn.pid --daemon
# to kill
# kill $(cat logs/gunicorn.pid) 

mkdir ~/goinfre/.brew/etc/nginx/sites-enabled
cd ~/goinfre/.brew/etc/nginx/sites-enabled
ln -s ~/d08/nginx.conf d08
brew services restart nginx