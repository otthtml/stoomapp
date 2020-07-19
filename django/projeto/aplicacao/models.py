from django.db import models

# Create your models here.
class Endereco(models.Model):
    streetName = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    complement = models.CharField(max_length=50, default=None, blank=True, null=True)
    neighbourhood = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50, default=None, blank=True, null=True)
    longitude = models.CharField(max_length=50, default=None, blank=True, null=True)