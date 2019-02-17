from app.utils import client_test_helper
from json import dumps


def test_app_get(client):
    response = client.get('/')
    assert client_test_helper(response) == (True, True, True, True)
    assert response.get_data().decode('UTF-8') == 'Hello World, from webhook!'


def test_app_empty_post(client):
    response = client.post('/', data={})
    assert client_test_helper(response, c_type='application/json') == (True, True, True, True)
    assert response.get_json().get('fulfillmentText') == 'Something happened on our end.'


def test_app_sample_post(client):
    response = client.post('/', data=dumps(dict({'queryResult': {'intent': {'displayName': 'Test'}}})),
                           content_type='application/json')
    assert client_test_helper(response, c_type='application/json')
    assert response.get_json().get('fulfillmentText') == 'Test Passed'

# ['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__',
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
#  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__', '__weakref__', '_cached_json', '_ensure_sequence', '_get_data_for_json', '_get_mimetype_params',
#  '_is_range_request_processable', '_on_close', '_process_range_request', '_status', '_status_code', '_wrap_response',
#  'accept_ranges', 'add_etag', 'age', 'allow', 'autocorrect_location_header', 'automatically_set_content_length',
#  'cache_control', 'calculate_content_length', 'call_on_close', 'charset', 'close', 'content_encoding',
#  'content_language', 'content_length', 'content_location', 'content_md5', 'content_range', 'content_type', 'data',
#  'date', 'default_mimetype', 'default_status', 'delete_cookie', 'direct_passthrough', 'expires', 'force_type', 'freeze',
#  'from_app', 'get_app_iter', 'get_data', 'get_etag', 'get_json', 'get_wsgi_headers', 'get_wsgi_response', 'headers',
#  'implicit_sequence_conversion', 'is_json', 'is_sequence', 'is_streamed', 'iter_encoded', 'json', 'last_modified',
#  'location', 'make_conditional', 'make_sequence', 'max_cookie_size', 'mimetype', 'mimetype_params',
#  'on_json_loading_failed', 'response', 'retry_after', 'set_cookie', 'set_data', 'set_etag', 'status', 'status_code',
#  'stream', 'vary', 'www_authenticate']
