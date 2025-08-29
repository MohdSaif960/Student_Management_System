from django.db import models

# Create your models here.


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    location = models.TextField()

    def __str__(self):
        return self.name
