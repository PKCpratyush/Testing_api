from django.core.validators import validate_slug
from rest_framework import serializers
from .models import Student


class Student_data_serializer(serializers.Serializer):
    roll_no = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    # courses = serializers.CharField(max_length = 100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.roll_no = validated_data.get("roll_no", instance.roll_no)
        instance.city = validated_data.get("city", instance.city)
        instance.save()
        return instance



class Course_serializer(serializers.Serializer):
    course = serializers.CharField(max_length=100)
