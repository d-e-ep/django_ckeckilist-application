from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    mobile_no = models.IntegerField(max_length=100)
    password = models.CharField(max_length=70)