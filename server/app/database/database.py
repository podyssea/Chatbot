from app.models import ShortCourse


# http://flask-sqlalchemy.pocoo.org/2.3/queries/
# https://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query

def all_course_titles():
    records = ShortCourse.query.all()
    return records


def all_subjects():
    records = ShortCourse.query.with_entities(
        ShortCourse.Subject_area).distinct()  # returns as list of tuples with each tuple in the form (Subject Area, )
    return records


def specific_subject_courses(subject):
    records = ShortCourse.query.filter_by(Subject_area=subject).all()
    return records

# -----------------------------------TITLE------------------------------------


def title_give_cost(title):
    records = ShortCourse.query.with_entities(ShortCourse.Cost).filter_by(Title=title).first()
    return records


def title_give_classcode(title):
    records = ShortCourse.query.with_entities(ShortCourse.Class_code).filter_by(Title=title).first()
    return records


def title_give_credits(title):
    records = ShortCourse.query.with_entities(ShortCourse.Credits_attached).filter_by(Title=title).first()
    return records


def title_give_description(title):
    records = ShortCourse.query.with_entities(ShortCourse.Description).filter_by(Title=title).first()
    return records


def title_give_duration(title):
    records = ShortCourse.query.with_entities(ShortCourse.Duration).filter_by(Title=title).first()
    return records


def title_give_end(title):
    records = ShortCourse.query.with_entities(ShortCourse.End_date).filter_by(Title=title).first()
    return records


def title_give_start(title):
    records = ShortCourse.query.with_entities(ShortCourse.Start_date).filter_by(Title=title).first()
    return records


def title_give_subarea(title):
    records = ShortCourse.query.with_entities(ShortCourse.Subject_area).filter_by(Title=title).first()
    return records


def title_give_tutor(title):
    records = ShortCourse.query.with_entities(ShortCourse.Tutor).filter_by(Title=title).first()
    return records


def title_give_venue(title):
    records = None  # todo: make this work when the venue in the database does change
    return records

# -------------------------------ID-------------------------------------


def id_give_cost(class_code):
    records = ShortCourse.query.with_entities(ShortCourse.Cost).filter_by(Class_code=class_code).first()
    return records


def id_give_title(class_code):
    records = ShortCourse.query.with_entities(ShortCourse.Title).filter_by(Class_code=class_code).first()
    return records


def id_give_credits(class_code):
    records = ShortCourse.query.with_entities(ShortCourse.Credits_attached).filter_by(Class_code=class_code).first()
    return records


def id_give_description(class_code):
    records = ShortCourse.query.with_entities(ShortCourse.Description).filter_by(Class_code=class_code).first()
    return records


def id_give_duration(class_code):
    records = ShortCourse.query.with_entities(ShortCourse.Duration).filter_by(Class_code=class_code).first()
    return records


def id_give_end(class_code):
    records = ShortCourse.query.with_entities(ShortCourse.End_date).filter_by(Class_code=class_code).first()
    return records


def id_give_start(class_code):
    records = ShortCourse.query.with_entities(ShortCourse.Start_date).filter_by(Class_code=class_code).first()
    return records


def id_give_subarea(class_code):
    records = ShortCourse.query.with_entities(ShortCourse.Subject_area).filter_by(Class_code=class_code).first()
    return records


def id_give_tutor(class_code):
    records = ShortCourse.query.with_entities(ShortCourse.Tutor).filter_by(Class_code=class_code).first()
    return records


def id_give_venue(class_code):
    records = ShortCourse.query.with_entities(ShortCourse.Venue).filter_by(Class_code=class_code).first()
    return records

# ------------------------------OTHER---------------------------


def cost_give_title(cost):
    records = ShortCourse.query.with_entities(ShortCourse.Title).filter_by(Cost=cost).first()
    return records


def credits_give_title(credits_attached):
    records = ShortCourse.query.with_entities(ShortCourse.Title).filter_by(Credits_attached=credits_attached).first()
    return records


def duration_give_title(duration):
    records = ShortCourse.query.with_entities(ShortCourse.Title).filter_by(Duration=duration).first()
    return records


def end_give_title(end):
    records = ShortCourse.query.with_entities(ShortCourse.Title).filter_by(End_date=end).first()
    return records


def start_give_title(start):
    records = ShortCourse.query.with_entities(ShortCourse.Title).filter_by(Start_date=start).first()
    return records


def subarea_give_title(subarea):
    records = ShortCourse.query.with_entities(ShortCourse.Title).filter_by(Subject_area=subarea).first()
    return records


def tutor_give_title(tutor):
    records = ShortCourse.query.with_entities(ShortCourse.Title).filter_by(Tutor=tutor).first()
    return records


def venue_give_title(venue):
    records = ShortCourse.query.with_entities(ShortCourse.Title).filter_by(Venue=venue).first()
    return records
