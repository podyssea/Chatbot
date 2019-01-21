# import flask dependencies
from flask import Flask, request

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
        return request.data


# run the app
if __name__ == '__main__':
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
