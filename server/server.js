const fastify = require('fastify')();
const cors = require('fastify-cors');

fastify.register(cors);

const projectId = 'prototype-624d5';
// const sessionId = 'quickstart-session-id';
const languageCode = 'en-US';

const dialogflow = require('dialogflow');
const sessionClient = new dialogflow.SessionsClient();

// const sessionPath = sessionClient.sessionPath(projectId, sessionId);


fastify.post('/message', async (req, res) => {
    // get the message from the request
    let query = req.body.query;

    // build the request from the message
    // todo: see if the sessionID will be remembered from the front when integrating
    const sessionPath = sessionClient.sessionPath(projectId, String.fromCharCode(req.id));
    let request = {
        session: sessionPath,
        queryInput: {
            text: {
                text: query,
                languageCode: languageCode
            }
        }
    };

    // and now send it off to DF. the response text is in fulfillmentText
    let dfReply = await sessionClient
        .detectIntent(request)
        .then(responses => {
            console.log('Detected intent');
            const result = responses[0].queryResult;
            console.log(`  Query: ${result.queryText}`);
            console.log(`  Response: ${result.fulfillmentText}`);
            if (result.intent) {
                return {Response: result.fulfillmentText};
            } else {
                return {Response: 'No intent matched.'};
            }
        })
        .catch(err => {
            return {ERROR: err};
        });

    // return it to the backend. this is the response text from the agent.
    res.send(dfReply);
});

// this starts the server on port 3000
const start = async () => {
    try {
        await fastify.listen(4000);
        console.log('server listening on 4000');
        fastify.log.info('server listening on 4000');
    } catch (err) {
        console.log(err);
        fastify.log.error(err);
        process.exit(1);
    }
};

start();
