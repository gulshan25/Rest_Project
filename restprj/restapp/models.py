from django.db import models


<<<<<<< HEAD
# Create your models here.
class Employee (models.Model):
    
=======
class Employee (models.Model):

>>>>>>> 29bf8bf6f84c5797206169df8c8c338d1f82dad7
    name=models.CharField('Employee Name',max_length=100)
    email=models.EmailField('Email Address',max_length=100)
    salary=models.FloatField('Monthly Salary')

<<<<<<< HEAD
   

    def __str__(self):
        return self.name
=======
    

    def __str__(self):
        return self.name

    

>>>>>>> 29bf8bf6f84c5797206169df8c8c338d1f82dad7
