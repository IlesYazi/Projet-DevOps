#!/bin/bash

sudo su

if [-d "Projet-DevOps"]
then
    echo "folder exist"
    cd Projet-DevOps
    git pull
else
    git clone https://github.com/IlesYazi/Projet-DevOps.git
    cd Projet-DevOps
    git pull
fi

if [ -d "env" ] 
then
    echo "Python virtual environment exists." 
else
    apt install python3.10-venv
fi

source env/bin/activate

pip3 install install django==3.1.7
pip3 install Pillow

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000

