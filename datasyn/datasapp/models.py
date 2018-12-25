from django.db import models

# Create your models here.


class User(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    passwd = models.CharField(max_length=60)