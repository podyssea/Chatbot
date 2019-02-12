from flask import jsonify, request
from app.main import bp
from app.intents_handler import intent_handler


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/webhook', methods=['GET', 'POST'])
def index():
    # not a request from DialogFlow
    if request.method == 'GET':
        return 'Hello World, from webhook!'
    else:
        # request from dialogflow
        data = request.get_json()

        user_intent = data['queryResult']['intent']['displayName']

        return_data = intent_handler.handle({'intent': user_intent, 'parameters': data['queryResult']['parameters']})

        return jsonify({'fulfillmentText': return_data})

