# External Relations Chat-Bot

Developed to deal with redundant queries about University of Glasgow short courses.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

Please ensure all dependancies for both client and server are fully installed in order to run the project.

#### Installing client dependancies

```
$ npm install
```

#### Installing server dependancies

Make sure to run
```bash
$ pip install -r requirements.txt
```

or if you are not using a virtual environment,
```bash
$ pip3 install -r requirements.txt
```

when in the folder with that file. It is recommended to run the server in a virtual environment.


## Installing

The following commands for running the client and server must be ran simoultaneously in different terminals in order to run the full project.

### Running the client

Simply run

```
$ npm run dev
```

### Running the server

To run the server itself, in the folder where ```manage.py``` exists, run
```bash
$ python manage.py runserver 5000
```

or if you are not using a virtual environment,
```bash
$ python3 manage.py runserver 5000
```

## Testing

### Snapshot and Dialogflow intents tests

These tests have been developed using the Cypress testing framework
First navigate to the `client` directory

To install cypress run the following command
```
$ npm install cypress
```
To run the tests:

```
$ npm run cypress:open
```

### Server tests

Within the folder that contains ```manage.py```, run

```bash
$ python manage.py test
```

or if you are not using a virtual environment,
```bash
$ python3 manage.py test
```

## Deployment

### Building

Within the `client` directory

```
$ npm run build
```

Will create a `dist` directory containing your compiled code.

Depending on your needs, you might want to do more optimization to the production build.

### Webpack Bundle Analyzer


Run in development

```
$ npm run dev:bundleanalyzer
```

Run on the production optimized build

```
$ npm run build:bundleanalyzer
```


## Built With

* [React](https://reactjs.org/) - Frontend Library
* [DialogFlow](https://dialogflow.com) - Chat-Bot API
* [Django](https://www.djangoproject.com/) - Web Framework
* [Firebase](https://firebase.google.com/) - ???
* add more here ?????

## Contributing

Please read [CONTRIBUTING.md](http://stgit.dcs.gla.ac.uk/tp3-2018-se07/dissertation/blob/documentation/Contiributing.md) for our contact details.


## Authors

* **Anguel Hristozov** - *Backend*
* **Justyna Toporkiewicz** - *DialogFlow*
* **Hannah Mehravari** - *Frontend*
* **Odysseas Polycarpou** - *DialogFlow*
* **Martin Manov** - *DialogFlow*


## License

???

## Acknowledgments

* [React Simple Chatbot](https://lucasbassetti.com.br/react-simple-chatbot/) - Base React component use for frontend
* add more here ????
