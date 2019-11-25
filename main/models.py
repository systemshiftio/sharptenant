from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    receive_newsletter = models.BooleanField()