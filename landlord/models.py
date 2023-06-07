from django.db import models

# Create your models here.

class Property(models.Model):
    location = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)

class Room(models.Model):
    property_ = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(User)
    status = models.CharField(max_length=200)
    charge = models.FloatField()


options = [
    ('ten', 'tenant'),
    ('rm', 'room'),
    ('prop', 'property'),
    ('oth', 'others'), 
]
class Complaint(models.Model):
    kind = models.CharField(max_length=200, choices=options)
    summary = models.CharField(max_length=200)
    tenant = models.ForeignKey(User)
    room = models.ForeignKey(Room)
    property = models.ForeignKey(Property)
    others = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    reporter = models.ForeignKeyField(User,)
    status = models.CharField(max_length=200)


class Contract(models.Model):
    landlord = models.ForeignKey(User)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room)
    contract_document = models.FileField(upload_to='')
    contract_accepted = models.BooleanField(default= false)


    
