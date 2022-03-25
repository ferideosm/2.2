from pyexpat import model
from django.contrib import admin

from students.models import Student, Course, StudentCourse

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'birth_date')
    list_display =  ('id', 'name', 'birth_date')
    list_display_links =  ('id', 'name', 'birth_date')


class StudentCourseInline(admin.TabularInline):
    model =StudentCourse
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name')
    list_display =  ('id', 'name')
    list_display_links =  ('id', 'name')
    inlines = [StudentCourseInline]
