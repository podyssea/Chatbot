import React, {Component} from 'react';
import PropTypes from 'prop-types';
import firebase from 'firebase/app';
import 'firebase/functions';
import parse from 'html-react-parser';
import StarRatingComponent from 'react-star-rating-component';



class HandleFeedbackComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            rating: 5,
            editable: true,
            comment: "", // for now, comment is empty until it is implemented as an element
        };

        this.triggerNext = this.triggerNext.bind(this);
    }


    onStarClick(nextValue, prevValue, name) {
        this.setState({rating: nextValue, editable: false});
        let submitFeedback = firebase.functions().httpsCallable('feedback');

        submitFeedback({comment: this.state.comment, rating: nextValue}).then((res) => {
            console.log('feedback saved');
        });

        this.triggerNext();
    }

    triggerNext(value, trigger) {
        this.setState({trigger: true}, () => {
            this.props.triggerNextStep(value ? {value, trigger} : {});
        });
    }


    render() {
        const { rating, editable } = this.state;
        let styles = {
            height: '300px',
            width: '100%'
        };
        // https://github.com/voronianski/react-star-rating-component this was used
        return (
            <div className="handlefeedbackcomponent" style={styles}>
                {/*<h1>*/}
                {/*<StarRatingComponent*/}
                    {/*name="feedbackRating"*/}
                    {/*starCount={5}*/}
                    {/*value={rating}*/}
                    {/*editing={editable}*/}
                    {/*onStarClick={this.onStarClick.bind(this)}*/}
                {/*/></h1>*/}
                {parse('<iframe id="typeform-full" width="100%" height="100%" frameborder="0" src="https://externalrelations3.typeform.com/to/fAkmQs"></iframe> <script type="text/javascript" src="https://embed.typeform.com/embed.js"></script>')}
            </div>
        );
    }
}

HandleFeedbackComponent.propTypes = {
    steps: PropTypes.object,
    triggerNextStep: PropTypes.func
};

HandleFeedbackComponent.defaultProps = {
    steps: undefined,
    triggerNextStep: undefined,
};

export default HandleFeedbackComponent;