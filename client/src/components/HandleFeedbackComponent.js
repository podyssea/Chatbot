import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';
import StarRatingComponent from 'react-star-rating-component';


class HandleFeedbackComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            rating: 5
        };

        this.triggerNext = this.triggerNext.bind(this);
    }

    onStarClick(nextValue, prevValue, name) {
        this.setState({rating: nextValue});
        console.log('star clicked');
        // this.triggerNext();
    }

    componentDidMount() {
        console.log('mounted handle feedback component');
    }

    triggerNext(value, trigger) {
        this.setState({trigger: true}, () => {
            this.props.triggerNextStep(value ? {value, trigger} : {});
        });
    }


    render() {
        const { rating } = this.state;
        // https://github.com/voronianski/react-star-rating-component this was used
        return (
            <div className="handlefeedbackcomponent">
                <h2>
                <StarRatingComponent
                    name="feedbackRating"
                    starCount={5}
                    value={rating}
                    onStarClick={this.onStarClick.bind(this)}
                /></h2>
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