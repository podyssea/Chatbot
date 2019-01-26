# to connect to database and execute queries son
import mysql.connector
from mysql.connector import Error


class Database:
    username = 'chatbot'
    password = 'j2lpq7m9RIIns6muMlmw'
    database = 'Short_Courses_DB'
    host = 'chatbot-db-instance-1.cjxfnn0vqvp8.eu-west-1.rds.amazonaws.com'

    def __init__(self):
        self.connection = None
        self.cursor = None
        pass

    def get_connection(self):
        return self.connection

    def connect(self):
        # connects to database. returns true if connected, false if not, and a text describing what happened
        try:
            self.connection = mysql.connector.connect(host=self.host, database=self.database, user=self.username,
                                                      password=self.password, use_pure=True)
            if self.connection.is_connected():
                self.open_cursor()
                return True, 'Connected'
            return False, 'Failed to connect'
        except Error as e:
            return False, str(e)

    def open_cursor(self):
        self.cursor = self.connection.cursor(prepared=True)

    def close_cursor(self):
        self.cursor.close()

    def disconnect(self):
        # disconnect from the database, closing the cursor and then the connection
        if self.connection.is_connected():
            self.close_cursor()
            self.connection.close()
            return True
        return False

    def all_course_titles(self):
        query = """SELECT Title FROM Short_Courses"""
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def all_subjects(self):
        query = """SELECT DISTINCT Subject_area FROM Short_Courses"""
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def specific_subject_courses(self, subject):
        query = """SELECT Title from Short_Courses WHERE Subject_area = %s"""
        self.cursor.execute(query, (subject, ))
        records = self.cursor.fetchall()
        return records


