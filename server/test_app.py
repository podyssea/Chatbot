from utils import db
from utils import intent_handler
import unittest


class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.database = db.Database()
        cls.database.connect()
        cls.test_subject = 'Law'
        cls.test_subject_courses = ['You the jury: the criminal trial',
                                    'Law, Legal Systems and Legal Methods: An Introduction']

    def test_db_connect(self):
        self.assertTrue(self.database.get_connection().is_connected())

    def test_db_all_course_titles(self):
        data = self.database.all_course_titles()
        self.assertNotEqual(len(data), 0)
        self.assertEqual(type(data), list)
        self.assertEqual(type(data[0]), tuple)
        self.assertEqual(type(data[0][0]), str)

    def test_db_all_subjects(self):
        data = self.database.all_subjects()
        self.assertNotEqual(len(data), 0)
        self.assertEqual(type(data), list)
        self.assertEqual(type(data[0]), tuple)
        self.assertEqual(type(data[0][0]), str)

    def test_db_specific_subject_courses(self):
        data = self.database.specific_subject_courses(self.test_subject)
        self.assertNotEqual(len(data), 0)
        self.assertEqual(type(data), list)
        self.assertEqual(type(data[0]), tuple)
        self.assertEqual(type(data[0][0]), str)
        for i, record in enumerate(data):
            self.assertEqual(record[0], self.test_subject_courses[i])

    # imperative to run this last as we don't want the database to be disconnected when running other tests on it
    # begins with a z because unittest sorts alphabetically, and we want this to run last
    def test_z_db_disconnect(self):
        self.database.disconnect()
        self.assertFalse(self.database.disconnect())


if __name__ == '__main__':
    unittest.main()


