from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=60)
    employee_phone = models.CharField(max_length=10)
    employee_address = models.CharField(max_length=100)
    is_working = models.BooleanField(default=True)
    department= models.CharField(max_length=10, default="")