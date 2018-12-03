//https://www.robinwieruch.de/complete-firebase-authentication-react-tutorial/#react-firebase

import app from 'firebase/app';

const config = {
    apiKey: "AIzaSyBxjacU5G1EF4UC82N_JJSbrXcTLh9OT6Q",
    authDomain: "prototype-624d5.firebaseapp.com",
    databaseURL: "https://prototype-624d5.firebaseio.com",
    projectId: "prototype-624d5",
    storageBucket: "prototype-624d5.appspot.com",
    messagingSenderId: "156087064273"
};

class Firebase {
    constructor() {
        app.initializeApp(config);
    }
}

export default Firebase;
