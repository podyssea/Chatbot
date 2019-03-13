from .models import ShortCourse
from dateutil.relativedelta import *
import datetime


def handle(data):
    if data['intent'] == 'Available Courses':
        return all_course_titles()
    elif data['intent'] == 'Subject Areas':
        return all_subjects()
    elif data['intent'] == 'Subject area -> Title':
        return specific_subject_courses(data['parameters']['Subject_area'])
    elif data['intent'] == 'FindTitle':
        return find_title(data['parameters'])
    elif data['intent'] == 'FindClassCode':
        return find_id(data['parameters'])
    elif data['intent'] == 'FindCost':
        return find_cost(data['parameters'])
    elif data['intent'] == 'FindCredits':
        return find_credits(data['parameters'])
    elif data['intent'] == 'FindDescription':
        return find_description(data['parameters'])
    elif data['intent'] == 'FindDuration':
        return find_duration(data['parameters'])
    elif data['intent'] == 'FindEndDate':
        return find_end_date(data['parameters'])
    elif data['intent'] == 'FindLecturer':
        return find_lecturer(data['parameters'])
    elif data['intent'] == 'FindStartDate':
        return find_start_date(data['parameters'])
    elif data['intent'] == 'FindSubjectArea':
        return find_subject_area(data['parameters'])
    elif data['intent'] == 'FindVenue':
        return find_venue(data['parameters'])


def all_course_titles():
    data = ShortCourse.all_course_titles()
    resp = 'All courses that are available to take are as follows: '
    return '{}{}'.format(resp, ', '.join([row.Title for row in data]))


def all_subjects():
    data = ShortCourse.all_subjects()
    resp = 'All subjects that are available are as follows: '
    return '{}{}'.format(resp, ', '.join([row.get('Subject_area') for row in data]))


def specific_subject_courses(subject):
    data = ShortCourse.specific_subject_courses(subject)
    resp = 'All courses that belong to {} are as follows: '.format(subject)
    return '{}{}'.format(resp, ', '.join([row.Title for row in data]))


# ------------------------------------------Many to One questions ------------------------------------
# ----------------------------------------------------------------------------------------------------

def find_title(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY'}
    # figure out if number is ID or credits
    if isinstance(parameters['number'], (list,)):
        parameters['number'] = parameters['number'][0]
    if parameters['Credits'] and parameters['Class_code']:
        if parameters['number'] > parameters['number1']:
            dialog_to_db['number'] = 'Class_code'
            dialog_to_db['number1'] = 'Credits_attached'
        else:
            dialog_to_db['number'] = 'Credits_attached'
            dialog_to_db['number1'] = 'Class_code'
    elif parameters['Credits']:
        dialog_to_db['number'] = 'Credits_attached'
    elif parameters['Class_code']:
        dialog_to_db['number'] = 'Class_code'
    # figure out which date is start and/or end
    if isinstance(parameters['date'], (list,)):
        parameters['date'] = parameters['date'][0]
    if parameters['date'] and parameters['date1']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        date1 = datetime.datetime.strptime(parameters['date1'][0:10], '%Y-%m-%d')
        date1 = date1 + relativedelta(years=-1)
        parameters['date1'] = date1
        if date > date1:
            dialog_to_db['date'] = 'End_date'
            dialog_to_db['date1'] = 'Start_date'
        elif date < date1:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
        else:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_start']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_end']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'End_date'
    elif parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters['Start_date'])
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Cost':
            given_parameters[k] = v['amount']
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Title', given_parameters)
    resp = 'The title of a course matching that description is '
    return "{}{}".format(resp, title.get('Title'))


# ------------           ----------               -----------------            ----------

def find_id(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'number': 'Credits_attached', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY',
                    'Description': 'UNNECESSARY'}

    # figure out which date is start and/or end
    if isinstance(parameters['date'], (list,)):
        parameters['date'] = parameters['date'][0]
    if parameters['date'] and parameters['date1']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        date1 = datetime.datetime.strptime(parameters['date1'][0:10], '%Y-%m-%d')
        date1 = date1 + relativedelta(years=-1)
        parameters['date1'] = date1
        if date > date1:
            dialog_to_db['date'] = 'End_date'
            dialog_to_db['date1'] = 'Start_date'
        elif date < date1:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
        else:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_start']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_end']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'End_date'
    elif parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters)
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Cost':
            given_parameters[k] = v['amount']
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Class_code', given_parameters)
    resp = 'The id of a course matching that description is '
    return "{}{}".format(resp, title.get('Class_code'))


