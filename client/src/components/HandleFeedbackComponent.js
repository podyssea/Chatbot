import React, {Component} from 'react';
import PropTypes from 'prop-types';
import firebase from 'firebase/app';
import 'firebase/functions';
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
        // https://github.com/voronianski/react-star-rating-component this was used
        return (
            <div className="handlefeedbackcomponent">
                <h1>
                <StarRatingComponent
                    name="feedbackRating"
                    starCount={5}
                    value={rating}
                    editing={editable}
                    onStarClick={this.onStarClick.bind(this)}
                /></h1>
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