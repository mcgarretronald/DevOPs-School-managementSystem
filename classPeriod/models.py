from django.db import models
from course.models import Course
from classes.models import Class

class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    classroom = models.ForeignKey(Class, on_delete = models.CASCADE)
    # day_of_week = models.DateField()

    def __str__(self):
        return f"{self.course}, {self.classroom}"
