from schools.models import SchoolModel
from django.db import models
from datetime import date
from statistic.models import SubjectModel
from schools.models import SchoolModel


class Person(models.Model):
    name = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=date.today)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True

class StudentModel(Person):
    active = models.BooleanField(default=False)
    username = models.CharField(default='',max_length=25)
    password = models.CharField(default='',max_length=65)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'students'


class TeacherModel(Person):
    subject_id = models.ForeignKey(SubjectModel,on_delete=models.SET_NULL)
    salary = models.PositiveBigIntegerField(default=1)
    school = models.ManyToManyField(to=SchoolModel)
    
    class Meta:
        db_table = 'teachers'

