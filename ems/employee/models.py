from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()
    joining_date = models.DateField()

    def __str__(self):
        return self.name
