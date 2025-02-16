from django.db import models

class signup(models.Model):
    Firstname=models.CharField(max_length=20,default="")
    Lastname=models.CharField(max_length=20,default="")
    Email=models.CharField(max_length=20,default="")
    Password=models.CharField(max_length=20,default="")