from django.db import models
from datetime import date

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    date_of_birth = models.DateField(("Date"), default=date.today)
    code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length = 28)
    gender = models.CharField(max_length = 6)
    Bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name}"
    
    def age(self):
        return self.age
    
    def get_code(self):
        return self.code