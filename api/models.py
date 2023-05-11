from django.db import models

# Create your models here.

# name,dept,salary,address,phone,email

class Employee(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    salary=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name