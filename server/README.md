# How to set up the Flask webhook server

## Table of Contents
1. [Description](#description)
2. [Requirements](#requirements)
3. [Setting up environmental variables](#setting-up-environmental-variables)
4. [Database updates and migrations](#database-updates-and-migrations)
5. [Running the server](#running-the-server)

## Description
The server within folder `server` receives the POST request from DialogFlow. It has one entry point
`/` (alternatively listens for `/webhook` as well) and then passes the data from that request to a module
aptly named `intent_handler` in the `intents_handler` folder.

That file is the one responsible for communicating with the database using the `db` object (which is an SQLAlchemy object)
and then returning the data to DialogFlow.

## Requirements
This server runs on Python 3. It is recommended to make a virtual environment for it, as to not mess up your system python installation.

To install all the required packages, go into the `server` folder and run 
```bash
$ pip install -r requirements
```
Please note, the above command assumes that you have created and are using a virtual environment with Python 3. If you are not, then run it as so
```bash
$ pip3 install -r requirements.txt
```

## Setting up environmental variables
Within `server`, there is a file named `.flaskev.example`. In practice, it is bad to commit .env files since
they contain sensitive information, such as secret keys and passwords. The example env file shows the syntax of how your
personal `.flaskenv` file should look like. The different keys are explained below:

* FLASK_APP = this is always `webserver.py`. For when you type ```$ flask run```, this is the file that gets called, which in turn
starts the server.

* FLASK_ENV = this is either `development` or `production`. On your local machine, keep it on `development` in order to see all logs and whatnot.
On the production server, keep it `production` so flask works as intended in production.

* SECRET_KEY = this is up to you. It is any line of characters, any length, that is used by flask for various reasons. It should not be "secret" or something easily guessable.

* DATABASE_URL = this is used by SQLAlchemy to connect to the database. Where you see `{}`, replace it with the respective text that it says. So if your user is named
`testuser`, the password is `secret_password`, the url is `db.aws.whatever`, and the database name is `our_table`, it would look like
`mysql+pymysql://testuser:secret_password@db.aws.whatever/our_table`

**Never commit your personal `.flaskenv` file to the repository.**

## Database updates and migrations
The schema for the database is located in `server/app/models.py`. It specifies the name of the fields as well as what type they are. Please be careful when making changes to the types, as
it can result in data loss.

If you decide to change the type of anything else, you have to migrate and then update it in the actual database.

To migrate, run
```bash
$ flask db migrate
```

and then to update the database itself, run
```bash
$ flask db upgrade
```

In case you ever decide to revert to the previous migration, run
```bash
$ flask db downgrade
```

## Running the server
To run it, go into the root of the `server` folder and in the command line, write 
```bash
$ flask run
```

and the server will run. That should be all it takes to run it.
