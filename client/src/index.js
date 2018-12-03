import {AppContainer} from 'react-hot-loader';
import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';
import Firebase, {FirebaseContext} from './components/Firebase/Index';


const render = Component =>
    ReactDOM.render(
        <FirebaseContext.Provider value={new Firebase()}>
            <AppContainer>
                <Component/>
            </AppContainer>
        </FirebaseContext.Provider>,
        document.getElementById('root')
    );

render(App);
if (module.hot) module.hot.accept('./components/App', () => render(App));
