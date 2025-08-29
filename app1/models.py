import os
from datetime import datetime

def image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.student_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    return os.path.join('student_images', filename)



from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    # ✅ New Column:
    #educational_institution = models.CharField(max_length=150, blank=True, null=True)

    # ✅ Add this line for Image
    profile_image = models.ImageField(upload_to='image_upload_path', blank=True, null=True)

    def __str__(self):
        return self.name
