from django.db import models

# Create your models here.
class reg_tb(models.Model):
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    conformpassword=models.CharField(max_length=255)

class service_tb(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    image=models.ImageField(upload_to="serviceimg/")

class project_tb(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="projectimg/")

class gallery_tb(models.Model):
    image=models.ImageField(upload_to="galleryimg/")


class contact_tb(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField()

class getin_tb(models.Model):
    sername=models.ForeignKey(service_tb, on_delete=models.CASCADE)
    email=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    message=models.TextField()