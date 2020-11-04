from django.db import models

# Create your models here.
class StudentRegistration(models.Model):
    name=models.CharField(max_length=50)
    contact = models.IntegerField()
    date_of_birth=models.DateField()
    qualification = models.CharField(max_length=30)
    passing_year = models.DateField()
    emil=models.EmailField()
    password=models.CharField(max_length=30)

