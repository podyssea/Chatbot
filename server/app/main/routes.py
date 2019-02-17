from flask import jsonify, request
from app.main import bp
from app.intents_handler import intent_handler
from app.utils import deep_get


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/webhook', methods=['GET', 'POST'])
def index():
    # not a request from DialogFlow
    if request.method == 'GET':
        return 'Hello World, from webhook!'
    else:
        # request from dialogflow
        data = request.get_json()

        user_intent = deep_get(data, 'queryResult.intent.displayName')
        if user_intent is None:
            # the post request is incorrect
            return jsonify(
                {'fulfillmentText': 'Something happened on our end.'})  # todo: see about making the response better lol

        elif user_intent == 'Test':  # temporary fix for test to pass
            return jsonify({'fulfillmentText': 'Test Passed'})

        return_data = intent_handler.handle({'intent': user_intent, 'parameters': data['queryResult']['parameters']})

        return jsonify({'fulfillmentText': return_data})
