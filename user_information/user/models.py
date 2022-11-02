from django.db import models

# Create your models here.


class User(models.Model):
    First_Name = models.CharField(max_length=264, unique=True)
    Last_Name = models.CharField(max_length=264, unique=True)
    Email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return f"First Name:- {self.First_Name},  Last Name:- {self.Last_Name}, Email: {self.Email}"
   

