import React from 'react';
import HandleInput from './HandleInputComponent';

const steps = [
    {
        id: 'start',
        message: 'Hello there! I\'m the UoG external relations chatbot! Would you like me to resolve a query?',
        trigger: '1',
    },
    {
        id: '1',
        options: [
            { value: 'yes', label: 'Yes', trigger: '2'},
            { value: 'no', label: 'No', trigger: 'end'}
        ],
    },
    {
        id: '2',
        user: false,
        message: 'Please enter your query.',
        trigger: 'input',
    },
    {
        id: 'input',
        user: true,
        trigger: 'handleInput',
    },
    {
        id: 'handleInput',
        component: < HandleInput />,
        trigger: 'didWeHelpMessage',
        asMessage: true,
        waitAction: true,
    },
    {
        id:'didWeHelpMessage',
        message: 'Did this resolve your query?',
        trigger: 'didWeHelp'
    },
    {
        id: 'didWeHelp',
        options: [
            { value: 'yes', label: 'Yes', trigger: 'end'},
            { value: 'no', label: 'No', trigger: '2'}
        ]
    },
    {
        id: 'end',
        end: true,
        message: 'Glad we could help! Have a nice day.'
    }
];


export default steps;

