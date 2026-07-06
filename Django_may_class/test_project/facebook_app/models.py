from django.db import models

# Create your models here.
class Account(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    birthday = models.DateField()
    gender = models.CharField(max_length=10)