from json import dumps

from django.test import TestCase, Client


class AppGetTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.response = cls.client.get('/')

    def test_get_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_content_length(self):
        self.assertGreater(len(str(self.response.content)), 0)

    def test_get_charset_type(self):
        self.assertEqual(self.response.charset, 'utf-8')

    def test_get_body_content(self):
        self.assertEqual(self.response.content.decode('utf-8'), 'Hello World, from webhook!')


class AppEmptyPostTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.response = cls.client.post('/', data=dumps({}), format='json', content_type='application/json')

    def test_post_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_content_length(self):
        self.assertGreater(len(str(self.response.content)), 0)

    def test_post_charset_type(self):
        self.assertEqual(self.response.charset, 'utf-8')

    def test_post_body_content(self):
        self.assertJSONEqual(self.response.content.decode('utf-8'),
                             {'fulfillmentText': 'Something happened on our end.'})


class AppSamplePostTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.response = cls.client.post('/', dumps(dict({'queryResult': {'intent': {'displayName': 'Test'}}})),
                                       format='json', content_type='application/json')

    def test_post_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_content_length(self):
        self.assertGreater(len(str(self.response.content)), 0)

    def test_post_charset_type(self):
        self.assertEqual(self.response.charset, 'utf-8')

    def test_post_body_content(self):
        self.assertJSONEqual(self.response.content.decode('utf-8'), {'fulfillmentText': 'Test Passed'})


class IntentTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
