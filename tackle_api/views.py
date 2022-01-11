from functools import partial
from django.core.checks import messages
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.utils import json
from .models import Student,Courses
from .serializer import Student_data_serializer, Course_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import black

from tackle_api import serializer

# using this for ignoring csrf token need


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

@csrf_exempt
def insert_student_detail(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)# geeting stream object
        # converting into python data
        data = JSONParser().parse(stream)
        serializer = Student_data_serializer(data = data)
        if serializer.is_valid():
            serializer.save()
            message = {"msg":"Data Inserted"}

            return JsonResponse(message)

        else:
            return JsonResponse(JSONRenderer().render(serializer.errors))

@csrf_exempt
def update_student(request):
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        roll = data.get('roll_no')
        # print(Student.objects.get(roll_no = roll).exist())
        student_data = Student.objects.get(roll_no = roll)
        # partial = True to allow to make partial update in the row
        serializer = Student_data_serializer(student_data, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'Data Updated'})
        else:
            return JsonResponse(JSONRenderer().render(serializer.errors))
