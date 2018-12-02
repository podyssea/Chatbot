import React from 'react';
import ChatBot from 'react-simple-chatbot';
import axios from 'axios';
import {ThemeProvider} from 'styled-components';
import theme from './Theme';


const steps = [
    {
        id: '0',
        message: 'wassss your name?',
        trigger: '1',
    },
    {
        id: '1',
        user: true,
        trigger: '2',
        validator: (value) => {
            let data = {
                query: value
            };
            axios.post('http://127.0.0.1:4000/message', data, {headers: {'Access-Control-Allow-Origin': '*'}}).then(resp => {
                console.log(resp);
                return true;
            }).catch(err => {
                console.log(err);
                return false;
            });
        }
    },
    {
        id: '2',
        user: false,
        message: "well hello there",
        end: true,
    },
];

const App = () => {
    return (
        <ThemeProvider theme={theme}>
            <ChatBot steps={steps} floating={true}/>
        </ThemeProvider>
    );
};

export default App;
