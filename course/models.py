from django.db import models

# Create your models here.

class Course(models.Model):
    course_code = models.IntegerField()
    course_name= models.CharField(max_length = 20)
    # start_date = models.DateField()
    # end_date = models.DateField()
    department_id = models.IntegerField()
    instructor_id = models.IntegerField()
    enrollment_capacity = models.PositiveSmallIntegerField()
    location = models.CharField(max_length = 20)
    status = models.CharField(max_length = 15)

    def __str__(self):
        return f"{self.course_name}"