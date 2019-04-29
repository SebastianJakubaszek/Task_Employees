from rest_framework import viewsets
from .models import JobPosition, Employee
from .api.serializers import JobPositionSerializer, EmployeeSerializer

class Employeeviews(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class JobPositionviews(viewsets.ModelViewSet):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer