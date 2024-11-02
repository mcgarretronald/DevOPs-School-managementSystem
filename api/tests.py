from rest_framework.test import APITestCase
from student.models import Student
from django.urls import reverse
from rest_framework import status
from .serializers import StudentSerializer

# Create your tests here.

class StudentAPIViewTest(APITestCase):
    def setUp(self):
            self.student = Student(
                first_name = "Bonnette",
                last_name = "Umutoni",
                email = "umutonibonnette@gmail.com",
                # date_of_birth = datetime.date(2009, 9, 17),
                code = "032",)


    def test_get_student_list(self):
        url = reverse('student_list_view')
        response = self.client_get()
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        self.assertEqual(response.status.code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)