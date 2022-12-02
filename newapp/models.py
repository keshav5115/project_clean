from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class newusermodel(User):
    phone=models.PositiveBigIntegerField()
    list=[['Male','Male'],['Female','Female']]
    gender=models.CharField(max_length=10,choices=list)
    photo=models.ImageField(upload_to='image')
