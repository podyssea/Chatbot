import React from 'react';
import ChatBot from 'react-simple-chatbot';
import Loading from './Loading';

const steps = [
  {
    id: '0',
    message: 'Welcome to react chatbot!',
    trigger: '1',
  },
  {
    id: '1',
    message: 'Bye!',
    end: false,
  },
];

const App = () => {
  return (
    <div>
    <ChatBot steps={steps} floating={true}/>
  </div>
  );
};

export default App;
