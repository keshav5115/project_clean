from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Autheregister(User):
    phone=models.PositiveBigIntegerField()
    list=[['Male','Male'],['Female','Female']]
    gender=models.CharField(max_length=10,choices=list)