# ------------           ----------               -----------------            ----------

def find_cost(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY'}
    # figure out if number is ID or credits
    if isinstance(parameters['number'], (list,)):
        parameters['number'] = parameters['number'][0]
    if parameters['Credits'] and parameters['Class_code']:
        if parameters['number'] > parameters['number1']:
            dialog_to_db['number'] = 'Class_code'
            dialog_to_db['number1'] = 'Credits_attached'
        else:
            dialog_to_db['number'] = 'Credits_attached'
            dialog_to_db['number1'] = 'Class_code'
    elif parameters['Credits']:
        dialog_to_db['number'] = 'Credits_attached'
    elif parameters['Class_code']:
        dialog_to_db['number'] = 'Class_code'
    # figure out which date is start and/or end
    if isinstance(parameters['date'], (list,)):
        parameters['date'] = parameters['date'][0]
    if parameters['date'] and parameters['date1']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        date1 = datetime.datetime.strptime(parameters['date1'][0:10], '%Y-%m-%d')
        date1 = date1 + relativedelta(years=-1)
        parameters['date1'] = date1
        if date > date1:
            dialog_to_db['date'] = 'End_date'
            dialog_to_db['date1'] = 'Start_date'
        elif date < date1:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
        else:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_start']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_end']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'End_date'
    elif parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters)
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Cost', given_parameters)
    resp = 'This course costs '
    pounds = ' pounds'
    return "{}{}{}".format(resp, title.get('Cost'), pounds)


# ------------           ----------               -----------------            ----------

def find_credits(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'Class_code', 'Credits1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY'}

    # figure out which date is start and/or end
    if isinstance(parameters['date'], (list,)):
        parameters['date'] = parameters['date'][0]
    if parameters['date'] and parameters['date1']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        date1 = datetime.datetime.strptime(parameters['date1'][0:10], '%Y-%m-%d')
        date1 = date1 + relativedelta(years=-1)
        parameters['date1'] = date1
        if date > date1:
            dialog_to_db['date'] = 'End_date'
            dialog_to_db['date1'] = 'Start_date'
        elif date < date1:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
        else:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_start']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_end']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'End_date'
    elif parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters)
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Cost':
            given_parameters[k] = v['amount']
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Credits_attached', given_parameters)
    resp = 'The number of credits given by that course is '
    return "{}{}".format(resp, title.get('Credits_attached'))


# ------------           ----------               -----------------            ----------

def find_description(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY',
                    'desription': 'Description'}
    # figure out if number is ID or credits
    if isinstance(parameters['number'], (list,)):
        parameters['number'] = parameters['number'][0]
    if parameters['Credits'] and parameters['Class_code']:
        if parameters['number'] > parameters['number1']:
            dialog_to_db['number'] = 'Class_code'
            dialog_to_db['number1'] = 'Credits_attached'
        else:
            dialog_to_db['number'] = 'Credits_attached'
            dialog_to_db['number1'] = 'Class_code'
    elif parameters['Credits']:
        dialog_to_db['number'] = 'Credits_attached'
    elif parameters['Class_code']:
        dialog_to_db['number'] = 'Class_code'
    # figure out which date is start and/or end
    if isinstance(parameters['date'], (list,)):
        parameters['date'] = parameters['date'][0]
    if parameters['date'] and parameters['date1']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        date1 = datetime.datetime.strptime(parameters['date1'][0:10], '%Y-%m-%d')
        date1 = date1 + relativedelta(years=-1)
        parameters['date1'] = date1
        if date > date1:
            dialog_to_db['date'] = 'End_date'
            dialog_to_db['date1'] = 'Start_date'
        elif date < date1:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
        else:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_start']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_end']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'End_date'
    elif parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters)
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Description', given_parameters)
    resp = 'The description of a course matching those parameters is '
    return "{}{}".format(resp, title.get('Description'))


# ------------           ----------               -----------------            ----------

