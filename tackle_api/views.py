from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.utils import json
from .models import Student,Courses
from .serializer import Student_data_serializer, Course_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

from tackle_api import serializer

# Create your views here.

def student_detail(request, id=1):
    student = Student.objects.get(roll_no = id)
    serializer = Student_data_serializer(student)
    course_list = ""
    subjects = Courses.objects.filter(student=student)

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = 'application/json')

def course_detail(request, id=1):
    student = Student.objects.get(roll_no = id)
    
    subjects = Courses.objects.filter(student=student)
    serializer = Course_serializer(subjects, many=True)

    # json_data = JSONRenderer().render(serializer.data)

    # return HttpResponse(json_data, content_type = 'application/json')

    # safe=False for non dict objects otherwise left it as True as default
    return JsonResponse(serializer.data, safe=False)