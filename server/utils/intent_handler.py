# this file finna handle intents
from server.utils import db

# TODO: figure out how a proper database connection is maintained cause this surely ain't it lol
database = db.Database()
database.connect()


def tear_down():
    global database
    database.disconnect()


def handle(data):
    # this is the entry point. will call the methods below and return their data
    if data == 'Available Courses':
        return all_course_titles()


# go into the database and get a list of all available courses
def all_course_titles():
    data = database.all_course_titles()

    resp = "All courses that are available to take are as follows: \n\n"

    return resp + ", ".join([row[0] for row in data])
