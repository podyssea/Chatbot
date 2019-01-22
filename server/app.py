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

        # what follows is a very hacky way to show all courses for a specific subject. only god can judge me now
        query_text = data['queryResult']['queryText']
        if query_text[0: 20] == 'courses for subject ':
            return jsonify({'fulfillmentText': intent_handler.handle(query_text)})

        intent = data['queryResult']['intent']["displayName"]
        return_data = intent_handler.handle(intent)
        return jsonify({'fulfillmentText': return_data})


# run the app
if __name__ == '__main__':
    app.run()

