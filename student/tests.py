from django.test import TestCase
from .models import Student
from datetime import datetime
from .forms import StudentRegistrationForm

# Create your tests here.


class StudentTestCase(TestCase):

    def setUp(self):
            self.student = Student(
               first_name = "Bonnette",
                last_name = "Umutoni",
                email = "umutonibonnette@gmail.com",
                # date_of_birth = datetime.date(2009, 9, 17),
                code = "032",
                gender = "female",
                country = "Rwanda",
                Bio = "My name is Bonnette Umunyana, I am a new student"
                )
            
    # def test_full_name_contains_first_name(self):
    #     self.assertIn(self.student.first_name,self.student.full_name())

    # def test_age_is_number(self):
    #      self.assertIn(self.student.age, self.student.age())

    # def test_full_name_contains_last_name(self):
    #     self.assertIn(self.student.last_name,self.student.fullname())
         

class StudentFormTest(TestCase):
#      def test_student_form_valid(self):
#           form_data = {
#                'first_name': 'Glory',
#                'last_name': 'Maina',
#                'email': 'glorymaina@gmail.com',
#                'date_of_birth': '2002-09-21',
#                'code': '002',
#                'gender': 'female',
#                'country': 'Kenya',
#                'Bio': 'Hello, My name is Glory Joy, I am a DevOps Engineer'
#           }

#           form = StudentRegistrationForm(data=form_data)
#           self.assertTrue(form.is_valid())

     def test_student_form_invalid(self):
          form_data = {
               'first_name': 'Glory',
               'last_name': 'Maina',
               'email': 'glorymaina@gmail.com'
          }

          form = StudentRegistrationForm(data=form_data)
          self.assertFalse(form.is_valid())
          self.assertIn('date_of_birth', form.errors)

          

