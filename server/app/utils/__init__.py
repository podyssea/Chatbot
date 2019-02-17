# this method was created to handle when the flask server did not receive a properly formatted post request
def deep_get(dictionary, keys, default=None):
    from functools import reduce
    # https://stackoverflow.com/a/46890853/4004697 for safely getting nested values
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."),
                  dictionary)


# basic helper to check repetitive properties of responses when testing
def client_test_helper(response, c_type='text/html; charset=utf-8'):
    status_code = response.status_code == 200
    content_length = response.content_length > 0
    charset = response.charset == 'utf-8'
    content_type = response.content_type == c_type
    return status_code, content_length, charset, content_type


def database_test_helper(attribute, expected_type, expected_value):
    actual_type = type(attribute) is expected_type
    actual_value = attribute == expected_value
    return actual_type, actual_value
