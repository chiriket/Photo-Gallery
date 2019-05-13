#### PHOTO GALLERY

## By Shirley Keter ,2019

### Description
The application is a Photo Gallery that allows users to view photos based on category and location.On clicking the photo one is able to view its details and also expand it.

### Set Up and Installations
## Prerequisites
* Ubuntu Software
* Python3.6
* Postgres
* python virtualenv
* Clone the Repo -Run the following command on the terminal: git clone https://github.com/chiriket/Photo-Gallery.git && cd Photo-Gallery
* Activate virtual environment
* Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Create the Database
* psql
* CREATE DATABASE gallery;
* Create .env file and paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = <>
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

## Run initial Migration
* python3.6 manage.py makemigrations 
* python3.6 manage.py migrate

## Run the app
* python3.6 manage.py runserver
* Open terminal on localhost:8000

### Known bugs
There are no known bugs.

### Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql

### Support and contact details
Contact me on shirleyketer@gmail.com

###License
Copyright (c) Shirley Keter