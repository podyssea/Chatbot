const functions = require('firebase-functions');
const admin = require('firebase-admin');

admin.initializeApp({
    credential: admin.credential.applicationDefault()
});

admin.firestore().settings({
    timestampsInSnapshots: true
});

exports.message = functions.https.onCall((data, context) => {
    return {Response: 'allo', Sucess: true};
});

