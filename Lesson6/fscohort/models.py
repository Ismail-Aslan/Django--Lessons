from django.db import models
from django.db.models.fields import CharField, EmailField

class Student (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    GENDER = (
        ("1","Female")
        ("2","Male")
    )