from django.shortcuts import render

from .models import RegistrationForm
branches = [
    ('CSE','Computer Science Engineering'),
    ('ME','Mechanical Engineering'),
]

semesters = [
    ('S1','Semester 1'),
    ('S2','Semester 2'),
    ('S3','Semester 3'),
    ('S4','Semester 4'),
    ('S5','Semester 5'),
    ('S6','Semester 6'),
    ('S7','Semester 7'),
    ('S8','Semester 8'),
]
# Create your views here.
def index(request):
    form = RegistrationForm()
    context = {"form":form,"branches":branches,"semesters":semesters}
    return render(request,'index.html',context)