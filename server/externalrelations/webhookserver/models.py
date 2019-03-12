from django.db import models


class ShortCourse(models.Model):
    Subject_area = models.TextField(max_length=150)
    Title = models.TextField(max_length=150)
    Class_code = models.IntegerField()
    Start_date = models.TextField(max_length=50)
    End_date = models.TextField(max_length=50)
    Start_time = models.DecimalField(max_digits=10, decimal_places=2)
    End_time = models.DecimalField(max_digits=10, decimal_places=2)
    Cost = models.DecimalField(max_digits=10, decimal_places=2)
    Duration = models.IntegerField()
    Tutor = models.TextField(max_length=120)
    Venue = models.TextField()
    Link_to_Course_specification = models.TextField()
    Description = models.TextField(max_length=65535)
    Credits_attached = models.IntegerField()
    Language_Level_of_Study_links = models.TextField()
    pk_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'Short_Courses'
        managed = False  # to not override the tables
        verbose_name = 'Short Course'
        verbose_name_plural = 'Short Courses'

    def __str__(self):
        return self.Title

    @classmethod
    def all_course_titles(cls):
        records = ShortCourse.objects.all()
        return records

    @classmethod
    def all_subjects(cls):
        records = ShortCourse.objects.values('Subject_area').distinct()
        return records

    @classmethod
    def specific_subject_courses(cls, subject):
        records = ShortCourse.objects.filter(Subject_area=subject)
        return records

    # -----------------------------------TITLE------------------------------------
   

    @classmethod
    def find_with_filters(cls, value, filters):
        return ShortCourse.object.filter(**filters).values(value).first()

    @classmethod
    def find_by_title(cls, title, parameters):
        return ShortCourse.object.filter(Title=title).values_list(parameters)

    @classmethod
    def title_give_cost(cls, title):
        records = ShortCourse.objects.filter(Title=title).values('Cost').first()
        return records

    @classmethod
    def title_give_classcode(cls, title):
        records = ShortCourse.objects.filter(Title=title).values('Class_code').first()
        return records

    @classmethod
    def title_give_credits(cls, title):
        records = ShortCourse.objects.filter(Title=title).values('Credits_attached').first()
        return records

    @classmethod
    def title_give_description(cls, title):
        records = ShortCourse.objects.filter(Title=title).values('Description').first()
        return records

    @classmethod
    def title_give_duration(cls, title):
        records = ShortCourse.objects.filter(Title=title).values('Duration').first()
        return records

    @classmethod
    def title_give_end(cls, title):
        records = ShortCourse.objects.filter(Title=title).values('End_date').first()
        return records

    @classmethod
    def title_give_start(cls, title):
        records = ShortCourse.objects.filter(Title=title).values('Start_date').first()
        return records

    @classmethod
    def title_give_subarea(cls, title):
        records = ShortCourse.objects.filter(Title=title).values('Subject_area').first()
        return records

    @classmethod
    def title_give_tutor(cls, title):
        records = ShortCourse.objects.filter(Title=title).values('Tutor').first()
        return records

    @classmethod
    def title_give_venue(cls, title):
        records = ShortCourse.objects.filter(Title=title).values('Venue').first()
        print(records)
        return records

    # -------------------------------ID-------------------------------------

    @classmethod
    def id_give_cost(cls, class_code):
        records = ShortCourse.objects.filter(Class_code=class_code).values('Cost').first()
        return records

    @classmethod
    def id_give_title(cls, class_code):
        records = ShortCourse.objects.filter(Class_code=class_code).values('Title')
        return records

    @classmethod
    def id_give_credits(cls, class_code):
        records = ShortCourse.objects.filter(Class_code=class_code).values('Credits_attached').first()
        return records

    @classmethod
    def id_give_description(cls, class_code):
        records = ShortCourse.objects.filter(Class_code=class_code).values('Description').first()
        return records

    @classmethod
    def id_give_duration(cls, class_code):
        records = ShortCourse.objects.filter(Class_code=class_code).values('Duration').first()
        return records

    @classmethod
    def id_give_end(cls, class_code):
        records = ShortCourse.objects.filter(Class_code=class_code).values('End_date').first()
        return records

    @classmethod
    def id_give_start(cls, class_code):
        records = ShortCourse.objects.filter(Class_code=class_code).values('Start_date').first()
        return records

    @classmethod
    def id_give_subarea(cls, class_code):
        records = ShortCourse.objects.filter(Class_code=class_code).values('Subject_area').first()
        return records

    @classmethod
    def id_give_tutor(cls, class_code):
        records = ShortCourse.objects.filter(Class_code=class_code).values('Tutor').first()
        return records

    @classmethod
    def id_give_venue(cls, class_code):
        records = ShortCourse.objects.filter(Class_code=class_code).values('Venue').first()
        return records

    # ------------------------------OTHER---------------------------

    @classmethod
    def cost_give_title(cls, cost):
        records = ShortCourse.objects.filter(Cost=cost).values('Title')
        return records

    @classmethod
    def credits_give_title(cls, credits_attached):
        records = ShortCourse.objects.filter(Credits_attached=credits_attached).values('Title')
        return records

    @classmethod
    def duration_give_title(cls, duration):
        records = ShortCourse.objects.filter(Duration=duration).values('Duration')
        return records

    @classmethod
    def end_give_title(cls, end):
        records = ShortCourse.objects.filter(End_date=end).values('Title')
        return records

    @classmethod
    def start_give_title(cls, start):
        records = ShortCourse.objects.filter(Start_date=start).values('Title')
        return records

    @classmethod
    def subarea_give_title(cls, subarea):
        records = ShortCourse.objects.filter(Subject_area=subarea).values('Title')
        return records

    @classmethod
    def tutor_give_title(cls, tutor):
        records = ShortCourse.objects.filter(Tutor__startswith=tutor).values('Title')
        return records

    @classmethod
    def venue_give_title(cls, venue):
        records = ShortCourse.objects.filter(Venue=venue).values('Title')
        print(records)
        return records
