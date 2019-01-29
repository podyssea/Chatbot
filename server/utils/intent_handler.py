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
        return all_course_titles() #works
    elif data['intent'] == 'Subject Areas':
        return all_subjects() #works
    elif data['intent'] == 'Subject area -> Title':
        return specific_subject_courses(data["parameters"]["Subject_area"]) #works
    #----------------------------------------------------
    elif data['intent'] == 'Title -> Class Code':
        return title_give_classcode(data["parameters"]["Course"][0]) #works
    elif data['intent'] == 'Title -> Cost':
        return title_give_cost(data["parameters"]["Course"][0]) #works
    elif data['intent'] == 'Title -> Credits':
        return title_give_credits(data["parameters"]["Course"]) #works
    elif data['intent'] == 'Title -> Description':
        return title_give_description(data["parameters"]["Course"][0]) #works
    elif data['intent'] == 'Title -> Duration':
        return title_give_duration(data["parameters"]["Course"][0]) #works
    elif data['intent'] == 'Title -> End Date':
        return title_give_end(data["parameters"]["Course"][0]) #works
    elif data['intent'] == 'Title -> Start Date':
        return title_give_start(data["parameters"]["Course"][0]) #works
    elif data['intent'] == 'Title -> Subject Area':
        return title_give_subarea(data["parameters"]["Course"]) #works
    elif data['intent'] == 'Title -> Tutor':
        return title_give_tutor(data["parameters"]["Course"][0]) #works
    elif data['intent'] == 'Title -> Venue':
        return title_give_venue() #works
    #-------------------------------------------------
    elif data['intent'] == 'ID -> Title':
        return id_give_title(data["parameters"]["number"][0])
    elif data['intent'] == 'ID -> Cost':
        return id_give_cost(data["parameters"]["number"]) #works
    elif data['intent'] == 'ID -> Credits':
        return id_give_credits(data["parameters"]["number"][0]) #works
    elif data['intent'] == 'ID -> Description':
        return id_give_description(data["parameters"]["number"][0]) #works
    elif data['intent'] == 'ID -> Duration':
        return id_give_duration(data["parameters"]["number"][0]) #works
    elif data['intent'] == 'ID -> End Date':
        return id_give_end(data["parameters"]["number"][0]) #works
    elif data['intent'] == 'ID -> Start Date':
        return id_give_start(data["parameters"]["number"][0]) #works
    elif data['intent'] == 'ID -> Subject Area': 
        return id_give_subarea(data["parameters"]["number"][0]) #works
    elif data['intent'] == 'ID -> Tutor':
        return id_give_tutor(data["parameters"]["number"][0]) #works
    elif data['intent'] == 'ID -> Venue':
        return id_give_venue() #works
    #--------------------------------------------------
    elif data['intent'] == 'Cost -> Title':
        return cost_give_title(data['parameters']['unit-currency'][0]['amount']) #work
    elif data['intent'] == 'Credits -> Title':
        return credits_give_title(data['parameters']['Credits'][0]) #works
    elif data['intent'] == 'Duration -> Title':
        return duration_give_title(data['parameters']['duration'][0]['amount']) #works
    elif data['intent'] == 'End date -> Title':
        return end_give_title(data['parameters']['date'][0]) #NOT wokring
    elif data['intent'] == 'Start date -> Title':
        return start_give_title(data['parameters']['date'][0]) #NOT working
    elif data['intent'] == 'Subject area -> Title':
        return subarea_give_title(data['parameters']['Subject_area']) #NOT working
    elif data['intent'] == 'Tutor -> Title':
        return tutor_give_title(data['parameters']['given-name']) #NOT working
    elif data['intent'] == 'Venue -> Title':
        return venue_give_title() #working

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

    return resp + ", ".join(row[0] for row in data)


def specific_subject_courses(subject):
    data = database.specific_subject_courses(subject)

    resp = "All subjects that belong to {} are as follows: \n\n".format(subject)
    return resp + ", ".join(row[0] for row in data)

