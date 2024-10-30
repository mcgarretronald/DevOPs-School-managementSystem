
from rest_framework import serializers
from student.models import Student
from classes.models import Class
from classPeriod.models import ClassPeriod
from course.models import Course
from teacher.models import Teacher
from datetime import date
from classPeriod.models import ClassPeriod

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

class MinimalStudentSerializer(serializers.ModelSerializer):
   
   full_name = serializers.SerializerMethodField()
   def get_full_name(self, Student):
      return f"{Student.first_name} {Student.last_name}"
   
   class Meta:
      model = Student
      fields = ["id","full_name","email"]

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class
        fields="__all__"

class MinimalClassesSerializer(serializers.ModelSerializer):
   
   class_time = serializers.SerializerMethodField()
   def get_class_time(self, Class):
      return f"Starts: {Class.start_time} Ends:{Class.end_time}"
   
   class Meta:
      model = Class
      fields = ["course","classroom", "class_time"]
        
class ClassPeriodSerializer(serializers.ModelSerializer):
  class Meta:
    model=ClassPeriod
    fields="__all__"

class MinimalClassPeriodSerializer(serializers.ModelSerializer):
   
   class_time = serializers.SerializerMethodField()
   def get_class_time(self, ClassPeriod):
      return f"Starts: {ClassPeriod.start_time} Ends:{ClassPeriod.end_time}"
   
   class Meta:
      model = ClassPeriod
      fields = ["course","classroom", "class_time"]

class CoursesSerializer(serializers.ModelSerializer):
 class Meta:
    model=Course
    fields = "__all__"

class MinimalCoursesSerializer(serializers.ModelSerializer):
   
   school_direction = serializers.SerializerMethodField()
   def get_school_direction(self, Course):
      return f"School: {Course.location} Course: {Course.course_name}"
   
   class Meta:
      model = Course
      fields = ["instructor_id","school_direction","status"]

class TeacherSerializer(serializers.ModelSerializer):
 courses = CoursesSerializer(many = True)
 class Meta:
    model=Teacher
    fields = "__all__"
    # exclude = ["email"]

class MinimalTeacherSerializer(serializers.ModelSerializer):
   
   full_name = serializers.SerializerMethodField()
   age = serializers.SerializerMethodField()
   def get_full_name(self, Teacher):
      return f"{Teacher.first_name} {Teacher.last_name}"
   def get_age(self, Teacher):
      today = date.today()
      age = today - Teacher.date_of_birth
      return age
   class Meta:
      model = Teacher
      # fields = ["id","full_name","email"]
      fields = ["id","full_name","age","email"]