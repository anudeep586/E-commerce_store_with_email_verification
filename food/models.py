from django.db import models
import uuid

# Create your models here.
class Pizza(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
class Salads(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
class Noodles(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)

class Order(models.Model):
    def __str__(self):
        return self.name
    items=models.CharField(max_length=1000)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=200)
    total=models.CharField(max_length=200)





