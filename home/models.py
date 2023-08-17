from django.db import models

# Create your models here.
class Collections(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField


class Books(models.Model):
    title=models.CharField(max_length=255)
    arthor=models.CharField(max_length=255)
    cover=models.ImageField(upload_to='uploads/books/')
    description=models.TextField