def find_duration(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY',
                    'desription': 'Description'}
    # figure out if number is ID or credits
    if isinstance(parameters['number'], (list,)):
        parameters['number'] = parameters['number'][0]
    if parameters['Credits'] and parameters['Class_code']:
        if parameters['number'] > parameters['number1']:
            dialog_to_db['number'] = 'Class_code'
            dialog_to_db['number1'] = 'Credits_attached'
        else:
            dialog_to_db['number'] = 'Credits_attached'
            dialog_to_db['number1'] = 'Class_code'
    elif parameters['Credits']:
        dialog_to_db['number'] = 'Credits_attached'
    elif parameters['Class_code']:
        dialog_to_db['number'] = 'Class_code'
    # figure out which date is start and/or end
    if isinstance(parameters['date'], (list,)):
        parameters['date'] = parameters['date'][0]
    if parameters['date'] and parameters['date1']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        date1 = datetime.datetime.strptime(parameters['date1'][0:10], '%Y-%m-%d')
        date1 = date1 + relativedelta(years=-1)
        parameters['date1'] = date1
        if date > date1:
            dialog_to_db['date'] = 'End_date'
            dialog_to_db['date1'] = 'Start_date'
        elif date < date1:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
        else:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_start']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_end']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'End_date'
    elif parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters)
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
    title = ShortCourse.find_with_filters('Duration', given_parameters)
    resp = 'The duration of a course matching that description is '
    return "{}{}".format(resp, title.get('Duration'))


# ------------           ----------               -----------------            ----------

def find_end_date(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'Start_date', 'desription': 'Description'}
    # figure out if number is ID or credits
    if parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
    if isinstance(parameters['number'], (list,)):
        parameters['number'] = parameters['number'][0]
    if parameters['Credits'] and parameters['Class_code']:
        if parameters['number'] > parameters['number1']:
            dialog_to_db['number'] = 'Class_code'
            dialog_to_db['number1'] = 'Credits_attached'
        else:
            dialog_to_db['number'] = 'Credits_attached'
            dialog_to_db['number1'] = 'Class_code'
    elif parameters['Credits']:
        dialog_to_db['number'] = 'Credits_attached'
    elif parameters['Class_code']:
        dialog_to_db['number'] = 'Class_code'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters)
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('End_date', given_parameters)
    resp = 'The title of a course matching that description is '
    time = ' at '
    return "{}{}{}{}".format(resp, title.get('End_date'), time, title.get('End_time'))


# ------------           ----------               -----------------            ----------

def find_start_date(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'End_date', 'desription': 'Description'}
    # figure out if number is ID or credits
    if parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
    if isinstance(parameters['number'], (list,)):
        parameters['number'] = parameters['number'][0]
    if parameters['Credits'] and parameters['Class_code']:
        if parameters['number'] > parameters['number1']:
            dialog_to_db['number'] = 'Class_code'
            dialog_to_db['number1'] = 'Credits_attached'
        else:
            dialog_to_db['number'] = 'Credits_attached'
            dialog_to_db['number1'] = 'Class_code'
    elif parameters['Credits']:
        dialog_to_db['number'] = 'Credits_attached'
    elif parameters['Class_code']:
        dialog_to_db['number'] = 'Class_code'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters)
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Start_date', given_parameters)
    resp = 'The title of a course matching that description is '
    time = ' at '
    return "{}{}{}{}".format(resp, title.get('Start_date'), time, title.get('End_time'))


# ------------           ----------               -----------------            ----------

def find_lecturer(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY',
                    'desription': 'Description'}
    # figure out if number is ID or credits
    if isinstance(parameters['number'], (list,)):
        parameters['number'] = parameters['number'][0]
    if parameters['Credits'] and parameters['Class_code']:
        if parameters['number'] > parameters['number1']:
            dialog_to_db['number'] = 'Class_code'
            dialog_to_db['number1'] = 'Credits_attached'
        else:
            dialog_to_db['number'] = 'Credits_attached'
            dialog_to_db['number1'] = 'Class_code'
    elif parameters['Credits']:
        dialog_to_db['number'] = 'Credits_attached'
    elif parameters['Class_code']:
        dialog_to_db['number'] = 'Class_code'
    # figure out which date is start and/or end
    if isinstance(parameters['date'], (list,)):
        parameters['date'] = parameters['date'][0]
    if parameters['date'] and parameters['date1']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        date1 = datetime.datetime.strptime(parameters['date1'][0:10], '%Y-%m-%d')
        date1 = date1 + relativedelta(years=-1)
        parameters['date1'] = date1
        if date > date1:
            dialog_to_db['date'] = 'End_date'
            dialog_to_db['date1'] = 'Start_date'
        elif date < date1:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
        else:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_start']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_end']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'End_date'
    elif parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters)
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Tutor', given_parameters)
    resp = 'The lecturer of a course matching that description is '
    return "{}{}".format(resp, title.get('Tutor'))


# ------------           ----------               -----------------            ----------        

