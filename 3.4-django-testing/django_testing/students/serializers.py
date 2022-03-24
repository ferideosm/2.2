from rest_framework import serializers

from students.models import Course, Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("id", "name", "birth_date")
    

class CourseSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(many=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    # def create(self, validated_data):
    #     print('validated_data==', validated_data)
    #     students = validated_data.pop('students')
    #     print('students==', students)
        
    #     ls = []
    #     for student in students:
    #         student = Student.objects.get(name=student['name'])

    #         ls.append({
    #             'id': student.pk,
    #             'name': student.name,
    #         })
    #     validated_data["students"] = ls
    #     print('validated_data 2==', validated_data)
    #     course = super().create(validated_data)
    #     print('course==', course)
    #     return course