#-----------------------TITLE-------------------------------------------------

def title_give_cost(title):
    data = database.title_give_cost(title)

    resp = "The cost of this course is "
    return resp + str(data[0])

def title_give_classcode(title):
    data = database.title_give_classcode(title)

    resp = "The class code of this course is "
    return resp + str(data[0])

def title_give_credits(title):
    data = database.title_give_credits(title)

    resp = "The credits attached for this course is "
    return resp + str(data[0])

def title_give_description(title):
    data = database.title_give_description(title)

    resp = "To explain this course better.. "
    return resp + str(data[0])

def title_give_duration(title):
    data = database.title_give_duration(title)

    resp = "This course goes on for "
    return resp + str(data[0]) + " days"

def title_give_end(title):
    data = database.title_give_end(title)

    resp = "The end date of this course is "
    return resp + str(data[0])

def title_give_start(title):
    data = database.title_give_start(title)

    resp = "This course starts on "
    return resp + str(data[0])

def title_give_subarea(title):
    data = database.title_give_subarea(title)

    resp = "This course falls under the "
    return resp + str(data[0]) + "Subject Area"

def title_give_tutor(title):
    data = database.title_give_tutor(title)

    resp = "The tutor of this course is "
    return resp + str(data[0])

def title_give_venue(title):
    data = database.title_give_venue(title)

    resp = "The venue for this course is yet to be announced"
    return resp

#-----------------------ID--------------------------------------

def id_give_cost(id):
    data = database.id_give_cost(id)

    resp = "The cost of this course is "
    return resp + str(data[0])

def id_give_title(id):
    data = database.id_give_title(id)

    resp = "The Title of this course is "
    return resp + str(data[0])

def id_give_credits(id):
    data = database.id_give_credits(id)

    resp = "The credits attached for this course is "
    return resp + str(data[0])

def id_give_description(id):
    data = database.id_give_description(id)

    resp = "To explain this course better.. "
    return resp + str(data[0])

def id_give_duration(id):
    data = database.id_give_duration(id)

    resp = "This course goes on for "
    return resp + str(data[0]) + " days"

def id_give_end(id):
    data = database.id_give_end(id)

    resp = "The end date of this course is "
    return resp + str(data[0])

def id_give_start(id):
    data = database.id_give_start(id)

    resp = "This course starts on "
    return resp + str(data[0])

def id_give_subarea(id):
    data = database.id_give_subarea(id)

    resp = "This course falls under the "
    return resp + str(data[0]) + "Subject Area"

def id_give_tutor(id):
    data = database.id_give_tutor(id)

    resp = "The tutor of this course is "
    return resp + str(data[0])

def id_give_venue(id):
    data = database.id_give_cost(id)

    resp = "The venue for this course is yet to be announced"
    return resp

#--------------------------OTHER--------------------------------

def cost_give_title(cost):
    data = database.cost_give_title(cost)

    resp = "The Title of this course(s) is "
    return resp + str(data[0])

def credits_give_title(credits):
    data = database.credits_give_title(credits)

    resp = "The Title of this course(s) is "
    return resp + str(data[0])

def duration_give_title(duration):
    data = database.duration_give_title(duration)

    resp = "The Title of this course(s) is "
    return resp + str(data[0])

def end_give_title(end):
    data = database.end_give_title(end)

    resp = "The Title of this course is "
    return resp + str(data[0])

def start_give_title(start):
    data = database.start_give_title(start)

    resp = "The Title of this course is "
    return resp + str(data[0])

def subarea_give_title(subarea):
    data = database.subarea_give_title(subarea)

    resp = "The Title of this course is "
    return resp + str(data[0])

def tutor_give_title(tutor):
    data = database.tutor_give_title(tutor)

    resp = "The Title of this course is "
    return resp + str(data[0])

def venue_give_title(venue):
    data = database.venue_give_title(venue)

    resp = "The Title of this course is "
    return resp + str(data[0])