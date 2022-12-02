from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=40)
    author=models.CharField(max_length=30)
    textarea=models.TextField()
    photo=models.ImageField(upload_to='img')