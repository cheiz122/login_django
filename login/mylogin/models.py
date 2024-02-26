from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)

class name(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=50)
