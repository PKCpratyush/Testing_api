from rest_framework import serializers

class Student_data_serializer(serializers.Serializer):
    roll_no = serializers.IntegerField()
    name = serializers.CharField(max_length= 30)
    city = serializers.CharField(max_length=30)
    # courses = serializers.CharField(max_length = 100)

class Course_serializer(serializers.Serializer):
    course = serializers.CharField(max_length = 100)