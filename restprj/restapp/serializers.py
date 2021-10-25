from rest_framework import serializers
from restapp.models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
<<<<<<< HEAD
        fields=('id','name','email','salary')

=======
        fields=('id','name','email','salary')
>>>>>>> 29bf8bf6f84c5797206169df8c8c338d1f82dad7
