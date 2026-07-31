from datetime import date

from django.db import models

# Create your models here.


class Student(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=15)
	course = models.CharField(max_length=100)
	date_of_birth = models.DateField(default=date(2000, 1, 1))
	address = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
