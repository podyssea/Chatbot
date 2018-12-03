const functions = require('firebase-functions');
const admin = require('firebase-admin');

admin.initializeApp({
    credential: admin.credential.applicationDefault()
});

admin.firestore().settings({
    timestampsInSnapshots: true
});

const projectId = 'prototype-624d5';
const sessionId = 'firebase-testing-session';
const languageCode = 'en-US';
const dialogflow = require('dialogflow');
const sessionClient = new dialogflow.SessionsClient();
const sessionPath = sessionClient.sessionPath(projectId, sessionId);

exports.message = functions.https.onCall((data, context) => {
    let query = data.query;

    let request = {
        session: sessionPath,
        queryInput: {
            text: {
                text: query,
                languageCode: languageCode
            }
        }
    };

    return sessionClient.detectIntent(request).then(responses => {
        console.log('Detected Intent');
        const result = responses[0].queryResult;
        console.log(`  Query: ${result.queryText}`);
        console.log(`  Response: ${result.fulfillmentText}`);
        if (result.intent) {
            let status = 200;
            let text = result.fulfillmentText;
            if (text.charAt(text.length - 1) === '?'){
                status = 400; // this means that the return response was a question
                // and dialogflow did not understand.
            }
            return {resp: text, status: status};
        } else {
            return {resp: 'No intent matched.', status: 500};
        }
    });

});

