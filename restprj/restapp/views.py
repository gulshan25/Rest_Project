from django.shortcuts import render
from django.views.generic import *
from rest_framework import viewsets
from restapp.models import Employee
from restapp.serializers import EmployeeSerializer
<<<<<<< HEAD
=======

>>>>>>> 29bf8bf6f84c5797206169df8c8c338d1f82dad7
# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'

class EmployeeViewset(viewsets.ModelViewSet): 
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
<<<<<<< HEAD
=======

>>>>>>> 29bf8bf6f84c5797206169df8c8c338d1f82dad7
