import React from 'react';
import ChatBot from 'react-simple-chatbot';
import Loading from './Loading';
import { ThemeProvider } from 'styled-components';

const theme = {
  background: '#f5f8fb',
  fontFamily: 'Swiss 721 BT',
  headerBgColor: '#005398',
  headerFontColor: '#fff',
  headerFontSize: '15px',
  botBubbleColor: '#005398',
  botFontColor: '#fff',
  userBubbleColor: '#fff',
  userFontColor: '#4a4a4a',
};

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
  },
  {
    id: '2',
    user: false,
    message : "well hello there {previousValue}",
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
