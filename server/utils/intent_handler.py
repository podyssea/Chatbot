# this file finna handle intents
from utils import db

# TODO: figure out how a proper database connection is maintained cause this surely ain't it lol
database = db.Database()
database.connect()


def tear_down():
    global database
    database.disconnect()


def handle(data):
    # this is the entry point. will call the methods below and return their data
    if data['intent'] == 'Available Courses':
        return all_course_titles()
    elif data['intent'] == 'Subject Areas':
        return all_subjects()
    elif data['intent'] == 'Subject area -> Title':
        return specific_subject_courses(data["parameters"]["Subject_area"])


# go into the database and get a list of all available courses
def all_course_titles():
    data = database.all_course_titles()

    resp = "All courses that are available to take are as follows: \n\n"

    return resp + ", ".join([row[0] for row in data])


def all_subjects():
    data = database.all_subjects()

    resp = "All subjects that are available are as follows: \n\n"
    for row in data:
        print(row[0])

    return resp + ", ".join([row[0] for row in data])


def specific_subject_courses(subject):
    data = database.specific_subject_courses(subject)

    resp = "All subjects that belong to {} are as follows: \n\n".format(subject)
    return resp + ", ".join([row[0] for row in data])

