from rest_framework import serializers
from ..models import JobPosition, Employee

class JobPositionSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = JobPosition
        fields = ('id', 'name', 'date', 'last_update','employees')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'date', 'last_update', 'jobposition', 'is_working', 'comment')