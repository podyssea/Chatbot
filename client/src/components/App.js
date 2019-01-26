import React from 'react';
import ChatBot from 'react-simple-chatbot';
import {ThemeProvider} from 'styled-components';
import theme from './Theme';
import steps from './Steps';


class App extends React.Component {

    render() {
        return (
            <div>
                <ThemeProvider theme={theme}>
                    <ChatBot steps={steps} floating={true} headerTitle='Gilbert'
                             speechSynthesis={{enable: false, lang: 'en'}} hideUserAvatar='true'/>
                </ThemeProvider>
            </div>
        );
    }
}

export default App;
