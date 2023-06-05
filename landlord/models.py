from django.db import models

# Create your models here.

class Property(models.Model):
    location = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)

class Room(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(User)
    status = models.CharField(max_length=200)
    charge = models.FloatField()

class Complaint(models.Model):
    kind = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    reporter = models.ForeignKeyField(User,)
    status = models.CharField(max_length=200)


    
