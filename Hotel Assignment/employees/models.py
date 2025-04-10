from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    department_number = models.CharField(max_length=75)

    def __str__(self):
        return self.emp_id