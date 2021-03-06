from django.db import models
from django.core.validators import RegexValidator
import uuid

class JobPosition (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30,unique=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    phone = models.BigIntegerField( validators=[RegexValidator(regex='^\d{9,15}$')],blank=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    jobposition = models.ForeignKey(JobPosition, related_name="employees", on_delete=models.CASCADE)
    is_working = models.BooleanField(default=False)
    comment = models.TextField(blank=True)
