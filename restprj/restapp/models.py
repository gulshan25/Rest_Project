from django.db import models


# Create your models here.
class Employee (models.Model):
    
    name=models.CharField('Employee Name',max_length=100)
    email=models.EmailField('Email Address',max_length=100)
    salary=models.FloatField('Monthly Salary')

   

    def __str__(self):
        return self.name