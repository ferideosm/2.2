from pyexpat import model
from django.db import models


class Student(models.Model):

    name = models.TextField()

    birth_date = models.DateField(
        null=True,
    )

    def __str__(self):
        return self.name

class Course(models.Model):

    name = models.TextField()

    students = models.ManyToManyField(
        Student,
        through="StudentCourse",
        related_name='course',        
        blank=True,
    )

class StudentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_course')
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_course')
    
