from .models import ShortCourse


def handle(data):
    if data['intent'] == 'Available Courses':
        return all_course_titles()
    elif data['intent'] == 'Subject Areas':
        return all_subjects()
    elif data['intent'] == 'Subject area -> Title':
        return specific_subject_courses(data['parameters']['Subject_area'])
    elif data['intent'] == 'FindTitle':
        return find_title(data['parameters'])
        # ----------------------------------------------------
#    elif data['intent'] == 'Title -> Class Code':
#        return title_give_classcode(data['parameters']['Course'][0])
#    elif data['intent'] == 'Title -> Cost':
#        return title_give_cost(data['parameters']['Course'][0])
#    elif data['intent'] == 'Title -> Credits':
#        return title_give_credits(data['parameters']['Course'][0])
#    elif data['intent'] == 'Title -> Description':
#        return title_give_description(data['parameters']['Course'][0])
#    elif data['intent'] == 'Title -> Duration':
#        return title_give_duration(data['parameters']['Course'][0])
#    elif data['intent'] == 'Title -> End Date':
#        return title_give_end(data['parameters']['Course'][0])
#    elif data['intent'] == 'Title -> Start Date':
#        return title_give_start(data['parameters']['Course'][0])
#    elif data['intent'] == 'Title -> Subject Area':
#        return title_give_subarea(data['parameters']['Course'][0])
#    elif data['intent'] == 'Title -> Tutor':
#        return title_give_tutor(data['parameters']['Course'][0])
#    elif data['intent'] == 'Title -> Venue':
#        return title_give_venue(data['parameters']['Course'][0])
        # -------------------------------------------------
#    elif data['intent'] == 'ID -> Title':
#        return id_give_title(data['parameters']['number'][0])
#    elif data['intent'] == 'ID -> Cost':
#        return id_give_cost(data['parameters']['number'])
#    elif data['intent'] == 'ID -> Credits':
#        return id_give_credits(data['parameters']['number'][0])
#    elif data['intent'] == 'ID -> Description':
#        return id_give_description(data['parameters']['number'][0])
#    elif data['intent'] == 'ID -> Duration':
 #       return id_give_duration(data['parameters']['number'][0])
 #   elif data['intent'] == 'ID -> End Date':
 #       return id_give_end(data['parameters']['number'][0])
 #   elif data['intent'] == 'ID -> Start Date':
 #       return id_give_start(data['parameters']['number'][0])
 #   elif data['intent'] == 'ID -> Subject Area':
#        return id_give_subarea(data['parameters']['number'][0])
#    elif data['intent'] == 'ID -> Tutor':
#        return id_give_tutor(data['parameters']['number'][0])
#    elif data['intent'] == 'ID -> Venue':
#        return id_give_venue(data['parameters']['number'][0])
        # --------------------------------------------------
#    elif data['intent'] == 'Cost -> Title':
#        return cost_give_title(data['parameters']['unit-currency'][0]['amount'])
#    elif data['intent'] == 'Credits -> Title':
#        return credits_give_title(data['parameters']['Credits'][0])
#    elif data['intent'] == 'Duration -> Title':
#        return duration_give_title(data['parameters']['duration'][0]['amount'])
#    elif data['intent'] == 'End date -> Title':
#        return end_give_title(data['parameters']['date'][0])  # TODO: fix these to be proper datetime fields
#    elif data['intent'] == 'Start date -> Title':
#        return start_give_title(data['parameters']['date'][0])  # TODO: same as above. proper datetime!!!!
#    elif data['intent'] == 'Subject area -> Title':
#        return subarea_give_title(data['parameters']['Subject_area'])
#    elif data['intent'] == 'Tutor -> Title':
#        return tutor_give_title(data['parameters']['given-name'])
 #   elif data['intent'] == 'Venue -> Title':
 #       return venue_give_title(data['parameters']['location'][0].get('subadmin-area'))


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


def find_title(parameters):
    # turn the dialogflow parameter names into database column names
    dialog_to_db = {'Subject_area':'Subject_area', 'unit-currency':'Cost', 'duration':'Duration', 'Lecturer':'Tutor','location':'Venue'}
    # figure out if number is ID or credits
    if len(parameters['number'])!=0 and parameters['number1']:
        if parameters['number'] > parameters['number1']:
            dialog_to_db['number'] = 'Class_code'
            dialog_to_db['number1'] = 'Credits_attached'
    elif parameters['Credits']:
        dialog_to_db['number'] = 'Credits_attached'
    elif parameters['Class_code']:
        dialog_to_db['number'] = 'Class_code'
    # figure out which date is start and/or end
    if len(parameters['date'])!=0 and parameters['date1']:
        date = [parameters['date'][0][5:6], parameters['date'][0][8:9]]
        date1 = [parameters['date1'][5:6], parameters['date1'][8:9]]
        if date[0] > date1[0] or (date[0]==date1[0] and date[1] > date1[1]):
            dialog_to_db['date'] = 'End_date'
            dialog_to_db['date1'] = 'Start_date'
        elif date[0] < date1[0] or (date[0]==date1[0] and date[1] < date1[1]):
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
        else:
            dialog_to_db['date1'] = 'End_date'
            dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_start']:
        dialog_to_db['date'] = 'Start_date'
    elif parameters['Date_end']:
        dialog_to_db['date'] = 'End_date'
    else:
        dialog_to_db['date'] = 'Start_date'
 
    given_parameters = {dialog_to_db[k]: v for k, v in metadata.items() if v is not None}
    title = ShortCourse.find_with_filters('Title', given_parameters)
    resp = 'The title of a course matching that description is '
    return "{}{}".format(resp, title.get('Title'))

