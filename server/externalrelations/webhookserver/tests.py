from json import dumps

from django.test import TestCase, Client
from .models import ShortCourse
import datetime


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

# ---------------------------------------------- models.py ----------------------------------------------
class AncientEgyptAndIllustrationTestCase(TestCase):
    @classmethod
    def setUp(self):
        ShortCourse.objects.create(Subject_area = 'Archaeology Classical Studies and Egyptology', Title = 'Ancient Egypt and the Bible', Class_code = 9248, Start_time = 19.00, End_time = 21.00, Cost = 125.00, Duration = 64, Tutor = 'Judit Blair', Venue = 'University of Glasgow- Building will be confirmed by email three days before the start date. Room number will be listed at reception on the day/evening of the class', Link_to_Course_specification = 'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11520E', Description = 'Christian thinking has been greatly influenced by ancient traditions. According to the Bible, throughout history there had always been a contact between the Egyptians and the Israelites. Indeed, Egyptology in the 19th century was mainly concerned with discovering cultural records and thus evidence for certain biblical events. Without intending to prove or disprove the historicity of biblical events or characters, this course looks at similar themes in the religions of ancient Egypt and Israel, as well as key figures using the latest discoveries in the field.', Credits_attached = 10, Language_Level_of_Study_link = 'N/A', Start_date = datetime.datetime(2019, 1, 17), End_date = datetime.datetime(2019, 3, 21))
        ShortCourse.objects.create(Subject_area = 'Art and Art History', Title = 'Botanical painting and illustration', Class_code = 13926, Start_time = 9.30, End_time = 12.30, Cost = 180.00, Duration = 10, Tutor = 'Clare Crines', Venue = 'University of Glasgow- Building will be confirmed by email three days before the start date. Room number will be listed at reception on the day/evening of the class', Link_to_Course_specification = 'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11217', Description = 'This course is suitable for beginners and students with some previous experience. It is for people with little or no prior drawing experience who want to learn how to draw flowers, fruit and vegetables with ease. Through tutor demonstrations you will see how to use watercolour properly and by the end of the course you will have a body of completed work. Materials are not included.', Credits_attached = 0, Language_Level_of_Study_link = 'N/A', Start_date = datetime.datetime(2018, 9, 24), End_date = datetime.datetime(2018, 11, 26))

    def test_all_course_titles(self):
        titles = ShortCourse.all_course_titles()
        titles_list = [row.Title for row in titles]
        self.assertEqual(titles_list, ['Ancient Egypt and the Bible', 'Botanical painting and illustration'])

    def test_all_subjects(self):
        subjects = ShortCourse.all_subjects()
        subjects_list = [row.get('Subject_area') for row in titles]
        self.asserEqual(subjects_list, ['Archaeology Classical Studies and Egyptology', 'Art and Art History'])

    def test_specific_subject_courses(self):
        subject_courses = ShortCourse.specific_subject_courses('Archaeology Classical Studies and Egyptology')
        subject_courses_list = [row.Title for row in data]
        self.assertEqual(subject_courses_list, ['Ancient Egypt and the Bible'])

    def test_find_with_filters(self):
        result = ShortCourse.find_with_filters('Class_code', {'Tutor':'Judit Blair'})
        self.assertEqual(result.get('Class_code'), 9248)
    
