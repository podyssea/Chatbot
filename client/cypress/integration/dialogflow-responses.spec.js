import firebase from 'firebase/app';
import 'firebase/functions';

const config = {
    apiKey: "AIzaSyBxjacU5G1EF4UC82N_JJSbrXcTLh9OT6Q",
    authDomain: "prototype-624d5.firebaseapp.com",
    databaseURL: "https://prototype-624d5.firebaseio.com",
    projectId: "prototype-624d5",
    storageBucket: "prototype-624d5.appspot.com",
    messagingSenderId: "156087064273"
};
firebase.initializeApp(config);

let makeQuery = (query) => {
    return new Cypress.Promise((resolve, reject) => {
        let message = firebase.functions().httpsCallable('message');
        message({
            query: query
        }).then((result) => {
            return resolve(result);
        });
    });
}


describe('Dialogflow detects the correct intent fromt the following queries:', function () {
    beforeEach(function () {
        let intent = "";
     });
    it('Show me all available courses.', function () {
        cy.wrap(null).then(() => {
            return makeQuery('all available courses').then((response) => {
                expect(response.data.intent).to.equal('Available Courses');
            });
        });
    });

    it('Are there any courses for 40 pounds?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Are there any courses for 40 pounds?').then((response) => {
                expect(response.data.intent).to.equal('Cost -> Title');
            });
        });
    });

    it('Are there any courses with zero credits?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Are there any courses with zero credits?').then((response) => {
                expect(response.data.intent).to.equal('Credits -> Title');
            });
        });
    });

    it('Are there any courses with duration of one day?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Are there any courses with duration of one day?').then((response) => {
                expect(response.data.intent).to.equal('Duration -> Title');
            });
        });
    });

    it('What are the courses finishing on the 24th November?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What are the courses finishing on the 24th November?').then((response) => {
                expect(response.data.intent).to.equal('End date -> Title');
            });
        });
    });


    it('How much do i have to pay for the course with id 2580?', function () {
 
        cy.wrap(null).then(() => {
            return makeQuery('How much do i have to pay for the course with id 2580?').then((response) => {
                expect(response.data.intent).to.equal('ID -> Cost');
            });
        });
    });


    it('How many credits does id 2580 give?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('How many credits does id 2580 give?').then((response) => {
                expect(response.data.intent).to.equal('ID -> Credits');
            });
        });
    });

    it('What is the description of class code 2580?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the description of class code 2580?').then((response) => {
                expect(response.data.intent).to.equal('ID -> Description');
            });
        });
    });


    it('What is the end date of course with ID 2580?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the end date of course with ID 2580?').then((response) => {
                expect(response.data.intent).to.equal('ID -> End Date');
            });
        });
    });


    it('What is the start date of course with ID 2580?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the start date of course with ID 2580?').then((response) => {
                expect(response.data.intent).to.equal('ID -> Start Date');
            });
        });
    });

    it('What is the subject area of course with ID 2580?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the subject area of course with ID 2580?').then((response) => {
                expect(response.data.intent).to.equal('ID -> Subject Area');
            });
        });
    });


    it('What is the title of course with ID 2580?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the title of course with ID 2580?').then((response) => {
                expect(response.data.intent).to.equal('ID -> Title');
            });
        });
    });

    it('Who teaches course with ID 2580?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Who teaches course with ID 2580?').then((response) => {
                expect(response.data.intent).to.equal('ID -> Tutor');
            });
        });
    });

    it('What is the venue of course with ID 2580?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the venue of course with ID 2580?').then((response) => {
                expect(response.data.intent).to.equal('ID -> Venue');
            });
        });
    });

    it('Which courses begin on the twenty fourth of november?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Which courses begin on the twenty fourth of november?').then((response) => {
                expect(response.data.intent).to.equal('Start date -> Title');
            });
        });
    });

    it('Are there any classes about Archaeology Classical Studies and Egyptology?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Are there any classes about Archaeology Classical Studies and Egyptology?').then((response) => {
                expect(response.data.intent).to.equal('Subject area -> Title');
            });
        });
    });

    it('What subject areas are there?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What subject areas are there?').then((response) => {
                expect(response.data.intent).to.equal('Subject Areas');
            });
        });
    });


    it('What is the id of Cleopatra: Queen of Egypt?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the id of Cleopatra: Queen of Egypt?').then((response) => {
                expect(response.data.intent).to.equal('Title -> Class Code');
            });
        });
    });


    it('Give me the Cleopatra: Queen of Egypt cost', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Give me the Cleopatra: Queen of Egypt cost').then((response) => {
                expect(response.data.intent).to.equal('Title -> Cost');
            });
        });
    });



    it('I\'d like to know how many credits does Cleopatra: Queen of Egypt gives', function () {

        cy.wrap(null).then(() => {
            return makeQuery('I\'d like to know how many credits does Cleopatra: Queen of Egypt gives').then((response) => {
                expect(response.data.intent).to.equal('Title -> Credits');
            });
        });
    });


    it('What is Cleopatra: Queen of Egypt\'s description?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is Cleopatra: Queen of Egypt\'s description?').then((response) => {
                expect(response.data.intent).to.equal('Title -> Description');
            });
        });
    });

    it('What is the length of Cleopatra: Queen of Egypt?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the length of Cleopatra: Queen of Egypt?').then((response) => {
                expect(response.data.intent).to.equal('Title -> Duration');
            });
        });
    });


    it('What is the end date of Cleopatra: Queen of Egypt?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the end date of Cleopatra: Queen of Egypt?').then((response) => {
                expect(response.data.intent).to.equal('Title -> End Date');
            });
        });
    });

    it('What is the start date of Cleopatra: Queen of Egypt?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the start date of Cleopatra: Queen of Egypt?').then((response) => {
                expect(response.data.intent).to.equal('Title -> Start Date');
            });
        });
    });

    it('Can you tell me the subject area of Cleopatra: Queen of Egypt?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Can you tell me the subject area of Cleopatra: Queen of Egypt?').then((response) => {
                expect(response.data.intent).to.equal('Title -> Subject Area');
            });
        });
    });

    it('Who teaches Cleopatra: Queen of Egypt', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Who teaches Cleopatra: Queen of Egypt').then((response) => {
                expect(response.data.intent).to.equal('Title -> Tutor');
            });
        });
    });

    it('What is the venue for Cleopatra: Queen of Egypt?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the venue for Cleopatra: Queen of Egypt?').then((response) => {
                expect(response.data.intent).to.equal('Title -> Venue');
            });
        });
    });

    it('What are the courses taught by Jane Draycott?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What are the courses taught by Jane Draycott?').then((response) => {
                expect(response.data.intent).to.equal('Tutor -> Title');
            });
        });
    });


    it('What are the courses in the main building?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What are the courses in the main building').then((response) => {
                expect(response.data.intent).to.equal('Venue -> Title');
            });
        });
    });








    

    

    
});