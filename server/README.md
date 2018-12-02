To run this server locally, first you need to download the ```account.json``` file that was uploaded in the discord chat and store it in the root of the ```server``` folder.

Once this is done, open up the command line and cd into the ```server``` folder. Please note the absolute file path of the ```account.json``` file. 

Copy it. 

_Do it_ 

Once in it, in the command line, write

```
$ export GOOGLE_APPPLICATION_CREDENTIALS=ctrl+v
```
where ctrl+v is you pasting the file path you just copied above.

For example, it could look like

```
$ export GOOGLE_APPLICATION_CREDENTIALS=/home/anguel/PycharmProjects/dissertation/server/account.json
```

Once this is done, still in the same directory on the command line, run 

```
$ npm run dev
```
which will start the api server for you. This server will run on port 4000. This is different than the React Webpack server because this is the backend and communicates with DialogFlow.