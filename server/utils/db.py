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
        self.cursor.execute(query, (subject,))
        records = self.cursor.fetchall()
        return records

    # -----------------------------------TITLE------------------------------------

    def title_give_cost(self, title):
        query = """SELECT Cost from Short_Courses WHERE Title = %s"""
        self.cursor.execute(query, (title,))
        records = self.cursor.fetchone()
        return records

    def title_give_classcode(self, title):
        query = """SELECT Class_code from Short_Courses WHERE Title = %s"""
        self.cursor.execute(query, (title,))
        records = self.cursor.fetchone()
        return records

    def title_give_credits(self, title):
        query = """SELECT Credits_attached from Short_Courses WHERE Title = %s"""
        self.cursor.execute(query, (title,))
        records = self.cursor.fetchone()
        return records

    def title_give_description(self, title):
        query = """SELECT Description from Short_Courses WHERE Title = %s"""
        self.cursor.execute(query, (title,))
        records = self.cursor.fetchone()
        return records

    def title_give_duration(self, title):
        query = """SELECT Duration from Short_Courses WHERE Title = %s"""
        self.cursor.execute(query, (title,))
        records = self.cursor.fetchone()
        return records

    def title_give_end(self, title):
        query = """SELECT End_date from Short_Courses WHERE Title = %s"""
        self.cursor.execute(query, (title,))
        records = self.cursor.fetchone()
        return records

    def title_give_start(self, title):
        query = """SELECT Start_date from Short_Courses WHERE Title = %s"""
        self.cursor.execute(query, (title,))
        records = self.cursor.fetchone()
        return records

    def title_give_subarea(self, title):
        query = """SELECT Subject_area from Short_Courses WHERE Title = %s"""
        self.cursor.execute(query, (title,))
        records = self.cursor.fetchone()
        return records

    def title_give_tutor(self, title):
        query = """SELECT Tutor from Short_Courses WHERE Title = %s"""
        self.cursor.execute(query, (title,))
        records = self.cursor.fetchone()
        return records

    def title_give_venue(self, title):
        query = """SELECT Venue from Short_Courses WHERE Title = %s"""
        self.cursor.execute(query, (title,))
        records = self.cursor.fetchone()
        return records

    # -------------------------------ID-------------------------------------

    def id_give_cost(self, course_id):
        query = """SELECT Cost from Short_Courses WHERE Class_code = %s"""
        self.cursor.execute(query, (course_id,))
        records = self.cursor.fetchone()
        return records

    def id_give_credits(self, course_id):
        query = """SELECT Credits_attached from Short_Courses WHERE Class_code = %s"""
        self.cursor.execute(query, (course_id,))
        records = self.cursor.fetchone()
        return records

    def id_give_description(self, course_id):
        query = """SELECT Description from Short_Courses WHERE Class_code = %s"""
        self.cursor.execute(query, (course_id,))
        records = self.cursor.fetchone()
        return records

    def id_give_duration(self, course_id):
        query = """SELECT Duration from Short_Courses WHERE Class_code = %s"""
        self.cursor.execute(query, (course_id,))
        records = self.cursor.fetchone()
        return records

    def id_give_end(self, course_id):
        query = """SELECT End_date from Short_Courses WHERE Class_code = %s"""
        self.cursor.execute(query, (course_id,))
        records = self.cursor.fetchone()
        return records

    def id_give_start(self, course_id):
        query = """SELECT Start_date from Short_Courses WHERE Class_code = %s"""
        self.cursor.execute(query, (course_id,))
        records = self.cursor.fetchone()
        return records

    def id_give_subarea(self, course_id):
        query = """SELECT Subject_area from Short_Courses WHERE Class_code = %s"""
        self.cursor.execute(query, (course_id,))
        records = self.cursor.fetchone()
        return records

    def id_give_title(self, course_id):
        query = """SELECT Title from Short_Courses WHERE Class_code = %s"""
        self.cursor.execute(query, (course_id,))
        records = self.cursor.fetchone()
        return records

    def id_give_tutor(self, course_id):
        query = """SELECT Tutor from Short_Courses WHERE Class_code = %s"""
        self.cursor.execute(query, (course_id,))
        records = self.cursor.fetchone()
        return records

    def id_give_venue(self, course_id):
        query = """SELECT Venue from Short_Courses WHERE Class_code = %s"""
        self.cursor.execute(query, (course_id,))
        records = self.cursor.fetchone()
        return records

    # ------------------------------OTHER---------------------------

    def cost_give_title(self, cost):
        query = """SELECT Title from Short_Courses WHERE Cost = %s"""
        self.cursor.execute(query, (cost,))
        records = self.cursor.fetchall()
        return records

    def credits_give_title(self, course_credits):
        query = """SELECT Title from Short_Courses WHERE Credits_attached = %s"""
        self.cursor.execute(query, (course_credits,))
        records = self.cursor.fetchone()
        return records

    def duration_give_title(self, duration):
        query = """SELECT Title from Short_Courses WHERE Duration = %s"""
        self.cursor.execute(query, (duration,))
        records = self.cursor.fetchone()
        return records

    def end_give_title(self, end):
        query = """SELECT Title from Short_Courses WHERE End_date = %s"""
        self.cursor.execute(query, (end,))
        records = self.cursor.fetchone()
        return records

    def start_give_title(self, start):
        query = """SELECT Title from Short_Courses WHERE Start_date = %s"""
        self.cursor.execute(query, (start,))
        records = self.cursor.fetchone()
        return records

    def subarea_give_title(self, subarea):
        query = """SELECT Title from Short_Courses WHERE Subject_area = %s"""
        self.cursor.execute(query, (subarea,))
        records = self.cursor.fetchone()
        return records

    def tutor_give_title(self, tutor):
        query = """SELECT Title from Short_Courses WHERE Tutor = %s"""
        self.cursor.execute(query, (tutor,))
        records = self.cursor.fetchone()
        return records

    def venue_give_title(self, venue):
        query = """SELECT Title from Short_Courses WHERE Venue = %s"""
        self.cursor.execute(query, (venue,))
        records = self.cursor.fetchone()
        return records
