from email.policy import default

from django.db import models
from django.utils import timezone

# Create your models here.


class todo(models.Model):

    todoType = [
        ('RG', 'Regular'),
        ('EDU', 'Education'),
        ('OFF', 'Office'),
        ('GK', 'General Knowledge'),
    ]

    taskName = models.CharField(max_length=100)
    taskDescription = models.TextField(max_length=250)
    image = models.ImageField(upload_to='todo/')
    taskType = models.CharField(max_length=3, choices=todoType, default='RG')
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.taskName
