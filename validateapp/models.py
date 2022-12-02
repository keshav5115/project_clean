from django.db import models
from  validateapp.validators import *
from django.core.validators import *

# Create your models here.
class library(models.Model):
    bookid=models.CharField(max_length=15,primary_key=True)
    bname=models.CharField(max_length=40,validators=[namelength,firstletter])
    author=models.CharField(max_length=30,validators=[namelength])
    price=models.IntegerField()
    edition=models.CharField(max_length=10)
