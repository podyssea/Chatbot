# todo: is it proper to test on the live database? probably not, but we do not have a dev one
# todo: shall we test with non-existant data to see what it returns? probably
from decimal import Decimal
from app.database import database
from app.models import ShortCourse
from app.utils import database_test_helper

# sample test values to use below. perhaps these can be put in a setUp class somewhere?
test_subject = 'Law'
test_title = 'You the jury: the criminal trial'
test_end_date = '03/11/2018'
test_duration = 1
test_description = 'This day event provides an opportunity to ask the questions the jury may not. We consider ' \
                   'the procedure, the processes and roles in a Scottish criminal court. By reflecting on criminal ' \
                   'cases of the past this develops an understanding of how cases are put together and presented. ' \
                   'This day event will be interactive allowing you to take on the various roles including judge and ' \
                   'the jury. There is the chance to look to future changes and developments including technology ' \
                   'that may change the court trial of the 21st century. '
test_credits_attached = 0
test_class_code = 5621
test_cost = Decimal(40.00)
test_start_date = '03/11/2018'
test_tutor = 'Gillian  Mawdsley'


def test_all_course_titles(app):
    with app.app_context():
        response = database.all_course_titles()
        assert type(response) is list
        assert len(response) > 0
        assert all(isinstance(item, ShortCourse) for item in response)


def test_all_subjects(app):
    with app.app_context():
        response = database.all_subjects()
        assert type(response) is list
        assert len(response) > 0
        assert all(isinstance(item, tuple) for item in response)
        assert all(isinstance(item[0], str) for item in response)


# -----------------------TITLE-------------------------------------------------


def test_specific_subject_courses(app):
    with app.app_context():
        response = database.specific_subject_courses(test_subject)
        assert type(response) is list
        assert len(response) > 0
        assert all(isinstance(item, ShortCourse) for item in response)


def test_title_give_cost(app):
    with app.app_context():
        response = database.title_give_cost(test_title)
        assert hasattr(response, 'Cost')
        cost = response.Cost
        assert database_test_helper(cost, Decimal, test_cost) == (True, True)


def test_title_give_classcode(app):
    with app.app_context():
        response = database.title_give_classcode(test_title)
        assert hasattr(response, 'Class_code')
        class_code = response.Class_code
        assert database_test_helper(class_code, int, test_class_code) == (True, True)


def test_title_give_credits(app):
    with app.app_context():
        response = database.title_give_credits(test_title)
        assert hasattr(response, 'Credits_attached')
        credits_attached = response.Credits_attached
        assert database_test_helper(credits_attached, int, test_credits_attached) == (True, True)


def test_title_give_description(app):
    with app.app_context():
        response = database.title_give_description(test_title)
        assert hasattr(response, 'Description')
        description = response.Description
        assert database_test_helper(description, str, test_description) == (True, True)


def test_title_give_duration(app):
    with app.app_context():
        response = database.title_give_duration(test_title)
        assert hasattr(response, 'Duration')
        duration = response.Duration
        assert database_test_helper(duration, int, test_duration) == (True, True)


def test_title_give_end(app):
    with app.app_context():
        response = database.title_give_end(test_title)
        assert hasattr(response, 'End_date')
        end_date = response.End_date
        assert database_test_helper(end_date, str, test_end_date) == (True, True)


def test_title_give_start(app):
    with app.app_context():
        response = database.title_give_start(test_title)
        assert hasattr(response, 'Start_date')
        start_date = response.Start_date
        assert database_test_helper(start_date, str, test_start_date) == (True, True)


def test_title_give_subarea(app):
    with app.app_context():
        response = database.title_give_subarea(test_title)
        assert hasattr(response, 'Subject_area')
        subject_area = response.Subject_area
        assert database_test_helper(subject_area, str, test_subject) == (True, True)


def test_title_give_tutor(app):
    with app.app_context():
        response = database.title_give_tutor(test_title)
        assert hasattr(response, 'Tutor')
        tutor = response.Tutor
        assert database_test_helper(tutor, str, test_tutor) == (True, True)


def test_title_give_venue(app):
    with app.app_context():
        response = database.title_give_venue(test_title)
        assert response is None  # this is because the method isn't completed


# -------------------------------ID-------------------------------------


def test_id_give_cost(app):
    with app.app_context():
        response = database.id_give_cost(test_class_code)
        assert hasattr(response, 'Cost')
        cost = response.Cost
        assert database_test_helper(cost, Decimal, test_cost) == (True, True)


def test_id_give_title(app):
    with app.app_context():
        response = database.id_give_title(test_class_code)
        assert hasattr(response, 'Title')
        title = response.Title
        assert database_test_helper(title, str, test_title) == (True, True)


def test_id_give_credits(app):
    with app.app_context():
        response = database.id_give_credits(test_class_code)
        assert hasattr(response, 'Credits_attached')
        credits_attached = response.Credits_attached
        assert database_test_helper(credits_attached, int, test_credits_attached) == (True, True)


def test_id_give_description(app):
    with app.app_context():
        response = database.id_give_description(test_class_code)
        assert hasattr(response, 'Description')
        description = response.Description
        assert database_test_helper(description, str, test_description) == (True, True)


def test_id_give_duration(app):
    with app.app_context():
        response = database.id_give_duration(test_class_code)
        assert hasattr(response, 'Duration')
        duration = response.Duration
        assert database_test_helper(duration, int, test_duration) == (True, True)


def test_id_give_end(app):
    with app.app_context():
        response = database.id_give_end(test_class_code)
        assert hasattr(response, 'End_date')
        end_date = response.End_date
        assert database_test_helper(end_date, str, test_end_date) == (True, True)
