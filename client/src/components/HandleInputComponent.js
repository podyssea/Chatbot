// this is the react component that will be shown and also send the question to the backend
import React, {Component} from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import { Loading } from 'react-simple-chatbot';

class HandleInputComponent extends Component {
    constructor(props) {
        super(props);

        this.state = {
            loading: true,
            result: '',
            trigger: false
        };

        this.triggerNext = this.triggerNext.bind(this);
    }

    componentDidMount() {
        const self = this;
        const {steps} = this.props;
        const query = steps.input.value; // this is the value that the user gave aka their query string

        const intentApi = 'http://localhost:4000/message'; // where to post to
        const data = {
            query: query
        };
        // this is needed because of the current architecture
        const headers = {
            headers: {
                'Access-Control-Allow-Origin': '*'
            }
        };

        axios.post(intentApi, data, headers).then(resp => {
            console.log(resp);
            if (resp.status === 200 && resp.statusText === 'OK')
                self.setState({loading: false, result: resp.data.Response});
            else
                self.setState({loading: false, result: 'Something happened, please try again.'});
        }).catch(err => {
            console.log(err);
            self.setState({loading: false, result: 'Something happened, please try again.'});
        });

    }

    triggerNext() {
        this.setState({trigger: true}, () => {
            this.props.triggerNextStep();
        });
    }

    render() {
        const {trigger, loading, result} = this.state;

        return (
            <div className="handleinputcomponent">
                {loading ? <Loading/> : result}
                {
                    !loading &&
                    <div
                        style={{
                            textAlign: 'center',
                            marginTop: 20,
                        }}
                    >
                        {
                            !trigger &&
                            <button
                                onClick={() => this.triggerNext()}
                            >
                                Did this answer your query?
                            </button>
                        }
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
