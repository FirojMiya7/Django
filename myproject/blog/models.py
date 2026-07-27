from email.policy import default

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.


class todo(models.Model):

    todoType = [
        ('RG', 'Regular'),
        ('EDU', 'Education'),
        ('OFF', 'Office'),
        ('GK', 'General Knowledge'),
    ]

    id = models.BigAutoField(primary_key=True)
    taskName = models.CharField(max_length=100)
    taskDescription = models.TextField(max_length=250)
    image = models.ImageField(upload_to='todo/')
    taskType = models.CharField(max_length=3, choices=todoType, default='RG')
    createdAt = models.DateTimeField(default=timezone.now)
    assignedTo = models.CharField(max_length=100, default='Unassigned')
    completedAt = models.DateTimeField(default='2026-01-01')

    def __str__(self):
        return self.taskName


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# One to Many Relationship

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    rating = models.IntegerField()
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}: {self.product.name} -> {self.rating} stars"


# Many to Many Relationship

class productStore(models.Model):
    product = models.ManyToManyField(Product, related_name='stores')
    storeName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.storeName} -> {self.location}"


# One to One Relationship

class ProductCertificates(models.Model):
    product = models.OneToOneField(Product, related_name='certificates', on_delete=models.CASCADE)
    certificateNumber = models.CharField(max_length=100)
    issuedBy = models.CharField(max_length=100)
    issuedDate = models.DateField(default=timezone.now)
    validUntil = models.DateField()

    def __str__(self):
        return f"Certificate for {self.product.name} issued by {self.certificateNumber} issued by {self.issuedBy} valid until {self.validUntil}"