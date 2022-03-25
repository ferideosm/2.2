from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from students.filters import CourseFilter
from students.models import Course, Student, StudentCourse
from students.serializers import CourseSerializer, StudentCourseSerializer, StudentSerializer


class CoursesViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CourseFilter
    filter_fields = ('name', 'id')


class StudentViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend, )
    # filterset_class = CourseFilter


class StudentCoursesViewSet(ModelViewSet):

    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
    # filter_backends = (DjangoFilterBackend, )
    # filterset_class = CourseFilter