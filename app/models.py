from django.db import models
from django.forms import ModelForm

# Create your models here.

branch = [
    ('CSE','Computer Science Engineering'),
    ('ME','Mechanical Engineering'),
]

semester = [
    ('S1','Semester 1'),
    ('S2','Semester 2'),
    ('S3','Semester 3'),
    ('S4','Semester 4'),
    ('S5','Semester 5'),
    ('S6','Semester 6'),
    ('S7','Semester 7'),
    ('S8','Semester 8'),
]

class Registration(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    branch = models.CharField(max_length=3,choices=branch,default="CSE")
    semester = models.CharField(max_length=2,choices=semester,default="S1")
    question = models.TextField()

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"