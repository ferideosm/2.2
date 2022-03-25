from asyncore import read
from importlib.util import source_hash
from rest_framework import serializers

from students.models import Course, Student, StudentCourse

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        read_only = ["name", ]
    
class StudentCourseSerializer(serializers.ModelSerializer):
    # courses = CourseSerializer()
    # students = StudentSerializer()

    class Meta:
        model = StudentCourse
        fields = ['id', 'students'] 
        read_only = ['course', 'students'] 

class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students"]

    def create(self, validated_data):
        # почему то сюда (students) приходить только name ,хотя в серилизаторе указаны все поля. Поэтому приходится использовать не ид, а name
        students = validated_data.pop('students') if validated_data.get('students') else []

        course = super().create(validated_data)

        for student in students:

            student = Student.objects.get(name=student['name'])

            StudentCourse.objects.update_or_create(students=student,
                                                    course=course,
                                                    defaults={"students": student})
        return course


