import React from 'react';
import HandleInput from './HandleInputComponent';

const steps = [
    {
        id: 'start',
        message: 'Hi! Could I help you find something out about a course?',
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
        message: 'Please write your question.',
        trigger: 'input',
    },
    {
        id: 'input',
        user: true,
        trigger: 'handleInput'
    },
    {
        id: 'handleInput',
        component: < HandleInput />,
        trigger: 'didWeHelp',
        waitAction: true,
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

