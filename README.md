#  project name:
LETS_SHARE 


# AUTHOR
EDWIKE NYAUNCHO


## Project description
The application will allow a user to post a project he/she has created and get it reviewed by his/her peers.


## USER STORY
-The user is able to sign in to the application to start using

-User is able to view posted projects and their details

-User can be able to post a project to be reviewed or rated

-User is able to rate/review other users prjects

-User is able to search for projects

-User is able to view projects overall score

-User is able to view profile page


## Setup Instructions and Installation
For the application to run, you have to install:

- python3.8

- Django framework

- virtual environment

- Postgres

Setup and Installation
- open terminal

- git clone this repository https://github.com/Edwike12/Lets_share

- use a code editor

- Actvate the virtual env 

        -$ source venv/bin/activate

- Install dependancies 

        -$ pip install -r requirements.txt

- Create a database

        -psql

        -CREATE DATABASE share;

- .env file- create  .env file and hve the following filling where appropriate:

            -SECRET_KEY = '<Secret_key>'

            -DBNAME = 'share'

            -USER = '<Username>'

            -PASSWORD = '<password>'

            -DEBUG = True

- Run initial migration

        -$ python3.8 manage.py makemigrations share

        -$ python3.8 manage.py migrate

- Run the app

        -$ python3.8 manage.py runserver


## Technologies used
- python3.8

- Django

- Html, Css and Bootstrap

- postgres sql

- Heroku


## Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug


## Development 
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request


### Testing Application
-To run the tests for the class files:

    -$ python3.6 manage.py test




### contact information
Feel free to reach out:

Email: nyaunchoedwike@gmail.com




