## Current Issues

These are issues we identified but were not able to fix in time.

## Current issues
### Refactor the database to have proper relations and be more flexible
### Refactor React code to make it follow proper React practices
Currently our React code is not structured correctly according to React coding conventions.
### Phase out firebase
### Figure out better way to integrate text-to-speech
The current implementation of the text-to-speech feature is quite 'hacky'. There is a window variable in the index.html file that is updated
every time the text-to-speech is turned on and off. We add this as we could not find a way to keep a global variable for this using Node
### Look into Microsoft Forms instead of TypeForm
The clients expressed interest in us finding a Microsoft service to deal with the feedback form as they already use a lot of Microsoft services.
Time did not allow for us to fully investigate this.
### Find some way to encourage the user to take the feedback form
The clients expressed interest in finding a way to encourage user to actually leave feedback as right now the feedback form is only prompted when
a user says 'bye' to the chatbot. This could probably be improved by triggering the feedback form with a timeout when the user has be inactive for
a while or a pop up of some sort on the main page.

