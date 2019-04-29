from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('job_position', views.JobPositionviews)
router.register('employee', views.Employeeviews)

urlpatterns = [
    path('',include(router.urls))
]