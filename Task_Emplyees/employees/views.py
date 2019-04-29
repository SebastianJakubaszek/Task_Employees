from django.shortcuts import render
from rest_framework import viewsets
from .models import JobPosition
from .api.serializers import JobPositionSerializer

class JobPositionviews(viewsets.ModelViewSet):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer