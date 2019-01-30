// this is the react component that will be shown and also send the question to the backend
import React, {Component} from 'react';
import PropTypes from 'prop-types';
import firebase from 'firebase/app';
import 'firebase/functions';
import { Loading } from 'react-simple-chatbot';


const config = {
    apiKey: "AIzaSyBxjacU5G1EF4UC82N_JJSbrXcTLh9OT6Q",
    authDomain: "prototype-624d5.firebaseapp.com",
    databaseURL: "https://prototype-624d5.firebaseio.com",
    projectId: "prototype-624d5",
    storageBucket: "prototype-624d5.appspot.com",
    messagingSenderId: "156087064273"
};
firebase.initializeApp(config);

class HandleInputComponent extends Component {
    constructor(props) {
        super(props);

        this.state = {
            loading: true,
            result: '',
            trigger: false,
            textToSpeech : false
        };

        this.triggerNext = this.triggerNext.bind(this);
    }

    componentDidMount() {
        const self = this;
        const {steps} = this.props;
        const query = steps.input.value; // this is the value that the user gave aka their query string

        let message = firebase.functions().httpsCallable('message');
        message({
            query: query
        }).then((result) => {
            let status = result.data.status;
            console.log(status);
            let response = result.data.resp;
            console.log(response);
            if (status === 200) {
                self.setState({loading: false, result: response});
                self.triggerNext();
            } else if (status === 300) {
                self.setState({loading: false, result: 'Glad we could help. Have a nice day! One last thing...if you could please rate our service, we would appreciate it!'});
                self.triggerNext('feedback', 'feedback');
            } else if (status === 500) {
                self.setState({loading: false, result: 'Sorry, I\'m currently not knowledgeable enough to answer that question, Please rephrase or try another question!'});
                self.triggerNext();
                // this is where no intent was matched i.e. the agent has not been been taught this
            } else if (status === 600){
                window.ttsOn = true;
                self.setState({loading: false, result: 'You\'ve enabled text-to-speech!', textToSpeech: true});
                self.triggerNext();

            }else if (status === 700 ) {
                window.ttsOn = false;
                self.setState({loading: false, result: 'You\'ve disabled text-to-speech!'});
                self.triggerNext();

            }
            if (window.ttsOn) {
            this.play(this.state.result);
        }
        });

    }

    triggerNext(value, trigger) {
        this.setState({trigger: true}, () => {
            this.props.triggerNextStep(value ? {value, trigger} : {});
        });
    }

    play(text){
        responsiveVoice.speak(text, 'UK English Male');
    }

    render() {
        const {loading, result} = this.state;

        return (
            <div className="handleinputcomponent">
                {loading ? <Loading/> : result }
                {
                    !loading &&
                    <div
                        style={{
                            textAlign: 'center',
                            marginTop: 20,
                        }}
                    >
                    
                    </div>
                }
            </div>
        );
    }
}

HandleInputComponent.propTypes = {
    steps: PropTypes.object,
    triggerNextStep: PropTypes.func
};

HandleInputComponent.defaultProps = {
    steps: undefined,
    triggerNextStep: undefined,
};

export default HandleInputComponent;
