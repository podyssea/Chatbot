import React from 'react';
import HandleInput from './HandleInputComponent';
import HandleFeedback from './HandleFeedbackComponent'
import TextToSpeech from './TextToSpeechComponenet'

const steps = [
    {
        id: 'start',
        message: 'Hello there! I\'m Gilbert, the UoG external relations chatbot!',
        trigger: '2',
    },
    {
        id: '2',
        user: false,
        message: 'What can I help you with today?',
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
        trigger: 'input',
        asMessage: true,
        waitAction: true,
    },
    {
        id: 'feedback',
        component: < HandleFeedback />,
        end: true
    },
    {
        id: 'speech-toggle',
        component: < TextToSpeech />,
        trigger: 'input'
    },
    {
        id: 'end',
        end: true,
        message: 'Glad we could help! Have a nice day.'
    }
];


export default steps;

