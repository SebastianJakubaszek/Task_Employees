from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
import uuid

class JobPosition (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employees (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)
    phone = models.IntegerField( validators=[MaxLengthValidator(100),MinLengthValidator(1)],blank=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    jobposition = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    is_working = models.BooleanField(default=False)
    comment = models.TextField(blank=True)