def find_subject_area(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'location': 'Venue', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY', 'desription': 'Description'}
    # figure out if number is ID or credits
    if isinstance(parameters['number'], (list,)):
        parameters['number'] = parameters['number'][0]
    if parameters['Credits'] and parameters['Class_code']:
        if parameters['number'] > parameters['number1']:
            dialog_to_db['number'] = 'Class_code'
            dialog_to_db['number1'] = 'Credits_attached'
        else:
            dialog_to_db['number'] = 'Credits_attached'
            dialog_to_db['number1'] = 'Class_code'
    elif parameters['Credits']:
        dialog_to_db['number'] = 'Credits_attached'
    elif parameters['Class_code']:
        dialog_to_db['number'] = 'Class_code'
    # figure out which date is start and/or end
    if isinstance(parameters['date'], (list,)):
        parameters['date'] = parameters['date'][0]
    if parameters['date'] and parameters['date1']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        date1 = datetime.datetime.strptime(parameters['date1'][0:10], '%Y-%m-%d')
        date1 = date1 + relativedelta(years=-1)
        parameters['date1'] = date1
        if date > date1:
            dialog_to_db['date'] = 'End_date'
            dialog_to_db['date1'] = 'Start_date'
        elif date < date1:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
        else:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_start']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_end']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'End_date'
    elif parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters)
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Subject_area', given_parameters)
    resp = 'The subject area of a course matching that description is '
    return "{}{}".format(resp, title.get('Subject_area'))


# ------------           ----------               -----------------            ----------

def find_venue(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area': 'Subject_area', 'unit-currency': 'Cost', 'duration': 'Duration', 'Course': 'Title', 'Lecturer': 'Tutor', 'Keyword_Course': 'UNNECESSARY', 'Cost': 'UNNECESSARY', 'Credits': 'UNNECESSARY', 'Date_end': 'UNNECESSARY', 'Class_code': 'UNNECESSARY', 'Date_start': 'UNNECESSARY', 'Keyword_Subject_Area': 'UNNECESSARY', 'Keyword_Lecturer': 'UNNECESSARY', 'number': 'UNNECESSARY', 'number1': 'UNNECESSARY', 'date': 'UNNECESSARY', 'date1': 'UNNECESSARY',
                    'desription': 'Description'}
    # figure out if number is ID or credits
    if isinstance(parameters['number'], (list,)):
        parameters['number'] = parameters['number'][0]
    if parameters['Credits'] and parameters['Class_code']:
        if parameters['number'] > parameters['number1']:
            dialog_to_db['number'] = 'Class_code'
            dialog_to_db['number1'] = 'Credits_attached'
        else:
            dialog_to_db['number'] = 'Credits_attached'
            dialog_to_db['number1'] = 'Class_code'
    elif parameters['Credits']:
        dialog_to_db['number'] = 'Credits_attached'
    elif parameters['Class_code']:
        dialog_to_db['number'] = 'Class_code'
    # figure out which date is start and/or end
    if isinstance(parameters['date'], (list,)):
        parameters['date'] = parameters['date'][0]
    if parameters['date'] and parameters['date1']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        date1 = datetime.datetime.strptime(parameters['date1'][0:10], '%Y-%m-%d')
        date1 = date1 + relativedelta(years=-1)
        parameters['date1'] = date1
        if date > date1:
            dialog_to_db['date'] = 'End_date'
            dialog_to_db['date1'] = 'Start_date'
        elif date < date1:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
        else:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_start']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_end']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'End_date'
    elif parameters['date']:
        date = datetime.datetime.strptime(parameters['date'][0:10], '%Y-%m-%d')
        date = date + relativedelta(years=-1)
        parameters['date'] = date
        dialog_to_db['date'] = 'Start_date'

    given_parameters = {dialog_to_db[k]: v for k, v in parameters.items() if v != "" and v != [] and ".original" not in k}
    print(given_parameters)
    del given_parameters['UNNECESSARY']
    for k, v in given_parameters.items():
        if isinstance(v, (list,)):
            given_parameters[k] = v[0]
        if k == 'Duration':
            if v['unit'] == 'day':
                given_parameters[k] = v['amount']
            elif v['unit'] == 'week':
                given_parameters[k] = v['amount'] * 7
            elif v['unit'] == 'month':
                given_parameters[k] = v['amount'] * 30
    title = ShortCourse.find_with_filters('Venue', given_parameters)
    resp = 'The venue for a course matching that description is '
    return "{}{}".format(resp, title.get('Venue'))
