from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from api.serializers import EmployeeSerializer
from api.models import Employee



# Create your views here.

class EmployeesView(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    