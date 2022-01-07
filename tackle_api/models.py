from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices

from django.db.models.fields.related import ForeignKey

# Create your models here.

class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length= 30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Courses(models.Model):
    student = ForeignKey(Student, on_delete=CASCADE)

    course_choices = [
        ('Sc', 'Science'),
        ('Art','Arts'),
        ('Cmc','commerce'),
        ('Math', 'Maths')
    ]

    course = models.CharField(choices=course_choices, max_length=10,default='Maths')

    def __str__(self):
        return self.student.name