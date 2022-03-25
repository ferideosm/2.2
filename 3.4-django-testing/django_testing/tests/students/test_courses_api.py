from codecs import backslashreplace_errors
from urllib import response
import pytest
from students.models import Course, Student
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def sourse_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

# 1 проверка получения 1го курса (retrieve-логика)
@pytest.mark.django_db
def test_retrieve_courses(client, sourse_factory):
    sourses = sourse_factory(id=1)
    response = client.get(f'/courses/{sourses.id}/')   
    assert response.status_code == 200

# 2 проверка получения списка курсов (list-логика)
@pytest.mark.django_db
def test_list_courses(client, sourse_factory):
    sourses = sourse_factory(_quantity=10)

    response = client.get('/courses/')   
    data = response.json()

    assert len(data) == len(sourses)

# 3 проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_courses_by_id(client, sourse_factory):
    sourses = sourse_factory(id=10)
    response = client.get('/courses/?id=10')  
    assert response.status_code == 200


# 4 проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_courses_by_name(client, sourse_factory):
    sourses = sourse_factory(name='2')
    response = client.get('/courses/?name=2') 
    assert response.status_code == 200
     
# 5 тест успешного создания курса
@pytest.mark.django_db
def test_create_new_courses(client):
    data  = {
                "name": "11"
            }
    response = client.post('/courses/', data=data) 
    assert response.status_code == 201

# 5a тест успешного создания курса со студентом
@pytest.mark.django_db
def test_create_new_course_with_student(client, student_factory):

    student = student_factory(id=1)

    data  = {
        "name": "3",
        "students":[
            {
            "id": student.pk,
            "name": student.name
            }
        ]
    }

    response = client.post('/courses/', data=data, format='json') 
    assert response.status_code == 201
    data = response.json()
    for data_student in data['students']:
        print('student ==', data_student)
        assert data_student['name'] == student.name

# 6 тест успешного обновления курса
@pytest.mark.django_db
def test_update_courses(client, sourse_factory):
    sourse_factory = sourse_factory()
    data  = {
                "name": "100"
            }
    response = client.patch(f'/courses/{sourse_factory.id}/', data=data) 
    assert response.status_code == 200

# 7 тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, sourse_factory):
    sourse_factory = sourse_factory()
    response = client.delete(f'/courses/{sourse_factory.id}/') 
    assert response.status_code == 204   
        
        