from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    rooms = models.CharField(max_length=200)
    landlord = models.CharField(max_length=200)
 
class Room(models.Model):
     estate = models.CharField(max_length=200)
     tenant = models.CharField(max_length=200)
     status = models.CharField(max_length=200)
    

class Landlord(models.Model):
    info = models.CharField(max_length=200)
    estate = models.CharField(max_length=200)

class Tenant(models.Model):
    info = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

class Contracts(models.Model):
    form = models.CharField(max_length=200)

class Complaint(models.Model):
    kind = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    reporter = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

class Payment(models.Model):
    methods = models.CharField(max_length=200)
    reminder_of_payment = models.CharField(max_length=200)
    