# -----------------------TITLE-------------------------------------------------


def title_give_cost(title):
    data = ShortCourse.title_give_cost(title)
    resp = 'The cost of this course is '
    return "{}{}".format(resp, data.get('Cost'))


def title_give_classcode(title):
    data = ShortCourse.title_give_classcode(title)
    resp = 'The class code of this course is '
    return '{}{}'.format(resp, data.get('Class_code'))


def title_give_credits(title):
    data = ShortCourse.title_give_credits(title)
    resp = 'The credits attached for this course is '
    return '{}{}'.format(resp, data.get('Credits_attached'))


def title_give_description(title):
    data = ShortCourse.title_give_description(title)
    resp = 'To explain this course better.. '
    return '{}{}'.format(resp, data.get('Description'))


def title_give_duration(title):
    data = ShortCourse.title_give_duration(title)
    resp = 'This course goes on for '
    return '{}{} days'.format(resp, data.get('Duration'))


def title_give_end(title):
    data = ShortCourse.title_give_end(title)
    resp = 'The end date of this course is '
    return '{}{}'.format(resp, data.get('End_date'))


def title_give_start(title):
    data = ShortCourse.title_give_start(title)
    resp = 'This course starts on '
    return '{}{}'.format(resp, data.get('Start_date'))


def title_give_subarea(title):
    data = ShortCourse.title_give_subarea(title)
    resp = 'The subject area for this course is '
    return '{}{}'.format(resp, data.get('Subject_area'))


def title_give_tutor(title):
    data = ShortCourse.title_give_tutor(title)
    resp = 'The tutor of this course is '
    return '{}{}'.format(resp, data.get('Tutor'))


def title_give_venue(title):
    data = ShortCourse.title_give_venue(title)
    return '{}'.format(data.get('Venue'))


# -----------------------ID--------------------------------------

def id_give_cost(class_code):
    data = ShortCourse.id_give_cost(class_code)
    resp = 'The cost of this course is '
    return '{}{}'.format(resp, data.get('Cost'))


def id_give_title(class_code):
    data = ShortCourse.id_give_title(class_code)
    resp = 'The Title of this course is '
    return '{}{}'.format(resp, data.get('Title'))


def id_give_credits(class_code):
    data = ShortCourse.id_give_credits(class_code)
    resp = 'The credits attached for this course is '
    return '{}{}'.format(resp, data.get('Credits_attached'))


def id_give_description(class_code):
    data = ShortCourse.id_give_description(class_code)
    resp = 'To explain this course better.. '
    return '{}{}'.format(resp, data.get('Description'))


def id_give_duration(class_code):
    data = ShortCourse.id_give_duration(class_code).get('Duration')
    resp = 'This course goes on for '
    return '{}{} {}'.format(resp, data, 'day' if data == 1 else 'days')  # todo: day(s) depending on duration


def id_give_end(class_code):  # todo: see if these incorporate both date and time, think they should
    data = ShortCourse.id_give_end(class_code)
    resp = 'The end date of this course is '
    return '{}{}'.format(resp, data.get('End_date'))


def id_give_start(class_code):  # todo: read todo for id_give_end above, applies here as well
    data = ShortCourse.id_give_start(class_code)
    resp = 'This course starts on '
    return '{}{}'.format(resp, data.get('Start_date'))


def id_give_subarea(class_code):
    data = ShortCourse.id_give_subarea(class_code)
    resp = 'The subject area of this course is '
    return '{}{}'.format(resp, data.get('Subject_area'))


def id_give_tutor(class_code):
    data = ShortCourse.id_give_tutor(class_code)
    resp = 'The tutor of this course is '
    return '{}{}'.format(resp, data.get('Tutor'))


def id_give_venue(class_code):
    data = ShortCourse.id_give_venue(class_code)
    return '{}'.format(data.get('Venue'))


# --------------------------OTHER--------------------------------

def cost_give_title(cost):
    data = ShortCourse.cost_give_title(cost)
    resp = 'The Title of this course(s) is '
    return '{}{}'.format(resp, data.get('Title'))


def credits_give_title(credits_attached):
    data = ShortCourse.credits_give_title(credits_attached)
    resp = 'The Title of this course(s) is '
    return '{}{}'.format(resp, data.get('Title'))


def duration_give_title(duration):
    data = ShortCourse.duration_give_title(duration)
    resp = 'The Title of this course(s) is '
    return '{}{}'.format(resp, data.get('Title'))


def end_give_title(end):
    data = ShortCourse.end_give_title(end)
    resp = 'The Title of this course is '
    return '{}{}'.format(resp, data.get('Title'))


def start_give_title(start):
    data = ShortCourse.start_give_title(start)
    resp = 'The Title of this course is '
    return '{}{}'.format(resp, data.get('Title'))


def subarea_give_title(subarea):
    data = ShortCourse.subarea_give_title(subarea)
    resp = 'The Title of this course is '
    return '{}{}'.format(resp, data.get('Title'))


def tutor_give_title(tutor):
    data = ShortCourse.tutor_give_title(tutor)
    if data is None:
        return 'This tutor does not lead any course.'
    resp = 'The Title of this course is '
    return '{}{}'.format(resp, data.get('Title'))


def venue_give_title(venue):
    data = ShortCourse.venue_give_title(venue)
    if data is None:
        return 'There are no courses held in this venue.'
    resp = 'The Title of this course is '
    return '{}{}'.format(resp, data.get('Title'))
