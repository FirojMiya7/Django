from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField(default='2000-01-01')
    address = models.TextField(max_length=100, default='Home Address')


    def __str__(self):
        return self.first_name
