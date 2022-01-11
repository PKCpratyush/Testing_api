from django.contrib import admin
from tackle_api import models

# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.Courses)

class StudentAdmin(admin.ModelAdmin):
    list_display = ["roll_no","name","city"]