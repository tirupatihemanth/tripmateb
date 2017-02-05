from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField('Name of the User', max_length=200);
    date = models.DateTimeField('Date Registered');
    password = models.CharField('Hash of Email Registration Password', max_length=100);