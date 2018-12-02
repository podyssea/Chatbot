const fastify = require('fastify')();


const projectId = 'prototype-624d5';
const sessionId = 'quickstart-session-id';
const query = 'When does course begin?';
const languageCode = 'en-US';

const dialogflow = require('dialogflow');
const sessionClient = new dialogflow.SessionsClient();

const sessionPath = sessionClient.sessionPath(projectId, sessionId);

// The text query request.
// const request = {
//     session: sessionPath,
//     queryInput: {
//         text: {
//             text: query,
//             languageCode: languageCode,
//         },
//     },
// };

fastify.post('/message', async (req, res) => {
    // get the message from the request
    console.log(req.body.query);
    res.send({Body: req.body});


    // sessionClient
    //     .detectIntent(request)
    //     .then(responses => {
    //         console.log('Detected intent');
    //         const result = responses[0].queryResult;
    //         console.log(`  Query: ${result.queryText}`);
    //         console.log(`  Response: ${result.fulfillmentText}`);
    //         if (result.intent) {
    //             reply.send({Intent: result.intent.displayName});
    //         } else {
    //             reply.send({Intent: 'No intent matched.'});
    //         }
    //     })
    //     .catch(err => {
    //         reply.send({ERROR: err});
    //     });
});

// this starts the server on port 3000
const start = async () => {
    try {
        await fastify.listen(3000);
        fastify.log.info('server listening on 3000');
    } catch (err) {
        fastify.log.error(err);
        process.exit(1);
    }
};

start();
