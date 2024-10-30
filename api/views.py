
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from student.models import Student
from .serializers import StudentSerializer
from classes.models import Class
from .serializers import ClassesSerializer
from classPeriod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from course.models import Course
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework import status
from .serializers import MinimalTeacherSerializer
from .serializers import MinimalCoursesSerializer
from .serializers import MinimalClassPeriodSerializer
from .serializers import MinimalStudentSerializer

class StudentListViews(APIView):
    def get(self,request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name = first_name)
        serializer = MinimalStudentSerializer(students, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self,request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    def enroll(self, student, course_id):
        course = Course.objects.get(id = course_id)
        student.courses.add(course)

    def unenroll(self, student, class_id):
        classes = Class.objects.get(id=class_id)
        classes.students.add(student)

    def add_to_class(self, student, class_id):
        classes = Class.objects.get(id=class_id)
        classes.students.add(student)

    def post(self, request,id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")

        if action=="email":
            course_id = request.data.get("course_id")
            self.enroll(student, course_id)
            return Response(status=status.HTTP_201_CREATED)
        
        elif  action == "unenroll":
            course_id = request.data.get("course_id")
            self.unenroll(student, course_id)
            return Response(status=status.HTTP_200_OK)
        
        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_201_CREATED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ClassListViews(APIView):
    def get(self,request):
        Classes = Class.objects.all()
        serializer = ClassesSerializer(Classes,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class ClassDetailView(APIView):
    def get(self,request, id):
        classe = Class.objects.get(id=id)
        serializer = ClassesSerializer(classe)
        return Response(serializer.data)
    
    def put(self,request, id):
        classe = Class.objects.get(id=id)
        serializer = ClassesSerializer(classe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, id):
        classe = Class.objects.get(id=id)
        classe.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class ClassPeriodListViews(APIView):
    def get(self,request):
        Periods = ClassPeriod.objects.all()
        serializer = MinimalClassPeriodSerializer(Periods,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassPeriodSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class ClassPeriodDetailView(APIView):
    def get(self,request, id):
        classe = Class.objects.get(id=id)
        serializer = ClassPeriodSerializer(classe)
        return Response(serializer.data)
    
    def put(self,request, id):
        period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, id):
        classe = Class.objects.get(id=id)
        classe.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def post(self, request, id):
        action = request.data.get("action")
        if action == "create_class_period":
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            self.create_class_period(teacher_id, course_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def create_class_period(self, teacher_id, course_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Course.objects.get(id=course_id)
        class_period = ClassPeriod(teacher=teacher, course=course)
        class_period.save()
        return Response(status=status.HTTP_201_CREATED)

class CoursesListViews(APIView):
    def get(self,request):
        Periods = Course.objects.all()
        serializer = MinimalCoursesSerializer(Periods,many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class CoursesDetailView(APIView):
    def get(self,request, id):
        course = Course.objects.get(id=id)
        serializer = CoursesSerializer(course)
        return Response(serializer.data)
    
    def put(self,request, id):
        course = Course.objects.get(id=id)
        serializer = CoursesSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class TeacherListViews(APIView):
    def get(self,request):
        Teachers = Teacher.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            teachers = Teachers.filter(first_name = first_name)

        serializer = MinimalTeacherSerializer(Teachers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
class TeacherDetailView(APIView):
    
    def get(self,request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self,request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

    def assign_course(self, teacher, course_id):
        course = Course.objects.get(id=course_id)
        teacher.courses.add(course)

    def assign_class(self, teacher, class_id):
        student_class = Student.objects.get(id=class_id)
        student_class.teacher = teacher
        student_class.save()

    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")

        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response(status=status.HTTP_201_CREATED)
        
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            self.assign_class(teacher, class_id)
            return Response(status=status.HTTP_201_CREATED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def post(self, request, id):
        teacher = Teacher.objects.get(id = id)
        action =request.data.get("action")
        if action == "enroll":
            class_name = request.data.get("class_name")
            self.enroll(teacher, class_name)
            return Response(status = status.HTTP_201_CREATED)
    
class WeeklyTimetable(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
