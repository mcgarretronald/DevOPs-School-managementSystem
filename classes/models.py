from django.db import models

# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length = 20)
    teacher = models.CharField(max_length = 20)
    room_number = models.PositiveSmallIntegerField()
    class_size = models.PositiveSmallIntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    school_year = models.DateField()
    created_at = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.class_name}"
