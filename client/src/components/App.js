import React from 'react';
import ChatBot from 'react-simple-chatbot';
import {ThemeProvider} from 'styled-components';
import theme from './Theme';
import steps from './Steps';



const App = () => {
    return (
        <ThemeProvider theme={theme}>
            <ChatBot steps={steps} floating={true} headerTitle='External Relations ChatBot' hideUserAvatar='true'/>
        </ThemeProvider>
    );
};

export default App;