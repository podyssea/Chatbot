# import flask dependencies
from flask import Flask, request, jsonify
# from pprint import pprint
from server.utils import intent_handler

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
        intent = data['queryResult']['intent']["displayName"]
        return_data = intent_handler.handle(intent)
        return jsonify({'fulfillmentText': return_data})


# run the app
if __name__ == '__main__':
    intent_handler.set_up()
    app.run()

# function for responses
'''def results():
    # build a request object
    req = request.get_json(force=True)
    # fetch action from json
    action = req.get('queryResult').get('action')
    # return a fulfillment response
    return {'fulfillmentText': 'This is a response from webhook.'}

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])

def webhook():
    # return response
    return make_response(jsonify(results()))'''
