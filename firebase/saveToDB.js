const parse = require('csv-parse');
const admin = require('firebase-admin');
const fs = require('fs');
let serviceAccount = require('./firebaseServiceAccount.json');

let file = 'Short_Courses_Data.csv';

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
});

admin.firestore().settings({
    timestampsInSnapshots: true
});

// reference to the firebase database
let db = admin.firestore();
let course_ref = db.collection('courses');

// now parse the csv
const parser = parse({
    delimiter: ','
}, (err, data) => {
    // let columnHeaders = data[0];
    // console.log(columnHeaders);
    data.slice(1).forEach((line) => {
        // save each line to database. for now it will all be in one object :(
        let item = course_ref.doc(line[2]).set({
            'Subject Area': line[0],
            'Title': line[1],
            'Start Date': line[3],
            'End Date': line[4],
            'Start Time': line[5],
            'End Time': line[6],
            'Cost': line[7],
            'Duration': line[8],
            'Tutor': line[9],
            'Venue': line[10],
            'Course Specification Link': line[11],
            'Course Description': line[12],
            'Credits': line[13],
            'Language Level of Study Link': line[14]
        });
    });
});


fs.createReadStream(file).pipe(parser);

