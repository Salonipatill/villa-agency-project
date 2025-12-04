from django.db import models
from django.utils.timezone import now
# Create your models here.
class Customer(models.Model):
    cname=models.CharField(max_length=50)
    cadd=models.CharField(max_length=90)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    unm=models.CharField(max_length=70)
    pw=models.CharField(max_length=70)

class ImageUploader(models.Model):
    photo=models.ImageField(upload_to="ALLImages")
    date=models.DateTimeField(default=now)


class Property(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='properties/')
     