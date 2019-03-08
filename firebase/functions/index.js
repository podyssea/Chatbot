const functions = require('firebase-functions');
const admin = require('firebase-admin');
const dialogflow = require('dialogflow');

admin.initializeApp({
    credential: admin.credential.applicationDefault()
});

admin.firestore().settings({
    timestampsInSnapshots: true
});

const projectId = 'prototype-624d5';
const sessionId = 'firebase-testing-session';
const languageCode = 'en-US';
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
        console.log(result.action);

        const intent = result.intent;
        const action = result.action;

        const text = result.fulfillmentText;
        let status = 500; // 500 is an error

        // const smallTalkHello = ['smalltalk.greetings.goodevening', 'smalltalk.greetings.goodmorning', 'input.welcome', 'smalltalk.greetings.how_are_you', 'smalltalk.greetings.nice_to_meet_you', 'smalltalk.greetings.nice_to_talk_to_you', 'smalltalk.greetings.whatsup'];
        const smallTalkBye = ['smalltalk.greetings.goodnight', 'smalltalk.greetings.bye'];

        if (smallTalkBye.indexOf(action) > -1) {
            // we need this to be able to know when we are done talking
            status = 300;
        } else if (smallTalkBye.indexOf(action) === -1 && action.startsWith('smalltalk')) {
            status = 200;
        } else if (intent) {
            // here we actually match an intent
            if (text.length !== 0) {
                status = 200;
            }
            if (intent.displayName === 'Text-To-Speech ON') {
                status = 600;
            } else if (intent.displayName === 'Text-To-Speech OFF') {
                status = 700;
            } else if (intent.displayName === 'Send email to client') {
                status = 800;
            }

        }

        return {resp:text, status: status};

    });

});

// stupid mail function that doesn't work. thanks google for your examples that never work
// exports.mail = functions.https.onCall((data, context) => {
//     // these are declared in the GCP console for functions in the mail function
//
//     const password = process.env.gmailpassword;
//     const email = process.env.gmailemail;
//     console.log(email);
//     console.log(password);
//
//     const mailTransport = nodemailer.createTransport({
//         service: 'Gmail',
//         auth: {
//             user: email,
//             pass: password
//         }
//     });
//
//     const mailOptions = {
//         to: email
//     };
//
//     mailOptions.subject = data.name + ' has a question.';
//     mailOptions.text = data.query;
//
//     return mailTransport.sendMail(mailOptions, (err, info) => {
//         if (err) {
//             console.log(err);
//             return {resp: 'Failed to send', status: 500};
//         }
//         return {resp: 'Sent', status: 200};
//     })
// });

