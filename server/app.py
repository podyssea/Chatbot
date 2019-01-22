# import flask dependencies
from flask import Flask, request, jsonify
# from pprint import pprint
from utils import intent_handler

# initialize the flask app
app = Flask(__name__)


# default route
@app.route('/', methods=['POST', 'GET'])
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


# run the app
if __name__ == '__main__':
    app.run()

