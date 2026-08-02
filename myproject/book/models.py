from django.db import models

# Create your models here.

class Book(models.Model):
    title =models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    publishedDate=models.DateField()

    def __str__(self):
        return self.title
