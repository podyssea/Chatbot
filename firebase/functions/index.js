const functions = require('firebase-functions');
const admin = require('firebase-admin');
const { WebhookClient } = require('dialogflow-fulfillment');

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
            if (text.charAt(text.length - 1) === '?') {
                status = 400; // this means that the return response was a question
                // and dialogflow did not understand.
            }else if (text.length === 0){
                status = 500
            }
            return {resp: text, status: status};
        } else {
            return {resp: 'No intent matched.', status: 500};
        }
    });

});

process.env.DEBUG = 'dialogflow:debug';
exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
    const agent = new WebhookClient({request, response});
    console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
    console.log('Dialogflow Request body: ' + JSON.stringify(request.body));

    function classCodeHandler(agent) {
        // console.log(db);
        agent.send('hello there');
    }

    // Run the proper function handler based on the matched Dialogflow intent name
    let intentMap = new Map();
    intentMap.set('Class code', classCodeHandler);
    agent.handleRequest(intentMap);
});

