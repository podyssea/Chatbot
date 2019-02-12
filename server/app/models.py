from app import db


class ShortCourse(db.Model):
    __tablename__ = 'Short_Courses'
    Subject_area = db.Column(db.Text(150))
    Title = db.Column(db.Text(150))
    Class_code = db.Column(db.Integer)
    Start_date = db.Column(db.Text(50))
    End_date = db.Column(db.Text(50))
    Start_time = db.Column(db.DECIMAL(10, 2))
    End_time = db.Column(db.DECIMAL(10, 2))
    Cost = db.Column(db.DECIMAL(10, 2))
    Duration = db.Column(db.Integer)
    Tutor = db.Column(db.Text(120))
    Venue = db.Column(db.Text)
    Link_to_Course_specification = db.Column(db.Text)
    Description = db.Column(db.Text(65535))
    Credits_attached = db.Column(db.Integer)
    Language_Level_of_Study_links = db.Column(db.Text)
    pk_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        return "Title: {}".format(self.Title)
