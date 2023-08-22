from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Property(models.Model):
    location = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'properties'

class Room(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    charge = models.FloatField()



class Complaint(models.Model):
    tenant = 'tenant'
    room = 'room'
    property = 'property'
    others = 'others'
    options = [
            ('tenant', 'tenant'),
            ('room', 'room'),
            ('property','property'),
            ('others', 'others'),
        ]

    kind = models.CharField(max_length=200, choices=options)
    summary = models.CharField(max_length=200)
    #tenant = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
   # others = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
   # reporter = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    

class Contract(models.Model):
   # landlord = models.ForeignKey(User,on_delete=models.CASCADE)
   # tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    contract_document = models.FileField(upload_to='')
    contract_accepted = models.BooleanField(default=False)



class Profile(models.Model):
    landlord = 'landlord'
    tenant = 'tenant'

    user_type_opts = [
            ('landlord', 'Landlord'),
            ('tenant', 'Tenant'),
        ]

    male = 'Male'
    female = 'Female'

    gender_opts = [
            ('male', 'Male'),
            ('female', 'Female'),
        ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, default=landlord, choices=user_type_opts )
    phone_number = models.CharField(max_length=20, db_index=True)
    secondary_phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=False,choices=gender_opts)



    # override save model to prevent integrity errors
    '''
    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = Profile.objects.get(user=self.user)
                self.pk = p.pk
            except Profile.DoesNotExist:
                pass
        super(Profile, self).save(*args, **kwargs)
    '''
