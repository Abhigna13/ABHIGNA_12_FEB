from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dob', 'gender', 'branch', 'phone', 'blood_group')
    search_fields = ('name', 'branch', 'phone')
    list_filter = ('gender', 'blood_group', 'branch')  # optional filters
    